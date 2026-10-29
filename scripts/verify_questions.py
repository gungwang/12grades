#!/usr/bin/env python3
"""Automatically verify question-bank answers using only the standard library.

Usage:
  python3 scripts/verify_questions.py                       # Verify data/questions.json and write data/verification_report.json
  python3 scripts/verify_questions.py --file data/_qbatches/01.json   # Verify only one batch file (including format checks); do not write a report
  python3 scripts/verify_questions.py --report out.json     # Set the report path

The question's verify field is a Python expression string evaluated in a restricted environment (AST allowlist:
arithmetic, **, //, %, comparisons, comprehensions, tuples/lists, and indexing; no attribute access, imports, or assignments).
Available names:
  Fraction sqrt pi e sin cos tan asin acos atan atan2 radians degrees log log10 log2 exp
  factorial comb perm gcd lcm abs round sum min max len sorted range floor ceil isqrt int float
  mean median pvariance variance mode
  solve2(a1,b1,c1,a2,b2,c2) -> (x, y)    Solve a1x+b1y=c1 and a2x+b2y=c2 (exact Fractions)
  roots2(a,b,c) -> sorted list of real roots; returns Fractions when the discriminant is a rational square, otherwise floats

Comparison rules:
  numeric: Compare the expression result (a number, or a list/tuple for multiple answers) with answer. Compare
           int/Fraction values exactly; use a 1e-9 tolerance for floats (the larger of relative and absolute tolerance).
           When answer has multiple values, unordered determines whether order matters.
  choice: Compare the expression result with the correct option's text. If the option text parses as a number,
          compare numerically (using the same rules); otherwise, require str(result) to match the option text exactly.
          Also check that no other option has the same numeric value (to prevent multiple correct answers).
Questions without verify are counted as unverifiable and covered by the independent second pass.
"""
import argparse
import ast
import json
import math
import os
import re
import signal
import statistics
import sys
from collections import Counter
from fractions import Fraction

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import validate as V  # noqa: E402

QUESTIONS_PATH = os.path.join(ROOT, "data", "questions.json")
REPORT_PATH = os.path.join(ROOT, "data", "verification_report.json")
SECOND_PASS_LOG = os.path.join(ROOT, "data", "second_pass_log.json")
TOL = 1e-9


# ------------------------------------------------------------ Restricted evaluation

def solve2(a1, b1, c1, a2, b2, c2):
    a1, b1, c1, a2, b2, c2 = [Fraction(v) for v in (a1, b1, c1, a2, b2, c2)]
    det = a1 * b2 - a2 * b1
    if det == 0:
        raise ValueError("The system has no unique solution")
    return ((c1 * b2 - c2 * b1) / det, (a1 * c2 - a2 * c1) / det)


def _rat_sqrt(fr):
    if fr < 0:
        return None
    n, d = fr.numerator, fr.denominator
    rn, rd = math.isqrt(n), math.isqrt(d)
    return Fraction(rn, rd) if rn * rn == n and rd * rd == d else None


def roots2(a, b, c):
    a, b, c = Fraction(a), Fraction(b), Fraction(c)
    if a == 0:
        raise ValueError("a cannot be zero")
    disc = b * b - 4 * a * c
    if disc < 0:
        return []
    r = _rat_sqrt(disc)
    if r is not None:
        xs = sorted({(-b - r) / (2 * a), (-b + r) / (2 * a)})
        return xs
    s = math.sqrt(float(disc))
    return sorted([(-float(b) - s) / (2 * float(a)), (-float(b) + s) / (2 * float(a))])


def _mode(xs):
    return statistics.mode(xs)


NAMES = {
    "Fraction": Fraction, "sqrt": math.sqrt, "pi": math.pi, "e": math.e,
    "sin": math.sin, "cos": math.cos, "tan": math.tan, "asin": math.asin, "acos": math.acos,
    "atan": math.atan, "atan2": math.atan2, "radians": math.radians, "degrees": math.degrees,
    "log": math.log, "log10": math.log10, "log2": math.log2, "exp": math.exp,
    "factorial": math.factorial, "comb": math.comb, "perm": math.perm, "gcd": math.gcd, "lcm": math.lcm,
    "abs": abs, "round": round, "sum": sum, "min": min, "max": max, "len": len, "sorted": sorted,
    "range": range, "floor": math.floor, "ceil": math.ceil, "isqrt": math.isqrt, "int": int, "float": float,
    "mean": statistics.mean, "median": statistics.median, "pvariance": statistics.pvariance,
    "variance": statistics.variance, "mode": _mode, "solve2": solve2, "roots2": roots2,
}

ALLOWED_NODES = (
    ast.Expression, ast.BinOp, ast.UnaryOp, ast.BoolOp, ast.Compare, ast.IfExp, ast.Call, ast.Name,
    ast.Load, ast.Store, ast.Constant, ast.Tuple, ast.List, ast.Subscript, ast.Slice,
    ast.ListComp, ast.GeneratorExp, ast.comprehension,
    ast.Add, ast.Sub, ast.Mult, ast.Div, ast.FloorDiv, ast.Mod, ast.Pow, ast.USub, ast.UAdd,
    ast.And, ast.Or, ast.Not, ast.Eq, ast.NotEq, ast.Lt, ast.LtE, ast.Gt, ast.GtE,
)


class UnsafeExpression(Exception):
    pass


def _check_ast(tree):
    bound = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.comprehension):
            for n in ast.walk(node.target):
                if isinstance(n, ast.Name):
                    bound.add(n.id)
    for node in ast.walk(tree):
        if not isinstance(node, ALLOWED_NODES):
            raise UnsafeExpression("Syntax not allowed: %s" % type(node).__name__)
        if isinstance(node, ast.Name) and node.id not in NAMES and node.id not in bound:
            raise UnsafeExpression("Name not allowed: %s" % node.id)
        if isinstance(node, ast.Call) and not isinstance(node.func, ast.Name):
            raise UnsafeExpression("Only allowlisted functions may be called directly")
        if isinstance(node, ast.Call) and node.keywords:
            raise UnsafeExpression("Keyword arguments are not allowed")
        if isinstance(node, ast.Constant) and not isinstance(node.value, (int, float, str, bool, type(None))):
            raise UnsafeExpression("Constant not allowed")
        if isinstance(node, ast.Constant) and isinstance(node.value, int) and abs(node.value) > 10 ** 12:
            raise UnsafeExpression("Integer constant is too large")
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Pow):
            r = node.right
            if isinstance(r, ast.Constant) and isinstance(r.value, (int, float)) and abs(r.value) > 400:
                raise UnsafeExpression("Exponent is too large")


class _Timeout(Exception):
    pass


def _alarm(signum, frame):
    raise _Timeout()


def safe_eval(expr):
    if not isinstance(expr, str) or len(expr) > 600:
        raise UnsafeExpression("Expression is empty or too long")
    tree = ast.parse(expr.strip(), mode="eval")
    _check_ast(tree)
    code = compile(tree, "<verify>", "eval")
    old = None
    try:
        old = signal.signal(signal.SIGALRM, _alarm)
        signal.alarm(2)
    except (ValueError, AttributeError):
        old = None
    try:
        env = {"__builtins__": {}}
        env.update(NAMES)  # Names must be in globals because comprehensions cannot see locals.
        return eval(code, env)
    finally:
        if old is not None:
            signal.alarm(0)
            signal.signal(signal.SIGALRM, old)


# ------------------------------------------------------------ Comparison

def num_equal(expected, got):
    """expected comes from answer (Fraction); got comes from the expression (int/Fraction/float/bool)."""
    if isinstance(got, bool):
        return False
    if isinstance(got, (int, Fraction)):
        return Fraction(got) == expected
    if isinstance(got, float):
        if math.isnan(got) or math.isinf(got):
            return False
        return abs(float(expected) - got) <= TOL * max(1.0, abs(got))
    return False


def flatten_result(res):
    if isinstance(res, (list, tuple)):
        return list(res)
    return [res]


def compare_numeric(q, res):
    exp = V.parse_numeric_answer(q["answer"])
    got = flatten_result(res)
    if exp is None:
        return False, "Could not parse answer"
    if len(exp) != len(got):
        return False, "Different number of values: answer has %d, verify has %d" % (len(exp), len(got))
    if q.get("unordered") is True:
        left = list(got)
        for e in exp:
            hit = next((i for i, g in enumerate(left) if num_equal(e, g)), None)
            if hit is None:
                return False, "Value %s from answer was not found in the verify result" % e
            left.pop(hit)
        return True, ""
    for e, g in zip(exp, got):
        if not num_equal(e, g):
            return False, "Ordered comparison: answer %s != verify %s" % (e, g)
    return True, ""


def choice_text_value(text):
    t = text.strip().replace(" ", "").replace("−", "-")
    return V.parse_numeric_answer(t) if V.NUM_RE.match(t) else None


# Physics options often use "number + unit" (for example, 20 m/s or 2.7 g/cm³). Parse numeric values only for cnp_ questions,
# and accept only the units listed here. Options are duplicates only when both the number and unit match.
PHY_UNITS = ("J/(kg·℃)", "kg/m³", "g/cm³", "kW·h", "m/s", "km/h", "N/kg", "J/kg", "kPa", "kW", "kJ", "kV", "kΩ",
             "mV", "mA", "mL", "mg", "mm", "cm³", "dm³", "m³", "cm²", "m²", "cm", "km", "μm", "nm", "min", "Hz", "dB",
             # Keep legacy Chinese suffixes alongside translated English unit labels.
             "Pa", "kg", "℃", "Ω", "%", "m", "g", "t", "L", "s", "h", "N", "J", "W", "V", "A", "个", "倍", "times",
             # High school physics
             "m/s²", "cm/s", "rad/s", "r/min", "r/s", "rad", "°", "N·s", "kg·m/s", "N·m", "N/m", "V/m", "N/C", "C", "μC", "nC",
             "pF", "μF", "mF", "F", "mT", "μT", "T", "Wb", "Ω·m", "mH", "μH", "H", "MHz", "kHz", "GHz", "eV", "keV", "MeV",
             "K", "mol", "J/K", "ms", "μs", "ns", "MW", "MJ", "mW", "kN", "cm/s²", "atm", "mmHg", "MPa", "J/mol", "m/s³",
             "kg·m²", "W/m²", "天", "年", "圈", "次", "匝", "u", "个/s")
_PHY_RE = re.compile(r"^(-?\d+(?:\.\d+)?)\s*(" + "|".join(re.escape(u) for u in PHY_UNITS) + r")$")


def phy_choice_value(text):
    """Return a (Fraction, unit) pair or None."""
    m = _PHY_RE.match(text.strip())
    if not m:
        return None
    unit = "times" if m.group(2) == "倍" else m.group(2)
    return Fraction(m.group(1)), unit


def compare_phy_choice(q, res):
    texts = {c["key"]: c["text"].strip() for c in q["choices"]}
    right = texts[q["answer"]]
    rv = phy_choice_value(right)
    if rv is None or isinstance(res, (str, bool)) or not isinstance(res, (int, float, Fraction)):
        return None
    if not num_equal(rv[0], res):
        return False, "verify returned %s, but the value of correct option %s is %s" % (res, q["answer"], right)
    dup = [k for k, t in texts.items() if k != q["answer"] and phy_choice_value(t) is not None
           and phy_choice_value(t)[1] == rv[1] and num_equal(phy_choice_value(t)[0], res)]
    if dup:
        return False, "Option(s) %s have the same value and unit as the correct option (multiple correct answers)" % ", ".join(dup)
    return True, ""


def compare_choice(q, res):
    if str(q.get("id", "")).startswith("cnp_"):
        out = compare_phy_choice(q, res)
        if out is not None:
            return out
    texts = {c["key"]: c["text"].strip() for c in q["choices"]}
    right = texts[q["answer"]]
    rv = choice_text_value(right)
    if rv is not None and len(rv) == 1 and isinstance(res, (int, float, Fraction)) and not isinstance(res, bool):
        if not num_equal(rv[0], res):
            return False, "verify returned %s, but the value of correct option %s is %s" % (res, q["answer"], rv[0])
        dup = [k for k, t in texts.items() if k != q["answer"] and choice_text_value(t) is not None
               and len(choice_text_value(t)) == 1 and num_equal(choice_text_value(t)[0], res)]
        if dup:
            return False, "Option(s) %s have the same value as the correct option (multiple correct answers)" % ", ".join(dup)
        return True, ""
    if str(res).strip() == right:
        dup = [k for k, t in texts.items() if k != q["answer"] and t == right]
        return (False, "Duplicate option text") if dup else (True, "")
    return False, "verify returned %r, but the text of correct option %s is %r" % (res, q["answer"], right)


# ------------------------------------------------------------ Main flow

def verify_all(questions):
    r = {"auto_verified": [], "mismatch": [], "unverifiable": [], "expression_errors": []}
    for q in questions:
        typ = q.get("type")
        expr = q.get("verify")
        if typ not in ("numeric", "choice") or not expr:
            r["unverifiable"].append(q["id"])
            continue
        try:
            res = safe_eval(expr)
        except Exception as ex:  # noqa: BLE001
            r["expression_errors"].append({"id": q["id"], "verify": expr, "error": "%s: %s" % (type(ex).__name__, ex)})
            r["mismatch"].append({"id": q["id"], "type": typ, "answer": q["answer"], "verify": expr,
                                  "detail": "Could not evaluate verify expression: %s: %s" % (type(ex).__name__, ex)})
            continue
        ok, detail = compare_numeric(q, res) if typ == "numeric" else compare_choice(q, res)
        if ok:
            r["auto_verified"].append(q["id"])
        else:
            r["mismatch"].append({"id": q["id"], "type": typ, "answer": q["answer"], "verify": expr,
                                  "verify_result": repr(res), "detail": detail})
    return r


def load_second_pass_log():
    if not os.path.exists(SECOND_PASS_LOG):
        return None
    with open(SECOND_PASS_LOG, encoding="utf-8") as f:
        return json.load(f)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", help="Verify only this question-bank or batch file")
    ap.add_argument("--report", help="Report output path (default: data/verification_report.json; omitted with --file)")
    args = ap.parse_args()

    path = args.file or QUESTIONS_PATH
    with open(path, encoding="utf-8") as f:
        questions = json.load(f)
    with open(os.path.join(ROOT, "data", "topics.json"), encoding="utf-8") as f:
        topics = {t["id"]: t for t in json.load(f)}

    errs, stats = V.question_errors(questions, topics, require_coverage=not args.file)
    if errs:
        print("Format errors: %d" % len(errs))
        for e in errs[:80]:
            print("  - " + e)
        if len(errs) > 80:
            print("  ... and %d more" % (len(errs) - 80))
    questions_ok = [q for q in questions if isinstance(q, dict) and isinstance(q.get("id"), str)
                    and q.get("type") in V.Q_TYPES]
    # Choice questions with invalid structure (missing choices or an answer key not in the options) are excluded from expression comparison; format errors already report them.
    safe = [q for q in questions_ok if not (q["type"] == "choice" and not (
        isinstance(q.get("choices"), list) and all(isinstance(c, dict) and "key" in c and "text" in c for c in q["choices"])
        and q.get("answer") in [c["key"] for c in q["choices"]]))
        and not (q["type"] == "numeric" and V.parse_numeric_answer(q.get("answer")) is None)]
    res = verify_all(safe)
    bad_ids = {q["id"] for q in questions_ok} - {q["id"] for q in safe}
    for qid in sorted(bad_ids):
        res["unverifiable"].append(qid)

    n_eligible = sum(1 for q in questions_ok if q["type"] in ("numeric", "choice"))
    unver_by_type = Counter(q["type"] for q in questions_ok if q["id"] in set(res["unverifiable"]))
    report = {
        "generated_at": __import__("datetime").datetime.now().isoformat(timespec="seconds"),
        "source": os.path.relpath(path, ROOT),
        "total_questions": len(questions),
        "by_type": dict(Counter(q.get("type") for q in questions)),
        "format_errors": errs,
        "auto_verified": len(res["auto_verified"]),
        "mismatch": len(res["mismatch"]),
        "unverifiable": len(res["unverifiable"]),
        "unverifiable_by_type": dict(unver_by_type),
        "numeric_choice_total": n_eligible,
        "numeric_choice_auto_verified_share": round(len(res["auto_verified"]) / float(n_eligible), 4) if n_eligible else None,
        "mismatches": res["mismatch"],
        "unverifiable_ids": sorted(res["unverifiable"]),
    }
    sp = load_second_pass_log() if not args.file else None
    if sp is not None:
        report["second_pass"] = dict(sp)
        report["second_pass"].setdefault("second_pass_mismatch", [])
    out = args.report or (None if args.file else REPORT_PATH)
    if out:
        with open(out, "w", encoding="utf-8") as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
            f.write("\n")

    print("Questions: %d; numeric + choice: %d" % (len(questions), n_eligible))
    print("Auto-verified %d; mismatches %d; unverifiable %d (%s)" % (
        report["auto_verified"], report["mismatch"], report["unverifiable"],
        ", ".join("%s %d" % kv for kv in sorted(unver_by_type.items())) or "none"))
    for m in res["mismatch"][:60]:
        print("  MISMATCH %s answer=%r verify=%r → %s" % (m["id"], m["answer"], m["verify"], m["detail"]))
    if len(res["mismatch"]) > 60:
        print("  ... and %d more" % (len(res["mismatch"]) - 60))
    if out:
        print("Report: " + os.path.relpath(out, ROOT))
    if res["mismatch"] or errs:
        print("VERIFICATION FAILED")
        return 1
    sp_bad = (report.get("second_pass") or {}).get("second_pass_mismatch")
    if sp_bad:
        print("VERIFICATION FAILED (%d issue(s) remain after the second review)" % len(sp_bad))
        return 1
    print("VERIFICATION PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
