# -*- coding: utf-8 -*-
"""Grade 6 topics following the current unified curriculum. The upper volume follows the fall 2026 sequence; the lower volume avoids repeating texts already covered above."""
from zh_lib import K

# Keep Han only for assessed Chinese-language content such as target characters, words, and quoted lines; zh_lib.K emits these items.
# Domain labels and semester markers are schema tokens consumed by zh_lib.K and scripts/validate.py; keep them unchanged.
# ---------- Grade 6, upper volume ----------

K(
    "g6a_cao", "The Grassland", "阅读理解", 6, "上", 1, "reasoning",
    "Understand Lao She's account of the grassland: its boundless green scenery and the deep bond between Mongolian and Han people that makes parting difficult.",
    "yd_56",
    [
        ("Who wrote “The Grassland”?", "Lao She", ["Zong Pu", "Zhu Ziqing", "Lu Xun"], "This text was written by Lao She; Zong Pu wrote “The Knot of Lilacs.”"),
        ("In “羊群一会儿上了小丘，一会儿又下来,” what are the sheep compared to?", "给无边的绿毯绣上了白色的大花", ["Stars hung in the sky", "Lotus leaves spread across a lake", "Buds on a lilac knot"], "The grassland is a green carpet, and the sheep are white flowers embroidered on it. The lilac knot is a metaphor from the next text."),
        ("What does the text emphasize about the grassland's sky and air?", "Fresh air and a clear sky; the view stretches endlessly without seeming hazy", ["Dark clouds press over the city as rain splashes into a boat", "Frogs are the only sound at night", "Lilacs fill the city and countryside"], "The description stresses a clear, far-reaching view. The rainstorm appears in “Drinking at Wanghu Tower after Rain”; the frogs appear in “Moonlit Night on the Yellow Sand Road.”"),
        ("Which line expresses the feeling at the end of the visit?", "蒙汉情深何忍别，天涯碧草话斜阳", ["丁香空结雨中愁", "三军过后尽开颜", "路转溪桥忽见"], "The scenery is beautiful, and the bond between the visitors is deep. The other lines come from “The Knot of Lilacs,” “The Long March,” and “Moonlit Night on the Yellow Sand Road.”"),
    ],
)

K(
    "g6a_ding", "The Knot of Lilacs", "阅读理解", 6, "上", 1, "reasoning",
    "Understand Zong Pu's account of lilacs in the city and countryside, and how a lilac knot represents unresolved sorrow. The after-reading link “Song of Flowers” is not a separate topic.",
    "yd_56",
    [
        ("Who wrote “The Knot of Lilacs”?", "Zong Pu", ["Lao She", "Zhu Ziqing", "Shi Tiesheng"], "This essay was written by Zong Pu; Lao She wrote “The Grassland.”"),
        ("What features of the lilacs does the author emphasize?", "Pale purple flowers clustered together like a knot", ["Large scarlet blossoms", "Leaves only, with no flowers", "Flowers blooming underwater"], "The small buds gather into clusters, which inspire the image of a knot."),
        ("In “丁香空结雨中愁,” what does the sorrow refer to?", "A knot in the rain that cannot be untied, like sorrow in one's heart", ["Lilacs cannot be eaten", "The rain has collapsed a house", "There are too few flowers"], "The knot is a metaphor for sorrow that cannot be easily resolved."),
        ("How does the author view the knots in life at the end?", "Some knots cannot be untied, just as life's problems cannot all be solved", ["Every knot should be avoided", "Lilacs should not bloom", "Sorrow can only keep growing"], "She says knots return every year. A life without any problems would be dull."),
    ],
)

K(
    "g6a_xi", "“Moonlit Night on the Yellow Sand Road”", "古诗文积累", 6, "上", 1, "conceptual",
    "Memorize Xin Qiji's “Moonlit Night on the Yellow Sand Road,” especially the frogs and the sudden appearance of the inn. Also study “A Night at Jiande River” and “Drinking at Wanghu Tower after Rain”; do not mix up their lines.",
    "gs_56",
    [
        ("Which line follows “明月别枝惊鹊”?", "清风半夜鸣蝉", ["稻花香里说丰年", "七八个星天外", "路转溪桥忽见"], "The poem first shows moonlight startling magpies, then cicadas singing at midnight. The line about a good harvest comes later."),
        ("Which line follows “稻花香里说丰年”?", "听取蛙声一片", ["七八个星天外", "听取蝉声一片", "两三点雨山前"], "The speaker hears news of a good harvest in a chorus of frogs, not cicadas. Cicadas appear in the preceding line."),
        ("Which line follows “旧时茅店社林边”?", "路转溪桥忽见", ["路转溪桥忽现", "两三点雨山前", "稻花香里说丰年"], "The poem uses “忽见,” not “忽现.” After the turn at the bridge, the familiar inn suddenly comes into view."),
        ("Who wrote “Moonlit Night on the Yellow Sand Road”?", "Xin Qiji", ["Su Shi", "Meng Haoran", "Li Bai"], "Xin Qiji wrote this ci poem. Su Shi wrote “Drinking at Wanghu Tower after Rain,” and Meng Haoran wrote “A Night at Jiande River.”"),
    ],
)

K(
    "g6a_su", "“A Night at Jiande River”", "古诗文积累", 6, "上", 1, "conceptual",
    "Memorize Meng Haoran's “A Night at Jiande River.” Distinguish its line about the moon drawing near from the line about a chorus of frogs.",
    "gs_56",
    [
        ("Which line follows “移舟泊烟渚”?", "日暮客愁新", ["野旷天低树", "江清月近人", "日暮客愁深"], "The boat stops beside a misty islet, and the traveler's sorrow rises again at dusk. The line about the open fields comes third."),
        ("Which line follows “野旷天低树”?", "江清月近人", ["日暮客愁新", "江清月照人", "野旷天接树"], "The sky seems lower than the trees, and the moon appears close to the traveler. The poem says “近人,” not “照人.”"),
        ("Who wrote “A Night at Jiande River”?", "Meng Haoran", ["Xin Qiji", "Li Bai", "Su Shi"], "This five-character poem was written by Meng Haoran. Do not attribute it to Li Bai just because it mentions the moon."),
        ("Which line is not from “A Night at Jiande River”?", "听取蛙声一片", ["移舟泊烟渚", "日暮客愁新", "江清月近人"], "“听取蛙声一片” is from Xin Qiji's “Moonlit Night on the Yellow Sand Road.”"),
    ],
)

K(
    "g6a_hu", "“Drinking at Wanghu Tower after Rain on June 27”", "古诗文积累", 6, "上", 1, "conceptual",
    "Memorize Su Shi's poem about a sudden rainstorm, especially the raindrops like pearls and Wanghu Tower.",
    "gs_56",
    [
        ("Which line follows “黑云翻墨未遮山”?", "白雨跳珠乱入船", ["卷地风来忽吹散", "白雨跳珠乱入湖", "望湖楼下水如天"], "The raindrops leap into the boat like pearls. They do not leap into the lake. The gusting wind appears in the third line."),
        ("Which line follows “卷地风来忽吹散”?", "望湖楼下水如天", ["黑云翻墨未遮山", "望湖楼下水连天", "白雨跳珠乱入船"], "The wind scatters the clouds, and the water below the tower becomes as clear as the sky."),
        ("Who wrote this poem?", "Su Shi", ["Xin Qiji", "Meng Haoran", "Du Fu"], "Su Shi wrote the poem about Wanghu Tower; Xin Qiji wrote “Moonlit Night on the Yellow Sand Road.”"),
        ("How is the rain in the poem?", "It arrives suddenly and passes quickly", ["It rains all night", "Only one drop falls", "It turns into snow"], "The clouds have not yet covered the mountain when the rain leaps into the boat; one gust of wind scatters the clouds."),
    ],
)

K(
    "g6a_bian", "Writing: A Transformation Story", "习作基础", 6, "上", 1, "application",
    "Imagine becoming something else. Describe what you see and feel after the change, developing the most important part in detail. “I changed and felt happy” is not enough.",
    "xz_56",
    [
        ("If you became a raindrop, which sentence describes an experience after the change?", "I rolled off a leaf tip and struck the dry soil, darkening a crack in the ground.", ["I became rain and felt happy.", "Rain is water.", "The words “A Transformation Story.”"], "Rolling off a leaf and striking dry soil are actions possible only after becoming a raindrop. Simply saying “I was happy” does not describe an experience."),
        ("What should be the focus of a transformation story?", "What you see and do after the change", ["Your home address before the change", "Only your original name", "Copying “The Grassland”"], "Readers want to know what happens in the new form. An address or a copied text does not develop the imagined experience."),
        ("Which approach best fits this writing task?", "Develop the key scene in detail and keep the rest concise", ["Write only “Then I was happy” in every sentence", "Change into an unrelated object in each paragraph", "List vocabulary without describing feelings"], "Detailed development gives the story a memorable scene."),
        ("Which sentence does not describe life after a transformation?", "I handed in my math homework at school on Monday morning.", ["I lay beneath a shoe, bouncing with every step.", "The wind carried my dandelion fluff across the playground.", "I became a pencil and heard the sharpener scrape my body."], "Handing in homework describes the original person. The shoe, dandelion fluff, and pencil belong to transformed viewpoints."),
    ],
)

K(
    "g6a_zi", "Language Corner 1: Pronouncing 屹, 悼, 炽, and 湃", "识字写字", 6, "上", 1, "conceptual",
    "Learn the pronunciations of 屹, 悼, 炽, and 湃 rather than guessing from their components. The memorization poem is Meng Haoran's “Passing an Old Friend's Village,” not “A Night at Jiande River.”",
    "sz_56",
    [
        ("How is the character “屹” pronounced?", "yì", ["qì", "qǐ", "yǐ"], "The character 屹 is pronounced yì."),
        ("How is the character “悼” pronounced?", "dào", ["diào", "dǎo", "zhào"], "The character 悼 is pronounced dào."),
        ("How is the character “炽” pronounced?", "chì", ["zhì", "zhī", "chī"], "The character 炽 is pronounced chì; its phonetic component is only a clue, not the full reading."),
        ("How is the character “湃” pronounced?", "pài", ["bài", "bǎi", "pāi"], "湃 is pronounced pài, not bài."),
    ],
)

K(
    "g6a_chang", "“The Long March” (Seven-Character Regulated Verse)", "古诗文积累", 6, "上", 2, "conceptual",
    "Memorize Mao Zedong's “The Long March,” especially the phrases about taking hardships in stride, a mud pellet, and smiling after victory.",
    "gs_56",
    [
        ("Which line follows “红军不怕远征难”?", "万水千山只等闲", ["五岭逶迤腾细浪", "金沙水拍云崖暖", "千山万水只等闲"], "In the Red Army's eyes, the hardships of the march are ordinary. The poem says “万水千山,” not “千山万水.”"),
        ("Which line follows “五岭逶迤腾细浪”?", "乌蒙磅礴走泥丸", ["金沙水拍云崖暖", "乌蒙磅礴走泥团", "乌蒙磅礴走泥球"], "Even the mighty Wumeng Mountains seem like a rolling mud pellet. The poem says “泥丸,” not “泥团” or “泥球.”"),
        ("Which line follows “金沙水拍云崖暖”?", "大渡桥横铁索寒", ["更喜岷山千里雪", "大渡桥横铁索寒气", "金沙水拍悬崖暖"], "The warmth of the Jinsha River contrasts with the cold iron chains over the Dadu River. The poem says “云崖,” not “悬崖.”"),
        ("Which line ends the poem?", "三军过后尽开颜", ["更喜岷山千里雪", "三军过后尽开颜笑", "红军不怕远征难"], "After crossing Mount Min, the whole army smiles. Do not add a character after “尽开颜.”"),
    ],
)

K(
    "g6a_lang", "The Five Heroes of Langya Mountain", "阅读理解", 6, "上", 2, "reasoning",
    "Understand how the five soldiers lured the enemy to the summit of Langya Mountain and jumped from the cliff after completing their cover mission. Do not confuse this text with the later account of Qiu Shaoyun.",
    "yd_56",
    [
        ("Who was the squad leader?", "Ma Baoyu", ["Huang Jiguang", "Qiu Shaoyun", "Ge Zhenlin"], "Ma Baoyu was the squad leader, and Ge Zhenlin was the deputy. Qiu Shaoyun appears in another text in the unit."),
        ("Why did the soldiers retreat to the summit of Langya Mountain?", "To lure the enemy into a dead end and give the troops and civilians time to evacuate", ["They had lost their way", "There was a bridge at the summit", "They were going to the founding ceremony"], "After completing their cover mission, they deliberately led the enemy to the dead end at Qipantuo."),
        ("What did the soldiers do after running out of ammunition?", "They smashed their weapons and jumped from the cliff one after another", ["They surrendered", "They lay still in the flames", "They returned to the village"], "They could not leave their weapons to the enemy. Smashing them and jumping from the cliff is the climax; remaining still in the flames happens in “My Comrade Qiu Shaoyun.”"),
        ("Which statement agrees with the text?", "They completed their cover mission", ["They left the civilians in front of the enemy", "The five had gone sightseeing", "The squad leader left the group"], "The civilians and troops escaped while the five soldiers held the enemy on Langya Mountain."),
    ],
)

K(
    "g6a_kai", "The Founding Ceremony", "阅读理解", 6, "上", 2, "reasoning",
    "Recall the major events at Tiananmen on October 1, 1949, in chronological order.",
    "yd_56",
    [
        ("On what date was the founding ceremony held?", "October 1, 1949", ["May 4, 1919", "July 1921", "October 1950"], "The text gives October 1, 1949. Do not confuse it with other historical dates."),
        ("Where was the ceremony held?", "Tiananmen Square", ["The summit of Langya Mountain", "The Hall of Supreme Harmony in the Forbidden City", "A ravine in western Shanxi"], "Chairman Mao read the proclamation from Tiananmen Gate. The Hall of Supreme Harmony appears in “The Palace Museum.”"),
        ("What happened after the Central People's Government proclamation was read?", "The national flag was raised and a salute was fired", ["A theatrical performance began immediately", "The crowd dispersed at once", "The flag raising was postponed until the next day"], "The flag was raised, the salute was fired, and then came the military review and the procession."),
        ("What is the main order used in the text?", "The chronological order of the ceremony", ["From the north side of the buildings to the south", "Weather first, with no ceremony", "The procession ends before anything else is mentioned"], "The gathering, proclamation, flag raising, military review, and procession are described in sequence. “The Palace Museum” uses spatial order."),
    ],
)

K(
    "g6a_qiu", "My Comrade Qiu Shaoyun", "阅读理解", 6, "上", 2, "reasoning",
    "Understand how Qiu Shaoyun remained still after catching fire during an ambush so that he would not expose his unit, even at the cost of his life.",
    "yd_56",
    [
        ("What were Qiu Shaoyun and his comrades doing?", "Hiding on a hillside and preparing to attack at dusk", ["Jumping from the summit of Langya Mountain", "Attending the ceremony at Tiananmen", "Fishing in a meadow"], "They were hiding near the enemy's front line. The cliff jump belongs to the five heroes; the fishing story is “The Golden Fishhook.”"),
        ("What did Qiu Shaoyun do when the fire reached him?", "He remained completely still until he died", ["He jumped up and tried to put out the fire", "He shouted for help", "He rolled down the hillside"], "Any movement could expose the whole unit, so he chose to stay still."),
        ("Why could he not put out the fire?", "Moving would have exposed the hidden soldiers", ["He did not know he was on fire", "His comrades would not let him earn merit", "The fire was far away"], "An incendiary bomb landed nearby and set his padded uniform alight. He stayed down for the sake of the others."),
        ("What is the key difference between this text and “The Five Heroes of Langya Mountain”?", "Qiu Shaoyun stayed still in the flames; the five heroes jumped after completing their cover mission", ["Both describe the same battle", "Qiu Shaoyun also jumped from Langya Mountain", "Both take place on October 1, 1949"], "Both are revolutionary soldiers, but they acted differently. Do not confuse the fire with the cliff jump."),
    ],
)

K(
    "g6a_huo", "Writing: A Colorful Event", "习作基础", 6, "上", 2, "application",
    "Describe a group event with both the overall scene and the specific actions of one or two people. “Everyone was happy” does not yet create a scene.",
    "xz_56",
    [
        ("When writing about tug-of-war, which sentence describes the whole scene?", "People shouted on both sides of the field as the red marker in the middle of the rope swayed back and forth.", ["My desk mate gritted their teeth and dug their feet into the dirt.", "The words “tug-of-war.”", "We have P.E. on Monday."], "The shouting on both sides and the swaying marker show the whole scene. The desk mate's effort is one person's detail."),
        ("When describing an event, what counts as a specific detail?", "One or two people's actions, expressions, or words", ["The event's name", "The school's address", "The weather report"], "A specific detail focuses on a person within the larger scene. An address or forecast does not."),
        ("Which passage combines the overall scene with a specific detail?", "The track was crowded with spectators. When it was my turn, I took the baton and nearly slipped.", ["We held an event.", "The track was long.", "The event was colorful and exciting."], "The crowded track gives the overall scene; taking the baton and nearly slipping give personal details."),
        ("What should you avoid when writing about an event?", "Writing only “Everyone was happy,” without showing what anyone did", ["Describing the crowd you saw", "Describing the sounds you heard", "Describing one person's action"], "Let the scene and people show the happiness; otherwise the same phrase could describe any event."),
    ],
)

K(
    "g6a_yan", "Language Corner 2: Patriotic Quotations", "古诗文积累", 6, "上", 2, "conceptual",
    "Memorize the patriotic quotations in this section and identify their authors. A speech should state a position and support it with specific examples; scene writing should combine the overall view with an individual's actions.",
    "gs_56",
    [
        ("Who wrote “捐躯赴国难，视死忽如归”?", "Cao Zhi", ["Lu You", "Li Gang", "Confucius"], "This line is from Cao Zhi's “The White Horse.” Lu You wrote “位卑未敢忘忧国.”"),
        ("What does “位卑未敢忘忧国” mean?", "Even a person of low status dares not forget the country's troubles", ["People of low status need not care about the country", "Only officials should worry about the country", "Forgetting the country brings peace"], "The phrase means that even someone with little status still remembers the country's concerns."),
        ("Who said “祖宗疆土，当以死守，不可以尺寸与人”?", "Li Gang", ["Cao Zhi", "Lu You", "Mencius"], "Li Gang said that ancestral territory should be defended at all costs and not surrendered, even by an inch."),
        ("What kind of person is described by “无求生以害仁，有杀身以成仁”?", "Someone who would rather sacrifice life than harm virtue", ["Someone who will do anything to survive", "Someone who values virtue less than life", "Anyone who is alive"], "This line is from the Analects. Survival should not come at the cost of benevolence."),
    ],
)

K(
    "g6a_zhu", "Bamboo Joint Figures", "阅读理解", 6, "上", 3, "reasoning",
    "Understand how the students make toy fighters from brush handles, only for the teacher to confiscate them and become engrossed in playing too.",
    "yd_56",
    [
        ("What were the toy fighters made from?", "Short sections of brush handle tied together with string", ["Bamboo carved to life size", "Molded clay", "Folded paper airplanes"], "The students sawed old brush handles into short pieces, added heads, and made figures that could fight."),
        ("What happened when the students played with them in class?", "The teacher caught them and confiscated the figures", ["The teacher joined the game immediately", "The figures ran away by themselves", "The students gave them to the principal for safekeeping"], "The teacher came over and took the figures. The students thought they would never see them again."),
        ("What did the students see through the office door after school?", "The teacher playing with the figures, completely absorbed", ["The teacher throwing them in the trash", "An empty office", "The teacher writing a self-criticism"], "The teacher had found them fun too. Confiscating them did not mean he wanted to destroy them."),
        ("What is the funniest part of the story?", "The teacher who forbade the game becomes just as absorbed in it", ["The figures really defeat an enemy", "The students stop making crafts forever", "Brush handles become more important than books"], "Even a toy made from discarded materials can be hard to put down. That reversal invites the reader to smile."),
    ],
)

K(
    "g6a_yu", "The Mystery of Life in the Universe", "阅读理解", 6, "上", 3, "reasoning",
    "Identify the conditions needed for life in this explanatory text and understand that there is still no conclusive evidence of life on Mars.",
    "yd_56",
    [
        ("What evidence does the text use to discuss whether life can exist?", "Conditions such as temperature, water, atmosphere, light, and heat", ["Who finishes memorizing a poem first", "A route through a palace from south to north", "How long a character's dialogue is"], "An explanatory text reasons from conditions, not from a story's plot or a sightseeing route."),
        ("Which object does the text focus on because its conditions are relatively close to Earth's?", "Mars", ["The Sun", "The Moon", "Polaris"], "Mercury and Venus are too hot, while more distant planets are too cold. The text focuses on Mars."),
        ("What does the text say about the results of Mars probes?", "No conclusive evidence of life has been found yet", ["Human-like creatures have already been found", "Mars is covered in forests", "The text does not mention Mars"], "The absence of evidence is not a definitive answer. Whether life exists beyond Earth remains a mystery."),
        ("What is a good way to read this kind of explanatory text?", "Identify the conditions and conclusions the author uses", ["Look only for the bravest character", "Memorize it as a myth", "Guess without considering the probe results"], "The conditions and probe results support the article's reasoning; its conclusion should follow from that evidence."),
    ],
)

K(
    "g6a_gong", "The Palace Museum", "阅读理解", 6, "上", 3, "reasoning",
    "Locate the Hall of Supreme Harmony along the north-south central axis and describe its function. Read with the purpose of tracing the palace buildings and route.",
    "yd_56",
    [
        ("What order does the text mainly use to describe the Forbidden City?", "A spatial route from south to north", ["A timeline from morning to evening", "Buildings ordered by construction cost", "Legends without a route"], "The text moves inward from Tiananmen, describing buildings one by one along the central axis. “The Founding Ceremony” uses chronological order."),
        ("What is the Hall of Supreme Harmony's role in the Forbidden City?", "It is the largest hall, on the central axis, and hosts major ceremonies", ["It is the smallest side gate", "It is outside the palace", "It is used only for storing grain"], "The Hall of Supreme Harmony, also known as the Golden Carriage Hall, hosted an emperor's enthronement and holiday ceremonies."),
        ("From south to north, what is the order of the three main halls?", "Hall of Supreme Harmony, Hall of Central Harmony, Hall of Preserving Harmony", ["Hall of Preserving Harmony, Hall of Central Harmony, Hall of Supreme Harmony", "Hall of Supreme Harmony, Hall of Preserving Harmony, Hall of Central Harmony", "Hall of Central Harmony, Hall of Supreme Harmony, Hall of Preserving Harmony"], "The order is Supreme, Central, then Preserving. Do not reverse it."),
        ("What lies at the northern end of the central axis?", "The Imperial Garden", ["Tiananmen", "Meridian Gate", "Hall of Supreme Harmony"], "The Imperial Garden lies beyond the inner court. Tiananmen and Meridian Gate are southern entrances."),
    ],
)

K(
    "g6a_mei", "Writing: ____ Makes Life Better", "习作基础", 6, "上", 3, "application",
    "Fill the blank with a topic such as reading, music, or exercise. Describe a specific way it changed an experience and explain your view.",
    "xz_56",
    [
        ("The title is “Reading Makes Life Better.” Which sentence expresses a personal view?", "After reading the biography, I realized I could write down the steps when I face a difficult problem.", ["The word “reading.”", "The book is thick.", "The library is on the second floor."], "Writing down the steps is a view shaped by reading. The book's thickness and the library's floor are not."),
        ("Which topic fits the blank and is easy to develop?", "Taking a walk", ["More", "Of", "Better"], "Taking a walk is a concrete topic. “More,” “of,” and “better” do not make a complete title."),
        ("How should you choose material for this essay?", "Choose an experience changed by the topic and explain what was different before and after", ["Write one sentence about every hobby", "Only write “Life is better now”", "Copy a text and present it as your experience"], "A before-and-after change shows how the topic affected your life. Vague claims and copied texts are not your experience."),
        ("Under the title “Music Makes Life Better,” which sentence is off topic?", "Our class had a mental-math test yesterday afternoon.", ["I am tense before playing piano, but my shoulders relax after one piece.", "During choir, I heard the singers beside me and realized I was off-key.", "I now think music can untangle the mess in my mind."], "The math test is unrelated to music. The piano, choir, and reflection all fit the topic."),
    ],
)

K(
    "g6a_xing", "Language Corner 3: Confusable Characters 慨, 概, and 溉", "识字写字", 6, "上", 3, "conceptual",
    "Distinguish 慨, 概, and 溉 by their radicals; do not write 慷慨 as 慷概. The memorization poem is Zhu Xi's “Reflections on Reading, No. 2,” not “Spring Day.” When reading explanatory texts, select material according to your purpose.",
    "sz_56",
    [
        ("Which character completes “慷__”?", "慨", ["概", "溉", "凯"], "慨 is the correct character in 慷慨 and has the heart radical. 凯 does not."),
        ("Which character completes “大__”?", "概", ["慨", "溉", "盖"], "概 appears in 大概 and 气概; it has the wood radical. Do not write 气慨."),
        ("Which character completes “灌__”?", "溉", ["慨", "概", "盖"], "溉 appears in 灌溉 and has the water radical. 盖 does not."),
        ("Which group is spelled correctly?", "慷慨、大概、灌溉", ["慷概、大概、灌溉", "慷慨、大慨、灌溉", "慷慨、大概、灌概"], "慨 has the heart radical, 概 the wood radical, and 溉 the water radical. These characters are not interchangeable."),
    ],
)

K(
    "g6a_qiao", "The Bridge", "阅读理解", 6, "上", 4, "reasoning",
    "Understand how the old village secretary sent the villagers across the bridge first during the flood and stayed behind with his son.",
    "yd_56",
    [
        ("Who did the old secretary send across the bridge first?", "The villagers", ["Himself", "Only his son", "No one"], "He gave the villagers a chance to survive and directed them across in order."),
        ("What did the old secretary do when a young man tried to push ahead?", "He pulled him out and sent him to the back of the line", ["He let him cross first", "He ran across first himself", "He dismantled the bridge"], "The young man was his son. The secretary let no one cut the line, not even his own child."),
        ("What happened to the secretary and his son in the end?", "They were swept away after the villagers crossed", ["They were the first to reach the far bank", "They stayed home", "They swam to the top of a mountain"], "After the villagers had crossed, the wooden bridge collapsed and the two were carried away by the flood."),
        ("Why does the ending show an old woman coming to mourn the two men?", "The secretary gave others a chance to live, sacrificing himself and his son", ["The woman went to the wrong bridge", "The flood was not dangerous", "His son should not have come"], "The woman is mourning her husband and son. Their relationship is revealed only at the end."),
    ],
)

K(
    "g6a_qiong", "The Poor", "阅读理解", 6, "上", 4, "reasoning",
    "Understand how Sanna brings home Simon's children and how the fisherman agrees that they will raise them together.",
    "yd_56",
    [
        ("What did Sanna see when she opened Simon's door?", "Simon had died, but the two children were still alive", ["Simon had come to visit with the children", "The fisherman had already taken the children", "No one was in the house"], "Simon was dead, but the children were still beside her. The story was written by Leo Tolstoy."),
        ("What did Sanna do with the children?", "She brought them home", ["She took them somewhere else", "She left them alone in Simon's house", "She handed them to a passerby"], "She could not bear to leave the children beside their dead mother."),
        ("What did the fisherman say after he found out?", "Bring the children here first; we will get through this together", ["Take them back", "This has nothing to do with us", "Hide them so no one finds out"], "The fisherman says to bring the children over. They will struggle through poverty and raise them together."),
        ("What does the story mainly show about the couple?", "They are poor but kindhearted", ["They want to give the children away", "They refuse to help their neighbor", "They care only about their fishing nets"], "Although they are already poor, they take in their neighbor's children."),
    ],
)

K(
    "g6a_gou", "The Golden Fishhook", "阅读理解", 6, "上", 4, "reasoning",
    "Understand how the old squad leader saved the fish for three young soldiers on the grassland but did not make it out himself.",
    "yd_56",
    [
        ("What mission was the old squad leader given?", "To lead three sick young soldiers out of the grassland", ["Direct villagers across a bridge", "Bring a neighbor's children home", "Hide on a hillside"], "The political instructor entrusted the soldiers to him. The bridge and the children belong to other stories."),
        ("When the squad leader caught fish, what did he do for himself?", "He gave the fish to the soldiers and chewed grass roots and fish bones", ["He ate first and shared the leftovers", "He returned the fish to the water", "He traded a fish for clothes"], "He endured hunger so the soldiers could eat, just as Sanna and the village secretary put others' lives first."),
        ("What happened to the squad leader as the group left the grassland?", "He had died and could not leave with the soldiers", ["He was the first to escape", "He returned to his village", "He gave the fishhook to the enemy"], "The soldiers made it out, but the squad leader fell at the edge of the grassland."),
        ("What do the words “The Golden Fishhook” represent?", "The hook shines, but more importantly it recalls the squad leader's duty, worth more than gold", ["The hook is made of gold", "The fish are a golden species", "Gold is buried in the grassland"], "The author keeps the hook to remember the squad leader, not to show its metal."),
    ],
)

K(
    "g6a_bi", "Writing: A Story from the Pen", "习作基础", 6, "上", 4, "application",
    "Create a story with a beginning, a development, and an ending. Let the characters act in a concrete setting; “Once there was a person” is not yet a story.",
    "xz_56",
    [
        ("What does a story need at minimum?", "A beginning, something that happens, and an ending", ["A title only", "A description of nice weather", "A copied vocabulary list"], "A story connects its beginning, development, and ending. A title or vocabulary list has no plot."),
        ("Which sentence places a character in a setting?", "Rain struck the bridge planks as he pulled the smallest child behind him.", ["Once there was a person.", "The story was moving.", "Four words: “The pen tells a story.”"], "The rain, bridge planks, and protective movement establish the setting and action. Saying only that it is moving does not introduce a character."),
        ("What is a good approach to a fictional story?", "Use imagination, but make the characters' actions follow from what happened earlier", ["Switch to a different character without warning", "Leave out the ending", "Copy the text line by line"], "Imagination still needs continuity. Copying a text is not inventing your own story."),
        ("Which passage tells a story?", "After the lights went out, my sister thought someone was in the room, but the cat had knocked over a cup.", ["The lights.", "Sister, cat, cup.", "Today I will tell a story. The end."], "The lights go out, the sister misunderstands, and the cat knocks over a cup: one connected event. A list or empty announcement has no plot."),
    ],
)

K(
    "g6a_ci", "Language Corner 4: Interpreting Words in Context", "词语", 6, "上", 4, "conceptual",
    "Use context to infer what a word means in a sentence instead of relying only on a dictionary definition. When asking someone to support you, explain why and say what you hope they will do.",
    "cy_56",
    [
        ("In “The bridge trembled in the flood,” what does the word “发抖” mean?", "The flood battered the bridge until it seemed unsteady", ["The bridge felt cold", "The bridge was talking", "The bridge had already collapsed"], "The bridge cannot literally feel cold. “发抖” describes its shaking in the flood."),
        ("The fisherman says “一起熬.” What does “熬” mean here?", "To endure hardship and raise the children", ["To boil water", "To stay awake all night", "To cook fish"], "Given their poverty and the added responsibility of raising children, “熬” means to persevere through hardship."),
        ("Which sentence uses a word in a figurative sense?", "It felt as if something had pierced his heart.", ["A needle pierced his hand.", "He drew a heart on the paper.", "“Pierce” is a vocabulary word."], "A pierced heart describes emotional pain, not a physical injury."),
        ("What should you do first when inferring a word's meaning?", "Read the surrounding sentences, then decide what it means here", ["Always choose the first dictionary definition", "Replace the word with its opposite", "Decide without reading the sentence"], "The same word can have different meanings in different contexts."),
    ],
)

K(
    "g6a_xiao", "Happy Reading: Laughter, Tears, Experience, and Growth", "阅读理解", 6, "上", 4, "conceptual",
    "When reading about a character's growth, note the experiences that make you laugh or feel sad and track how the character changes. This is different from the Grade 5 lower-volume reading of classical novels.",
    "yd_56",
    [
        ("What should you pay most attention to in this reading?", "What makes the characters laugh or cry and how they grow afterward", ["Only the author's nationality", "Only the cover color", "Copying the contents page as vocabulary"], "The title's four ideas—laughter, tears, experience, and growth—guide the reading."),
        ("What can you do after reading a sad passage?", "Note what happened and what choice the character made", ["Skip straight to the last page", "Cross out the passage", "Change it into another story"], "A sad episode is often a turning point in a character's growth. Skipping it hides that change."),
        ("Which reading approach best fits this activity?", "After reading an experience, explain in your own words how the character changed", ["Read only the summary", "Memorize the book's price", "Switch halfway through to an unrelated dictionary"], "Explaining the change shows that you have followed the character's growth. A summary or price is too superficial."),
        ("How is this different from “Reading Classical Novels”?", "This activity focuses on how experiences help a character grow, not on summarizing a chapter", ["Both activities read the same chapter of the same book", "Stories are not allowed this time", "Classical novels have no characters"], "The Grade 5 activity focused on chapters of classical novels; this one focuses on the laughter and tears in growth stories."),
    ],
)

K(
    "g6a_deng", "The Light", "阅读理解", 6, "上", 5, "reasoning",
    "Understand Wang Yuanjian's account of Deputy Battalion Commander Hao: he longs for the life shown in a picture of children studying by electric light, then lights a book to guide the following troops and dies in battle.",
    "yd_56",
    [
        ("What was in the picture Deputy Battalion Commander Hao looked at before the battle?", "Children studying under electric lights", ["A wooden bridge in a flood", "A ceremony at Tiananmen", "A golden fishhook"], "He pointed to the picture and said he wanted children to study under lights like those in the future."),
        ("Why did he set his book alight during the battle?", "To show the following troops where the breakthrough was", ["To burn it before a homework check", "To heat food", "To signal surrender to the enemy"], "The flame exposed his position, but it also showed the following troops the way."),
        ("Where does the text begin its reflection on light?", "The lights in Tiananmen Square", ["A fire on Langya Mountain", "A campfire on the grassland", "Palace lanterns in the Forbidden City"], "The lights in the square lead into a memory of Deputy Battalion Commander Hao. Do not confuse this with the founding ceremony."),
        ("What is the central idea of the text?", "A revolutionary gave his life so future generations could live well under the light", ["Who invented the electric light", "How many lights Tiananmen has", "A training exercise with no casualties"], "The real lights, the lights in the picture, and the battlefield flame all point to this idea."),
    ],
)

K(
    "g6a_pan", "Longing", "阅读理解", 6, "上", 5, "reasoning",
    "Understand Tie Ning's story about a child longing to wear a new raincoat: after receiving it, the child waits for rain, hopes to go out to buy soy sauce, and finally gets the chance.",
    "yd_56",
    [
        ("What is the child longing for?", "To wear the new raincoat bought by the child's mother and walk in the rain", ["Deputy Battalion Commander Hao seeing electric lights", "Selling the raincoat for a good price", "Having no school tomorrow"], "The story centers on the new raincoat. Electric light is the focus of “The Light.”"),
        ("When it rains, what does the mother tell the child to do?", "Stay home and not go out in the new raincoat", ["Run around in the rain three times", "Give the raincoat to a classmate", "Go see the lights at Tiananmen"], "The more the mother says not to go out, the more specific the child's longing becomes."),
        ("What errand does the child hope will be a chance to wear the raincoat?", "Buying soy sauce for the family", ["Attending the founding ceremony", "Fishing on the grassland", "Visiting the teacher's office"], "Buying soy sauce gives the child a reason to go outside. The other options belong to different texts."),
        ("What do this story and “The Light” have in common?", "Each stays focused on one central idea", ["Both describe the 1949 ceremony", "Both are explanatory texts", "Both are about the same raincoat"], "One centers on light and sacrifice, the other on longing. Their subjects differ, but both are tightly focused."),
    ],
)

K(
    "g6a_xie", "Writing Around a Central Idea", "习作基础", 6, "上", 5, "application",
    "Choose a central idea first, then select material that supports it and develop the most relevant part in detail. “Dad's Plan” and “The Little Station” are not separate topics. This unit has no language corner.",
    "xz_56",
    [
        ("The central idea is “Our class held on during the tug-of-war.” Which detail deserves the most space?", "In the last few seconds, several students leaned back together, and the rope finally moved our way.", ["I ate an egg for breakfast.", "The classroom has four windows.", "The words “tug-of-war.”"], "Leaning back and moving the rope show that the class held on. The egg and windows are unrelated."),
        ("What does “Longing” demonstrate about writing?", "One idea can run through the whole piece, expressed through several small events", ["Give every paragraph an unrelated focus", "Write only the title", "Mention the central idea once and never return to it"], "Receiving the raincoat, waiting for rain, and hoping to buy soy sauce all develop the idea of longing."),
        ("If several pieces of material fit, how should you handle detail?", "Develop the part that best supports the central idea; summarize the rest", ["Give every event the same amount of space", "Keep only an unrelated event", "Delete the central idea so the material feels focused"], "Detailed writing highlights the main idea; equal space is not the goal. Without a central idea, the piece wanders."),
        ("Which paragraph stays focused on one central idea?", "To show “I learned to repair my own supplies,” I chose the wrong part, installed it backward, then took it apart and tried again.", ["First I repaired supplies, then wrote about yesterday's cartoon, and finally described my grandmother's cooking.", "Repair.", "Supplies, cartoons, food."], "Choosing the wrong part, installing it backward, and trying again all support the idea of learning to repair something."),
    ],
)

K(
    "g6a_di", "Only One Earth", "阅读理解", 6, "上", 6, "reasoning",
    "Understand the key argument: Earth is beautiful and small, its resources are limited, and humanity cannot yet move to another planet, so we must protect this one carefully.",
    "yd_56",
    [
        ("What is Earth compared to in the text?", "Humanity's mother and the cradle of life", ["A replaceable new ship", "An inexhaustible warehouse", "A moon of Mars"], "Both images show that humanity cannot live without Earth."),
        ("What does the text say about natural resources?", "They are limited and will run out if used carelessly", ["Earth's minerals will never run out", "Damage does not matter because people can move away", "Only water is limited"], "Nonrenewable resources are especially vulnerable to overuse, which is why the text calls for protection."),
        ("Could people move to another planet if Earth were destroyed?", "For now, we cannot rely on moving elsewhere", ["The text says Mars is already habitable", "The Moon has ready-made cities", "The text does not discuss this"], "The text says we cannot count on moving to another planet. Whether Mars has life is a different question in “The Mystery of Life in the Universe.”"),
        ("What main idea should readers remember?", "There is only one Earth, and we must protect it carefully", ["Earth is small, so it does not need protection", "Scientists will build a second Earth", "Resource issues do not concern children"], "The title states the main idea. Earth's small size, limited resources, and lack of an alternative all support it."),
    ],
)

K(
    "g6a_qing", "Green Hills Never Grow Old", "阅读理解", 6, "上", 6, "reasoning",
    "Understand how an old man spent more than a decade planting trees in northwest Shanxi and left a green landscape beyond his window.",
    "yd_56",
    [
        ("Where did the old man plant trees for years?", "In a mountain ravine in northwest Shanxi", ["At Tiananmen in Beijing", "On the grasslands of Inner Mongolia", "In the Imperial Garden"], "He planted trees in windy, sandy northwest Shanxi. Do not confuse the setting with the grasslands or the palace garden."),
        ("What does the green view beyond the window show?", "The old man's persistence over many years has become a forest", ["The trees grew in one day", "The village was already a forest, so planting was unnecessary", "The trees have nothing to do with the old man"], "The landscape outside the window confirms what he accomplished."),
        ("What does “Green hills never grow old” mean in the text?", "The man will age, but the green landscape and his spirit will endure", ["The hills can never change", "Planting trees is useless", "The hills will not let the man leave"], "The line closes the text: the man leaves both a green landscape and a spirit of environmental stewardship."),
        ("How is this text different from “Only One Earth”?", "One tells how an individual planted trees; the other explains why the whole planet must be protected", ["Both describe the same old man", "One says the environment need not be protected", "The other is a poem"], "One presents a specific person's work; the other develops an explanatory argument. Both are in the same unit but are different texts."),
    ],
)

K(
    "g6a_hei", "Sanhei and the Land", "阅读理解", 6, "上", 6, "reasoning",
    "Understand Su Jinsan's poem about Sanhei, a farmer who has regained his land and longs to become a seed resting in the soil.",
    "yd_56",
    [
        ("Why is Sanhei so happy?", "The land has returned to the farmers", ["He grew a forest in northwest Shanxi", "He discovered that Earth can be moved", "He received a new raincoat"], "The poem is about land being returned to its people. Tree planting is the subject of “Green Hills Never Grow Old”; the raincoat is from “Longing.”"),
        ("What does Sanhei wish he could become?", "A seed resting in the soil", ["A ship sailing away from the land", "A lamp in front of Tiananmen", "A stone that cannot burn"], "Becoming a seed expresses his desire to be close to the land."),
        ("In “活像旱天的鹅，一见了水就连头带尾巴钻进水里,” who is compared to the goose?", "Farmers rushing toward the land they have regained", ["Clouds in the sky", "A boat in the river", "A teacher in class"], "The image of a goose rushing toward water after a drought conveys the farmers' eagerness to return to the land."),
        ("What is the main idea of the poem?", "The farmers' deep and sincere love for the land", ["An explanation of geese's habits", "How seeds sprout", "A call for everyone to leave the countryside"], "Plowing, smelling the soil, and wishing to become a seed all express that love."),
    ],
)

K(
    "g6a_sha", "“Washing Sand” (No. 1)", "古诗文积累", 6, "上", 6, "conceptual",
    "Memorize Liu Yuxi's “Washing Sand” (No. 1), especially the winding Yellow River and the home of the Cowherd and Weaver Girl. Do not mix it up with “Spring in the South.”",
    "gs_56",
    [
        ("Which line follows “九曲黄河万里沙”?", "浪淘风簸自天涯", ["如今直上银河去", "千里莺啼绿映红", "浪淘风簸到天涯"], "The Yellow River carries sand through great waves from a faraway source. The line about reaching the Milky Way comes third."),
        ("Which line follows “如今直上银河去”?", "同到牵牛织女家", ["同到牛郎织女家", "一起到牵牛织女家", "两山排闼送青来"], "The poet imagines the river reaching the Milky Way and meeting the Cowherd and Weaver Girl. The poem says “牵牛,” not “牛郎”; the line about opening a door belongs to another poem."),
        ("Who wrote “Washing Sand” (No. 1)?", "Liu Yuxi", ["Du Mu", "Wang Anshi", "Su Shi"], "Liu Yuxi wrote this poem. Du Mu wrote “Spring in the South.”"),
        ("What impression does the Yellow River create in the poem?", "It is winding and powerful, and the poem imagines it rushing toward the Milky Way", ["It is quiet like a flower bed in a courtyard", "It is delicate like misty rain in the south", "The poem describes only one drop of water"], "The winding river, thousands of miles of sand, and distant source create a vast scene. The courtyard and misty rain belong to other poems."),
    ],
)

K(
    "g6a_chun", "“Spring in the South”", "古诗文积累", 6, "上", 6, "conceptual",
    "Memorize Du Mu's “Spring in the South,” especially the singing orioles and the four hundred and eighty temples. Do not mix it up with “Washing Sand.”",
    "gs_56",
    [
        ("Which line follows “千里莺啼绿映红”?", "水村山郭酒旗风", ["南朝四百八十寺", "九曲黄河万里沙", "水村山郭酒旗中"], "After the orioles, green trees, and red flowers come waterside villages, mountain towns, and wine flags in the wind. The temples appear in the third line."),
        ("Which line follows “南朝四百八十寺”?", "多少楼台烟雨中", ["多少楼台风雨中", "多少楼阁烟雨中", "两山排闼送青来"], "Four hundred and eighty is a large number, not an exact count. The towers are veiled in misty rain. The poem says “烟雨,” not “风雨”; the line about opening a door is from another poem."),
        ("Who wrote “Spring in the South”?", "Du Mu", ["Liu Yuxi", "Wang Anshi", "Xin Qiji"], "Du Mu wrote this poem; Liu Yuxi wrote “Washing Sand” (No. 1)."),
        ("Which line is not from “Spring in the South”?", "同到牵牛织女家", ["千里莺啼绿映红", "水村山郭酒旗风", "多少楼台烟雨中"], "“同到牵牛织女家” is the last line of “Washing Sand” (No. 1)."),
    ],
)

K(
    "g6a_shu", "“Written on Mr. Huyin's Wall”", "古诗文积累", 6, "上", 6, "conceptual",
    "Memorize Wang Anshi's “Written on Mr. Huyin's Wall,” especially the water protecting the fields and the mountains opening the door. Do not confuse it with “Spring in the South.”",
    "gs_56",
    [
        ("What does “茅檐长扫净无苔” describe?", "The area under the eaves is swept so often that it stays free of moss", ["The Yellow River rushing from the horizon", "Temples hidden in misty rain", "A thatched house washed away by a storm"], "The line shows how carefully the owner tends the courtyard. The river and misty rain belong to other poems."),
        ("Which line follows “一水护田将绿绕”?", "两山排闼送青来", ["花木成畦手自栽", "多少楼台烟雨中", "两山排闼送春来"], "Green water circles the fields, and two mountains seem to open the door and send in their green. The line about planting flowers and trees by hand comes earlier."),
        ("Who wrote this poem?", "Wang Anshi", ["Du Mu", "Liu Yuxi", "Meng Haoran"], "Wang Anshi wrote the poem on Mr. Huyin's wall. Du Mu wrote “Spring in the South,” and Liu Yuxi wrote “Washing Sand.”"),
        ("What does “排闼” mean in this line?", "To push open a door", ["To dig away a mountain", "To enclose a field", "To hang a wine flag"], "闼 means a door. The mountains seem to push it open and send their green inside."),
    ],
)

K(
    "g6a_yi", "Writing: An Advocacy Letter", "习作基础", 6, "上", 6, "application",
    "An advocacy letter needs an addressee, a reason, one or two specific actions, a signature, and a date. A bare request to protect the environment is not enough.",
    "xz_56",
    [
        ("What usually comes first in an advocacy letter?", "A greeting that makes clear who you are addressing", ["A drawing", "A copied poem", "Your student number, and nothing else"], "The greeting changes depending on whether you are addressing classmates or neighbors. Without an audience, readers will not know who the proposal is for."),
        ("Which is a specific proposal?", "Starting this week, sort classroom paper into two boxes every afternoon.", ["Please protect the environment.", "The environment is important.", "We should care for Earth."], "Two boxes and an afternoon routine are actionable. A slogan alone does not tell readers what to do first."),
        ("Why should the main text explain the reason for the proposal?", "Readers are more likely to act when they understand how the issue affects them", ["Reasons make the letter worse", "Advocacy letters must not give reasons", "The reason must be written as a poem"], "An idea such as the one in “Only One Earth” can support the proposal, but it should lead to specific actions."),
        ("What must be included at the end of an advocacy letter?", "The writer's name and the date", ["A copy of the text", "A map", "A crossed-out title"], "A signature and date show who made the proposal and when. Copying a text cannot replace a signature."),
    ],
)

# Keep these Chinese conjunction patterns: they are the assessed grammar content in this topic.
K(
    "g6a_ju", "Language Corner 6: Paired Conjunctions", "句子", 6, "上", 6, "procedural",
    "Unit 5 is a writing unit with no language corner, so paired conjunctions are practiced here. Match 不但 with 而且, 只要 with 就, and 只有 with 才. In a discussion, state your view clearly and listen to the other person's reasons.",
    "jz_56",
    [
        ("Which pair completes the Chinese sentence meaning “He not only repaired the desk but also put the tools away”?", "不但……而且……", ["不但……就……", "只要……而且……", "虽然……而且……"], "Both actions happened, and the second adds another point, so use 不但……而且……."),
        ("Which pair completes the Chinese sentence meaning “As long as you finish reading the problem, you will not misread the number”?", "只要……就……", ["只有……就……", "不但……才……", "因为……就……"], "Finishing the problem is a sufficient condition, so use 只要……就……."),
        ("Which pair completes the Chinese sentence meaning “Only if the writing is clear will others understand”?", "只有……才……", ["只要……才……", "只有……就……", "不但……才……"], "Clear writing is necessary, so use 只有……才……. 只要 does not pair with 才 here."),
        ("Which sentence expresses the correct pairing?", "只要……就……: Leave on time, and you will not be late.", ["只要……才……: Leave on time, and you will not be late.", "不但……就……: Leave on time, and you will not be late.", "只有……就……: Leave on time, and you will not be late."], "只要 pairs with 就, while 只有 pairs with 才. The other combinations are incorrect."),
    ],
)

K(
    "g6a_er", "Classical Text: Two Children Debate the Sun", "阅读理解", 6, "上", 7, "reasoning",
    "Understand two children debating whether the Sun is closer in the morning or at noon, and why Confucius cannot decide who is right. Do not confuse this with “Cao Chong Weighs an Elephant.”",
    "yd_wenyan",
    [
        ("What are the two children debating?", "When the Sun is closer to people and when it is farther away", ["How much an elephant weighs", "Whose cart cover is larger", "Whether Confucius is going to school"], "One child says the Sun is closer in the morning; the other says it is closer at noon. The elephant story is separate."),
        ("The child who says the Sun looks as large as a cart cover in the morning and as small as a bowl at noon thinks it is closer when?", "In the morning, because it looks larger", ["At noon, because it looks smaller", "At night, because it cannot be seen", "It is equally close at both times"], "That child uses apparent size as evidence. The other child judges by warmth and coolness instead."),
        ("What does Confucius conclude after listening?", "He cannot decide which child is right", ["The child who says morning is closer wins", "The child who says noon is closer wins", "He sends both children away"], "Confucius cannot decide; he does not announce a winner."),
        ("Which work is this passage from?", "Liezi", ["Records of the Three Kingdoms", "Mencius", "Analects"], "“Two Children Debate the Sun” is selected from “Questions of Tang” in Liezi. “Cao Chong Weighs an Elephant” is from the Records of the Three Kingdoms."),
    ],
)

K(
    "g6a_xiang", "Classical Text: Cao Chong Weighs an Elephant", "阅读理解", 6, "上", 7, "reasoning",
    "Understand Cao Chong's method: put the elephant on a boat, mark the waterline, then weigh another load until the boat reaches the same line. Do not confuse this with “Two Children Debate the Sun.”",
    "yd_wenyan",
    [
        ("What did Cao Cao want to know?", "How much the elephant weighed", ["Whether the Sun is closer in the morning or at noon", "How many people were on the boat", "What color the stones were"], "The elephant was too large to weigh directly. The question about the Sun belongs to the previous story."),
        ("What was the officials' first reaction?", "No one could think of a solution", ["They immediately slaughtered the elephant to weigh it", "They had already weighed it", "They told Cao Chong not to speak"], "The officials could not devise a method; Cao Chong was the one who proposed one."),
        ("What is the key step in Cao Chong's method?", "Mark the waterline with the elephant aboard, then add weighable objects until the boat reaches the same line", ["Measure the elephant's height with a rope", "Make the elephant stand on a scale", "Weigh the river water"], "The same waterline indicates the same weight. Height alone cannot tell the elephant's weight."),
        ("What does the story show?", "A young person can think of a solution others have missed", ["Elephants are easy to weigh", "Cao Cao disliked the method", "Objects must be weighed by comparing the Sun's distance"], "Cao Cao was delighted and put the method into practice. The idea was used, not rejected."),
    ],
)

K(
    "g6a_biao", "The Living Creature Inside the Watch", "阅读理解", 6, "上", 7, "reasoning",
    "Understand Feng Zhi's childhood memory: he thinks anything that makes a sound by itself is alive, and his father tells him there is a small scorpion inside a pocket watch.",
    "yd_56",
    [
        ("As a child, what did “I” think could make a sound by itself?", "A living creature", ["Any kind of stone", "Only the wind", "Only people speaking"], "Birds, dogs, and cicadas all make sounds, and they are alive. So when the watch ticked, he thought it contained a creature."),
        ("What did the child see when his father opened the watch?", "Gears and a small part that kept swinging", ["A real bird", "A seed", "A map"], "He saw tiny blue and red jewels, gears, and a part that swung back and forth. His father called it a scorpion's tail."),
        ("What did the father say the swinging part was?", "A small scorpion's tail that would sting if it moved", ["A string that could be pulled out and played with", "Water inside the watch", "A fishhook"], "His father used this explanation to stop him from reaching inside, and the child truly believed it."),
        ("What did the child later tell people about the watch?", "That there was a little scorpion inside his father's watch", ["He never mentioned the watch again", "There was nothing inside it", "He took it apart and shared the pieces"], "He repeated what he understood. The story combines curiosity with misunderstanding."),
    ],
)

K(
    "g6a_qu", "How Interesting They Were!", "阅读理解", 6, "上", 7, "reasoning",
    "Understand Isaac Asimov's science fiction: in 2155, Margie studies at home with a mechanical teacher but longs for the old days when children went to school together.",
    "yd_56",
    [
        ("In what year does the story take place?", "2155", ["1949", "No year is given", "Confucius's time"], "The opening gives the date as May 17, 2155, placing the story in an imagined future."),
        ("What is Margie's teacher like?", "A mechanical teacher at home, where she studies alone", ["A human teacher in a classroom", "A watch in her father's pocket", "Two children debating the Sun"], "The machine is at home. Human teachers and many classmates belong to the past she reads about in an old book."),
        ("Why does Margie find “how interesting they were”?", "Children in the past went to school together, laughed together, and had human teachers", ["There were no books in the past, so life was easy", "Every day was a holiday", "Teachers in the past were scorpions"], "Margie lacks companions. The lively school in the book makes her both envious and sad."),
        ("Both this story and “The Living Creature Inside the Watch” involve curiosity. How are they different?", "This one imagines future schools; the other shows a child misunderstanding a watch", ["They are the same story", "This one says machines are better than classmates", "The other takes place in 2155"], "One looks from the future toward the past; the other recalls a childhood misunderstanding. They are separate texts."),
    ],
)

K(
    "g6a_chi", "Writing: Give Science the Wings of Imagination", "习作基础", 6, "上", 7, "application",
    "Begin with a curious question and imagine boldly, but explain the steps clearly so readers can follow.",
    "xz_56",
    [
        ("Which title best fits this writing task?", "What if my schoolbag could return a forgotten pen to the classroom by itself?", ["Today's mental-math practice", "Copying the Five Elements and Five Grains", "My home address"], "A schoolbag delivering a pen is a science-fiction idea. Arithmetic, copying, and an address leave no room for imagination."),
        ("What does it mean to make an imagined event clear?", "Readers can follow how it happens, not just see the final result", ["Longer sentences are always better", "Causes do not need explanation", "Paste in the original text"], "Explain the steps. If you only say “Then it flew,” the middle is missing."),
        ("Which sentence develops the imagined event concretely?", "The pen pointed toward the empty slot, rolled into its case, and the lid clicked shut.", ["My invention is scientific.", "The wings of science.", "The future is wonderful."], "The empty slot, rolling pen, and closing lid let readers picture exactly what it does."),
        ("How should you use this unit's texts as models?", "Borrow their curiosity, but create your own idea instead of retelling their stories", ["Copy the original lines from “Cao Chong Weighs an Elephant”", "Do not imagine; write only real events", "Let the imagined events contradict each other"], "The elephant, the watch, and the future school can spark questions. The writing should develop your own idea."),
    ],
)

K(
    "g6a_xu", "Language Corner 7: Classical Particles 之, 其, and 而", "阅读理解", 6, "上", 7, "reasoning",
    "Distinguish 之, 其, and 而 in sentences from “Two Children Debate the Sun” and “Cao Chong Weighs an Elephant.” The memorization section also covers the Five Elements, Five Grains, Five Tones, and Five Colors; here, focus on the particles.",
    "yd_wenyan",
    [
        ("In “问其故,” what does “其” refer to?", "The reason the children made those claims", ["The elephant's weight", "Confucius's name", "A small scorpion"], "Confucius asks why one child says the Sun is closer in the morning and the other says it is closer at noon. Here, 其 refers to the reason."),
        ("What role does “而” play in “我以日始出时去人近，而日中时远也”?", "It marks a contrast between the claims that the Sun is closer in the morning and at noon", ["It introduces a question", "It means “of”", "It means “yesterday”"], "The claims about near and far oppose each other, so 而 means “but” here."),
        ("What does “其” mean in “欲知其斤重”?", "Its, referring to the elephant's weight", ["One of the people", "If", "Already"], "Cao Cao wants to know the elephant's weight. Here, 其 means “its.”"),
        ("What role does “而” play in “置象大船之上，而刻其水痕所至”?", "It connects two consecutive actions: placing the elephant on the boat and marking the waterline", ["It marks a contrast", "It says the elephant is heavy", "It says Confucius cannot decide"], "First the elephant is put on the boat, then the waterline is marked. 而 is not contrastive here."),
    ],
)

K(
    "g6a_run", "Young Runtu", "阅读理解", 6, "上", 8, "reasoning",
    "Understand Lu Xun's memory of Runtu in “Hometown”: a boy with a silver neck ring who holds a steel fork and tells stories about trapping birds in snow and guarding melons.",
    "yd_56",
    [
        ("From whose work is “Young Runtu” taken?", "Lu Xun's “Hometown”", ["Zhou Ye's story about her uncle", "Zang Kejia's “Some People”", "Lao She's “The Grassland”"], "The narrator remembers a childhood friend named Runtu. Zhou Ye wrote the text about her uncle."),
        ("What did Runtu wear around his neck when the narrator first met him in the kitchen?", "A silver neck ring", ["A red scarf", "A string of shells", "His father's pocket watch"], "He has a round, purplish face, a small felt hat, and a silver neck ring. The shells come from a later story about the seashore."),
        ("After setting the bamboo tray for snow bird-trapping, what should you do?", "Wait at a distance for birds to land on the grain, then pull the string", ["Stand under the tray immediately", "Catch each bird and release it", "Use the steel fork to stab a bird"], "Pulling the string drops the tray. The steel fork is used when guarding melons."),
        ("What is the name Runtu associated with?", "He was born in a leap month, and the Five Elements lacked Earth", ["He lived in Runtu Village", "He liked the color ochre", "It was a nickname given by his teacher"], "The text explains that the Five Elements lacked Earth, so he was named Runtu."),
    ],
)

K(
    "g6a_hao", "A Good Story", "阅读理解", 6, "上", 8, "reasoning",
    "Understand Lu Xun's dream: on a gloomy night, the dream is beautiful, graceful, and interesting, and he remembers it after waking.",
    "yd_56",
    [
        ("Who wrote “A Good Story”?", "Lu Xun", ["Zhou Ye", "Zang Kejia", "Feng Zhi"], "This prose poem was written by Lu Xun. Zhou Ye wrote about her uncle, and Zang Kejia wrote “Some People.”"),
        ("Where does the good story appear?", "In a dream on a gloomy night", ["In Young Runtu's melon field", "At the ceremony in Tiananmen Square", "Inside a pocket watch"], "The real setting is a gloomy night; the good story is a dream scene."),
        ("Which three words describe the dream's scenery?", "Beautiful, graceful, and interesting", ["Dangerous, cold, and hungry", "Angry, silent, and explosive", "Fresh, bright, and boundless"], "Beautiful, graceful, and interesting are recurring qualities in the text. Fresh and bright describe “The Grassland.”"),
        ("What happens after the author wakes up?", "The dream has ended, but he still remembers the good story", ["He forgets the dream completely", "He walks into the mountain road from the dream", "He stops writing"], "He returns to the gloomy night, but the story remains in his memory."),
    ],
)

K(
    "g6a_bofu", "My Uncle Lu Xun", "阅读理解", 6, "上", 8, "reasoning",
    "Understand Zhou Ye's memories of her uncle: he quizzes her about “Water Margin,” talks about “碰壁,” helps a rickshaw puller, and cares for the housekeeper.",
    "yd_56",
    [
        ("Who wrote the text, and who was her uncle?", "Zhou Ye wrote it about her uncle, Lu Xun", ["Lu Xun wrote it about Runtu", "Zang Kejia wrote it about Zhou Ye", "Lao She wrote it about Lu Xun"], "A niece recalls her uncle. Do not mistake the author for Lu Xun."),
        ("Why could the narrator not answer when they discussed “Water Margin”?", "She could not remember many characters and was stumped by her uncle's questions", ["Her uncle would not let her read", "“Water Margin” has no characters", "She had lent the book to Runtu"], "Her face flushed as her uncle encouraged her to remember what she read."),
        ("In “The whole world is dark; isn't it easy to run into a wall?” what does “碰壁” really mean?", "People face obstacles in a dark, unjust society", ["His nose literally hit a wall", "The room has no lights", "He is talking about Runtu hunting a wild animal"], "“碰壁” is a metaphor. The children take it literally as bumping his nose, while adults understand the deeper meaning."),
        ("What do the rickshaw puller and the housekeeper's stories show about the uncle?", "He thinks less about himself and more about others", ["He dislikes talking to people", "He cares only about his books", "He does not want visitors"], "The housekeeper's words make this clear. It echoes the poem “俯首甘为孺子牛.”"),
    ],
)

K(
    "g6a_you", "Some People", "阅读理解", 6, "上", 8, "reasoning",
    "Understand Zang Kejia's poem commemorating Lu Xun: some people remain alive after death, while others are dead even while living.",
    "yd_56",
    [
        ("Who wrote “Some People,” and whom does it commemorate?", "Zang Kejia commemorates Lu Xun", ["Lu Xun commemorates Runtu", "Zhou Ye commemorates the rickshaw puller", "Lao She commemorates the grassland"], "The subtitle says the poem is written in memory of Lu Xun. Lu Xun is not its author."),
        ("What kind of person is meant by “有的人死了，他还活着”?", "Someone whose spirit remains in the people's hearts after death", ["Someone who can return from the dead", "Someone whose name is carved in stone and therefore lives forever", "Anyone who is alive"], "To “live” here means to be remembered by the people. The poem says a name carved in stone can decay before a person's body."),
        ("Which action does the poem praise?", "Bowing low to serve the people", ["Riding on the people's backs and proclaiming one's greatness", "Carving one's name in stone to show off", "Keeping others from living while one is alive"], "Those who serve the people are held in high regard; those who dominate them are brought down."),
        ("How do you read this poem alongside “My Uncle Lu Xun”?", "The poem gives an overall judgment; the prose shows Lu Xun through specific events and conversations", ["Both describe the same cliff jump", "The poem is a classical prose text", "Neither mentions Lu Xun"], "One is a poem and the other is a niece's memoir. They are different texts in the same unit."),
    ],
)

K(
    "g6a_jia", "Writing: Passing Down Good Family Values", "习作基础", 6, "上", 8, "application",
    "Use one or two real family experiences to show a family value. Saying only “My family has good values” does not show what they are.",
    "xz_56",
    [
        ("Which sentence shows a family value rather than just praising the family?", "Grandpa promised to fix a neighbor's stool by Friday and stayed up Thursday night repairing its leg.", ["My family has good values.", "The words “family values.”", "We are one family."], "Repairing the stool on Thursday shows that Grandpa keeps his word. Saying “good” without an example tells readers nothing."),
        ("How should you choose material for writing about family values?", "Choose a specific event that shows how the family usually acts", ["Write one sentence about every relative", "Say how many rooms the house has", "Copy a Lu Xun poem as if it were a family event"], "One clearly described event can show a family value. The number of rooms and a copied poem do not describe your family's actions."),
        ("Which passage shows a value being passed down rather than simply praised?", "Dad taught me, “Return other people's books first.” On Friday, I put the book I had borrowed on my classmate's desk.", ["My dad is a good person.", "Passing values on is important.", "Family values should be passed down."], "The act of returning a book moves from the father to the child, making the inheritance visible."),
        ("How can you use the Unit 8 readings as models?", "Learn to portray people through specific events, but write about someone in your own family", ["Rename “Young Runtu” and submit it", "Write only about Lu Xun, not your family", "Family values cannot be shown through events"], "Runtu and Lu Xun's uncle are portrayed through events. Use an event from your own family."),
    ],
)

K(
    "g6a_ji", "Language Corner 8: Quotations by Lu Xun", "古诗文积累", 6, "上", 8, "conceptual",
    "Memorize Lu Xun's quotations and distinguish those from “Answering a Tease,” “Self-Portrait,” and “Hometown” from his essays. This section also practices titling texts and introduces the firm, slender style of Liu Gongquan's “Mysterious Pagoda Stele.”",
    "gs_56",
    [
        ("Which line follows “无情未必真豪杰”?", "怜子如何不丈夫", ["我以我血荐轩辕", "走的人多了，也便成了路", "俯首甘为孺子牛"], "This is from “Answering a Tease”: a true hero can love children. “我以我血荐轩辕” is from “Self-Portrait.”"),
        ("Which line follows “寄意寒星荃不察”?", "我以我血荐轩辕", ["怜子如何不丈夫", "我以我血荐轩辕人", "中国才有真进步"], "This is from “Self-Portrait,” offering one's passionate devotion to the motherland. Do not add a character after “轩辕.”"),
        ("Which line follows “其实地上本没有路”?", "走的人多了，也便成了路", ["走的人少了，也便成了路", "路就永远不会有", "这就是中国的脊梁"], "This is from “Hometown”: people make the road by walking it. “这就是中国的脊梁” is a different quotation."),
        ("What kind of people are meant by “这就是中国的脊梁”?", "People who work hard, persevere, speak up for the people, and sacrifice themselves for justice", ["People who only carve their names in stone", "People who ride on the people's backs", "People who do nothing"], "This is from “Has China Lost Its Self-Confidence?” The nation's backbone is made up of people who sustain it."),
    ],
)


# ---------- Grade 6, lower volume ----------
# Follows the current unified curriculum and aligns with the fall 2026 upper-volume sequence. “Two Children Debate the Sun,” “Written on Mr. Huyin's Wall,” “The Living Creature Inside the Watch,” “How Interesting They Were!,” and “Give Science the Wings of Imagination” are already covered above. “Early Spring: Presented to Zhang Shiba of the Water Ministry” is covered in Grade 5, lower volume.

K(
    "g6b_chun", "Spring Festival in Beijing", "阅读理解", 6, "下", 1, "reasoning",
    "Describe the sequence of the Laba Festival, Little New Year, New Year's Eve, New Year's Day, and the Lantern Festival in Lao She's account. New Year's Eve and the Lantern Festival receive more detail.",
    "yd_56",
    [
        ("Which day does Lao She mention first?", "The Laba Festival", ["New Year's Eve", "New Year's Day", "The Lantern Festival"], "The text begins with Laba congee and then moves forward through the calendar."),
        ("Which day between Laba and New Year's Eve receives special attention?", "Little New Year, on the 23rd day of the twelfth lunar month", ["The Dragon Boat Festival", "The Mid-Autumn Festival", "The Qingming Festival"], "Little New Year includes making offerings to the Kitchen God. The other festivals are not part of this sequence."),
        ("After New Year's Day, which later celebration is another climax?", "The Lantern Festival", ["New Year's Eve", "The Laba Festival", "Little New Year"], "Viewing lanterns is another high point of Spring Festival. New Year's Eve comes before New Year's Day."),
        ("What order does the article mainly use?", "Chronological order", ["People first and objects later, with no timeline", "The Lantern Festival before Laba", "New Year's Day only"], "The text follows the dates from Laba through the Lantern Festival."),
    ],
)

K(
    "g6b_la", "Laba Congee", "阅读理解", 6, "下", 1, "reasoning",
    "Understand how Ba'er, in Shen Congwen's story, eagerly awaits a thick, sweet pot of Laba congee. Do not confuse this text with Lao She's “Spring Festival in Beijing.”",
    "yd_56",
    [
        ("What is the name of the child who eagerly waits for the congee?", "Ba'er", ["Yu Lai", "The Cowherd", "Runtu"], "Ba'er circles the stove and keeps asking when the congee will be ready."),
        ("What is the Laba congee like?", "Thick and sweet, with rice, dates, chestnuts, and other ingredients", ["As thin as plain water", "A salty vegetable soup", "A single grain of rice"], "The text describes thick, sweet congee filled with fruit and grains."),
        ("Why is Ba'er impatient?", "The congee will not be ready until evening, and he has been waiting since morning", ["The congee is already gone", "His mother will not tell him about Laba", "He knocked over the pot"], "The longer he has to wait, the more clearly the text shows his appetite and anticipation."),
        ("Both this story and “Spring Festival in Beijing” mention Laba congee. How do they differ?", "This story follows one child's anticipation; the other describes a city's customs across the calendar", ["They are the same story", "This one does not mention congee", "The other mentions only the Lantern Festival"], "Lao She traces the whole Spring Festival period; “Laba Congee” closely follows Ba'er as he waits."),
    ],
)

K(
    "g6b_han", "“Cold Food Festival”", "古诗文积累", 6, "下", 1, "conceptual",
    "Memorize Han Hong's “Cold Food Festival,” especially the flying blossoms, imperial willows, and the Five Lords' households. Also study “The Faraway Cowherd Star” and “Watching the Moon on the Fifteenth Night.”",
    "gs_56",
    [
        ("Which line follows “春城无处不飞花”?", "寒食东风御柳斜", ["日暮汉宫传蜡烛", "春城无处不飞雪", "春城无处不飞絮"], "The Cold Food Festival breeze tilts the imperial willows. The poem says “飞花,” not “飞雪” or “飞絮.”"),
        ("Which line follows “日暮汉宫传蜡烛”?", "轻烟散入五侯家", ["寒食东风御柳斜", "轻烟散入百姓家", "轻烟散入五侯家门"], "The candle smoke drifts into the Five Lords' households, not ordinary people's homes."),
        ("Who wrote “Cold Food Festival”?", "Han Hong", ["Du Fu", "Wang Anshi", "Du Mu"], "Han Hong wrote this poem. Do not attribute it to Du Fu just because it describes spring."),
        ("Fires were traditionally forbidden on the Cold Food Festival, yet the poem describes candles being distributed. What does this suggest?", "Powerful court families received special permission unlike ordinary people", ["Every household received candles", "Candles were used to light poetry readings", "The Han palace was celebrating the Mid-Autumn Festival"], "The smoke reaching the Five Lords' homes points to privilege, not a celebration shared by everyone."),
    ],
)

K(
    "g6b_tiao", "“The Faraway Cowherd Star”", "古诗文积累", 6, "下", 1, "conceptual",
    "Memorize “The Faraway Cowherd Star” from “Nineteen Old Poems.” Remember “脉脉,” not “默默.”",
    "gs_56",
    [
        ("Which line follows “迢迢牵牛星”?", "皎皎河汉女", ["纤纤擢素手", "盈盈一水间", "札札弄机杼"], "The Cowherd Star is paired with the Weaver Girl. The lines about her slender hands and weaving come later."),
        ("Which line follows “纤纤擢素手”?", "札札弄机杼", ["终日不成章", "泣涕零如雨", "皎皎河汉女"], "She raises her slender hands and works the loom. The line about failing to finish the cloth comes next."),
        ("Which line follows “盈盈一水间”?", "脉脉不得语", ["默默不得语", "脉脉不能语", "盈盈不得语"], "The poem uses “脉脉,” not “默默” or “不能语.”"),
        ("What happens to the Cowherd and Weaver Girl in the poem?", "They are separated only by the Milky Way but cannot speak to each other", ["They meet on a bridge every day", "The Weaver Girl is happy because she has finished weaving", "The Cowherd Star falls into the river"], "“河汉清且浅，相去复几许。盈盈一水间，脉脉不得语。”"),
    ],
)

K(
    "g6b_yue", "“Watching the Moon on the Fifteenth Night”", "古诗文积累", 6, "下", 1, "conceptual",
    "Memorize Wang Jian's “Watching the Moon on the Fifteenth Night.” Remember the phrase about autumn thoughts, not sorrowful thoughts.",
    "gs_56",
    [
        ("Which line follows “中庭地白树栖鸦”?", "冷露无声湿桂花", ["不知秋思落谁家", "冷露有声湿桂花", "今夜月明人尽望"], "Moonlight brightens the courtyard, followed by dew silently wetting the osmanthus flowers. The poem says the dew is silent."),
        ("Which line follows “今夜月明人尽望”?", "不知秋思落谁家", ["不知愁思落谁家", "不知秋思在谁家", "冷露无声湿桂花"], "Wang Jian writes of autumn thoughts. “愁思” and “在谁家” are not the poem's wording."),
        ("Who wrote “Watching the Moon on the Fifteenth Night”?", "Wang Jian", ["Han Hong", "Li Bai", "Xin Qiji"], "Wang Jian wrote this poem. Han Hong wrote “Cold Food Festival”; do not confuse them because both concern festivals."),
        ("Which night does the title's “fifteenth night” refer to?", "The night of the Mid-Autumn Festival", ["The Cold Food Festival", "New Year's Eve", "The Lantern Festival on the fifteenth day of the first lunar month"], "The poem is about viewing the moon at Mid-Autumn. The Lantern Festival is also on a fifteenth, but in the first lunar month."),
    ],
)

K(
    "g6b_zang", "Tibetan Opera", "阅读理解", 6, "下", 1, "reasoning",
    "Understand Tibetan opera's masks, lack of a stage, and performances that can last several days, and learn how Thangtong Gyalpo founded it while raising support to build bridges.",
    "yd_56",
    [
        ("Which three features of Tibetan opera are emphasized by the opening rhetorical questions?", "Performers wear masks, there is no stage, and one play can last three to five days", ["It must be performed in a theater all night", "Masks are forbidden and elaborate scenery is required", "Only one person may sing"], "The opening highlights masks, the absence of a stage, and the long performance time."),
        ("Why did Thangtong Gyalpo organize a Tibetan opera troupe?", "To use performances to raise money and labor for bridges over the Yarlung Tsangpo", ["He wanted to turn Peking opera into Tibetan opera", "He planned to celebrate Spring Festival in Beijing", "He wanted to sell masks to tourists"], "There were no bridges over the river. He used Tibetan opera to recruit support for building them."),
        ("What did he leave behind and become known for?", "Many iron-chain bridges across the Yarlung Tsangpo", ["One wooden bridge only", "The end of the opera troupe", "A book about Laba congee"], "Building bridges and founding Tibetan opera are parts of the same story. A founder is a pioneer of the art form."),
        ("What color is the king's mask, and what does it represent?", "Red, representing authority", ["Green, representing gentleness", "White, representing duplicity", "A blue face with fangs, representing simplicity"], "The king wears red to show authority. Green represents the queen's gentleness; the sorceress has a half-black, half-white face."),
    ],
)

K(
    "g6b_su", "Writing: A Custom from My Hometown", "习作基础", 6, "下", 1, "application",
    "Explain a hometown custom, show how people observe it, develop its most distinctive part in detail, and include your own response. Saying only “Festivals are lively where I live” is not enough.",
    "xz_56",
    [
        ("Which passage explains how a hometown custom is carried out?", "On the evening of Little New Year, Grandma melts sticky stove candy, puts it on the Kitchen God's lips, and asks him to speak well of the family in heaven.", ["My hometown has many customs.", "Festivals are lively and fun.", "Lao She wrote “Spring Festival in Beijing.”"], "Putting candy on the Kitchen God's lips and asking for kind words describe what people do. Saying only “lively” does not identify a custom."),
        ("Which part should receive the most detail?", "The most distinctive part of the custom, especially one you know well", ["Name every festival in the country", "Write only your birth date", "Copy all of “Tibetan Opera”"], "A piece usually has only one or two main scenes. Mentioning everything briefly makes the hometown custom hard to remember."),
        ("Which sentence expresses a personal response while staying connected to the custom?", "As the candy melted, the room smelled so sweet that Little New Year suddenly felt more ceremonial than an ordinary dinner.", ["I was happy.", "A custom is a custom.", "Lao She wrote about New Year's Eve."], "The sweet smell and sense of ceremony show how the event felt to you. “I was happy” alone does not explain the occasion."),
        ("Which material does not belong in this essay?", "Yesterday afternoon's math test score", ["How people in your hometown wrap rice dumplings for the Dragon Boat Festival", "How the Lantern Festival parade route runs", "What adults say during the stove-god ritual"], "A test score is unrelated to customs. The food, parade, and ritual are customs."),
    ],
)

K(
    "g6b_yin", "Language Corner 1: Pronouncing 粥, 宵, 饺, and 祭", "识字写字", 6, "下", 1, "conceptual",
    "Learn the pronunciations of 粥, 宵, 饺, and 祭. For an impromptu speech, identify your audience and make one or two points. Also distinguish main ideas from supporting details. The memorization poem is the Han Yuefu “The Long Song.”",
    "sz_56",
    [
        ("How is the character “粥” pronounced?", "zhōu", ["zhù", "yù", "zhǒu"], "粥 is pronounced zhōu."),
        ("How is the character “宵” pronounced?", "xiāo", ["xiǎo", "shāo", "xiào"], "宵 is pronounced xiāo."),
        ("How is the character “饺” pronounced?", "jiǎo", ["jiāo", "jiào", "xiáo"], "饺 is pronounced jiǎo."),
        ("How is the character “祭” pronounced?", "jì", ["cài", "jī", "qì"], "祭 is pronounced jì."),
    ],
)

K(
    "g6b_lu", "Robinson Crusoe", "阅读理解", 6, "下", 2, "reasoning",
    "Understand how Daniel Defoe's Robinson Crusoe organizes life after being stranded on an island and weighs disadvantages against advantages.",
    "yd_56",
    [
        ("Who wrote “Robinson Crusoe”?", "Daniel Defoe", ["Mark Twain", "Leo Tolstoy", "Lao She"], "The author is the English writer Daniel Defoe. Mark Twain wrote “The Adventures of Tom Sawyer.”"),
        ("What did Crusoe first do to steady himself after being stranded?", "He listed the disadvantages and advantages side by side", ["He immediately built a large ship home", "He did nothing every day", "He threw away the calendar"], "Having no companions was a disadvantage, but having no one to harm him could be an advantage. The list helped him calm down."),
        ("How did he live on the island?", "He built shelter, grew food, raised goats, and later rescued Friday", ["He slept only on the beach", "A ship rescued him the next day", "He opened a shop with sailors"], "The story summary describes his years on the island and his rescue of a man he calls Friday."),
        ("What does the excerpt mainly show about him?", "He keeps finding ways to survive hardship", ["He regrets leaving home and stops working", "He only waits for someone to rescue him", "He burns the whole island"], "Making tools, finding food, and writing to encourage himself all show active survival."),
    ],
)

K(
    "g6b_qi", "The Wonderful Adventures of Nils", "阅读理解", 6, "下", 2, "reasoning",
    "Understand how Selma Lagerlöf's Nils travels on a goose after being turned into a tiny person and later becomes kinder. Do not confuse his story with Robinson Crusoe's.",
    "yd_56",
    [
        ("Who wrote “The Wonderful Adventures of Nils”?", "Selma Lagerlöf", ["Daniel Defoe", "Mark Twain", "Hans Christian Andersen"], "The author was the Swedish writer Selma Lagerlöf. Defoe wrote Robinson Crusoe."),
        ("Why was Nils turned into a tiny person?", "He disliked studying and teased animals, so a little elf punished him", ["He asked to become small", "The goose made him small", "He became small in a dream and woke up normal"], "Being made small was a punishment. At first, Nils felt frightened and anxious."),
        ("How did he travel?", "He rode on a goose's back and flew across many places", ["He traveled by train", "He rode a horse", "He sailed with Robinson Crusoe"], "The gander carried him away, letting him see wild animals and the countryside."),
        ("Why was he eventually allowed to return to normal size?", "He became kind and learned to take responsibility during the journey", ["He sold the goose", "The elf forgot the punishment", "He returned to normal as soon as the journey began"], "The story ends with Nils protecting the flock and learning to treat others well, so the elf restores him."),
    ],
)

K(
    "g6b_tang", "The Adventures of Tom Sawyer", "阅读理解", 6, "下", 2, "reasoning",
    "Understand how Mark Twain's Tom makes whitewashing a fence seem like a rare privilege, so his friends compete to do it. Do not confuse this text with Robinson Crusoe or Nils.",
    "yd_56",
    [
        ("Who wrote “The Adventures of Tom Sawyer”?", "Mark Twain", ["Daniel Defoe", "Leo Tolstoy", "Selma Lagerlöf"], "Mark Twain also wrote “The Boat in Venice.” Defoe wrote Robinson Crusoe."),
        ("What did Aunt Polly ask Tom to do?", "Paint the fence white", ["Grow wheat on a desert island", "Travel on a goose", "Perform on stage"], "In the excerpt, Tom is initially unhappy about having to paint the fence."),
        ("How did Tom get the others to compete for the job?", "He made painting the fence seem fun and like a rare privilege", ["He paid them", "He hid the brush", "He promised they could skip school for a year"], "The more Tom refuses to let them paint, the more they see it as a rare opportunity and offer him things in exchange."),
        ("What does the excerpt mainly show about Tom?", "He is clever and can turn an unpleasant chore into something others envy", ["He always obeys his aunt and never schemes", "He cannot talk to people", "He tears down the fence"], "One friend after another joins in, while Tom sits aside. That is his cleverness."),
    ],
)

K(
    "g6b_geng", "Writing: Summarize a Book", "习作基础", 6, "下", 2, "application",
    "Briefly summarize the main characters and events in order, cutting long descriptions of scenery and thoughts. Do not change the ending.",
    "xz_56",
    [
        ("What should a book summary keep?", "The main characters, their key actions, and how events develop", ["The color of every scene", "The number of metaphors the author used", "Copied vocabulary and favorite lines"], "A summary presents the story's framework. Detailed scenery and favorite wording can stay in the original."),
        ("Which passage is more like a summary of “Robinson Crusoe”?", "Crusoe is stranded on an island, builds shelter, finds food, rescues Friday, and eventually leaves.", ["Waves crash against the rocks, and the foam is white as salt.", "My heart raced as I read, and I felt as if I were on the island.", "The words “Friday.”"], "The first passage gives the character, events, and outcome. Waves are description; a racing heart is a reader response."),
        ("Which approach is wrong when writing a summary?", "Changing an original character's fate so a person who was not rescued is rescued", ["Cutting minor characters' conversations", "Condensing several chapters in your own words", "Keeping the original order"], "A summary can be shorter, but it must preserve the main facts."),
        ("How does a summary differ from a reader response?", "A summary tells what happens in the book; a response explains what the book makes you think about", ["Both must copy the entire original", "A summary cannot name characters", "A response cannot mention the book"], "First explain the events clearly, then respond to them. These are different tasks."),
    ],
)

K(
    "g6b_duo", "Language Corner 2: Characters with Multiple Readings—泊, 漂, 载, 难", "识字写字", 6, "下", 2, "conceptual",
    "Choose the pronunciation of 泊, 漂, 载, and 难 from context. In a book discussion, name the book, a memorable character, and your view. The memorization line is “Read with care; each word is worth its weight in gold.”",
    "sz_56",
    [
        ("How is the character “泊” pronounced in the word for mooring a boat?", "bó", ["pō", "bò", "pò"], "泊 is pronounced bó in the sense of mooring or drifting; it is pō in words for a lake or pool."),
        ("How is the character “漂” pronounced in the word for drifting?", "piāo", ["piào", "piǎo", "biāo"], "漂 is pronounced piāo in words for drifting or floating, but piào in the word for pretty."),
        ("How is the character “载” pronounced in the word for recording?", "zǎi", ["zài", "zāi", "cái"], "载 is pronounced zǎi in the sense of recording or publishing, and zài in the sense of carrying a load."),
        ("How is the character “难” pronounced in the word for disaster?", "nàn", ["nán", "nǎn", "nuó"], "难 is pronounced nàn in words for disaster or refugees, and nán in words for difficulty."),
    ],
)

K(
    "g6b_ci", "Language Corner 2: Meaning in Context", "词语", 6, "下", 2, "conceptual",
    "Infer how the same word changes meaning across contexts. When evaluating a character in a classic, connect your judgment to the character's actions instead of applying one label to everyone.",
    "cy_56",
    [
        ("What does 意思 mean in a sentence describing an interesting problem?", "Interesting or enjoyable", ["An opinion", "A gift", "Another meaning that needs explanation"], "Calling a problem 意思 means it is interesting, not that someone should give a gift."),
        ("If someone complains that a gift has no 意思, what does 意思 mean?", "Thoughtfulness or the gift's meaning", ["The problem's entertainment value", "A written definition", "A suggestion box"], "In a gift-giving context, 意思 can refer to the thought behind the gift."),
        ("What does 走 mean in the term for moving a chess piece?", "To move a chess piece", ["To walk", "To leave one's hometown", "To write a character incorrectly"], "In the chess expression, 走 means moving a piece, not walking."),
        ("What should you do first to infer a word's contextual meaning?", "Put the word back into its sentence", ["Always choose the first dictionary definition", "Delete the word", "Replace it with a homophone"], "Outside its sentence, the same word can have several meanings."),
    ],
)

K(
    "g6b_man", "Happy Reading: A Garden of World Classics", "阅读理解", 6, "下", 2, "conceptual",
    "Continue reading world classics. Choose a book related to this unit, and note its characters, key events, and your own view. Do not simply copy a textbook passage.",
    "yd_56",
    [
        ("What kind of books are the focus of this reading activity?", "World classics", ["Only the vocabulary list in this volume", "Only classical Chinese poems", "Only math word problems"], "The “garden” contains classics from around the world, not vocabulary lists or math problems."),
        ("Which reading approach is closest to the texts in this unit?", "Choose a foreign classic and focus on its characters and events", ["Memorize “Spring Festival in Beijing”", "Collect only pictures of Tibetan opera masks", "Copy a poem into a chart"], "Robinson Crusoe, Nils, and Tom are characters from world classics. Read another book in that spirit."),
        ("What is a useful note to make after reading?", "Who the characters are, one memorable event, and why you remember it", ["Only the total number of pages", "Only the author's nationality", "Only “I finished reading”"], "Page count and nationality cannot replace the story. Tie your opinion to a specific event."),
        ("Which activity does not count as reading a classic?", "Memorizing the author's name without being able to describe any event", ["Explaining a difficulty the main character faces", "Comparing how two translations present the same event", "Sharing a passage you want to discuss"], "A name is only an entry point. If you cannot describe an event, you have not engaged with the book."),
    ],
)

K(
    "g6b_cong", "In a Hurry", "阅读理解", 6, "下", 3, "reasoning",
    "Understand how Zhu Ziqing uses ordinary moments such as washing hands and eating to show time quietly passing.",
    "yd_56",
    [
        ("When the author washes his hands, where does he say the day passes?", "Through the washbasin", ["Through the window", "Through a schoolbag", "Through a crack in the door"], "The author says the day passes through the washbasin while he washes his hands."),
        ("When the author eats, where does he say the day passes?", "Through the rice bowl", ["Through the chopsticks", "Through the kitchen chimney", "Through the washbasin"], "The day passes through the rice bowl during a meal; the washbasin is mentioned while washing hands."),
        ("How are swallows, willows, peach blossoms, and time different?", "They can return, but time never comes back", ["They, like time, will never return next year", "Time can fly back like a swallow", "The author thinks time does not matter"], "Swallows return, but lost days do not."),
        ("What is the author trying to show?", "Time slips away during ordinary activities, so we should value it", ["Washing and eating waste time and should stop", "Days can be stored in a basin", "Remembering time is enough to keep it"], "More than eight thousand days slipped away silently, prompting the author to ask what had been left behind."),
    ],
)

K(
    "g6b_zhou", "That Sunday", "阅读理解", 6, "下", 3, "reasoning",
    "Understand Shi Tiesheng's story of a child who waits from morning to afternoon while the mother stays busy, until anticipation turns to disappointment.",
    "yd_56",
    [
        ("Who wrote “That Sunday”?", "Shi Tiesheng", ["Zhu Ziqing", "Lao She", "Lu Xun"], "Shi Tiesheng wrote this story. Zhu Ziqing wrote “In a Hurry.”"),
        ("What is the child longing for from the morning onward?", "For the mother to take the child out", ["For the father to return and repair a boat", "For a teacher to visit", "For the rain to stop so homework can begin"], "The mother promised to go out that Sunday, and the child keeps waiting."),
        ("Why does the mother not leave for so long?", "One household chore follows another, keeping her busy", ["She forgot the promise", "A snowstorm has started", "The child changed their mind"], "Shopping, cooking, and washing keep the mother occupied as the child's hope slowly fades."),
        ("By the afternoon, how has the child's mood changed?", "From anticipation to disappointment", ["It has become more excited", "The child decides to leave without the mother", "The child has completely forgotten the promise"], "The light fades, and the promise remains unfulfilled. That hollow disappointment drives the second half of the story."),
    ],
)

K(
    "g6b_qing", "Writing: Let Genuine Feelings Emerge", "习作基础", 6, "下", 3, "application",
    "Write about an event that moved you, describing the actions, words, and feelings in the moment. “I was moved” alone is not enough. Model texts in this unit are not separate topics.",
    "xz_56",
    [
        ("Which passage grounds emotion in a specific event?", "She reheated the cold food. I opened my mouth, but the words “You promised” never came out.", ["I was moved, very moved.", "The six words “Let genuine feelings emerge.”", "Sunday is the first day of the week."], "Reheating the food and holding back the words let readers see the moment. A bare claim of emotion gives them no event."),
        ("What kind of writing should you avoid in this assignment?", "Using only words like “happy” and “sad” without showing what happened", ["Developing the few minutes that moved you", "Including words you could not say at the time", "Ending with what you later understood"], "Let feelings grow from events. Without an event, the emotion has no foundation."),
        ("Which text offers a useful model?", "Like “That Sunday,” show how feelings change during a period of waiting", ["Copy “In a Hurry” into the essay", "Turn the assignment into a book summary", "List only three good words"], "Waiting, disappointment, and not wanting to blame someone are techniques to learn from. Copying or listing words cannot replace your own experience."),
        ("Which sentence sounds more like a slogan than a genuine feeling?", "We must always love life and everything in it.", ["The bowl burned my finger, but I still carried the soup inside.", "He did not look up; he just pushed the eraser toward me.", "I said it was fine, but my voice was softer than before."], "Anyone can write “always love everything.” A burned finger, a shared eraser, or a quieter voice belongs to a specific moment."),
    ],
)

K(
    "g6b_biao", "Ellipses and Em Dashes", "句子", 6, "下", 3, "procedural",
    "When writing to express genuine feelings, use an ellipsis for unfinished speech or an incomplete list, and an em dash for an explanation or an extended sound.",
    "jz_56",
    [
        ("Which mark shows that a speaker has not finished?", "Ellipsis ……", ["Em dash —", "Book-title brackets 《》", "Interpunct ·"], "Use an ellipsis when speech breaks off and more remains unsaid."),
        ("In “This is our class monitor—Li Qing,” what does the dash do?", "It introduces an explanation", ["It interrupts the speech", "It extends a sound", "It ends a list"], "The words after the em dash explain who the class monitor is."),
        ("In “The shelf holds fairy tales, stories, poems……,” what does the ellipsis mean?", "There are more books that have not been listed", ["The shelf is empty", "The books have disappeared", "The word “poems” needs an explanation"], "Use an ellipsis when a list is incomplete. An em dash can introduce an explanation."),
        ("Which punctuation mark shows a sound being held for a long time?", "Hey—— (em dash)", ["Hey…… (ellipsis)", "Hey. (period)", "Hey, (enumeration comma)"], "Use an em dash to stretch a sound. An ellipsis indicates omitted or unfinished content."),
    ],
)

K(
    "g6b_ma", "“Horse Poem”", "古诗文积累", 6, "下", 4, "conceptual",
    "Memorize Li He's “Horse Poem,” especially the sand like snow, the moon like a hook, and the golden bridle. Also study “Ode to Lime” and “Bamboo and Stone”; do not mix up their lines.",
    "gs_56",
    [
        ("Which line follows “大漠沙如雪”?", "燕山月似钩", ["何当金络脑", "燕山月如钩", "快走踏清秋"], "The desert sand looks like snow, and the Yan Mountains' moon looks like a curved hook. The poem says “似钩,” not “如钩.”"),
        ("Which line follows “何当金络脑”?", "快走踏清秋", ["燕山月似钩", "快走踏清秋风", "要留清白在人间"], "The speaker longs to wear a golden bridle and gallop through autumn. “清白” belongs to “Ode to Lime.”"),
        ("Who wrote “Horse Poem”?", "Li He", ["Yu Qian", "Zheng Xie", "Wang Wei"], "Li He wrote this poem. Yu Qian wrote “Ode to Lime,” and Zheng Xie wrote “Bamboo and Stone.”"),
        ("What does the poet mainly express through the horse?", "A hope to be recognized and given a chance to gallop freely", ["That desert sand is literally snow", "That horses should not wear bridles", "That no one should ride in autumn"], "A golden bridle is a precious fitting. “何当” expresses hope that the day will come."),
    ],
)

K(
    "g6b_shi", "“Ode to Lime”", "古诗文积累", 6, "下", 4, "conceptual",
    "Memorize Yu Qian's “Ode to Lime,” especially the lines about being crushed without fear and preserving purity. Also study “Horse Poem” and “Bamboo and Stone.”",
    "gs_56",
    [
        ("Which line follows “千锤万凿出深山”?", "烈火焚烧若等闲", ["粉骨碎身浑不怕", "要留清白在人间", "千磨万击还坚劲"], "The poem first describes lime being quarried, then its fearlessness in fire. “粉骨碎身” is the third line; “千磨万击” is from “Bamboo and Stone.”"),
        ("Which line follows “粉骨碎身浑不怕”?", "要留清白在人间", ["粉身碎骨全不怕", "要留清白在人世", "烈火焚烧若等闲"], "Yu Qian wrote “粉骨碎身” and “浑不怕.” “粉身碎骨,” “全不怕,” and “在人世” are common mix-ups."),
        ("Who wrote “Ode to Lime”?", "Yu Qian", ["Zheng Xie", "Wang Wei", "Wang Changling"], "Yu Qian wrote this poem; Zheng Xie wrote “Bamboo and Stone.”"),
        ("What does the poet express through lime?", "Even if crushed to pieces, one should preserve one's integrity", ["How to make lime", "How difficult the mountain road is", "That lime should sell for a high price"], "Hammering, chiseling, and burning are tests. What must be preserved is integrity, not a price."),
    ],
)

K(
    "g6b_zhu", "“Bamboo and Stone”", "古诗文积累", 6, "下", 4, "conceptual",
    "Memorize Zheng Xie's “Bamboo and Stone.” Do not confuse it with Yu Qian's “Ode to Lime” or Li He's “Horse Poem.”",
    "gs_56",
    [
        ("Which line follows “咬定青山不放松”?", "立根原在破岩中", ["立根原在破崖中", "立根原在岩石中", "千磨万击还坚劲"], "The bamboo roots grow in broken rock. The poem says “破岩,” not “破崖.”"),
        ("Which line follows “千磨万击还坚劲”?", "任尔东西南北风", ["凭尔东西南北风", "任你东西南北风", "任尔东南西北风"], "The poem says “任尔,” not “凭尔” or “任你.” Keep the order “东西南北.”"),
        ("Who wrote “Bamboo and Stone”?", "Zheng Xie", ["Yu Qian", "Du Fu", "Su Shi"], "Zheng Xie is also known as Zheng Banqiao. Yu Qian wrote “Ode to Lime”; do not confuse the poets."),
        ("Which line is not from “Bamboo and Stone”?", "粉骨碎身浑不怕", ["咬定青山不放松", "立根原在破岩中", "任尔东西南北风"], "“粉骨碎身浑不怕” is from “Ode to Lime.”"),
    ],
)

K(
    "g6b_hui", "Memories of Sixteen Years Ago", "阅读理解", 6, "下", 4, "reasoning",
    "Understand Li Xinghua's memories of her father, Li Dazhao: April 28, 1927, was the day he was executed; he burned documents and remained calm and composed in court.",
    "yd_56",
    [
        ("Who wrote this memoir, and whom is it about?", "Li Xinghua wrote about her father, Li Dazhao", ["Li Dazhao wrote about his daughter, Li Xinghua", "Mao Zedong wrote about Zhang Side", "Dong Cunrui wrote about his comrades"], "The author was Li Dazhao's daughter. Zhang Side appears in “Serve the People,” and Dong Cunrui appears in the next text."),
        ("Which date does the opening say the author will never forget?", "April 28, 1927", ["October 1, 1949", "The day Longhua was liberated in 1948", "September 8, 1944"], "It was the day her father was executed, sixteen years before she wrote. The founding ceremony, Longhua, and Zhang Side's memorial were on different dates."),
        ("Why did the father burn books and documents when the situation became tense?", "To keep them from falling into enemy hands and exposing the organization", ["There was too much paper in the house", "He planned to become a teacher", "His daughter needed kindling"], "He burned them to protect the revolutionary work, not to save space."),
        ("How did the father look in court?", "Calm and composed", ["He shouted at the enemy", "He was too frightened to speak", "He handed over the documents"], "He glanced at his family with a calm, composed expression, showing his confidence in the revolutionary cause."),
    ],
)

K(
    "g6b_wei", "Serve the People", "阅读理解", 6, "下", 4, "reasoning",
    "Understand Mao Zedong's speech at Zhang Side's memorial: dying for the people's interests is heavier than Mount Tai. Do not confuse Zhang Side with Li Dazhao or Dong Cunrui.",
    "yd_56",
    [
        ("Whom does this speech honor?", "Zhang Side", ["Li Dazhao", "Dong Cunrui", "Qiu Shaoyun"], "On September 8, 1944, Mao Zedong spoke at Zhang Side's memorial. The other people belong to different texts."),
        ("What does “人固有一死，或重于泰山，或轻于鸿毛” explain?", "The meaning of death depends on whom one dies for", ["People can live forever", "Mount Tai is easier to weigh than a feather", "Zhang Side died on Mount Tai"], "The quotation is from Sima Qian. Dying for the people's interests is heavier than Mount Tai."),
        ("What does the text say the group works for?", "完全是为着解放人民，彻底地为人民的利益工作", ["To make everyone join the army", "To keep their own positions", "To write a memoir"], "The words “completely” and “thoroughly” show that the group has no other motive."),
        ("What follows “我们都是来自五湖四海”?", "We have come together for one common revolutionary goal", ["So no one knows anyone else", "So there is no need for unity", "So everyone must return home"], "People come from different places but share a goal. The speech then calls for mutual care and support."),
    ],
)

K(
    "g6b_dong", "Dong Cunrui Blows Up the Bunker", "阅读理解", 6, "下", 4, "reasoning",
    "Understand how Dong Cunrui held an explosive charge against a bunker during the 1948 liberation of Longhua and shouted, “为了新中国，前进.” Do not confuse his action with those of Qiu Shaoyun or Huang Jiguang.",
    "yd_56",
    [
        ("What did Dong Cunrui blow up?", "A bunker blocking the road", ["An enemy warship", "A lime kiln", "A machine gun on Langya Mountain"], "Fire from the bridge-shaped bunker pinned down the troops and blocked their advance."),
        ("What did he do when the explosive charge would not stay in place?", "He held it up with his hand and lit the fuse", ["He handed it to someone else and retreated", "He lay still on the ground", "He blocked a firing hole with his chest"], "With no support, he used his body to hold the charge beneath the bunker. Huang Jiguang blocked a firing hole; Qiu Shaoyun stayed still in flames."),
        ("What did he shout as he lit the fuse?", "为了新中国，前进", ["为了新中国，停下", "蒙汉情深何忍别", "人固有一死"], "He was urging his comrades to charge forward, not stop. The other lines come from different texts."),
        ("What happened after the bunker was destroyed?", "The troops charged, Longhua was liberated, and Dong Cunrui died", ["The bunker remained and the battle was postponed", "He returned carrying the explosive charge", "The enemy dismantled the bridge"], "The mission opened the way forward, but Dong Cunrui did not return."),
    ],
)

K(
    "g6b_fen", "Integrated Study: A Record of Struggle", "阅读理解", 6, "下", 4, "reasoning",
    "Research a revolutionary's story and explain what the person did and why it is worth remembering. You can tell the story or create a small newspaper.",
    "yd_56",
    [
        ("What should this activity investigate?", "The actions and struggles of revolutionaries", ["What people eat at Spring Festival", "How to summarize a foreign novel", "The difference between ellipses and em dashes"], "The Unit 4 readings provide source material. Spring Festival, book summaries, and punctuation belong to other units."),
        ("Which activity fits this assignment?", "After reading “Memories of Sixteen Years Ago,” briefly describe Li Dazhao's conduct in court", ["Copy the class schedule into the newspaper", "Draw a bridge without explaining it", "Collect classmates' birthdays"], "The activity focuses on a specific person and event. A schedule or birthdays do not explain a struggle."),
        ("What should a small newspaper include?", "What the person did, what happened, and why you remember the person", ["A title above a blank page", "All three readings pasted in full", "Only the activity date"], "A title and date are just layout. Readers need the story and your understanding; pasting everything is not research."),
        ("Who is not a suitable person for this activity?", "Tom, who turned fence painting into a game", ["Li Dazhao", "Zhang Side", "Dong Cunrui"], "Tom is a child from a novel in Unit 2. The other three are revolutionaries covered in this unit."),
    ],
)

K(
    "g6b_yd4", "Language Corner 4: Framing and Symbolic Objects", "阅读理解", 6, "下", 4, "reasoning",
    "Notice how a text's opening and ending echo each other, and explain how a poem turns an object into a statement of personal principle. The memorization proverb is “良药苦口利于病，忠言逆耳利于行.”",
    "yd_56",
    [
        ("Which date appears at both the beginning and the end of “Memories of Sixteen Years Ago”?", "April 28, 1927", ["The 23rd day of the twelfth lunar month", "October 1, 1949", "An ordinary Sunday"], "The opening says the author will never forget the day; the ending returns to her father's execution. This creates an echo."),
        ("What aspiration is expressed by “要留清白在人间” in “Ode to Lime”?", "Even if crushed to pieces, preserve one's integrity", ["Hope a horse wears a golden bridle", "Hope bamboo never faces wind", "Hope candles are distributed to everyone"], "Preserving integrity is the poem's conclusion. The golden bridle is from “Horse Poem,” and the winds are from “Bamboo and Stone.”"),
        ("What kind of person does “Bamboo and Stone” portray through the bamboo?", "Rooted in broken rock and unshaken by any wind", ["Someone who falls at the first wind", "Someone concerned only with appearance", "Someone who wants to leave the green hills"], "Clinging to the hills, taking root, and remaining firm all express resilience."),
        ("Which line follows “良药苦口利于病”?", "忠言逆耳利于行", ["树欲静而风不止", "少壮不努力", "春风又绿江南岸"], "Bitter medicine helps cure illness; advice that is hard to hear can help us act well. “树欲静...” is a different proverb."),
    ],
)

K(
    "g6b_xue", "Classical Text: Learning Chess", "阅读理解", 6, "下", 5, "reasoning",
    "Understand “Learning Chess” from the Mencius: Yi Qiu teaches two students; one concentrates, while the other thinks about shooting a swan and learns less. The difference is not intelligence. Do not confuse this with the upper-volume “Two Children Debate the Sun.”",
    "yd_wenyan",
    [
        ("What kind of person was Yi Qiu?", "The best chess player in the whole country", ["The stronger of the two students", "A student of Confucius", "One of the children debating the Sun"], "“通国之善弈者” means the best chess player in the country. Yi Qiu is the teacher, not a student."),
        ("Why did the two students get different results?", "One listened attentively; the other kept thinking about drawing a bow to shoot a swan", ["One was much more intelligent", "Yi Qiu taught the method to only one student", "They were not learning chess"], "“其一人专心致志，惟弈秋之为听.” The other listened but kept thinking a swan was coming."),
        ("What does “为是其智弗若与？曰：非然也” mean?", "Is it because his intelligence is inferior? No, that is not so.", ["Is it because his teacher is inferior? Yes.", "Is the Sun closer? We cannot decide.", "Did the swan fly away? Yes."], "“非然也” means “that is not so.” The difference is concentration, not intelligence. The question about the Sun belongs to “Two Children Debate the Sun.”"),
        ("Which work is this passage from?", "Mencius", ["Liezi", "Analects", "Records of the Grand Historian"], "“Learning Chess” is selected from “Gaozi I” in the Mencius. “Two Children Debate the Sun” is from Liezi."),
    ],
)

K(
    "g6b_li", "Truth Is Born from a Hundred Questions", "阅读理解", 6, "下", 5, "reasoning",
    "Understand how Ye Yonglie uses examples from Boyle, Wegener, and Aserinsky to argue that truth is born from persistent questioning and investigation.",
    "yd_56",
    [
        ("Which claim is the text trying to prove?", "Truth is born from a hundred questions", ["Truth appears automatically whenever something unexpected happens", "Scientists do not need experiments", "Truth exists only in books"], "The title states the claim. An unexpected observation is only the beginning of a question."),
        ("What did Boyle notice, and what did he later make?", "Hydrochloric acid turned violet petals red; he later made litmus paper", ["Swirling bathwater led him to discover Earth's rotation", "His son's moving eyes revealed that people dream", "Coastlines on a map fit together"], "The color change raised questions that experiments helped answer. The bathwater and coastlines belong to other scientists."),
        ("What observation led Wegener to propose continental drift?", "The bulge on South America's east coast fit the indentation on Africa's west coast", ["Violet petals changed color", "Bathwater rotated counterclockwise in the Northern Hemisphere", "A sleeping person's eyes moved"], "Wegener suspected the match was not a coincidence, gathered more evidence, and proposed continental drift."),
        ("What do the three examples have in common?", "Each starts with an ordinary observation, raises questions, and reaches a conclusion through investigation", ["All three people were ancient Chinese chess players", "They knew the answers from the start", "Their conclusions came by chance without research"], "Observation, questioning, repeated investigation, and a conclusion appear in all three examples."),
    ],
)

K(
    "g6b_xie", "Writing: Choose Material Around a Central Idea", "习作基础", 6, "下", 5, "application",
    "After choosing a central idea, keep material that supports it and remove unrelated details. The upper volume already practiced developing an event around one idea.",
    "xz_56",
    [
        ("The central idea is “Classmates help one another.” Which material should stay?", "My desk mate lent me notes and explained the problem.", ["I watched a movie on Sunday.", "My cat is very fat.", "The wind was strong yesterday."], "Lending notes and explaining a problem show classmates helping each other. The movie, cat, and wind do not."),
        ("The central idea is “This experiment taught me to be more careful.” Which sentence is off topic?", "After school, I played soccer on the playground for half an hour.", ["I read the steps backward the first time.", "The second time, I followed the checklist and succeeded.", "I learned that care matters more than speed."], "Soccer has nothing to do with the experiment or carefulness. The other details develop the central idea."),
        ("What should you do when you have too much material?", "Remove details that do not support the central idea", ["Include everything on the list", "Change the central idea to every event", "Keep one example unrelated to the idea"], "Selecting material around one idea keeps the writing focused."),
        ("Which paragraph selects details around one central idea?", "To show that Dad is punctual, I describe how he arrives early at the station and is never late.", ["I describe Dad's punctuality, then my cat, then yesterday's cartoon.", "Punctuality.", "Dad, cat, cartoon."], "Arriving early and never being late both support punctuality. The cat and cartoon belong to other ideas."),
    ],
)

K(
    "g6b_yd5", "Language Corner 5: Debate", "句子", 6, "下", 5, "procedural",
    "This language corner practices debate. State your position in one sentence, support it with an example, listen to the other side, and respond without mocking anyone.",
    "jz_56",
    [
        ("What should you do first when starting a debate?", "State in one sentence whether you agree or disagree", ["Tell a joke unrelated to the topic", "Ask the other person to admit they are wrong", "Raise your voice without giving a point"], "The audience needs to know your position. A joke or a louder voice is not an argument."),
        ("Which statement gives a reason?", "In “Learning Chess,” the student who did not concentrate learned less, so attention matters in learning.", ["You are never right.", "I do not want to hear you.", "There is nothing to debate."], "Using an outcome from the text supports an opinion with evidence. Insulting a person does not address the argument."),
        ("What is a good response after hearing the other side?", "Address the reason they just gave and explain your different view", ["Ignore it and repeat your first sentence", "Mock their accent", "Change the subject to yesterday's game"], "Debate responds to reasons. Repeating, mocking, or changing the topic does not answer the other person."),
        ("Which statement sounds like an insult rather than a debate?", "You are so stupid. Why are you even debating?", ["I do not think an unexpected observation proves a truth, because the scientists in the text continued researching.", "You say concentration does not matter, but the unfocused student in “Learning Chess” did not learn.", "I agree with the first part, and I would like to add an example to the second."], "Calling someone stupid attacks the person. The other statements address ideas and examples."),
    ],
)

K(
    "g6b_wang", "Integrated Study: Looking Back", "习作基础", 6, "下", 6, "application",
    "Choose a real event from elementary school and describe when and where it happened, what people did, and how you felt. “Elementary school was fun” alone is not a memory.",
    "xz_56",
    [
        ("How should you choose material for a memoir?", "Choose a real experience with details you still remember", ["Include all six years of class schedules", "Invent a heroic event that never happened", "Copy a text and call it your memory"], "Real, specific details show readers what your school life was like. Inventing and copying are not memoir."),
        ("Which passage sounds most like a memory?", "On a rainy afternoon in Grade 4, Lin Xiao pushed her umbrella into my hand and ran back to class in the rain.", ["Elementary school was colorful, happy, and unforgettable.", "Looking back on the past.", "Our school has a classroom building."], "The rain, offered umbrella, and wet dash form one specific event. “Colorful and unforgettable” could describe anyone's school years."),
        ("Besides what happened, what else should you include?", "How you felt then or how you understand the event now", ["The school's postal code", "Classmates' birth months", "That day's schedule"], "Your feelings make the event personal. A postal code, birth month, or schedule cannot show what you remember."),
        ("Which approach makes a memoir lose focus?", "Write about one tug-of-war, then your cat, then yesterday's television show", ["Describe how your tug-of-war team fell behind and caught up", "Focus on one classmate you remember from the tug-of-war", "End by recalling the cheer you still remember"], "The cat and television pull the piece away from its focus. The other approaches stay with the same tug-of-war."),
    ],
)

K(
    "g6b_bie", "Integrated Study: Saying Goodbye", "习作基础", 6, "下", 6, "application",
    "Write a farewell message to a teacher or classmate that recalls something you experienced together, then expresses your affection and good wishes. A generic “Best of luck” does not show who the message is for.",
    "xz_56",
    [
        ("Who is a farewell message mainly for?", "A teacher or classmate you have spent a lot of time with", ["A celebrity you have never met", "Robinson Crusoe from a text", "An exam paper"], "Farewells mark an upcoming separation. A celebrity and an exam paper are not people who shared your school years."),
        ("Which sentence sounds like it is addressed to a specific person?", "That afternoon you helped me revise my essay; I still remember the sentence you circled in red.", ["Wishing you a bright future.", "Life is like a song.", "Take care."], "The essay, red pen, and circled sentence are details only the two of you share. A four-word wish could go to anyone."),
        ("A farewell can include good wishes. How can you make them personal?", "Connect them to an event so the reader knows why you are offering them", ["Replace them with a longer idiom", "Write the wish three times", "Avoid naming anyone"], "Because you patiently helped me revise, I hope you meet people who are just as patient. That gives the wish a reason."),
        ("Which does not fit a farewell message?", "Listing every question the person failed on the latest test", ["Remembering that they always locked up last during cleanup", "Telling a teacher you remember a story she shared", "Saying you will remember a small moment after you part"], "Listing mistakes is keeping score, not saying goodbye. The other choices recall shared moments."),
    ],
)

K(
    "g6b_zeng", "Activity: Make Graduation Messages Personal", "习作基础", 6, "下", 6, "application",
    "Write a sincere message to a classmate or teacher, preferably including something you experienced together. It can become a keepsake from saying goodbye.",
    "xz_56",
    [
        ("Which sentence sounds like a thoughtful graduation message?", "The day you lent me an eraser, I realized you notice when others are having a hard time.", ["Wishing you a bright future.", "May everything go well.", "Study hard."], "The eraser gives the reader a shared memory. A four-word wish is so broad it could be for anyone."),
        ("What should you avoid in a graduation message?", "Copying an empty phrase that has nothing to do with the person", ["Mentioning a small thing the person did for you", "Including a sentence you remember", "Offering a wish and explaining why"], "A general wish is fine, but if that is all you write, the reader cannot tell who it is for."),
        ("Which message is appropriate for a teacher?", "I remember you calling me to the board and patiently explaining that problem again.", ["I hope you never teach again.", "The weather is nice today.", "Your office is on the second floor."], "Explaining the problem again is something the two of you shared. The weather and office location are not farewell messages."),
        ("What should be at the center of a message about memorable school years?", "Your gratitude, good wishes, or a memory of the person", ["Criticizing every classmate", "Only your home address", "A copied class schedule"], "A message is meant for a particular person. An address or schedule is not what you want to say."),
    ],
)

K(
    "g6b_cai", "“Picking Ferns” (Excerpt)", "古诗文积累", 6, "下", 7, "conceptual",
    "Memorize the excerpt from “Picking Ferns” in the Book of Songs, distinguishing the spring departure from the snowy return.",
    "gs_56",
    [
        ("Which line follows “昔我往矣”?", "杨柳依依", ["雨雪霏霏", "今我来思", "行道迟迟"], "The speaker departs in spring, when the willow branches are soft. Snow belongs to the return journey."),
        ("Which line follows “今我来思”?", "雨雪霏霏", ["杨柳依依", "载渴载饥", "莫知我哀"], "On the return, heavy snow is falling. “载渴载饥” comes later; 思 is a grammatical particle here, not “to think.”"),
        ("Which line follows “行道迟迟”?", "载渴载饥", ["我心伤悲", "莫知我哀", "杨柳依依"], "The road is long, and the traveler is thirsty and hungry. “我心伤悲” comes in the preceding line."),
        ("Where is this excerpt from?", "The Book of Songs", ["Mencius", "A poem by Li Bai", "A poem by Du Fu"], "“Picking Ferns” is from the Xiaoya section of the Book of Songs. Do not attribute it to a later poet just because it mentions willows."),
    ],
)

K(
    "g6b_song", "“Seeing Yuan Er off to Anxi”", "古诗文积累", 6, "下", 7, "conceptual",
    "Memorize Wang Wei's farewell poem, especially the rain dampening the dust, the fresh willow color, and the loneliness beyond Yang Pass.",
    "gs_56",
    [
        ("Which line follows “渭城朝雨浥轻尘”?", "客舍青青柳色新", ["劝君更尽一杯酒", "客舍青青柳色青", "西出阳关无故人"], "Morning rain dampens the dust, and the willows beside the inn look fresh. The line about having no old friends comes last."),
        ("Which line follows “劝君更尽一杯酒”?", "西出阳关无故人", ["西出阳关无故人在", "客舍青青柳色新", "劝君更进一杯酒"], "The poet urges one more drink because familiar friends will be hard to find beyond Yang Pass. The poem says “更尽,” not “更进,” and adds nothing after “无故人.”"),
        ("Who wrote this poem?", "Wang Wei", ["Wang Changling", "Wang Jian", "Wang Anshi"], "Wang Wei wrote this farewell poem. Do not confuse him with Wang Jian or Wang Anshi because they share a surname."),
        ("Why does the poet urge his friend to drink one more cup?", "The friend is going to Anxi and will have few familiar companions beyond Yang Pass", ["They are celebrating the New Year at home", "The rain is too heavy to leave", "He wants to exchange the wine for tea"], "The line about having no old friends beyond Yang Pass explains the farewell, not a New Year celebration or tea."),
    ],
)

K(
    "g6b_yu", "“Happy Rain on a Spring Night”", "古诗文积累", 6, "下", 7, "conceptual",
    "Memorize Du Fu's “Happy Rain on a Spring Night,” especially the rain arriving in spring, nourishing things silently, and flowers weighing down the city.",
    "gs_56",
    [
        ("Which line follows “好雨知时节”?", "当春乃发生", ["随风潜入夜", "当春才发生", "润物细无声"], "The timely rain arrives with spring. The poem says “乃,” not “才.” The line about entering the night comes in the next couplet."),
        ("Which line follows “随风潜入夜”?", "润物细无声", ["润物细无声息", "野径云俱黑", "花重锦官城"], "The rain follows the wind into the night and nourishes everything without a sound. Do not add a character after “无声.”"),
        ("Which line follows “晓看红湿处”?", "花重锦官城", ["花重锦官城外", "江船火独明", "花重锦官城中"], "In the morning, rain-heavy blossoms weigh down the city of Chengdu. The poem says “锦官城,” with no extra word after it."),
        ("Who wrote this poem?", "Du Fu", ["Wang Wei", "Du Mu", "Li Bai"], "Du Fu wrote “Happy Rain on a Spring Night.” Do not confuse him with Du Mu just because they share a surname."),
    ],
)

K(
    "g6b_bo", "“Mooring at Guazhou”", "古诗文积累", 6, "下", 8, "conceptual",
    "Memorize Wang Anshi's “Mooring at Guazhou,” especially the spring wind greening the southern shore and the question of when the moon will shine on the speaker's return. Do not confuse it with “Written on Mr. Huyin's Wall.”",
    "gs_56",
    [
        ("Which line follows “京口瓜洲一水间”?", "钟山只隔数重山", ["春风又绿江南岸", "钟山只隔数重山外", "明月何时照我还"], "Jingkou and Guazhou are separated by a river, while Zhongshan is only a few hills away. The line about the moon comes last."),
        ("Which line follows “春风又绿江南岸”?", "明月何时照我还", ["明月何时照我归", "春风又到江南岸", "两山排闼送青来"], "绿 means that the spring wind turns the southern shore green. The poem says “照我还,” not “照我归”; the other lines belong elsewhere."),
        ("Who wrote this poem?", "Wang Anshi", ["Du Fu", "Ye Shaoweng", "Wang Wei"], "Wang Anshi wrote “Mooring at Guazhou.” He also wrote “Written on Mr. Huyin's Wall”; do not merge the two poems."),
        ("What does 绿 mean in “春风又绿江南岸”?", "To turn green", ["The noun “green,” with no action", "To come again", "To push open a mountain"], "The spring wind turns the southern shore green; 绿 functions as a verb. The line about the mountains opening a door is from “Written on Mr. Huyin's Wall.”"),
    ],
)

K(
    "g6b_yuan", "“A Visit to the Garden Is Unrewarded”", "古诗文积累", 6, "下", 8, "conceptual",
    "Memorize Ye Shaoweng's poem, especially the gently knocked wooden gate and the apricot branch that escapes the garden wall. 不值 means the visitor did not meet the owner.",
    "gs_56",
    [
        ("Which line follows “应怜屐齿印苍苔”?", "小扣柴扉久不开", ["春色满园关不住", "小叩柴门久不开", "一枝红杏出墙来"], "The visitor may have avoided damaging the moss, so the wooden gate stayed closed despite a gentle knock. The poem says “小扣” and “柴扉,” not “小叩” and “柴门.”"),
        ("Which line follows “春色满园关不住”?", "一枝红杏出墙来", ["一枝红杏出墙外", "小扣柴扉久不开", "一枝红杏出墙头"], "The gate can be shut, but spring cannot be kept in; a branch of red apricot reaches over the wall. The poem says “出墙来.”"),
        ("Who wrote “A Visit to the Garden Is Unrewarded”?", "Ye Shaoweng", ["Wang Anshi", "Du Fu", "Su Shi, Ye Shaoweng's teacher"], "Ye Shaoweng wrote this poem. Wang Anshi wrote “Mooring at Guazhou”; do not confuse them because both describe spring."),
        ("What does 不值 mean in the title?", "The visitor did not meet the person they came to see", ["The garden is not valuable", "The flowers are not worth seeing", "The owner is not worth visiting"], "值 means to meet. The visitor came to the garden but did not meet the owner."),
    ],
)

K(
    "g6b_bu", "“Song of Divination: Sending Bao Haoran to Eastern Zhejiang”", "古诗文积累", 6, "下", 8, "conceptual",
    "Memorize Wang Guan's farewell poem, especially the water like sideways glances, mountains like gathered brows, and the wish to stay with spring in the south. Do not mix it up with “Seeing Yuan Er off to Anxi.”",
    "gs_56",
    [
        ("Which line follows “水是眼波横”?", "山是眉峰聚", ["山是眉峰竖", "欲问行人去那边", "眉眼盈盈处"], "The water is compared to sideways glances, and the hills to gathered brows. The question about the traveler comes later."),
        ("Which line follows “欲问行人去那边”?", "眉眼盈盈处", ["眉眼盈盈处去", "才始送春归", "千万和春住"], "The traveler is headed toward the meeting place of the waters and hills, imagined as graceful brows and eyes. Do not add a word after “盈盈处.”"),
        ("Which line follows “若到江南赶上春”?", "千万和春住", ["千万与春住", "又送君归去", "劝君更尽一杯酒"], "If the traveler catches spring in the south, the poet wishes them to stay with it. The line about drinking one more cup is by Wang Wei."),
        ("Who wrote this poem?", "Wang Guan", ["Wang Wei", "Xin Qiji", "Su Shi"], "Wang Guan wrote this farewell poem for Bao Haoran. Wang Wei wrote “Seeing Yuan Er off to Anxi”; do not confuse the two farewells."),
    ],
)
