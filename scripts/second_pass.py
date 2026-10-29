#!/usr/bin/env python3
"""Helper for the independent second review of the question bank (standard library only).

Workflow:
  1) python3 scripts/second_pass.py prepare [--chunk 90] [--prefix b]
       --prefix b: second pass containing only questions without a verify check and all advanced questions; writes blind_b_NN.json (the solver should include derivations).
       Run compare --prefix b to read ans_b_NN.json.
       Removes answer, explanation, verify, and accept from numeric / choice / short questions, leaving only prompts and choices,
       then writes chunks to data/_second_pass/blind_NN.json for an independent solver who does not see the answers.
  2) The solver writes answers to data/_second_pass/ans_NN.json: {"question_id": "answer"}.
       numeric: a number (integer/decimal/fraction a/b/negative number); separate multiple answers with the Chinese comma token `，`.
       choice: an option letter; short: answer text.
  3) python3 scripts/second_pass.py compare
       Compares independent answers with the answers in questions.json and writes mismatches to data/_second_pass/mismatches.json
       (including both answers and the prompt for each item to review).
After review, record the results in data/second_pass_log.json; verify_questions.py will merge them into verification_report.json.
"""
# The Chinese comma token is retained because the numeric-answer parser accepts it as a separator.
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import validate as V  # noqa: E402
from engine_norm import norm_text  # noqa: E402  (see the sibling module below)

QPATH = os.path.join(ROOT, "data", "questions.json")
DIR = os.path.join(ROOT, "data", "_second_pass")


def load_questions():
    with open(QPATH, encoding="utf-8") as f:
        return json.load(f)


def is_risky(q):
    """Select questions without a verify-expression check and all advanced questions for the second, more careful blind solve."""
    return q["type"] in ("numeric", "choice", "short") and (not q.get("verify") or q["difficulty"] == "advanced")


def prepare(chunk, prefix=""):
    os.makedirs(DIR, exist_ok=True)
    qs = [q for q in load_questions() if q["type"] in ("numeric", "choice", "short") and (not prefix or is_risky(q))]
    blind = []
    for q in qs:
        b = {"id": q["id"], "type": q["type"], "prompt": q["prompt"]}
        if q["type"] == "choice":
            b["choices"] = {c["key"]: c["text"] for c in q["choices"]}
        if q["type"] == "numeric" and q.get("unordered"):
            b["note"] = "Multiple answers; order does not matter."
        blind.append(b)
    n = 0
    for i in range(0, len(blind), chunk):
        n += 1
        path = os.path.join(DIR, "blind_%s%02d.json" % (prefix and prefix + "_", n))
        with open(path, "w", encoding="utf-8") as f:
            json.dump(blind[i:i + chunk], f, ensure_ascii=False, indent=1)
    print("Wrote %d chunks containing %d questions → data/_second_pass/blind_NN.json" % (n, len(blind)))


def same_numeric(q, mine):
    exp = V.parse_numeric_answer(q["answer"])
    got = V.parse_numeric_answer(str(mine))
    if exp is None or got is None or len(exp) != len(got):
        return False
    if q.get("unordered"):
        return sorted(exp) == sorted(got)
    return exp == got


def compare(prefix=""):
    qs = {q["id"]: q for q in load_questions()}
    if prefix:
        qs = {k: v for k, v in qs.items() if is_risky(v)}
    answers = {}
    pat = r"^ans_%s\d+\.json$" % (prefix and prefix + "_")
    for name in sorted(os.listdir(DIR)):
        if re.match(pat, name):
            with open(os.path.join(DIR, name), encoding="utf-8") as f:
                answers.update(json.load(f))
    mism, missing = [], []
    checked = 0
    for qid, q in qs.items():
        if q["type"] not in ("numeric", "choice", "short"):
            continue
        if qid not in answers:
            missing.append(qid)
            continue
        checked += 1
        mine = str(answers[qid]).strip()
        if q["type"] == "choice":
            ok = mine.strip().upper()[:1] == q["answer"]
        elif q["type"] == "numeric":
            ok = same_numeric(q, mine)
        else:
            refs = [q["answer"]] + list(q.get("accept", []))
            ok = norm_text(mine) in {norm_text(r) for r in refs}
        if not ok:
            m = {"id": qid, "type": q["type"], "prompt": q["prompt"], "answer": q["answer"], "independent": mine}
            if q["type"] == "choice":
                m["choices"] = {c["key"]: c["text"] for c in q["choices"]}
            mism.append(m)
    out = os.path.join(DIR, "mismatches%s.json" % (prefix and "_" + prefix))
    with open(out, "w", encoding="utf-8") as f:
        json.dump(mism, f, ensure_ascii=False, indent=1)
    by = {}
    for m in mism:
        by[m["type"]] = by.get(m["type"], 0) + 1
    print("Independent answers: %d; missing: %d; mismatches: %d (%s) → %s" % (
        checked, len(missing), len(mism), ", ".join("%s %d" % kv for kv in sorted(by.items())) or "none",
        os.path.relpath(out, ROOT)))
    if missing:
        print("Missing: " + ", ".join(missing[:30]) + (" ..." if len(missing) > 30 else ""))
    return 0 if not missing else 2


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "prepare":
        size = int(sys.argv[sys.argv.index("--chunk") + 1]) if "--chunk" in sys.argv else 90
        prepare(size, sys.argv[sys.argv.index("--prefix") + 1] if "--prefix" in sys.argv else "")
    elif cmd == "compare":
        sys.exit(compare(sys.argv[sys.argv.index("--prefix") + 1] if "--prefix" in sys.argv else ""))
    else:
        print(__doc__)
        sys.exit(1)
