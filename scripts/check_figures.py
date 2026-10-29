#!/usr/bin/env python3
"""Check questions with figures: SVG parses, uses no external references, and figure choices do not show their names.

Usage: python3 scripts/check_figures.py
"""
import json
import os
import re
import sys
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUESTIONS_PATH = os.path.join(ROOT, "data", "questions.json")

_BAD_TAGS = {"script", "foreignobject", "image", "iframe", "embed", "object", "audio", "video", "link", "use"}
_NS_OK = (
    'xmlns="http://www.w3.org/2000/svg"',
    "xmlns='http://www.w3.org/2000/svg'",
)


def figure_problems(svg, where):
    """Return a list of errors; an empty list means the figure is ready to use."""
    if not isinstance(svg, str) or not svg.strip():
        return ["%s has an empty figure" % where]
    probe = svg
    for ns in _NS_OK:
        probe = probe.replace(ns, "")
    if re.search(r"https?://", probe, re.I):
        return ["%s figure references an external URL" % where]
    try:
        root = ET.fromstring(svg)
    except ET.ParseError as ex:
        return ["%s figure is not valid SVG: %s" % (where, ex)]
    errs = []
    if root.tag.split("}")[-1] != "svg":
        errs.append("%s figure's root element is not svg" % where)
    if not (root.attrib.get("viewBox") or "").strip():
        errs.append("%s figure is missing viewBox" % where)
    for el in root.iter():
        tag = el.tag.split("}")[-1]
        if tag.lower() in _BAD_TAGS:
            errs.append("%s figure contains disallowed <%s>" % (where, tag))
        for key, val in el.attrib.items():
            name = key.split("}")[-1].lower()
            text = str(val)
            if name in ("href", "src") and text and not text.startswith("#"):
                errs.append("%s figure has an external reference" % where)
            if re.search(r"url\(\s*(?!#)", text, re.I):
                errs.append("%s figure uses a url() that is not an in-page fragment" % where)
    return errs


def question_figure_problems(q):
    if not isinstance(q, dict):
        return []
    where = q.get("id") or "Question"
    errs = []
    if "figure" in q:
        errs.extend(figure_problems(q.get("figure"), where))
    choices = q.get("choices") if isinstance(q.get("choices"), list) else []
    if "hideChoiceText" in q:
        if q.get("hideChoiceText") is not True:
            errs.append("%s: hideChoiceText must be true" % where)
        elif q.get("type") != "choice":
            errs.append("%s is not a multiple-choice question, so choice text cannot be hidden" % where)
        elif not choices or not all(
            isinstance(c, dict) and isinstance(c.get("figure"), str) and c.get("figure").strip()
            for c in choices
        ):
            errs.append("%s must provide a figure for every choice when choice text is hidden" % where)
        else:
            for c in choices:
                if c.get("text") and c["text"] in c["figure"]:
                    errs.append("%s choice %s figure contains the name \"%s\"" % (where, c.get("key"), c["text"]))
    for c in choices:
        if isinstance(c, dict) and "figure" in c:
            errs.extend(figure_problems(c.get("figure"), "%s choice %s" % (where, c.get("key"))))
    return errs


def main():
    with open(QUESTIONS_PATH, encoding="utf-8") as f:
        questions = json.load(f)
    errs = []
    n = 0
    for q in questions:
        if not isinstance(q, dict):
            continue
        has = "figure" in q or "hideChoiceText" in q or any(
            isinstance(c, dict) and "figure" in c for c in (q.get("choices") or []) if isinstance(q.get("choices"), list)
        )
        if not has:
            continue
        n += 1
        errs.extend(question_figure_problems(q))
    if errs:
        print("Figure check failed with %d error(s):" % len(errs))
        for line in errs[:40]:
            print("  " + line)
        if len(errs) > 40:
            print("  ... and %d more" % (len(errs) - 40))
        return 1
    print("Figure check passed: %d question(s) have figures; SVG parses and has no external references" % n)
    return 0


if __name__ == "__main__":
    sys.exit(main())
