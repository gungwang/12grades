#!/usr/bin/env python3
"""Check the first three stages' content requirements against the 2025 revision of the Compulsory Education Mathematics Curriculum Standards (2022 edition).

Usage:
    python3 scripts/moe2025_check.py --moe /path/to/math-2025.txt

math-2025.txt is a public transcription of the full revised text (see section 1 of docs/moe2025-alignment.md).
The script only parses, aligns, and reports; it does not write files. A person decides whether to change the data.

Output has three sections:
  1. Clause counts in the revised text versus repository item counts for each (stage, domain);
  2. Pairs below the similarity threshold (>0.995 is considered a match; only differences are shown);
  3. Extra clauses in the revised text (potential omissions from the repository).
Uses only the standard library.
"""
import argparse
import difflib
import json
import os
import re
import sys

try:  # The default Windows console encoding is GBK and can fail on characters such as ².
    sys.stdout.reconfigure(errors="replace")
except AttributeError:
    pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STD_PATH = os.path.join(ROOT, "data", "cn-curriculum-standards.json")

# These Chinese stage labels, numerals, and domain headings are parser tokens in the curriculum source.
STAGE_RE = re.compile(r"^第([一二三四])学段（(\d)～(\d)年级）$")
CN = {"一": "1", "二": "2", "三": "3", "四": "4"}
DOMAINS = {"（一）数与代数": "NA", "（二）图形与几何": "GG",
           "（三）统计与概率": "SP", "（四）综合与实践": "IP"}
PAIRS = [("1", "NA"), ("2", "NA"), ("3", "NA"),
         ("1", "GG"), ("2", "GG"), ("3", "GG"),
         ("1", "SP"), ("2", "SP"), ("3", "SP")]


# These Chinese punctuation marks are structural escapes in the source curriculum text.
def unescape(s):
    for a, b in [("\\#", "#"), ("\\:", "："), ("\\.", "."), ("\\,", "，"), ("\\=", "="),
                 ("\\>", ">"), ("\\<", "<"), ("\\+", "+"), ("\\(", "("), ("\\)", ")"),
                 ("\\%", "%"), ("\\;", "；"), ("\\!", "！"), ("\\?", "？"), ("\\~", "~"),
                 ("\\*", "*"), ("\\[", "["), ("\\]", "]")]:
        s = s.replace(a, b)
    return s


def blocks(lines):
    """Extract the body lines in the content-requirements section for each domain and stage."""
    # These Chinese section headings are required source markers; keep them literal for parsing.
    out, cur, i = [], None, 0
    while i < len(lines):
        t = unescape(lines[i]).strip()
        if t in DOMAINS:
            cur = DOMAINS[t]
        m = STAGE_RE.match(t)
        if m and cur:
            j = i + 1
            while j < len(lines) and "【内容要求】" not in unescape(lines[j]):
                j += 1
            k = j + 1
            body = []
            while k < len(lines) and "【学业要求】" not in unescape(lines[k]) \
                    and "【教学提示】" not in unescape(lines[k]):
                body.append(lines[k])
                k += 1
            out.append((CN[m.group(1)], cur, j + 1, body))
            i = k
            continue
        i += 1
    return out


def parse(body):
    """Split body lines into clauses: subsection headings (1. Number and operations) and numbered clauses; treat an unnumbered paragraph as one clause."""
    # Full-width parentheses delimit numbered clauses in the source curriculum text.
    items, sub, cur, prose = [], None, None, []
    for raw in body:
        t = unescape(raw).strip()
        if not t or re.match(r"^\[1\]", t):  # Skip footnotes that appear inside the body.
            continue
        m = re.match(r"^(\d+)\\?\.\s*(.+)$", t)
        if m and len(t) <= 20:
            if cur:
                items.append(cur)
                cur = None
            sub = m.group(2).strip()
            continue
        m2 = re.match(r"^（(\d+)）(.+)$", t)
        if m2:
            if cur:
                items.append(cur)
            cur = {"section": sub, "clause": "(" + m2.group(1) + ")", "text": m2.group(2)}
            continue
        if cur:
            cur["text"] += t
        else:
            prose.append(t)
    if cur:
        items.append(cur)
    if not items and prose:
        items = [{"section": sub or "", "clause": "", "text": "".join(prose)}]
    for it in items:
        it["text"] = re.sub(r"\s+", "", it["text"])
    return items


def norm(s):
    # Keep the Chinese example marker and Han range: they identify source examples and characters used in normalization.
    s = re.sub(r"（例\s*\d+[^）]*）", "", s)
    return re.sub(r"[^\u4e00-\u9fffA-Za-z0-9]", "", s)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--moe", required=True, help="Full text of the 2025 revision (math-2025.txt)")
    ap.add_argument("--std", default=STD_PATH, help="cn-curriculum-standards.json")
    ap.add_argument("--threshold", type=float, default=0.995)
    args = ap.parse_args()

    lines = open(args.moe, encoding="utf-8").read().split("\n")
    new = {}
    for stage, dom, start, body in blocks(lines):
        for it in parse(body):
            it["line"] = start
            new.setdefault((stage, dom), []).append(it)

    std = json.load(open(args.std, encoding="utf-8"))["items"]
    old = {}
    for it in std:
        m = re.match(r"cms-2022:(\d)\.([A-Z]{2})\.(\d+)$", it["id"])
        if m:
            old.setdefault((m.group(1), m.group(2)), []).append((int(m.group(3)), it))
    for k in old:
        old[k].sort()

    print("Stage Domain | Repository items | Revised clauses")
    bad = 0
    for key in PAIRS:
        a, b = old.get(key, []), new.get(key, [])
        print("  %s %s | %d | %d" % (key[0], key[1], len(a), len(b)))
        if len(a) != len(b):
            bad += 1
    print("\nGroups with mismatched clause counts: %d" % bad)

    print("\nDiffering pairs (similarity < %.3f)" % args.threshold)
    n = 0
    for key in PAIRS:
        a = [x[1] for x in old.get(key, [])]
        b = new.get(key, [])
        for x, y in zip(a, b):
            r = difflib.SequenceMatcher(None, norm(x["text"]), norm(y["text"])).ratio()
            if r < args.threshold:
                n += 1
                print("\n  [%.3f] %s  %s:%d" % (r, x["id"], os.path.basename(args.moe), y["line"]))
                print("    Repository: ", x["text"])
                print("    Revised:    ", y["text"])
    print("\nTotal differing pairs: %d" % n)

    print("\nExtra clauses in the revised text (potential repository omissions)")
    m = 0
    for key in PAIRS:
        b = new.get(key, [])[len(old.get(key, [])):]
        for y in b:
            m += 1
            print("  %s %s %s %s | %s" % (key[0], key[1], y["section"], y["clause"], y["text"]))
    print("Total: %d" % m)
    return 0


if __name__ == "__main__":
    sys.exit(main())
