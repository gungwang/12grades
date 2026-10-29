#!/usr/bin/env python3
"""Compile physics drafts into four files under data/: junior high (phy_g8a / phy_g8b / phy_g9) and senior high (phy_hs_a01 … a11; see phy_hs_build.py).

Safe to rerun: remove and rewrite only the section this script owns; preserve the other section.
  Junior high: cnp_NNN topics, edges, and questions; cps-2022: standards entries
  Senior high: cnp_hNNN topics, edges, and questions; cps-hs-2017: standards entries
Do not modify the mathematics or English sections. Do not create prerequisite edges between physics and mathematics (validate.py disallows cross-subject edges); use the mathLinks field on topics instead.

Usage: python3 scripts/phy_build.py                 # Rebuild junior and senior high data (senior-high prerequisites may point to junior-high topics)
       python3 scripts/phy_build.py --junior-only    # Rebuild junior high only; leave existing senior-high data unchanged
       python3 scripts/phy_build.py --senior-only    # Rebuild senior high only; leave existing junior-high data unchanged
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import phy_g8a  # noqa: E402,F401
import phy_g8b  # noqa: E402,F401
import phy_g9  # noqa: E402,F401
from phy_lib import TOPICS  # noqa: E402
from phy_std import CLAUSES, SECTIONS, TOP  # noqa: E402
from verify_questions import verify_all  # noqa: E402

# These Chinese grade labels are source keys consumed by the GRADE lookup; the semester markers are structural values passed into output records.
GRADE = {"八上": (8, "上"), "八下": (8, "下"), "九全": (9, "全")}
STD_SOURCE = {
    "title": "Compulsory Education Physics Curriculum Standards (2022 Edition, Revised 2025)",
    "issuer": "Ministry of Education of the People's Republic of China",
    "year": 2022,
    "revision": "2025 routine revision (Ministry of Education, Routine Revision of the Curriculum Plan and Curriculum Standards for Primary and Secondary Schools, Textbook [2025] No. 1)",
    "stage": "Compulsory Education, Stage 4 (Grades 8–9)",
    "section": "Curriculum Content · [Content Requirements]",
    "note": ("The provisions are taken from the scanned PDF of the 2022 edition revised in 2025, OCR-processed and manually checked against page images (a few visually similar characters were corrected). "
             "They have not been checked word for word against the printed edition, so verbatim is false; page_or_ref is the PDF page number. Standard IDs in the form cps-2022:<level-1>.<level-2>.<number> "
             "match the numbering in the original standards. The top-level theme “Experimental Inquiry” (4.1 and 4.2, required student experiments) is represented only as a standards entry; topic domains are limited to "
             "Matter, Motion and Interactions, Energy, and Interdisciplinary Practice. The textbooks are the People's Education Press editions revised for the 2022 curriculum standards: Grade 8, Book 1 (2024), "
             "Grade 8, Book 2 (2025), and Grade 9, full year (2025); topics follow the table of contents down to the lesson level."),
    "retrieved": "2026-10-22",
}


def load(name):
    with open(os.path.join(ROOT, "data", name), encoding="utf-8") as f:
        return json.load(f)


def dump(name, data):
    with open(os.path.join(ROOT, "data", name), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def slot(key, i):
    return int(hashlib.md5(("%s#%d" % (key, i)).encode()).hexdigest(), 16) % 4


JR_TOPIC = re.compile(r"^cnp_\d")
SR_TOPIC = re.compile(r"^cnp_h\d")


def _drop(items, key, rx):
    keep, old = [], []
    for it in items:
        (old if rx.match(str(it.get(key, ""))) else keep).append(it)
    return keep, old


def build_junior(math_ids, id_of, order, name_of):
    std_items = []
    for cid, text, page in CLAUSES:
        top, sec, num = cid.split(".")
        std_items.append({
            "id": "cps-2022:%s" % cid,
            "domain": TOP[top],
            "section": "%s.%s %s" % (top, sec, SECTIONS["%s.%s" % (top, sec)]),
            "clause": cid,
            "text": text,
            "page_or_ref": "PDF page %d" % page,
            "verbatim": False,
            "text_status": "Scanned PDF, OCR-processed and manually proofread; not checked word for word against the printed edition",
        })
    std_ids = {it["id"] for it in std_items}
    new_topics, new_deps, new_qs = [], [], []
    errs = []
    for t in TOPICS:
        tid = id_of[t["key"]]
        vol, chn, chname, secno = t["sec"]
        g, s = GRADE[vol]
        assert " " not in chname, chname
        q1 = t["qs"][0]
        topic = {
            "id": tid, "name": t["name"], "domain": t["domain"], "grade": g, "semester": s,
            "chapter": "%s %s %s %s" % (vol, chn, chname, secno), "type": t["type"],
            "description": t["description"], "mastery_criteria": t["mastery"],
            "diagnostic_question": {"question": q1["prompt"],
                                    "answer": q1["right"] if q1["kind"] == "choice" else q1["answer"]},
            "external": False, "subject": "physics",
            "standards": [{"id": "cps-2022:%s" % c, "confidence": conf} for c, conf in t["std"]],
        }
        for sref in topic["standards"]:
            if sref["id"] not in std_ids:
                errs.append("%s references a nonexistent standard %s" % (tid, sref["id"]))
        if t["math"]:
            links = []
            for mid, reason in t["math"]:
                if mid not in math_ids:
                    errs.append("%s has a mathLink to nonexistent mathematics topic %s" % (tid, mid))
                links.append({"id": mid, "reason": reason})
            topic["mathLinks"] = links
        if t["root"]:
            topic["root_reason"] = t["root"]
        if not t["pre"] and not t["root"]:
            errs.append("%s has neither a prerequisite nor a root" % tid)
        new_topics.append(topic)
        for pk, strength in t["pre"]:
            if order[pk] >= order[t["key"]]:
                errs.append("%s has prerequisite %s after it in the sequence" % (tid, pk))
            reason = ("To learn “%s,” first understand “%s.”" if strength == "hard" else "“%s” uses knowledge from “%s.”") % (
                t["name"], name_of[pk])
            new_deps.append({"topicId": tid, "prerequisiteId": id_of[pk], "strength": strength, "reason": reason})
        if len(t["qs"]) != 4:
            errs.append("%s does not have 4 questions" % tid)
        for i, q in enumerate(t["qs"], 1):
            qid = "%s_q%d" % (tid, i)
            if q["kind"] == "numeric":
                obj = {"id": qid, "topicId": tid, "difficulty": q["diff"], "type": "numeric", "prompt": q["prompt"],
                       "answer": q["answer"], "explanation": q["expl"], "verify": q["verify"]}
                if q.get("percent"):
                    obj["percent"] = True
            else:
                texts = list(q["wrongs"])
                if len(set(texts + [q["right"]])) != len(texts) + 1:
                    errs.append("%s has duplicate choices" % qid)
                pos = q["pos"] if q["pos"] is not None else slot(t["key"], i) % (len(texts) + 1)
                texts.insert(pos, q["right"])
                keys = "ABCD"
                obj = {"id": qid, "topicId": tid, "difficulty": q["diff"], "type": "choice", "prompt": q["prompt"],
                       "choices": [{"key": keys[j], "text": x} for j, x in enumerate(texts)],
                       "answer": keys[pos], "explanation": q["expl"],
                       "verify": q["verify"] if q["verify"] else json.dumps(q["right"], ensure_ascii=False)}
            if q.get("figure"):
                obj["figure"] = q["figure"]
            new_qs.append(obj)
    res = verify_all(new_qs)
    for m in res["mismatch"]:
        errs.append("Validation failed for %s: %s" % (m["id"], m.get("detail")))
    return dict(topics=new_topics, deps=new_deps, qs=new_qs, std_items=std_items, errs=errs, verified=len(res["auto_verified"]))


def main():
    only_j = "--junior-only" in sys.argv
    only_s = "--senior-only" in sys.argv
    if only_j and only_s:
        print("--junior-only and --senior-only cannot be used together", file=sys.stderr)
        return 2
    do_j, do_s = not only_s, not only_j

    topics_all = load("topics.json")
    deps_all = load("dependencies.json")
    qs_all = load("questions.json")
    standards = load("cn-curriculum-standards.json")

    topics, tj = _drop(topics_all, "id", JR_TOPIC)
    topics, ts = _drop(topics, "id", SR_TOPIC)
    deps, dj = _drop(deps_all, "topicId", JR_TOPIC)
    deps, ds = _drop(deps, "topicId", SR_TOPIC)
    questions, qj = _drop(qs_all, "id", JR_TOPIC)
    questions, qsr = _drop(questions, "id", SR_TOPIC)
    items = standards["items"]
    keep_items = [it for it in items if not str(it.get("id", "")).startswith("cps-")]
    sj = [it for it in items if str(it.get("id", "")).startswith("cps-2022:")]
    ss = [it for it in items if str(it.get("id", "")).startswith("cps-hs-2017:")]
    other_cps = [it for it in items if str(it.get("id", "")).startswith("cps-")
                 and not str(it["id"]).startswith(("cps-2022:", "cps-hs-2017:"))]
    if other_cps:
        print("Error: unrecognized cps- standards entry: %s" % other_cps[0]["id"], file=sys.stderr)
        return 1
    math_ids = {t["id"]: t for t in topics if str(t["id"]).startswith("cnm_")}

    id_of = {t["key"]: "cnp_%03d" % (i + 1) for i, t in enumerate(TOPICS)}
    order = {t["key"]: i for i, t in enumerate(TOPICS)}
    name_of = {t["key"]: t["name"] for t in TOPICS}

    J = build_junior(math_ids, id_of, order, name_of)
    errs = list(J["errs"]) if do_j else []
    S_ = None
    if do_s:
        import phy_hs_build  # noqa: E402
        S_ = phy_hs_build.compile_senior(math_ids, id_of, name_of)
        errs += S_["errs"]
    if errs:
        for e in errs:
            print("Error: " + e, file=sys.stderr)
        return 1

    out_topics = topics + (J["topics"] if do_j else tj) + (S_["topics"] if do_s else ts)
    out_deps = deps + (J["deps"] if do_j else dj) + (S_["deps"] if do_s else ds)
    out_qs = questions + (J["qs"] if do_j else qj) + (S_["qs"] if do_s else qsr)
    standards["items"] = keep_items + (J["std_items"] if do_j else sj) + (S_["std_items"] if do_s else ss)
    if do_j:
        standards["physics"] = STD_SOURCE
    if do_s:
        standards["physics_senior"] = phy_hs_build.STD_SOURCE
    dump("topics.json", out_topics)
    dump("dependencies.json", out_deps)
    dump("questions.json", out_qs)
    dump("cn-curriculum-standards.json", standards)

    def line(tag, R):
        print("%s: %d topics, %d prerequisite edges (hard %d, soft %d), %d questions (%d auto-validated), %d standards entries, %d mathLinks (%d topic references)" % (
            tag, len(R["topics"]), len(R["deps"]), sum(d["strength"] == "hard" for d in R["deps"]),
            sum(d["strength"] == "soft" for d in R["deps"]), len(R["qs"]), R["verified"], len(R["std_items"]),
            sum(len(t.get("mathLinks", [])) for t in R["topics"]), sum(1 for t in R["topics"] if t.get("mathLinks"))))
    if do_j:
        line("Junior High Physics", J)
    if do_s:
        line("Senior High Physics", S_)
    return 0


if __name__ == "__main__":
    sys.exit(main())
