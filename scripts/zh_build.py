#!/usr/bin/env python3
"""Compile the elementary-school Chinese-language draft into data/topics.json, dependencies.json, questions.json, and the curriculum standards file.

Can be rerun: remove existing cnc_ topics and ccs- standards entries, then regenerate them from this script.
Does not modify mathematics, English, or physics topics, prerequisites, questions, or standards. Transitively reduce prerequisites only among Chinese-language edges.

Usage: python3 scripts/zh_build.py
"""
from __future__ import annotations

import json
import os
import re
import sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import zh_g1  # noqa: E402,F401
import zh_g2  # noqa: E402,F401
import zh_g3  # noqa: E402,F401
import zh_g4  # noqa: E402,F401
import zh_g5  # noqa: E402,F401
import zh_g6  # noqa: E402,F401
import zh_edges  # noqa: E402,F401
from zh_lib import HARD, STANDARD_ROWS, TOPICS, chapter, check_question, materialise_questions  # noqa: E402
from verify_questions import verify_all  # noqa: E402

# Parser-required Chinese domain labels; these must match the imported curriculum-standard rows.
ZH_CODES = {
    "PY": "拼音", "SZ": "识字写字", "CY": "词语", "JZ": "句子",
    "YD": "阅读理解", "GS": "古诗文积累", "XZ": "习作基础",
}
# Parser-required Chinese grade, semester, and chapter markers matching the chapter catalog format.
CHAPTER_RE = re.compile(r"^([一二三四五六七八九])年级([上下全])册 (第\d+单元|预备单元\d) (.+)$")
# Parser-required Chinese semester markers in volume identifiers.
VOLUMES = ["1上", "1下", "2上", "2下", "3上", "3下", "4上", "4下", "5上", "5下", "6上", "6下"]


def load(name):
    with open(os.path.join(ROOT, "data", name), encoding="utf-8") as f:
        return json.load(f)


def dump(name, data):
    path = os.path.join(ROOT, "data", name)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def is_zh_topic_id(tid):
    return str(tid).startswith("cnc_")


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


def reduce_chinese(edges):
    """Remove redundant edges only among Chinese-language topics. Drop a hard edge only if another all-hard path exists; drop a soft edge if any alternate path exists."""
    adj = defaultdict(list)
    for e in edges:
        adj[e["topicId"]].append([e["prerequisiteId"], e["strength"]])
    kept = []
    dropped = 0
    for e in edges:
        if not is_zh_topic_id(e["topicId"]):
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
        if domain != ZH_CODES[code]:
            raise SystemExit("Curriculum domain mismatch: %s" % symbol)
        key = (level, code)
        counters[key] = counters.get(key, 0) + 1
        sid = "ccs-2022:%s.%s.%02d" % (level, code, counters[key])
        id_of[symbol] = sid
        items.append({
            "id": sid,
            "domain": domain,
            "section": section,
            "clause": "(%d)" % counters[key],
            "text": text,
            "page_or_ref": "Needs verification",
            "verbatim": False,
            "text_status": "Public paraphrase; not checked page by page against the Curriculum Standards for Chinese Language in Compulsory Education (2022 Edition)",
        })
    return id_of, items


def build_question(tid, index, made, slot):
    qid = "%s_q%d" % (tid, index)
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


def rank_of(spec):
    return spec["grade"] * 2 + (1 if spec["semester"] == "下" else 0)


def main():
    topics = load("topics.json")
    deps = load("dependencies.json")
    questions = load("questions.json")
    standards = load("cn-curriculum-standards.json")

    by_vol = Counter("%d%s" % (t["grade"], t["semester"]) for t in TOPICS)
    for k in VOLUMES:
        n = by_vol[k]
        # Grades 1–6, both semesters, are covered lesson by lesson in the unified textbook sequence.
        lo, hi = (30, 48) if k in ("1上", "1下", "2上", "2下", "3上", "3下", "4上", "4下", "5上", "5下", "6上", "6下") else (18, 22)
        if n < lo or n > hi:
            print("%s has %d topics; each volume should have %d–%d" % (k, n, lo, hi), file=sys.stderr)
            return 1
    if TOPICS[0]["key"] != "g1a_tian":
        print("The first topic must be g1a_tian", file=sys.stderr)
        return 1
    # Keep this validation aligned with the translated topic title.
    if not any("Quiet Night Thoughts" in t["name"] for t in TOPICS):
        print("A topic name must include 'Quiet Night Thoughts'", file=sys.stderr)
        return 1
    keys = [t["key"] for t in TOPICS]
    if len(set(keys)) != len(keys):
        print("Duplicate topic key", file=sys.stderr)
        return 1

    base_topics = [t for t in topics if not is_zh_topic_id(t.get("id"))]
    base_deps = [e for e in deps if not is_zh_topic_id(e.get("topicId")) and not is_zh_topic_id(e.get("prerequisiteId"))]
    base_questions = [q for q in questions if not is_zh_topic_id(q.get("topicId"))]
    base_items = [it for it in standards.get("items", []) if not str(it.get("id", "")).startswith("ccs-")]
    if any(is_zh_topic_id(t.get("id")) for t in base_topics):
        print("Failed to remove Chinese-language topics", file=sys.stderr)
        return 1

    id_of_std, new_items = build_standards()
    used_std = {t["std"] for t in TOPICS}
    missing_std = [row[0] for row in STANDARD_ROWS if row[0] not in used_std]
    if missing_std:
        print("Curriculum standard rows are not referenced by any topic: %s" % ", ".join(missing_std), file=sys.stderr)
        return 1
    index = {t["key"]: i for i, t in enumerate(TOPICS)}
    by_key = {t["key"]: t for t in TOPICS}
    names = {t["key"]: t["name"] for t in TOPICS}
    hard_pairs = {}
    for src, dst, reason in HARD:
        if src not in index or dst not in index:
            print("Hard prerequisite points to an unregistered topic: %s → %s" % (src, dst), file=sys.stderr)
            return 1
        if index[dst] >= index[src]:
            print("Hard prerequisite is not earlier than the dependent topic: %s depends on %s" % (src, dst), file=sys.stderr)
            return 1
        if rank_of(by_key[dst]) > rank_of(by_key[src]):
            print("Hard prerequisite is in a later volume: %s depends on %s" % (src, dst), file=sys.stderr)
            return 1
        if (src, dst) in hard_pairs:
            print("Duplicate hard edge %s → %s" % (src, dst), file=sys.stderr)
            return 1
        hard_pairs[(src, dst)] = reason

    new_topics = []
    new_questions = []
    id_of = {}
    for i, spec in enumerate(TOPICS, start=1):
        tid = "cnc_p%03d" % i
        id_of[spec["key"]] = tid
        if spec["std"] not in id_of_std:
            print("Curriculum standard %s does not exist for %s" % (spec["std"], spec["key"]), file=sys.stderr)
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
        ch = chapter(spec["grade"], spec["semester"], spec["unit"])
        if not CHAPTER_RE.match(ch):
            print("Chapter format cannot be browsed by volume for %s: %s" % (spec["key"], ch), file=sys.stderr)
            return 1
        ref = {"id": id_of_std[spec["std"]], "confidence": spec["conf"]}
        if spec.get("note"):
            ref["note"] = spec["note"]
        topic = {
            "id": tid,
            "name": spec["name"],
            "domain": spec["domain"],
            "grade": spec["grade"],
            "semester": spec["semester"],
            "chapter": ch,
            "type": spec["type"],
            "description": spec["description"],
            "mastery_criteria": spec["mastery_criteria"],
            "diagnostic_question": {"question": built[0]["prompt"], "answer": diag_answer},
            "external": False,
            "subject": "chinese",
            "standards": [ref],
        }
        if spec["key"] == "g1a_tian":
            topic["root_reason"] = "First-grade Chinese begins with character recognition in “Heaven, Earth, and People.” In the unified textbooks revised in 2024, character recognition comes before Chinese pinyin, and there is no earlier elementary-school Chinese topic."
        new_topics.append(topic)
        new_questions.extend(built)

    raw = []
    for i in range(1, len(TOPICS)):
        cur = TOPICS[i]["key"]
        prev = TOPICS[i - 1]["key"]
        if (cur, prev) in hard_pairs:
            continue
        reason = "The usual teaching sequence in the unified textbooks teaches “%s” before “%s”." % (names[prev], names[cur])
        raw.append((cur, prev, "soft", reason))
    for src, dst, reason in HARD:
        raw.append((src, dst, "hard", reason))

    new_edges = []
    seen = set()
    for src, dst, strength, reason in raw:
        if index[dst] >= index[src]:
            print("Prerequisite is not earlier than the dependent topic: %s depends on %s" % (src, dst), file=sys.stderr)
            return 1
        if rank_of(by_key[dst]) > rank_of(by_key[src]):
            print("Prerequisite is in a later grade: %s depends on %s" % (src, dst), file=sys.stderr)
            return 1
        key = (id_of[src], id_of[dst])
        if key in seen:
            print("Duplicate edge %s → %s" % key, file=sys.stderr)
            return 1
        seen.add(key)
        new_edges.append({
            "topicId": id_of[src],
            "prerequisiteId": id_of[dst],
            "strength": strength,
            "reason": reason,
        })

    merged_deps, dropped = reduce_chinese(base_deps + new_edges)
    zh_edges = [e for e in merged_deps if is_zh_topic_id(e["topicId"])]
    if any(not is_zh_topic_id(e["prerequisiteId"]) for e in zh_edges):
        print("A Chinese-language prerequisite edge points to another subject", file=sys.stderr)
        return 1
    if any(is_zh_topic_id(e["topicId"]) or is_zh_topic_id(e["prerequisiteId"]) for e in base_deps):
        print("A Chinese-language prerequisite edge remains after removal", file=sys.stderr)
        return 1
    covered = {e["topicId"] for e in zh_edges}
    missing = [t["id"] for t in new_topics if t["id"] != "cnc_p001" and t["id"] not in covered]
    if missing:
        print("Topics still have no prerequisite after reduction: %s" % ", ".join(missing), file=sys.stderr)
        return 1

    checked = verify_all(new_questions)
    if checked["mismatch"] or checked["unverifiable"]:
        for m in checked["mismatch"][:40]:
            print("Question verification failed for %s: %s" % (m["id"], m.get("detail")), file=sys.stderr)
        print("Question verification failed: %d mismatches, %d unverifiable" % (
            len(checked["mismatch"]), len(checked["unverifiable"])), file=sys.stderr)
        return 1

    kept_std = {k: v for k, v in standards.items() if k != "items" and k != "chinese"}
    standards_out = dict(standards)
    standards_out["items"] = list(base_items) + new_items
    standards_out["chinese"] = {
        "title": "Curriculum Standards for Chinese Language in Compulsory Education (2022 Edition)",
        "issuer": "Ministry of Education of the People's Republic of China",
        "year": 2022,
        "stage": "Stages 1–3",
        "note": "Items are public paraphrases of the learning requirements for Stages 1–3, not text verified page by page. `verbatim` is false, and `page_or_ref` is “Needs verification.” The `ccs-2022` identifiers are assigned by this graph, not by the Ministry of Education. Grade 1 follows the unified textbook sequence revised from 2024; Grades 2–3 fall terms follow the autumn 2025 revised contents and spring terms follow the spring 2026 revised contents; Grade 4 fall follows the 2024 revised sequence lesson by lesson, and spring follows the current unified contents; Grade 5 fall follows the autumn 2026 sequence, and spring follows the current sequence; Grade 6 fall follows the autumn 2026 sequence, and spring follows the current sequence. No page numbers are included.",
    }
    for k, v in kept_std.items():
        standards_out[k] = v

    math_before = [(t["id"], t["name"]) for t in base_topics if str(t["id"]).startswith("cnm_")]
    en_before = [(t["id"], t["name"]) for t in base_topics if str(t["id"]).startswith("cne_")]
    phy_before = [(t["id"], t["name"]) for t in base_topics if str(t["id"]).startswith("cnp_")]

    n_hard = sum(1 for e in zh_edges if e["strength"] == "hard")
    n_soft = sum(1 for e in zh_edges if e["strength"] == "soft")
    by_dom = Counter(t["domain"] for t in new_topics)
    print("Chinese-language topics: %d" % len(new_topics))
    for k in ["1上", "1下", "2上", "2下", "3上", "3下", "4上", "4下", "5上", "5下", "6上", "6下"]:
        print("  %s %d" % (k, by_vol[k]))
    for k, v in by_dom.most_common():
        print("  %s %d" % (k, v))
    print("Chinese-language edges written: %d (reduced by %d); hard: %d, soft: %d" % (len(zh_edges), dropped, n_hard, n_soft))
    print("Questions: %d" % len(new_questions))
    print("Curriculum standard items: %d" % len(new_items))

    dump("topics.json", base_topics + new_topics)
    dump("dependencies.json", merged_deps)
    dump("questions.json", base_questions + new_questions)
    dump("cn-curriculum-standards.json", standards_out)

    again_t = load("topics.json")
    again_d = load("dependencies.json")
    again_q = load("questions.json")
    again_s = load("cn-curriculum-standards.json")
    again_topics = [t for t in again_t if not is_zh_topic_id(t.get("id"))]
    again_deps = [e for e in again_d if not is_zh_topic_id(e.get("topicId")) and not is_zh_topic_id(e.get("prerequisiteId"))]
    again_qs = [q for q in again_q if not is_zh_topic_id(q.get("topicId"))]
    again_items = [it for it in again_s.get("items", []) if not str(it.get("id", "")).startswith("ccs-")]
    if again_topics != base_topics or again_deps != base_deps or again_qs != base_questions or again_items != base_items:
        print("Mathematics, English, or physics data changed after writing", file=sys.stderr)
        return 1
    if [(t["id"], t["name"]) for t in again_t if str(t["id"]).startswith("cnm_")] != math_before:
        print("Mathematics topic IDs or names changed", file=sys.stderr)
        return 1
    if [(t["id"], t["name"]) for t in again_t if str(t["id"]).startswith("cne_")] != en_before:
        print("English topic IDs or names changed", file=sys.stderr)
        return 1
    if [(t["id"], t["name"]) for t in again_t if str(t["id"]).startswith("cnp_")] != phy_before:
        print("Physics topic IDs or names changed", file=sys.stderr)
        return 1
    for k, v in kept_std.items():
        if again_s.get(k) != v:
            print("Existing curriculum standards object %s changed" % k, file=sys.stderr)
            return 1
    if again_s.get("chinese", {}).get("title") != "Curriculum Standards for Chinese Language in Compulsory Education (2022 Edition)":
        print("Incorrect Chinese-language curriculum standards title", file=sys.stderr)
        return 1
    print("IDs and names unchanged for %d mathematics, %d English, and %d physics topics" % (
        len(math_before), len(en_before), len(phy_before)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
