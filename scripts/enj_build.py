#!/usr/bin/env python3
"""Compile middle school English drafts into data/topics.json, dependencies.json, questions.json, and the curriculum standards file.

Append cne_j topics only. Do not change existing math or elementary English IDs and names, or reduce existing edges.
Prerequisites may point to elementary English, but not to math.

Usage: python3 scripts/enj_build.py
"""
from __future__ import annotations

import json
import os
import sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import en_lib  # noqa: E402
import en_topics  # noqa: E402,F401

PRIMARY_TOPICS = list(en_lib.TOPICS)
PRIMARY_BY_KEY = {t["key"]: t for t in PRIMARY_TOPICS}
en_lib.TOPICS = []
en_lib.HARD = []

import enj_topics  # noqa: E402
from en_lib import HARD, TOPICS, check_question, materialise_questions  # noqa: E402
from verify_questions import verify_all  # noqa: E402

# These category values are shared source tokens checked against en_topics.py; output labels are translated below.
EN_CODES = {"PH": "语音", "VO": "词汇", "GR": "语法", "FU": "日常表达", "RW": "读写"}
DOMAIN_LABELS = {
    "语音": "Pronunciation",
    "词汇": "Vocabulary",
    "语法": "Grammar",
    "日常表达": "Everyday English",
    "读写": "Reading and Writing",
}
CN = "0123456789"

# Curriculum-standard entries paraphrase public descriptions; they have not been checked page by page against the source.
STANDARD_ROWS = [
    ("stress", "3", "PH", "语音", "Level 3 · Pronunciation",
     "Recognize common stress patterns in two- and multisyllabic words and stress the correct syllables when reading aloud."),
    ("tone", "3", "PH", "语音", "Level 3 · Pronunciation",
     "Use falling intonation for statements and wh-questions, and rising intonation for yes/no questions."),
    ("esound", "3", "PH", "语音", "Level 3 · Pronunciation",
     "Distinguish common pronunciations of plural and third-person singular -s and -es by their final sounds."),
    ("edsound", "3", "PH", "语音", "Level 3 · Pronunciation",
     "Distinguish the three common pronunciations of regular past-tense -ed by the verb's final sound."),
    ("link", "3", "PH", "语音", "Level 3 · Pronunciation",
     "Recognize linking between a word ending in a consonant and one beginning with a vowel, and begin to use it when reading phrases aloud."),
    ("plosion", "3", "PH", "语音", "Level 3 · Pronunciation",
     "Recognize incomplete release when stop consonants occur together, as with /t/ in “sit down.”"),
    ("pause", "3", "PH", "语音", "Level 3 · Pronunciation",
     "Pause between sense groups when reading aloud without splitting a group."),
    ("vocab7", "3", "VO", "词汇", "Level 3 · Vocabulary",
     "Understand core vocabulary about names, family, school, food, clothing, animals, weather, and places in context. The Level 3 word list is in the curriculum appendix; this entry is a paraphrase."),
    ("vocab8", "3", "VO", "词汇", "Level 3 · Vocabulary",
     "Understand vocabulary about habits, comparison, plans, health, housework, stories, and travel experiences in context. The Level 3 word list is in the curriculum appendix; this entry is a paraphrase."),
    ("vocab9", "3", "VO", "词汇", "Level 3 · Vocabulary",
     "Understand and begin to use vocabulary about learning, festivals, inventions, rules, customs, and environmental protection in context. The Level 3 word list is in the curriculum appendix; this entry is a paraphrase."),
    ("be_have", "3", "GR", "语法", "Level 3 · Grammar",
     "Use am, is, and are correctly, and distinguish have from has."),
    ("noun_pron", "3", "GR", "语法", "Level 3 · Grammar",
     "Distinguish countable and uncountable nouns, and use plural nouns, demonstrative pronouns, and possessive adjectives."),
    ("present", "3", "GR", "语法", "Level 3 · Grammar",
     "Use the simple present to describe habits and facts, including third-person singular forms and questions and negatives with do or does."),
    ("continuous", "3", "GR", "语法", "Level 3 · Grammar",
     "Use the present continuous to describe actions happening now, with am, is, or are plus a verb in the -ing form."),
    ("past", "3", "GR", "语法", "Level 3 · Grammar",
     "Use the simple past to describe past events, including was, were, regular -ed verbs, common irregular verbs, and questions with did."),
    ("future", "3", "GR", "语法", "Level 3 · Grammar",
     "Use be going to for plans and will for predictions or decisions made at the moment of speaking."),
    ("pastcont", "3", "GR", "语法", "Level 3 · Grammar",
     "Use the past continuous for an action in progress at a particular time in the past, and connect past actions with when and while."),
    ("perfect", "3", "GR", "语法", "Level 3 · Grammar",
     "Use the present perfect to talk about experiences and completed events, with already, yet, ever, never, been, gone, for, and since."),
    ("pastperf", "3", "GR", "语法", "Level 3 · Grammar",
     "Use the past perfect for an event completed before another past event, with had plus a past participle."),
    ("modal", "3", "GR", "语法", "Level 3 · Grammar",
     "Use can, could, must, should, have to, would, and might to express ability, obligation, requests, suggestions, or possibility."),
    ("compare", "3", "GR", "语法", "Level 3 · Grammar",
     "Use comparative and superlative adjectives and adverbs to compare two or more items."),
    ("sentence", "3", "GR", "语法", "Level 3 · Grammar",
     "Use imperative sentences, exclamations, and tag questions."),
    ("question", "3", "GR", "语法", "Level 3 · Grammar",
     "Use what, where, when, who, why, how, how much, how often, and how far to ask for information."),
    ("to_ing", "3", "GR", "语法", "Level 3 · Grammar",
     "Use infinitives as objects, object complements, and adverbials of purpose, and distinguish verbs followed by infinitives from those followed by gerunds."),
    ("clause_obj", "3", "GR", "语法", "Level 3 · Grammar",
     "Use that, if, whether, and question words to introduce object clauses, with statement word order in the clause."),
    ("clause_attr", "3", "GR", "语法", "Level 3 · Grammar",
     "Use restrictive relative clauses introduced by who, which, or that to modify people or things."),
    ("clause_adv", "3", "GR", "语法", "Level 3 · Grammar",
     "Use because, if, unless, when, although, and so that to introduce adverbial clauses."),
    ("passive", "3", "GR", "语法", "Level 3 · Grammar",
     "Use the present and past simple passive, formed with be plus a past participle."),
    ("there_prep", "3", "GR", "语法", "Level 3 · Grammar",
     "Use there is/are and prepositions of place to describe what is somewhere and where things are."),
    ("tense", "3", "GR", "语法", "Level 3 · Grammar",
     "Use time expressions and context to choose among the simple present, simple past, simple future, continuous, and perfect tenses."),
    ("func_school", "3", "FU", "日常表达", "Level 3 · Everyday English",
     "Greet people, introduce yourself and family members, and talk about school subjects, routines, rules, and activities."),
    ("func_life", "3", "FU", "日常表达", "Level 3 · Everyday English",
     "Shop, order food, ask for directions, and talk about weather, appearance, animals, and current activities."),
    ("func_plan", "3", "FU", "日常表达", "Level 3 · Everyday English",
     "Invite people, accept or decline invitations, make suggestions, and talk about plans and past experiences."),
    ("func_view", "3", "FU", "日常表达", "Level 3 · Everyday English",
     "Express opinions, ask polite questions, explain customs, and exchange views about rules, health, and the environment."),
    ("read_detail", "3", "RW", "读写", "Level 3 · Reading and Writing",
     "Understand short texts on textbook topics and identify people, times, places, events, and reasons."),
    ("read_cloze", "3", "RW", "Level 3 · Reading and Writing",
     "Use context to choose words or sentences that make a passage coherent."),
    ("write_point", "3", "RW", "Level 3 · Reading and Writing",
     "Choose or complete sentences in a written response based on key points, keeping pronouns, tense, and content consistent."),
]

NOTE = {
    "语音": "Pronunciation items follow a common middle-school teaching sequence. The sequence has not been checked against the People's Education Press contents; volume and semester are pending verification.",
    "词汇": "Theme vocabulary from the corresponding Go for it! unit. The curriculum standard does not list every word; the word list and volume are pending verification.",
    "语法": "Grammar items follow the common sequence in Go for it! from Grade 7, Semester 1 through the full Grade 9 volume; volume and semester are pending verification.",
    "日常表达": "Functional language from the textbook. The curriculum standard does not list each expression; volume and semester are pending verification.",
    "读写": "Passages were written for diagnostic use and assess reading or writing skills; volume and semester are pending verification.",
}

# Chinese semester values are source tokens used by UNITS and rank(); chapter() translates them for display.
UNITS = {
    (7, "上", 1): "My name's Gina",
    (7, "上", 2): "This is my sister",
    (7, "上", 3): "Is this your pencil",
    (7, "上", 4): "Where's my schoolbag",
    (7, "上", 5): "Do you have a soccer ball",
    (7, "上", 6): "Do you like bananas",
    (7, "上", 7): "How much are these socks",
    (7, "上", 8): "When is your birthday",
    (7, "上", 9): "My favorite subject is science",
    (7, "下", 1): "Can you play the guitar",
    (7, "下", 2): "What time do you go to school",
    (7, "下", 3): "How do you get to school",
    (7, "下", 4): "Don't eat in class",
    (7, "下", 5): "Why do you like pandas",
    (7, "下", 6): "I'm watching TV",
    (7, "下", 7): "It's raining",
    (7, "下", 8): "Is there a post office near here",
    (7, "下", 9): "What does he look like",
    (7, "下", 10): "I'd like some noodles",
    (7, "下", 11): "How was your school trip",
    (7, "下", 12): "What did you do last weekend",
    (8, "上", 1): "Where did you go on vacation",
    (8, "上", 2): "How often do you exercise",
    (8, "上", 3): "I'm more outgoing than my sister",
    (8, "上", 4): "What's the best movie theater",
    (8, "上", 5): "Do you want to watch a game show",
    (8, "上", 6): "I'm going to study computer science",
    (8, "上", 7): "Will people have robots",
    (8, "上", 8): "How do you make a banana milk shake",
    (8, "上", 9): "Can you come to my party",
    (8, "上", 10): "If you go to the party, you'll have a great time",
    (8, "下", 1): "What's the matter",
    (8, "下", 2): "I'll help to clean up the city parks",
    (8, "下", 3): "Could you please clean your room",
    (8, "下", 4): "Why don't you talk to your parents",
    (8, "下", 5): "What were you doing when the rainstorm came",
    (8, "下", 6): "An old man tried to move the mountains",
    (8, "下", 7): "What's the highest mountain in the world",
    (8, "下", 8): "Have you read Treasure Island yet",
    (8, "下", 9): "Have you ever been to a museum",
    (8, "下", 10): "I've had this bike for three years",
    (9, "全", 1): "How can we become good learners",
    (9, "全", 2): "I think that mooncakes are delicious",
    (9, "全", 3): "Could you please tell me where the restrooms are",
    (9, "全", 4): "I used to be afraid of the dark",
    (9, "全", 5): "What are the shirts made of",
    (9, "全", 6): "When was it invented",
    (9, "全", 7): "Teenagers should be allowed to choose their own clothes",
    (9, "全", 8): "It must belong to Carla",
    (9, "全", 9): "I like music that I can dance to",
    (9, "全", 10): "You're supposed to shake hands",
    (9, "全", 11): "Sad movies make me cry",
    (9, "全", 12): "Life is full of the unexpected",
    (9, "全", 13): "We're trying to save the earth",
    (9, "全", 14): "I remember meeting all of you in Grade 7",
}


def load(name):
    with open(os.path.join(ROOT, "data", name), encoding="utf-8") as f:
        return json.load(f)


def dump(name, data):
    path = os.path.join(ROOT, "data", name)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def chapter(grade, sem, unit):
    title = UNITS[(grade, sem, unit)]
    semester = {"上": "Semester 1", "下": "Semester 2", "全": "Full year"}[sem]
    return "Grade %s, %s, Unit %d: %s" % (CN[grade], semester, unit, title)


def rank(grade, sem):
    return grade * 2 + (1 if sem == "下" else 0)


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


def reduce_junior(edges):
    """Remove redundant new edges from cne_j only. Leave math and elementary English edges unchanged."""
    adj = defaultdict(list)
    for e in edges:
        adj[e["topicId"]].append([e["prerequisiteId"], e["strength"]])
    kept = []
    dropped = 0
    for e in edges:
        if not str(e["topicId"]).startswith("cne_j"):
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


def build_standards():
    counters = {}
    id_of = {}
    items = []
    for symbol, level, code, domain, section, text in STANDARD_ROWS:
        if domain != EN_CODES[code]:
            raise SystemExit("Curriculum-standard domain mismatch: %s" % symbol)
        if level != "3":
            raise SystemExit("Middle school curriculum-standard level must be 3: %s" % symbol)
        key = (level, code)
        counters[key] = counters.get(key, 0) + 1
        sid = "ces-2022:%s.%s.%02d" % (level, code, counters[key])
        id_of[symbol] = sid
        items.append({
            "id": sid,
            "domain": DOMAIN_LABELS[domain],
            "section": section,
            "clause": "(%d)" % counters[key],
            "text": text,
            "page_or_ref": "pending verification",
            "verbatim": False,
            "text_status": "Public paraphrase; not checked page by page against Level 3 of the English Curriculum Standards for Compulsory Education (2022 Edition)",
        })
    return id_of, items


def build_question(tid, index, made, slot):
    qid = "%s_q%d" % (tid, index)
    if made["t"] == "numeric":
        return {
            "id": qid,
            "topicId": tid,
            "difficulty": made["d"],
            "type": "numeric",
            "prompt": made["p"],
            "answer": made["a"],
            "explanation": made["e"],
            "verify": made["v"],
        }, made["a"]
    texts = list(made["w"])
    texts.insert(slot % 4, made["a"])
    keys = list("ABCD")
    pos = texts.index(made["a"])
    return {
        "id": qid,
        "topicId": tid,
        "difficulty": made["d"],
        "type": "choice",
        "prompt": made["p"],
        "choices": [{"key": keys[i], "text": texts[i]} for i in range(4)],
        "answer": keys[pos],
        "explanation": made["e"],
        "verify": json.dumps(made["a"], ensure_ascii=False),
    }, made["a"]


def main():
    topics = load("topics.json")
    deps = load("dependencies.json")
    questions = load("questions.json")
    standards = load("cn-curriculum-standards.json")
    if any(str(t.get("id", "")).startswith("cne_j") for t in topics):
        print("cne_j topics already exist. enj_build.py cannot compile twice.", file=sys.stderr)
        return 1
    if not any(str(t.get("id", "")) == "cne_p001" for t in topics):
        print("Elementary English topic cne_p001 is missing; middle school topics cannot be compiled alone.", file=sys.stderr)
        return 1
    if not (180 <= len(TOPICS) <= 260):
        print("Topic count %d is outside the range 180–260" % len(TOPICS), file=sys.stderr)
        return 1
    if TOPICS[0]["key"] != enj_topics.SPINE[0]:
        print("The first topic does not match the topic spine", file=sys.stderr)
        return 1

    id_of_std, new_items = build_standards()
    index = {t["key"]: i for i, t in enumerate(TOPICS)}
    by_key = {t["key"]: t for t in TOPICS}
    names = {t["key"]: t["name"] for t in TOPICS}
    primary_id = {"p:%s" % t["key"]: "cne_p%03d" % i for i, t in enumerate(PRIMARY_TOPICS, start=1)}
    if len(primary_id) != 197:
        print("Elementary English topic count is not 197", file=sys.stderr)
        return 1

    hard_pairs = {}
    resolved_hard = []
    for src, dst, reason in HARD:
        if src not in index:
            print("Hard-prerequisite dependent topic is not registered: %s" % src, file=sys.stderr)
            return 1
        if dst.startswith("p:"):
            if dst not in primary_id:
                print("Hard prerequisite points to an unknown elementary topic: %s → %s" % (src, dst), file=sys.stderr)
                return 1
            pkey = dst[2:]
            pt = PRIMARY_BY_KEY[pkey]
            if rank(pt["grade"], pt["semester"]) > rank(by_key[src]["grade"], by_key[src]["semester"]):
                print("Elementary prerequisite comes later than the middle school topic: %s depends on %s" % (src, pkey), file=sys.stderr)
                return 1
            pid = primary_id[dst]
        else:
            if dst not in index:
                print("Hard prerequisite points to an unregistered topic: %s → %s" % (src, dst), file=sys.stderr)
                return 1
            if index[dst] >= index[src]:
                print("Hard prerequisite is not earlier than its dependent topic: %s depends on %s" % (src, dst), file=sys.stderr)
                return 1
            if rank(by_key[dst]["grade"], by_key[dst]["semester"]) > rank(by_key[src]["grade"], by_key[src]["semester"]):
                print("Hard prerequisite is in a later grade or semester: %s depends on %s" % (src, dst), file=sys.stderr)
                return 1
            pid = None
        if (src, dst) in hard_pairs:
            print("Duplicate hard edge %s → %s" % (src, dst), file=sys.stderr)
            return 1
        hard_pairs[(src, dst)] = reason
        resolved_hard.append((src, dst, pid, reason))

    for spec in TOPICS:
        if spec["std"] not in id_of_std:
            print("%s refers to missing curriculum standard %s" % (spec["key"], spec["std"]), file=sys.stderr)
            return 1
        spec["note"] = NOTE[spec["domain"]]
        if (spec["grade"], spec["semester"], spec["unit"]) not in UNITS:
            print("%s refers to a missing unit: Grade %s, semester %s, Unit %s" % (spec["key"], spec["grade"], spec["semester"], spec["unit"]), file=sys.stderr)
            return 1
        if spec["grade"] not in (7, 8, 9):
            print("%s is not in Grades 7–9" % spec["key"], file=sys.stderr)
            return 1
        if spec["grade"] == 9 and spec["semester"] != "全":
            print("%s must use the full-year Grade 9 volume" % spec["key"], file=sys.stderr)
            return 1
        if spec["grade"] != 9 and spec["semester"] not in ("上", "下"):
            print("%s has an invalid semester token" % spec["key"], file=sys.stderr)
            return 1

    new_topics = []
    new_questions = []
    id_of = {}
    for i, spec in enumerate(TOPICS, start=1):
        tid = "cne_j%03d" % i
        id_of[spec["key"]] = tid
        made = materialise_questions(spec)
        for q in made:
            check_question(spec["key"], q)
        built = []
        diag_answer = None
        for n, item in enumerate(made, start=1):
            q, shown = build_question(tid, n, item, slot=i + n)
            built.append(q)
            if n == 1:
                diag_answer = shown
        ref = {"id": id_of_std[spec["std"]], "confidence": spec["conf"]}
        if spec.get("note"):
            ref["note"] = spec["note"]
        topic = {
            "id": tid,
            "name": spec["name"],
            "domain": DOMAIN_LABELS[spec["domain"]],
            "grade": spec["grade"],
            # "上", "下", and "全" are semester tokens consumed by the topic-scope readers.
            "semester": spec["semester"],
            "chapter": chapter(spec["grade"], spec["semester"], spec["unit"]),
            "type": spec["type"],
            "description": spec["description"],
            "mastery_criteria": spec["mastery_criteria"],
            "diagnostic_question": {"question": built[0]["prompt"], "answer": diag_answer},
            "external": False,
            "subject": "english",
            "standards": [ref],
        }
        new_topics.append(topic)
        new_questions.extend(built)

    raw = []
    for i in range(1, len(TOPICS)):
        cur = TOPICS[i]["key"]
        prev = TOPICS[i - 1]["key"]
        if (cur, prev) in hard_pairs:
            continue
        reason = "Following the usual Go for it! teaching sequence, study %s before %s." % (names[prev], names[cur])
        raw.append((cur, prev, "soft", reason, id_of[prev]))
    for src, dst, pid, reason in resolved_hard:
        pre_id = pid if pid else id_of[dst]
        raw.append((src, dst, "hard", reason, pre_id))

    # The first middle school topic has no previous unit and must have an elementary prerequisite.
    if not any(src == TOPICS[0]["key"] for src, _, _, _, _ in raw):
        print("The first middle school topic has no prerequisite", file=sys.stderr)
        return 1

    new_edges = []
    seen = set()
    for src, dst, strength, reason, pre_id in raw:
        key = (id_of[src], pre_id)
        if key in seen:
            print("Duplicate edge %s → %s" % key, file=sys.stderr)
            return 1
        seen.add(key)
        if not str(pre_id).startswith("cne_"):
            print("English edge points to a non-English topic: %s" % pre_id, file=sys.stderr)
            return 1
        new_edges.append({
            "topicId": id_of[src],
            "prerequisiteId": pre_id,
            "strength": strength,
            "reason": reason,
        })

    merged_deps, dropped = reduce_junior(deps + new_edges)
    jun_edges = [e for e in merged_deps if str(e["topicId"]).startswith("cne_j")]
    if any(not str(e["prerequisiteId"]).startswith("cne_") for e in jun_edges):
        print("A middle school English edge points to a math topic", file=sys.stderr)
        return 1
    if any(str(e["topicId"]).startswith("cne_j") for e in deps):
        print("Existing dependencies already contain middle school English edges", file=sys.stderr)
        return 1
    covered = {e["topicId"] for e in jun_edges}
    missing = [t["id"] for t in new_topics if t["id"] not in covered]
    if missing:
        print("Topics still without prerequisites after reduction: %s" % ", ".join(missing), file=sys.stderr)
        return 1
    cross = [e for e in jun_edges if str(e["prerequisiteId"]).startswith("cne_p")]
    if len(cross) < 8:
        print("Only %d edges point to elementary English" % len(cross), file=sys.stderr)
        return 1

    checked = verify_all(new_questions)
    if checked["mismatch"] or checked["unverifiable"]:
        for m in checked["mismatch"][:40]:
            print("Question verification failed for %s: %s" % (m["id"], m.get("detail")), file=sys.stderr)
        print("Question verification failed: %d mismatches, %d unverifiable" % (
            len(checked["mismatch"]), len(checked["unverifiable"])), file=sys.stderr)
        return 1

    n_hard = sum(1 for e in jun_edges if e["strength"] == "hard")
    n_soft = sum(1 for e in jun_edges if e["strength"] == "soft")
    n_cross_h = sum(1 for e in cross if e["strength"] == "hard")
    n_cross_s = sum(1 for e in cross if e["strength"] == "soft")
    by_grade = Counter("%d%s" % (t["grade"], t["semester"]) for t in new_topics)
    by_dom = Counter(t["domain"] for t in new_topics)
    print("Middle school English topics: %d" % len(new_topics))
    # These keys preserve the source semester tokens; only the printed labels are translated.
    for k, label in [("7上", "Grade 7, Semester 1"), ("7下", "Grade 7, Semester 2"),
                     ("8上", "Grade 8, Semester 1"), ("8下", "Grade 8, Semester 2"),
                     ("9全", "Grade 9, full year")]:
        print("  %s: %d" % (label, by_grade[k]))
    for k, v in by_dom.most_common():
        print("  %s: %d" % (DOMAIN_LABELS[k], v))
    print("Middle school English edges: %d (reduced by %d); hard: %d; soft: %d" % (len(jun_edges), dropped, n_hard, n_soft))
    print("Of these, cross-stage edges: %d (hard: %d; soft: %d)" % (len(cross), n_cross_h, n_cross_s))
    print("Questions: %d" % len(new_questions))
    print("Curriculum-standard entries: %d" % len(new_items))

    old_topic_n = len(topics)
    old_dep_n = len(deps)
    old_q_n = len(questions)
    old_std_n = len(standards["items"])
    old_ids = [(t["id"], t["name"]) for t in topics]
    eng = standards.get("english")
    if not isinstance(eng, dict):
        print("English curriculum-standard object is missing", file=sys.stderr)
        return 1
    eng["stage"] = "Level 1 (Grades 3–4), Level 2 (Grades 5–6), and Level 3 (Grades 7–9)"
    eng["note"] = (
        "Entries paraphrase publicly available language-knowledge descriptions for Levels 1 (Grades 3–4), 2 (Grades 5–6), and 3 (Grades 7–9); they are not checked page by page against the source. "
        "verbatim is false and page_or_ref is pending verification. IDs beginning ces-2022 are assigned by this graph and are not original Ministry of Education IDs. "
        "Elementary topics follow the common People's Education Press PEP sequence starting in Grade 3; middle school topics follow the common Go for it! sequence from Grade 7, Semester 1 through the full Grade 9 volume. Page numbers are not included."
    )
    standards["items"].extend(new_items)
    dump("topics.json", topics + new_topics)
    dump("dependencies.json", merged_deps)
    dump("questions.json", questions + new_questions)
    dump("cn-curriculum-standards.json", standards)

    again_t = load("topics.json")
    again_d = load("dependencies.json")
    again_q = load("questions.json")
    again_s = load("cn-curriculum-standards.json")
    if again_t[:old_topic_n] != topics or [(t["id"], t["name"]) for t in again_t[:old_topic_n]] != old_ids:
        print("Existing topics changed after writing", file=sys.stderr)
        return 1
    if again_d[:old_dep_n] != deps or again_q[:old_q_n] != questions:
        print("Existing edges or questions changed after writing", file=sys.stderr)
        return 1
    if again_s["items"][:old_std_n] != standards["items"][:old_std_n]:
        print("Existing curriculum-standard entries changed after writing", file=sys.stderr)
        return 1
    print("Existing topics whose IDs and names are unchanged: %d" % len(old_ids))
    return 0


if __name__ == "__main__":
    sys.exit(main())
