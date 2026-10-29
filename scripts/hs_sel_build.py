#!/usr/bin/env python3
"""Compile the high-school selective-compulsory drafts into files such as data/topics.json.

Run only once, while cnm_h144 is absent. A second run is rejected to prevent duplicate additions.
Transitive reduction applies only to edges on newly added topics; existing primary, junior-high, and compulsory edges are preserved, as are existing node IDs and names.

Usage: python3 scripts/hs_sel_build.py
"""
from __future__ import annotations

import json
import os
import re
import sys
from collections import defaultdict
from fractions import Fraction

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from hs_sel_common import EDGES, QUESTIONS, STANDARDS, TOPICS  # noqa: E402
import hs_sel_standards  # noqa: E402,F401
import hs_sel_b1  # noqa: E402,F401
import hs_sel_b2  # noqa: E402,F401
import hs_sel_b3  # noqa: E402,F401
import hs_sel_edges  # noqa: E402,F401
from verify_questions import safe_eval  # noqa: E402

CJK_RE = re.compile(r"[\u4e00-\u9fff]")
# These Han strings and the CJK codepoint check validate unchanged Chinese drafts and edge reasons in other hs_sel modules.
BAD_START = ("同一", "上题", "该函数", "这个函数", "同上")
BAD_ANY = ("本知识点", "课标", "是否要求")
FIRST_ID = 144

# These exact Chinese names are comparison tokens for existing topic records; keep them unchanged to preserve the ID/name checks.
KNOWN = {
    "cnm_056": "角的概念与表示",
    "cnm_065": "垂线段最短与点到直线的距离",
    "cnm_067": "平行线与平行公理",
    "cnm_071": "定义、命题与定理",
    "cnm_082": "平面直角坐标系与点的坐标",
    "cnm_174": "勾股定理",
    "cnm_201": "一次函数的概念",
    "cnm_211": "平均数",
    "cnm_215": "极差、方差与标准差",
    "cnm_219": "一元二次方程的概念",
    "cnm_229": "二次函数的概念",
    "cnm_250": "圆的有关概念",
    "cnm_286": "用列举法求概率",
    "cnm_p095": "简单的搭配",
    "cnm_h027": "函数的概念",
    "cnm_h028": "函数的定义域",
    "cnm_h032": "函数的单调性",
    "cnm_h034": "函数的最大（小）值",
    "cnm_h037": "幂函数",
    "cnm_h041": "指数函数的概念",
    "cnm_h042": "指数函数的性质",
    "cnm_h079": "平面向量的概念",
    "cnm_h081": "向量加法",
    "cnm_h084": "向量共线定理",
    "cnm_h085": "平面向量基本定理",
    "cnm_h086": "向量的坐标表示",
    "cnm_h088": "向量数量积",
    "cnm_h090": "向量的模与夹角",
    "cnm_h113": "平面的基本事实",
    "cnm_h114": "空间直线的位置关系",
    "cnm_h116": "直线与平面平行的判定",
    "cnm_h118": "平面与平面平行的判定",
    "cnm_h120": "直线与平面垂直的判定",
    "cnm_h122": "平面与平面垂直",
    "cnm_h127": "频率分布直方图",
    "cnm_h130": "用样本估计总体的中心",
    "cnm_h134": "样本点与样本空间",
    "cnm_h135": "随机事件",
    "cnm_h137": "古典概型",
    "cnm_h140": "事件的相互独立",
    "cnm_h141": "独立事件的概率计算",
    "cnm_h142": "频率与概率",
}

# These Chinese volume labels and chapter labels are structural tokens consumed by the chapter parser below.
VOLUMES = {1: "选必一", 2: "选必二", 3: "选必三"}
GRADES = {1: 12, 2: 13, 3: 14}


def load(name):
    with open(os.path.join(ROOT, "data", name), encoding="utf-8") as f:
        return json.load(f)


def dump(name, data):
    path = os.path.join(ROOT, "data", name)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def fmt_one(v):
    if isinstance(v, bool) or v is None:
        raise TypeError(repr(v))
    if isinstance(v, str):
        raise TypeError("A numeric question's verify expression must not return a string: %r" % v)
    if isinstance(v, float):
        fr = Fraction(v).limit_denominator(64)
        if abs(float(fr) - v) > 1e-9:
            raise ValueError("The result is not a simple fraction: %r" % (v,))
        v = fr
    if isinstance(v, int):
        v = Fraction(v)
    if not isinstance(v, Fraction):
        raise TypeError(type(v).__name__)
    if v.denominator == 1:
        return str(int(v))
    return "%d/%d" % (v.numerator, v.denominator)


def fmt_result(v):
    if isinstance(v, (list, tuple)):
        if len(v) < 2:
            raise ValueError("Multiple answers require at least 2 values")
        # Keep the Chinese comma as the established separator in serialized multiple-answer values.
        return "，".join(fmt_one(x) for x in v)
    return fmt_one(v)


def check_wording(qid, text):
    body = text.strip()
    for prefix in BAD_START:
        if body.startswith(prefix):
            raise ValueError("%s prompt starts with '%s'" % (qid, prefix))
    for word in BAD_ANY:
        if word in text:
            raise ValueError("%s contains '%s'" % (qid, word))


def build_question(tid, index, spec, slot):
    kind = spec[0]
    diff = "basic" if index <= 2 else "standard"
    qid = "%s_q%d" % (tid, index)
    if kind in ("n", "nu"):
        prompt, verify, expl = spec[1], spec[2], spec[3]
        check_wording(qid, prompt)
        check_wording(qid, expl)
        res = safe_eval(verify)
        answer = fmt_result(res)
        multi = isinstance(res, (list, tuple))
        item = {
            "id": qid,
            "topicId": tid,
            "difficulty": diff,
            "type": "numeric",
            "prompt": prompt,
            "answer": answer,
            "explanation": expl,
            "verify": verify,
        }
        if kind == "nu":
            if not multi:
                raise ValueError("%s is marked unordered, but verify does not return multiple answers" % qid)
            item["unordered"] = True
        return item, answer
    if kind == "c":
        prompt, correct, wrongs, expl = spec[1], spec[2], spec[3], spec[4]
        check_wording(qid, prompt)
        check_wording(qid, expl)
        check_wording(qid, correct)
        for wrong in wrongs:
            check_wording(qid, wrong)
        texts = list(wrongs)
        if correct in texts or len(set(texts)) != len(texts):
            raise ValueError("%s has duplicate choices or includes the correct answer among the distractors" % qid)
        if not (2 <= len(wrongs) <= 3):
            raise ValueError("%s must have 2–3 distractors" % qid)
        texts.insert(slot % (len(wrongs) + 1), correct)
        if len(set(t.strip() for t in texts)) != len(texts):
            raise ValueError("%s has duplicate choice text" % qid)
        keys = list("ABCD")[:len(texts)]
        pos = texts.index(correct)
        item = {
            "id": qid,
            "topicId": tid,
            "difficulty": diff,
            "type": "choice",
            "prompt": prompt,
            "choices": [{"key": keys[i], "text": texts[i]} for i in range(len(texts))],
            "answer": keys[pos],
            "explanation": expl,
            "verify": json.dumps(correct, ensure_ascii=False),
        }
        return item, correct
    raise ValueError("Unknown question type: %s" % kind)


def reaches(adj, src, dst, hard_only):
    seen = {src}
    stack = [src]
    while stack:
        node = stack.pop()
        for pre, strength in adj.get(node, []):
            if hard_only and strength != "hard":
                continue
            if pre == dst:
                return True
            if pre not in seen:
                seen.add(pre)
                stack.append(pre)
    return False


def reduce_new(edges, new_ids):
    """Remove redundant edges only for newly added topics; preserve all existing edges."""
    adj = defaultdict(list)
    for e in edges:
        adj[e["topicId"]].append([e["prerequisiteId"], e["strength"]])
    kept = []
    dropped = 0
    for e in edges:
        if e["topicId"] not in new_ids:
            kept.append(e)
            continue
        lst = adj[e["topicId"]]
        idx = next(i for i, (p, s) in enumerate(lst)
                   if p == e["prerequisiteId"] and s == e["strength"])
        lst.pop(idx)
        if reaches(adj, e["topicId"], e["prerequisiteId"], e["strength"] == "hard"):
            dropped += 1
            continue
        lst.append([e["prerequisiteId"], e["strength"]])
        kept.append(e)
    return kept, dropped


def chapter_of(spec):
    vol = VOLUMES[spec["book"]]
    # These exact chapter labels are used to construct the parser's structural chapter string.
    if spec["chapter"] in ("数学建模", "数学探究"):
        return "%s %s %s" % (vol, spec["chapter"], spec["section"])
    return "%s %s %s" % (vol, spec["chapter"], spec["section"])


def main():
    topics = load("topics.json")
    if any(t.get("id") == "cnm_h144" for t in topics):
        print("cnm_h144 already exists. hs_sel_build.py cannot be run twice.", file=sys.stderr)
        return 1
    if not any(t.get("id") == "cnm_h143" for t in topics):
        print("cnm_h143 is missing. Compile the high-school compulsory material first.", file=sys.stderr)
        return 1
    frozen = [(t.get("id"), t.get("name")) for t in topics]
    by_id = {t["id"]: t for t in topics}
    for tid, name in KNOWN.items():
        hit = by_id.get(tid)
        if hit is None or hit["name"] != name:
            print("Prerequisite ID mismatch for %s: expected '%s', got %s" % (
                tid, name, None if hit is None else hit["name"]), file=sys.stderr)
            return 1

    if len(TOPICS) < 110 or len(TOPICS) > 160:
        print("Topic count %d is outside the range 110–160" % len(TOPICS), file=sys.stderr)
        return 1
    missing_q = [t["key"] for t in TOPICS if t["key"] not in QUESTIONS]
    if missing_q:
        print("Missing questions: %s" % ", ".join(missing_q), file=sys.stderr)
        return 1
    extra_q = sorted(set(QUESTIONS) - {t["key"] for t in TOPICS})
    if extra_q:
        print("Unexpected question keys: %s" % ", ".join(extra_q), file=sys.stderr)
        return 1

    std_codes = [s["code"] for s in STANDARDS]
    if len(std_codes) != len(set(std_codes)):
        print("Duplicate curriculum-standard code.", file=sys.stderr)
        return 1
    index = {t["key"]: i for i, t in enumerate(TOPICS)}
    grade_of = {t["key"]: GRADES[t["book"]] for t in TOPICS}

    new_topics = []
    new_questions = []
    id_of = {}
    for i, spec in enumerate(TOPICS):
        tid = "cnm_h%03d" % (FIRST_ID + i)
        id_of[spec["key"]] = tid
        if spec["std"] not in std_codes:
            print("Curriculum standard %s does not exist for %s" % (spec["std"], spec["key"]), file=sys.stderr)
            return 1
        if spec["confidence"] not in ("exact", "inferred"):
            print("Invalid confidence value for %s" % spec["key"], file=sys.stderr)
            return 1
        if spec["confidence"] == "inferred" and not spec.get("note"):
            print("%s is inferred but has no note" % spec["key"], file=sys.stderr)
            return 1
        if spec["book"] not in GRADES:
            print("Invalid book number for %s" % spec["key"], file=sys.stderr)
            return 1
        try:
            built = []
            diag_answer = None
            for n, item in enumerate(QUESTIONS[spec["key"]], start=1):
                q, shown = build_question(tid, n, item, slot=i + n)
                if not q["prompt"].strip() or not q["explanation"].strip():
                    raise ValueError("The prompt or explanation is empty")
                built.append(q)
                if n == 1:
                    diag_answer = shown
        except Exception as exc:  # noqa: BLE001
            print("Failed to build questions for %s (%s): %s" % (tid, spec["name"], exc), file=sys.stderr)
            return 1
        std_ref = {"id": "cms-2017:H.%s" % spec["std"], "confidence": spec["confidence"]}
        if spec.get("note"):
            std_ref["note"] = spec["note"]
        new_topics.append({
            "id": tid,
            "name": spec["name"],
            "domain": spec["domain"],
            "grade": GRADES[spec["book"]],
            # "上" is the schema's fixed semester token; preserve it unchanged.
            "semester": "上",
            "chapter": chapter_of(spec),
            "type": spec["type"],
            "description": spec["description"],
            "mastery_criteria": spec["mastery_criteria"],
            "diagnostic_question": {"question": built[0]["prompt"], "answer": str(diag_answer)},
            "external": False,
            "standards": [std_ref],
        })
        new_questions.extend(built)

    raw_edges = []
    seen = set()
    for src, dst, strength, reason in EDGES:
        if src not in id_of:
            print("Edge source is not a selective-compulsory topic: %s" % src, file=sys.stderr)
            return 1
        if len(CJK_RE.findall(reason)) < 9:
            print("Prerequisite reason is too short: %s → %s: %s" % (src, dst, reason), file=sys.stderr)
            return 1
        if dst in id_of:
            if index[dst] >= index[src]:
                print("Prerequisite does not precede its dependent topic: %s depends on %s" % (src, dst), file=sys.stderr)
                return 1
            if grade_of[dst] > grade_of[src]:
                print("Prerequisite is in a higher grade: %s depends on %s" % (src, dst), file=sys.stderr)
                return 1
            pid = id_of[dst]
        elif dst in KNOWN:
            pid = dst
        else:
            print("Prerequisite is neither a selective-compulsory key nor a registered existing ID: %s" % dst, file=sys.stderr)
            return 1
        key = (id_of[src], pid)
        if key in seen:
            print("Duplicate edge %s → %s" % key, file=sys.stderr)
            return 1
        seen.add(key)
        raw_edges.append({
            "topicId": id_of[src],
            "prerequisiteId": pid,
            "strength": strength,
            "reason": reason,
        })

    new_ids = {t["id"] for t in new_topics}
    deps = load("dependencies.json")
    merged, dropped = reduce_new(deps + raw_edges, new_ids)
    new_only = [e for e in merged if e["topicId"] in new_ids]
    internal = [e for e in new_only if e["prerequisiteId"] in new_ids]
    cross = [e for e in new_only if e["prerequisiteId"] not in new_ids]
    to_compulsory = [e for e in cross if str(e["prerequisiteId"]).startswith("cnm_h")]
    to_primary = [e for e in cross if str(e["prerequisiteId"]).startswith("cnm_p")]
    to_junior = [e for e in cross if e not in to_compulsory and e not in to_primary]
    print("Selective-compulsory topics: %d (Volume 1: %d, Volume 2: %d, Volume 3: %d)" % (
        len(new_topics),
        sum(1 for t in new_topics if t["grade"] == 12),
        sum(1 for t in new_topics if t["grade"] == 13),
        sum(1 for t in new_topics if t["grade"] == 14)))
    print("New edges: %d written, %d removed by reduction, %d retained" % (len(raw_edges), dropped, len(new_only)))
    print("Selective-compulsory internal: %d; cross-module: %d (compulsory: %d, junior high: %d, primary: %d)" % (
        len(internal), len(cross), len(to_compulsory), len(to_junior), len(to_primary)))
    print("Questions: %d" % len(new_questions))
    print("Curriculum standards: %d" % len(STANDARDS))

    from verify_questions import verify_all
    checked = verify_all(new_questions)
    if checked["mismatch"] or checked["unverifiable"]:
        for m in checked["mismatch"][:40]:
            print("Question verification failed for %s: %s" % (m["id"], m.get("detail")), file=sys.stderr)
        print("Question verification did not pass: %d mismatches, %d unverifiable" % (
            len(checked["mismatch"]), len(checked["unverifiable"])), file=sys.stderr)
        return 1
    covered = {e["topicId"] for e in new_only}
    naked = [t["id"] + " " + t["name"] for t in new_topics if t["id"] not in covered]
    if naked:
        print("These new topics have no prerequisites: " + ", ".join(naked), file=sys.stderr)
        return 1
    # Keep these Chinese labels and regex groups because they define the chapter-string grammar.
    ch_model = re.compile(r"^(选必[一二三]) (数学建模|数学探究) (\S+)$")
    ch_num = re.compile(r"^(\S+) (第\S+章) (\S+?)(?: (\S+))?$")
    for t in new_topics:
        if not (ch_model.match(t["chapter"]) or ch_num.match(t["chapter"])):
            print("Could not parse chapter name for %s: %s" % (t["id"], t["chapter"]), file=sys.stderr)
            return 1

    std = load("cn-curriculum-standards.json")
    note = std["source"].get("note") or ""
    extra = (" Selective-compulsory entries continue the same numbering scheme (Functions from FUN.18, "
             "Geometry and Algebra from GA.13, Probability and Statistics from PS.09, and Modeling and "
             "Inquiry from MI.03); they remain public paraphrases, not verbatim, and page_or_ref is pending verification.")
    # This exact phrase is an idempotency marker in pre-existing Chinese source metadata.
    if "选择性必修条目" not in note:
        std["source"]["note"] = note + extra
    std["source"]["stage"] = "Compulsory education stages 1–4 (Grades 1–9); general high-school compulsory and selective-compulsory courses"
    retrieved = std["source"].get("retrieved") or ""
    # Preserve the Chinese metadata marker used to detect an existing retrieval annotation.
    if "高中选择性必修" not in retrieved:
        std["source"]["retrieved"] = retrieved + "; 2026-10-20 (high-school selective-compulsory curriculum)"
    hs = std["source"].setdefault("high_school", {})
    old_hs_note = hs.get("note") or ""
    # Preserve the Chinese substring check because it is a marker in existing standards metadata.
    if "选择性必修" not in old_hs_note:
        hs["note"] = old_hs_note + " Selective-compulsory topics have likewise not been checked page by page and are marked pending verification."
    existing_ids = {it["id"] for it in std["items"]}
    for s in STANDARDS:
        sid = "cms-2017:H.%s" % s["code"]
        if sid in existing_ids:
            print("Curriculum-standard ID already exists: %s" % sid, file=sys.stderr)
            return 1
        std["items"].append({
            "id": sid,
            "domain": s["domain"],
            "theme": s["theme"],
            "section": s["section"],
            "clause": s["clause"],
            "text": s["text"],
            "page_or_ref": "Pending verification",
            "verbatim": False,
            "text_status": "Public paraphrase, not checked page by page against the Ministry of Education PDF; pending verification",
        })

    topics.extend(new_topics)
    if [(t.get("id"), t.get("name")) for t in topics[:len(frozen)]] != frozen:
        print("An existing topic ID or name was changed.", file=sys.stderr)
        return 1
    questions = load("questions.json")
    questions.extend(new_questions)
    dump("topics.json", topics)
    dump("dependencies.json", merged)
    dump("questions.json", questions)
    dump("cn-curriculum-standards.json", std)
    batch = os.path.join(ROOT, "data", "_qbatches", "high_sel.json")
    with open(batch, "w", encoding="utf-8") as f:
        json.dump(new_questions, f, ensure_ascii=False, indent=2)
        f.write("\n")

    log_path = os.path.join(ROOT, "data", "second_pass_log.json")
    with open(log_path, encoding="utf-8") as f:
        log = json.load(f)
    pass_name = "E: High-school selective-compulsory questions generate verify expressions, then verify_questions.py checks the expressions and answers"
    passes = log.setdefault("passes", [])
    if not any(p.get("name") == pass_name for p in passes):
        passes.append({
            "name": pass_name,
            "solver": "scripts/hs_sel_build.py + scripts/verify_questions.py",
            "questions": len(new_questions),
            "note": "The answer is written by evaluating the same verify expression and then compared by the checker, so a mismatch indicates a formatting issue rather than a separate solution. No blind-solving pass like the junior-high A/B rounds was done. For concept questions, the choice text matches the string returned by verify.",
            "disagreements": 0,
        })
    log["high_school_selective_checked_by_verify"] = len(new_questions)
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(log, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("Data written to data/. Run validate.py and verify_questions.py next.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
