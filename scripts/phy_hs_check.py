#!/usr/bin/env python3
"""Check one high-school physics draft (scripts/phy_hs_<id>.py): structure, prerequisites, standards references, and question validation.

Usage: python3 scripts/phy_hs_check.py a01          # Check phy_hs_a01.py; report errors only and write no data files
       python3 scripts/phy_hs_check.py a01 --show   # Also print each topic's questions for manual review
"""
from __future__ import annotations

import importlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import phy_g8a, phy_g8b, phy_g9  # noqa: E402,F401
import phy_lib  # noqa: E402
import phy_hs_lib as L  # noqa: E402
import phy_hs_plan as P  # noqa: E402
from verify_questions import verify_all  # noqa: E402
import validate as V  # noqa: E402

# Keep these exact Chinese phrases: the validator still checks legacy Chinese drafts for prohibited copy.
BAN = re.compile(r"免费|AI\s*初稿|AI初稿")
JUNIOR = {t["key"]: t for t in phy_lib.TOPICS}


def lint_topic(key, t, errs, warns, math_ids):
    plan = P.PLAN_BY_KEY[key]
    where = "%s(%s)" % (key, plan["name"])
    if t["type"] not in V.TYPES:
        errs.append("%s has invalid type: %r" % (where, t["type"]))
    if not (30 <= len(t["description"]) <= 260):
        warns.append("%s description length is %d; recommended: 40–200 characters" % (where, len(t["description"])))
    if not t["std"]:
        errs.append("%s has no standards entries" % where)
    if len(t["std"]) > V.MAX_STANDARDS_PER_TOPIC:
        errs.append("%s exceeds the limit of %d standards entries" % (where, V.MAX_STANDARDS_PER_TOPIC))
    for tail, conf in t["std"]:
        if tail not in L.VALID_STD:
            errs.append("%s references nonexistent standards entry %s" % (where, tail))
        if conf not in V.CONFIDENCES:
            errs.append("%s has invalid standards confidence: %r" % (where, conf))
    if len({s[0] for s in t["std"]}) != len(t["std"]):
        errs.append("%s has duplicate standards entries" % where)
    if not t["pre"] and not t["root"]:
        errs.append("%s has neither prerequisites nor a root" % where)
    if t["root"] is not None and not str(t["root"]).strip():
        errs.append("%s has an empty root string" % where)
    seen = set()
    for pk, strength in t["pre"]:
        if strength not in V.STRENGTHS:
            errs.append("%s has invalid prerequisite strength: %r" % (where, strength))
        if pk in seen:
            errs.append("%s has duplicate prerequisite: %s" % (where, pk))
        seen.add(pk)
        if pk.startswith("J:"):
            if pk[2:] not in JUNIOR:
                errs.append("%s references nonexistent middle-school prerequisite %s (see the keys in phy_g8a/g8b/g9)" % (where, pk))
        elif pk not in P.PLAN_BY_KEY:
            errs.append("%s references prerequisite %s, which is not in the plan" % (where, pk))
        elif P.ORDER[pk] >= P.ORDER[key]:
            errs.append("%s prerequisite %s appears after it or is the topic itself" % (where, pk))
    for ml in t["math"]:
        if not (isinstance(ml, (tuple, list)) and len(ml) == 2 and str(ml[1]).strip()):
            errs.append("%s mathLinks must be (id, description)" % where)
        elif ml[0] not in math_ids:
            errs.append("%s mathLinks points to nonexistent math topic %s" % (where, ml[0]))
    qs = t["qs"]
    if len(qs) != 4:
        errs.append("%s has %d questions; exactly 4 are required" % (where, len(qs)))
    diffs = [q["diff"] for q in qs]
    if not {"basic", "standard"} <= set(diffs):
        errs.append("%s must include at least basic and standard difficulty: %s" % (where, diffs))
    for q in diffs:
        if q not in V.Q_DIFFICULTIES:
            errs.append("%s has invalid difficulty: %s" % (where, q))
    if qs and qs[0]["diff"] != "basic":
        warns.append("%s first question (diagnostic) should preferably be basic" % where)
    for i, q in enumerate(qs, 1):
        w = "%s_q%d" % (key, i)
        for field in ("prompt", "expl"):
            if BAN.search(q[field]):
                errs.append("%s %s contains prohibited copy" % (w, field))
        if q["kind"] == "numeric":
            # This exact phrase is required by the Chinese numeric-question format checked here.
            if "只填数值" not in q["prompt"]:
                warns.append("%s numeric prompt should end with the numeric-only marker and specify the unit" % w)
            if not q["verify"]:
                errs.append("%s numeric question is missing verify" % w)
            if re.search(r"[eE]\d|×10", q["answer"]):
                errs.append("%s numeric answer must be written as a decimal: %s" % (w, q["answer"]))
        else:
            if not (2 <= len(q["wrongs"]) <= 3):
                errs.append("%s multiple-choice question needs 2–3 incorrect options (3 recommended)" % w)
            if len(q["wrongs"]) == 2:
                warns.append("%s has only 2 incorrect options; 3 are recommended" % w)
            for x in [q["right"]] + q["wrongs"]:
                if BAN.search(x):
                    errs.append("%s option contains prohibited copy" % w)
            lens = [len(q["right"])] + [len(x) for x in q["wrongs"]]
            if len(q["right"]) >= 2 * max(len(x) for x in q["wrongs"]) + 6:
                warns.append("%s correct option is much longer than the distractors and may be easy to guess" % w)
        if len(q["expl"]) < 12:
            errs.append("%s explanation is too short" % w)


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in P.ASSIGN:
        print("Usage: phy_hs_check.py <%s> [--show]" % "|".join(P.ASSIGN))
        return 2
    fid = sys.argv[1]
    show = "--show" in sys.argv
    mod = importlib.import_module("phy_hs_" + fid)  # noqa: F841
    want = P.keys_for(fid)
    got = [k for k in L.HS if k in set(want)]
    extra = [k for k in L.HS if k not in set(want)]
    errs, warns = [], []
    for k in want:
        if k not in L.HS:
            errs.append("Missing topic %s (%s)" % (k, P.PLAN_BY_KEY[k]["name"]))
    for k in extra:
        errs.append("Topic %s is not assigned to %s" % (k, fid))
    with open(os.path.join(ROOT, "data", "topics.json"), encoding="utf-8") as f:
        math_ids = {t["id"] for t in json.load(f) if str(t["id"]).startswith("cnm_")}
    allq = []
    for k in want:
        if k not in L.HS:
            continue
        t = L.HS[k]
        lint_topic(k, t, errs, warns, math_ids)
        allq.extend(L.compile_questions(k, L.tid_of(k), t, errs))
    res = verify_all(allq)
    for m in res["mismatch"]:
        errs.append("Verification failed for %s: %s (answer=%s verify=%s)" % (m["id"], m.get("detail"), m["answer"], m["verify"]))
    unver = [q["id"] for q in allq if q["type"] == "choice" and q["verify"].startswith('"')]
    print("%s: %d/%d topics, %d questions, %d automatically verified, %d choice questions checked by text only" % (
        fid, len(got), len(want), len(allq), len(res["auto_verified"]), len(unver)))
    if show:
        for k in want:
            if k not in L.HS:
                continue
            t = L.HS[k]
            print("\n## %s %s [%s] pre=%s" % (L.tid_of(k), P.PLAN_BY_KEY[k]["name"], t["domain"], t["pre"]))
            for q in L.compile_questions(k, L.tid_of(k), t, []):
                print("  - [%s] %s" % (q["difficulty"], q["prompt"]))
                if q["type"] == "choice":
                    print("     " + " | ".join("%s.%s" % (c["key"], c["text"]) for c in q["choices"]) + "  → " + q["answer"])
                else:
                    print("     Answer " + q["answer"])
                print("     Explanation: " + q["explanation"])
    for w in warns:
        print("Warning: " + w)
    for e in errs:
        print("Error: " + e)
    print("CHECK %s" % ("FAILED (%d errors)" % len(errs) if errs else "PASSED"))
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
