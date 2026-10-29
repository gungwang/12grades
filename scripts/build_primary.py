#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compile the primary-school catalog into data/. Safe to rerun: junior-high topics, questions, and prerequisite edges retain their original objects.

Primary-school IDs are assigned in catalog order starting at cnm_p001. Legacy cnm_ext_* IDs are omitted from topics.json and written to data/id-aliases.json.
"""
import copy
import hashlib
import json
import os
import sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from primary_g12 import TOPICS as T12
from primary_g34 import TOPICS as T34
from primary_g46 import TOPICS as T46
from primary_g56 import TOPICS as T56
from primary_std import ITEMS as PRIMARY_ITEMS
from primary_recheck import expected_numeric, eval_zh, fmt_value, solve_question
import verify_questions as VQ

DATA = os.path.join(ROOT, "data")
ZH = "123456"

# (junior-high ID, legacy external ID) -> list of primary-school slugs. Keep each edge's original strength.
# At compile time, combine the original reason with the specific primary-school topic to form a complete sentence.
RETARGET = {
    ("cnm_001", "cnm_ext_006"): ["neg_know"],
    ("cnm_003", "cnm_ext_002"): ["frac_meaning"],
    ("cnm_003", "cnm_ext_003"): ["dec_meaning"],
    ("cnm_023", "cnm_ext_003"): ["dec_approx"],
    ("cnm_025", "cnm_ext_007"): ["letter"],
    ("cnm_027", "cnm_ext_009"): ["qty_rel"],
    ("cnm_044", "cnm_ext_008"): ["lcm"],
    ("cnm_048", "cnm_ext_004"): ["pct_discount"],
    ("cnm_050", "cnm_ext_012"): ["cuboid", "cylinder"],
    ("cnm_051", "cnm_ext_015"): ["observe"],
    ("cnm_053", "cnm_ext_014"): ["line_seg"],
    ("cnm_056", "cnm_ext_013"): ["angle_measure"],
    ("cnm_057", "cnm_ext_009"): ["time_hms"],
    ("cnm_064", "cnm_ext_014"): ["perp"],
    ("cnm_067", "cnm_ext_014"): ["parallel"],
    ("cnm_072", "cnm_ext_015"): ["translate"],
    ("cnm_081", "cnm_ext_016"): ["coord_pair"],
    ("cnm_102", "cnm_ext_017"): ["stat_table"],
    ("cnm_105", "cnm_ext_017"): ["bar", "line_chart", "pie"],
    ("cnm_105", "cnm_ext_004"): ["pct_meaning"],
    ("cnm_106", "cnm_ext_017"): ["stat_table"],
    ("cnm_110", "cnm_ext_011"): ["tri_class"],
    ("cnm_120", "cnm_ext_015"): ["translate"],
    ("cnm_131", "cnm_ext_015"): ["reflect"],
    ("cnm_148", "cnm_ext_010"): ["rect_area"],
    ("cnm_150", "cnm_ext_008"): ["factor"],
    ("cnm_171", "cnm_ext_008"): ["factor"],
    ("cnm_200", "cnm_ext_005"): ["direct_prop"],
    ("cnm_211", "cnm_ext_017"): ["mean"],
    ("cnm_212", "cnm_ext_004"): ["pct_meaning"],
    ("cnm_213", "cnm_ext_017"): ["mean"],
    ("cnm_227", "cnm_ext_004"): ["pct_app"],
    ("cnm_237", "cnm_ext_005"): ["inverse_prop"],
    ("cnm_244", "cnm_ext_015"): ["rotate"],
    ("cnm_268", "cnm_ext_005"): ["proportion"],
    ("cnm_284", "cnm_ext_018"): ["chance"],
    ("cnm_285", "cnm_ext_002"): ["frac_meaning"],
    ("cnm_293", "cnm_ext_017"): ["stat_table"],
    ("cnm_295", "cnm_ext_004"): ["pct_meaning"],
    ("cnm_295", "cnm_ext_013"): ["angle_measure"],
    ("cnm_297", "cnm_ext_004"): ["pct_meaning"],
}

ALIASES = [
    ("cnm_ext_001", "Integer arithmetic and operation laws", ["add_col", "mul_1d", "paren", "dist_law"]),
    ("cnm_ext_002", "Meaning and operations of fractions", ["frac_meaning", "frac_add", "frac_mul", "frac_div"]),
    ("cnm_ext_003", "Meaning and operations of decimals", ["dec_meaning", "dec_add", "dec_mul", "dec_div"]),
    ("cnm_ext_004", "Percentages and their applications", ["pct_meaning", "pct_discount", "pct_app"]),
    ("cnm_ext_005", "Ratios and proportions, including direct and inverse proportions", ["ratio", "proportion", "direct_prop", "inverse_prop"]),
    ("cnm_ext_006", "Understanding negative numbers", ["neg_know"]),
    ("cnm_ext_007", "Representing numbers with letters and simple equations", ["letter", "eq_solve"]),
    ("cnm_ext_008", "Factors, multiples, primes, and composites", ["factor", "prime", "lcm"]),
    ("cnm_ext_009", "Common quantity relationships and unit conversion", ["qty_rel", "km", "g_kg", "time_hms"]),
    ("cnm_ext_010", "Plane figures, perimeter, and area", ["rect_area", "para_area", "tri_area", "circ_area"]),
    ("cnm_ext_011", "Classifying triangles and the sum of their interior angles", ["tri_class", "tri_angle_sum"]),
    ("cnm_ext_012", "Solid figures, surface area, and volume", ["cuboid", "cylinder", "cone"]),
    ("cnm_ext_013", "Understanding and measuring angles", ["angle_measure", "angle_class"]),
    ("cnm_ext_014", "Parallel and perpendicular lines", ["perp", "parallel"]),
    ("cnm_ext_015", "Translations, rotations, and reflections of figures", ["translate", "rotate", "reflect"]),
    ("cnm_ext_016", "Locating points with coordinate pairs, directions, and distances", ["coord_pair", "dir_dist"]),
    ("cnm_ext_017", "Statistical tables, charts, and averages", ["stat_table", "line_chart", "pie", "mean"]),
    ("cnm_ext_018", "Probability", ["chance"]),
]


def load(name):
    with open(os.path.join(DATA, name), encoding="utf-8") as f:
        return json.load(f)


def dump(name, obj, indent):
    path = os.path.join(DATA, name)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=indent)
        f.write("\n")


def is_junior_id(tid):
    return isinstance(tid, str) and tid.startswith("cnm_") and not tid.startswith("cnm_p") and not tid.startswith("cnm_ext_")


def grade_rank(grade, semester):
    # "上" and "下" are parser-structural semester codes in the primary catalog.
    return grade * 2 + (1 if semester == "下" else 0)


def chapter_of(t):
    g = ZH[t["grade"] - 1]
    semester = "Semester 1" if t["semester"] == "上" else "Semester 2"
    if t["ip"]:
        return "Grade %s, %s, Integrated Study and Practice: %s" % (g, semester, t["uname"])
    if not t["unit"]:
        raise SystemExit("Topic outside Integrated Study and Practice has no unit number: %s" % t["slug"])
    return "Grade %s, %s, Unit %d: %s" % (g, semester, t["unit"], t["uname"])


def standards_of(codes):
    out = []
    for c in codes:
        if isinstance(c, tuple):
            code, note = c
            out.append({"id": "cms-2022:" + code, "confidence": "inferred", "note": note})
        else:
            out.append({"id": "cms-2022:" + c, "confidence": "exact"})
    return out


def primary_reason(child, pre, strength):
    if strength == "soft":
        return '"%s" helps with learning "%s", but the latter can be started without the former.' % (pre["name"], child["name"])
    return 'Learning "%s" requires first mastering "%s".' % (child["name"], pre["name"])


def build_question(raw, tid, n):
    q = {
        "id": "%s_q%d" % (tid, n),
        "topicId": tid,
        "difficulty": raw["difficulty"],
        "type": raw["type"],
        "prompt": raw["prompt"],
    }
    ev = VQ.safe_eval(raw["verify"])
    if raw.get("_numchoice"):
        # The original Chinese result delimiter is required to extract the arithmetic expression.
        expr = raw["prompt"].split(" 的得数")[0]
        as_dec = ("." in expr) or ("314" in expr)
        correct = fmt_value(eval_zh(expr), as_decimal=as_dec)
        wrongs = []
        for w in raw["wrongs"]:
            text = w
            guard = 0
            while text == correct or text in wrongs:
                guard += 1
                if guard > 5:
                    raise SystemExit("%s: could not avoid a duplicate choice: %s" % (q["id"], raw["prompt"]))
                text = text + str(guard)
            wrongs.append(text)
        shift = int(hashlib.md5(raw["prompt"].encode("utf-8")).hexdigest(), 16) % 4
        opts = wrongs[:]
        opts.insert(shift, correct)
        q["choices"] = [{"key": "ABCD"[i], "text": opts[i]} for i in range(4)]
        q["answer"] = "ABCD"[shift]
    elif raw["type"] == "choice":
        q["choices"] = raw["choices"]
        q["answer"] = solve_question(raw)
    else:
        ans = expected_numeric(raw["prompt"])
        if ans is None:
            raise SystemExit("Could not solve numeric question independently: %s %s" % (tid, raw["prompt"][:60]))
        q["answer"] = ans
    q["explanation"] = raw["explanation"]
    q["verify"] = raw["verify"]
    if q["type"] == "numeric":
        ok, detail = VQ.compare_numeric(q, ev)
    else:
        ok, detail = VQ.compare_choice(q, ev)
        # Also have the independent solver use only the prompt to check the choice key.
        if ok and not raw.get("_numchoice"):
            if solve_question(q) != q["answer"]:
                ok, detail = False, "solve_question does not match answer"
        elif ok and raw.get("_numchoice"):
            solved = solve_question(q)
            if solved != q["answer"]:
                ok, detail = False, "Choice result mismatch: solved %s, answer %s" % (solved, q["answer"])
    if not ok:
        raise SystemExit("%s: validation failed: %s\n  %s" % (q["id"], detail, q["prompt"][:80]))
    return q


def reachable(graph, start_topic, skip, hard_only):
    """Follow prerequisites from start_topic and return reachable prerequisite IDs, excluding itself."""
    seen = set()
    stack = []
    for pre, strength in graph.get(start_topic, []):
        if (start_topic, pre) == skip:
            continue
        if hard_only and strength != "hard":
            continue
        stack.append(pre)
    while stack:
        node = stack.pop()
        if node in seen:
            continue
        seen.add(node)
        for pre, strength in graph.get(node, []):
            if hard_only and strength != "hard":
                continue
            if pre not in seen:
                stack.append(pre)
    return seen


def reduce_new(edges, new_keys):
    """Remove only new edges, testing each against the full graph with that edge removed."""
    graph = defaultdict(list)
    for e in edges:
        graph[e["topicId"]].append((e["prerequisiteId"], e["strength"]))
    drop = set()
    for e in edges:
        key = (e["topicId"], e["prerequisiteId"])
        if key not in new_keys:
            continue
        if e["strength"] == "hard":
            hit = reachable(graph, e["topicId"], key, True)
        else:
            hit = reachable(graph, e["topicId"], key, False)
        if e["prerequisiteId"] in hit:
            drop.add(key)
    kept = [e for e in edges if (e["topicId"], e["prerequisiteId"]) not in drop]
    return kept, len(drop)


def main():
    catalog = T12 + T34 + T46 + T56
    by_slug = {}
    for i, t in enumerate(catalog):
        if t["slug"] in by_slug:
            raise SystemExit("Duplicate slug: " + t["slug"])
        by_slug[t["slug"]] = t
        t["_i"] = i

    topics_raw = load("topics.json")
    deps_raw = load("dependencies.json")
    questions_raw = load("questions.json")
    standards_raw = load("cn-curriculum-standards.json")

    junior_topics = [t for t in topics_raw if is_junior_id(t.get("id"))]
    junior_snap = copy.deepcopy(junior_topics)
    junior_ids = {t["id"] for t in junior_topics}
    if len(junior_topics) != 315:
        raise SystemExit("Expected 315 official junior-high topics, found %d" % len(junior_topics))

    junior_deps = [d for d in deps_raw
                   if is_junior_id(d.get("topicId")) and is_junior_id(d.get("prerequisiteId"))]
    junior_dep_snap = copy.deepcopy(junior_deps)
    # Protect cnm_221: its edges must not change.
    cnm_221_before = [(d["prerequisiteId"], d["strength"]) for d in deps_raw if d["topicId"] == "cnm_221"]

    ext_edges = [d for d in deps_raw
                 if str(d.get("topicId", "")).startswith("cnm_ext_") or str(d.get("prerequisiteId", "")).startswith("cnm_ext_")]
    # On the first run, verify strengths against the original edges; on later runs, those edges are no longer in the file.
    if ext_edges:
        seen_retarget = {}
        for d in ext_edges:
            if str(d["topicId"]).startswith("cnm_ext_"):
                continue
            seen_retarget[(d["topicId"], d["prerequisiteId"])] = d["strength"]
        if set(seen_retarget) != set(RETARGET):
            missing = set(seen_retarget) - set(RETARGET)
            extra = set(RETARGET) - set(seen_retarget)
            raise SystemExit("Retargeting table does not match existing edges: missing=%s extra=%s" % (missing, extra))

    # Original edge reasons and strengths: read them from the file when possible; the first run must be able to read them.
    orig_meta = {}
    if ext_edges:
        for d in ext_edges:
            if is_junior_id(d["topicId"]):
                orig_meta[(d["topicId"], d["prerequisiteId"])] = (d["strength"], d["reason"])
    else:
        # On reruns, this script cannot recover the original text, and strengths are not stored according to the RETARGET convention.
        # Refuse to overwrite reasons when the caller cannot preserve them; existing edges to primary topics are indistinguishable here.
        raise SystemExit("dependencies.json no longer contains cnm_ext_* edges. Compile once using the original graph with external nodes; to rebuild, first restore data/dependencies.json and data/topics.json with git checkout.")

    primary_topics = []
    primary_questions = []
    slug_to_id = {}
    for i, t in enumerate(catalog, start=1):
        tid = "cnm_p%03d" % i
        slug_to_id[t["slug"]] = tid
        qs = [build_question(raw, tid, n) for n, raw in enumerate(t["qs"], start=1)]
        q1 = qs[0]
        if q1["type"] == "choice":
            diag_answer = next(c["text"] for c in q1["choices"] if c["key"] == q1["answer"])
        else:
            diag_answer = q1["answer"]
        node = {
            "id": tid,
            "name": t["name"],
            "domain": t["domain"],
            "grade": t["grade"],
            "semester": t["semester"],
            "chapter": chapter_of(t),
            "type": t["type"],
            "description": t["description"],
            "mastery_criteria": list(t["mastery_criteria"]),
            "diagnostic_question": {"question": q1["prompt"], "answer": diag_answer},
            "external": False,
            "standards": standards_of(t["standards"]),
        }
        if t.get("root_reason"):
            node["root_reason"] = t["root_reason"]
        primary_topics.append(node)
        primary_questions.extend(qs)

    id_to_topic = {t["id"]: t for t in primary_topics}
    id_to_topic.update({t["id"]: t for t in junior_topics})

    new_edges = []
    for t in catalog:
        tid = slug_to_id[t["slug"]]
        for pre in t["pre"]:
            if isinstance(pre, tuple):
                slug, strength = pre
            else:
                slug, strength = pre, "hard"
            if slug not in slug_to_id:
                raise SystemExit("%s: prerequisite %s does not exist" % (t["slug"], slug))
            pid = slug_to_id[slug]
            if slug_to_id and catalog[by_slug[slug]["_i"]]["_i"] >= t["_i"]:
                raise SystemExit("%s: prerequisite %s does not appear earlier" % (t["slug"], slug))
            new_edges.append({
                "topicId": tid,
                "prerequisiteId": pid,
                "strength": strength,
                "reason": primary_reason(t, by_slug[slug], strength),
            })

    for (jid, ext), slugs in RETARGET.items():
        strength, reason = orig_meta[(jid, ext)]
        jname = next(t["name"] for t in junior_topics if t["id"] == jid)
        for slug in slugs:
            pid = slug_to_id[slug]
            pname = by_slug[slug]["name"]
            text = reason if reason.endswith("。") else reason + "。"
            new_edges.append({
                "topicId": jid,
                "prerequisiteId": pid,
                "strength": strength,
                "reason": 'Learning "%s" requires first learning the primary-school topic "%s". %s' % (jname, pname, text),
            })

    # Grade order is monotonic: a prerequisite cannot be in a later grade than its topic.
    for e in new_edges + junior_deps:
        a = id_to_topic[e["topicId"]]
        b = id_to_topic[e["prerequisiteId"]]
        if grade_rank(b["grade"], b["semester"]) > grade_rank(a["grade"], a["semester"]):
            raise SystemExit("Grade order regresses: %s(%s%s) depends on %s(%s%s)" % (
                a["id"], a["grade"], a["semester"], b["id"], b["grade"], b["semester"]))

    all_edges = new_edges + junior_deps
    new_keys = {(e["topicId"], e["prerequisiteId"]) for e in new_edges}
    # Duplicate edges.
    seen = set()
    for e in all_edges:
        k = (e["topicId"], e["prerequisiteId"])
        if k in seen:
            raise SystemExit("Duplicate edge %s <- %s" % k)
        seen.add(k)
    reduced, n_drop = reduce_new(all_edges, new_keys)

    # Aliases.
    alias_obj = {
        "description": "Plan B: the 18 cnm_ext_* IDs have been removed from topics.json and are no longer nodes. When diagnosis or browsing encounters a legacy ID (for example, ?target=cnm_ext_002), use targets to navigate to the corresponding official primary-school topics. These are representative topics covered by the external node, not an exhaustive list.",
        "aliases": {},
    }
    for key, name, slugs in ALIASES:
        alias_obj["aliases"][key] = {"name": name, "targets": [slug_to_id[s] for s in slugs]}

    # Curriculum standards: place primary-school items before Stage 4 and leave Stage 4 item objects unchanged.
    stage4 = [it for it in standards_raw["items"] if isinstance(it, dict) and str(it.get("id", "")).startswith("cms-2022:4.")]
    if len(stage4) != 157:
        raise SystemExit("Expected 157 Stage 4 items, found %d" % len(stage4))
    stage4_snap = copy.deepcopy(stage4)
    src = standards_raw["source"]
    src["stage"] = "Stages 1–4 (Grades 1–9)"
    src["retrieved"] = "2026-10-17 (Stage 4); 2026-10-19 (Stages 1–3)"
    extra = ("Stages 1–3 were compiled from publicly available transcriptions (21st Century Education Network preview http://zy.21cnjy.com/20610065, accessed 2026-10-19); "
             "they were not checked page by page against the Ministry of Education PDF, page_or_ref is \"to be verified\", and verbatim is false. "
             "Stage 4 item text is unchanged.")
    if extra not in src.get("note", ""):
        src["note"] = src.get("note", "").rstrip() + extra
    standards_raw["items"] = list(PRIMARY_ITEMS) + stage4

    topics_out = primary_topics + junior_topics
    questions_out = primary_questions + [q for q in questions_raw if is_junior_id(q.get("topicId"))]
    if len(questions_out) - len(primary_questions) != 1407:
        raise SystemExit("Expected to retain 1,407 junior-high questions, found %d" % (len(questions_out) - len(primary_questions)))

    # Deep comparisons: junior-high objects must remain unchanged.
    if junior_topics != junior_snap:
        raise SystemExit("Junior-high topic objects were changed")
    if junior_deps != junior_dep_snap:
        raise SystemExit("Prerequisite edges between junior-high topics were changed")
    if stage4 != stage4_snap:
        raise SystemExit("Stage 4 curriculum-standard items were changed")
    cnm_221_after = [(d["prerequisiteId"], d["strength"]) for d in reduced if d["topicId"] == "cnm_221"]
    if cnm_221_after != cnm_221_before:
        raise SystemExit("cnm_221 edges were changed: %s -> %s" % (cnm_221_before, cnm_221_after))

    dump("topics.json", topics_out, 2)
    dump("dependencies.json", reduced, 2)
    dump("questions.json", questions_out, 1)
    dump("cn-curriculum-standards.json", standards_raw, 2)
    dump("id-aliases.json", alias_obj, 2)

    # Write batches by grade for easier review; the merged result is in questions.json.
    os.makedirs(os.path.join(DATA, "_qbatches"), exist_ok=True)
    by_grade = defaultdict(list)
    for q in primary_questions:
        g = id_to_topic[q["topicId"]]["grade"]
        by_grade[g].append(q)
    for g, qs in sorted(by_grade.items()):
        dump("_qbatches/primary_g%d.json" % g, qs, 1)

    # Independent review record; do not overwrite the junior-high second_pass field.
    log_path = os.path.join(DATA, "second_pass_log.json")
    with open(log_path, encoding="utf-8") as f:
        log = json.load(f)
    disagree = []
    by_type = Counter()
    for q in primary_questions:
        by_type[q["type"]] += 1
        got = solve_question(q)
        if got != q["answer"]:
            # Keep these legacy Chinese keys to preserve the mismatch-log object shape.
            disagree.append({"id": q["id"], "独立答案": got, "题库答案": q["answer"]})
    # The full-width C prefix is a structural token used to replace this review pass on rebuilds.
    passes = [p for p in log.get("passes", []) if not str(p.get("name", "")).startswith("C：")]
    passes.append({
        "name": "C：Independent review of primary-school questions (primary_recheck; reads only prompts and choices, not answer / verify / explanation)",
        "solver": "scripts/primary_recheck.py",
        "questions": len(primary_questions),
        "by_type": dict(by_type),
        "disagreements": len(disagree),
        "adjudication": "Resolve disagreements by updating the catalog before compiling; none in this run" if not disagree else "See primary_disagreements",
    })
    log["passes"] = passes
    log["primary_checked"] = len(primary_questions)
    log["primary_disagreements"] = disagree
    log["second_pass_mismatch"] = log.get("second_pass_mismatch") or []
    if disagree:
        log["second_pass_mismatch"] = disagree
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(log, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print("Primary-school topics: %d" % len(primary_topics), Counter(t["grade"] for t in primary_topics))
    print("New edges (before reduction): %d; redundant edges removed: %d; edges written: %d (junior-high to junior-high: %d)" % (
        len(new_edges), n_drop, len(reduced), len(junior_deps)))
    print("Primary-school questions: %d" % len(primary_questions), Counter(q["type"] for q in primary_questions),
          Counter(q["difficulty"] for q in primary_questions))
    print("Curriculum standards: %d (primary school: %d + Stage 4: %d)" % (len(standards_raw["items"]), len(PRIMARY_ITEMS), len(stage4)))
    print("Review disagreements: %d" % len(disagree))
    if disagree:
        raise SystemExit(disagree[:10])


if __name__ == "__main__":
    main()
