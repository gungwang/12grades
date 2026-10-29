#!/usr/bin/env python3
"""Validate data/topics.json and data/dependencies.json using only the standard library.

Usage: python3 scripts/validate.py
Prints "VALIDATION PASSED" and exits with status 0 on success; otherwise exits with status 1.

Curriculum-standard alignment (data/cn-curriculum-standards.json):
- If the file exists, every topic.standards[].id must appear in items[].id, and confidence must be exact or inferred.
- Empty standards on core topics produce a WARNING (listing at most 30) and do not affect the exit status.
  Set STRICT_STANDARDS=1 to treat empty standards as errors.
"""
import json
import os
import re
import sys
from collections import Counter, defaultdict
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_figures import question_figure_problems  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOPICS_PATH = os.path.join(ROOT, "data", "topics.json")
DEPS_PATH = os.path.join(ROOT, "data", "dependencies.json")
STANDARDS_PATH = os.path.join(ROOT, "data", "cn-curriculum-standards.json")
QUESTIONS_PATH = os.path.join(ROOT, "data", "questions.json")
STRICT_STANDARDS = os.environ.get("STRICT_STANDARDS") == "1"

# Chinese subject/domain labels and semester markers are schema values used by the data builders and this validator; keep them unchanged.
MATH_DOMAINS = {"数与代数", "图形与几何", "统计与概率", "综合与实践"}
EN_DOMAINS = {"语音", "词汇", "语法", "日常表达", "读写"}
ZH_DOMAINS = {"拼音", "识字写字", "词语", "句子", "阅读理解", "古诗文积累", "习作基础"}
# Physics-topic domains use the curriculum's top-level themes; "Experimental inquiry" appears only in standard entries.
PHY_DOMAINS = {"物质", "运动和相互作用", "能量", "跨学科实践"}
PHY_STD_TOPS = {"1": "物质", "2": "运动和相互作用", "3": "能量", "4": "实验探究", "5": "跨学科实践"}
PHY_STD_ID_RE = re.compile(r"^cps-2022:([1-5])\.(\d)\.(\d+)$")
# Senior-high physics standards: cps-hs-2017:<B required|S elective required><volume 1-3>.<theme 1-4 or X student-required experiment>.<number>
PHY_HS_STD_ID_RE = re.compile(r"^cps-hs-2017:([BS])([1-3])\.([1-4X])\.(\d+)$")
PHY_HS_STD_DOMAINS = {"物质", "运动和相互作用", "能量", "实验探究", "跨学科实践"}
PHY_SENIOR_GRADES = (10, 11, 12, 13, 14, 15)
DOMAINS = MATH_DOMAINS | EN_DOMAINS | PHY_DOMAINS | ZH_DOMAINS
TYPES = {"conceptual", "procedural", "reasoning", "application", "modeling"}
STRENGTHS = {"hard", "soft"}
CONFIDENCES = {"exact", "inferred"}
MAX_STANDARDS_PER_TOPIC = 3
MAX_WARNINGS_LISTED = 30
STD_DOMAIN_CODES = {"NA": "数与代数", "GG": "图形与几何", "SP": "统计与概率", "IP": "综合与实践"}
STD_ID_RE = re.compile(r"^cms-2022:([1-4])\.(NA|GG|SP|IP)\.(\d{2,})$")
# Senior-high required math: cms-2017:H.<module>.NN. Modules are not domain codes (geometry and algebra span number/algebra and geometry).
HS_STD_ID_RE = re.compile(r"^cms-2017:H\.(PRE|FUN|GA|PS|MI)\.(\d{2,})$")
HS_STD_MODULES = ("PRE", "FUN", "GA", "PS", "MI")
EN_STD_CODES = {"PH": "语音", "VO": "词汇", "GR": "语法", "FU": "日常表达", "RW": "读写"}
EN_STD_ID_RE = re.compile(r"^ces-2022:([123])\.(PH|VO|GR|FU|RW)\.(\d{2,})$")
# Senior-high English: ces-2017:H.B is required and ces-2017:H.S is elective required. IDs are assigned by this graph.
EN_HS_STD_ID_RE = re.compile(r"^ces-2017:H\.(B|S)\.(PH|VO|GR|FU|RW)\.(\d{2,})$")
# Elementary Chinese language arts: ccs-2022:<stage 1–3>.<PY|SZ|CY|JZ|YD|GS|XZ>.<NN>. IDs are assigned by this graph.
ZH_STD_CODES = {
    "PY": "拼音", "SZ": "识字写字", "CY": "词语", "JZ": "句子",
    "YD": "阅读理解", "GS": "古诗文积累", "XZ": "习作基础",
}
ZH_STD_ID_RE = re.compile(r"^ccs-2022:([123])\.(PY|SZ|CY|JZ|YD|GS|XZ)\.(\d{2,})$")
# English labels are for reports only; the Chinese domain values above remain schema values.
DOMAIN_LABELS = {
    "数与代数": "Number and algebra",
    "图形与几何": "Geometry",
    "统计与概率": "Statistics and probability",
    "综合与实践": "Integrated practice",
    "语音": "Pronunciation",
    "词汇": "Vocabulary",
    "语法": "Grammar",
    "日常表达": "Everyday expressions",
    "读写": "Reading and writing",
    "拼音": "Pinyin",
    "识字写字": "Character recognition and handwriting",
    "词语": "Words and phrases",
    "句子": "Sentences",
    "阅读理解": "Reading comprehension",
    "古诗文积累": "Classical Chinese and poetry",
    "习作基础": "Writing",
    "物质": "Matter",
    "运动和相互作用": "Motion and interactions",
    "能量": "Energy",
    "实验探究": "Experimental inquiry",
    "跨学科实践": "Interdisciplinary practice",
}
# Keep these Chinese fragments: this validator rejects them in English prompts to catch untranslated references.
EN_PROMPT_START_RE = re.compile(r"^(同一|上题|该题|同上)")
EN_PROMPT_BAN_RE = re.compile(r"本知识点|课标|是否要求")
CORE_FIELDS = ["id", "name", "domain", "grade", "semester", "chapter", "type",
               "description", "mastery_criteria", "diagnostic_question", "external"]
EXT_FIELDS = ["id", "name", "domain", "grade", "description", "external"]
# cnm_001 is a core middle-school topic; cnm_p001 is elementary; cnm_h001 is senior high. cne_p/j/h identify elementary/middle/senior-high English.
# cnp_001 is middle-school physics; cnp_h001 is senior-high physics (required 1 through elective-required 3, grades 10–15). cnc_p001 is elementary Chinese language arts.
ID_RE = re.compile(r"^(?:cnm_(?:p|h)?|cne_[pjh]|cnp_h?|cnc_p)\d{3,}$")
# Grades 10–11 represent required volumes 1–2; grades 12–14 represent elective-required volumes 1–3, not school years.
GRADES = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
ALIASES_PATH = os.path.join(ROOT, "data", "id-aliases.json")
ALIAS_ID_RE = re.compile(r"^cnm_ext_\d{3,}$")
# Optional textbook-edition mappings: topic.mappings and data/mappings/*.json; see docs/edition-mappings.md.
MAPPINGS_DIR = os.path.join(ROOT, "data", "mappings")
EDITION_KEY_RE = re.compile(r"^[a-z][a-z0-9]*(?:_[a-z0-9]+)*$")
# Renjiao editions are reserved because Renjiao is represented by the topic's own grade/semester/chapter.
EDITION_RESERVED = {"renjiao_math", "pep_math"}
# Preserve these Chinese values: check_mapping_entry validates them as serialized semester tokens in topic mappings.
MAPPING_TERMS = ("上", "下", "全")
MAPPING_ENTRY_FIELDS = {"grade", "term", "unit", "chapter", "note"}
MAPPING_FILE_STATUS = ("example", "draft", "reviewed")

errors = []
warnings = []
N_PHY_EDGES = 0


def err(msg):
    errors.append(msg)


def load(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        err("File not found: %s" % path)
    except json.JSONDecodeError as e:
        err("Invalid JSON: %s (%s)" % (path, e))
    return None


def nonempty_str(v):
    return isinstance(v, str) and v.strip() != ""


def is_english_id(tid):
    return str(tid).startswith("cne_")


def is_physics_id(tid):
    return str(tid).startswith("cnp_")


def is_physics_senior_id(tid):
    return str(tid).startswith("cnp_h")


def is_chinese_id(tid):
    return str(tid).startswith("cnc_")


def topic_subject(tid):
    if is_english_id(tid):
        return "english"
    if is_physics_id(tid):
        return "physics"
    if is_chinese_id(tid):
        return "chinese"
    if str(tid).startswith("cnm_"):
        return "math"
    return ""


def volume_rank(topic):
    grade = topic.get("grade")
    if not isinstance(grade, int):
        return None
    return grade * 2 + (1 if topic.get("semester") == "下" else 0)


def physics_rank(topic):
    """Rank middle-school physics (grades 8–9) before senior-high physics (cnp_h, grades 10–15); prerequisites cannot come later."""
    g = topic.get("grade")
    if not isinstance(g, int):
        return None
    return 100 + g if is_physics_senior_id(topic.get("id")) else g


def english_prompt_problem(text):
    s = str(text or "").strip()
    if EN_PROMPT_START_RE.match(s):
        return "Prompt must not begin with a cross-reference to the same item, previous question, that question, or the item above"
    if EN_PROMPT_BAN_RE.search(s):
        return "Prompt must not refer to this topic, curriculum standards, or whether something is required"
    return ""


def check_mapping_entry(m, where):
    """Validate one textbook-edition mapping: {grade, term, unit?, chapter?, note?}. grade is an integer; term is a serialized semester value."""
    if not isinstance(m, dict):
        err("%s must be an object" % where)
        return
    for k in m:
        if k not in MAPPING_ENTRY_FIELDS:
            err("%s has unknown field %s (allowed: %s)" % (where, k, ", ".join(sorted(MAPPING_ENTRY_FIELDS))))
    g = m.get("grade")
    if not (isinstance(g, int) and not isinstance(g, bool) and g in GRADES):
        err("%s grade must be an integer from 1 to 14" % where)
    if m.get("term") not in MAPPING_TERMS:
        err("%s term must be first semester, second semester, or full year" % where)
    for k in ("unit", "chapter", "note"):
        if k in m and not nonempty_str(m[k]):
            err("%s %s, if present, must be a non-empty string" % (where, k))


def check_mappings(maps, where):
    """Validate optional topic.mappings, shaped as {edition_key: mapping}; omission means only the Renjiao edition."""
    if not (isinstance(maps, dict) and maps):
        err("%s mappings must be a non-empty object (omit the field when there is no mapping)" % where)
        return
    for key, m in maps.items():
        if not (isinstance(key, str) and EDITION_KEY_RE.match(key)):
            err("%s mappings has an invalid edition key %r (use lowercase letters, digits, and underscores, e.g. hujiao_math)" % (where, key))
        elif key in EDITION_RESERVED:
            err("%s mappings must not include the Renjiao edition (%s); it is represented by the topic’s own grade/semester/chapter" % (where, key))
        check_mapping_entry(m, "%s mappings.%s" % (where, key))


def check_mapping_files(ids):
    """Validate contributed mapping files in data/mappings/*.json. A missing or empty directory is valid. Return (file_count, entry_count)."""
    if not os.path.isdir(MAPPINGS_DIR):
        return 0, 0
    n_files = n_entries = 0
    for fn in sorted(os.listdir(MAPPINGS_DIR)):
        if not fn.endswith(".json"):
            continue
        n_files += 1
        where = "data/mappings/%s" % fn
        data = load(os.path.join(MAPPINGS_DIR, fn))
        if not isinstance(data, dict):
            err("%s top level must be an object" % where)
            continue
        edition = data.get("edition")
        if not (isinstance(edition, str) and EDITION_KEY_RE.match(edition)) or edition in EDITION_RESERVED:
            err("%s has an invalid edition: %r" % (where, edition))
        elif not fn.startswith(edition + "."):
            err("%s filename must start with edition (%s)" % (where, edition))
        if not nonempty_str(data.get("label")):
            err("%s is missing label (edition name)" % where)
        status = data.get("status")
        if status not in MAPPING_FILE_STATUS:
            err("%s status must be %s" % (where, " / ".join(MAPPING_FILE_STATUS)))
        if ".example." in fn and status != "example":
            err("%s is an example file and must have status example" % where)
        if status == "example" and ".example." not in fn:
            err("%s has status example, so the filename must be <edition>.example.json" % where)
        if status in ("draft", "reviewed") and not nonempty_str(data.get("source")):
            err("%s non-example files must state the mapping basis in source" % where)
        entries = data.get("entries")
        if not (isinstance(entries, list) and entries):
            err("%s entries must be a non-empty array" % where)
            continue
        if status == "example" and len(entries) > 10:
            err("%s example file may contain at most 10 entries; found %d" % (where, len(entries)))
        seen = set()
        for i, e in enumerate(entries):
            ew = "%s entries[%d]" % (where, i)
            if not isinstance(e, dict):
                err("%s is not an object" % ew)
                continue
            tid = e.get("topicId")
            t = ids.get(tid)
            if t is None:
                err("%s topicId does not exist: %r" % (ew, tid))
            elif t.get("external") or topic_subject(tid) != "math":
                err("%s may map only to core math topics: %s" % (ew, tid))
            if tid in seen:
                err("%s has a duplicate topicId: %s" % (ew, tid))
            seen.add(tid)
            check_mapping_entry({k: v for k, v in e.items() if k != "topicId"}, ew)
            n_entries += 1
    return n_files, n_entries


def check_topics(topics):
    ids = {}
    if not isinstance(topics, list):
        err("topics.json top level must be an array")
        return ids
    for i, t in enumerate(topics):
        where = "topics[%d]" % i
        if not isinstance(t, dict):
            err("%s is not an object" % where)
            continue
        tid = t.get("id")
        if not nonempty_str(tid):
            err("%s is missing id" % where)
            continue
        where = "%s(%s)" % (tid, t.get("name", "?"))
        if tid in ids:
            err("Duplicate ID: %s" % tid)
        ids[tid] = t
        if not ID_RE.match(tid):
            err("%s has an invalid ID format" % where)
        ext = t.get("external")
        if not isinstance(ext, bool):
            err("%s external must be a boolean" % where)
            continue
        if ext != ("_ext_" in tid):
            err("%s external value does not match the ID prefix" % where)
        fields = EXT_FIELDS if ext else CORE_FIELDS
        for f in fields:
            if f not in t:
                err("%s is missing required field %s" % (where, f))
            elif f not in ("mastery_criteria", "diagnostic_question", "external") and not nonempty_str(t[f]) \
                    and not (f == "grade" and isinstance(t[f], int)):
                err("%s field %s is empty or has the wrong type" % (where, f))
        subj = topic_subject(tid)
        marked = t.get("subject")
        if subj == "english":
            if marked != "english":
                err("%s English topic subject must be english" % where)
            if t.get("domain") not in EN_DOMAINS:
                err("%s has an invalid English domain: %r" % (where, t.get("domain")))
        elif subj == "physics":
            if marked != "physics":
                err("%s physics topic subject must be physics" % where)
            if t.get("domain") not in PHY_DOMAINS:
                err("%s has an invalid physics domain: %r" % (where, t.get("domain")))
            sem_p = t.get("semester")
            if is_physics_senior_id(tid):
                if t.get("grade") not in PHY_SENIOR_GRADES:
                    err("%s senior-high physics grade must be 10–15 (10–12 are three required volumes; 13–15 are three elective-required volumes)" % where)
                if sem_p != "上":
                    err("%s senior-high physics semester must be the first semester" % where)
            else:
                if t.get("grade") not in (8, 9):
                    err("%s middle-school physics grade must be 8 or 9" % where)
                if (t.get("grade") == 8 and sem_p not in ("上", "下")) or (t.get("grade") == 9 and sem_p != "全"):
                    err("%s physics semester must be first or second semester for Grade 8, and full year for Grade 9 (Renjiao Grade 9 uses one full-year volume)" % where)
            for j, ml in enumerate(t.get("mathLinks") or []):
                if not (isinstance(ml, dict) and nonempty_str(ml.get("id")) and nonempty_str(ml.get("reason"))):
                    err("%s mathLinks[%d] must have the shape {id, reason}" % (where, j))
                elif not str(ml["id"]).startswith("cnm_"):
                    err("%s mathLinks[%d] may point only to a math topic: %s" % (where, j, ml["id"]))
            if "mathLinks" in t and not (isinstance(t["mathLinks"], list) and t["mathLinks"]):
                err("%s mathLinks must be a non-empty array" % where)
        elif subj == "chinese":
            if marked != "chinese":
                err("%s Chinese language arts topic subject must be chinese" % where)
            if t.get("domain") not in ZH_DOMAINS:
                err("%s has an invalid Chinese language arts domain: %r" % (where, t.get("domain")))
            if "mathLinks" in t:
                err("%s may include mathLinks only for physics topics" % where)
        else:
            if "mathLinks" in t:
                err("%s may include mathLinks only for physics topics" % where)
            if marked not in (None, "math"):
                err("%s math topic cannot be marked as another subject: %r" % (where, marked))
            if t.get("domain") not in MATH_DOMAINS:
                err("%s has an invalid domain value: %r" % (where, t.get("domain")))
        if "mappings" in t:
            if ext:
                err("%s external nodes must not have mappings" % where)
            else:
                check_mappings(t["mappings"], where)
        if ext:
            # Keep "小学": scripts/validate.py requires it as the serialized grade token for external elementary nodes.
            if t.get("grade") != "小学":
                err("%s external-node grade must be the elementary-school label" % where)
            continue
        g = t.get("grade")
        if subj == "english" and str(tid).startswith("cne_h"):
            if g not in (10, 11, 12, 13, 14, 15, 16):
                err("%s senior-high English grade must be 10–16 (10–12 are three required volumes; 13–16 are four elective-required volumes)" % where)
        elif subj == "physics" and is_physics_senior_id(tid):
            pass
        elif g not in GRADES:
            err("%s grade must be an integer from 1 to 14 (10–11 are the two required volumes; 12–14 are the three elective-required volumes)" % where)
        if subj == "chinese" and g not in (1, 2, 3, 4, 5, 6):
            err("%s elementary Chinese language arts grade must be 1–6" % where)
        if subj == "english":
            if str(tid).startswith("cne_p") and g not in (3, 4, 5, 6):
                err("%s elementary English grade must be 3–6" % where)
            elif str(tid).startswith("cne_j") and g not in (7, 8, 9):
                err("%s middle-school English grade must be 7–9" % where)
            elif str(tid).startswith("cne_h") and t.get("semester") != "上":
                err("%s senior-high English semester must be the first semester" % where)
        sem = t.get("semester")
        if subj == "physics":
            pass
        elif subj == "english" and t.get("grade") == 9:
            if sem not in ("上", "全"):
                err("%s Grade 9 English semester must be first semester for the new edition or full year for the older edition (the new second-semester volume has not been published)" % where)
        elif sem not in ("上", "下"):
            err("%s semester must be the first or second semester" % where)
        if t.get("type") not in TYPES:
            err("%s has an invalid type value: %r" % (where, t.get("type")))
        mc = t.get("mastery_criteria")
        if not (isinstance(mc, list) and 2 <= len(mc) <= 3 and all(nonempty_str(x) for x in mc)):
            err("%s mastery_criteria must contain 2–3 non-empty strings" % where)
        dq = t.get("diagnostic_question")
        if not (isinstance(dq, dict) and nonempty_str(dq.get("question")) and nonempty_str(dq.get("answer"))):
            err("%s diagnostic_question must contain non-empty question and answer values" % where)
        if "root_reason" in t and not nonempty_str(t["root_reason"]):
            err("%s root_reason must not be empty" % where)
        if subj in ("english", "chinese") and isinstance(t.get("diagnostic_question"), dict):
            problem = english_prompt_problem(t["diagnostic_question"].get("question"))
            if problem:
                err("%s diagnostic question %s" % (where, problem))
    return ids


def check_deps(deps, ids):
    prereqs = defaultdict(list)   # topic -> [prerequisite]
    dependents = defaultdict(list)
    seen = set()
    n_hard = n_soft = n_en_hard = n_en_soft = 0
    global N_PHY_EDGES
    N_PHY_EDGES = 0
    if not isinstance(deps, list):
        err("dependencies.json top level must be an array")
        return prereqs, dependents, 0, 0, 0, 0
    for i, d in enumerate(deps):
        where = "dependencies[%d]" % i
        if not isinstance(d, dict):
            err("%s is not an object" % where)
            continue
        a, b = d.get("topicId"), d.get("prerequisiteId")
        for f in ("topicId", "prerequisiteId", "strength", "reason"):
            if not nonempty_str(d.get(f)):
                err("%s is missing required field %s or its value is empty" % (where, f))
        if a not in ids:
            err("%s topicId does not exist: %r" % (where, a))
        if b not in ids:
            err("%s prerequisiteId does not exist: %r" % (where, b))
        if a == b:
            err("%s has a self-loop: %r" % (where, a))
        if d.get("strength") not in STRENGTHS:
            err("%s has an invalid strength value: %r" % (where, d.get("strength")))
        elif d["strength"] == "hard":
            n_hard += 1
        else:
            n_soft += 1
        sa, sb = topic_subject(a), topic_subject(b)
        if sa and sb and sa != sb:
            err("%s cross-subject edge: %s -> %s" % (where, a, b))
        if sa == "physics":
            N_PHY_EDGES += 1
        if sa == "english" and d.get("strength") in STRENGTHS:
            if d["strength"] == "hard":
                n_en_hard += 1
            else:
                n_en_soft += 1
        if sa == "english" and sb == "english" and a in ids and b in ids:
            ra, rb = volume_rank(ids[a]), volume_rank(ids[b])
            if ra is not None and rb is not None and rb > ra:
                err("%s English prerequisite is in a later grade or volume: %s depends on %s" % (where, a, b))
        if sa == "chinese" and sb == "chinese" and a in ids and b in ids:
            ra, rb = volume_rank(ids[a]), volume_rank(ids[b])
            if ra is not None and rb is not None and rb > ra:
                err("%s Chinese language arts prerequisite is in a later grade or volume: %s depends on %s" % (where, a, b))
        if sa == "physics" and sb == "physics" and a in ids and b in ids:
            ra, rb = physics_rank(ids[a]), physics_rank(ids[b])
            if ra is not None and rb is not None and rb > ra:
                err("%s physics prerequisite is in a later grade or volume: %s depends on %s" % (where, a, b))
        key = (a, b)
        if key in seen:
            err("%s has a duplicate edge: %s -> %s" % (where, a, b))
        seen.add(key)
        if a in ids and b in ids and a != b:
            prereqs[a].append(b)
            dependents[b].append(a)
    return prereqs, dependents, n_hard, n_soft, n_en_hard, n_en_soft


def find_cycle(ids, prereqs):
    WHITE, GREY, BLACK = 0, 1, 2
    color = {t: WHITE for t in ids}
    for start in ids:
        if color[start] != WHITE:
            continue
        stack = [(start, iter(prereqs.get(start, [])))]
        path = [start]
        color[start] = GREY
        while stack:
            node, it = stack[-1]
            nxt = next(it, None)
            if nxt is None:
                color[node] = BLACK
                stack.pop()
                path.pop()
                continue
            if color[nxt] == GREY:
                return path[path.index(nxt):] + [nxt]
            if color[nxt] == WHITE:
                color[nxt] = GREY
                stack.append((nxt, iter(prereqs.get(nxt, []))))
                path.append(nxt)
    return None


def check_graph(ids, prereqs, dependents):
    cyc = find_cycle(ids, prereqs)
    if cyc:
        err("Cycle detected: " + " -> ".join("%s(%s)" % (c, ids[c].get("name")) for c in cyc))
    for tid, t in ids.items():
        has_pre = bool(prereqs.get(tid))
        has_dep = bool(dependents.get(tid))
        if not t.get("external") and not has_pre and not nonempty_str(t.get("root_reason")):
            err("%s(%s) has no prerequisite edge and no root_reason" % (tid, t.get("name")))
        if not has_pre and not has_dep:
            err("%s(%s) is isolated (no prerequisites and no dependents)" % (tid, t.get("name")))


def report(ids, prereqs, dependents, n_hard, n_soft, n_en_hard, n_en_soft):
    core = [t for t in ids.values() if not t.get("external")]
    ext = [t for t in ids.values() if t.get("external")]
    math_core = [t for t in core if topic_subject(t.get("id")) == "math"]
    en_core = [t for t in core if is_english_id(t.get("id"))]
    phy_core = [t for t in core if is_physics_id(t.get("id"))]
    zh_core = [t for t in core if is_chinese_id(t.get("id"))]
    print("Topic count: %d (%d core, %d external elementary topics)" % (len(ids), len(core), len(ext)))
    print("By subject: math %d, Chinese language arts %d, English %d, physics %d" % (
        len(math_core), len(zh_core), len(en_core), len(phy_core)))
    print("\nMath core topics by domain:")
    for k, v in sorted(Counter(t["domain"] for t in math_core).items(), key=lambda x: -x[1]):
        print("  %-30s %d" % (DOMAIN_LABELS.get(k, k), v))
    print("\nMath core topics by grade and semester:")
    semesters = {"上": "Semester 1", "下": "Semester 2", "全": "Full year"}

    def vol_label(t):
        if is_physics_senior_id(t.get("id")):
            return {
                10: "Physics required volume 1", 11: "Physics required volume 2", 12: "Physics required volume 3",
                13: "Physics elective-required volume 1", 14: "Physics elective-required volume 2",
                15: "Physics elective-required volume 3",
            }.get(t["grade"], str(t["grade"]))
        if is_english_id(t.get("id")) and isinstance(t.get("grade"), int) and t["grade"] >= 10:
            return {
                10: "Required volume 1", 11: "Required volume 2", 12: "Required volume 3",
                13: "Elective-required volume 1", 14: "Elective-required volume 2",
                15: "Elective-required volume 3", 16: "Elective-required volume 4",
            }.get(t["grade"], str(t["grade"]))
        if t["grade"] == 10:
            return "High school grade 1, required volume 1"
        if t["grade"] == 11:
            return "High school grade 2, required volume 2"
        if t["grade"] == 12:
            return "Elective-required volume 1"
        if t["grade"] == 13:
            return "Elective-required volume 2"
        if t["grade"] == 14:
            return "Elective-required volume 3"
        return "Grade %s, %s" % (t["grade"], semesters.get(t["semester"], t["semester"]))

    c = Counter(vol_label(t) for t in math_core)
    order = [
        "Grade 1, Semester 1", "Grade 1, Semester 2", "Grade 2, Semester 1", "Grade 2, Semester 2",
        "Grade 3, Semester 1", "Grade 3, Semester 2", "Grade 4, Semester 1", "Grade 4, Semester 2",
        "Grade 5, Semester 1", "Grade 5, Semester 2", "Grade 6, Semester 1", "Grade 6, Semester 2",
        "Grade 7, Semester 1", "Grade 7, Semester 2", "Grade 8, Semester 1", "Grade 8, Semester 2",
        "Grade 9, Semester 1", "Grade 9, Semester 2", "High school grade 1, required volume 1",
        "High school grade 2, required volume 2", "Elective-required volume 1", "Elective-required volume 2",
        "Elective-required volume 3",
    ]
    for k in order:
        if c.get(k, 0) or k.startswith(("Grade 7,", "Grade 8,", "Grade 9,", "High school", "Elective-required")):
            print("  %-42s %d" % (k, c.get(k, 0)))
    n_pri = sum(1 for t in math_core if isinstance(t.get("grade"), int) and t["grade"] <= 6)
    n_jun = sum(1 for t in math_core if isinstance(t.get("grade"), int) and 7 <= t["grade"] <= 9)
    n_req = sum(1 for t in math_core if t.get("grade") in (10, 11))
    n_sel = sum(1 for t in math_core if isinstance(t.get("grade"), int) and t["grade"] >= 12)
    print("By grade band: elementary (1–6) %d, middle school (7–9) %d, high-school required (10–11) %d, elective-required (12–14) %d" % (
        n_pri, n_jun, n_req, n_sel))
    if zh_core:
        print("\nChinese language arts by domain:")
        for k, v in sorted(Counter(t["domain"] for t in zh_core).items(), key=lambda x: -x[1]):
            print("  %-30s %d" % (DOMAIN_LABELS.get(k, k), v))
        print("Chinese language arts by volume:")
        zc = Counter(vol_label(t) for t in zh_core)
        for k in [
                "Grade 1, Semester 1", "Grade 1, Semester 2", "Grade 2, Semester 1", "Grade 2, Semester 2",
                "Grade 3, Semester 1", "Grade 3, Semester 2", "Grade 4, Semester 1", "Grade 4, Semester 2",
                "Grade 5, Semester 1", "Grade 5, Semester 2", "Grade 6, Semester 1", "Grade 6, Semester 2"]:
            print("  %-30s %d" % (k, zc.get(k, 0)))
    if en_core:
        print("\nEnglish by domain:")
        for k, v in sorted(Counter(t["domain"] for t in en_core).items(), key=lambda x: -x[1]):
            print("  %-30s %d" % (DOMAIN_LABELS.get(k, k), v))
        print("English by volume:")
        ec = Counter(vol_label(t) for t in en_core)
        for k in [
                "Grade 3, Semester 1", "Grade 3, Semester 2", "Grade 4, Semester 1", "Grade 4, Semester 2",
                "Grade 5, Semester 1", "Grade 5, Semester 2", "Grade 6, Semester 1", "Grade 6, Semester 2",
                "Grade 7, Semester 1", "Grade 7, Semester 2", "Grade 8, Semester 1", "Grade 8, Semester 2",
                "Grade 9, Semester 1", "Grade 9, Full year", "Required volume 1", "Required volume 2",
                "Required volume 3", "Elective-required volume 1", "Elective-required volume 2",
                "Elective-required volume 3", "Elective-required volume 4"]:
            if ec.get(k, 0) or k in (
                    "Required volume 1", "Required volume 2", "Required volume 3",
                    "Elective-required volume 1", "Elective-required volume 2",
                    "Elective-required volume 3", "Elective-required volume 4"):
                print("  %-30s %d" % (k, ec.get(k, 0)))
    if phy_core:
        print("\nPhysics by domain:")
        for k, v in sorted(Counter(t["domain"] for t in phy_core).items(), key=lambda x: -x[1]):
            print("  %-30s %d" % (DOMAIN_LABELS[k], v))
        pc = Counter(vol_label(t) for t in phy_core)
        print("Physics by volume: " + ", ".join("%s %d" % (k, pc.get(k, 0)) for k in (
            "Grade 8, Semester 1", "Grade 8, Semester 2", "Grade 9, Full year",
            "Physics required volume 1", "Physics required volume 2", "Physics required volume 3",
            "Physics elective-required volume 1", "Physics elective-required volume 2",
            "Physics elective-required volume 3")))
    print("\nCore topics by type:")
    for k, v in sorted(Counter(t["type"] for t in core).items(), key=lambda x: -x[1]):
        print("  %-12s %d" % (k, v))
    total = n_hard + n_soft
    print("\nPrerequisite edges: %d (hard %d, soft %d)" % (total, n_hard, n_soft))
    if en_core:
        print("English: %d (hard %d, soft %d); physics: %d; math: %d" % (
            n_en_hard + n_en_soft, n_en_hard, n_en_soft, N_PHY_EDGES, total - n_en_hard - n_en_soft - N_PHY_EDGES))
    roots = [t["id"] for t in core if not prereqs.get(t["id"])]
    leaves = [t["id"] for t in core if not dependents.get(t["id"])]
    print("Root topics with root_reason: %d; terminal topics with no dependents: %d" % (len(roots), len(leaves)))
    if core:
        print("Average prerequisites per core topic: %.2f" % (sum(len(prereqs.get(t["id"], [])) for t in core) / len(core)))


def check_standards_file(std):
    """Validate the curriculum-standard file and return {id: item}; return None if the file is absent."""
    if std is None:
        return None
    items_by_id = {}
    if not isinstance(std, dict):
        err("cn-curriculum-standards.json top level must be an object")
        return items_by_id
    src = std.get("source")
    if not isinstance(src, dict):
        err("cn-curriculum-standards.json is missing the source object")
    else:
        for f in ("title", "issuer", "stage", "url", "retrieved", "note"):
            if not nonempty_str(src.get(f)):
                err("source.%s is missing or empty" % f)
        if not isinstance(src.get("year"), int):
            err("source.year must be an integer")
    items = std.get("items")
    if not isinstance(items, list) or not items:
        err("cn-curriculum-standards.json items must be a non-empty array")
        return items_by_id
    last = {}
    saw_english = False
    saw_physics = False
    saw_physics_senior = False
    saw_chinese = False
    for i, it in enumerate(items):
        where = "standards.items[%d]" % i
        if not isinstance(it, dict):
            err("%s is not an object" % where)
            continue
        sid = it.get("id")
        if not nonempty_str(sid):
            err("%s is missing id" % where)
            continue
        where = "%s(%s)" % (where, sid)
        if sid in items_by_id:
            err("Duplicate curriculum-standard entry ID: %s" % sid)
        items_by_id[sid] = it
        m = STD_ID_RE.match(sid)
        hm = HS_STD_ID_RE.match(sid)
        em = EN_STD_ID_RE.match(sid)
        ehm = EN_HS_STD_ID_RE.match(sid)
        zm = ZH_STD_ID_RE.match(sid)
        pm = PHY_STD_ID_RE.match(sid)
        phm = PHY_HS_STD_ID_RE.match(sid)
        if phm:
            saw_physics_senior = True
            kind, vol, sec, num = phm.group(1), phm.group(2), phm.group(3), int(phm.group(4))
            if it.get("domain") not in PHY_HS_STD_DOMAINS:
                err("%s has an invalid domain value: %r" % (where, it.get("domain")))
            if sec == "X":
                if it.get("domain") != "实验探究":
                    err("%s domain for a student-required experiment must be Experimental inquiry" % where)
                # The English experiment prefix is part of the serialized curriculum clause format.
                if not re.match(r"^Experiment \d+$", str(it.get("clause", ""))):
                    err("%s experiment clause must have the form “Experiment N” (the original curriculum number)" % where)
            elif it.get("clause") != "%s.%s.%d" % (vol, sec, num):
                err("%s clause must be %s.%s.%d (the curriculum clause number)" % (where, vol, sec, num))
            key = ("cpshs", kind, vol, sec)
            if num != last.get(key, 0) + 1:
                err("%s numbering is not consecutive within the volume and theme (previous number: %d)" % (where, last.get(key, 0)))
            last[key] = num
            if it.get("verbatim") is not False:
                err("%s senior-high physics standard entries must explicitly set verbatim:false (publisher PDF text layer, not verified word-for-word against the printed edition)" % where)
            # "To be verified" is the required placeholder for unverified page references.
            if it.get("page_or_ref") != "To be verified":
                err("%s senior-high physics standard page_or_ref must use the required unverified-reference placeholder; do not invent page numbers" % where)
        elif pm:
            saw_physics = True
            if it.get("domain") != PHY_STD_TOPS[pm.group(1)]:
                err("%s domain does not match the top-level theme in the ID: %r" % (where, it.get("domain")))
            if it.get("clause") != "%s.%s.%s" % pm.groups():
                err("%s clause must match the clause number in the ID" % where)
            key = ("cps", pm.group(1), pm.group(2))
            if int(pm.group(3)) != last.get(key, 0) + 1:
                err("%s numbering is not consecutive within the subtopic (previous number: %d)" % (where, last.get(key, 0)))
            last[key] = int(pm.group(3))
            if it.get("verbatim") is not False:
                err("%s physics standard entries must explicitly set verbatim:false (OCR text was manually checked but not verified word-for-word against the printed edition)" % where)
        elif m:
            stage, code, num = m.group(1), m.group(2), int(m.group(3))
            if it.get("domain") != STD_DOMAIN_CODES[code]:
                err("%s domain does not match the domain code in the ID: %r" % (where, it.get("domain")))
            key = ("2022", stage, code)
            if num != last.get(key, 0) + 1:
                err("%s numbering is not consecutive within the domain (previous number: %02d)" % (where, last.get(key, 0)))
            last[key] = num
        elif hm:
            code, num = hm.group(1), int(hm.group(2))
            if it.get("domain") not in MATH_DOMAINS:
                err("%s has an invalid domain value: %r" % (where, it.get("domain")))
            key = ("2017", code)
            if num != last.get(key, 0) + 1:
                err("%s numbering is not consecutive within the module (previous number: %02d)" % (where, last.get(key, 0)))
            last[key] = num
            if it.get("verbatim") is not False:
                err("%s senior-high entries must explicitly set verbatim:false (the source was not checked page by page)" % where)
        elif em:
            saw_english = True
            level, code, num = em.group(1), em.group(2), int(em.group(3))
            if it.get("domain") != EN_STD_CODES[code]:
                err("%s domain does not match the domain code in the ID: %r" % (where, it.get("domain")))
            if level not in ("1", "2", "3"):
                err("%s English standard level must be 1, 2, or 3" % where)
            key = ("ces", level, code)
            if num != last.get(key, 0) + 1:
                err("%s numbering is not consecutive within the level and domain (previous number: %02d)" % (where, last.get(key, 0)))
            last[key] = num
            if it.get("verbatim") is not False:
                err("%s English standard entries must explicitly set verbatim:false (the source was not checked page by page)" % where)
            if it.get("page_or_ref") != "To be verified":
                err("%s English standard page_or_ref must use the required unverified-reference placeholder; do not invent page numbers" % where)
        elif ehm:
            saw_english = True
            band, code, num = ehm.group(1), ehm.group(2), int(ehm.group(3))
            if it.get("domain") != EN_STD_CODES[code]:
                err("%s domain does not match the domain code in the ID: %r" % (where, it.get("domain")))
            key = ("ces2017", band, code)
            if num != last.get(key, 0) + 1:
                err("%s numbering is not consecutive within the level and domain (previous number: %02d)" % (where, last.get(key, 0)))
            last[key] = num
            if it.get("verbatim") is not False:
                err("%s senior-high English standard entries must explicitly set verbatim:false (the source was not checked page by page)" % where)
            if it.get("page_or_ref") != "To be verified":
                err("%s senior-high English standard page_or_ref must use the required unverified-reference placeholder; do not invent page numbers" % where)
        elif zm:
            saw_chinese = True
            level, code, num = zm.group(1), zm.group(2), int(zm.group(3))
            if it.get("domain") != ZH_STD_CODES[code]:
                err("%s domain does not match the domain code in the ID: %r" % (where, it.get("domain")))
            key = ("ccs", level, code)
            if num != last.get(key, 0) + 1:
                err("%s numbering is not consecutive within the stage and domain (previous number: %02d)" % (where, last.get(key, 0)))
            last[key] = num
            if it.get("verbatim") is not False:
                err("%s Chinese language arts standard entries must explicitly set verbatim:false (the source was not checked page by page)" % where)
            if it.get("page_or_ref") != "To be verified":
                err("%s Chinese language arts standard page_or_ref must use the required unverified-reference placeholder; do not invent page numbers" % where)
        else:
            err("%s has an invalid ID format (expected cms-2022:<stage>.<NA|GG|SP|IP>.<NN>, cms-2017:H.<PRE|FUN|GA|PS|MI>.<NN>, ces-2022:<1|2|3>.<PH|VO|GR|FU|RW>.<NN>, ces-2017:H.<B|S>.<PH|VO|GR|FU|RW>.<NN>, ccs-2022:<1|2|3>.<PY|SZ|CY|JZ|YD|GS|XZ>.<NN>, cps-2022:<1-5>.<subtopic>.<sequence>, or cps-hs-2017:<B|S><1-3>.<1-4|X>.<sequence>)" % where)
        for f in ("domain", "section", "text"):
            if not nonempty_str(it.get(f)):
                err("%s field %s is missing or empty" % (where, f))
        if "verbatim" in it and not isinstance(it["verbatim"], bool):
            err("%s verbatim must be a boolean" % where)
    if saw_physics:
        phy = std.get("physics")
        if not isinstance(phy, dict):
            err("Physics standard entries exist, but the physics object is missing")
        else:
            for f in ("title", "issuer", "stage", "note", "revision"):
                if not nonempty_str(phy.get(f)):
                    err("physics.%s is missing or empty" % f)
            if not isinstance(phy.get("year"), int):
                err("physics.year must be an integer")
    if saw_physics_senior:
        phs = std.get("physics_senior")
        if not isinstance(phs, dict):
            err("Senior-high physics standard entries exist, but the physics_senior object is missing")
        else:
            for f in ("title", "issuer", "stage", "note", "revision", "url", "textbook"):
                if not nonempty_str(phs.get(f)):
                    err("physics_senior.%s is missing or empty" % f)
            if not isinstance(phs.get("year"), int):
                err("physics_senior.year must be an integer")
    if saw_english:
        eng = std.get("english")
        if not isinstance(eng, dict):
            err("English standard entries exist, but the english object is missing")
        else:
            for f in ("title", "issuer", "stage", "note"):
                if not nonempty_str(eng.get(f)):
                    err("english.%s is missing or empty" % f)
            if not isinstance(eng.get("year"), int):
                err("english.year must be an integer")
            if any(str(sid).startswith("ces-2017:H.") for sid in items_by_id):
                senior = eng.get("senior")
                if not isinstance(senior, dict):
                    err("Senior-high English standard entries exist, but english.senior is missing")
                else:
                    for f in ("title", "issuer", "url", "note"):
                        if not nonempty_str(senior.get(f)):
                            err("english.senior.%s is missing or empty" % f)
                    if senior.get("year") != 2025:
                        err("english.senior.year must be 2025 (the 2017 edition was revised in 2025)")
    if saw_chinese:
        zh = std.get("chinese")
        if not isinstance(zh, dict):
            err("Chinese language arts standard entries exist, but the chinese object is missing")
        else:
            for f in ("title", "issuer", "stage", "note"):
                if not nonempty_str(zh.get(f)):
                    err("chinese.%s is missing or empty" % f)
            if not isinstance(zh.get("year"), int):
                err("chinese.year must be an integer")
            elif zh.get("year") != 2022:
                err("chinese.year must be 2022")
    return items_by_id


def check_topic_standards(ids, std_items):
    """Validate each topic's standards and return (referenced standard IDs, core topics with no standards)."""
    cited = set()
    empty_core = []
    for tid, t in ids.items():
        where = "%s(%s)" % (tid, t.get("name"))
        core = not t.get("external")
        if "standards" not in t:
            if core:
                empty_core.append(t)
            continue
        sts = t["standards"]
        if not isinstance(sts, list):
            err("%s standards must be an array" % where)
            continue
        if not sts and core:
            empty_core.append(t)
        if len(sts) > MAX_STANDARDS_PER_TOPIC:
            err("%s has more than %d standards" % (where, MAX_STANDARDS_PER_TOPIC))
        seen = set()
        for j, s in enumerate(sts):
            sw = "%s standards[%d]" % (where, j)
            if not isinstance(s, dict):
                err("%s is not an object" % sw)
                continue
            sid = s.get("id")
            if not nonempty_str(sid):
                err("%s is missing id" % sw)
                continue
            if sid in seen:
                err("%s references curriculum-standard entry %s more than once" % (where, sid))
            seen.add(sid)
            if std_items is None:
                err("%s cites %s, but data/cn-curriculum-standards.json does not exist" % (sw, sid))
            elif sid not in std_items:
                err("%s curriculum-standard entry is not in cn-curriculum-standards.json: %s" % (sw, sid))
            else:
                cited.add(sid)
                if is_physics_id(tid) != str(sid).startswith("cps-"):
                    err("%s subject does not match the curriculum-standard entry: %s" % (sw, sid))
                elif is_physics_id(tid) and is_physics_senior_id(tid) != str(sid).startswith("cps-hs-2017:"):
                    err("%s middle-school physics may cite only cps-2022; senior-high physics may cite only cps-hs-2017: %s" % (sw, sid))
                if is_chinese_id(tid) != str(sid).startswith("ccs-"):
                    err("%s subject does not match the curriculum-standard entry: %s" % (sw, sid))
            if s.get("confidence") not in CONFIDENCES:
                err("%s confidence must be exact or inferred, got %r" % (sw, s.get("confidence")))
            if "note" in s and not nonempty_str(s["note"]):
                err("%s note must not be empty" % sw)
    return cited, empty_core


def report_standards(ids, std_items, cited, empty_core):
    core = [t for t in ids.values() if not t.get("external")]
    if std_items is None:
        print("\nCurriculum-standard alignment: data/cn-curriculum-standards.json not found; skipped")
        return
    c = Counter(it.get("domain") for it in std_items.values())
    # Keep these Chinese labels as schema keys; map them to English only for display.
    std_order = ("数与代数", "图形与几何", "统计与概率", "综合与实践",
                 "拼音", "识字写字", "词语", "句子", "阅读理解", "古诗文积累", "习作基础",
                 "语音", "词汇", "语法", "日常表达", "读写",
                 "物质", "运动和相互作用", "能量", "实验探究", "跨学科实践")
    print("\nCurriculum-standard entries: %d (%s)" % (
        len(std_items), ", ".join("%s %d" % (DOMAIN_LABELS.get(k, k), c[k]) for k in std_order if c[k])))
    n_ok = len(core) - len(empty_core)
    pct = 100.0 * n_ok / len(core) if core else 0.0
    print("Core topics with standards: %d / %d (%.1f%%); without standards: %d" % (
        n_ok, len(core), pct, len(empty_core)))
    conf = Counter(s.get("confidence") for t in core for s in t.get("standards", []) if isinstance(s, dict))
    print("Mappings: %d exact, %d inferred; topics with at least one exact mapping: %d" % (
        conf.get("exact", 0), conf.get("inferred", 0),
        sum(1 for t in core if any(isinstance(s, dict) and s.get("confidence") == "exact" for s in t.get("standards", [])))))
    print("Standards cited by at least one topic: %d / %d; uncited standards: %d" % (
        len(cited), len(std_items), len(std_items) - len(cited)))
    if empty_core:
        label = "ERROR" if STRICT_STANDARDS else "WARNING"
        print("\n%s: These core topics have no standards (%d total; listing at most %d):" % (label, len(empty_core), MAX_WARNINGS_LISTED))
        for t in empty_core[:MAX_WARNINGS_LISTED]:
            print("  %s %s" % (t["id"], t.get("name")))
        if len(empty_core) > MAX_WARNINGS_LISTED:
            print("  ... and %d more not listed" % (len(empty_core) - MAX_WARNINGS_LISTED))


# ---------------------------------------------------------------- Question bank (data/questions.json)

Q_DIFFICULTIES = ("basic", "standard", "challenge")
Q_DIFFICULTY_ALIASES = {"advanced": "challenge"}  # Legacy name, equivalent to challenge.
Q_TYPES = ("numeric", "choice", "short", "self")
Q_FIELDS = {"id", "topicId", "difficulty", "type", "prompt", "answer", "choices", "accept",
            "explanation", "verify", "unordered", "fixed_from_source", "figure", "hideChoiceText", "percent"}
# Pure integer/decimal arithmetic unrelated to a topic (excluding fraction notation a/b).
# Grades 1–6 challenge questions must not be bare "Calculate: ... = ?". Simple calculations may appear in lower-grade contexts,
# but the entire question must not be only "Calculate: 2+3=?" or "Which is the sum of 3+2?".
# The Chinese prompt markers below are parser tokens used by this validator for the existing math-question format; preserve their regexes.
PURE_ARITH_PROMPT_RE = re.compile(
    r"^(计算：)?\d+(?:\.\d+)?(?:\s*[＋+\-－×*÷]\s*\d+(?:\.\d+)?)+＝？(?:（用小数作答）)?$"
)
PURE_ARITH_CHOICE_RE = re.compile(
    r"^\d+(?:\.\d+)?(?:\s*[＋+\-－×*÷]\s*\d+(?:\.\d+)?)+ 的得数是哪一个？$"
)
CHALLENGE_BARE_CALC_RE = re.compile(r"^计算：.*＝？")
Q_ID_RE = re.compile(r"^((?:cnm_(?:p|h)?|cne_[pjh]|cnp_h?|cnc_p)\d{3,})_q([1-9]\d*)$")
NUM_RE = re.compile(r"^-?\d+(?:\.\d+)?(?:/\d+(?:\.\d+)?)?$")
MIN_QUESTIONS_PER_TOPIC = 3
MIN_AUTO_SHARE = 0.60


def parse_numeric_answer(s):
    """Parse a numeric answer into a list of Fractions; return None if invalid.
    A value may be an integer, decimal, fraction a/b, or negative number; separate multiple answers with a full-width comma (，) or an ASCII comma.
    The full-width comma is retained as a parser-supported delimiter."""
    if not isinstance(s, str):
        return None
    parts = [p.replace(" ", "") for p in re.split(r"[，,]", s)]
    out = []
    for p in parts:
        if not NUM_RE.match(p):
            return None
        try:
            out.append(Fraction(p))
        except (ValueError, ZeroDivisionError):
            return None
    return out


def question_errors(questions, topics_by_id, require_coverage=True):
    """Return (errors, statistics). With require_coverage=False, validate one batch file without requiring at least 3 questions per topic."""
    errs = []
    stats = {"total": 0, "by_type": Counter(), "by_difficulty": Counter(), "per_topic": Counter()}
    if not isinstance(questions, list):
        return ["questions.json top level must be an array"], stats
    seen = set()
    by_topic = defaultdict(list)
    for i, q in enumerate(questions):
        w = "questions[%d]" % i
        if not isinstance(q, dict):
            errs.append("%s is not an object" % w)
            continue
        qid = q.get("id")
        if not nonempty_str(qid):
            errs.append("%s is missing id" % w)
            continue
        w = qid
        if qid in seen:
            errs.append("%s has a duplicate ID" % w)
        seen.add(qid)
        m = Q_ID_RE.match(qid)
        if not m:
            errs.append("%s ID must have the form <topicId>_q<N>" % w)
        unknown = set(q) - Q_FIELDS
        if unknown:
            errs.append("%s contains unknown fields: %s" % (w, ", ".join(sorted(unknown))))
        tid = q.get("topicId")
        t = topics_by_id.get(tid) if isinstance(tid, str) else None
        if t is None:
            errs.append("%s topicId does not exist: %r" % (w, tid))
        elif t.get("external"):
            errs.append("%s topicId is an external node, which must not have questions: %s" % (w, tid))
        if m and tid != m.group(1):
            errs.append("%s ID prefix does not match topicId(%r)" % (w, tid))
        for f in ("difficulty", "type", "prompt", "answer", "explanation"):
            if not nonempty_str(q.get(f)):
                errs.append("%s field %s is missing or empty (answer must be a string)" % (w, f))
        if is_english_id(tid) or is_chinese_id(tid):
            problem = english_prompt_problem(q.get("prompt"))
            if problem:
                errs.append("%s %s" % (w, problem))
        diff, typ = q.get("difficulty"), q.get("type")
        if nonempty_str(diff) and diff not in Q_DIFFICULTIES and diff not in Q_DIFFICULTY_ALIASES:
            errs.append("%s has an invalid difficulty value: %r" % (w, diff))
        if nonempty_str(typ) and typ not in Q_TYPES:
            errs.append("%s has an invalid type value: %r" % (w, typ))
        if "accept" in q:
            acc = q["accept"]
            if not (isinstance(acc, list) and all(nonempty_str(x) for x in acc)):
                errs.append("%s accept must be a non-empty array of strings" % w)
        if "verify" in q and not nonempty_str(q["verify"]):
            errs.append("%s verify must be a non-empty string" % w)
        if "unordered" in q and not (q["unordered"] is True and typ == "numeric"):
            errs.append("%s unordered may be used only for numeric questions and must be true" % w)
        if "percent" in q and not (q["percent"] is True and typ == "numeric" and is_physics_id(tid)):
            errs.append("%s percent may be true only for physics numeric questions (answer contains the numeric percentage value)" % w)
        if "fixed_from_source" in q and not nonempty_str(q["fixed_from_source"]):
            errs.append("%s fixed_from_source must not be empty" % w)
        ans = q.get("answer")
        if typ == "choice":
            ch = q.get("choices")
            if not (isinstance(ch, list) and 3 <= len(ch) <= 4):
                errs.append("%s choice question must have 3–4 options" % w)
            else:
                keys = []
                texts = []
                for c in ch:
                    if not (isinstance(c, dict) and nonempty_str(c.get("key")) and nonempty_str(c.get("text"))
                            and set(c) <= {"key", "text", "figure"}):
                        errs.append("%s each choice must be a non-empty {key, text} object; put figures in the optional figure field" % w)
                        break
                    keys.append(c["key"])
                    texts.append(c["text"].strip())
                else:
                    if len(set(keys)) != len(keys):
                        errs.append("%s has duplicate choice keys" % w)
                    if keys != list("ABCD")[:len(keys)]:
                        errs.append("%s choice keys must be consecutive A, B, C, D: %r" % (w, keys))
                    if len(set(texts)) != len(texts):
                        errs.append("%s has duplicate choice text" % w)
                    if nonempty_str(ans) and ans not in keys:
                        errs.append("%s answer(%r) is not a choice key" % (w, ans))
        elif "choices" in q:
            errs.append("%s may include choices only for choice questions" % w)
        if typ == "numeric" and nonempty_str(ans):
            vals = parse_numeric_answer(ans)
            if vals is None:
                errs.append("%s numeric answer is not a parseable number: %r" % (w, ans))
            elif len(vals) == 1 and q.get("unordered") is True:
                errs.append("%s must not set unordered when there is only one answer" % w)
        errs.extend(question_figure_problems(q))
        if isinstance(tid, str):
            by_topic[tid].append(q)
        if nonempty_str(typ):
            stats["by_type"][typ] += 1
        if nonempty_str(diff):
            stats["by_difficulty"][diff] += 1
        stats["total"] += 1
    for tid, qs in by_topic.items():
        stats["per_topic"][tid] = len(qs)
    if require_coverage:
        for tid, t in topics_by_id.items():
            if t.get("external"):
                continue
            qs = by_topic.get(tid, [])
            if len(qs) < MIN_QUESTIONS_PER_TOPIC:
                errs.append("%s(%s) has only %d questions; at least %d are required" % (tid, t.get("name"), len(qs), MIN_QUESTIONS_PER_TOPIC))
            ds = {q.get("difficulty") for q in qs}
            if qs and not {"basic", "standard"} <= ds:
                errs.append("%s(%s) must include at least basic and standard difficulty levels" % (tid, t.get("name")))
            # Grades 1–6 math require all three difficulty levels, forbid unrelated integer/decimal arithmetic, and forbid bare "Calculate: ... = ?" challenges.
            if t.get("grade") in (1, 2, 3, 4, 5, 6) and str(tid).startswith("cnm_") and not (
                    is_english_id(tid) or is_physics_id(tid) or is_chinese_id(tid)):
                label = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6"}[t.get("grade")]
                if qs and ("standard" not in ds or "challenge" not in ds):
                    errs.append("%s(%s) Grade %s question bank must include at least one standard and one challenge question" % (
                        tid, t.get("name"), label))
                for q in qs:
                    p = str(q.get("prompt") or "").strip()
                    if PURE_ARITH_PROMPT_RE.match(p) or PURE_ARITH_CHOICE_RE.match(p):
                        errs.append("%s is an integer or decimal arithmetic question unrelated to its topic" % q.get("id"))
                    if q.get("difficulty") == "challenge" and CHALLENGE_BARE_CALC_RE.match(p):
                        errs.append("%s challenge prompt must not be a bare “Calculate: ... = ?” question" % q.get("id"))
            q1 = [q for q in qs if q.get("id") == tid + "_q1"]
            dq = (t.get("diagnostic_question") or {}).get("question")
            if qs and not q1:
                errs.append("%s is missing %s_q1 (it should be migrated from diagnostic_question)" % (tid, tid))
            elif q1 and nonempty_str(dq) and "fixed_from_source" not in q1[0] \
                    and not str(q1[0].get("prompt", "")).startswith(dq):
                errs.append("%s_q1 prompt must begin with diagnostic_question.question from topics.json" % tid)
    return errs, stats


def report_questions(stats, topics_by_id):
    core = [tid for tid, t in topics_by_id.items() if not t.get("external")]
    counts = [stats["per_topic"].get(tid, 0) for tid in core]
    print("\nQuestion bank: %d questions" % stats["total"])
    print("By type: " + ", ".join("%s %d" % (k, stats["by_type"].get(k, 0)) for k in Q_TYPES))
    print("By difficulty: " + ", ".join("%s %d" % (k, stats["by_difficulty"].get(k, 0)) for k in Q_DIFFICULTIES + ("advanced",)))
    auto = stats["by_type"].get("numeric", 0) + stats["by_type"].get("choice", 0)
    if stats["total"]:
        print("Numeric + choice share: %.1f%%" % (100.0 * auto / stats["total"]))
    if counts:
        dist = Counter(counts)
        print("Questions per topic: min %d, max %d, mean %.2f; distribution %s" % (
            min(counts), max(counts), sum(counts) / float(len(counts)),
            ", ".join("%d questions × %d" % (k, dist[k]) for k in sorted(dist))))


def check_aliases(ids):
    """Validate data/id-aliases.json: legacy cnm_ext_* IDs must map to existing core elementary topics."""
    if not os.path.exists(ALIASES_PATH):
        err("Missing data/id-aliases.json (the redirect table for legacy cnm_ext_* IDs)")
        return
    data = load(ALIASES_PATH)
    if not isinstance(data, dict):
        return
    aliases = data.get("aliases")
    if not isinstance(aliases, dict) or not aliases:
        err("id-aliases.json aliases must be a non-empty object")
        return
    for i in range(1, 19):
        key = "cnm_ext_%03d" % i
        if key not in aliases:
            err("id-aliases.json is missing legacy node %s" % key)
    for key, spec in aliases.items():
        if not ALIAS_ID_RE.match(key):
            err("Alias has an invalid ID format: %s" % key)
        if key in ids:
            err("Alias %s still exists as a topic and should appear only in id-aliases.json" % key)
        targets = spec.get("targets") if isinstance(spec, dict) else None
        if not (isinstance(targets, list) and targets):
            err("Alias %s targets must be a non-empty array" % key)
            continue
        if len(set(targets)) != len(targets):
            err("Alias %s has duplicate targets" % key)
        for tid in targets:
            t = ids.get(tid)
            if t is None:
                err("Alias %s points to a topic that does not exist: %s" % (key, tid))
            elif t.get("external") or not (isinstance(t.get("grade"), int) and t["grade"] <= 6):
                err("Alias %s must point to a core elementary topic, not %s" % (key, tid))
        if isinstance(spec, dict) and not nonempty_str(spec.get("name")):
            err("Alias %s is missing its original name" % key)


def main():
    topics = load(TOPICS_PATH)
    deps = load(DEPS_PATH)
    if topics is None or deps is None:
        for e in errors:
            print("Error: " + e)
        print("VALIDATION FAILED")
        return 1
    ids = check_topics(topics)
    check_aliases(ids)
    n_map_files, n_map_entries = check_mapping_files(ids)
    n_topic_maps = sum(1 for t in ids.values() if "mappings" in t)
    print("Optional textbook mappings: %d topics with topic.mappings; %d files and %d entries in data/mappings" % (
        n_topic_maps, n_map_files, n_map_entries))
    prereqs, dependents, n_hard, n_soft, n_en_hard, n_en_soft = check_deps(deps, ids)
    check_graph(ids, prereqs, dependents)
    std_items = None
    if os.path.exists(STANDARDS_PATH):
        std_items = check_standards_file(load(STANDARDS_PATH))
    cited, empty_core = check_topic_standards(ids, std_items)
    if STRICT_STANDARDS and std_items is not None and empty_core:
        err("STRICT_STANDARDS=1: %d core topics have no standards" % len(empty_core))
    report(ids, prereqs, dependents, n_hard, n_soft, n_en_hard, n_en_soft)
    report_standards(ids, std_items, cited, empty_core)
    if os.path.exists(QUESTIONS_PATH):
        qs = load(QUESTIONS_PATH)
        if qs is not None:
            qerrs, qstats = question_errors(qs, ids, require_coverage=True)
            for e in qerrs:
                err("Question bank: " + e)
            auto = qstats["by_type"].get("numeric", 0) + qstats["by_type"].get("choice", 0)
            if qstats["total"] and auto < MIN_AUTO_SHARE * qstats["total"]:
                err("Question bank: numeric + choice share %.1f%% < %d%%" % (100.0 * auto / qstats["total"], MIN_AUTO_SHARE * 100))
            report_questions(qstats, ids)
    else:
        print("\nQuestion bank: data/questions.json not found; skipped")
    print()
    if errors:
        for e in errors:
            print("Error: " + e)
        print("\n%d errors in total" % len(errors))
        print("VALIDATION FAILED")
        return 1
    print("VALIDATION PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
