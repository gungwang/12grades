"""Registry for senior-high selective-compulsory data. Compiled into data/*.json by scripts/hs_sel_build.py.

Keep this separate from scripts/hs_common.py to avoid mixing it with the already-compiled compulsory drafts.
"""
from __future__ import annotations

TOPICS = []
QUESTIONS = {}
EDGES = []
STANDARDS = []


def standard(code, domain, theme, section, clause, text):
    STANDARDS.append({
        "code": code,
        "domain": domain,
        "theme": theme,
        "section": section,
        "clause": clause,
        "text": text,
    })


def topic(key, book, chapter, section, name, domain, typ, desc, crit, std, conf="exact", note=None):
    if any(t["key"] == key for t in TOPICS):
        raise SystemExit("Duplicate topic key: %s" % key)
    if book not in (1, 2, 3):
        raise SystemExit("%s must use book number 1, 2, or 3" % key)
    if not (2 <= len(crit) <= 3):
        raise SystemExit("%s must have 2–3 mastery criteria" % key)
    TOPICS.append({
        "key": key,
        "book": book,
        "chapter": chapter,
        "section": section,
        "name": name,
        "domain": domain,
        "type": typ,
        "description": desc,
        "mastery_criteria": list(crit),
        "std": std,
        "confidence": conf,
        "note": note,
    })


def questions(key, items):
    if key in QUESTIONS:
        raise SystemExit("Duplicate question set: %s" % key)
    if len(items) != 4:
        raise SystemExit("%s needs 4 questions; received %d" % (key, len(items)))
    QUESTIONS[key] = items


def edge(src, dst, strength, reason):
    EDGES.append((src, dst, strength, reason))


def hard(src, dst, reason):
    edge(src, dst, "hard", reason)


def soft(src, dst, reason):
    edge(src, dst, "soft", reason)
