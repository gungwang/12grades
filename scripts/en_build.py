#!/usr/bin/env python3
"""Compile the elementary English draft into data/topics.json, dependencies.json, questions.json, and the curriculum standards file.

Run only when cne_p001 is not already present. A second run is rejected to prevent duplicate additions.
Transitive reduction is applied only to newly added English prerequisite edges; existing math edges are not changed.

Usage: python3 scripts/en_build.py
"""
from __future__ import annotations

import json
import os
import sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import en_topics  # noqa: E402,F401
from en_lib import HARD, STANDARD_ROWS, TOPICS, check_question, materialise_questions  # noqa: E402
from verify_questions import verify_all  # noqa: E402

# Keep these Chinese domain values: they are schema tokens consumed by scripts/validate.py.
EN_CODES = {"PH": "语音", "VO": "词汇", "GR": "语法", "FU": "日常表达", "RW": "读写"}


def load(name):
    with open(os.path.join(ROOT, "data", name), encoding="utf-8") as f:
        return json.load(f)


def dump(name, data):
    path = os.path.join(ROOT, "data", name)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


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


def reduce_english(edges):
    """Remove only redundant new edges among English topics. Drop a hard edge only if another all-hard path exists; drop a soft edge if any alternate path exists."""
    adj = defaultdict(list)
    for e in edges:
        adj[e["topicId"]].append([e["prerequisiteId"], e["strength"]])
    kept = []
    dropped = 0
    for e in edges:
        if not str(e["topicId"]).startswith("cne_"):
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


def build_standards():
    counters = {}
    id_of = {}
    items = []
    for symbol, level, code, domain, section, text in STANDARD_ROWS:
        if domain != EN_CODES[code]:
            raise SystemExit("Curriculum domain mismatch: %s" % symbol)
        key = (level, code)
        counters[key] = counters.get(key, 0) + 1
        sid = "ces-2022:%s.%s.%02d" % (level, code, counters[key])
        id_of[symbol] = sid
        items.append({
            "id": sid,
            "domain": domain,
            "section": section,
            "clause": "(%d)" % counters[key],
            "text": text,
            "page_or_ref": "待核",  # Required schema token checked by scripts/validate.py for unverified page references.
            "verbatim": False,
            "text_status": "Public paraphrase; not checked page by page against the English Curriculum Standards for Compulsory Education (2022 Edition).",
        })
    return id_of, items


def build_question(tid, index, made, slot):
    qid = "%s_q%d" % (tid, index)
    if made["t"] == "numeric":
        return {
            "id": qid,
            "topicId": tid,
            "difficulty": made["d"],
            "type": "numeric",
            "prompt": made["p"],
            "answer": made["a"],
            "explanation": made["e"],
            "verify": made["v"],
        }, made["a"]
    texts = list(made["w"])
    texts.insert(slot % 4, made["a"])
    keys = list("ABCD")
    pos = texts.index(made["a"])
    return {
        "id": qid,
        "topicId": tid,
        "difficulty": made["d"],
        "type": "choice",
        "prompt": made["p"],
        "choices": [{"key": keys[i], "text": texts[i]} for i in range(4)],
        "answer": keys[pos],
        "explanation": made["e"],
        "verify": json.dumps(made["a"], ensure_ascii=False),
    }, made["a"]


def main():
    topics = load("topics.json")
    deps = load("dependencies.json")
    questions = load("questions.json")
    standards = load("cn-curriculum-standards.json")
    if any(str(t.get("id", "")).startswith("cne_") for t in topics):
        print("cne_ topics already exist. en_build.py cannot be run twice.", file=sys.stderr)
        return 1
    if not (150 <= len(TOPICS) <= 250):
        print("Topic count %d is outside the range 150–250." % len(TOPICS), file=sys.stderr)
        return 1
    if TOPICS[0]["key"] != "ph_alpha":
        print("The first topic must be ph_alpha.", file=sys.stderr)
        return 1

    id_of_std, new_items = build_standards()
    index = {t["key"]: i for i, t in enumerate(TOPICS)}
    by_key = {t["key"]: t for t in TOPICS}
    names = {t["key"]: t["name"] for t in TOPICS}
    hard_pairs = {}
    for src, dst, reason in HARD:
        if src not in index or dst not in index:
            print("Hard prerequisite points to an unregistered topic: %s → %s" % (src, dst), file=sys.stderr)
            return 1
        if index[dst] >= index[src]:
            print("Hard prerequisite is not earlier than its dependent: %s depends on %s." % (src, dst), file=sys.stderr)
            return 1
        if (src, dst) in hard_pairs:
            print("Duplicate hard edge %s → %s." % (src, dst), file=sys.stderr)
            return 1
        hard_pairs[(src, dst)] = reason

    new_topics = []
    new_questions = []
    id_of = {}
    for i, spec in enumerate(TOPICS, start=1):
        tid = "cne_p%03d" % i
        id_of[spec["key"]] = tid
        if spec["std"] not in id_of_std:
            print("Curriculum standard %s is missing for %s." % (spec["std"], spec["key"]), file=sys.stderr)
            return 1
        made = materialise_questions(spec)
        for q in made:
            check_question(spec["key"], q)
        built = []
        diag_answer = None
        for n, item in enumerate(made, start=1):
            q, shown = build_question(tid, n, item, slot=i + n)
            built.append(q)
            if n == 1:
                diag_answer = shown
        ref = {"id": id_of_std[spec["std"]], "confidence": spec["conf"]}
        if spec.get("note"):
            ref["note"] = spec["note"]
        topic = {
            "id": tid,
            "name": spec["name"],
            "domain": spec["domain"],
            "grade": spec["grade"],
            "semester": spec["semester"],
            "chapter": __import__("en_lib").chapter(spec["grade"], spec["semester"], spec["unit"]),
            "type": spec["type"],
            "description": spec["description"],
            "mastery_criteria": spec["mastery_criteria"],
            "diagnostic_question": {"question": built[0]["prompt"], "answer": diag_answer},
            "external": False,
            "subject": "english",
            "standards": [ref],
        }
        if spec["key"] == "ph_alpha":
            topic["root_reason"] = "Grade 3 English begins with recognizing the alphabet; there are no earlier elementary English topics."
        new_topics.append(topic)
        new_questions.extend(built)

    raw = []
    seen = set()
    for i in range(1, len(TOPICS)):
        cur = TOPICS[i]["key"]
        prev = TOPICS[i - 1]["key"]
        if (cur, prev) in hard_pairs:
            continue
        reason = "Following the common curriculum sequence for a Grade 3 starting point, learn “%s” before “%s”." % (names[prev], names[cur])
        raw.append((cur, prev, "soft", reason))
    for src, dst, reason in HARD:
        raw.append((src, dst, "hard", reason))

    new_edges = []
    for src, dst, strength, reason in raw:
        if index[dst] >= index[src]:
            print("Prerequisite is not earlier than its dependent: %s depends on %s." % (src, dst), file=sys.stderr)
            return 1
        ra = by_key[src]["grade"] * 2 + (1 if by_key[src]["semester"] == "下" else 0)
        rb = by_key[dst]["grade"] * 2 + (1 if by_key[dst]["semester"] == "下" else 0)
        if rb > ra:
            print("Prerequisite is in a later grade: %s depends on %s." % (src, dst), file=sys.stderr)
            return 1
        key = (id_of[src], id_of[dst])
        if key in seen:
            print("Duplicate edge %s → %s." % key, file=sys.stderr)
            return 1
        seen.add(key)
        new_edges.append({
            "topicId": id_of[src],
            "prerequisiteId": id_of[dst],
            "strength": strength,
            "reason": reason,
        })

    merged_deps, dropped = reduce_english(deps + new_edges)
    eng_edges = [e for e in merged_deps if str(e["topicId"]).startswith("cne_")]
    if any(not str(e["prerequisiteId"]).startswith("cne_") for e in eng_edges):
        print("An English edge points to a math topic.", file=sys.stderr)
        return 1
    if any(str(e["topicId"]).startswith("cne_") for e in deps):
        print("The existing dependencies already contain English edges.", file=sys.stderr)
        return 1
    covered = {e["topicId"] for e in eng_edges}
    missing = [t["id"] for t in new_topics if t["id"] != "cne_p001" and t["id"] not in covered]
    if missing:
        print("Topics still lack prerequisites after reduction: %s" % ", ".join(missing), file=sys.stderr)
        return 1

    checked = verify_all(new_questions)
    if checked["mismatch"] or checked["unverifiable"]:
        for m in checked["mismatch"][:40]:
            print("Question verification failed for %s: %s" % (m["id"], m.get("detail")), file=sys.stderr)
        print("Question verification failed: %d mismatches, %d unverifiable." % (
            len(checked["mismatch"]), len(checked["unverifiable"])), file=sys.stderr)
        return 1

    n_hard = sum(1 for e in eng_edges if e["strength"] == "hard")
    n_soft = sum(1 for e in eng_edges if e["strength"] == "soft")
    # Keep 上/下 in these internal bucket keys: they are serialized semester values checked by scripts/validate.py.
    by_grade = Counter("%d%s" % (t["grade"], t["semester"]) for t in new_topics)
    by_dom = Counter(t["domain"] for t in new_topics)
    print("English topics: %d" % len(new_topics))
    for k in ["3上", "3下", "4上", "4下", "5上", "5下", "6上", "6下"]:
        print("  Grade %s, semester %s: %d" % (k[0], "1" if k[1] == "上" else "2", by_grade[k]))
    for k, v in by_dom.most_common():
        label = {
            "语音": "Pronunciation",
            "词汇": "Vocabulary",
            "语法": "Grammar",
            "日常表达": "Everyday expressions",
            "读写": "Reading and writing",
        }.get(k, k)
        print("  %s: %d" % (label, v))
    print("English edges written: %d (reduced by %d); hard: %d, soft: %d" % (len(eng_edges), dropped, n_hard, n_soft))
    print("Questions: %d" % len(new_questions))
    print("Curriculum standards: %d" % len(new_items))

    old_topic_n = len(topics)
    old_dep_n = len(deps)
    old_q_n = len(questions)
    old_std_n = len(standards["items"])
    standards["english"] = {
        "title": "English Curriculum Standards for Compulsory Education (2022 Edition)",
        "issuer": "Ministry of Education of the People's Republic of China",
        "year": 2022,
        "stage": "Compulsory education levels 3 (Grades 3–4, first level) and 4 (Grades 5–6, second level)",
        "note": "The entries are public paraphrases of the first- and second-level language skills, not text verified page by page. verbatim is false and page_or_ref is the required placeholder “待核”. The ces-2022 identifiers belong to this graph, not the Ministry of Education. The curriculum follows the common Grade 3-start sequence of the People's Education Press PEP textbooks and includes no page numbers.",
    }
    standards["items"].extend(new_items)
    dump("topics.json", topics + new_topics)
    dump("dependencies.json", merged_deps)
    dump("questions.json", questions + new_questions)
    dump("cn-curriculum-standards.json", standards)

    again_t = load("topics.json")
    again_d = load("dependencies.json")
    again_q = load("questions.json")
    again_s = load("cn-curriculum-standards.json")
    if again_t[:old_topic_n] != topics or again_d[:old_dep_n] != deps or again_q[:old_q_n] != questions:
        print("Math data changed during write-back.", file=sys.stderr)
        return 1
    if again_s["items"][:old_std_n] != standards["items"][:old_std_n]:
        print("Existing curriculum-standard entries changed.", file=sys.stderr)
        return 1
    math_names = [(t["id"], t["name"]) for t in topics]
    if [(t["id"], t["name"]) for t in again_t if str(t["id"]).startswith("cnm_")] != math_names:
        print("A math topic ID or name changed.", file=sys.stderr)
        return 1
    print("Math topic IDs and names remain unchanged: %d topics." % len(math_names))
    return 0


if __name__ == "__main__":
    sys.exit(main())
