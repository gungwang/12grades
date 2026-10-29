# -*- coding: utf-8 -*-
"""Generate primary-school questions. primary_recheck recalculates prompt expressions, so answers are not hard-coded in hidden fields outside the prompts."""
from fractions import Fraction


def ask(prompt, py, diff, expl):
    """Use wording that independent validation can recognize; verify uses an equivalent Python expression."""
    return {"difficulty": diff, "type": "numeric", "prompt": prompt, "verify": py, "explanation": expl}


def calc(py, zh, diff, expl, decimal=False):
    prompt = "Calculate: %s＝？" % zh
    if decimal:
        prompt += " (answer as a decimal)"
    return {"difficulty": diff, "type": "numeric", "prompt": prompt, "verify": py, "explanation": expl}


def story(prefix, py, zh, diff, expl, decimal=False):
    prompt = prefix + "Calculate: %s＝？" % zh
    if decimal:
        prompt += " (answer as a decimal)"
    return {"difficulty": diff, "type": "numeric", "prompt": prompt, "verify": py, "explanation": expl}


def rem(a, b, diff, expl, prefix=""):
    prompt = prefix + "Write the quotient first, then the remainder. Quotient and remainder: %d÷%d" % (a, b)
    return {"difficulty": diff, "type": "numeric", "prompt": prompt,
            "verify": "(%d//%d, %d%%%d)" % (a, b, a, b), "explanation": expl}


def choice_num(zh, py, wrongs, diff, expl):
    """Choices are numerical results. wrongs contains strings and must not include the correct result."""
    return {"difficulty": diff, "type": "choice",
            "prompt": "What is the result of %s?" % zh,
            "wrongs": list(wrongs), "verify": py, "explanation": expl, "_numchoice": True}


def fact(prompt, options, correct, expl, diff="basic"):
    if correct not in options:
        raise ValueError("Correct answer is not among the choices: %s" % prompt)
    if len(options) not in (3, 4) or len(set(options)) != len(options):
        raise ValueError("Invalid choices: %s" % prompt)
    keys = "ABCD"
    return {"difficulty": diff, "type": "choice", "prompt": prompt,
            "choices": [{"key": keys[i], "text": t} for i, t in enumerate(options)],
            "verify": repr(correct), "explanation": expl}


def add4(pairs, thing="apples", unit=""):
    """pairs contains four (a, b) pairs of nonnegative integers whose sums stay within the required range."""
    (a, b), (c, d), (e, f), (g, h) = pairs
    return [
        calc("%d+%d" % (a, b), "%d＋%d" % (a, b), "basic", "%d＋%d＝%d." % (a, b, a + b)),
        calc("%d+%d" % (c, d), "%d＋%d" % (c, d), "basic", "%d＋%d＝%d." % (c, d, c + d)),
        story("There are %d %s%s, and %d more %s%s. How many %s%s are there in total?" %
              (e, unit, thing, f, unit, thing, unit, thing),
              "%d+%d" % (e, f), "%d＋%d" % (e, f), "standard",
              "Combine the two groups: %d＋%d＝%d." % (e, f, e + f)),
        choice_num("%d＋%d" % (g, h), "%d+%d" % (g, h),
                   [str(g + h + 1), str(max(g + h - 1, 0)), str(g + h + 2)],
                   "standard", "%d＋%d＝%d." % (g, h, g + h)),
    ]


def sub4(pairs, thing="apples", unit=""):
    (a, b), (c, d), (e, f), (g, h) = pairs
    for x, y in pairs:
        if x < y:
            raise ValueError("The minuend must not be smaller than the subtrahend: %s - %s" % (x, y))
    return [
        calc("%d-%d" % (a, b), "%d－%d" % (a, b), "basic", "%d－%d＝%d." % (a, b, a - b)),
        calc("%d-%d" % (c, d), "%d－%d" % (c, d), "basic", "%d－%d＝%d." % (c, d, c - d)),
        story("There are %d %s%s. %d %s%s are taken away. How many %s%s remain?" %
              (e, unit, thing, f, unit, thing, unit, thing),
              "%d-%d" % (e, f), "%d－%d" % (e, f), "standard",
              "Subtract the part taken away from the total: %d－%d＝%d." % (e, f, e - f)),
        choice_num("%d－%d" % (g, h), "%d-%d" % (g, h),
                   [str(g - h + 1), str(g - h + 2), str(abs(g - h - 1))],
                   "standard", "%d－%d＝%d." % (g, h, g - h)),
    ]


def mul4(pairs, thing="pencils", unit=""):
    (a, b), (c, d), (e, f), (g, h) = pairs
    return [
        calc("%d*%d" % (a, b), "%d×%d" % (a, b), "basic", "%d×%d＝%d." % (a, b, a * b)),
        calc("%d*%d" % (c, d), "%d×%d" % (c, d), "basic", "%d×%d＝%d." % (c, d, c * d)),
        story("Each box contains %d %s%s. There are %d boxes. How many %s%s are there in total?" %
              (e, unit, thing, f, unit, thing),
              "%d*%d" % (e, f), "%d×%d" % (e, f), "standard",
              "Find the sum of %d groups of %d using multiplication: %d×%d＝%d." %
              (f, e, e, f, e * f)),
        choice_num("%d×%d" % (g, h), "%d*%d" % (g, h),
                   [str(g * h + g), str(g * h + 1), str(g + h)],
                   "standard", "%d×%d＝%d." % (g, h, g * h)),
    ]


def div4(pairs, thing="candies", unit=""):
    (a, b), (c, d), (e, f), (g, h) = pairs
    for x, y in pairs:
        if y == 0 or x % y:
            raise ValueError("Division must divide evenly: %s / %s" % (x, y))
    return [
        calc("%d/%d" % (a, b), "%d÷%d" % (a, b), "basic", "%d÷%d＝%d." % (a, b, a // b)),
        calc("%d/%d" % (c, d), "%d÷%d" % (c, d), "basic", "%d÷%d＝%d." % (c, d, c // d)),
        story("Divide %d %s%s equally into %d groups. How many %s%s are in each group?" %
              (e, unit, thing, f, unit, thing),
              "%d/%d" % (e, f), "%d÷%d" % (e, f), "standard",
              "%d÷%d＝%d." % (e, f, e // f)),
        choice_num("%d÷%d" % (g, h), "%d/%d" % (g, h),
                   [str(g // h + 1), str(g // h + 2), str(max(g // h - 1, 0))],
                   "standard", "%d÷%d＝%d." % (g, h, g // h)),
    ]


def expr4(items):
    """items: four (py, zh, diff, expl, optional prefix, optional decimal) tuples. diff must contain two basic and two standard questions, with the first question basic."""
    out = []
    for it in items:
        py, zh, diff, expl = it[:4]
        prefix = it[4] if len(it) > 4 else ""
        decimal = it[5] if len(it) > 5 else False
        if prefix:
            out.append(story(prefix, py, zh, diff, expl, decimal))
        else:
            out.append(calc(py, zh, diff, expl, decimal))
    return out


def mix_basic_fact(calc_q, fact_q, std1, std2):
    """q1 and q2 are basic (numeric and multiple-choice, respectively); q3 and q4 are standard numeric questions."""
    calc_q = dict(calc_q, difficulty="basic")
    fact_q = dict(fact_q, difficulty="basic")
    std1 = dict(std1, difficulty="standard")
    std2 = dict(std2, difficulty="standard")
    return [calc_q, fact_q, std1, std2]
