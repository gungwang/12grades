#!/usr/bin/env python3
"""Compile high school compulsory-course drafts into data/topics.json, dependencies.json, questions.json, and the curriculum standards file.

Run only once, before cnm_h001 exists. Further runs are rejected to prevent duplicate additions.
Transitive reduction applies only to new high school prerequisite edges; existing elementary and middle school edges are unchanged.

Usage: python3 scripts/hs_build.py
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

from hs_common import EDGES, QUESTIONS, STANDARDS, TOPICS  # noqa: E402
import hs_standards  # noqa: E402,F401
import hs_book1  # noqa: E402,F401
import hs_book2  # noqa: E402,F401
from verify_questions import safe_eval  # noqa: E402

CJK_RE = re.compile(r"[\u4e00-\u9fff]")

# Existing topics referenced by cross-stage edges. Their legacy names are checked during compilation to avoid mismatching IDs.
# Keep these exact legacy Chinese names: main() compares them with existing generated topic names, and this builder does not emit them.
KNOWN = {
    "cnm_003": "有理数的分类",
    "cnm_025": "用字母表示数",
    "cnm_040": "等式的性质",
    "cnm_049": "分段计费与方案选择",
    "cnm_050": "立体图形与平面图形",
    "cnm_052": "点、线、面、体",
    "cnm_056": "角的概念与表示",
    "cnm_064": "垂线",
    "cnm_067": "平行线与平行公理",
    "cnm_071": "定义、命题与定理",
    "cnm_072": "平移的概念与性质",
    "cnm_074": "平方根与算术平方根",
    "cnm_077": "无理数",
    "cnm_078": "实数的分类与数轴表示",
    "cnm_082": "平面直角坐标系与点的坐标",
    "cnm_094": "不等式及其解集",
    "cnm_096": "不等式的性质",
    "cnm_097": "一元一次不等式的解法",
    "cnm_102": "全面调查与抽样调查",
    "cnm_103": "总体、个体、样本与样本容量",
    "cnm_105": "扇形图、条形图与折线图",
    "cnm_106": "频数分布表与数据分组",
    "cnm_107": "频数分布直方图",
    "cnm_115": "三角形内角和定理",
    "cnm_142": "同底数幂的乘法",
    "cnm_163": "同底数幂的除法",
    "cnm_164": "零指数幂、负整数指数幂与科学记数法",
    "cnm_167": "二次根式的概念与有意义的条件",
    "cnm_174": "勾股定理",
    "cnm_183": "平行四边形的性质",
    "cnm_194": "函数的概念",
    "cnm_195": "自变量的取值范围",
    "cnm_197": "函数的图象",
    "cnm_198": "函数的三种表示方法",
    "cnm_201": "一次函数的概念",
    "cnm_203": "一次函数的性质",
    "cnm_211": "平均数",
    "cnm_213": "中位数与众数",
    "cnm_215": "极差、方差与标准差",
    "cnm_216": "数据的四分位数",
    "cnm_219": "一元二次方程的概念",
    "cnm_222": "公式法与求根公式",
    "cnm_224": "因式分解法",
    "cnm_229": "二次函数的概念",
    "cnm_230": "y=ax² 的图象与性质",
    "cnm_232": "y=ax²+bx+c 的图象与性质",
    "cnm_234": "二次函数与一元二次方程",
    "cnm_235": "二次函数的最值",
    "cnm_237": "反比例函数的概念",
    "cnm_244": "图形的旋转",
    "cnm_250": "圆的有关概念",
    "cnm_256": "弧长",
    "cnm_257": "扇形面积",
    "cnm_258": "圆锥的侧面积与全面积",
    "cnm_276": "锐角三角函数的定义",
    "cnm_277": "特殊角的三角函数值与计算",
    "cnm_278": "解直角三角形",
    "cnm_283": "三视图及由三视图想象立体图形",
    "cnm_284": "随机事件、必然事件与不可能事件",
    "cnm_285": "概率的意义与等可能事件的概率",
    "cnm_286": "用列举法求概率",
    "cnm_288": "用频率估计概率",
    "cnm_292": "数据收集的方法：问卷调查、实验与查阅资料",
    "cnm_297": "频率（相对频数）的计算与意义",
    "cnm_298": "简单随机抽样的实施（抽签法与随机数）",
    "cnm_302": "用样本平均数估计总体平均数",
    "cnm_306": "用样本方差估计总体的稳定性",
    "cnm_308": "概率的取值范围与概率的性质",
    "cnm_309": "等可能性与古典概型的判断",
    "cnm_p163": "长方体和正方体的体积",
    "cnm_p207": "圆柱的体积",
    "cnm_p208": "圆柱的表面积",
    "cnm_p209": "圆锥的体积",
}


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
        raise TypeError("Numeric-question verify expressions must not return strings: %r" % v)
    if isinstance(v, float):
        fr = Fraction(v).limit_denominator(64)
        if abs(float(fr) - v) > 1e-9:
            raise ValueError("Result is not a simple fraction: %r" % (v,))
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
            raise ValueError("Multiple answers must contain at least two values")
        # Keep the full-width comma as the multi-answer separator consumed by verify_questions.py.
        return "，".join(fmt_one(x) for x in v)
    return fmt_one(v)


def build_question(tid, index, spec, slot):
    kind = spec[0]
    diff = "basic" if index <= 2 else "standard"
    qid = "%s_q%d" % (tid, index)
    if kind in ("n", "nu"):
        prompt, verify, expl = spec[1], spec[2], spec[3]
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
                raise ValueError("%s is marked unordered, but verify did not return multiple answers" % qid)
            item["unordered"] = True
        elif multi:
            pass
        return item, answer
    if kind == "c":
        prompt, correct, wrongs, expl = spec[1], spec[2], spec[3], spec[4]
        texts = list(wrongs)
        if correct in texts or len(set(texts)) != len(texts):
            raise ValueError("%s has duplicate choices or the correct choice among the distractors" % qid)
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
    raise ValueError("Unknown question type %s" % kind)


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


def reduce_new(edges):
    """Remove redundant new edges only from high school topics. Drop a hard edge only if another all-hard path exists; drop a soft edge if any other path exists."""
    adj = defaultdict(list)
    for e in edges:
        adj[e["topicId"]].append([e["prerequisiteId"], e["strength"]])
    kept = []
    dropped = 0
    for e in edges:
        if not str(e["topicId"]).startswith("cnm_h"):
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
    # Chinese grade/chapter markers are consumed by the chapter parsers below.
    vol = "高一" if spec["book"] == 1 else "高二"
    if spec["chapter"] in ("数学建模", "数学探究"):
        return "%s %s %s" % (vol, spec["chapter"], spec["section"])
    return "%s %s %s" % (vol, spec["chapter"], spec["section"])


def main():
    topics = load("topics.json")
    if any(t.get("id") == "cnm_h001" for t in topics):
        print("cnm_h001 already exists. hs_build.py cannot compile twice.", file=sys.stderr)
        return 1
    by_name = {t["name"]: t for t in topics}
    for tid, name in KNOWN.items():
        hit = next((t for t in topics if t["id"] == tid), None)
        if hit is None or hit["name"] != name:
            print("Cross-stage ID/name validation failed for %s" % tid, file=sys.stderr)
            return 1

    if len(TOPICS) < 120 or len(TOPICS) > 180:
        print("Topic count %d is outside the range 120–180" % len(TOPICS), file=sys.stderr)
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
        print("Duplicate curriculum-standard code", file=sys.stderr)
        return 1
    index = {t["key"]: i for i, t in enumerate(TOPICS)}
    grade_of = {t["key"]: (10 if t["book"] == 1 else 11) for t in TOPICS}

    new_topics = []
    new_questions = []
    id_of = {}
    for i, spec in enumerate(TOPICS, start=1):
        tid = "cnm_h%03d" % i
        id_of[spec["key"]] = tid
        if spec["std"] not in std_codes:
            print("%s refers to missing curriculum standard %s" % (spec["key"], spec["std"]), file=sys.stderr)
            return 1
        if spec["confidence"] not in ("exact", "inferred"):
            print("%s has an invalid confidence value" % spec["key"], file=sys.stderr)
            return 1
        if spec["confidence"] == "inferred" and not spec.get("note"):
            print("%s is inferred but has no note" % spec["key"], file=sys.stderr)
            return 1
        try:
            built = []
            diag_answer = None
            for n, item in enumerate(QUESTIONS[spec["key"]], start=1):
                q, shown = build_question(tid, n, item, slot=i + n)
                if not q["prompt"].strip() or not q["explanation"].strip():
                    raise ValueError("Question prompt or explanation is empty")
                if "because" in q["explanation"] and q["explanation"].count("option") > 2:
                    pass
                built.append(q)
                if n == 1:
                    diag_answer = shown
        except Exception as exc:  # noqa: BLE001
            print("Failed to build question %s %s: %s" % (tid, spec["name"], exc), file=sys.stderr)
            return 1
        std_ref = {"id": "cms-2017:H.%s" % spec["std"], "confidence": spec["confidence"]}
        if spec.get("note"):
            std_ref["note"] = spec["note"]
        new_topics.append({
            "id": tid,
            "name": spec["name"],
            "domain": spec["domain"],
            "grade": 10 if spec["book"] == 1 else 11,
            # "上" is the semester token consumed by diagnose/engine.js when matching topic scopes.
            "semester": "上",
            "chapter": chapter_of(spec),
            "type": spec["type"],
            "description": spec["description"],
            "mastery_criteria": spec["mastery_criteria"],
            "diagnostic_question": {"question": built[0]["prompt"], "answer": diag_answer},
            "external": False,
            "standards": [std_ref],
        })
        new_questions.extend(built)

    raw_edges = []
    seen = set()
    for src, dst, strength, reason in EDGES:
        if src not in id_of:
            print("Edge source is not a high school topic: %s" % src, file=sys.stderr)
            return 1
        if len(CJK_RE.findall(reason)) < 9:
            print("Prerequisite reason is too short: %s → %s: %s" % (src, dst, reason), file=sys.stderr)
            return 1
        if dst in id_of:
            if index[dst] >= index[src]:
                print("Prerequisite is not earlier than its dependent topic: %s depends on %s" % (src, dst), file=sys.stderr)
                return 1
            if grade_of[dst] > grade_of[src]:
                print("Prerequisite is in a higher grade: %s depends on %s" % (src, dst), file=sys.stderr)
                return 1
            pid = id_of[dst]
        elif dst in KNOWN:
            pid = dst
        else:
            print("Prerequisite is neither a high school key nor a registered legacy ID: %s" % dst, file=sys.stderr)
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

    deps = load("dependencies.json")
    merged, dropped = reduce_new(deps + raw_edges)
    new_only = [e for e in merged if str(e["topicId"]).startswith("cnm_h")]
    internal = [e for e in new_only if str(e["prerequisiteId"]).startswith("cnm_h")]
    cross = [e for e in new_only if not str(e["prerequisiteId"]).startswith("cnm_h")]
    print("High school topics: %d" % len(new_topics))
    print("New edges: %d (reduced by %d); within high school: %d; cross-stage: %d" % (
        len(new_only), dropped, len(internal), len(cross)))
    print("Questions: %d" % len(new_questions))

    from verify_questions import verify_all
    checked = verify_all(new_questions)
    if checked["mismatch"] or checked["unverifiable"]:
        for m in checked["mismatch"][:40]:
            print("Question verification failed for %s: %s" % (m["id"], m.get("detail")), file=sys.stderr)
        print("Question verification failed: %d mismatches, %d unverifiable" % (
            len(checked["mismatch"]), len(checked["unverifiable"])), file=sys.stderr)
        return 1
    covered = {e["topicId"] for e in new_only}
    naked = [t["id"] + " " + t["name"] for t in new_topics if t["id"] not in covered]
    if naked:
        print("These high school topics have no prerequisites and cannot be new roots: " + ", ".join(naked), file=sys.stderr)
        return 1
    ch_model = re.compile(r"^(高[一二]) (数学建模|数学探究) (\S+)$")
    ch_num = re.compile(r"^(\S+) (第\S+章) (\S+?)(?: (\S+))?$")
    for t in new_topics:
        if not (ch_model.match(t["chapter"]) or ch_num.match(t["chapter"])):
            print("Could not parse chapter name: %s %s" % (t["id"], t["chapter"]), file=sys.stderr)
            return 1

    std = load("cn-curriculum-standards.json")
    note = std["source"].get("note") or ""
    extra = (" High school compulsory-course entries are summaries of the five themes in the General Senior High School Mathematics Curriculum Standards (2017 Edition, revised in 2025),"
             " not text verified page by page; verbatim is false and page_or_ref is pending verification."
             " IDs in the form cms-2017:H.<module>.NN are assigned by this graph by theme and are not original Ministry of Education IDs.")
    if "cms-2017" not in note:
        std["source"]["note"] = note + extra
    std["source"]["stage"] = "Compulsory education stages 1–4 (Grades 1–9); senior high school compulsory courses"
    retrieved = std["source"].get("retrieved") or ""
    if "2026-10-20" not in retrieved:
        std["source"]["retrieved"] = retrieved + "; 2026-10-20 (senior high school compulsory courses)"
    std["source"]["high_school"] = {
        "title": "General Senior High School Mathematics Curriculum Standards (2017 Edition, revised in 2025)",
        "issuer": "Ministry of Education of the People's Republic of China",
        "year": 2020,
        "url": "http://www.moe.gov.cn/srcsite/A26/s8001/202006/t20200603_462199.html",
        "reference_pdf": "https://www.pep.com.cn/xw/zt/rjwy/gzkb2020/202205/P020220517519489596282.pdf",
        "note": "The issuance notice is available on the Ministry of Education website. The text of the clauses has not been checked page by page against the PDF and is pending verification.",
    }
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
            "page_or_ref": "pending verification",
            "verbatim": False,
            "text_status": "Publicly available summary; not checked page by page against the Ministry of Education PDF; pending verification",
        })

    topics.extend(new_topics)
    questions = load("questions.json")
    questions.extend(new_questions)
    dump("topics.json", topics)
    dump("dependencies.json", merged)
    dump("questions.json", questions)
    dump("cn-curriculum-standards.json", std)
    batch = os.path.join(ROOT, "data", "_qbatches", "high.json")
    with open(batch, "w", encoding="utf-8") as f:
        json.dump(new_questions, f, ensure_ascii=False, indent=2)
        f.write("\n")

    log_path = os.path.join(ROOT, "data", "second_pass_log.json")
    with open(log_path, encoding="utf-8") as f:
        log = json.load(f)
    pass_name = "D: High school compulsory-course questions have verify expressions written by the generator and checked against their answers by verify_questions.py"
    # Keep the legacy name only to recognize the existing deduplication key in second_pass_log.json.
    legacy_pass_name = "D：高中必修题由生成脚本写 verify，再经 verify_questions.py 核对表达式与答案"
    passes = log.setdefault("passes", [])
    if not any(p.get("name") in (pass_name, legacy_pass_name) for p in passes):
        passes.append({
            "name": pass_name,
            "solver": "scripts/hs_build.py + scripts/verify_questions.py",
            "questions": len(new_questions),
            "note": "Answers are written by evaluating the same verify expression and then compared by the verification script, so a mismatch indicates a formatting issue rather than an independent solution. No blind-solving pass like the middle school A/B rounds was performed. For conceptual questions, the correct-choice text matches the string returned by verify.",
            "disagreements": 0,
        })
    log["high_school_checked_by_verify"] = len(new_questions)
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(log, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("Wrote data/. Run validate.py and verify_questions.py next.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
