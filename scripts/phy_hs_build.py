"""Compile the senior-high physics drafts (phy_hs_a01 … phy_hs_a11) into topics, prerequisite edges, questions, and standards entries.

Do not run standalone; phy_build.py calls this module and merges its output into four files under data/, ensuring junior-high physics is not overwritten.
IDs: topics start at cnp_h001 and follow the textbook order in phy_hs_plan.py; standards use cps-hs-2017:<B|S><book>.<theme>.<number>.
"""
from __future__ import annotations

import importlib
import json

import phy_hs_lib as L
import phy_hs_plan as P
import phy_hs_std as S
from verify_questions import verify_all

STD_SOURCE = {
    "title": "General Senior High School Physics Curriculum Standards (2017 Edition, revised in 2020)",
    "issuer": "Ministry of Education of the People's Republic of China",
    "year": 2017,
    "revision": "Revised in 2020",
    "stage": "Senior high school (compulsory volumes 1–3; selective compulsory volumes 1–3)",
    "section": "Curriculum content · [Content Requirements]; required student experiments",
    "url": "https://www.esph.com.cn/docs/2025-04/b8fb91c002624b2e90ebfb1095f23a32.pdf",
    "textbook": ("People's Education Press, Senior High School Textbook: Physics (PEP edition), Compulsory Volumes 1–3 and Selective Compulsory Volumes 1–3, "
                 "approved in 2019 based on the 2017 standard. The table of contents is from the 2019 edition; the printing of each volume was not checked against its copyright page. "
                 "Topics follow the table of contents down to the section level; some longer sections are split into 2–3 topics."),
    "note": ("Clauses are taken from the text layer of the publicly available Education Science Press PDF of the General Senior High School Physics Curriculum Standards "
             "(2017 Edition, revised in 2020), and are split by original clause. They were not checked word-for-word against the printed edition, so verbatim is false; "
             "page_or_ref is \"Pending verification\". Standards IDs use cps-hs-2017:<B for compulsory | S for selective compulsory><book number>.<theme>.<clause>, "
             "matching clause numbering such as \"Compulsory 1, 1.1.1\" in the standard. Only the Content Requirements for compulsory and selective compulsory "
             "(87 clauses) and required student experiments (21 items) are included. The original experiment number is in clause, and IDs are renumbered by X theme "
             "within each volume; elective courses (Electives 1–3), activity suggestions, and examples are excluded. Topic domains retain the four junior-high physics "
             "categories—matter, motion and interactions, energy, and interdisciplinary practice—and do not correspond to the standard's theme names."),
    "retrieved": "2026-10-23",
}


def load_drafts():
    for fid in P.ASSIGN:
        importlib.import_module("phy_hs_" + fid)
        # The split files are imported by the main file itself.
    return L.HS


def compile_senior(math_ids, junior_id_of, junior_name_of):
    """Return dict(topics, deps, qs, std_items, errs, verified)."""
    errs = []
    load_drafts()
    for r in P.PLAN:
        if r["key"] not in L.HS:
            errs.append("Missing senior-high physics topic %s (%s)" % (r["key"], r["name"]))
    std_items = []
    for tail, clause, text in S.CLAUSES:
        mod, sec, n = tail.split(".")
        std_items.append({
            "id": L.std_id(tail),
            "domain": S.DOMAIN["%s.%s" % (mod, sec)],
            "section": "%s · %s.%s %s" % (S.MODULE_NAME[mod], clause.split(".")[0], sec, S.SECTIONS["%s.%s" % (mod, sec)]),
            "module": S.MODULE_NAME[mod],
            "clause": clause,
            "text": text,
            "page_or_ref": "Pending verification",
            "verbatim": False,
            "text_status": "Text layer of the publisher's public PDF; not checked word-for-word against the printed edition",
        })
    for tail, clause, text in S.EXPERIMENTS:
        mod = tail.split(".")[0]
        std_items.append({
            "id": L.std_id(tail),
            "domain": "Experimental inquiry",
            "section": "%s · Required student experiments" % S.MODULE_NAME[mod],
            "module": S.MODULE_NAME[mod],
            "clause": clause,
            "text": text,
            "page_or_ref": "Pending verification",
            "verbatim": False,
            "text_status": "Text layer of the publisher's public PDF; not checked word-for-word against the printed edition",
        })
    std_ids = {it["id"] for it in std_items}

    topics, deps, qs = [], [], []
    name_of = {r["key"]: r["name"] for r in P.PLAN}
    for r in P.PLAN:
        key = r["key"]
        t = L.HS.get(key)
        if t is None:
            continue
        tid = L.tid_of(key)
        q1 = t["qs"][0]
        topic = {
            "id": tid, "name": r["name"], "domain": t["domain"], "grade": r["grade"], "semester": "First semester",
            "chapter": "%s %s %s %s" % r["sec"], "type": t["type"],
            "description": t["description"], "mastery_criteria": t["mastery"],
            "diagnostic_question": {"question": q1["prompt"],
                                    "answer": q1["right"] if q1["kind"] == "choice" else q1["answer"]},
            "external": False, "subject": "physics",
            "standards": [{"id": L.std_id(c), "confidence": conf} for c, conf in t["std"]],
        }
        for sref in topic["standards"]:
            if sref["id"] not in std_ids:
                errs.append("%s references nonexistent standard %s" % (tid, sref["id"]))
        if t["math"]:
            links = []
            for mid, reason in t["math"]:
                if mid not in math_ids:
                    errs.append("%s has a mathLinks entry pointing to nonexistent math topic %s" % (tid, mid))
                links.append({"id": mid, "reason": reason})
            topic["mathLinks"] = links
        if t["root"]:
            topic["root_reason"] = t["root"]
        if not t["pre"] and not t["root"]:
            errs.append("%s has neither prerequisites nor a root reason" % tid)
        topics.append(topic)
        for pk, strength in t["pre"]:
            if pk.startswith("J:"):
                if pk[2:] not in junior_id_of:
                    errs.append("%s has nonexistent junior-high prerequisite %s" % (tid, pk))
                    continue
                pid, pname = junior_id_of[pk[2:]], junior_name_of[pk[2:]]
            else:
                if pk not in L.HS or P.ORDER[pk] >= P.ORDER[key]:
                    errs.append("%s has nonexistent prerequisite %s or it does not come earlier" % (tid, pk))
                    continue
                pid, pname = L.tid_of(pk), name_of[pk]
            reason = ("Studying “%s” requires prior knowledge of “%s”." if strength == "hard" else "“%s” uses knowledge from “%s”.") % (r["name"], pname)
            deps.append({"topicId": tid, "prerequisiteId": pid, "strength": strength, "reason": reason})
        qs.extend(L.compile_questions(key, tid, t, errs))

    res = verify_all(qs)
    for m in res["mismatch"]:
        errs.append("Verification failed for %s: %s" % (m["id"], m.get("detail")))
    return dict(topics=topics, deps=deps, qs=qs, std_items=std_items, errs=errs, verified=len(res["auto_verified"]))
