# -*- coding: utf-8 -*-
"""Thin wrappers for primary-school English topics. Each book script supplies content only."""
from en_lib import vocab, sound, four, C, N

# These category values are lookup/schema tokens: X indexes _CRIT with them and passes them to en_lib.four.
_CRIT = {
    "语音": ["Choose the correct item based on its letter or sound", "Match letters with their sounds and example words"],
    "词汇": ["Choose the meaning of a word", "Choose the English word that matches the given meaning"],
    "语法": ["Choose the grammatically correct word or sentence", "Use this sentence pattern correctly in context"],
    "日常表达": ["Choose the English sentence that fits the situation", "Understand what this functional sentence asks or says"],
    "读写": ["Choose information that matches the passage", "Choose the sentence that matches the passage"],
}


def V(key, name, g, s, u, desc, words, std=None):
    if std is None:
        std = "vocab34" if g <= 4 else "vocab56"
    vocab(key, name, g, s, u, desc, _CRIT["词汇"], words, std)


def S(key, name, g, s, u, desc, sound_name, goods, bads, std, mode="vowel"):
    sound(key, name, g, s, u, desc, _CRIT["语音"], std, sound_name, goods, bads, mode)


def X(key, name, domain, g, s, u, typ, desc, std, qs, conf="inferred", note=None):
    items = []
    for q in qs:
        if q[0] == "n":
            items.append(N(q[1], q[2], q[3]))
        else:
            items.append(C(q[1], q[2], q[3], q[4]))
    four(key, name, domain, g, s, u, typ, desc, _CRIT[domain], std, items, conf, note)


def P(key, name, g, s, u, desc, std, qs, conf="exact"):
    X(key, name, "语音", g, s, u, "procedural", desc, std, qs, conf)


def G(key, name, g, s, u, desc, std, qs):
    X(key, name, "语法", g, s, u, "procedural", desc, std, qs, "exact")


def F(key, name, g, s, u, desc, std, qs):
    X(key, name, "日常表达", g, s, u, "application", desc, std, qs)


def R(key, name, g, s, u, desc, std, qs):
    X(key, name, "读写", g, s, u, "application", desc, std, qs)
