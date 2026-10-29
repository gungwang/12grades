"""Registry for high-school required-course data, compiled into data/*.json by scripts/hs_build.py."""
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
        raise SystemExit("Duplicate question: %s" % key)
    if len(items) != 4:
        raise SystemExit("%s requires 4 questions, got %d" % (key, len(items)))
    QUESTIONS[key] = items


def edge(src, dst, strength, reason):
    EDGES.append((src, dst, strength, reason))


def hard(src, dst, reason):
    edge(src, dst, "hard", reason)


def soft(src, dst, reason):
    edge(src, dst, "soft", reason)
