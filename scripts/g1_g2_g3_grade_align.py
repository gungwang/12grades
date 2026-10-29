#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Align the difficulty of the Grade 1–3 question bank.

Each topic has 2 basic, 1 standard, and 1 challenge question.
Lower grades may use simple calculations, but each question must assess its topic;
unrelated arithmetic must not be attached to statistics, geometry, or concepts.
Writes data/questions.json, topics.json's diagnostic_question, and
data/_qbatches/primary_g1.json, primary_g2.json, and primary_g3.json.
Does not modify Grades 4–6.
"""
import os
import sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import validate as V  # noqa: E402
import verify_questions as VQ  # noqa: E402
from g123_bank_g1 import BANK as BANK_G1  # noqa: E402
from g123_bank_g2 import BANK as BANK_G2  # noqa: E402
from g123_bank_g3 import BANK as BANK_G3  # noqa: E402


def n(diff, prompt, answer, expl, verify):
    return {
        "difficulty": diff, "type": "numeric", "prompt": prompt,
        "answer": str(answer), "explanation": expl, "verify": verify,
    }


def c(diff, prompt, options, correct, expl, verify=None):
    keys = "ABCD"
    q = {
        "difficulty": diff, "type": "choice", "prompt": prompt,
        "choices": [{"key": keys[i], "text": t} for i, t in enumerate(options)],
        "answer": correct, "explanation": expl,
    }
    if verify is None:
        verify = repr(options["ABCD".index(correct)])
    q["verify"] = verify
    return q


def convert(row):
    kind = row[0]
    adopt = None
    if kind == "n":
        diff, prompt, answer, expl, verify = row[1:6]
        q = n(diff, prompt, answer, expl, verify)
        if len(row) > 6:
            adopt = row[6]
    elif kind == "c":
        diff, prompt, options, correct, expl = row[1:6]
        verify = row[6] if len(row) > 6 and row[6] else None
        q = c(diff, prompt, options, correct, expl, verify)
        if len(row) > 7:
            adopt = row[7]
    else:
        raise SystemExit("Unknown question row type: %r" % (row,))
    if adopt:
        q["_adopt"] = adopt
    return q


BANK = {}
for part in (BANK_G1, BANK_G2, BANK_G3):
    overlap = set(BANK) & set(part)
    if overlap:
        raise SystemExit("Duplicate topic IDs: " + ", ".join(sorted(overlap)))
    BANK.update(part)
BANK = {tid: [convert(row) for row in rows] for tid, rows in BANK.items()}


def load(name):
    import json
    with open(os.path.join(DATA, name), encoding="utf-8") as f:
        return json.load(f)


def dump(name, obj, indent=2):
    import json
    path = os.path.join(DATA, name)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=indent)
        f.write("\n")


def apply_adopt(item, old_by_id):
    aid = item.pop("_adopt", None)
    if not aid:
        return
    old = old_by_id.get(aid)
    if old is None:
        raise SystemExit("Cannot find the old question whose figure should be reused: " + aid)
    if old.get("figure"):
        item["figure"] = old["figure"]
    if old.get("hideChoiceText"):
        item["hideChoiceText"] = True
    old_figs = {c["text"]: c["figure"] for c in old.get("choices") or [] if c.get("figure")}
    for ch in item.get("choices") or []:
        if ch["text"] in old_figs:
            ch["figure"] = old_figs[ch["text"]]
    if item.get("hideChoiceText"):
        missing = [ch["text"] for ch in item.get("choices") or [] if "figure" not in ch]
        if missing:
            raise SystemExit("%s hides choice text, but these options have no images: %s" % (aid, ", ".join(missing)))


def prompt_problem(q):
    p = str(q.get("prompt") or "").strip()
    if V.PURE_ARITH_PROMPT_RE.match(p) or V.PURE_ARITH_CHOICE_RE.match(p):
        return "pure integer or decimal calculation"
    # These Han phrases are validator match tokens for prompts in the primary banks; keep them unchanged.
    if "得数是哪一个" in p:
        return "asks which result is correct"
    if "？计算：" in p or "。计算：" in p or p.startswith("计算："):
        return "prompt already supplies an expression"
    if q.get("difficulty") == "challenge" and V.CHALLENGE_BARE_CALC_RE.match(p):
        return "challenge question is bare calculation"
    if "免费" in p or "AI 初稿" in p or "免费" in str(q.get("explanation")):
        return "prohibited wording"
    return None


def check_bank(new_qs, by_id):
    extra = []
    for q in new_qs:
        why = prompt_problem(q)
        if why:
            extra.append("%s %s: %s" % (q["id"], why, q["prompt"][:48]))
        grade = by_id[q["topicId"]].get("grade")
        if grade == 1 and any(ch in q["prompt"] for ch in "×÷xyzXYZ"):
            extra.append("%s Grade 1 prompt contains an out-of-scope symbol: %s" % (q["id"], q["prompt"][:40]))
        if "verify" not in q:
            extra.append("%s is missing a verification expression" % q["id"])
            continue
        try:
            res = VQ.safe_eval(q["verify"])
        except Exception as ex:  # noqa: BLE001
            extra.append("%s verification failed: %s" % (q["id"], ex))
            continue
        if q["type"] == "numeric":
            ok, detail = VQ.compare_numeric(q, res)
        else:
            ok, detail = VQ.compare_choice(q, res)
        if not ok:
            extra.append("%s %s" % (q["id"], detail))
    return extra


def main():
    topics = load("topics.json")
    questions = load("questions.json")
    by_id = {t["id"]: t for t in topics}
    missing = [tid for tid in BANK if tid not in by_id]
    if missing:
        raise SystemExit("Unknown topics: " + ", ".join(missing))
    low = [t for t in topics if t.get("grade") in (1, 2, 3) and str(t.get("id", "")).startswith("cnm_")
           and not t.get("external")]
    not_in_bank = [t["id"] for t in low if t["id"] not in BANK]
    if not_in_bank:
        raise SystemExit("Topics in Grades 1–3 are missing questions: " + ", ".join(not_in_bank))
    extra_topics = [tid for tid in BANK if by_id[tid].get("grade") not in (1, 2, 3)]
    if extra_topics:
        raise SystemExit("Topics outside Grades 1–3 were added: " + ", ".join(extra_topics))

    old_by_qid = {q["id"]: q for q in questions}
    old_prompts = defaultdict(list)
    for q in questions:
        if q.get("topicId") in BANK:
            old_prompts[q["topicId"]].append(q.get("prompt"))

    new_qs = []
    extra = []
    changed = 0
    for tid, raw in BANK.items():
        ds = [q["difficulty"] for q in raw]
        if ds.count("basic") != 2 or ds.count("standard") != 1 or ds.count("challenge") != 1:
            extra.append("%s does not have 2 basic + 1 standard + 1 challenge: %s" % (tid, ds))
        if len(raw) != 4 or raw[0]["difficulty"] != "basic" or raw[1]["difficulty"] != "basic":
            extra.append("%s must start with two basic questions and have four questions total" % tid)
        if len({q["prompt"] for q in raw}) != 4:
            extra.append("%s has duplicate prompts" % tid)
        oldps = old_prompts.get(tid, [])
        for i, q in enumerate(raw, 1):
            item = dict(q)
            item["id"] = "%s_q%d" % (tid, i)
            item["topicId"] = tid
            apply_adopt(item, old_by_qid)
            if i - 1 >= len(oldps) or oldps[i - 1] != item["prompt"]:
                changed += 1
            new_qs.append(item)
        t = by_id[tid]
        q1 = [q for q in new_qs if q["topicId"] == tid][0]
        if q1["type"] == "choice":
            dq_ans = [x["text"] for x in q1["choices"] if x["key"] == q1["answer"]][0]
        else:
            dq_ans = str(q1["answer"])
        t["diagnostic_question"] = {"question": q1["prompt"], "answer": dq_ans}

    extra.extend(check_bank(new_qs, by_id))
    if extra:
        raise SystemExit("Question-bank validation failed:\n" + "\n".join(extra))

    old_ids = set(BANK)
    out = []
    seen = set()
    i = 0
    while i < len(questions):
        tid = questions[i].get("topicId")
        if tid in old_ids and tid not in seen:
            j = i
            while j < len(questions) and questions[j].get("topicId") == tid:
                j += 1
            out.extend(q for q in new_qs if q["topicId"] == tid)
            seen.add(tid)
            i = j
        else:
            out.append(questions[i])
            i += 1
    leftover = old_ids - seen
    if leftover:
        raise SystemExit("No existing questions for these topics were found in questions.json: " + ", ".join(sorted(leftover)))
    if len(out) != len(questions):
        raise SystemExit("Question count changed: %d → %d" % (len(questions), len(out)))
    ids = [q["id"] for q in out]
    if len(ids) != len(set(ids)):
        raise SystemExit("Duplicate IDs after replacement")
    protected = [q for q in out if by_id.get(q["topicId"], {}).get("grade") in (4, 5, 6)
                 and q["topicId"].startswith("cnm_")]
    old_protected = [q for q in questions if by_id.get(q["topicId"], {}).get("grade") in (4, 5, 6)
                     and str(q["topicId"]).startswith("cnm_")]
    if protected != old_protected:
        raise SystemExit("Grade 4–6 questions were modified")

    dump("questions.json", out, 2)
    dump("topics.json", topics, 2)
    for grade, name in ((1, "_qbatches/primary_g1.json"), (2, "_qbatches/primary_g2.json"),
                        (3, "_qbatches/primary_g3.json")):
        batch = [q for q in out if by_id.get(q["topicId"], {}).get("grade") == grade
                 and str(q["topicId"]).startswith("cnm_")]
        dump(name, batch, 1)

    sem = Counter((by_id[tid]["grade"], by_id[tid]["semester"]) for tid in BANK)
    print("Grade 1–3 topics: %d; questions: %d" % (len(BANK), len(new_qs)))
    # "上"/"下" are semester values in topics.json and must remain lookup tokens.
    for g in (1, 2, 3):
        for s in ("上", "下"):
            n_topic = sem[(g, s)]
            print("%d %s: %d topics, %d questions" % (g, "fall" if s == "上" else "spring", n_topic, n_topic * 4))
    print("Difficulty", Counter(q["difficulty"] for q in new_qs))
    print("Question types", Counter(q["type"] for q in new_qs))
    print("Rewritten prompts: %d / %d" % (changed, len(new_qs)))

    print("\nExample rewritten prompt by term (one per term)")
    shown = set()
    for q in new_qs:
        t = by_id[q["topicId"]]
        key = (t["grade"], t["semester"])
        if key in shown or not q["id"].endswith("_q1"):
            continue
        oldps = old_prompts.get(q["topicId"], [])
        if not oldps or oldps[0] == q["prompt"]:
            continue
        shown.add(key)
        print("%d %s %s" % (t["grade"], "fall" if t["semester"] == "上" else "spring", t["name"]))
        print("  Before: %s" % oldps[0])
        print("  After: %s" % q["prompt"])
    missing_sem = [(g, s) for g in (1, 2, 3) for s in ("上", "下") if (g, s) not in shown]
    if missing_sem:
        print(
            "The first prompt was unchanged for these terms; showing the first rewrite for each instead:",
            [(g, "fall" if s == "上" else "spring") for g, s in missing_sem],
        )
        for q in new_qs:
            t = by_id[q["topicId"]]
            key = (t["grade"], t["semester"])
            if key not in missing_sem:
                continue
            idx = int(q["id"].rsplit("_q", 1)[1]) - 1
            oldps = old_prompts.get(q["topicId"], [])
            if idx >= len(oldps) or oldps[idx] == q["prompt"]:
                continue
            missing_sem.remove(key)
            print("%d %s %s %s" % (t["grade"], "fall" if t["semester"] == "上" else "spring", t["name"], q["id"]))
            print("  Before: %s" % oldps[idx])
            print("  After: %s" % q["prompt"])


if __name__ == "__main__":
    main()
