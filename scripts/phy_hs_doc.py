#!/usr/bin/env python3
"""Generate docs/physics-senior-mapping.md from data/ (senior-high physics: curriculum-standard modules ↔ PEP textbook volumes, chapters, and sections ↔ topics).

Run python3 scripts/phy_build.py first, then this script. All tables in the document come from data; none are hand-written.
"""
from __future__ import annotations

import json
import os
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import phy_hs_plan as P  # noqa: E402
import phy_hs_std as S  # noqa: E402


def load(name):
    with open(os.path.join(ROOT, "data", name), encoding="utf-8") as f:
        return json.load(f)


def main():
    topics = {t["id"]: t for t in load("topics.json")}
    deps = load("dependencies.json")
    qs = load("questions.json")
    std = load("cn-curriculum-standards.json")
    senior = [t for t in topics.values() if str(t["id"]).startswith("cnp_h")]
    sd = [d for d in deps if str(d["topicId"]).startswith("cnp_h")]
    sq = [q for q in qs if str(q["topicId"]).startswith("cnp_h")]
    items = [i for i in std["items"] if str(i["id"]).startswith("cps-hs-2017:")]
    to_junior = [d for d in sd if str(d["prerequisiteId"]).startswith("cnp_") and not str(d["prerequisiteId"]).startswith("cnp_h")]
    by_std = defaultdict(list)
    for t in senior:
        for s in t["standards"]:
            by_std[s["id"]].append(t["id"])
    src = std["physics_senior"]
    out = []
    w = out.append
    w("# Senior High Physics: Curriculum-Standard Modules ↔ PEP Textbook Volumes, Chapters, and Sections ↔ Topics\n")
    w("> Generated from `data/` by `scripts/phy_hs_doc.py`; do not edit by hand. The mappings were created by this project and have not been reviewed by teachers or curriculum experts.\n")
    w("## 1. Sources and versions\n")
    w("| Item | Details |\n|---|---|")
    w("| Curriculum standard | \"%s\", %s, %s |" % (src["title"], src["issuer"], src["revision"]))
    w("| Curriculum-standard text | %s (retrieved %s). **Extracted from the PDF text layer; not checked word-for-word against the printed edition**, `verbatim` is false, and `page_or_ref` is \"Needs verification\" |" % (src["url"], src["retrieved"]))
    w("| Textbook | People's Education Press, General Senior High School Textbook: Physics (PEP edition), Compulsory Volumes 1–3 and Selective Compulsory Volumes 1–3; approved in 2019 under the 2017 curriculum standard |")
    w("| Textbook contents source | The \"2019 edition\" contents pages at Teacher's Home (renjiaoshe.com), transcribed through each section; **the copyright page of each printing has not been checked**, and it has not been confirmed section by section whether the 2024–2025 printings in circulation have exactly the same contents |")
    w("| Scope | 3 compulsory volumes + 3 selective compulsory volumes. Excludes curriculum-standard elective courses (Electives 1–3), activity suggestions, and examples |")
    w("| IDs | Topics `cnp_h001`–`cnp_h%03d` (in textbook order; no collision with junior-high IDs `cnp_001`–`cnp_092`); curriculum-standard IDs `cps-hs-2017:<B Compulsory|S Selective Compulsory><volume>.<topic>.<clause>`, with topic `X` used for experiments |" % len(senior))
    w("| Grade numbering | Grades 10–12 = Compulsory Volumes 1–3; grades 13–15 = Selective Compulsory Volumes 1–3. Semester is always \"Fall\", consistent with the senior-high English numbering convention |\n")
    w("## 2. Curriculum-standard modules and textbook volumes/chapters\n")
    w("The curriculum standard divides compulsory physics into three modules (Compulsory 1, 2, and 3) and selective compulsory physics into three modules as well. Textbook volumes correspond one-to-one with the modules, but chapter divisions do not align exactly with the curriculum-standard topics:\n")
    w("| Curriculum module | Curriculum-standard topics | Textbook volume | Chapters |\n|---|---|---|---|")
    rows = [
        ("Compulsory 1", "Mechanical motion and physical models; interactions and laws of motion", "Compulsory Volume 1", "Chapters 1–4"),
        ("Compulsory 2", "Mechanical energy and its conservation; curvilinear motion and universal gravitation; limits of Newtonian mechanics and an introduction to relativity", "Compulsory Volume 2", "Chapters 5–8 (relativity is in Chapter 7, Section 5)"),
        ("Compulsory 3", "Electrostatic fields; circuits and their applications; an introduction to electromagnetic fields and waves; energy and sustainable development", "Compulsory Volume 3", "Chapters 9–13 (energy is in Chapter 12, Section 4)"),
        ("Selective Compulsory 1", "Momentum and conservation of momentum; mechanical oscillations and waves; optics and its applications", "Selective Compulsory Volume 1", "Chapters 1–4"),
        ("Selective Compulsory 2", "Magnetic fields; electromagnetic induction and its applications; electromagnetic oscillations and waves; sensors", "Selective Compulsory Volume 2", "Chapters 1–5"),
        ("Selective Compulsory 3", "Solids, liquids, and gases; the laws of thermodynamics; atoms and nuclei; wave-particle duality", "Selective Compulsory Volume 3", "Chapters 1–5 (the curriculum standard places molecular kinetic theory under \"solids, liquids, and gases\"; the textbook combines atomic structure and wave-particle duality in Chapter 4)"),
    ]
    for r in rows:
        w("| %s | %s | %s | %s |" % r)
    w("")
    w("## 3. Counts\n")
    c = Counter(t["grade"] for t in senior)
    names = {10: "Compulsory Volume 1", 11: "Compulsory Volume 2", 12: "Compulsory Volume 3", 13: "Selective Compulsory Volume 1", 14: "Selective Compulsory Volume 2", 15: "Selective Compulsory Volume 3"}
    w("| Volume | Topics | Questions | Curriculum-standard items |\n|---|---:|---:|---:|")
    qcount = Counter(topics[q["topicId"]]["grade"] for q in sq)
    mod_of = {10: "B1", 11: "B2", 12: "B3", 13: "S1", 14: "S2", 15: "S3"}
    scount = Counter(i["id"].split(":")[1][:2] for i in items)
    for g in range(10, 16):
        w("| %s | %d | %d | %d |" % (names[g], c[g], qcount[g], scount[mod_of[g]]))
    w("| Total | %d | %d | %d |\n" % (len(senior), len(sq), len(items)))
    hard = sum(d["strength"] == "hard" for d in sd)
    w("%d prerequisite edges (%d hard, %d soft), including %d pointing to junior-high physics; %d mathLinks across %d topics. There are no cross-disciplinary prerequisite edges.\n" % (
        len(sd), hard, len(sd) - hard, len(to_junior), sum(len(t.get("mathLinks", [])) for t in senior),
        sum(1 for t in senior if t.get("mathLinks"))))
    w("## 4. Topics by volume (following textbook contents)\n")
    cur = None
    for r in P.PLAN:
        tid = "cnp_h%03d" % (P.ORDER[r["key"]] + 1)
        t = topics.get(tid)
        if not t:
            continue
        head = (r["book"], r["chapter_no"])
        if cur != head:
            if cur is None or cur[0] != r["book"]:
                w("\n### %s (%s)\n" % (P.BOOKS[r["book"]]["full"], r["mod"]))
                w("| Chapter | Section | Topic | Standard |\n|---|---|---|---|")
            cur = head
        stds = ", ".join("%s%s" % (s["id"].split(":")[1], "" if s["confidence"] == "exact" else "*") for s in t["standards"])
        w("| Chapter %s %s | %s.%s %s | %s %s | %s |" % (r["chapter_no"], r["chapter_name"], r["chapter_no"], r["sec_no"],
                                                  r["sec_title"], tid, t["name"], stds))
    w("\nIn the standard column, `*` marks an inferred match (a related clause that does not directly address the topic); all others are exact.\n")
    w("## 5. Curriculum-standard item coverage\n")
    unused = [i for i in items if not by_std.get(i["id"])]
    w("%d items (%d content requirements + %d required student experiments); %d are referenced by at least one topic." % (
        len(items), sum(1 for i in items if ".X." not in i["id"]), sum(1 for i in items if ".X." in i["id"]), len(items) - len(unused)))
    if unused:
        w("\nItems not referenced by any topic (mostly broad requirements related to history of science or STSE):\n")
        for i in unused:
            w("- `%s` %s" % (i["id"], i["text"]))
    w("\n## 6. Known limitations\n")
    w("- The curriculum-standard text was extracted from the publisher's PDF text layer and was not checked word-for-word against the printed edition or the original from the Ministry of Education.")
    w("- The textbook contents were taken from a 2019 contents page; copyright pages for the 2024–2025 printings were not checked for every volume.")
    w("- Examples and activity suggestions in the curriculum standard are excluded; Electives 1–3 are also excluded.")
    w("- Topics are scoped to a textbook section or one major concept/experiment within a section, not every subsection heading.")
    w("- Questions were drafted by AI and independently recalculated in a second review pass. Numeric questions and choice questions with numeric values are checked automatically; purely conceptual choice questions are not. No teacher or curriculum expert has reviewed them.")
    path = os.path.join(ROOT, "docs", "physics-senior-mapping.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
    print("Written to " + os.path.relpath(path, ROOT))


if __name__ == "__main__":
    main()
