"""Registration helpers for high-school physics drafts. Chapters, names, grades, and volumes all come from phy_hs_plan.py; drafts contain content only.

T(key, domain, typ, desc, mastery, std, pre=(), math=(), qs=(), root=None)
  key    knowledge-point key registered in phy_hs_plan.py
  std    [("B1.1.3", "exact"), ...]  trailing part of a curriculum clause ID (after cps-hs-2017:), up to 3 clauses
  pre    [("velocity", "hard"), ("J:ohm", "soft")]  prerequisites: high-school keys must come before this topic; the "J:" prefix marks junior-high physics keys (from phy_g8a/g8b/g9)
  math   [("cnm_h012", "One-sentence explanation of why this math topic is needed")]  mathLinks only; no prerequisite edge
  qs     exactly 4 questions, using C (choice) and N (numeric)
C and N are shared with junior-high physics (see phy_lib.py).
"""
from __future__ import annotations

import hashlib
import json

from phy_lib import C, N, PHY_DOMAINS  # noqa: F401
from phy_hs_plan import PLAN, PLAN_BY_KEY, ORDER, BOOKS  # noqa: F401
import phy_hs_std as S

HS = {}     # key -> draft
VALID_STD = {c[0] for c in S.CLAUSES} | {e[0] for e in S.EXPERIMENTS}


def T(key, domain, typ, desc, mastery, std, pre=(), math=(), qs=(), root=None):
    assert key in PLAN_BY_KEY, "No such key in phy_hs_plan.py: %s" % key
    assert key not in HS, "Duplicate registration: %s" % key
    assert domain in PHY_DOMAINS, (key, domain)
    assert 2 <= len(mastery) <= 3, key
    HS[key] = dict(key=key, domain=domain, type=typ, description=desc, mastery=list(mastery), std=list(std),
                   pre=list(pre), math=list(math), qs=list(qs), root=root)
    return HS[key]


def std_id(tail):
    return "cps-hs-2017:" + tail


def tid_of(key):
    return "cnp_h%03d" % (ORDER[key] + 1)


def _slot(key, i):
    return int(hashlib.md5(("%s#%d" % (key, i)).encode()).hexdigest(), 16) % 4


def compile_questions(key, tid, t, errs):
    out = []
    if len(t["qs"]) != 4:
        errs.append("%s must have exactly 4 questions" % key)
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
                errs.append("%s contains duplicate choices" % qid)
            pos = q["pos"] if q["pos"] is not None else _slot(key, i) % (len(texts) + 1)
            texts.insert(pos, q["right"])
            keys = "ABCD"
            obj = {"id": qid, "topicId": tid, "difficulty": q["diff"], "type": "choice", "prompt": q["prompt"],
                   "choices": [{"key": keys[j], "text": x} for j, x in enumerate(texts)],
                   "answer": keys[pos], "explanation": q["expl"],
                   "verify": q["verify"] if q["verify"] else json.dumps(q["right"], ensure_ascii=False)}
        if q.get("figure"):
            obj["figure"] = q["figure"]
        out.append(obj)
    return out
