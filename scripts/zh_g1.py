# -*- coding: utf-8 -*-
"""Grade 1, both volumes. Volume 1 follows the revised 2024 unified curriculum, lesson by lesson; Volume 2 follows the spring 2025 sequence and excludes the older “Four Suns” text."""
from zh_lib import K

# Keep the semester markers unchanged: diagnose/engine.js uses them when matching grade scopes.
# Han text remains only for the character, word, line, or response being assessed; surrounding prose is English.
# Chinese punctuation remains only where the punctuation symbol itself is being tested.

# ---------- Grade 1, Volume 1 ----------
# Revised 2024 unified-curriculum outline. Literacy lessons and texts are listed individually; pinyin is grouped by lesson, and oral communication is grouped under language activities.

K(
    "g1a_tian", "Literacy: Heaven, Earth, People", "Literacy and Writing", 1, "上", 1, "conceptual",
    "Recognize 天, 地, 人, 你, 我, and 他; distinguish 人 from 入 and 天 from 夫.",
    "sz_12",
    [
        ("Which character below is 人?", "人", ["入", "八", "大"], "The character 人 has a left-falling stroke and a right-falling stroke that separate. 入 has closer strokes; 八 and 大 are different characters."),
        ("What is the correct stroke order for 人?", "Left-falling stroke, then right-falling stroke", ["Right-falling stroke, then left-falling stroke", "Horizontal stroke, then vertical stroke", "Vertical stroke, then horizontal stroke"], "Write 人 with a left-falling stroke first, then a right-falling stroke. It has no horizontal or vertical strokes."),
        ("Among 你, 我, and 他, which character refers to oneself?", "我", ["你", "他", "它"], "我 refers to oneself. 你 refers to the person addressed, 他 refers to another person, and 它 commonly refers to things."),
        ("Which character below is 天?", "天", ["夫", "太", "大"], "天 has a short upper horizontal stroke and a longer lower one, followed by two falling strokes. 夫 has the reverse horizontal-stroke lengths, 太 has an extra dot, and 大 has no short upper stroke."),
    ],
)

K(
    "g1a_jin", "Literacy: Gold, Wood, Water, Fire, Earth", "Literacy and Writing", 1, "上", 1, "conceptual",
    "Read the rhyme 金木水火土; distinguish 土 from 士 and 木 from 禾; recognize the sequence 一二三四五 and the words for above and below.",
    "sz_12",
    [
        ("Which character below is 土?", "土", ["士", "干", "工"], "土 has a short upper horizontal stroke and a longer lower one. 士 has the reverse; 干 and 工 have different strokes."),
        ("In 金木水火土, which character represents a tree?", "木", ["禾", "本", "火"], "木 means a tree. 禾 is a grain seedling, 本 has an extra stroke at the bottom, and 火 means fire."),
        ("Which line follows 一二三四五?", "金木水火土", ["天地分上下", "日月照今古", "站如松，坐如钟"], "In the rhyme, 一二三四五 is followed by 金木水火土."),
        ("Which line follows 天地分上下?", "日月照今古", ["金木水火土", "一二三四五", "你我他"], "In the rhyme, 天地分上下 is followed by 日月照今古. 金木水火土 appears earlier."),
    ],
)

K(
    "g1a_kou", "Literacy: Mouth, Ear, Eye, Hand, Foot", "Literacy and Writing", 1, "上", 1, "conceptual",
    "Recognize 口, 耳, 目, 手, and 足, and understand the sayings 站如松, 坐如钟, 行如风, and 卧如弓.",
    "sz_12",
    [
        ("Which character means eye?", "目", ["日", "口", "耳"], "目 represents an eye and has two horizontal strokes inside. 日 represents the sun, 口 means mouth, and 耳 means ear."),
        ("In 手 and 足, what does 足 mean?", "Foot", ["Mouth", "Ear", "Hair"], "足 means foot. 口 means mouth and 耳 means ear."),
        ("What does 站如松 say about standing?", "Stand straight and tall, like a pine tree", ["Sit upright like a clock", "Run like the wind", "Lie down like a bow"], "站如松 means to stand straight and tall like a pine tree. 坐如钟 describes sitting upright."),
        ("In 行如风，卧如弓, how should one walk?", "Lightly and briskly, like the wind", ["Stand still like a pine tree", "Sit like a clock", "Sleep curled up like a bow"], "行如风 means to walk lightly and briskly. 卧如弓 describes a sleeping posture."),
    ],
)

K(
    "g1a_shan", "Literacy: Sun, Moon, Mountains, Rivers", "Literacy and Writing", 1, "上", 1, "conceptual",
    "Use pictures to recognize 日, 月, 山, 川, 水, 火, 田, and 禾; distinguish 日 from 目, 山 from 川, and 木 from 禾.",
    "sz_12",
    [
        ("Which character represents the sun?", "日", ["目", "月", "田"], "日 represents the sun, 目 represents an eye, 月 represents the moon, and 田 represents a field."),
        ("What does 月 represent?", "The moon", ["The sun", "An eye", "A flame"], "月 represents the moon. The sun, eye, and fire each have a different character."),
        ("What does 川 refer to?", "A river", ["A mountain peak", "A grain seedling", "A field"], "川 represents a river; its three vertical strokes resemble flowing water. The other choices are different characters."),
        ("Which character represents a grain seedling?", "禾", ["木", "日", "田"], "禾 represents a grain seedling and has an extra left-falling stroke above 木. 日 represents the sun and 田 a field."),
    ],
)

K(
    "g1a_xue", "School Readiness: Starting School", "Literacy and Writing", 1, "上", 1, "conceptual",
    "Say “I am Chinese,” recognize the Five-Star Red Flag and Tiananmen in Beijing, sing the school song, and enjoy reading, writing, and listening to stories.",
    "sz_12",
    [
        ("Which sentence has the same meaning as “我是中国人”?", "We are all Chinese people", ["We are not Chinese", "We are Tiananmen", "We are a schoolbag"], "“我是中国人” can also be expressed as “We are all Chinese people.” The other choices do not match its meaning."),
        ("The line “我爱我们的祖国” mentions which pair?", "The Five-Star Red Flag and Tiananmen in Beijing", ["Only a schoolbag", "Only a snowman", "Only a lotus flower"], "The verse says that the speaker loves the Five-Star Red Flag and Tiananmen in Beijing, and also mentions the Yangtze and Yellow Rivers."),
        ("In the school song, why does the speaker carry a schoolbag?", "To go to school and arrive on time every day", ["To draw in the snow", "To pick lotus flowers in a pond", "To watch geese by a river"], "The song answers that the speaker goes to school and is never late."),
        ("Which group of activities is named in “I love learning Chinese”?", "Reading, writing, telling stories, and listening to stories", ["Only playing soccer and never reading", "Only sleeping", "Only looking at snow and never writing"], "The lesson illustrates reading, writing, telling stories, and listening to stories."),
    ],
)

K(
    "g1a_zuo", "Language Activities 1: I Say, You Do", "Writing Foundations", 1, "上", 1, "procedural",
    "Give instructions clearly and loudly; listen carefully and follow them.",
    "xz_12",
    [
        ("In “I Say, You Do,” how should the person giving instructions speak?", "Loudly and clearly",
          ["Very softly and unclearly", "Turn away and say nothing", "Only gesture without saying a word"],
          "Others need to hear and understand the instruction to follow it. If the speaker is too quiet or says nothing, the game cannot work."),
        ("What should you do when someone gives an instruction?", "Listen carefully and follow it",
          ["Cover your ears", "Interrupt with something unrelated", "Run away halfway through"],
          "Listen to the whole instruction before acting. If you do not listen or run away, you will not know what to do."),
        ("Which instruction makes it clear what to do?", "Please close your book and sit up straight.",
          ["Book.", "That thing.", "Whatever."],
          "Say clearly what action to take. A single word does not tell the listener whether to close the book or do something else."),
        ("The teacher says, “Please raise your hand.” What should you do?", "Raise your hand",
          ["Throw your book on the floor", "Lie down on the desk", "Run out of the classroom"],
          "Do what the instruction says: raise your hand, not throw a book or run away."),
    ],
)

K(
    "g1a_le", "Happy Reading: Reading Is Fun", "Reading Comprehension", 1, "上", 1, "conceptual",
    "Enjoy reading picture books and telling stories with adults; know that learning pinyin helps you recognize more characters.",
    "yd_12",
    [
        ("What does “Reading Is Fun” mean?", "Reading is an enjoyable activity",
          ["Books are only for propping up a table", "You should feel sad after reading", "Books should not be opened"],
          "This section encourages children to enjoy reading and open books."),
        ("Which activity is suitable?", "Read an interesting story with a parent",
          ["Tear out the pages", "Look only at the cover without opening the book", "Do not let anyone tell a story"],
          "You can read with an adult, listen to stories, or tell stories. Tearing a book or leaving it closed is not reading."),
        ("What can you do after learning pinyin?", "Recognize more characters and read more books",
          ["Never read again", "Read only blank pages", "Close every book"],
          "Pinyin helps you recognize characters. Knowing more characters lets you read more books."),
        ("Which material is most suitable for this reading section?", "A book with pictures and a story",
          ["A blank sheet of paper", "A bill with only numbers", "A ruler"],
          "This section is for stories and picture books, not blank paper, bills, or rulers."),
    ],
)

K(
    "g1a_dan", "Simple Finals a, o, e and the Four Tones", "Pinyin", 1, "上", 2, "procedural",
    "Pronounce the simple finals a, o, and e, and distinguish the four tones.",
    "py_read",
    [
        ("How is 妈 pronounced in the first tone?", "mā", ["má", "mǎ", "mà"], "妈 is pronounced mā in the first tone. The other options use the second, third, and fourth tones."),
        ("Which pronunciation matches 马?", "mǎ", ["mā", "má", "mà"], "马 is pronounced mǎ in the third tone."),
        ("Which simple final begins 鹅?", "e", ["a", "o", "i"], "The simple final in 鹅 is e."),
        ("Which simple final is used in 大?", "a", ["o", "e", "i"], "The final in 大 is a."),
    ],
)

K(
    "g1a_iu", "Simple Finals i, u, ü", "Pinyin", 1, "上", 2, "procedural",
    "Pronounce the simple finals i, u, and ü, and distinguish u from ü.",
    "py_read",
    [
        ("Which option is the simple final ü?", "ü", ["u", "i", "e"], "The simple final ü has a diaeresis."),
        ("Which final is used in 乌?", "u", ["ü", "i", "a"], "乌 is pronounced with u, which has no diaeresis; ü has one."),
        ("Which final is used in 衣?", "i", ["u", "ü", "o"], "衣 is pronounced with the simple final i."),
        ("Which group contains only simple finals?", "i, u, ü", ["b, p, m", "zh, ch, sh", "ai, ei, ui"], "i, u, and ü are simple finals. The other groups are consonant initials or compound finals."),
    ],
)

K(
    "g1a_bpm", "Initial Consonants b, p, m, f", "Pinyin", 1, "上", 2, "procedural",
    "Read the initials b, p, m, and f; distinguish unaspirated b from aspirated p.",
    "py_read",
    [
        ("Which initial consonant begins 八?", "b", ["p", "m", "f"], "八 is pronounced bā, with the unaspirated initial b. 爬 begins with the aspirated p."),
        ("Which initial consonant begins 爬?", "p", ["b", "f", "m"], "爬 is pronounced pá, with the aspirated initial p. 八 begins with b."),
        ("Which initial consonant begins 妈?", "m", ["b", "f", "p"], "妈 is pronounced mā and begins with m."),
        ("Which initial consonant begins 发?", "f", ["b", "p", "m"], "发 is pronounced fā and begins with f, not b or p."),
    ],
)

K(
    "g1a_dtn", "Initial Consonants d, t, n, l", "Pinyin", 1, "上", 2, "procedural",
    "Read the initials d, t, n, and l; distinguish unaspirated d from aspirated t, and n from l.",
    "py_read",
    [
        ("Which initial consonant begins 大?", "d", ["t", "n", "l"], "大 is pronounced dà and begins with the unaspirated d. 兔 begins with the aspirated t."),
        ("Which initial consonant begins 兔?", "t", ["d", "n", "l"], "兔 is pronounced tù and begins with the aspirated t. 大 begins with d."),
        ("Which initial consonant begins 你?", "n", ["l", "d", "t"], "你 is pronounced nǐ and begins with n. 拉 begins with l."),
        ("Which initial consonant begins 拉?", "l", ["n", "d", "t"], "拉 is pronounced lā and begins with l. 你 begins with n."),
    ],
)

K(
    "g1a_hua", "Language Activities 2: The Poem “A Painting”", "Poetry", 1, "上", 2, "conceptual",
    "Memorize the poem: 远看山有色，近听水无声，春去花还在，人来鸟不惊.",
    "gs_12",
    [
        ("Which line follows 远看山有色?", "近听水无声", ["春去花还在", "人来鸟不惊", "春去花不在"], "The poem first describes the distant mountain's colors, then says that nearby water makes no sound."),
        ("Which line follows 春去花还在?", "人来鸟不惊", ["近听水无声", "远看山有色", "人来鸟飞走"], "The flowers remain when spring has passed, and the birds are not startled when people arrive. The last option contradicts the poem."),
        ("Why does the water make no sound and the birds remain unafraid when people arrive?", "Because the poem describes a painting, not a real landscape",
          ["Because there is no water in the mountains", "Because all the birds have flown away", "Because all the flowers have wilted"],
          "Water in a painting makes no sound, and painted birds cannot be frightened away."),
        ("What is the poem about?", "A painting", ["A heavy rainstorm", "A flock of geese", "A flag"], "The colorful mountain, silent water, flowers that remain, and unfrightened birds are all part of a painting."),
    ],
)

K(
    "g1a_gkh", "Initial Consonants g, k, h", "Pinyin", 1, "上", 3, "procedural",
    "Read the initials g, k, and h; distinguish unaspirated g from aspirated k.",
    "py_read",
    [
        ("Which initial consonant begins 哥?", "g", ["k", "h", "d"], "哥 is pronounced gē and begins with the unaspirated g. 科 begins with the aspirated k."),
        ("Which initial consonant begins 科?", "k", ["g", "h", "b"], "科 is pronounced kē and begins with the aspirated k. 哥 begins with g."),
        ("Which initial consonant begins 河?", "h", ["g", "k", "f"], "河 is pronounced hé and begins with h, not g or k."),
        ("Which initial consonant begins 瓜?", "g", ["k", "h", "p"], "瓜 is pronounced guā and begins with g. 夸 begins with k."),
    ],
)

K(
    "g1a_jqx", "Initial Consonants j, q, x", "Pinyin", 1, "上", 3, "procedural",
    "Read the initials j, q, and x, and distinguish them from flat-tongue and retroflex sounds.",
    "py_read",
    [
        ("Which initial consonant begins 鸡?", "j", ["q", "x", "g"], "鸡 is pronounced jī and begins with j. 七 begins with q."),
        ("Which initial consonant begins 七?", "q", ["j", "x", "c"], "七 is pronounced qī and begins with q. 鸡 begins with j, and 西 begins with x."),
        ("Which initial consonant begins 西?", "x", ["Flat-tongue s", "Retroflex sh", "j"], "西 is pronounced xī and begins with x, not flat-tongue s or retroflex sh."),
        ("Which initial consonant begins 下?", "x", ["q", "j", "Flat-tongue s"], "下 is pronounced xià and begins with x. 请 begins with q, 家 with j, and 撒 with s."),
    ],
)

K(
    "g1a_zcs", "Flat-Tongue Initials z, c, s", "Pinyin", 1, "上", 3, "procedural",
    "Read the flat-tongue initials z, c, and s with the tongue tip flat rather than curled.",
    "py_read",
    [
        ("Which initial consonant begins 字?", "z", ["zh", "c", "s"], "字 is pronounced zì and begins with flat-tongue z, not retroflex zh."),
        ("Which initial consonant begins 草?", "c", ["ch", "z", "s"], "草 is pronounced cǎo and begins with flat-tongue c, not retroflex ch."),
        ("Which initial consonant begins 四?", "s", ["sh", "z", "c"], "四 is pronounced sì and begins with flat-tongue s, not retroflex sh."),
        ("What should the tongue do when pronouncing z, c, and s?", "Stay flat", ["Curl upward", "Avoid using the tongue", "Press against the nose"], "For z, c, and s, keep the tongue tip flat. Curl it for zh, ch, and sh."),
    ],
)

K(
    "g1a_sheng", "Retroflex Initials zh, ch, sh, r", "Pinyin", 1, "上", 3, "procedural",
    "Read the retroflex initials zh, ch, sh, and r; distinguish them from flat-tongue sounds and recognize the whole syllable zhī.",
    "py_read",
    [
        ("Which initial begins 中 in 中国?", "zh", ["z", "ch", "sh"], "中 is pronounced zhōng and begins with retroflex zh. Flat-tongue z and retroflex ch and sh are different sounds."),
        ("Which initial consonant begins 书?", "sh", ["s", "zh", "ch"], "书 is pronounced shū and begins with retroflex sh, not flat-tongue s."),
        ("Which initial consonant begins 吃?", "ch", ["c", "zh", "sh"], "吃 begins with retroflex ch, not c, zh, or sh."),
        ("Which syllable is recognized as a whole and does not need to be blended?", "The whole syllable zhī", ["The initial zh", "The blended syllable mā", "The blended syllable bā"], "Read zhī as a whole. Blend the initial zh with a final; mā and bā also require blending."),
    ],
)

K(
    "g1a_yw", "Initials y and w", "Pinyin", 1, "上", 3, "procedural",
    "Read y and w; recognize yi, wu, and yu as whole syllables, and remember that u in yu is pronounced ü.",
    "py_read",
    [
        ("Which initial begins 鸭?", "y", ["w", "n", "l"], "鸭 is pronounced yā and begins with y; 蛙 begins with w."),
        ("Which initial begins 蛙?", "w", ["y", "f", "h"], "蛙 is pronounced wā and begins with w; 鸭 begins with y."),
        ("How is 衣 written as a whole syllable without blending?", "The whole syllable yī", ["Blend the simple final i again", "The blended syllable yá", "The initial w"], "Read 衣 as the whole syllable yī. The second-tone yá is a different syllable."),
        ("When 鱼 is written as yu, how is the u pronounced?", "Remove the two dots in writing; keep the ü sound", ["Change it to the u in 乌", "Change it to i", "Change it to e"], "In yu, yue, and yun, u is written without the diaeresis but pronounced ü."),
    ],
)

K(
    "g1a_zheng", "Language Activities 3: Whole-Syllable Recognition", "Pinyin", 1, "上", 3, "procedural",
    "Review which whole syllables are read as a unit and which syllables must be blended from an initial and a final.",
    "py_read",
    [
        ("Which syllable is read as a whole without blending?", "The whole syllable yī (衣)", ["The blended syllable bā (八)", "The blended syllable mā (妈)", "The blended syllable dà (大)"], "Read yī as a whole. Blend bā, mā, and dà from their initials and finals."),
        ("How should the syllable sì in 四 be read?", "As a whole syllable, without blending", ["Say s, then blend it with i", "Say retroflex shì", "Say only the initial s"], "Sì is a whole-syllable recognition syllable. 十 is pronounced with retroflex sh."),
        ("What kind of syllable is rì in 日?", "The whole-syllable recognition syllable rì", ["Blend initial r with i", "The whole-syllable recognition syllable yi", "The blended syllable bá"], "Read rì as a whole syllable; it is not blended."),
        ("Which syllable must be blended from an initial and a final?", "The blended syllable bā (八)", ["The whole syllable yī (衣)", "The whole syllable wū (乌)", "The whole syllable sī (丝)"], "Blend bā. Read yī, wū, and sī as whole syllables."),
    ],
)

K(
    "g1a_fu", "Compound Finals ai, ei, ui, ao, ou, iu", "Pinyin", 1, "上", 4, "procedural",
    "Distinguish the compound finals ai, ei, ui, ao, ou, and iu.",
    "py_read",
    [
        ("Which final is used in 白?", "ai", ["ei", "ao", "ou"], "白 is pronounced bái and has the final ai."),
        ("Which final is used in 高?", "ao", ["ou", "ai", "ei"], "高 is pronounced gāo and has the final ao."),
        ("Which final is used in 对?", "ui", ["iu", "ei", "ao"], "对 is pronounced duì and has the final ui."),
        ("Which final is used in 秋?", "iu", ["ui", "ou", "ai"], "秋 is pronounced qiū and has the final iu."),
    ],
)

K(
    "g1a_ie", "Special Finals ie, üe, er", "Pinyin", 1, "上", 4, "procedural",
    "Pronounce ie, üe, and er, and recognize that er forms a syllable on its own.",
    "py_read",
    [
        ("Which final is used in 叶?", "ie", ["ei", "er", "üe"], "叶 is pronounced yè and has the final ie."),
        ("Which final is used in 月?", "üe", ["ie", "er", "ei"], "月 is pronounced yuè and has the final üe."),
        ("Which final is used in 耳?", "er", ["ie", "ei", "en"], "耳 is pronounced ěr. Er forms a syllable on its own and is not blended with an initial."),
        ("Which final, ie or ei, is used in 叶?", "ie", ["ei", "er", "üe"], "叶 has the final ie: i comes before e."),
    ],
)

K(
    "g1a_bi", "Nasal Finals an, en, in, un, ün, ang, eng, ing, ong", "Pinyin", 1, "上", 4, "procedural",
    "Distinguish front-nasal and back-nasal finals, especially an from ang and in from ing.",
    "py_read",
    [
        ("Which final is used in 方?", "Back-nasal ang", ["Front-nasal an", "Back-nasal eng", "Front-nasal en"], "方 is pronounced fāng and has the back-nasal final ang."),
        ("Which final is used in 星?", "Back-nasal ing", ["Front-nasal in", "Back-nasal eng", "Back-nasal ang"], "星 is pronounced xīng and has the back-nasal final ing."),
        ("Which final is used in 安?", "Front-nasal an", ["Back-nasal ang", "Front-nasal en", "Back-nasal eng"], "安 is pronounced ān and has the front-nasal final an."),
        ("Which final is used in 云?", "Front-nasal ün", ["Back-nasal ing", "Back-nasal eng", "Front-nasal an"], "云 is pronounced yún and has the front-nasal final ün."),
    ],
)

K(
    "g1a_pin", "Blending Syllables", "Pinyin", 1, "上", 4, "procedural",
    "Blend initials and finals into syllables, distinguish tones, and pronounce j, q, and x with ü.",
    "py_read",
    [
        ("Which character is pronounced by blending initial b with final ā?", "八 (bā, first tone)", ["爸 (bà, fourth tone)", "拔 (bá, second tone)", "把 (bǎ, third tone)"], "Blending b with ā gives first-tone bā, as in 八. 爸 is fourth-tone bà."),
        ("Which pronunciation matches 鱼?", "yú (second tone)", ["yū (first tone)", "yǔ (third tone)", "yù (fourth tone)"], "鱼 is pronounced yú in the second tone; the other options use different tones."),
        ("When j, q, or x is combined with ü, what happens to the two dots over ü?", "They are dropped in writing, but the sound remains ü", ["Keep the dots and change the sound to u", "Change the sound to i", "Change the sound to e"], "In ju, qu, and xu, u is pronounced ü and is written without the dots."),
        ("Which syllable matches 门?", "mén (second tone, front-nasal final)", ["mēn (first tone)", "méng (back-nasal final)", "mèng (back-nasal final)"], "门 is pronounced mén in the second tone with the front-nasal final en."),
    ],
)

K(
    "g1a_gu", "Language Activities 4: Marking Tone in Syllables", "Pinyin", 1, "上", 4, "procedural",
    "Mark tones on syllables: use a when present; otherwise look for o or e; when i and u occur together, mark the latter.",
    "py_read",
    [
        ("Where is the tone mark placed in gāo (高)?", "On a", ["On o", "On g", "This syllable has no tone mark"], "The final ao contains a, so place the tone mark on a: gāo."),
        ("Where is the tone mark placed in fēi (飞)?", "On e", ["On i", "On f", "On a"], "The final ei has no a but contains e, so place the tone mark on e."),
        ("The final in shuǐ (水) is ui. Where is the tone mark placed?", "On the later letter, i", ["On the earlier letter, u", "On sh", "On a"], "When i and u occur together, place the tone mark on the later one. In ui, that is i."),
        ("Where is the tone mark placed in niǎo (鸟)?", "On a", ["On i", "On o", "On n"], "The final iao contains a, so place the tone mark on a."),
    ],
)

K(
    "g1a_qiu", "Reading “Autumn”", "Reading Comprehension", 1, "上", 5, "reasoning",
    "Use pinyin to read “Autumn” and understand that leaves turn yellow and geese fly south.",
    "yd_12",
    [
        ("In “Autumn,” what color do the leaves turn, and what happens next?", "They turn yellow and fall from the trees",
          ["They turn red and stay on the trees", "They turn green and keep growing", "They turn white and fly into the sky"],
          "The passage says the weather cools, the leaves turn yellow, and they fall from the trees."),
        ("Which direction do the geese fly?", "South", ["North", "East", "They stay in the trees for winter"], "The passage says a flock of geese flies south as the weather cools."),
        ("Which two shapes do the geese form as they fly?", "The characters 人 and 一", ["The characters 大 and 小", "The characters 口 and 日", "Circles and squares"], "The geese form 人 and then 一."),
        ("What is the sky like in the passage?", "Blue and high", ["Gray and low", "Covered with clouds", "Snowy"], "The passage describes the autumn sky as blue and high."),
    ],
)

K(
    "g1a_jiang", "Reading “South of the Yangtze”", "Reading Comprehension", 1, "上", 5, "reasoning",
    "Read the Han yuefu poem and remember the east, west, south, and north sequence in its lines about fish among lotus leaves.",
    "yd_12",
    [
        ("Which line follows 鱼戏莲叶间?", "鱼戏莲叶东", ["鱼戏莲叶西", "鱼戏莲叶南", "鱼戏莲叶北"], "The poem lists east, west, south, and north; the next line is 鱼戏莲叶东."),
        ("Which line follows 鱼戏莲叶东?", "鱼戏莲叶西", ["鱼戏莲叶南", "鱼戏莲叶北", "鱼戏莲叶间"], "The directions proceed east, west, south, and north. The line about fish among the leaves already appeared."),
        ("What does 莲叶何田田 describe?", "Lotus leaves growing lushly and densely", ["Very few fish", "No lotus leaves in the south", "Children picking water caltrops"], "田田 describes lotus leaves growing thickly together and looking lush."),
        ("What are people mainly doing in the poem?", "Picking lotus flowers and watching fish swim among the leaves", ["Swimming in a pond", "Picking every lotus leaf", "Flying kites on the bank"], "The poem describes picking lotus flowers and fish swimming among the leaves in different directions."),
    ],
)

K(
    "g1a_xuedi", "Reading “Little Artists in the Snow”", "Reading Comprehension", 1, "上", 5, "reasoning",
    "Match the tracks made by a chick, puppy, duckling, and foal, and understand that the frog is asleep in its cave.",
    "yd_12",
    [
        ("What does the chick draw?", "Bamboo leaves", ["Plum blossoms", "Maple leaves", "A crescent moon"], "The chick's footprints look like bamboo leaves. The puppy makes plum-blossom prints."),
        ("Which animal makes plum-blossom prints?", "The puppy", ["The chick", "The duckling", "The foal"], "The puppy's footprints look like plum blossoms. The chick makes bamboo-leaf prints, the duckling maple-leaf prints, and the foal crescent-moon prints."),
        ("What do the duckling and foal each draw?", "The duckling draws maple leaves; the foal draws a crescent moon",
          ["The duckling draws a crescent moon; the foal draws maple leaves", "The duckling draws plum blossoms; the foal draws bamboo leaves", "The duckling draws bamboo leaves; the foal draws plum blossoms"],
          "The duckling makes maple-leaf prints and the foal makes crescent-moon prints; do not switch them."),
        ("Why does the frog not join in?", "It is asleep in its cave", ["It cannot walk", "Frogs are not allowed in the snow", "It has used up all its paint"], "The passage says the frog is asleep in its cave."),
    ],
)

K(
    "g1a_siji", "Reading “The Four Seasons”", "Reading Comprehension", 1, "上", 5, "reasoning",
    "Match 草芽, 荷叶, 谷穗, and the snowman with spring, summer, autumn, and winter.",
    "yd_12",
    [
        ("草芽 is pointed and tells a bird what season it is. Which season does it name?", "Spring", ["Summer", "Autumn", "Winter"], "草芽 says it is spring. 荷叶 identifies itself as summer."),
        ("Who says “我是夏天” in the poem?", "荷叶", ["草芽", "谷穗", "The snowman"], "荷叶 is round and tells the frog, “我是夏天.”"),
        ("谷穗 is bent over. Which season does it name?", "Autumn", ["Spring", "Summer", "Winter"], "谷穗 bows and says it is autumn. The snowman identifies winter."),
        ("How does the snowman introduce itself?", "It puffs out its belly and says “我就是冬天”",
          ["It speaks in a high voice and says “I am spring”", "It tells the frog “I am summer”", "It bows and says “I am autumn”"],
          "The snowman puffs out its belly and playfully says “我就是冬天.” 谷穗 is the one that bows."),
    ],
)

K(
    "g1a_ju", "Language Activities 5: Complete Sentences", "Sentences", 1, "上", 5, "procedural",
    "Form complete sentences that state who is doing what and where.",
    "jz_12",
    [
        ("Which sentence expresses a complete idea?", "The duckling is swimming in the river.", ["A duckling.", "Swimming.", "In the river."], "A complete sentence says who is doing what and where. A single word is not enough."),
        ("Picture prompt: a rabbit is eating a carrot in a meadow. Which description is best?", "The rabbit is eating a carrot in the meadow.", ["The rabbit eats.", "The meadow.", "Carrot rabbit meadow."], "State who is doing what and where so the listener understands."),
        ("Which sentence below is complete?", "The bird is flying in the sky.", ["The bird flies", "In the sky", "Flying bird the"], "The sentence identifies who is acting, where, and what the action is."),
        ("What is good about saying “The moon looks like a boat”?", "It clearly describes what the moon looks like", ["It writes only the word “moon”", "It does not describe the moon", "It replaces “boat” with “car”"], "A complete sentence explains who or what is being described and what it is like."),
    ],
)

K(
    "g1a_dui", "Literacy: Paired-Word Rhyme", "Literacy and Writing", 1, "上", 6, "conceptual",
    "Read the paired-word rhyme and learn 云对雨, 雪对风, 花对树, 鸟对虫, 山清对水秀, and 柳绿对桃红.",
    "sz_12",
    [
        ("Which pair follows 云对雨?", "雪对风", ["花对树", "鸟对虫", "柳绿对桃红"], "The rhyme lists 云对雨 and 雪对风 before 花对树 and 鸟对虫."),
        ("Which pair follows 花对树?", "鸟对虫", ["雪对风", "山清对水秀", "云对雨"], "鸟对虫 follows 花对树; 山清对水秀 comes later."),
        ("Which pair follows 山清对水秀?", "柳绿对桃红", ["云对雨", "雪对风", "花对树"], "柳绿对桃红 follows 山清对水秀."),
        ("What is paired with 云?", "雨", ["风", "雪", "树"], "The rhyme pairs 云 with 雨, 雪 with 风, and 花 with 树."),
    ],
)

K(
    "g1a_ming", "Literacy: 日月明", "Literacy and Writing", 1, "上", 6, "conceptual",
    "Combine familiar characters to remember new ones: 日月明, 田力男, 二人从, and 三木森.",
    "sz_12",
    [
        ("Which character is formed by combining 日 and 月?", "明", ["朋", "胆", "期"], "Combining 日 and 月 makes 明, meaning bright. 朋 contains two 月 components."),
        ("Which character is formed by combining 田 and 力?", "男", ["电", "累", "苗"], "田 and 力 combine to form 男. 电 is related to 田 but is a different character; 苗 has the grass radical."),
        ("Which character can be remembered as two people standing together?", "从", ["众", "林", "森"], "二人 form 从. Three people form 众, and two 木 components form 林."),
        ("Which character is formed from three 木 components?", "森", ["林", "丛", "苗"], "Two 木 components form 林; three form 森. 丛 and 苗 are not made of three 木 components."),
    ],
)

K(
    "g1a_bao", "Literacy: My Schoolbag", "Literacy and Writing", 1, "上", 6, "conceptual",
    "Recognize the stationery words 橡皮, 尺子, 作业本, and 笔袋, and know to put stationery in a schoolbag.",
    "sz_12",
    [
        ("Which word names a stationery item in the schoolbag?", "橡皮", ["南瓜", "荷叶", "石子"], "橡皮 is stationery and belongs in a schoolbag. The other words name a pumpkin, a lotus leaf, and a pebble."),
        ("What is 尺子 used for?", "Measuring length", ["Erasing pencil marks", "Holding drinking water", "Raising a flag"], "A 尺子 measures length. Use 橡皮 to erase pencil marks."),
        ("What is 笔袋 used to hold?", "Pens", ["Lunch", "Shoes", "A flag"], "A 笔袋 is a stationery pouch for pens."),
        ("Where should 作业本 go after use?", "Back in the schoolbag", ["In the snow", "In a pond", "In the mouth of a bottle"], "A 作业本 is a school supply; return it to the schoolbag so it is not lost."),
    ],
)

K(
    "g1a_qi", "Reading “Raising the National Flag”", "Reading Comprehension", 1, "上", 6, "reasoning",
    "Read about raising the national flag and learn to stand at attention and salute.",
    "yd_12",
    [
        ("Which flag is described in the text?", "五星红旗", ["彩旗", "队旗", "校旗"], "五星红旗 is the national flag. The other options are a colorful flag, a team flag, and a school flag."),
        ("How is the flag raised?", "Slowly as the national anthem plays", ["It is blown away by the wind", "Children toss it into the air", "It is lowered below the flagpole"], "The text says the flag rises 徐徐 while the national anthem plays. 徐徐 means slowly."),
        ("What should children do facing the raised flag?", "Stand at attention and salute", ["Sit down and rest", "Turn and leave", "Talk and laugh loudly"], "The text says to stand at attention and salute the flag."),
        ("What does 迎风飘扬 describe?", "The flag waving in the wind", ["Clouds running across the sky", "Leaves falling to the ground", "Classmates running a race"], "The text describes the raised 五星红旗 waving in the wind."),
    ],
)

K(
    "g1a_duo", "Language Activities 6: Size, Quantity, and Classifiers", "Vocabulary", 1, "上", 6, "conceptual",
    "Distinguish large from small and many from few, and use classifiers such as 一头, 一只, 一群, and 一条.",
    "cy_12",
    [
        ("Can the classifier 头 in 一头黄牛 be replaced with another classifier?", "No; 一头黄牛 cannot be changed to 一只黄牛",
          ["一只黄牛 is also correct", "一条黄牛 is also correct", "一群黄牛 is also correct"],
          "黄牛 is commonly counted with 头. Use 只 for birds and 条 for fish."),
        ("Which word best fits after the classifier 一只?", "鸟", ["黄牛", "大雁", "鱼"], "Use 只 for 鸟, 头 for 黄牛, 群 for 大雁, and 条 for 鱼."),
        ("What contrast is shown by 一群大雁 and 一条鱼?", "Many versus one",
          ["Large versus fish", "Group versus goose", "Strip versus bird"],
          "一群 indicates many, while 一条 refers to one. Large and small form a different contrast."),
        ("What is the opposite of 大?", "小", ["少", "短", "低"], "大 is paired with 小, and 多 with 少. 少 is not the opposite of 大."),
    ],
)

K(
    "g1a_chuan", "Reading “The Little Boat”", "Reading Comprehension", 1, "上", 7, "reasoning",
    "Read Ye Shengtao's poem and understand how it compares the curved moon to a little boat.",
    "yd_12",
    [
        ("What is the curved moon compared to?", "A little boat", ["A little bridge", "A round plate", "A tall tree"], "The poem compares the curved moon to a little boat, not a bridge or tree."),
        ("What shape is described in 小小的船儿两头尖?", "Pointed at both ends", ["Square", "Round like a ball", "Pointed at only one end"], "The line says 小小的船儿两头尖: the curved moon is pointed at both ends."),
        ("What does the speaker see while sitting in the little boat?", "Twinkling stars and a blue sky", ["A red sun", "Green lotus leaves", "Yellow fallen leaves"], "The poem says the speaker sees twinkling stars and a blue sky, not the sun or lotus leaves."),
        ("Who wrote “The Little Boat”?", "Ye Shengtao", ["Luo Binwang", "Li Bai", "Du Fu"], "“The Little Boat” is by Ye Shengtao. Luo Binwang wrote “Ode to the Goose”; Li Bai wrote “Quiet Night Thoughts.”"),
    ],
)

K(
    "g1a_ying", "Reading “Shadow”", "Reading Comprehension", 1, "上", 7, "reasoning",
    "Read about a shadow that follows a person like a little black dog.",
    "yd_12",
    [
        ("What is the shadow compared to in the text?", "A little black dog", ["A little white rabbit", "A small boat", "A large tree"], "The text says the shadow often follows the speaker like a little black dog."),
        ("What does the shadow being in front, behind, left, and right show?", "It keeps following the speaker",
          ["It goes home by itself", "It appears only at noon", "It is a real dog"],
          "The shadow appears in different places because it follows and accompanies the person."),
        ("In “It is my good friend,” what does it refer to?", "The shadow", ["A dog", "The sun", "A classmate"], "The text describes the shadow as a friend; it is not about finding a real dog."),
        ("Which sentence agrees with the text?", "The shadow often follows and accompanies me",
          ["The shadow disappears at sunrise and never returns", "The shadow only walks on my left", "The shadow needs a leash to follow me"],
          "The text says the shadow often follows and accompanies the speaker like a friend."),
    ],
)

K(
    "g1a_jian", "Reading “Two Treasures”", "Reading Comprehension", 1, "上", 7, "reasoning",
    "Read about how hands work and the brain thinks, and how using both makes creativity possible.",
    "yd_12",
    [
        ("What are the two treasures people have?", "Two hands and a brain", ["A schoolbag and a pencil", "The sun and the moon", "A shadow and a dog"], "The text names the hands and the brain as the two treasures."),
        ("What can the hands and brain each do?", "Hands can work, and the brain can think",
          ["Hands can think, and the brain can work", "Hands can sleep, and the brain can run", "Hands can fly, and the brain can swim"],
          "Hands do work and the brain thinks; do not switch their roles."),
        ("What happens if you use your hands but not your brain?", "The task will not be done well",
          ["You will become creative", "The task will certainly be done better", "You can do anything"],
          "Using hands without thinking does not lead to good work. Creativity requires both."),
        ("What do you need to do to be creative?", "Use both your hands and your brain",
          ["Use your hands but not your brain", "Use your brain but not your hands", "Use neither"],
          "The text concludes that creativity comes from using both hands and brain."),
    ],
)

K(
    "g1a_yin", "Language Activities 7: Choosing Your Volume", "Writing Foundations", 1, "上", 7, "procedural",
    "Choose your volume for the situation: speak loudly enough to be heard, or quietly enough not to disturb others.",
    "xz_12",
    [
        ("How should you speak in a library?", "Quietly", ["Shout loudly", "Bang on a desk while speaking", "Shout into someone's ear"], "Keep your voice low in a library so you do not disturb people reading."),
        ("A classmate is far away on the playground, and you want them to come over. What should you do?", "Call loudly enough for them to hear",
          ["Mumble so they cannot hear", "Make no sound at all", "Wait until you reach them before making any sound"],
          "Someone far away may not hear a quiet voice, so call loudly enough."),
        ("How should you speak when answering a question in class?", "Clearly and loudly enough for the teacher and classmates to hear",
          ["So quietly that only you can hear", "Louder than a shout, drowning out the teacher", "Look down and do not answer"],
          "Speak clearly and loudly enough for everyone to hear, without shouting over others."),
        ("Your grandfather is asleep. How should you speak?", "Quietly so you do not wake him",
          ["Sing loudly", "Beat a drum to wake him", "Shout in his ear"],
          "Speak softly when someone is resting; singing, drumming, or shouting can wake them."),
    ],
)

K(
    "g1a_weiba", "Reading “Whose Tail Is It?”", "Reading Comprehension", 1, "上", 8, "reasoning",
    "Read about the tails of a monkey, rabbit, squirrel, duck, rooster, and peacock.",
    "yd_12",
    [
        ("Whose tail is long?", "The monkey's", ["The rabbit's", "The squirrel's", "The duck's"], "The monkey's tail is long. The rabbit's is short, and the squirrel's looks like an umbrella."),
        ("Whose tail looks like an umbrella?", "The squirrel's", ["The monkey's", "The peacock's", "The rooster's"], "The squirrel has a large, fluffy tail that looks like an umbrella. The peacock's tail is the prettiest."),
        ("How does the text describe the duck's and rooster's tails?", "The duck's tail is flat; the rooster's tail is curved",
          ["The duck's tail is curved; the rooster's is flat", "The duck's tail is long; the rooster's is short", "The duck's tail is the prettiest"],
          "The duck's tail is flat and the rooster's is curved. The peacock's tail is the prettiest."),
        ("Whose tail is the prettiest?", "The peacock's", ["The rooster's", "The squirrel's", "The monkey's"], "The text says the peacock's tail is the prettiest; the rooster's tail is simply curved."),
    ],
)

K(
    "g1a_wu", "Reading “The Crow Drinks Water”", "Reading Comprehension", 1, "上", 8, "reasoning",
    "Read how a crow drops pebbles into a bottle, raising the water so it can drink.",
    "yd_12",
    [
        ("Why could the crow not drink the water at first?", "There was little water, and the bottle opening was small",
          ["The bottle had no water at all", "The opening was too large and all the water spilled", "The water was too hot to drink"],
          "There was some water, but the level was low and the opening was too small for the crow's beak."),
        ("What solution did the crow find?", "Drop small pebbles into the bottle one by one",
          ["Kick the bottle over", "Ask someone to pour out the water", "Bury the bottle"],
          "The crow saw many small pebbles nearby and dropped them into the bottle one at a time."),
        ("What happened to the water after the pebbles were added?", "It rose gradually, and the crow could drink",
          ["It all leaked out", "It froze", "Nothing changed, and the crow still could not drink"],
          "The pebbles took up space, so the water rose until the crow could drink."),
        ("What is the main idea of the story?", "Look for a solution when you face a problem",
          ["Give up if you cannot drink", "Never put pebbles in a bottle", "Bottle water cannot be drunk"],
          "The crow did not give up; it found a way to raise the water."),
    ],
)

K(
    "g1a_yu", "Reading “Raindrops”", "Reading Comprehension", 1, "上", 8, "reasoning",
    "Read about the small raindrops going where flowers and grass grow, and the big raindrops going where they do not.",
    "yd_12",
    [
        ("Where do the small raindrops want to go?", "Somewhere with flowers and grass",
          ["Somewhere without flowers or grass", "A snowy field", "A bottle"],
          "The small raindrops say they want to go where flowers and grass grow. The big raindrops go where they do not."),
        ("Where do the big raindrops want to go?", "Somewhere without flowers or grass",
          ["Somewhere with flowers and grass", "Above the clouds, never to come down", "The small raindrops' home"],
          "The big raindrops say they want to go where there are no flowers or grass."),
        ("What happens after the rain in places that already have flowers and grass?", "The flowers become redder and the grass greener",
          ["The flowers and grass disappear", "The first flower blooms", "Stones grow"],
          "Where flowers and grass already grow, the flowers become redder and the grass greener."),
        ("What happens after the rain in places that had no flowers or grass?", "Red flowers bloom and green grass grows",
          ["Nothing changes", "The flowers become redder and the grass greener", "The place turns into a snowy field"],
          "The rain brings red flowers and green grass to places where none grew before."),
    ],
)

K(
    "g1a_shuo", "Language Activities 8: Describe a Picture in Order", "Writing Foundations", 1, "上", 8, "procedural",
    "Describe who is where and what happens first and next, following the picture.",
    "xz_12",
    [
        ("Picture prompt: a child washes hands before eating. Which sentence gives the events in order?", "The child washes their hands first, then eats.",
          ["The child eats and washes hands.", "Eating.", "The child eats first; washing hands is not mentioned"],
          "First and then make the order of the two actions clear. A single word is not enough."),
        ("Picture prompt: a bird is singing in a tree. Which sentence matches the picture?", "The bird is perched in a tree and singing.",
          ["The bird is swimming in a river.", "The bird chopped down the tree.", "Only the word “tree.”"],
          "Describe who is where and what they are doing; do not change the event."),
        ("Which description is easiest for someone else to understand?", "Mom is washing dishes in the kitchen.",
          ["Mom dishes.", "Kitchen dishes Mom.", "Wash."],
          "State who is doing what and where, in that order, to make the sentence clear."),
        ("Which approach is not suitable when describing a picture?", "Say only the word “run”",
          ["Xiaoming is running on the playground.", "A cat is sleeping on the sofa.", "The rain stopped and the sky cleared."],
          "One word does not tell who is running or where. The other sentences express complete ideas."),
    ],
)

# ---------- Grade 1, Volume 2 ----------
# Revised 2024 unified-curriculum outline used in spring 2025. Texts are listed in volume order; language activities cover vocabulary and sentence skills.

K(
    "g1b_chun", "Literacy: Spring, Summer, Autumn, Winter", "Literacy and Writing", 1, "下", 1, "conceptual",
    "Recognize the four seasons and the phrases 春风吹, 夏雨落, 秋霜降, and 冬雪飘.",
    "sz_12",
    [
        ("In 秋霜降, during which season is frost most common?", "The cold period from autumn into winter",
          ["At midday in summer", "When flowers bloom in spring", "Every afternoon"],
          "Frost appears in cold weather; the text pairs it with autumn and winter, not summer."),
        ("Which phrase describes a winter scene?", "冬雪飘", ["春风吹", "夏雨落", "山花红"], "冬雪飘 describes winter; the other phrases describe spring, summer, or flowers."),
        ("Which radical appears at the top of both 雪 and 霜?", "The rain radical", ["The roof radical", "The grass radical", "The bamboo radical"], "雪, 霜, and 雷 have the rain radical. 花 has the grass radical."),
        ("Which pair matches the text?", "春风吹，夏雨落", ["春风落，夏雨吹", "秋霜飘，冬雪降", "冬雪吹，春霜落"], "The text pairs 春风 with 吹, 夏雨 with 落, 秋霜 with 降, and 冬雪 with 飘."),
    ],
)

K(
    "g1b_xingshi", "Literacy: Surnames Song", "Literacy and Writing", 1, "下", 1, "conceptual",
    "Read the Surnames Song and use familiar characters to remember common surnames such as 李, 张, 胡, and 吴.",
    "sz_12",
    [
        ("In the mnemonic 木子李, which two parts form the surname 李?", "木 and 子", ["弓 and 长", "古 and 月", "口 and 天"], "木 and 子 combine to form 李. 弓 and 长 form 张; 古 and 月 form 胡; 口 and 天 form 吴."),
        ("Which surname is described by the mnemonic 弓长张?", "张", ["李", "胡", "吴"], "弓 and 长 combine to form 张. 李 is formed from 木 and 子, not 弓 and 长."),
        ("Which surname is formed by 古 and 月?", "胡", ["吴", "徐", "许"], "古 and 月 form 胡. 口 and 天 form 吴; 徐 and 许 are introduced later."),
        ("The song says China has many surnames. Which line follows?", "张王李赵遍地刘", ["There is only one surname, 李", "春风吹，夏雨落", "小娃撑小艇"], "The next line lists 张, 王, 李, and 赵, followed by 刘."),
    ],
)

K(
    "g1b_qing", "Literacy: Little Frog", "Literacy and Writing", 1, "下", 1, "conceptual",
    "Read “Little Frog,” distinguish 清, 晴, 睛, 情, and 请, and learn that frogs protect seedlings.",
    "sz_12",
    [
        ("What good things does the frog do in “Little Frog”?", "Protects seedlings and eats pests",
          ["Bites the seedlings", "Only sleeps in the river", "Makes the seedlings sick"],
          "The poem says the frog protects seedlings and eats pests."),
        ("In the phrase about a little frog with big eyes, which character means “eye”?", "睛", ["晴", "清", "请"], "睛, meaning “eye,” has the eye radical 目. 晴 has the sun radical, 清 the water radical, and 请 the speech radical."),
        ("How does the poem ask readers to treat the frog?", "Protect it so the seedlings stay healthy",
          ["Catch it to play with it", "Stop it from eating pests", "Chase it out of the rice field"],
          "The poem asks readers to protect the frog so the seedlings stay healthy."),
        ("Which radical appears in 情?", "The heart radical 忄", ["The water radical", "The sun radical", "The speech radical"],
          "情 in 心情 and 事情 has the heart radical 忄. 清 has the water radical, and 晴 has the sun radical."),
    ],
)

K(
    "g1b_mi", "Literacy: Character Riddles", "Literacy and Writing", 1, "下", 1, "conceptual",
    "Read the character riddles and use radicals to identify 秋, 请, 情, 晴, and 清.",
    "sz_12",
    [
        ("“Green on the left, red on the right; when they meet, cool winds arrive.” Which character is the answer?", "秋", ["春", "明", "花"], "禾 is green on the left and 火 is red on the right; together they form 秋, the character for autumn."),
        ("“When 言 arrives, people treat one another with respect.” Which character is the answer?", "请", ["情", "晴", "清"], "Adding the speech radical 言 to 青 forms 请, a polite way to make a request."),
        ("“The sun rises and the sky is cloudless.” Which character is the answer?", "晴", ["清", "请", "情"], "Adding the sun radical 日 to 青 forms 晴, meaning clear weather."),
        ("“Water arrives, pure and transparent.” Which character is the answer?", "清", ["晴", "请", "青"], "Adding the water radical 氵 to 青 forms 清, meaning clear or pure."),
    ],
)

K(
    "g1b_bang", "Oral Communication: Asking for Help", "Writing Foundations", 1, "下", 1, "procedural",
    "When asking for help, say who you are asking, what you need, and use polite words such as “please” and “thank you.”",
    "xz_12",
    [
        ("A pencil rolled under the desk and you want a classmate to help. Which request is most appropriate?", "请你帮我捡一下铅笔，谢谢！",
          ["You must pick it up for me right now!", "Pencil.", "Do not pick it up."],
          "Start with a polite request, explain what help you need, and thank the person. A command or a single word is unclear."),
        ("What should you say after someone has helped you?", "谢谢你", ["Go away", "That was your job anyway", "Run off without saying anything"],
          "Thank the person for helping. Do not tell them to go away or leave without saying thanks."),
        ("What should you make clear when asking for help?", "Whom you are asking and what help you need",
          ["Only shout “Hey”", "Criticize the other person first", "Start with something completely unrelated"],
          "The other person needs to know whom you are addressing and what you need."),
        ("Which approach is inappropriate?", "Loudly order someone to hurry up and do it for you",
          ["Use a polite request", "Explain what help you need", "Thank the person afterward"],
          "Ask politely. Ordering someone is not a request."),
    ],
)

K(
    "g1b_tongyao", "Happy Reading: Nursery Rhymes and Songs", "Reading Comprehension", 1, "下", 1, "conceptual",
    "Enjoy reading nursery rhymes and songs aloud with rhythm, and share them with others.",
    "yd_12",
    [
        ("What is a common feature of nursery rhymes and children's songs?", "Short, rhythmic lines that are easy to say aloud",
          ["Very long lines with no rhythm", "They can only be written from memory, not read aloud", "They must be rewritten in classical prose"],
          "Nursery rhymes and songs often have short, rhyming lines that are suitable for reading aloud."),
        ("What is a good way to read a nursery rhyme?", "Read with a rhythm and clap along",
          ["Skip every word", "Read only the title", "Deliberately read without pauses"],
          "Reading with rhythm helps listeners enjoy the rhyme. Skipping the lines is not reading them."),
        ("What can you do after reading a song you like?", "Read it to an adult or read it again with someone",
          ["Close the book and never read it again", "Remember only one punctuation mark", "Change it into another story but call it the original"],
          "Happy Reading encourages reading more and sharing it. Changing the content means it is no longer the same song."),
        ("Which material is suitable for this reading section?", "A short, rhythmic nursery rhyme",
          ["A long product manual", "A blank page", "A table of numbers"],
          "This section is for nursery rhymes and songs, not manuals or tables."),
    ],
)

K(
    "g1b_reai", "Reading “Love for the Communist Party of China”", "Reading Comprehension", 1, "下", 2, "reasoning",
    "Identify the feeling expressed in the text and distinguish it from the neighboring readings.",
    "yd_12",
    [
        ("What feeling does “Love for the Communist Party of China” mainly express?", "Love for the Communist Party of China",
          ["How to wrap rice dumplings", "Whom a gecko asks for a tail", "A lotus leaf as a cradle"],
          "The title and text express love for the Communist Party of China, not a story about rice dumplings or borrowing a tail."),
        ("Which sentence matches the message of the text?", "We love the Communist Party of China",
          ["We do not want to learn about the Communist Party of China", "This text is about a duckling swimming", "This is an old poem about the moon"],
          "The text expresses love. The duckling story and moon poem are different readings."),
        ("How is it different from “The Well-Digger Must Not Be Forgotten”?", "This text expresses love for the Party; the other is about a village well and its stone tablet",
          ["Both texts are about lotus leaves and dragonflies", "Both are the same poem by Luo Binwang", "Both are only about games on the playground"],
          "The other text describes the well and its inscription; this one expresses love for the Communist Party of China."),
        ("Which interpretation is incorrect?", "The text encourages readers to hate the Communist Party of China",
          ["The text expresses love", "The title shows that it is about love", "It is not the same reading as “The Well-Digger Must Not Be Forgotten”"],
          "The text expresses love, not hate. The other interpretations are consistent with it."),
    ],
)

K(
    "g1b_shui", "Reading “The Well-Digger Must Not Be Forgotten”", "Reading Comprehension", 1, "下", 2, "reasoning",
    "Identify who led the villagers in digging the well at Shazhouba and what the stone tablet said.",
    "yd_12",
    [
        ("Where is the well?", "Shazhouba, outside Ruijin", ["A school in Beijing", "A lotus pond south of the Yangtze", "There is no village near the well"],
          "The passage says the well was dug in Shazhouba, a village outside Ruijin."),
        ("Who led the villagers in digging the well?", "Chairman Mao",
          ["A rooster", "The poet Li Bai", "A shopkeeper"],
          "The passage says Chairman Mao led the villagers in digging a well while working in Shazhouba."),
        ("What sentence was carved on the stone tablet beside the well?", "吃水不忘挖井人，时刻想念毛主席",
          ["When I was young, I did not know the moon; I called it a white jade plate", "Goose, goose, goose, neck curved toward the sky", "The curved moon is like a little boat"],
          "The inscription reads 吃水不忘挖井人，时刻想念毛主席."),
        ("Why do the villagers remember the person who helped dig the well?", "They could drink its sweet, clear water",
          ["Lotus flowers grew in the well", "The water was salty", "They filled in the well"],
          "The villagers remember the well digger because the well provided sweet, clear water."),
    ],
)

K(
    "g1b_kankan", "Reading “I Really Want to Go and See”", "Reading Comprehension", 1, "下", 2, "reasoning",
    "Understand that the speaker wants to see the flag-raising at Tiananmen and the snow lotuses in the Tianshan Mountains.",
    "yd_12",
    [
        ("Where will the winding path lead, according to the mother?", "Out of the Tianshan Mountains",
          ["Out of Beijing", "Out of a lotus pond", "Out of a playground"],
          "The mother says the winding path leads out of the Tianshan Mountains, with Beijing in the distance."),
        ("What does the speaker want to see in Beijing?", "The magnificent Tiananmen and the flag-raising ceremony",
          ["Snow lotuses in the Tianshan Mountains", "A well in Shazhouba", "White lotuses in a pond"],
          "Beijing has the magnificent Tiananmen and a grand flag-raising ceremony. Snow lotuses grow in the Tianshan Mountains."),
        ("What can be seen by following the broad road out of Beijing, according to the father?", "Distant snow lotuses in the Tianshan Mountains",
          ["The flag-raising ceremony at Tiananmen", "Rice dumplings for the Dragon Boat Festival", "A soccer ball on the playground"],
          "The road leads from Beijing toward the distant Tianshan Mountains, where white snow lotuses grow. The flag-raising is in Beijing."),
        ("Which line does the speaker repeat to the parents?", "我多想去看看",
          ["I do not want to see anything", "Before my bed, the bright moonlight", "A little child rows a small boat"],
          "The speaker repeats 我多想去看看. The other lines come from poems, not this text."),
    ],
)

K(
    "g1b_xing", "Language Activities 2: Similar-Looking and Homophonous Characters", "Literacy and Writing", 1, "下", 2, "conceptual",
    "Distinguish 青, 清, 请, 晴, and 情, and choose the correct character by its radical.",
    "sz_12",
    [
        ("Which character belongs in “The river water is clear”?", "清", ["青", "请", "晴"], "清 in 清水 has the water radical. 青 in 青草 does not; 请 has the speech radical, and 晴 has the sun radical."),
        ("Which character belongs in “The weather is sunny today”?", "晴", ["清", "请", "情"], "晴 relates to the sun and has the sun radical. 清 has the water radical, 请 the speech radical, and 情 the heart radical."),
        ("Which character belongs in “Please come in”?", "请", ["清", "晴", "青"], "Use 请, with the speech radical, when politely asking someone to do something."),
        ("Which character belongs in “I am in a good mood”?", "情", ["请", "晴", "清"], "情 in 心情 relates to feelings and has the heart radical. 请 has the speech radical and 晴 the sun radical."),
    ],
)

K(
    "g1b_gong", "Reading “The Rooster and the Duckling”", "Reading Comprehension", 1, "下", 3, "reasoning",
    "Understand that the rooster catches insects, the duckling swims, and they help each other.",
    "yd_12",
    [
        ("Who caught an insect beside the haystack?", "The rooster", ["The duckling", "The gecko", "The fish"], "The rooster has a pointed beak and can catch insects. The duckling's flat beak cannot."),
        ("What did the rooster do when the duckling could not catch an insect?", "Shared the insects he had caught with the duckling",
          ["Ate them all and left", "Pushed the duckling into the river", "Told the duckling to catch fish"],
          "The rooster gave the duckling some of the insects he caught."),
        ("What happened when the rooster secretly went into the river?", "It could not swim and began to sink",
          ["It swam faster than the duck", "It caught many insects in the river", "The river was shallow, so it walked across"],
          "The duckling warned that the rooster could not swim. The rooster ignored the warning and began to sink."),
        ("Who rescued the rooster and brought it to shore?", "The duckling", ["The rooster itself", "A fish", "A frog"],
          "The duckling swam over, let the rooster ride on its back, and carried it to shore."),
    ],
)

K(
    "g1b_que", "Reading “The Tree and the Magpie”", "Reading Comprehension", 1, "下", 3, "reasoning",
    "Understand that one tree and one magpie were lonely, but neighbors later made them happy.",
    "yd_12",
    [
        ("At first, how many trees and magpies were there?", "One tree and one magpie",
          ["Many trees and many magpies", "No trees and no magpies", "Two trees and three magpies"],
          "At first there was one tree, one nest, and one magpie."),
        ("How did the tree and magpie feel then?", "Lonely", ["Happy", "Noisy", "Eager to chase away the neighbors"], "With only one of each, both the tree and the magpie felt lonely."),
        ("What arrived later and made everyone happy?", "Many trees, nests, and magpies",
          ["A large river", "A snowstorm", "A well"],
          "With more neighbors, they could play together and became happy."),
        ("What is the main message of the story?", "Neighbors and friends help us feel less lonely",
          ["Fewer trees are always better", "Magpies should not build nests", "Loneliness is better than happiness"],
          "They were lonely at first and became happy after making friends. Friends and neighbors matter."),
    ],
)

K(
    "g1b_kuaile", "Reading “Fun Any Way You Play”", "Reading Comprehension", 1, "下", 3, "reasoning",
    "Understand that playing alone can be fun and playing with others can be even more enjoyable.",
    "yd_12",
    [
        ("What does the text say about playing alone?", "It can be good too; you can quietly do your own activity",
          ["Playing alone is never fun", "Playing alone is forbidden", "Playing alone is always more fun than playing with many people"],
          "The text says playing alone can be good and playing with many people can be even more fun."),
        ("What does “A story needs someone to listen” mean?", "Some activities require another person",
          ["You can only tell stories secretly by yourself", "Fewer listeners are always better", "Stories must not be shared"],
          "A story needs someone to tell it and someone to listen, so this activity requires another person."),
        ("What is the main message of the text?", "Playing alone can be fun, and playing together can be even more fun",
          ["Only playing alone is fun", "A group can never play successfully", "A game counts only if someone loses"],
          "The text says that both solo play and group play can be fun."),
        ("Which statement is the opposite of the text's message?", "Playing with others is not fun at all",
          ["Playing alone can be good", "Playing with many people can be more fun", "Different group sizes allow different kinds of play"],
          "The text says playing with others can be more fun, so the first statement contradicts it."),
    ],
)

K(
    "g1b_dian", "Oral Communication: Making a Phone Call", "Writing Foundations", 1, "下", 3, "procedural",
    "Greet the caller, identify yourself, explain the reason clearly, and say goodbye at the end.",
    "xz_12",
    [
        ("Which is the best way to begin a phone call?", "喂，你好，我是小明",
          ["Who are you? Hurry up and talk.", "Hang up without saying anything", "Order the other person around without giving your name"],
          "Greet the other person first, then say who you are. Without a greeting or your name, the other person may not know who is calling."),
        ("You want your mother to pick you up. Which sentence explains the request clearly?", "妈妈，我是小明，请您放学后来学校接我",
          ["Pick me up.", "Guess who I am; I will not tell you.", "Come quickly, but I will not say where."],
          "Explain who you are, when you need help, and where. A single word does not give enough information."),
        ("What should you do if you did not hear what the other person said?", "请您慢慢再说一遍",
          ["Scold them loudly", "Hang up immediately and never call again", "Pretend you heard and agree to anything"],
          "Ask the person to repeat it if you did not hear. Agreeing without understanding may cause a mistake."),
        ("How should you end the call after you have finished speaking?", "Say 再见, then hang up",
          ["Throw the phone away without speaking", "Keep the line open and say nothing", "Scold the other person before hanging up"],
          "Say goodbye before hanging up. Do not throw the phone away or end the call without saying goodbye."),
    ],
)

K(
    "g1b_jing", "Classical Poem: “Quiet Night Thoughts”", "Poetry", 1, "下", 4, "conceptual",
    "Recite Li Bai's poem and distinguish its lines from those in “Song of the Old Bright Moon.”",
    "gs_12",
    [
        ("Which line follows 床前明月光?", "疑是地上霜", ["呼作白玉盘", "低头思故乡", "举头望明月"], "The speaker first mistakes the moonlight for frost on the ground; the lines about looking up and thinking of home come later. 白玉盘 is from another poem."),
        ("Which line follows 举头望明月?", "低头思故乡", ["疑是地上霜", "飞在青云端", "床前明月光"], "After looking up at the moon, the speaker looks down and thinks of home."),
        ("Who wrote “Quiet Night Thoughts”?", "Li Bai", ["Du Fu", "Luo Binwang", "Li Jiao"], "“Quiet Night Thoughts” was written by Li Bai."),
        ("What does the poet mistake the moonlight for?", "Frost on the ground", ["A white jade plate", "A little boat", "A mirror in a celestial palace"], "The poem says 疑是地上霜. The white jade plate and celestial mirror are from another poem."),
    ],
)

K(
    "g1b_ye", "Reading “Nighttime”", "Reading Comprehension", 1, "下", 4, "reasoning",
    "Read how a child changes from being afraid of the dark to becoming brave.",
    "yd_12",
    [
        ("What is the child like at the beginning of the story?", "Very timid and afraid to look outside after dark",
          ["Very brave and runs outside every night", "Already unafraid of every dark night", "Afraid to open his eyes during the day"],
          "At first, he is so timid that he will not look outside when it gets dark."),
        ("What does the mother do to help him?", "Tells him brave stories again and again",
          ["Boards up every window", "Tells him never to look outside", "Takes him swimming in the river"],
          "The mother tells him stories about bravery repeatedly."),
        ("What does he discover when he looks outside later?", "Night is not so frightening",
          ["There really is a monster outside", "The plants disappear at night", "The moon has fallen"],
          "When he looks outside again, he sees the nighttime scenery and his heart no longer races."),
        ("What is the story mainly about?", "Understanding the night can help someone become brave",
          ["Never go outside after dark", "Stories about courage are useless", "Children should always be afraid"],
          "He changes from being afraid to look outside to feeling less afraid, even on a very dark night."),
    ],
)

K(
    "g1b_zong", "Reading “Dragon Boat Festival Rice Dumplings”", "Reading Comprehension", 1, "下", 4, "reasoning",
    "Learn that rice dumplings are wrapped in reed leaves and that the festival's races and dumplings honor Qu Yuan.",
    "yd_12",
    [
        ("What are the rice dumplings wrapped in?", "Green reed leaves (箬叶)",
          ["Red plastic wrap", "Thick cotton cloth", "Hard metal"],
          "The dumplings are wrapped in green 箬叶 and filled with white glutinous rice."),
        ("What is often placed in the middle of a dumpling?", "A red date (枣)",
          ["A pebble", "A piece of ice", "A wad of cotton"],
          "The passage says there is a red date in the glutinous rice."),
        ("What else do people do during the festival to honor Qu Yuan?", "Race dragon boats",
          ["Build snowmen", "Put up a moon-inscribed tablet beside a well", "Play tug-of-war on a field"],
          "The passage says people race dragon boats and eat rice dumplings to honor the patriotic poet Qu Yuan."),
        ("Which kind of dumpling does the grandmother make?", "Fresh-meat rice dumplings (鲜肉粽)",
          ["Snow-lotus dumplings", "Lotus-leaf cradle dumplings", "Pencil dumplings"],
          "The grandmother makes red-date, red-bean, and fresh-meat dumplings."),
    ],
)

K(
    "g1b_biao", "Language Activities 4: Punctuation and Words", "Sentences", 1, "下", 4, "procedural",
    "Choose a period, question mark, or exclamation mark to match the sentence's meaning.",
    "jz_12",
    [
        ("Which punctuation mark belongs at the end of “What is your name”?", "Question mark (？)", ["Period (。)", "Exclamation mark (！)", "Comma (，)"], "It is a question, so end it with a question mark."),
        ("Which punctuation mark belongs at the end of “The weather is so nice today”?", "Exclamation mark (！)", ["Question mark (？)", "Comma (，)", "Enumeration comma (、)"], "It expresses excitement, so use an exclamation mark. Use a period for a neutral statement."),
        ("Which punctuation mark belongs at the end of “I have a pencil”?", "Period (。)", ["Question mark (？)", "Exclamation mark (！)", "Comma (，)"], "It states a fact, so end it with a period."),
        ("Which sentence uses punctuation correctly?", "I like drawing。", ["Who are you。", "This flower smells wonderful？", "The bird is singing？"], "I like drawing is a statement. Who are you is a question, and wonderful expresses excitement."),
    ],
)

K(
    "g1b_dongwu", "Literacy: Animal Rhyme", "Literacy and Writing", 1, "下", 5, "conceptual",
    "Read the animal rhyme and match 蜻蜓, 蝴蝶, 蚯蚓, 蚂蚁, 蝌蚪, and 蜘蛛 with their actions.",
    "sz_12",
    [
        ("Which animal spreads its wings and flies in the sky?", "蜻蜓", ["蚯蚓", "蚂蚁", "蝌蚪"], "蜻蜓 flies in the sky; 蚯蚓 lives underground, 蚂蚁 moves on the ground, and 蝌蚪 swims in a pond."),
        ("Which animal builds a palace underground?", "蚯蚓", ["蝴蝶", "蜘蛛", "蜻蜓"], "蚯蚓 builds underground; 蝴蝶 is among the flowers, and 蜘蛛 weaves a web by the house."),
        ("What does 蚂蚁 do?", "Carries food on the ground", ["Plays hide-and-seek among flowers", "Weaves a web by the house", "Swims around in a pond"], "蚂蚁 carries food. 蝴蝶 plays hide-and-seek, and 蜘蛛 weaves a web."),
        ("Which animal busily weaves a web in front of the house?", "蜘蛛", ["蝌蚪", "蝴蝶", "蚯蚓"], "蜘蛛 weaves a web; 蝌蚪 swims in a pond."),
    ],
)

K(
    "g1b_gujin", "Literacy: Past and Present", "Literacy and Writing", 1, "下", 5, "conceptual",
    "Read the paired-word rhyme and remember 古对今, 严寒对酷暑, and 和风对细雨.",
    "sz_12",
    [
        ("Which pair comes immediately after 古对今?", "圆对方", ["严寒对酷暑", "晨对暮", "桃对李"], "The rhyme lists 古对今 and 圆对方 before 严寒对酷暑."),
        ("What is paired with 严寒?", "酷暑", ["春暖", "秋凉", "细雨"], "严寒 pairs with 酷暑; 春暖 pairs with 秋凉, and 和风 with 细雨."),
        ("Which pair follows 和风对细雨?", "朝霞对夕阳", ["莺歌对燕舞", "鸟语对花香", "雪对霜"], "朝霞对夕阳 follows 和风对细雨; 莺歌对燕舞 comes later."),
        ("What is paired with 莺歌?", "燕舞", ["花香", "柳杨", "鸟语"], "莺歌 pairs with 燕舞. 鸟语 pairs with 花香."),
    ],
)

K(
    "g1b_caochang", "Literacy: On the Playground", "Literacy and Writing", 1, "下", 5, "conceptual",
    "Read “On the Playground” and distinguish the hand-radical characters 拍, 拔, 打 from the foot-radical characters 跳, 跑, 踢.",
    "sz_12",
    [
        ("Which radical do 拍, 拔, and 打 share?", "The hand radical 扌", ["The foot radical", "The speech radical", "The water radical"], "拍, 拔, and 打 describe hand actions, so they use the hand radical 扌."),
        ("Which radical do 跳, 跑, and 踢 share?", "The foot radical 足", ["The hand radical", "The mouth radical", "The wood radical"], "跳, 跑, and 踢 describe foot actions, so they use the foot radical 足."),
        ("Which activity is mainly done with the foot?", "踢足球",
          ["拍皮球", "拔河", "打球"],
          "踢足球 is grouped with jumping and running. 拍, 拔, and 打 use the hand radical and relate to hand actions."),
        ("Where do students do activities such as playing ball and running in the text?", "On the playground",
          ["In a pond", "Beside the well in Shazhouba", "On a lotus leaf"],
          "The text is about students doing activities on the playground."),
    ],
)

K(
    "g1b_ren", "Literacy: “At the Beginning of Life”", "Literacy and Writing", 1, "下", 5, "conceptual",
    "Read an excerpt from the Three Character Classic and memorize 人之初, 性本善, 子不学, and 玉不琢.",
    "sz_12",
    [
        ("Which line follows 人之初?", "性本善", ["习相远", "非所宜", "不知义"], "The excerpt reads 人之初，性本善, followed later by 性相近，习相远."),
        ("Which line follows 性相近?", "习相远", ["性本善", "老何为", "不成器"], "性相近，习相远 means people may be similar by nature but differ through their habits."),
        ("Which line follows 玉不琢?", "不成器", ["不知义", "非所宜", "性本善"], "玉不琢，不成器 is followed by 人不学，不知义. Do not mix up the pairs."),
        ("What does 子不学，非所宜 mean?", "It is wrong for a child not to study",
          ["Jade does not need carving", "People's natures are very different", "It is best to start learning only when old"],
          "子不学，非所宜 and 幼不学，老何为 both encourage learning from childhood."),
    ],
)

K(
    "g1b_youxi", "Oral Communication: Playing a Game Together", "Writing Foundations", 1, "下", 5, "procedural",
    "Explain the rules when inviting others to play, then take turns and follow the rules.",
    "xz_12",
    [
        ("Which sentence is the best way to invite someone to play?", "我们一起做游戏，好吗",
          ["You are not allowed to play", "You cannot ask about the rules", "Game"],
          "Make a polite invitation first. A single word does not tell others what to play."),
        ("What should you do before starting the game?", "Explain the rules clearly",
          ["Start grabbing things without explaining the rules", "Push others away first", "Announce that only you can win"],
          "Everyone needs to know how to play before the game can begin."),
        ("What is the right thing to do while playing?", "Take turns and follow the agreed rules",
          ["Grab a turn before someone is finished", "Cry when you lose and stop others from playing", "Deliberately break the rules you just agreed on"],
          "Play together by taking turns and following the rules. Grabbing and crying can stop the game."),
        ("Which behavior is not suitable for a group game?", "One person changes the rules suddenly and will not let others speak",
          ["Explain how to play first", "Take turns", "Invite others to play again afterward"],
          "Everyone should know the rules, and everyone should be allowed to speak."),
    ],
)

K(
    "g1b_chi", "Classical Poem: “On the Pond”", "Poetry", 1, "下", 6, "conceptual",
    "Recite Bai Juyi's poem and understand that the child's lotus-picking leaves a trail in the duckweed.",
    "gs_12",
    [
        ("Which line follows 小娃撑小艇?", "偷采白莲回", ["浮萍一道开", "不解藏踪迹", "早有蜻蜓立上头"], "The child rows a little boat and secretly picks a white lotus. 浮萍一道开 is the final line."),
        ("Which line follows 不解藏踪迹?", "浮萍一道开", ["偷采白莲回", "小娃撑小艇", "树阴照水爱晴柔"], "The child does not know how to hide the trail; the boat parts the duckweed."),
        ("Who wrote “On the Pond”?", "Bai Juyi", ["Yang Wanli", "Li Bai", "Luo Binwang"], "“On the Pond” was written by Bai Juyi. Yang Wanli wrote a different poem, “The Little Pond.”"),
        ("What does 浮萍一道开 show?", "The boat passed and parted the duckweed in a line",
          ["There was no duckweed", "The child hid the trail completely", "The pond dried up"],
          "The child did not hide the trail; the boat left a line through the duckweed."),
    ],
)

K(
    "g1b_xiao", "Classical Poem: “The Little Pond”", "Poetry", 1, "下", 6, "conceptual",
    "Recite Yang Wanli's poem and distinguish it from Bai Juyi's “On the Pond.”",
    "gs_12",
    [
        ("Which line follows 泉眼无声惜细流?", "树阴照水爱晴柔", ["小荷才露尖尖角", "早有蜻蜓立上头", "偷采白莲回"], "The first lines describe the spring and tree shade; the last two describe the lotus and dragonfly. 偷采白莲回 belongs to “On the Pond.”"),
        ("Which line follows 小荷才露尖尖角?", "早有蜻蜓立上头", ["树阴照水爱晴柔", "浮萍一道开", "早有蜻蜓立上头尖"], "The lotus has just shown its pointed tip, and a dragonfly is already standing on it."),
        ("Who wrote “The Little Pond”?", "Yang Wanli", ["Bai Juyi", "Li Bai", "He Zhizhang"], "“The Little Pond” was written by Yang Wanli; Bai Juyi wrote “On the Pond.”"),
        ("Where does the dragonfly stand?", "On the lotus leaf that has just shown its tip",
          ["Inside the white-lotus boat", "On a path through the duckweed", "On a tree beside the spring"],
          "The poem says the lotus has just shown its pointed tip and a dragonfly is already standing on it."),
    ],
)

K(
    "g1b_lang", "Reading “Waves”", "Reading Comprehension", 1, "下", 6, "reasoning",
    "Understand how the waves tickle a child's feet on the beach, making the child laugh.",
    "yd_12",
    [
        ("Where is the speaker playing in “Waves”?", "On a beach by the sea",
          ["On a snowy mountain", "Inside a pencil case in a classroom", "On a Dragon Boat Festival boat"],
          "The child walks on the beach, where the waves reach their feet."),
        ("What do the waves do when they reach the child's feet?", "Tickle the child's feet",
          ["Bite the feet", "Drag the child into deep water", "Stop moving forever"],
          "The waves tickle the feet, making them tingle; they are not trying to hurt anyone."),
        ("How does the child feel?", "Tingly and ticklish, and unable to stop laughing",
          ["Terrified and crying", "Angry and never smiling", "Thinking the waves are monsters"],
          "Being tickled makes the child want to laugh. The text describes joy, not fear."),
        ("What happens after the waves tickle the child?", "They run away again as the child laughs",
          ["They stay on the feet all day", "They become a fish in a pencil case", "They carry away the whole beach"],
          "The waves run away again; they do not stay on the feet or turn into monsters."),
    ],
)

K(
    "g1b_heye", "Reading “Round Lotus Leaves”", "Reading Comprehension", 1, "下", 6, "reasoning",
    "Match the dewdrop, dragonfly, frog, and little fish with what each calls the lotus leaf.",
    "yd_12",
    [
        ("What does the dewdrop call the lotus leaf?", "A cradle", ["A landing pad", "A stage", "A parasol"], "The dewdrop lies on the leaf and calls it a cradle."),
        ("Who calls the lotus leaf a landing pad?", "The dragonfly", ["The dewdrop", "The frog", "The little fish"], "The dragonfly stands on the leaf and calls it a landing pad."),
        ("What does the frog call the lotus leaf?", "A stage", ["A cradle", "A parasol", "A boat"], "The frog sings on the leaf and calls it a stage."),
        ("What does the little fish call the lotus leaf?", "A parasol", ["A stage", "A landing pad", "A cradle"], "The little fish swims beneath the leaf and calls it a parasol."),
    ],
)

K(
    "g1b_xiayu", "Reading “It Is Going to Rain”", "Reading Comprehension", 1, "下", 6, "reasoning",
    "Understand that low-flying swallows, fish surfacing for air, and ants moving are signs of rain.",
    "yd_12",
    [
        ("Why are the swallows flying low?", "Rain is coming; insects cannot fly high, so the swallows fly low to catch them",
          ["The swallows' wings are broken", "They are racing a rabbit on the ground", "The air is too dry for them to fly"],
          "The air is damp, so tiny water droplets weigh down the insects' wings. The swallows fly low to catch them."),
        ("Why do the little fish swim to the water's surface?", "The water feels stuffy, so they surface for air before the rain",
          ["They want to sunbathe and sleep", "Someone borrowed their tails", "The pond has dried up"],
          "The fish say the water feels stuffy and they need to surface for air, a sign that rain is coming."),
        ("What are the ants busy doing?", "Moving things to higher ground",
          ["Digging holes low down to catch rain", "Running around with the rabbit", "Teaching the rabbit to swim"],
          "The ants know rain is coming and move things higher to keep them dry."),
        ("What happens after the rabbit runs home to tell its mother?", "A heavy rain really begins",
          ["It does not rain all day", "The sun comes out and not a drop falls", "It starts snowing"],
          "The rabbit says rain is coming, and then a heavy rain really begins."),
    ],
)

K(
    "g1b_liang", "Language Activities 6: Classifiers and Reduplicated Words", "Vocabulary", 1, "下", 6, "conceptual",
    "Use classifiers such as 只, 条, 朵, and 头, and understand reduplicated words such as 高高兴兴.",
    "cy_12",
    [
        ("Which classifier best completes 一（ ）鱼?", "条", ["只", "朵", "头"], "Use 条 for 鱼, 只 for frogs, 朵 for flowers, and 头 for cattle."),
        ("Which classifier best completes 一（ ）花?", "朵", ["条", "头", "群"], "Use 朵 for 花, 条 for fish, and 头 for cattle."),
        ("What does 高高兴兴 mean?", "Very happy", ["A little happy", "Unhappy", "Tall and excited"], "The AABB pattern intensifies the meaning; 高高兴兴 means very happy."),
        ("Which reduplicated word is written correctly?", "快快乐乐地唱歌", ["快乐乐地唱歌", "快快乐地唱歌", "乐乐快快地唱歌"], "快乐 becomes 快快乐乐 when reduplicated. Do not omit a character or reverse the order."),
    ],
)

K(
    "g1b_wen", "Reading “The Stationery's Home”", "Reading Comprehension", 1, "下", 7, "reasoning",
    "Understand that the pencil case is the home for the stationery.",
    "yd_12",
    [
        ("Why do Beibei's pencil and eraser often go missing?", "They are not returned to a regular place after use",
          ["The stationery runs away to play", "Her mother hides it", "The pencil case is too small"],
          "Beibei puts things down wherever she happens to be, so she often cannot find them."),
        ("Where does Beibei's mother say the stationery's home is?", "The pencil case",
          ["Outside the desk drawer", "The playground", "A flowerpot"],
          "Pencils, erasers, and sharpeners should all be put back in the pencil case."),
        ("What does Beibei do so that the stationery no longer gets lost?", "Puts it back in the pencil case every day",
          ["Throws all the stationery away", "Never uses pencils again", "Leaves everything on the floor"],
          "Beibei forms the habit of putting stationery away, so it no longer gets lost."),
        ("What is the main message of the story?", "Put things back where they belong after using them",
          ["Stationery has no home", "There is no need to look for lost things", "A pencil case is only for books"],
          "Give stationery a home and return it there after use to keep it from getting lost."),
    ],
)

K(
    "g1b_fen", "Reading “One Minute”", "Reading Comprehension", 1, "下", 7, "reasoning",
    "Understand that sleeping one extra minute made Yuanyuan arrive at school twenty minutes late.",
    "yd_12",
    [
        ("How much longer did Yuanyuan sleep that morning?", "One minute", ["Twenty minutes", "An hour", "A whole day"], "Yuanyuan yawns and asks to sleep one more minute. Being twenty minutes late happens later."),
        ("How late was Yuanyuan when he arrived at school?", "Twenty minutes", ["One minute", "Two minutes", "He was not late"], "After sleeping one extra minute, he meets a red light and misses the bus, arriving twenty minutes late."),
        ("Why did one extra minute of sleep lead to such a long delay?", "The green light turned red and the bus left",
          ["The school closed its doors for the whole day", "The teacher was late too", "The clock suddenly ran twenty times faster"],
          "The lost minute caused him to miss the next light and bus, so the delays added up."),
        ("What is the story's message?", "Value time; do not waste even one minute",
          ["Sleeping one extra minute never matters", "There is no need to go to school if you are late", "Run through a red light"],
          "Yuanyuan's experience shows that even one minute matters."),
    ],
)

K(
    "g1b_dahui", "Reading “The Animal Kingdom Holds a Meeting”", "Reading Comprehension", 1, "下", 7, "reasoning",
    "Understand that an announcement needs to state what, when, and where so people can attend.",
    "yd_12",
    [
        ("What does the bear call everyone to do with the loudspeaker?", "Attend the animal kingdom's meeting",
          ["Pick peaches together", "Help a cotton plant catch aphids", "Play soccer on the playground"],
          "The tiger asks the bear to announce a meeting, not a peach-picking trip or a soccer game."),
        ("What happens if the bear only says “Come to the meeting” without a time or place?", "The animals do not know when or where to go, so they do not come",
          ["Everyone arrives immediately", "Everyone already knows the time and place", "The loudspeaker automatically makes the location clear"],
          "Without the time and place, the animals do not know how to attend, so they stay away."),
        ("What three details should a complete announcement include?", "What the event is, when it is, and where it is",
          ["Only that there is a meeting", "Only whose tail is longest", "Only that the weather is nice"],
          "People need the event, time, and place to arrive on time. Saying only “meeting” is not enough."),
        ("What happens after the time and place are made clear?", "The animals come to the meeting",
          ["No animals come", "The meeting is moved underwater", "The bear cancels the announcement"],
          "Once they know when and where to go, the animals attend."),
    ],
)

K(
    "g1b_houzi", "Reading “The Monkey Goes Down the Mountain”", "Reading Comprehension", 1, "下", 7, "reasoning",
    "Understand how the monkey keeps dropping one thing for another and eventually goes home empty-handed.",
    "yd_12",
    [
        ("What does the monkey pick up first on the way down the mountain?", "An ear of corn", ["A peach", "A watermelon", "A rabbit"], "He first reaches a cornfield, picks an ear of corn, and carries it away. He sees the peach, watermelon, and rabbit later."),
        ("What does the monkey do when he sees a large, red peach?", "Drops the corn and picks the peach",
          ["Carries both the corn and peach home", "Does not look at the peach", "Gives the peach to the rabbit"],
          "He excitedly drops the corn and picks the peach instead."),
        ("What does he do when he sees a cute rabbit?", "Drops the watermelon and chases the rabbit",
          ["Keeps the watermelon and stops chasing", "Takes both the rabbit and watermelon home", "Picks up the corn before chasing"],
          "He drops the watermelon to chase the rabbit, but it runs into the woods and escapes."),
        ("How does the story end?", "The rabbit escapes, and the monkey goes home empty-handed",
          ["He carries the corn, peach, and watermelon home", "He rides the rabbit home", "He only drops the corn and keeps the watermelon"],
          "Because he keeps dropping each thing for the next, he brings nothing home."),
    ],
)

K(
    "g1b_ting", "Oral Communication: Listening to and Telling Stories", "Writing Foundations", 1, "下", 7, "procedural",
    "Listen to the whole story quietly; when retelling it, explain who did what and what happened next.",
    "xz_12",
    [
        ("What should you do while someone else is telling a story?", "Listen quietly until they finish without interrupting",
          ["Sing loudly while listening", "Interrupt with another topic before they finish", "Cover your ears"],
          "Listen carefully first so you can retell it. Singing or covering your ears means you are not listening."),
        ("What is the best order for retelling a story?", "Say who was involved, where it happened, what they did, and then the result",
          ["Give only the ending and omit everything before it", "Say only “then”", "Change the characters but claim it is the same story"],
          "Tell who, where, what happened, and the result in order so the listener can understand."),
        ("Which retelling is easiest to understand?", "The monkey picked corn, then a peach, and finally went home empty-handed",
          ["Corn peach rabbit home monkey", "Home.", "He went home empty-handed, but the earlier events are a secret"],
          "Tell the events in order. A result alone or a jumble of words is unclear."),
        ("Which approach is not suitable for telling a story?", "Put the ending first and leave out who did it",
          ["Tell events in order", "Explain what the characters did", "Ask afterward whether the listener understood"],
          "A mixed-up order and missing characters make a story hard to follow."),
    ],
)

K(
    "g1b_mian", "Reading “Miss Cotton”", "Reading Comprehension", 1, "下", 8, "reasoning",
    "Understand why the swallow, woodpecker, and frog cannot help Miss Cotton, and how ladybugs eat the aphids.",
    "yd_12",
    [
        ("What is making Miss Cotton feel uncomfortable?", "Aphids", ["Ladybugs", "A little fish", "A swallow"], "Aphids are on her leaves. Ladybugs arrive later to help; they are not pests."),
        ("Why can the swallow not remove the insects?", "It can only catch pests that fly in the air",
          ["It ate all the aphids on the leaves", "It can only catch pests in tree trunks", "It can only catch pests in fields"],
          "The swallow says it catches flying pests. Woodpeckers catch insects in tree trunks, and frogs catch pests in fields."),
        ("Where does the woodpecker say it catches pests?", "In tree trunks",
          ["Flying in the air", "On cotton leaves", "In the water"],
          "The woodpecker catches pests in tree trunks, so it cannot help Miss Cotton."),
        ("Who finally eats the aphids?", "A group of ladybugs", ["The swallow", "The woodpecker", "The frog"], "The ladybugs eat all the aphids, and Miss Cotton smiles."),
    ],
)

K(
    "g1b_gu", "Reading the Sound “咕咚”", "Reading Comprehension", 1, "下", 8, "reasoning",
    "Understand that 咕咚 is the sound of a papaya falling into a lake, not a monster.",
    "yd_12",
    [
        ("What is the sound 咕咚?", "The sound of a ripe papaya falling into a lake",
          ["A monster named 咕咚", "A rabbit calling for help", "A wild ox getting angry"],
          "The sound 咕咚 is made when a ripe papaya falls from a tree into the lake."),
        ("What does the rabbit do after hearing 咕咚?", "Runs away in fright",
          ["Jumps into the lake to pick up the papaya", "Checks what happened before running", "Tells everyone not to be afraid"],
          "The rabbit runs without checking and shouts, “Oh no, 咕咚 is coming!”"),
        ("Why do many animals run after the rabbit?", "They hear others shouting and become afraid too",
          ["They all saw the monster", "The wild ox ordered them to run", "The papaya chases them"],
          "The fox and monkeys do not see 咕咚; they run because they follow the shouting animals."),
        ("How does the wild ox help everyone stop being afraid?", "Takes them back to the lake to see that a papaya fell in",
          ["Chases the rabbit out of the woods", "Says 咕咚 is a monster and tells them to keep running", "Drinks all the water in the lake"],
          "After asking what happened, the animals see the papaya by the lake and realize there is nothing to fear."),
    ],
)

K(
    "g1b_xi", "Reading “The Little Gecko Borrows a Tail”", "Reading Comprehension", 1, "下", 8, "reasoning",
    "Understand whom the little gecko asks for a tail, why they cannot lend one, and how it later grows a new tail.",
    "yd_12",
    [
        ("How does the little gecko lose its tail?", "A snake bites it, and the tail breaks off when the gecko struggles",
          ["It cuts the tail off itself", "A little fish borrows it", "It falls off while swimming"],
          "A snake bites the gecko's tail while it catches mosquitoes by a wall. The gecko breaks free and escapes."),
        ("Why does the little fish refuse to lend its tail?", "It needs its tail to push water",
          ["It has no tail", "It already lent its tail to an ox", "It needs its tail to drive away flies"],
          "The fish says it needs its tail to push water. The ox uses its tail to drive away flies."),
        ("What does the swallow use its tail for?", "Controlling its direction",
          ["Pushing water", "Driving away flies", "Catching mosquitoes"],
          "The swallow says it uses its tail to control direction. Fish push water; oxen drive away flies."),
        ("How does the story end?", "The little gecko grows a new tail",
          ["It never has a tail again", "It borrows a peacock's tail", "The snake returns the old tail"],
          "Its mother tells it to turn around, and it sees that a new tail has grown."),
    ],
)

K(
    "g1b_kan", "Language Activities 8: Describe Events Clearly", "Writing Foundations", 1, "下", 8, "procedural",
    "Use the picture to explain in order who is where, what happens first, and what the result is.",
    "xz_12",
    [
        ("Picture prompt: a child puts stationery in a pencil case, then puts on a schoolbag. Which description gives the events in order?",
          "The child puts the stationery away first, then puts on the schoolbag.",
          ["Child schoolbag stationery.", "Then first put stationery away.", "Say only “schoolbag.”"],
          "First and then make the two steps clear. One word does not tell what happened."),
        ("Picture prompt: a duckling rescues a rooster that fell into a river. Which sentence is clearest?",
          "The rooster falls into the river, and the duckling rescues it.",
          ["Rooster duckling river.", "They are flying in the sky.", "The rooster pushes the duckling into the river."],
          "Describe the events in order and do not reverse who rescued whom."),
        ("Which description is suitable for telling someone else?", "In the morning, Yuanyuan slept one extra minute and ended up late",
          ["Yuanyuan.", "Late minute sleep.", "One."],
          "Include the time, who was involved, what happened, and the result."),
        ("Which approach is not suitable when describing a picture?", "Ignore the picture and invent a completely different event",
          ["Describe what you see in order", "Explain who is doing what", "Check afterward that you did not leave anything out"],
          "Describe the events shown in the picture; do not replace them with an unrelated story."),
    ],
)
