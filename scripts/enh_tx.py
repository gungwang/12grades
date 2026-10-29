# -*- coding: utf-8 -*-
"""High-school English topic registration. Book-specific scripts handle content; enh_build.py compiles it."""
from en_lib import vocab, four, C

_CRIT = {
    "Pronunciation": ["Choose the correct option based on stress, intonation, or sound changes", "Explain where a pronunciation rule applies"],
    "Vocabulary": ["Choose the Chinese meaning of a word or phrase", "Choose an English word or phrase based on its Chinese meaning"],
    "Grammar": ["Choose a grammatically correct word or sentence", "Explain the role this structure plays in a sentence"],
    "Everyday communication": ["Choose an English sentence that fits the situation", "Understand what a functional expression asks or says"],
    "Reading and writing": ["Choose information from a passage that matches the text", "Choose a sentence that matches the writing points"],
}


def q(prompt, answer, w1, w2, w3, expl):
    return (prompt, answer, [w1, w2, w3], expl)


def V(key, name, grade, unit, desc, words, std):
    # "上" is the schema's fixed first-semester token; retain it unchanged.
    vocab(
        key, name, grade, "上", unit, desc, _CRIT["Vocabulary"], words, std,
    )


def X(key, name, domain, grade, unit, typ, desc, std, rows, conf):
    if len(rows) != 4:
        raise SystemExit("%s requires exactly 4 questions; got %d" % (key, len(rows)))
    items = [C(r[0], r[1], r[2], r[3]) for r in rows]
    four(key, name, domain, grade, "上", unit, typ, desc, _CRIT[domain], std, items, conf)


def P(key, name, grade, unit, desc, std, rows):
    X(key, name, "Pronunciation", grade, unit, "procedural", desc, std, rows, "inferred")


def G(key, name, grade, unit, desc, std, rows, conf="exact"):
    X(key, name, "Grammar", grade, unit, "procedural", desc, std, rows, conf)


def F(key, name, grade, unit, desc, std, rows):
    X(key, name, "Everyday communication", grade, unit, "application", desc, std, rows, "inferred")


def R(key, name, grade, unit, desc, std, rows):
    X(key, name, "Reading and writing", grade, unit, "application", desc, std, rows, "inferred")
