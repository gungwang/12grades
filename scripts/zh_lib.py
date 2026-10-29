# -*- coding: utf-8 -*-
"""Register elementary Chinese-language data and generate questions. Called by scripts/zh_build.py."""

import re

TOPICS = []
HARD = []

# Unit titles are organized by volume. Grade 1 fall follows the unified textbook revised in fall 2024; Grade 1 spring uses the spring 2025 edition.
# Grades 2 and 3 fall follow the fall 2025 revised table of contents; their spring volumes follow the spring 2026 revision.
# Grade 4 fall follows the 2024 revision / fall 2026 unified table of contents; spring follows the current unified / commonly used spring 2026 contents.
# Grade 5 fall follows the fall 2026 unified table of contents; spring follows the current unified / commonly used spring 2026 contents.
# Grade 6 fall follows the fall 2026 unified table of contents; spring follows the current contents and aligns with Grade 6 fall 2026. A unit may cover multiple topics.
# The semester keys "上" and "下" are retained as builder-facing tokens.
UNITS = {}
for _g in range(1, 7):
    for _s in ("上", "下"):
        for _u in range(1, 9):
            UNITS[(_g, _s, _u)] = "Unit %d" % _u

UNITS.update({
    (1, "上", 1): "Literacy · Heaven, Earth, and People",
    (1, "上", 2): "Pinyin · Simple Finals",
    (1, "上", 3): "Pinyin · Initials",
    (1, "上", 4): "Pinyin · Compound Finals",
    (1, "上", 5): "Text · Autumn",
    (1, "上", 6): "Literacy · Rhyming Pairs",
    (1, "上", 7): "Text · The Little Boat",
    (1, "上", 8): "Text · Comparing Tails",
    (1, "下", 1): "Literacy · The Four Seasons",
    (1, "下", 2): "Text · Remember the Well Digger When You Drink",
    (1, "下", 3): "Text · The Little Rooster and the Little Duck",
    (1, "下", 4): "Text · Thoughts on a Quiet Night",
    (1, "下", 5): "Literacy · At the Beginning of Life",
    (1, "下", 6): "Classical Poem · By the Pond",
    (1, "下", 7): "Text · The Home for School Supplies",
    (1, "下", 8): "Text · The Little Gecko Borrows a Tail",
    (2, "上", 1): "Text · Tadpoles Look for Their Mother",
    (2, "上", 2): "Literacy · A Song of Scenes",
    (2, "上", 3): "Text · Rainbow",
    (2, "上", 4): "Classical Poem · Climbing Stork Tower",
    (2, "上", 5): "Text · A Frog in a Well",
    (2, "上", 6): "Text · At the Octagonal Tower",
    (2, "上", 7): "Classical Poem · River Snow",
    (2, "上", 8): "Text · Praise",
    (2, "下", 1): "Classical Poem · Ode to the Willow",
    (2, "下", 2): "Text · Uncle Lei Feng, Where Are You?",
    (2, "下", 3): "Literacy · Song of China",
    (2, "下", 4): "Text · Colorful Dreams",
    (2, "下", 5): "Fable · Mending the Pen after Losing the Sheep",
    (2, "下", 6): "Classical Poem · Quatrain",
    (2, "下", 7): "Text · The Elephant's Ears",
    (2, "下", 8): "Legend · Yi Shoots Down Nine Suns",
    (3, "上", 1): "Text · The School Beneath the Great Green Tree",
    (3, "上", 2): "Classical Poem · A Mountain Walk",
    (3, "上", 3): "Prediction · The Old House That Never Falls",
    (3, "上", 4): "Fairy Tale · A Journey Inside an Ox's Stomach",
    (3, "上", 5): "Composition · Our Colorful World",
    (3, "上", 6): "Text · The Rich Xisha Islands",
    (3, "上", 7): "Classical Poem · Looking at Tianmen Mountain",
    (3, "上", 8): "Classical Chinese · Sima Guang",
    (3, "下", 1): "Classical Poem · Quatrain",
    (3, "下", 2): "Fable · Waiting by a Stump for a Hare",
    (3, "下", 3): "Text · The Undersea World",
    (3, "下", 4): "Classical Poem · New Year's Day",
    (3, "下", 5): "Composition · Wonderful Imagination",
    (3, "下", 6): "Text · Soap Bubbles",
    (3, "下", 7): "Text · Sunset Clouds",
    (3, "下", 8): "Fairy Tale · The Leaky Roof",
    (4, "上", 1): "Text · Watching the Tide",
    (4, "上", 2): "Text · The Five Peas in a Pod",
    (4, "上", 3): "Classical Poem · Written on the Wall at Xilin Temple",
    (4, "上", 4): "Myth · Pangu Creates the World",
    (4, "上", 5): "Composition · A Kaleidoscope of Life",
    (4, "上", 6): "Text · The Great Wall",
    (4, "上", 7): "Text · The Cow and the Goose",
    (4, "上", 8): "Text · Study for the Rise of China",
    (4, "下", 1): "Classical Poem · Four Seasons in the Countryside",
    (4, "下", 2): "Text · Amber",
    (4, "下", 3): "Text · Green",
    (4, "下", 4): "Text · The Cat",
    (4, "下", 5): "Composition · A Visit to _____",
    (4, "下", 6): "Classical Chinese · Reading by Firefly Light",
    (4, "下", 7): "Classical Poem · Farewell to Xin Jian at Furong Tower",
    (4, "下", 8): "Fairy Tale · The Giant's Garden",
    (5, "上", 1): "Text · Osmanthus Rain",
    (5, "上", 2): "Text · Tunnel Warfare in Central Hebei",
    (5, "上", 3): "Folktale · The Hunter Hailibu",
    (5, "上", 4): "Classical Poem · To My Son",
    (5, "上", 5): "Text · The Sun",
    (5, "上", 6): "Text · A Mother's Deep Love",
    (5, "上", 7): "Classical Poem · Mountain Dwelling in Autumn Dusk",
    (5, "上", 8): "Text · Ancient Sayings on Reading",
    (5, "下", 1): "Classical Poem · Four Seasons in the Countryside",
    (5, "下", 2): "Classic Novel · Borrowing Arrows with Straw Boats",
    (5, "下", 3): "Integrated Learning · Exploring the Kingdom of Chinese Characters",
    (5, "下", 4): "Classical Poem · Song of the Army",
    (5, "下", 5): "Text · A Set of Character Sketches",
    (5, "下", 6): "Classical Chinese · The Spear and the Shield",
    (5, "下", 7): "Text · The Gondolas of Venice",
    (5, "下", 8): "Classical Chinese · The Yang Family's Son",
    (6, "上", 1): "Text · The Prairie",
    (6, "上", 2): "Classical Poem · The Long March (Seven-Character Regulated Verse)",
    (6, "上", 3): "Text · Bamboo Stick Figures",
    (6, "上", 4): "Novel · The Bridge",
    (6, "上", 5): "Text · Lights",
    (6, "上", 6): "Text · Only One Earth",
    (6, "上", 7): "Classical Chinese · Two Children Debate the Sun",
    (6, "上", 8): "Text · Young Runtu",
    (6, "下", 1): "Text · Spring Festival in Beijing",
    (6, "下", 2): "Classic Novel · Robinson Crusoe",
    (6, "下", 3): "Prose · In a Hurry",
    (6, "下", 4): "Text · Reminiscences of Sixteen Years Ago",
    (6, "下", 5): "Classical Chinese · Learning to Play Go",
    (6, "下", 6): "Integrated Learning · Unforgettable Primary School Days",
    (6, "下", 7): "Classical Poetry Reading · Gathering Ferns",
    (6, "下", 8): "Classical Poetry Reading · Mooring at Guazhou",
})

# Standards entries paraphrase public descriptions; they are not quotations checked page by page. Symbolic names are local to this file.
# Stage 1 covers Grades 1–2, Stage 2 Grades 3–4, and Stage 3 Grades 5–6.
# Chinese domain labels in these rows and CRIT remain API keys used by existing topic modules and validators.
STANDARD_ROWS = [
    ("py_read", "1", "PY", "拼音", "Stage 1 · Pinyin",
     "Pronounce initials, finals, tones, and whole-syllable readings accurately; use Pinyin to recognize characters and blend syllables."),
    ("sz_12", "1", "SZ", "识字写字", "Stage 1 · Character Literacy and Writing",
     "Enjoy learning Chinese characters and be motivated to recognize and write them. Distinguish common characters by strokes and components, recognize common characters, and write some of them."),
    ("cy_12", "1", "CY", "词语", "Stage 1 · Vocabulary",
     "Understand common words in context and begin building vocabulary that includes measure words, reduplicated forms, and antonyms."),
    ("jz_12", "1", "JZ", "句子", "Stage 1 · Sentences",
     "Express complete thoughts, recognize commas, periods, question marks, and exclamation marks, and willingly use complete sentences."),
    ("yd_12", "1", "YD", "阅读理解", "Stage 1 · Reading and Appreciation",
     "Understand accessible fairy tales, fables, and stories; use illustrations and life experience to describe the main ideas."),
    ("gs_12", "1", "GS", "古诗文积累", "Stage 1 · Classical Poetry and Prose",
     "Recite nursery rhymes and accessible classical poems, imagine vividly, memorize selected texts for the stage, and avoid mixing up lines."),
    ("xz_12", "1", "XZ", "习作基础", "Stage 1 · Writing Basics",
     "Show interest in writing, observe carefully, record ideas in order, and willingly read finished work aloud to others."),
    ("sz_34", "2", "SZ", "识字写字", "Stage 2 · Character Literacy and Writing",
     "Use alphabetic and radical-based dictionary lookup, develop basic independent character recognition, and pay attention to similar-looking, homophonic, and polyphonic characters."),
    ("cy_34", "2", "CY", "词语", "Stage 2 · Vocabulary",
     "Use context to understand words, build vocabulary that includes idioms and words from texts, and begin noticing connotation."),
    ("jz_34", "2", "JZ", "句子", "Stage 2 · Sentences",
     "Write specific sentences, distinguish similes from personification, and correctly use common conjunctions and quotation marks."),
    ("yd_34", "2", "YD", "阅读理解", "Stage 2 · Reading and Appreciation",
     "Identify an article's main ideas, retell the gist of a narrative, and use notes to understand accessible classical Chinese."),
    ("gs_34", "2", "GS", "古诗文积累", "Stage 2 · Classical Poetry and Prose",
     "Recite excellent literature with attention to tone and rhythm, memorize selected poems, and understand easily confused characters in lines."),
    ("xz_34", "2", "XZ", "习作基础", "Stage 2 · Composition",
     "Observe the world, freely record experiences and feelings, make a paragraph's meaning clear, and begin writing diaries."),
    ("sz_56", "3", "SZ", "识字写字", "Stage 3 · Character Literacy and Writing",
     "Develop strong independent character recognition, infer character meanings from components and context, and pronounce tricky characters accurately."),
    ("cy_56", "3", "CY", "词语", "Stage 3 · Vocabulary",
     "Use context and prior knowledge to infer word meanings and appreciate nuanced words and phrases."),
    ("jz_56", "3", "JZ", "句子", "Stage 3 · Sentences",
     "Correct obvious language errors, write fluent sentences, and use common punctuation such as ellipses and em dashes as needed."),
    ("yd_56", "3", "YD", "阅读理解", "Stage 3 · Reading and Appreciation",
     "Read narratives and expository texts, identify their main ideas, and appreciate the author's feelings."),
    ("yd_wenyan", "3", "YD", "阅读理解", "Stage 3 · Classical Chinese",
     "Use notes to understand accessible classical Chinese, explain the main idea, and avoid misremembering what characters did."),
    ("gs_56", "3", "GS", "古诗文积累", "Stage 3 · Classical Poetry and Prose",
     "Recite excellent literature expressively, memorize selected poems, and distinguish easily confused lines."),
    ("xz_56", "3", "XZ", "习作基础", "Stage 3 · Composition",
     "Write simple personal narratives with concrete details and genuine feeling, choose details around a central idea, and organize clearly."),
]

NOTE = "Common instructional content for the corresponding volume of the unified textbook. Entries are public paraphrases, not quotations checked page by page."
CRIT = {
    "拼音": ["Distinguish initials, finals, and tones", "Blend common syllables"],
    "识字写字": ["Distinguish similar-looking and homophonic characters", "Recognize new characters by components and structure"],
    "词语": ["Understand a word's meaning in a sentence", "Choose words that collocate appropriately"],
    "句子": ["Write fluent sentences", "Select or revise sentences as required"],
    "阅读理解": ["Select information that matches a passage", "State the main idea of a story or passage"],
    "古诗文积累": ["Recall poems required for the volume", "Distinguish authors and lines without mixing them up"],
    "习作基础": ["Write a complete response to a prompt", "Identify which sentence best fits a prompt"],
}


def chapter(grade, sem, unit):
    cn = str(grade)
    title = UNITS[(grade, sem, unit)]
    return "Grade %s, %s semester, Unit %d: %s" % (cn, "first" if sem == "上" else "second", unit, title)


def _add(spec):
    if any(t["key"] == spec["key"] for t in TOPICS):
        raise SystemExit("Duplicate topic key: %s" % spec["key"])
    TOPICS.append(spec)


def C(prompt, answer, wrongs, expl):
    wrongs = [str(w).strip() for w in wrongs]
    answer = str(answer).strip()
    prompt = str(prompt).strip()
    expl = str(expl).strip()
    if len(wrongs) != 3:
        raise SystemExit("A choice item must have exactly 3 distractors: %s" % prompt[:40])
    return ("choice", prompt, answer, wrongs, expl)


def hard(topic, prereq, reason):
    HARD.append((topic, prereq, reason))


def K(key, name, domain, grade, sem, unit, typ, desc, std, qs):
    """Register a topic. qs contains 4 multiple-choice questions: (prompt, correct answer, [three distractors], explanation)."""
    if domain not in CRIT:
        raise SystemExit("%s has an unrecognized domain: %s" % (key, domain))
    if len(qs) != 4:
        raise SystemExit("%s requires exactly 4 questions" % key)
    items = [C(q[0], q[1], q[2], q[3]) for q in qs]
    _add({
        "key": key, "name": name, "domain": domain, "grade": grade, "semester": sem,
        "unit": unit, "type": typ, "description": desc,
        "mastery_criteria": list(CRIT[domain]), "std": std, "conf": "inferred", "note": NOTE,
        "items": items,
    })


def materialise_questions(spec):
    diffs = ["basic", "basic", "standard", "standard"]
    made = []
    for diff, item in zip(diffs, spec["items"]):
        _kind, prompt, answer, wrongs, expl = item
        made.append({"d": diff, "t": "choice", "p": prompt, "a": answer, "w": list(wrongs), "e": expl})
    if len(made) != 4:
        raise SystemExit("%s produced %d questions" % (spec["key"], len(made)))
    return made


# Keep these Chinese validation patterns aligned with the existing Chinese topic text.
_BANNED_START = re.compile(r"^(同一|上题|该题|同上)")
_BANNED_META = re.compile(r"本知识点|课标|是否要求")
_BANNED_COPY = re.compile(r"免费|AI\s*初稿|AI初稿")


def norm_opt(text):
    s = str(text).strip().lower()
    s = re.sub(r"\s+", "", s)
    s = re.sub(r"[.!\s]+$", "", s)
    return s


def check_question(key, q):
    prompt = q["p"]
    if _BANNED_START.match(prompt.strip()):
        raise SystemExit("%s prompt starts with a banned phrase: %s" % (key, prompt[:20]))
    blob = prompt + "\n" + q["e"] + "\n" + q["a"]
    if q["t"] == "choice":
        blob += "\n" + "\n".join(q["w"])
    if _BANNED_META.search(blob):
        raise SystemExit("%s contains a banned meta-question phrase" % key)
    if _BANNED_COPY.search(blob):
        raise SystemExit("%s contains disallowed wording" % key)
    if q["t"] != "choice":
        raise SystemExit("%s: elementary Chinese-language questions must all be multiple choice" % key)
    opts = [q["a"]] + list(q["w"])
    if len(opts) != 4 or len(set(opts)) != 4:
        raise SystemExit("%s has duplicate options or not exactly 4: %s" % (key, opts))
    if len(set(norm_opt(o) for o in opts)) != 4:
        raise SystemExit("%s has duplicate options after normalization: %s" % (key, opts))
    for o in opts:
        if not str(o).strip():
            raise SystemExit("%s has an empty option" % key)
        if re.fullmatch(r"[A-Za-z]", o.strip()):
            raise SystemExit("%s option cannot be a single letter: %s" % (key, o))
    if not str(q["e"]).strip():
        raise SystemExit("%s is missing an explanation" % key)
