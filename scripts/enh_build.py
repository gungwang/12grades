#!/usr/bin/env python3
"""Compile senior-high English drafts into data/topics.json, dependencies.json, questions.json, and the curriculum-standard file.

Only append cne_h topics. Do not change existing math, primary-English, or junior-high-English IDs or names, and do not reduce pre-existing edges.
Prerequisites may point to junior-high or primary English, but not mathematics.

Usage: python3 scripts/enh_build.py
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

JUNIOR_TOPICS = list(en_lib.TOPICS)
JUNIOR_BY_KEY = {t["key"]: t for t in JUNIOR_TOPICS}
en_lib.TOPICS = []
en_lib.HARD = []

import enh_topics  # noqa: E402
from en_lib import HARD, TOPICS, check_question, materialise_questions  # noqa: E402
from enh_edges import SOFT  # noqa: E402
from verify_questions import verify_all  # noqa: E402

# These domain labels are schema values shared with enh_topics.py and must stay unchanged for validation.
EN_CODES = {"PH": "语音", "VO": "词汇", "GR": "语法", "FU": "日常表达", "RW": "读写"}
DOMAIN_DISPLAY = dict(zip(EN_CODES.values(), ("Phonetics", "Vocabulary", "Grammar", "Everyday Communication", "Reading and Writing")))

# Curriculum-standard items are paraphrases of public descriptions, not text verified page by page.
# Band: B = compulsory; S = selective compulsory. The ces-2017 identifiers are defined by this graph.
STANDARD_ROWS = [
    ("stress", "B", "PH", "语音", "Compulsory · Phonetics",
     "Use word stress to distinguish parts of speech and meanings, and place stress correctly when reading multisyllabic words aloud."),
    ("tone_b", "B", "PH", "语音", "Compulsory · Phonetics",
     "Read statements and wh-questions with falling intonation and yes/no questions with rising intonation; begin to recognize differences in attitude."),
    ("link", "B", "PH", "语音", "Compulsory · Phonetics",
     "Identify linking and unreleased stops within thought groups, and apply these patterns when reading phrases aloud."),
    ("attitude", "S", "PH", "语音", "Selective Compulsory · Phonetics",
     "Use intonation to express attitudes such as surprise, hesitation, emphasis, or politeness, rather than only distinguishing rising and falling tones."),
    ("weak", "S", "PH", "语音", "Selective Compulsory · Phonetics",
     "Recognize reduced forms of function words in sentences and read longer sentences with appropriate rhythm."),
    ("vo_school", "B", "VO", "词汇", "Compulsory · Vocabulary",
     "Understand vocabulary about school life, courses, clubs, and adapting to a new school in context. The word list follows the curriculum-standard appendix; this clause is a paraphrase."),
    ("vo_world", "B", "VO", "词汇", "Compulsory · Vocabulary",
     "Understand vocabulary about travel, sports, disasters, languages, the internet, and music in context. The word list follows the curriculum-standard appendix; this clause is a paraphrase."),
    ("vo_soc", "B", "VO", "词汇", "Compulsory · Vocabulary",
     "Understand vocabulary about cultural heritage, wildlife, historical traditions, festivals, ethics, multiculturalism, space exploration, and the value of money in context. The word list follows the curriculum-standard appendix; this clause is a paraphrase."),
    ("vo_form", "B", "VO", "词汇", "Compulsory · Vocabulary",
     "Use common prefixes, suffixes, and changes in word class to infer the meanings of derived words. The specific affix list follows the curriculum-standard appendix; this clause is a paraphrase."),
    ("vo_people", "S", "VO", "词汇", "Selective Compulsory · Vocabulary",
     "Understand vocabulary about people's achievements, future life, parks, body language, and agriculture in context. The word list follows the curriculum-standard appendix; this clause is a paraphrase."),
    ("vo_life", "S", "VO", "词汇", "Selective Compulsory · Vocabulary",
     "Understand vocabulary about scientific research, intercultural communication, food, long-distance travel, and first aid in context. The word list follows the curriculum-standard appendix; this clause is a paraphrase."),
    ("vo_mind", "S", "VO", "词汇", "Selective Compulsory · Vocabulary",
     "Understand vocabulary about art, healthy lifestyles, environmental protection, adversity, and poetry in context. The word list follows the curriculum-standard appendix; this clause is a paraphrase."),
    ("vo_work", "S", "VO", "词汇", "Selective Compulsory · Vocabulary",
     "Understand vocabulary about science fiction, landmarks, ocean exploration, public-interest sharing, and career planning in context. The word list follows the curriculum-standard appendix; this clause is a paraphrase."),
    ("sent", "B", "GR", "语法", "Compulsory · Grammar",
     "Identify subjects, predicates, objects, predicatives, adverbials, attributives, and complements; distinguish basic sentence patterns such as subject-verb, subject-verb-object, subject-linking verb-predicative, double-object, and object-complement."),
    ("phrase", "B", "GR", "语法", "Compulsory · Grammar",
     "Identify noun, adjective, and adverb phrases and determine their functions in sentences."),
    ("tense", "B", "GR", "语法", "Compulsory · Grammar",
     "Use the present continuous for arranged future events and the simple present for future events in time and conditional clauses; choose among the simple present, simple past, simple future, and present perfect in context."),
    ("tag", "B", "GR", "语法", "Compulsory · Grammar",
     "Use tag questions to confirm information, matching the tag's subject, auxiliary, and positive or negative form to the preceding statement."),
    ("rel", "B", "GR", "语法", "Compulsory · Grammar",
     "Use the relative pronouns who, whom, whose, which, and that and the relative adverbs when, where, and why in restrictive relative clauses; distinguish restrictive from nonrestrictive relative clauses."),
    ("passive", "B", "GR", "语法", "Compulsory · Grammar",
     "Use the present continuous and present perfect passive. The continuous passive uses be being plus a past participle; the perfect passive uses have been plus a past participle."),
    ("ing", "B", "GR", "语法", "Compulsory · Grammar",
     "Use the -ing form of a verb as an attributive, predicative, object complement, or adverbial."),
    ("pp", "B", "GR", "语法", "Compulsory · Grammar",
     "Use past participles as attributives, predicatives, object complements, and adverbials."),
    ("toinf", "B", "GR", "语法", "Compulsory · Grammar",
     "Use infinitives as subjects, objects, predicatives, attributives, adverbials, and object complements, and recognize cases where to is omitted."),
    ("modal", "B", "GR", "语法", "Compulsory · Grammar",
     "Use modal verbs to express probability, obligation, and advice; understand must, could, should, and similar modals plus have done as judgments about the past."),
    ("reported", "B", "GR", "语法", "Compulsory · Grammar",
     "Change direct speech to reported speech and account for changes in person, time expressions, and tense."),
    ("nouncls", "S", "GR", "语法", "Selective Compulsory · Grammar",
     "Use that, whether, and question words to introduce subject, predicative, and appositive clauses; distinguish appositive clauses from relative clauses."),
    ("nonfin", "S", "GR", "语法", "Selective Compulsory · Grammar",
     "Use perfect and passive forms of -ing forms and infinitives, and choose among to do, doing, and done in context."),
    ("subj", "S", "GR", "语法", "Selective Compulsory · Grammar",
     "Use the subjunctive mood for hypothetical situations contrary to present, past, or future facts, and in clauses with wish, if only, as if, and expressions of suggestion, command, or request."),
    ("invert", "S", "GR", "语法", "Selective Compulsory · Grammar",
     "Use inversion after negative adverbs, only plus an adverbial, so, neither, and conditional clauses with if omitted."),
    ("emph", "S", "GR", "语法", "Selective Compulsory · Grammar",
     "Use cleft sentences with It is or It was, the focused element, and that or who; use the auxiliary do to emphasize a verb."),
    ("ellip", "S", "GR", "语法", "Selective Compulsory · Grammar",
     "Recognize and use ellipsis to avoid repeating an already stated verb, material after an infinitive marker to, or an identical clause element."),
    ("advcls", "S", "GR", "语法", "Selective Compulsory · Grammar",
     "Use adverbial clauses introduced by although, even though, while, so that, in case, unless, and as long as to express concession, contrast, purpose, and condition."),
    ("mix", "S", "GR", "语法", "Selective Compulsory · Grammar",
     "Integrate tense, voice, non-finite forms, and clauses when analyzing longer sentences and passages."),
    ("fu_daily", "B", "FU", "日常表达", "Compulsory · Everyday Communication",
     "Greet others, introduce yourself, and talk about courses, clubs, and school life."),
    ("fu_plan", "B", "FU", "日常表达", "Compulsory · Everyday Communication",
     "Talk about arranged plans, make or respond to invitations, and give advice about travel and sports."),
    ("fu_view", "B", "FU", "日常表达", "Compulsory · Everyday Communication",
     "Exchange views on culture, the environment, traditions, and values, and explain reasons."),
    ("fu_desc", "S", "FU", "日常表达", "Selective Compulsory · Everyday Communication",
     "Describe people's achievements, body language, places, and processes, and give clear steps."),
    ("fu_argue", "S", "FU", "日常表达", "Selective Compulsory · Everyday Communication",
     "Explain scientific hypotheses, compare cultural differences, discuss health and the environment, and offer evidence-based views."),
    ("fu_plan_s", "S", "FU", "日常表达", "Selective Compulsory · Everyday Communication",
     "Talk about career plans, applications, and public-service arrangements, and make polite requests."),
    ("rw_detail", "B", "RW", "读写", "Compulsory · Reading and Writing",
     "Read narratives and expository texts on textbook topics and identify people, times, places, events, and reasons."),
    ("rw_main", "B", "RW", "读写", "Compulsory · Reading and Writing",
     "Summarize a passage's main idea and determine whether the author's attitude is supportive, concerned, or simply factual."),
    ("rw_write", "B", "RW", "读写", "Compulsory · Reading and Writing",
     "Choose or complete sentences in an email, poster, or report using the required points and consistent person and tense."),
    ("rw_infer", "S", "RW", "读写", "Selective Compulsory · Reading and Writing",
     "Infer word meaning, pronoun reference, and the author's unstated attitude from context."),
    ("rw_argue", "S", "RW", "读写", "Selective Compulsory · Reading and Writing",
     "Identify claims, supporting evidence, and paragraph functions in argumentative and expository texts."),
    ("rw_write_s", "S", "RW", "读写", "Selective Compulsory · Reading and Writing",
     "Choose sentences for a summary, application, set of instructions, or short opinion text based on key points, maintaining logical flow and consistent person."),
]

NOTE = {
    "语音": "Phonetics topics follow the common teaching sequence in the 2019 PEP edition. The PEP contents page was not checked; volume assignments need verification.",
    "词汇": "These are theme words from units in the 2019 PEP edition. The curriculum standard does not list every word; the word list and volume assignment need verification.",
    "语法": "Sentence patterns follow the common sequence in compulsory and selective compulsory units in the 2019 PEP edition; volume assignments need verification.",
    "日常表达": "These are functional expressions from the textbook. The curriculum standard does not list each expression; volume assignments need verification.",
    "读写": "Passages were written for diagnostic purposes and test reading or writing skills; volume assignments need verification.",
}

# (grade, unit) -> (volume name, unit label or Welcome Unit, English unit title)
TITLES = {
    (10, 0): ("Compulsory Volume 1", "Welcome Unit", "Welcome Unit"),
    (10, 1): ("Compulsory Volume 1", "Unit 1", "Teenage Life"),
    (10, 2): ("Compulsory Volume 1", "Unit 2", "Travelling Around"),
    (10, 3): ("Compulsory Volume 1", "Unit 3", "Sports and Fitness"),
    (10, 4): ("Compulsory Volume 1", "Unit 4", "Natural Disasters"),
    (10, 5): ("Compulsory Volume 1", "Unit 5", "Languages Around the World"),
    (11, 1): ("Compulsory Volume 2", "Unit 1", "Cultural Heritage"),
    (11, 2): ("Compulsory Volume 2", "Unit 2", "Wildlife Protection"),
    (11, 3): ("Compulsory Volume 2", "Unit 3", "The Internet"),
    (11, 4): ("Compulsory Volume 2", "Unit 4", "History and Traditions"),
    (11, 5): ("Compulsory Volume 2", "Unit 5", "Music"),
    (12, 1): ("Compulsory Volume 3", "Unit 1", "Festivals and Celebrations"),
    (12, 2): ("Compulsory Volume 3", "Unit 2", "Morals and Virtues"),
    (12, 3): ("Compulsory Volume 3", "Unit 3", "Diverse Cultures"),
    (12, 4): ("Compulsory Volume 3", "Unit 4", "Space Exploration"),
    (12, 5): ("Compulsory Volume 3", "Unit 5", "The Value of Money"),
    (13, 1): ("Selective Compulsory Volume 1", "Unit 1", "People of Achievement"),
    (13, 2): ("Selective Compulsory Volume 1", "Unit 2", "Looking into the Future"),
    (13, 3): ("Selective Compulsory Volume 1", "Unit 3", "Fascinating Parks"),
    (13, 4): ("Selective Compulsory Volume 1", "Unit 4", "Body Language"),
    (13, 5): ("Selective Compulsory Volume 1", "Unit 5", "Working the Land"),
    (14, 1): ("Selective Compulsory Volume 2", "Unit 1", "Science and Scientists"),
    (14, 2): ("Selective Compulsory Volume 2", "Unit 2", "Bridging Cultures"),
    (14, 3): ("Selective Compulsory Volume 2", "Unit 3", "Food and Culture"),
    (14, 4): ("Selective Compulsory Volume 2", "Unit 4", "Journey Across a Vast Land"),
    (14, 5): ("Selective Compulsory Volume 2", "Unit 5", "First Aid"),
    (15, 1): ("Selective Compulsory Volume 3", "Unit 1", "Art"),
    (15, 2): ("Selective Compulsory Volume 3", "Unit 2", "Healthy Lifestyle"),
    (15, 3): ("Selective Compulsory Volume 3", "Unit 3", "Environmental Protection"),
    (15, 4): ("Selective Compulsory Volume 3", "Unit 4", "Adversity and Courage"),
    (15, 5): ("Selective Compulsory Volume 3", "Unit 5", "Poems"),
    (16, 1): ("Selective Compulsory Volume 4", "Unit 1", "Science Fiction"),
    (16, 2): ("Selective Compulsory Volume 4", "Unit 2", "Iconic Attractions"),
    (16, 3): ("Selective Compulsory Volume 4", "Unit 3", "Sea Exploration"),
    (16, 4): ("Selective Compulsory Volume 4", "Unit 4", "Sharing"),
    (16, 5): ("Selective Compulsory Volume 4", "Unit 5", "Launching Your Career"),
}

BOOK_GRADE = {
    "Compulsory Volume 1": 10,
    "Compulsory Volume 2": 11,
    "Compulsory Volume 3": 12,
    "Selective Compulsory Volume 1": 13,
    "Selective Compulsory Volume 2": 14,
    "Selective Compulsory Volume 3": 15,
    "Selective Compulsory Volume 4": 16,
}


def load(name):
    with open(os.path.join(ROOT, "data", name), encoding="utf-8") as f:
        return json.load(f)


def dump(name, data):
    path = os.path.join(ROOT, "data", name)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def chapter(grade, unit):
    book, no, title = TITLES[(grade, unit)]
    return "%s %s %s" % (book, no, title)


# Semester markers are schema values shared with topics.json; keep them unchanged.
def rank_of(grade, semester):
    return grade * 2 + (1 if semester == "下" else 0)


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


def reduce_senior(edges):
    """Remove only redundant new edges for cne_h topics; leave math, primary-English, and junior-high-English edges unchanged."""
    adj = defaultdict(list)
    for e in edges:
        adj[e["topicId"]].append([e["prerequisiteId"], e["strength"]])
    kept = []
    dropped = 0
    for e in edges:
        if not str(e["topicId"]).startswith("cne_h"):
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
    band_of = {}
    items = []
    for symbol, band, code, domain, section, text in STANDARD_ROWS:
        if domain != EN_CODES[code]:
            raise SystemExit("Curriculum-standard domain mismatch: %s" % symbol)
        if band not in ("B", "S"):
            raise SystemExit("Curriculum-standard band must be B or S: %s" % symbol)
        key = (band, code)
        counters[key] = counters.get(key, 0) + 1
        sid = "ces-2017:H.%s.%s.%02d" % (band, code, counters[key])
        id_of[symbol] = sid
        band_of[symbol] = band
        items.append({
            "id": sid,
            "domain": DOMAIN_DISPLAY[domain],
            "section": section,
            "clause": "(%d)" % counters[key],
            "text": text,
            "page_or_ref": "Needs verification",
            "verbatim": False,
            "text_status": "Public paraphrase; not checked page by page against the Senior High School English Curriculum Standards (2017 Edition, revised in 2020)",
        })
    return id_of, band_of, items


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


def resolve_pre(src, dst, index, by_key, primary_id, junior_id):
    """Return a prerequisite ID on success; internal edges return a key for the caller to convert to a cne_h ID. Return None on failure."""
    if dst.startswith("p:"):
        if dst not in primary_id:
            print("Prerequisite points to an unknown primary-school topic: %s → %s" % (src, dst), file=sys.stderr)
            return None
        pkey = dst[2:]
        pt = PRIMARY_BY_KEY[pkey]
        if rank_of(pt["grade"], pt["semester"]) > rank_of(by_key[src]["grade"], by_key[src]["semester"]):
            print("Primary-school prerequisite occurs after the senior-high topic: %s depends on %s" % (src, pkey), file=sys.stderr)
            return None
        return primary_id[dst]
    if dst.startswith("j:"):
        if dst not in junior_id:
            print("Prerequisite points to an unknown junior-high topic: %s → %s" % (src, dst), file=sys.stderr)
            return None
        jkey = dst[2:]
        jt = JUNIOR_BY_KEY[jkey]
        if rank_of(jt["grade"], jt["semester"]) > rank_of(by_key[src]["grade"], by_key[src]["semester"]):
            print("Junior-high prerequisite occurs after the senior-high topic: %s depends on %s" % (src, jkey), file=sys.stderr)
            return None
        return junior_id[dst]
    if dst not in index:
        print("Prerequisite points to an unregistered topic: %s → %s" % (src, dst), file=sys.stderr)
        return None
    if index[dst] >= index[src]:
        print("Prerequisite is not earlier than its dependent topic: %s depends on %s" % (src, dst), file=sys.stderr)
        return None
    if rank_of(by_key[dst]["grade"], by_key[dst]["semester"]) > rank_of(by_key[src]["grade"], by_key[src]["semester"]):
        print("Prerequisite is in a later grade: %s depends on %s" % (src, dst), file=sys.stderr)
        return None
    return "key:" + dst


def main():
    topics = load("topics.json")
    deps = load("dependencies.json")
    questions = load("questions.json")
    standards = load("cn-curriculum-standards.json")
    if any(str(t.get("id", "")).startswith("cne_h") for t in topics):
        print("cne_h topics already exist. enh_build.py cannot compile them again.", file=sys.stderr)
        return 1
    if not any(str(t.get("id", "")) == "cne_j001" for t in topics):
        print("Junior-high English topic cne_j001 is missing; senior-high topics cannot be compiled alone.", file=sys.stderr)
        return 1
    if not (220 <= len(TOPICS) <= 320):
        print("Topic count %d is outside the expected range of 220–320." % len(TOPICS), file=sys.stderr)
        return 1
    # This imported topic name is the validation sentinel used by the source data.
    if not any(t["name"] == "Subjunctive Mood" for t in TOPICS):
        print("The required subjunctive-mood topic is missing.", file=sys.stderr)
        return 1

    id_of_std, band_of, new_items = build_standards()
    index = {t["key"]: i for i, t in enumerate(TOPICS)}
    by_key = {t["key"]: t for t in TOPICS}
    names = {t["key"]: t["name"] for t in TOPICS}
    primary_id = {"p:%s" % t["key"]: "cne_p%03d" % i for i, t in enumerate(PRIMARY_TOPICS, start=1)}
    junior_id = {"j:%s" % t["key"]: "cne_j%03d" % i for i, t in enumerate(JUNIOR_TOPICS, start=1)}
    if len(primary_id) != 197:
        print("Primary-English topic count is not 197.", file=sys.stderr)
        return 1
    if not (180 <= len(junior_id) <= 260):
        print("Junior-high English topic count %d is outside 180–260." % len(junior_id), file=sys.stderr)
        return 1

    for spec in TOPICS:
        if spec["std"] not in id_of_std:
            print("%s references unknown curriculum standard %s." % (spec["key"], spec["std"]), file=sys.stderr)
            return 1
        band = band_of[spec["std"]]
        if spec["grade"] <= 12 and band != "B":
            print("%s is in a compulsory volume but references selective-compulsory standard %s." % (spec["key"], spec["std"]), file=sys.stderr)
            return 1
        if spec["grade"] >= 13 and band != "S":
            print("%s is in a selective-compulsory volume but references compulsory standard %s." % (spec["key"], spec["std"]), file=sys.stderr)
            return 1
        spec["note"] = NOTE[spec["domain"]]
        if (spec["grade"], spec["unit"]) not in TITLES:
            print("%s references an unknown unit: grade %s, unit %s." % (spec["key"], spec["grade"], spec["unit"]), file=sys.stderr)
            return 1
        if spec["grade"] not in BOOK_GRADE.values():
            print("%s has a grade outside 10–16." % spec["key"], file=sys.stderr)
            return 1
        # The semester marker matches the source-data schema and must not be translated.
        if spec["semester"] != "上":
            print("%s must use the first-semester marker for senior-high English." % spec["key"], file=sys.stderr)
            return 1
        book = TITLES[(spec["grade"], spec["unit"])][0]
        if BOOK_GRADE[book] != spec["grade"]:
            print("%s has a volume that does not match its grade." % spec["key"], file=sys.stderr)
            return 1

    hard_pairs = {}
    resolved_hard = []
    for src, dst, reason in HARD:
        if src not in index:
            print("Hard-edge dependent topic is not registered: %s" % src, file=sys.stderr)
            return 1
        if (src, dst) in hard_pairs:
            print("Duplicate hard edge: %s → %s" % (src, dst), file=sys.stderr)
            return 1
        pid = resolve_pre(src, dst, index, by_key, primary_id, junior_id)
        if pid is None:
            return 1
        hard_pairs[(src, dst)] = reason
        resolved_hard.append((src, dst, pid, reason))

    soft_pairs = {}
    resolved_soft = []
    for src, dst, reason in SOFT:
        if src not in index:
            print("Soft-edge dependent topic is not registered: %s" % src, file=sys.stderr)
            return 1
        if (src, dst) in soft_pairs or (src, dst) in hard_pairs:
            print("Duplicate soft edge or edge repeated as hard: %s → %s" % (src, dst), file=sys.stderr)
            return 1
        pid = resolve_pre(src, dst, index, by_key, primary_id, junior_id)
        if pid is None:
            return 1
        soft_pairs[(src, dst)] = reason
        resolved_soft.append((src, dst, pid, reason))

    new_topics = []
    new_questions = []
    id_of = {}
    for i, spec in enumerate(TOPICS, start=1):
        tid = "cne_h%03d" % i
        id_of[spec["key"]] = tid
        made = materialise_questions(spec)
        if not (3 <= len(made) <= 5):
            print("%s has %d questions, outside the expected range of 3–5." % (spec["key"], len(made)), file=sys.stderr)
            return 1
        for item in made:
            check_question(spec["key"], item)
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
            "domain": DOMAIN_DISPLAY[spec["domain"]],
            "grade": spec["grade"],
            "semester": spec["semester"],
            "chapter": chapter(spec["grade"], spec["unit"]),
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
        if (cur, prev) in hard_pairs or (cur, prev) in soft_pairs:
            continue
        reason = "Following the common teaching sequence in the 2019 PEP edition, learn \"%s\" before \"%s\". Volume assignment needs verification." % (names[prev], names[cur])
        raw.append((cur, prev, "soft", reason, id_of[prev]))
    def edge_id(pid):
        if str(pid).startswith("key:"):
            return id_of[pid[4:]]
        return pid

    for src, dst, pid, reason in resolved_soft:
        raw.append((src, dst, "soft", reason, edge_id(pid)))
    for src, dst, pid, reason in resolved_hard:
        raw.append((src, dst, "hard", reason, edge_id(pid)))

    if not any(src == TOPICS[0]["key"] for src, _, _, _, _ in raw):
        print("The first senior-high topic has no prerequisite.", file=sys.stderr)
        return 1

    new_edges = []
    seen = set()
    for src, dst, strength, reason, pre_id in raw:
        key = (id_of[src], pre_id)
        if key in seen:
            print("Duplicate edge: %s → %s" % key, file=sys.stderr)
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

    merged_deps, dropped = reduce_senior(deps + new_edges)
    hs_edges = [e for e in merged_deps if str(e["topicId"]).startswith("cne_h")]
    if any(not str(e["prerequisiteId"]).startswith("cne_") for e in hs_edges):
        print("A senior-high English edge points to a math topic.", file=sys.stderr)
        return 1
    if any(str(e["topicId"]).startswith("cne_h") for e in deps):
        print("The original dependencies already contain senior-high English edges.", file=sys.stderr)
        return 1
    covered = {e["topicId"] for e in hs_edges}
    missing = [t["id"] for t in new_topics if t["id"] not in covered]
    if missing:
        print("Topics still without prerequisites after reduction: %s" % ", ".join(missing[:20]), file=sys.stderr)
        return 1
    cross_j = [e for e in hs_edges if str(e["prerequisiteId"]).startswith("cne_j")]
    cross_p = [e for e in hs_edges if str(e["prerequisiteId"]).startswith("cne_p")]
    if len(cross_j) < 8:
        print("Only %d edges point to junior-high English." % len(cross_j), file=sys.stderr)
        return 1
    n_hard = sum(1 for e in hs_edges if e["strength"] == "hard")
    n_soft = sum(1 for e in hs_edges if e["strength"] == "soft")
    if n_soft <= n_hard:
        print("Soft prerequisites (%d) do not outnumber hard prerequisites (%d)." % (n_soft, n_hard), file=sys.stderr)
        return 1

    checked = verify_all(new_questions)
    if checked["mismatch"] or checked["unverifiable"]:
        for m in checked["mismatch"][:40]:
            print("Question check failed for %s: %s" % (m["id"], m.get("detail")), file=sys.stderr)
        print("Question check did not pass: %d mismatches, %d unverifiable." % (
            len(checked["mismatch"]), len(checked["unverifiable"])), file=sys.stderr)
        return 1

    by_grade = Counter(t["grade"] for t in new_topics)
    by_dom = Counter(t["domain"] for t in new_topics)
    book_name = {10: "Compulsory Vol. 1", 11: "Compulsory Vol. 2", 12: "Compulsory Vol. 3", 13: "Selective Compulsory Vol. 1", 14: "Selective Compulsory Vol. 2", 15: "Selective Compulsory Vol. 3", 16: "Selective Compulsory Vol. 4"}
    print("Senior-high English topics: %d" % len(new_topics))
    for g in range(10, 17):
        print("  %s %d" % (book_name[g], by_grade[g]))
    for k, v in by_dom.most_common():
        print("  %s %d" % (k, v))
    print("Senior-high English edges written: %d (reduced edges removed: %d); hard: %d, soft: %d" % (len(hs_edges), dropped, n_hard, n_soft))
    print("Cross-level edges: %d to junior high, %d to primary school" % (len(cross_j), len(cross_p)))
    print("Questions: %d" % len(new_questions))
    print("Curriculum-standard items: %d" % len(new_items))
    # This imported topic-name sentinel is used for validation and lookup.
    sub_id = next(t["id"] for t in new_topics if t["name"] == "Subjunctive Mood")
    print("Subjunctive mood topic: %s" % sub_id)

    eng = standards.get("english")
    if not isinstance(eng, dict):
        print("Missing the english curriculum-standard object.", file=sys.stderr)
        return 1
    eng["stage"] = "Compulsory-education Levels 1–3; senior-high compulsory and selective compulsory"
    eng["note"] = (
        "The compulsory-education section paraphrases public descriptions of language knowledge for Level 1 (grades 3–4), Level 2 (grades 5–6), and Level 3 (grades 7–9). "
        "The senior-high section paraphrases the compulsory and selective-compulsory language requirements in the Senior High School English Curriculum Standards (2017 Edition, revised in 2020); "
        "it is not a separate senior-high English standard issued in 2022 and is not text verified page by page. "
        "`verbatim` is false and `page_or_ref` is \"Needs verification\". "
        "The ces-2022 identifiers correspond to compulsory education, ces-2017:H.B to senior-high compulsory, and ces-2017:H.S to senior-high selective compulsory; none are official Ministry of Education identifiers. "
        "Senior-high topics follow the commonly used unit titles in the 2019 PEP edition's three compulsory and four selective-compulsory volumes. Page numbers are omitted; volume assignments need verification."
    )
    eng["senior"] = {
        "title": "Senior High School English Curriculum Standards (2017 Edition, revised in 2025)",
        "issuer": "Ministry of Education of the People's Republic of China",
        "year": 2025,
        "url": "http://www.moe.gov.cn/srcsite/A26/s8001/202006/t20200603_462199.html",
        "note": "The issuance notice is available on the Ministry of Education website. The item text has not been checked page by page against the document and is marked as needing verification. Compulsory volumes correspond to the standard's compulsory content; selective-compulsory volumes correspond to its selective-compulsory content.",
    }

    old_topic_n = len(topics)
    old_dep_n = len(deps)
    old_q_n = len(questions)
    old_std_n = len(standards["items"])
    old_ids = [(t["id"], t["name"]) for t in topics]
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
        print("Existing topics changed after writing.", file=sys.stderr)
        return 1
    if again_d[:old_dep_n] != deps or again_q[:old_q_n] != questions:
        print("Existing edges or questions changed after writing.", file=sys.stderr)
        return 1
    if again_s["items"][:old_std_n] != standards["items"][:old_std_n]:
        print("Existing curriculum-standard items changed.", file=sys.stderr)
        return 1
    print("Existing topics preserved with IDs and names unchanged: %d" % len(old_ids))
    return 0


if __name__ == "__main__":
    sys.exit(main())
