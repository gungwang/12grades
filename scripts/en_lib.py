# -*- coding: utf-8 -*-
"""Registry and question generation for primary-school English data. Called by scripts/en_build.py."""

import re

TOPICS = []
HARD = []

UNITS = {
    # These Chinese semester values are internal lookup tokens used by callers and chapter(); emitted labels are translated below.
    (3, "上", 1): "Hello",
    (3, "上", 2): "Colours",
    (3, "上", 3): "Look at me",
    (3, "上", 4): "We love animals",
    (3, "上", 5): "Let's eat",
    (3, "上", 6): "Happy birthday",
    (3, "下", 1): "Welcome back to school",
    (3, "下", 2): "My family",
    (3, "下", 3): "At the zoo",
    (3, "下", 4): "Where is my car",
    (3, "下", 5): "Do you like pears",
    (3, "下", 6): "How many",
    (4, "上", 1): "My classroom",
    (4, "上", 2): "My schoolbag",
    (4, "上", 3): "My friends",
    (4, "上", 4): "My home",
    (4, "上", 5): "Dinner's ready",
    (4, "上", 6): "Meet my family",
    (4, "下", 1): "My school",
    (4, "下", 2): "What time is it",
    (4, "下", 3): "Weather",
    (4, "下", 4): "At the farm",
    (4, "下", 5): "My clothes",
    (4, "下", 6): "Shopping",
    (5, "上", 1): "What's he like",
    (5, "上", 2): "My week",
    (5, "上", 3): "What would you like",
    (5, "上", 4): "What can you do",
    (5, "上", 5): "There is a big bed",
    (5, "上", 6): "In a nature park",
    (5, "下", 1): "My day",
    (5, "下", 2): "My favourite season",
    (5, "下", 3): "My school calendar",
    (5, "下", 4): "When is the art show",
    (5, "下", 5): "Whose dog is it",
    (5, "下", 6): "Work quietly",
    (6, "上", 1): "How can I get there",
    (6, "上", 2): "Ways to go to school",
    (6, "上", 3): "My weekend plan",
    (6, "上", 4): "I have a pen pal",
    (6, "上", 5): "What does he do",
    (6, "上", 6): "How do you feel",
    (6, "下", 1): "How tall are you",
    (6, "下", 2): "Last weekend",
    (6, "下", 3): "Where did you go",
    (6, "下", 4): "Then and now",
}

# Curriculum-standard entries paraphrase public descriptions and are not checked page by page. Symbolic names are used only in this file.
STANDARD_ROWS = [
    ("letters", "1", "PH", "Phonics", "Level 1 · Phonics",
     "Recognize the 26 letters of the English alphabet in order and distinguish uppercase from lowercase forms of the same letter."),
    ("vowel_letter", "1", "PH", "Phonics", "Level 1 · Phonics",
     "Distinguish the vowel letters a, e, i, o, and u from common consonants."),
    ("short_vowel", "1", "PH", "Phonics", "Level 1 · Phonics",
     "Recognize common short-vowel sounds for vowel letters in stressed closed syllables and use them to sound out simple words."),
    ("consonant", "1", "PH", "Phonics", "Level 1 · Phonics",
     "Make an initial connection between common consonant letters and their sounds at the beginning of words."),
    ("magic_e", "1", "PH", "Phonics", "Level 1 · Phonics",
     "Recognize common vowel-letter sounds in open syllables, such as a-e, i-e, o-e, and u-e."),
    ("blend", "2", "PH", "Phonics", "Level 2 · Phonics",
     "Sound out words using learned letter combinations and common initial consonant blends."),
    ("tone", "2", "PH", "Phonics", "Level 2 · Phonics",
     "Pay attention to sentence stress when reading aloud and distinguish the basic intonation of statements and yes/no questions."),
    ("vocab34", "1", "VO", "Vocabulary", "Level 1 · Vocabulary",
     "Recognize core words related to greetings, colors, body parts, animals, food, school, family, and other themes in pictures and brief contexts. Consult the curriculum-standard appendix for the exact Level 1 word list; this entry is a paraphrase."),
    ("vocab56", "2", "VO", "Vocabulary", "Level 2 · Vocabulary",
     "Understand and use vocabulary about days of the week, months, seasons, sports, places, transportation, occupations, emotions, and plans in context. Consult the appendix for the exact Level 2 word list; this entry is a paraphrase."),
    ("confuse", "2", "VO", "Vocabulary", "Level 2 · Vocabulary",
     "Distinguish the meanings and uses of some commonly confused words in sentences, such as there/their, its/it's, and too/two."),
    ("be", "1", "GR", "Grammar", "Level 1 · Grammar",
     "Use am, is, and are to form simple affirmative sentences and pair them with I, you, he, she, it, and they."),
    ("plural", "1", "GR", "Grammar", "Level 1 · Grammar",
     "Recognize singular and plural count nouns and use common -s and -es forms correctly."),
    ("pronoun", "1", "GR", "Grammar", "Level 1 · Grammar",
     "Use subject pronouns and common possessive adjectives in sentences, such as I, you, he, she, my, your, his, and her."),
    ("pointer", "1", "GR", "Grammar", "Level 1 · Grammar",
     "Use this, that, these, and those, together with in, on, and under, to indicate proximity and location."),
    ("present_basic", "1", "GR", "Grammar", "Level 1 · Grammar",
     "Use common simple-present patterns to express likes and possession, such as I like, Do you like, and He has."),
    ("number_q", "1", "GR", "Grammar", "Level 1 · Grammar",
     "Use cardinal numbers and How many, How old, What time, and How much to ask about quantity, age, time, and price."),
    ("lets", "1", "GR", "Grammar", "Level 1 · Grammar",
     "Understand suggestions beginning with Let's, and use whose and the possessive 's to ask or state who something belongs to."),
    ("present3", "2", "GR", "Grammar", "Level 2 · Grammar",
     "Use the simple present to describe habits, including third-person singular verb forms and questions introduced by do or does."),
    ("continuous", "2", "GR", "Grammar", "Level 2 · Grammar",
     "Use the present continuous to describe actions happening now, with am, is, or are plus an -ing form."),
    ("can_there", "2", "GR", "Grammar", "Level 2 · Grammar",
     "Use can to talk about ability and There is/There are, including question forms, to describe what is in a place."),
    ("when_ord", "2", "GR", "Grammar", "Level 2 · Grammar",
     "Use adverbs of frequency, ordinal numbers, and in, on, and at to talk about routines, dates, and months."),
    ("poss_pron", "2", "GR", "Grammar", "Level 2 · Grammar",
     "Use mine, yours, his, hers, ours, and theirs to state who something belongs to."),
    ("future", "2", "GR", "Grammar", "Level 2 · Grammar",
     "Use be going to to express plans or future actions."),
    ("modal_imp", "2", "GR", "Grammar", "Level 2 · Grammar",
     "Use imperatives, should, and must to make suggestions or state rules."),
    ("past", "2", "GR", "Grammar", "Level 2 · Grammar",
     "Use the simple past to talk about completed events, including regular -ed forms and common irregular verbs."),
    ("compare", "2", "GR", "Grammar", "Level 2 · Grammar",
     "Use comparative adjectives and than to compare two things."),
    ("func_greet", "1", "FU", "Everyday expressions", "Level 1 · Everyday expressions",
     "Greet and say goodbye, thank others, and introduce one's name, age, and place of origin using simple English."),
    ("func_daily", "1", "FU", "Everyday expressions", "Level 1 · Everyday expressions",
     "Ask about and express colors, locations, likes, family, time, and prices using simple sentence patterns."),
    ("func_place", "1", "FU", "Everyday expressions", "Level 1 · Everyday expressions",
     "Use common functional phrases in settings such as school, home, mealtimes, and shops."),
    ("func_life", "2", "FU", "Everyday expressions", "Level 2 · Everyday expressions",
     "Ask about and describe school subjects, routines, dates, seasons, abilities, and current activities."),
    ("func_out", "2", "FU", "Everyday expressions", "Level 2 · Everyday expressions",
     "Ask for and give directions, describe ways of traveling, discuss plans and feelings, and offer simple advice."),
    ("read_pic", "1", "RW", "Reading and writing", "Level 1 · Reading and writing",
     "Use text-based picture descriptions to recognize words and sentences, and select the English sentence that matches the picture."),
    ("read_short", "1", "RW", "Reading and writing", "Level 1 · Reading and writing",
     "Read short dialogues and texts with clearly stated details and identify people, colors, quantities, or locations."),
    ("read_text", "2", "RW", "Reading and writing", "Level 2 · Reading and writing",
     "Read short diaries, notices, and letters about textbook topics and identify times, places, people, and events."),
    ("read_write", "2", "RW", "Reading and writing", "Level 2 · Reading and writing",
     "Choose a coherent English sentence based on a prompt to describe a person, a plan, or a day in the past."),
]

NOTE_VOCAB = "People's Education Press (PEP) vocabulary for this unit. The curriculum standard does not list every word individually; the word list and book placement require verification."
NOTE_FUNC = "Functional phrases from the textbook. The standard does not list every phrase individually; verification is pending."
NOTE_READ = "The question describes the image or text to test word recognition and reading comprehension. Book placement requires verification."
NOTE_PH = "Phonics items follow common Let's Spell sequences for courses beginning in Grade 3; book placement requires verification."
NOTE_GR = "Sentence patterns are assigned to grammar standards in the usual sequence for the PEP course beginning in Grade 3; book placement requires verification."


def chapter(grade, sem, unit):
    semester = {"上": "First", "下": "Second"}[sem]
    title = UNITS[(grade, sem, unit)]
    return "Grade %d, %s semester, Unit %d: %s" % (grade, semester, unit, title)


def _add(spec):
    if any(t["key"] == spec["key"] for t in TOPICS):
        raise SystemExit("Duplicate topic key: %s" % spec["key"])
    TOPICS.append(spec)


def vocab(key, name, grade, sem, unit, desc, criteria, words, std):
    _add({
        "key": key, "name": name, "domain": "Vocabulary", "grade": grade, "semester": {"上": "First semester", "下": "Second semester"}[sem],
        "unit": unit, "type": "conceptual", "description": desc,
        "mastery_criteria": criteria, "std": std, "conf": "inferred", "note": NOTE_VOCAB,
        "gen": "vocab", "words": words,
    })


def sound(key, name, grade, sem, unit, desc, criteria, std, sound_name, goods, bads, mode="vowel"):
    _add({
        "key": key, "name": name, "domain": "Phonics", "grade": grade, "semester": {"上": "First semester", "下": "Second semester"}[sem],
        "unit": unit, "type": "procedural", "description": desc,
        "mastery_criteria": criteria, "std": std, "conf": "inferred", "note": NOTE_PH,
        "gen": "sound", "sound": sound_name, "goods": goods, "bads": bads, "mode": mode,
    })


def four(key, name, domain, grade, sem, unit, typ, desc, criteria, std, items, conf="inferred", note=None):
    if note is None:
        # Existing callers pass these Chinese domain markers; four() uses them to select the matching note.
        note = {"语音": NOTE_PH, "词汇": NOTE_VOCAB, "语法": NOTE_GR, "日常表达": NOTE_FUNC, "读写": NOTE_READ}.get(domain, NOTE_GR)
    if conf == "exact":
        note = None
    _add({
        "key": key, "name": name, "domain": {"语音": "Phonics", "词汇": "Vocabulary", "语法": "Grammar", "日常表达": "Everyday expressions", "读写": "Reading and writing"}.get(domain, domain), "grade": grade, "semester": {"上": "First semester", "下": "Second semester"}[sem],
        "unit": unit, "type": typ, "description": desc,
        "mastery_criteria": criteria, "std": std, "conf": conf, "note": note,
        "gen": "custom", "items": items,
    })


def C(prompt, answer, wrongs, expl):
    wrongs = list(wrongs)
    if len(wrongs) != 3:
        raise SystemExit("A multiple-choice question must have exactly 3 distractors: %s" % prompt[:40])
    return ("choice", prompt, answer, wrongs, expl)


def N(prompt, answer, expl):
    return ("numeric", prompt, str(answer), expl)


def hard(topic, prereq, reason):
    HARD.append((topic, prereq, reason))


def gen_vocab(spec):
    words = spec["words"]
    if len(words) < 4:
        raise SystemExit("%s must have at least 4 words" % spec["key"])
    ens = [w[0] for w in words]
    zhs = [w[1] for w in words]
    if len(set(ens)) != len(ens) or len(set(zhs)) != len(zhs):
        raise SystemExit("%s has duplicate vocabulary entries" % spec["key"])

    def others(pool, i):
        return [pool[j] for j in range(len(pool)) if j != i][:3]

    return [
        C("Which word means “%s”?" % zhs[0], ens[0], others(ens, 0), "“%s” means “%s”." % (ens[0], zhs[0])),
        C("Which option gives the meaning of “%s”?" % ens[1], zhs[1], others(zhs, 1), "The meaning of “%s” is “%s”." % (ens[1], zhs[1])),
        C("Choose the word that means “%s”." % zhs[2], ens[2], others(ens, 2), "The word that means “%s” is “%s”." % (zhs[2], ens[2])),
        C("Which word means “%s”?" % zhs[3], ens[3], others(ens, 3), "“%s” means “%s”." % (ens[3], zhs[3])),
    ]


def gen_sound(spec):
    goods, bads = spec["goods"], spec["bads"]
    sound = spec["sound"]
    if len(goods) < 4 or len(bads) < 4:
        raise SystemExit("%s must have at least 4 positive and 4 negative examples" % spec["key"])
    if len(set(goods)) != len(goods) or len(set(bads)) != len(bads) or set(goods) & set(bads):
        raise SystemExit("%s positive and negative examples must be distinct" % spec["key"])
    if spec["mode"] == "start":
        same = "Which word starts with the same sound as %s?" % goods[1]
        why = "Both %s and %s start with the %s sound." % (goods[1], goods[2], sound)
    else:
        same = "Which word has the same vowel sound as %s?" % goods[1]
        why = "Both %s and %s contain %s." % (goods[1], goods[2], sound)
    return [
        C("Which word contains %s?" % sound, goods[0], bads[:3], "%s contains %s." % (goods[0], sound)),
        C("Which word does not contain %s?" % sound, bads[0], goods[:3], "%s does not contain %s." % (bads[0], sound)),
        C(same, goods[2], bads[:3], why),
        C("Choose the word that contains %s." % sound, goods[3], bads[1:4], "%s contains %s." % (goods[3], sound)),
    ]


def gen_custom(spec):
    items = spec["items"]
    if len(items) != 4:
        raise SystemExit("%s must have exactly 4 questions" % spec["key"])
    diffs = ["basic", "basic", "standard", "standard"]
    out = []
    for diff, item in zip(diffs, items):
        if item[0] == "choice":
            out.append((diff,) + item)
        elif item[0] == "numeric":
            out.append((diff,) + item)
        else:
            raise SystemExit("%s has an unrecognized question type" % spec["key"])
    return out


def materialise_questions(spec):
    if spec["gen"] == "vocab":
        raw = gen_vocab(spec)
    elif spec["gen"] == "sound":
        raw = gen_sound(spec)
    else:
        raw = gen_custom(spec)
    diffs = ["basic", "basic", "standard", "standard"]
    made = []
    for i, item in enumerate(raw):
        # C() returned by gen_vocab/sound has no difficulty; gen_custom already includes it.
        if item[0] in ("basic", "standard", "advanced"):
            diff, kind = item[0], item[1]
            rest = item[2:]
        else:
            diff, kind, rest = diffs[i], item[0], item[1:]
        if kind == "choice":
            prompt, answer, wrongs, expl = rest
            made.append({"d": diff, "t": "choice", "p": prompt, "a": answer, "w": list(wrongs), "e": expl})
        else:
            prompt, answer, expl = rest
            made.append({"d": diff, "t": "numeric", "p": prompt, "a": str(answer), "e": expl, "v": str(answer)})
    if len(made) != 4:
        raise SystemExit("%s generated %d questions" % (spec["key"], len(made)))
    return made


# check_question uses these Chinese markers to preserve the existing banned-prefix and metadata checks.
_BANNED_START = re.compile(r"^(同一|上题|该题|同上)")
_BANNED_META = re.compile(r"本知识点|课标|是否要求")
_BAD_CORRECT = (
    " a apple", " a elephant", " a orange", " a ice", " a umbrella", " a hour",
    "He are", "He am", "She are", "She am", "It are", "It am", "I is", "I are",
    "They is", "more bigger", "more taller", "more big", "gooses", "childs",
    "teached", "buyed", "goed", "eated", "comed",
)


def norm_opt(text):
    s = str(text).strip().lower()
    s = re.sub(r"\s+", "", s)
    s = re.sub(r"[.!\s]+$", "", s)
    return s


def check_question(key, q):
    prompt = q["p"]
    if _BANNED_START.match(prompt.strip()):
        raise SystemExit("%s prompt starts with a banned prefix: %s" % (key, prompt[:20]))
    blob = prompt + "\n" + q["e"] + "\n" + q["a"]
    if q["t"] == "choice":
        blob += "\n" + "\n".join(q["w"])
    if _BANNED_META.search(blob):
        raise SystemExit("%s contains curriculum-standard meta-question wording" % key)
    if q["t"] == "choice":
        opts = [q["a"]] + list(q["w"])
        if len(opts) != 4:
            raise SystemExit("%s does not have exactly 4 options" % key)
        if len(set(opts)) != 4:
            raise SystemExit("%s has duplicate options: %s" % (key, opts))
        if len(set(norm_opt(o) for o in opts)) != 4:
            raise SystemExit("%s has duplicate options after normalization: %s" % (key, opts))
        for o in opts:
            if re.fullmatch(r"[A-Za-z]", o.strip()):
                raise SystemExit("%s has a single-letter option: %s" % (key, o))
        for bad in _BAD_CORRECT:
            if bad in q["a"] or bad in prompt:
                raise SystemExit("%s answer or prompt may contain an ungrammatical form: %s" % (key, bad))
    if not str(q["e"]).strip():
        raise SystemExit("%s is missing an explanation" % key)
