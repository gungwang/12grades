# -*- coding: utf-8 -*-
"""Grade 4, both semesters. The first-semester topics follow the 2024 revision / autumn 2026 unified curriculum (6-3 system); the second-semester topics follow the current unified curriculum / common spring 2026 sequence."""
from zh_lib import K

# ---------- Grade 4, Semester 1 ----------
# Keep "上" and "下": they are the existing semester tokens passed to zh_lib.K.
# Topics follow the autumn 2026 sequence for the 2024 revision (6-3 system).
# Split each of the three-poem sets in Units 3 and 8 into separate entries; combine the two modern poems into one topic.
# Unit 5 has no language-workshop section; keep the writing unit "A Kaleidoscope of Life" separate, and do not create topics for the sample texts "My Apricots Are Ripe" and "The Wooden Boat".
# Keep "Long, Long Ago" as a separate reading-for-pleasure topic; merge oral communication and writing tasks into their corresponding language-workshop topics.
# Drop the older-edition texts "Walking on the Moon", "The Century of Calling the Wind and Rain", and "Ximen Bao Governs Ye"; move "The Square Hat Shop" from Grade 3, Semester 2, into this book.
# Grades 3, Semester 1, and 4, Semester 2, already include Bing Xin's short poem "Stars"; this book's "Stars" is Ba Jin's prose, so it uses the new key g4a_fanxing.
# The Grade 4, Semester 2, writing samples include "The Summer Palace"; this book's Unit 6 "The Summer Palace" is a full lesson, so it uses the new key g4a_yi.

K(
    "g4a_chao", "Reading “The Tidal Bore”", "Reading Comprehension", 4, "上", 1, "reasoning",
    "Describe how the Qiantang River tidal bore changes before it arrives, as it comes in, and after it passes.",
    "yd_34",
    [
        ("Before the tide arrived, what was the river surface like?", "Calm and still", ["A white line had already appeared", "Thousands of warhorses were charging together", "The waves were still sweeping across the sky and land"], "The text first describes a calm river as people wait for the tide. The white line and charging horses appear as the tide comes in."),
        ("What appeared in the distance when the tide first arrived?", "A white line", ["A red sun", "A stone bridge", "A small boat"], "From far away, the tide looked like a white line; as it came closer, it became a wall of waves."),
        ("What does the text compare the surging tide to?", "Thousands of white warhorses charging side by side", ["A sleeping fish", "A lotus slowly opening", "A still mirror"], "The sound is like rolling thunder, and the water looks like charging white horses. The lotus and mirror are not metaphors from this text."),
        ("What happens to the river right after the head of the tide passes?", "The waves keep surging for a long time before the river becomes calm again", ["Every drop of water disappears at once", "The white line stops in place", "The river never changed"], "After the tide moves west, the waves continue for a long time before the Qiantang River becomes calm."),
    ],
)

K(
    "g4a_fanxing", "Reading “Stars”", "Reading Comprehension", 4, "上", 1, "reasoning",
    "Understand Ba Jin's prose: he sees the stars in his hometown long ago, in Nanjing three years earlier, and at sea today, with a different scene and feeling each time. Do not confuse it with Bing Xin's short poem “Stars.”",
    "yd_34",
    [
        ("Who wrote the prose piece “Stars”?", "Ba Jin", ["Bing Xin", "Liu Dabai", "Xu Zhimo"], "Ba Jin wrote the piece about seeing the stars three times. Bing Xin's “Stars” is a short poem in Grade 4, Semester 2. Liu Dabai and Xu Zhimo wrote the two modern poems."),
        ("Which three times does the author describe?", "Long ago in his hometown courtyard, three years ago in a Nanjing garden, and today on a ship at sea", ["Only once, watching the tide by the Qiantang River", "Only on his mother's lap and under wisteria leaves", "Only at Zaoyuan in Yan'an"], "The locations change across three different times. The scenes on a mother's lap belong to Bing Xin's three short poems, not this piece."),
        ("What do the stars look like at sea today?", "Faint and bright by turns; they move with the ship and seem low enough to fall", ["Crowded together like a wall", "Like white warhorses charging side by side", "Like a flower-cow flattening a cockscomb flower"], "From the deck, the stars seem low and bright. The horses are from “The Tidal Bore,” and the flower-cow is from “Song of the Flower-Cow.”"),
        ("Which feeling appears in the text across the three viewings?", "Looking up at the stars feels like returning to his mother's embrace", ["The stars are stones left over from Nüwa repairing the sky", "The stars are wood and stones carried by Jingwei", "The stars are three memories Bing Xin wrote beneath wisteria leaves"], "Both the hometown and sea scenes feel like sleeping in his mother's embrace. Sky-repair, sea-filling, and Bing Xin's poems belong to other works."),
    ],
)

K(
    "g4a_xian", "Two Modern Poems", "Reading Comprehension", 4, "上", 1, "reasoning",
    "Read Liu Dabai's “Autumn Evening on the River” and Xu Zhimo's “Song of the Flower-Cow”: a returning bird drops the setting sun into the river, while a flower-cow sits, sleeps, walks, and dreams in the grass. The poems form one topic.",
    "yd_34",
    [
        ("Who wrote “Autumn Evening on the River” and “Song of the Flower-Cow,” respectively?", "Liu Dabai and Xu Zhimo", ["Ba Jin and Bing Xin", "Ye Shengtao and Fabre", "Wang Han and Wang Changling"], "Liu Dabai wrote the river poem, and Xu Zhimo wrote the flower-cow poem. Ba Jin wrote the prose piece “Stars.”"),
        ("What does the returning bird do in “Autumn Evening on the River”?", "Though tired, it carries the setting sun home, then tips it into the river with a turn of its wings", ["Drives the tide into the Qiantang River", "Flattens a cockscomb flower in the grass", "Carries a message to the River God"], "The bird is tired, carries the setting sun, and drops it into the river; the reeds also blush for a moment. The cockscomb flower is in “Song of the Flower-Cow.”"),
        ("What happens when the flower-cow sits in the grass in “Song of the Flower-Cow”?", "It flattens a cockscomb flower", ["It drops the setting sun into the river", "It carries wood and stones from the western mountain", "It climbs Tiandu Peak"], "In the first stanza, the cow sits and flattens a flower. The setting sun is in “Autumn Evening on the River,” and the wood and stones belong to Jingwei."),
        ("What happens to the sun while the flower-cow dreams?", "It slips over the green peaks of the western mountain", ["It carries the bird home to its nest", "It stops at the white line on the Qiantang River", "It turns into five-colored stones to repair the sky"], "The fourth stanza says that as the cow dreams, the sun quietly crosses the western peaks. Do not mix the two poems together."),
    ],
)

K(
    # The Chinese characters and example words here are the pronunciation targets being assessed.
    "g4a_duo", "Language Workshop 1: Pronunciations of 朝, 涨, 似, and 还", "Character and Writing Skills", 4, "上", 1, "conceptual",
    "Choose the reading of a polyphonic character from its context instead of using one pronunciation in every word. The oral-communication task “Our Environment” asks students to identify local environmental issues and small actions they can take. The writing task “Recommend a Good Place” asks them to describe a place and explain why it is worth visiting.",
    "sz_34",
    [
        ("In 朝霞 (morning glow), how is 朝 pronounced?", "zhāo", ["cháo", "zhào", "cáo"], "朝霞 and 朝阳 (morning sun) use zhāo. 朝代 and 朝廷 use cháo."),
        ("In 涨潮 (rising tide), how is 涨 pronounced?", "zhǎng", ["zhàng", "zhāng", "zàng"], "涨潮 and 涨水 (rising water) use zhǎng. 头昏脑涨 (dizziness) uses zhàng."),
        ("In 似的 (as if), how is 似 pronounced?", "shì", ["sì", "yǐ", "shī"], "似的 uses shì. 似乎 and 相似 use sì."),
        ("In 还 (to return), as in “return a book to a classmate,” which pronunciation is used?", "huán", ["hái", "huàn", "xuán"], "归还 (return) uses huán. 还有 and 还是 use hái."),
    ],
)

K(
    "g4a_dou", "Reading “Five Peas in a Pod”", "Reading Comprehension", 4, "上", 2, "reasoning",
    "Understand Andersen's fairy tale: the five peas go separate ways, and the one that lands in a crack beneath a mossy windowsill sprouts and gives a sick girl hope.",
    "yd_34",
    [
        ("Who wrote this fairy tale?", "Andersen", ["Ye Zhishan", "Gao Hongbo", "Ba Jin"], "Andersen wrote the story of the five peas. Ye Zhishan wrote “A Clumsy Big Tiger,” and Gao Hongbo wrote “The Spinning Top.”"),
        ("What happens to the five peas after they leave the pod?", "Some are eaten by birds, some land in a ditch or on the street, and one falls into a crack under a window", ["All five fly to the top of Tiandu Peak", "Nüwa turns all five into five-colored stones", "All five are planted at the foot of the Great Wall"], "They go separate ways. The pea that sprouts is the one that lands in a moss-covered crack beneath the windowsill."),
        ("What happens later to the pea that lands in the crack?", "It sprouts and grows leaves; the girl watches it and gradually gets better", ["It is immediately made into a square hat", "A cricket carries it into its home", "It turns into a white line on the Qiantang River"], "The pea shoot grows taller each day. The girl watches it, feels happier, and regains her strength."),
        ("What is the main idea of the story?", "Even an ordinary-looking pea can bring someone hope", ["A pea is useful only if it is made into a hat", "Sick people should stop looking out the window", "Only the magical parts of the five-pea story matter"], "The other peas want to fly out into the wide world, but the one that quietly sprouts is the one that makes a difference."),
    ],
)

K(
    "g4a_ye", "Reading “The Secret of Night Flight”", "Reading Comprehension", 4, "上", 2, "reasoning",
    "Understand how scientists investigate flight: bats navigate at night by emitting ultrasonic waves from their mouths and receiving echoes with their ears, not by using their eyes.",
    "yd_34",
    [
        ("What did the scientists want to find out?", "How bats avoid obstacles while flying at night", ["How bats filled the Eastern Sea", "How a flower-cow dreams in the grass", "Why square hats look better than round ones"], "The text focuses on night flight. Filling the sea, the flower-cow, and the hats belong to other stories."),
        ("What happens when a bat's eyes are covered?", "It can still fly skillfully", ["It immediately hits a rope", "It turns into a pea", "It can fly only during the day"], "Even with its eyes covered, the bat flies well, showing that it does not rely mainly on sight to navigate at night."),
        ("What happens when its ears are plugged or its mouth is covered?", "It bumps into things and cannot fly normally", ["It flies more steadily", "It starts navigating with its feet", "It immediately turns into a radar"], "The bat needs to emit ultrasonic waves and hear the echoes. Without either part, it bumps into things."),
        ("What does the experiment show?", "Bats use their mouths and ears together to navigate with ultrasound", ["Bats cannot sense anything at night", "Jingwei carries ultrasonic waves", "The secret of night flight is a myth"], "The bat sends out sound waves that bounce back from objects and are heard by its ears. This is the scientific explanation."),
    ],
)

K(
    "g4a_fang", "Reading “The Square Hat Shop”", "Reading Comprehension", 4, "上", 2, "reasoning",
    "Understand the fairy tale: a shop sells only square hats; round hats later become popular, but the owner refuses to change and ends up as the only person still wearing one.",
    "yd_34",
    [
        ("What kind of hats does the shop sell at first?", "Square hats", ["Round hats", "Terracotta-warrior helmets", "A tiger's stage costume"], "Long ago, everyone wore square hats, so the shop made only that kind."),
        ("Why do people later switch to round hats?", "They are more comfortable and look better", ["Round hats emit ultrasound at night", "Nüwa makes them from five-colored stones", "Teachers require them for plays"], "Someone makes a round hat, and people find it more suitable than the square kind."),
        ("How does the shop owner respond?", "He insists on selling only square hats and refuses to change", ["He immediately turns the shop into a round-hat shop", "He throws all the hats into the Qiantang River", "He starts selling pea shoots instead"], "He believes only a square hat is a real hat. Everyone else changes, but he does not."),
        ("How does the story end?", "Everyone wears round hats, and the owner is the only one still wearing a square hat", ["Square hats become popular again and all round hats disappear", "The hats in the shop turn into the Great Wall", "The five peas eat all the hats"], "Because he refuses to adapt, he ends up as the shop's only customer."),
    ],
)

K(
    "g4a_tianji", "Reading “Tian Ji's Horse Race”", "Reading Comprehension", 4, "上", 2, "reasoning",
    "Understand how Sun Bin helps Tian Ji beat King Wei of Qi by matching his lower-ranked horse against the king's best, his middle horse against the king's lowest, and his best against the king's middle horse, winning two races out of three.",
    "yd_34",
    [
        ("Who gives Tian Ji the winning strategy?", "Sun Bin", ["King Wei of Qi", "Wang Rong", "Zhou Enlai"], "Sun Bin studies both teams' horses and devises a new order. King Wei is Tian Ji's opponent."),
        ("How does Tian Ji arrange the races to win?", "He matches his lowest horse against the king's best, then his middle horse against the king's lowest, and his best against the king's middle horse", ["He uses his best horse in all three races", "He races the five peas instead", "He asks the square-hat-shop owner to ride for him"], "He deliberately loses the first race, then uses stronger horses against weaker ones to win the next two."),
        ("What is the result of this strategy?", "He wins two of the three races", ["He loses all three", "He wins all three", "The race is canceled"], "He loses the first race and wins the second and third, so he wins overall."),
        ("What does the story show?", "The outcome can change when the same horses are matched differently", ["More horses always mean more wins", "Shouting loudly is enough to win", "A horse race depends on whose hat is squarer"], "The horses are the same; only their order changes. Tian Ji does not buy another team."),
    ],
)

K(
    # Keep the Chinese characters and relevant components: distinguishing their written forms is the assessed content.
    "g4a_xing", "Language Workshop 2: Similar-Looking Characters: 辨, 辩, 辫, 瓣", "Character and Writing Skills", 4, "上", 2, "conceptual",
    "Distinguish 辨, 辩, 辫, and 瓣 by their middle components rather than guessing. The writing task “My Family” asks students to describe one family member and a specific event.",
    "sz_34",
    [
        ("Which character means “to distinguish right from wrong”?", "辨", ["辩", "辫", "瓣"], "辨别 uses 辨, whose middle has a dot and a slant. 辩论 uses the speech component 讠, 辫子 uses the silk component 纟, and 花瓣 uses 瓜."),
        ("Which character is used for “argue a point with someone”?", "辩", ["辨", "辫", "瓣"], "辩论 involves speech, so it uses the speech component 讠."),
        ("Which character completes “a ____ (braid) of hair”?", "辫", ["辨", "辩", "瓣"], "辫子 is related to threads, so its middle contains the silk component 纟."),
        ("Which character completes “flower ____”?", "瓣", ["辨", "辩", "辫"], "花瓣 uses 瓜 in the middle. Do not confuse it with 辩 in 辩论."),
    ],
)

K(
    # Keep the Chinese characters under study: choosing the correct written form is the assessed content.
    "g4a_tong", "Language Workshop 2: Homophones: 在/再 and 做/作", "Character and Writing Skills", 4, "上", 2, "conceptual",
    "Choose 在, 再, 做, or 作 by meaning instead of treating homophones as interchangeable. This topic is grouped with similar-looking characters in Language Workshop 2.",
    "sz_34",
    [
        ("Which Chinese character means “at” or “in” when marking a location?", "在", ["再", "做", "作"], "在 marks a location; 再 means “again.”"),
        ("Which Chinese character means “again”?", "再", ["在", "做", "作"], "Use 再 for a repeated action."),
        ("Which Chinese character is used for “do” in an activity?", "做", ["作", "在", "再"], "Use 做 for doing an activity."),
        ("Which character begins the Chinese word 作业 (homework)?", "作", ["做", "再", "在"], "作 is used in 作业 (homework) and 作文 (composition); 做 is used for actions."),
    ],
)

K(
    # Keep the original Chinese verse and the poem word 真珠: their exact wording is the assessed literary content.
    "g4a_mu", "Poem: “Song by the River at Dusk”", "Classical Poetry and Prose", 4, "上", 3, "conceptual",
    "Memorize Bai Juyi's “Song by the River at Dusk” and distinguish its images of sunset, dark green water, and pearls.",
    "gs_34",
    [
        ("What is the next line after “一道残阳铺水中”?", "半江瑟瑟半江红", ["半江瑟瑟半江蓝", "露似真珠月似弓", "可怜九月初三夜"], "Half the river is dark green and half is lit red by the sunset. The final two lines describe the night of the third day of the ninth lunar month."),
        ("What is the next line after “可怜九月初三夜”?", "露似真珠月似弓", ["半江瑟瑟半江红", "露似珍珠月似弓", "一道残阳铺水中"], "The dew is like pearls and the moon like a bow. The poem uses the word 真珠 for “pearl.”"),
        ("Who wrote “Song by the River at Dusk”?", "Bai Juyi", ["Su Shi", "Lu Meipo", "Li Bai"], "Bai Juyi wrote this poem. Su Shi wrote “Written on the Wall at Xilin Temple,” and Lu Meipo wrote “Snow and Plum Blossoms.”"),
        ("What does 瑟瑟 mean in this poem?", "The part of the river not lit by the sun, which looks dark green", ["The sound of wind in the leaves", "Very hot weather", "A completely dry river"], "In 半江瑟瑟半江红, 瑟瑟 contrasts with 红 and describes a color, not a sound."),
    ],
)

# Keep the original Chinese verse lines: their exact wording is assessed.
K(
    "g4a_ti", "Poem: “Written on the Wall at Xilin Temple”", "Classical Poetry and Prose", 4, "上", 3, "conceptual",
    "Memorize Su Shi's “Written on the Wall at Xilin Temple,” including the exact phrases 只缘 and 各不同.",
    "gs_34",
    [
        ("What is the next line after “横看成岭侧成峰”?", "远近高低各不同", ["远近高低都不同", "远近高低各相同", "不识庐山真面目"], "The mountain looks different from different distances and elevations."),
        ("What is the next line after “不识庐山真面目”?", "只缘身在此山中", ["只因身在此山中", "只缘人在此山中", "不识庐山真面貌"], "The poem says 只缘, not 只因 or 人在."),
        ("Who wrote “Written on the Wall at Xilin Temple”?", "Su Shi", ["Li Bai", "Du Fu", "Bai Juyi"], "Su Shi wrote this poem. Bai Juyi wrote “Song by the River at Dusk.”"),
        ("Why does the poet say he cannot see Mount Lu's true appearance?", "He is inside the mountain and can see only one side", ["Mount Lu has no peaks", "He has never visited Mount Lu", "The mountain is completely covered in snow"], "The view changes from the front, side, near, and far. Being inside the mountain makes it impossible to see the whole picture."),
    ],
)

# Keep the original Chinese verse lines: their exact wording is assessed.
K(
    "g4a_xue", "Poem: “Snow and Plum Blossoms”", "Classical Poetry and Prose", 4, "上", 3, "conceptual",
    "Memorize Lu Meipo's “Snow and Plum Blossoms” and understand that snow and plum blossoms each have a strength: snow is whiter, while plum blossoms are fragrant.",
    "gs_34",
    [
        ("What is the next line after “梅雪争春未肯降”?", "骚人阁笔费评章", ["梅须逊雪三分白", "雪却输梅一段香", "远近高低各不同"], "Plum blossoms and snow both claim to represent spring, so the poet sets down his brush rather than judging too quickly."),
        ("What is the next line after “梅须逊雪三分白”?", "雪却输梅一段香", ["骚人阁笔费评章", "半江瑟瑟半江红", "只缘身在此山中"], "Plum blossoms are not as white as snow, but snow is not as fragrant as plum blossoms. The two lines are paired."),
        ("Who wrote “Snow and Plum Blossoms”?", "Lu Meipo", ["Bai Juyi", "Su Shi", "Wang Changling"], "Lu Meipo wrote this poem. Bai Juyi wrote “Song by the River at Dusk,” and Su Shi wrote “Written on the Wall at Xilin Temple.”"),
        ("Which does the poet consider better, plum blossoms or snow?", "Each has its own strength: snow is whiter, and plum blossoms are fragrant", ["Plum blossoms are better in every way", "Snow is better in every way", "Neither compares with the Qiantang River tide"], "They compete for spring because each has something the other lacks; the poem does not dismiss either one."),
    ],
)

K(
    "g4a_pa", "Reading “The Foot of the Boston Ivy”", "Reading Comprehension", 4, "上", 3, "reasoning",
    "Understand Ye Shengtao's observations of Boston ivy: its feet grow on the stem and cling only after touching a wall.",
    "yd_34",
    [
        ("Where do the Boston ivy's feet grow?", "On the stem", ["At the tips of the leaves", "In the center of the flower", "At the very bottom of the roots; not on the stem"], "Ye Shengtao describes threadlike feet growing on the stem, not on the flowers."),
        ("What happens after a foot touches a wall?", "Its tip becomes a small disk and clings to the wall", ["It immediately withers", "It turns into a leaf", "It pulls away from the wall and stops climbing"], "When a threadlike tip touches a wall, it becomes a small disk and attaches the plant to the wall."),
        ("What happens later to a foot that does not touch a wall?", "It withers", ["It still grows into a small disk", "It produces a flower", "It becomes another plant"], "The text says that a foot that does not touch a wall soon withers. Only the attached feet help the ivy climb."),
        ("How does the author describe the ivy climbing?", "It climbs one foot at a time", ["The whole plant jumps upward at once", "Someone pulls it up by hand", "It grows only sideways along the ground"], "The phrase “one foot at a time” shows how it attaches with one foot and then moves forward."),
    ],
)

K(
    "g4a_zhai", "Reading “The Cricket's Home”", "Reading Comprehension", 4, "上", 3, "reasoning",
    "Understand Fabre's observations of a cricket's home: it is dug by the cricket, with a sloping tunnel, an entrance platform, and a smooth interior.",
    "yd_34",
    [
        ("Who wrote “The Cricket's Home”?", "Fabre", ["Ye Shengtao", "Andersen", "Turgenev"], "Fabre wrote about insects. Ye Shengtao wrote about Boston ivy, and Turgenev wrote about a sparrow."),
        ("How does the cricket's home come to be?", "The cricket digs it out bit by bit", ["It moves into a ready-made hole", "It asks Boston ivy to dig with its feet", "Nüwa builds it from five-colored stones"], "Other insects often take another creature's nest. The cricket does not; it digs its own."),
        ("What features does the home have?", "A sloping tunnel, an entrance, a smooth interior, and a platform outside", ["A white line like the Qiantang River", "One square doorway like the hat shop", "A wall built on the Great Wall's parapets"], "The site is well-drained and sunny, and the interior is carefully finished."),
        ("Why does the author praise this home?", "The small cricket makes a fine, clean home", ["It is longer than the Great Wall", "It emits ultrasound at night", "It is built from terracotta warriors"], "Compared with other insects' homes, this one is especially well made. Ultrasound belongs to bats, and the warriors are from another lesson."),
    ],
)

K(
    # Keep the Chinese vocabulary pairs: choosing among these near-synonyms is the assessed word-level content.
    "g4a_jin", "Language Workshop 3: Distinguishing Near-Synonyms", "Vocabulary", 4, "上", 3, "conceptual",
    "Distinguish near-synonyms that cannot be freely substituted, such as 发现/发明 (discover/invent) and 改正/改进 (correct/improve). The oral task “Care for Your Eyes” asks for eye-care habits. The writing task “Keep an Observation Journal” asks students to record changes observed over several days.",
    "cy_34",
    [
        ("Which word means noticing something that already exists?", "发现 (discover)", ["发明 (invent)", "发生 (happen)", "发挥 (bring into play)"], "Use 发现 for noticing something that already exists; use 发明 for creating something new."),
        ("Which verb means “correct” in “correct a shortcoming”?", "改正 (correct)", ["改进 (improve)", "改善 (make better)", "改变 (change) the weather"], "Use 改正 for a shortcoming; 改进 is commonly used for methods and work."),
        ("Which word completes “He ____ a new tool”?", "发明 (invented)", ["发现 (discovered)", "发生 (happened)", "发音 (pronounced)"], "The tool did not exist before, so it was invented."),
        ("Which pair consists of near-synonyms?", "立刻—马上 (immediately—right away)", ["发现—发明 (discover—invent)", "改正—改进 (correct—improve)", "冷—热 (cold—hot)"], "立刻 and 马上 both mean “immediately.” 发现/发明 and 改正/改进 are not interchangeable, while 冷/热 are opposites."),
    ],
)

K(
    "g4a_pan", "Reading “Pangu Creates the World”", "Reading Comprehension", 4, "上", 4, "reasoning",
    "Understand how Pangu separates the chaotic heavens and earth and later becomes part of the world.",
    "yd_34",
    [
        ("What were the heavens and earth like before Pangu awoke?", "Chaotic, like a huge egg", ["Already divided into mountains and seas", "Like a square-hat shop", "Like the white line of the Qiantang River"], "At that time, the heavens and earth were still mixed together."),
        ("How does Pangu separate the heavens and earth?", "He splits them apart with an axe and holds them up", ["He repairs them with five-colored stones", "He carries wood and stones from the western mountain to fill the sea", "He steals fire for humanity"], "After splitting them apart, he pushes the sky higher and the earth lower each day, growing along with them. Sky repair, filling the sea, and stealing fire belong to other myths."),
        ("What happens after Pangu falls?", "His body becomes the sun, moon, mountains, rivers, plants, and wind", ["He turns into a sparrow", "He races horses against King Wei of Qi", "He moves into a cricket's home"], "His breath becomes wind, his eyes become the sun and moon, and his limbs and body become parts of the earth."),
        ("What is the main subject of this myth?", "How the heavens and earth separated and how the world came to be", ["How bats fly at night", "Why Zhou Enlai studied", "How a girl performed as a tiger"], "The creation of the world and Pangu's transformation explain the world's origins. Night flight and studying appear in other lessons."),
    ],
)

K(
    "g4a_jing", "Reading “Jingwei Fills the Sea”", "Reading Comprehension", 4, "上", 4, "reasoning",
    "Understand the myth in which Jingwei is the bird formed from Emperor Yan's daughter after she drowns, and carries wood and stones from the western mountain to fill the Eastern Sea.",
    "yd_34",
    [
        ("How does Jingwei become a bird?", "She transforms after drowning in the Eastern Sea", ["She was a bird from the beginning", "The Dragon King turns her into one", "She jumps out of a rock on the western mountain"], "Nüwa, Emperor Yan's youngest daughter, drowns in the Eastern Sea and becomes Jingwei."),
        ("What does Jingwei carry to fill the sea?", "Twigs and stones from the western mountain", ["Water from the Eastern Sea", "Her own feathers", "Five-colored stones"], "She carries wood and stones from the western mountain and drops them into the Eastern Sea. Nüwa uses the five-colored stones to repair the sky."),
        ("What is the source of this story?", "The Classic of Mountains and Seas", ["A New Account of the Tales of the World", "The Mencius", "Romance of the Three Kingdoms"], "Jingwei Fills the Sea is a myth from The Classic of Mountains and Seas. Wang Rong's story appears in A New Account of the Tales of the World."),
        ("What does the story praise?", "A great goal and persistence", ["There is no point trying because the sea is stronger than a bird", "Giving up halfway", "Changing goals whenever a problem appears"], "The tiny bird carries wood and stones every day; the story celebrates persistence."),
    ],
)

K(
    "g4a_pu", "Reading “Prometheus”", "Reading Comprehension", 4, "上", 4, "reasoning",
    "Understand how Prometheus takes fire from the sun chariot for humanity, is chained to the Caucasus Mountains and tormented by an eagle, and is later rescued.",
    "yd_34",
    [
        ("What does Prometheus do for humanity?", "He takes fire from the sun chariot", ["He fills the Eastern Sea", "He repairs the collapsed sky", "He splits the chaotic heavens and earth"], "Humanity had no fire, so he risks taking it to people. Creation, sky repair, and filling the sea belong to other myths."),
        ("How does Zeus punish him?", "He chains him to the Caucasus Mountains and sends an eagle to peck at his liver", ["He makes him race horses against Tian Ji", "He makes him wear a square hat", "He makes him dream like a flower-cow in the grass"], "His liver grows back after being pecked, so the torment continues. Horse racing and hats are from other stories."),
        ("Who rescues him later?", "The strongman Heracles kills the eagle with an arrow and breaks the chains", ["Jingwei carries wood and stones to break the lock", "Nüwa repairs the lock with five-colored stones", "Pangu splits the mountain with an axe"], "Heracles passes by, shoots the eagle, and frees him. Jingwei and Nüwa do not rescue him."),
        ("What does the myth mainly praise?", "Being willing to suffer for others", ["There is no need to work once people have fire", "The eagle is the real hero", "Chains matter more than fire"], "Prometheus gives fire to humanity and does not regret it, even though he is punished."),
    ],
)

K(
    "g4a_nv", "Reading “Nüwa Repairs the Sky”", "Reading Comprehension", 4, "上", 4, "reasoning",
    "Understand how Nüwa melts five-colored stones to repair the sky, and distinguish this myth from Jingwei Fills the Sea.",
    "yd_34",
    [
        ("What does Nüwa use to repair the sky after it collapses?", "Melted five-colored stones", ["Twigs from the western mountain", "Plums from the roadside", "Fireflies"], "She gathers five-colored stones, melts them into a paste, and fills the holes in the sky. Jingwei carries wood and stones."),
        ("What else does Nüwa do?", "She kills a destructive black dragon and stops the flood", ["She fills the entire Eastern Sea", "She picks plums with Wang Rong", "She orders Boston ivy to climb into the sky"], "In addition to repairing the sky, she defeats monsters and stops the flood. Jingwei is the one who tries to fill the sea."),
        ("Why are people grateful to Nüwa?", "She restores the sky so that humanity can survive", ["She drives every child out of a garden", "She refuses to let anyone ask questions", "She calls the tide to the Qiantang River"], "Repairing the sky, supporting it, and stopping the flood all help people survive."),
        ("How are “Nüwa Repairs the Sky” and “Jingwei Fills the Sea” different?", "One repairs the sky; the other tries to fill the sea", ["Both fill the Eastern Sea", "Nüwa does both", "Both come from A New Account of the Tales of the World"], "Nüwa repairs the broken sky. Jingwei tries to fill the Eastern Sea where she drowned."),
    ],
)

K(
    "g4a_yd4", "Language Workshop 4: Writing “A Day with ____”", "Writing Skills", 4, "上", 4, "procedural",
    "Imagine spending a day with someone and describe what you do and see together. The person may come from a myth or from everyday life, but the day's events should connect.",
    "xz_34",
    [
        ("Which response best fits “A Day with ____”?", "I spent a day with Nüwa: I helped gather five-colored stones and watched her repair the sky", ["Nüwa.", "A day.", "I named no one and only copied the title"], "Name the person and describe what happened during the day. A name or title alone does not tell a story."),
        ("Imagine spending a day with Pangu. Which sentence describes the events clearly?", "He raised his axe, the chaos split apart, and I watched the sky rise little by little", ["We played all day.", "Pangu was amazing.", "The day went by quickly."], "Raised, split, and rose are visible actions. Simply saying someone was amazing or that time passed quickly does not show what happened."),
        ("Which response goes off topic?", "It describes the length of the Great Wall throughout, but never includes the writer or the person in the blank", ["I spend the day helping Jingwei carry wood and stones", "I help Prometheus carry fire to a village", "I spend the day with my family and connect what we do from morning to evening"], "The topic is “A Day with Someone.” Describing a place without including the writer or the other person does not fit."),
        ("What can you ask yourself when reviewing this piece?", "Can readers tell who I was with and what we did, in order, during the day?", ["Did I reach the required word count?", "Can I turn the myth into an informational article?", "Can I avoid including any people?"], "Both the people and events need to appear. Without a companion or a sequence of events, the topic has not been addressed."),
    ],
)

K(
    "g4a_jiu", "Reading for Pleasure: “Long, Long Ago”", "Reading Comprehension", 4, "上", 4, "conceptual",
    "Read myths and legends about figures such as Pangu, Nüwa, and Jingwei. Treat these “long, long ago” stories as myths, not as records of scientific experiments.",
    "yd_34",
    [
        ("What kind of books are included in “Long, Long Ago”?", "Myths and legends about creation, repairing the sky, filling the sea, and similar stories", ["Only a copy of today's class schedule", "A blank notebook", "A chart of multiplication facts"], "“Long, long ago” is a common opening for myths. A blank notebook and a multiplication chart are not part of this reading."),
        ("What is the main difference between these stories and “The Secret of Night Flight”?", "These are imagined ancient stories, not accounts of scientists conducting experiments", ["Both are only poems to memorize", "Myths cannot include characters", "Informational texts must be about repairing the sky"], "Bats navigating by ultrasound is science. Pangu creating the world and Nüwa repairing the sky are myths. Do not mix the genres."),
        ("After reading a myth, what should you be able to explain?", "Who did what and which ancient event the story describes", ["Only how thick the book is", "Rewrite the ending as a lab report and claim that was the author's meaning", "Only the cover's color"], "Creating the world, stealing fire, and repairing the sky are different events. Turning a myth into an experiment changes the story."),
        ("Which activity does not fit this reading-for-pleasure topic?", "Rewrite every myth as a made-up scientific law and claim that is what the ancients meant", ["Explain the characters and events in a myth", "Record a story that interested you", "Read more stories about figures such as Pangu and Nüwa"], "You may ask your own questions, but do not replace a myth with a conclusion from another subject and claim that was the book's meaning."),
    ],
)

K(
    "g4a_ma", "Reading “The Sparrow”", "Reading Comprehension", 4, "上", 5, "reasoning",
    "Understand how an old sparrow swoops down to protect a chick that has fallen to the ground, causing the hunting dog to retreat.",
    "yd_34",
    [
        ("Where is the sparrow chick?", "It has fallen from the nest to the ground", ["It is still in the nest", "It is standing on the dog's back", "It has flown into the sea"], "The chick has only just grown feathers and falls from the tree in front of the hunting dog."),
        ("What does the old sparrow do?", "It swoops down from the tree and spreads its feathers to protect the chick", ["It escapes with the chick", "It hides behind leaves", "It leads the dog away to play"], "The sparrow bristles its feathers, cries desperately, and puts its body between the dog and its young."),
        ("What does the hunting dog do after seeing the old sparrow?", "It freezes and steps backward", ["It immediately bites both birds", "It follows the sparrow to learn to fly", "It keeps charging forward as if nothing happened"], "The dog does not expect the sparrow to swoop down, so it slowly backs away."),
        ("Why does the narrator quickly call the dog back?", "The old sparrow's powerful protection of its young moves him", ["The dog has already eaten the birds", "The old sparrow asks for help catching insects", "He is afraid the dog cannot swim"], "A powerful force makes the tiny bird swoop down. The narrator calls the dog back because he cannot bear to see the bird hurt."),
    ],
)

K(
    "g4a_du", "Reading “Climbing Tiandu Peak”", "Reading Comprehension", 4, "上", 5, "reasoning",
    "Understand how the narrator and their father climb Tiandu Peak in Huangshan, meet an elderly man about grandfather's age, encourage one another, and reach the top.",
    "yd_34",
    [
        ("Who climbs Tiandu Peak with the narrator?", "Their father", ["Uncle Jin Kui", "Sun Bin", "The old sparrow"], "During the holiday, the father takes the narrator to climb Tiandu Peak in Huangshan. Uncle Jin Kui appears in “The Cow and the Goose.”"),
        ("Who do they meet on the way?", "An elderly man with white hair, about grandfather's age", ["A sparrow chick that fell from its nest", "An unattractive spinning top", "A group of terracotta warriors"], "The elderly man is also climbing. Later, he and the narrator climb together."),
        ("What does the narrator think on seeing the elderly man climb?", "If I can climb at my age and you can climb at yours, I should try even harder to reach the top", ["The mountain is too high, so we should go back immediately", "The elderly man should go back while I take a cable car", "Tiandu Peak should become a square-hat shop"], "Seeing someone else climb gives the narrator strength. The elderly man is similarly encouraged by seeing the child."),
        ("What does the father later say about the child and the elderly man?", "They both draw strength from others", ["Neither should have climbed", "They are competing to see who can become a sparrow first", "They should go fill the Eastern Sea"], "The child watches the elderly man, and the elderly man watches the child; each gives the other courage. That is the lesson of the text."),
    ],
)

K(
    "g4a_xie", "Writing: “A Kaleidoscope of Life”—Describe a Scene or Event", "Writing Skills", 4, "上", 5, "application",
    "Make descriptions of daily scenes and events more vivid with color, sound, action, or comparison. The samples “My Apricots Are Ripe” and “The Wooden Boat” describe ripening fruit and two friends making up after a quarrel; they are writing models, not separate lesson topics. This unit has no language-workshop section.",
    "xz_34",
    [
        ("Which sentence describes a scene at home vividly?", "The apricots ripened; when the wind blew, the golden fruit swayed gently on the branches", ["The apricots ripened.", "There are apricots at my home.", "A kaleidoscope of life."], "The sample “My Apricots Are Ripe” uses color and movement. Simply saying “they ripened” does not help readers picture the scene."),
        ("Two friends quarrel over an object. Which sentence describes what happens in detail?", "After the wooden boat breaks, neither friend speaks to the other; later they repair it together", ["We argued.", "A wooden boat.", "He is bad."], "The sample “The Wooden Boat” describes both the quarrel and how the friends make up. “We argued” alone leaves out what happened."),
        ("How can you make a daily event more specific?", "Describe colors you saw, sounds you heard, or actions that took place", ["Leave only one word in each sentence", "Write that you saw something you never saw", "Switch among three unrelated places in one paragraph"], "Color, sound, and action make an event vivid. Do not claim to have seen something you did not see."),
        ("What are “My Apricots Are Ripe” and “The Wooden Boat” in this writing unit?", "Writing models for describing scenes and events, not separate texts to memorize", ["Poems that must be memorized", "Texts only about numbers, unrelated to daily life", "Two separate lesson topics that must be added"], "One sample describes apricots at home, and the other describes a wooden boat and two friends. They model writing techniques rather than separate lessons."),
    ],
)

K(
    "g4a_cheng", "Reading “The Great Wall”", "Reading Comprehension", 4, "上", 6, "reasoning",
    "Understand the informational text: from a distance the Great Wall resembles a winding dragon, stretching from Shanhai Pass in the east to Jiayu Pass in the west; up close, it is built of stone blocks with parapets, lookout openings, and embrasures.",
    "yd_34",
    [
        ("What does the Great Wall look like from far away?", "A long dragon winding among high mountains", ["A sprouting pea", "A flower-cow dreaming in the grass", "A sparrow swooping down from a tree"], "It is long and follows the contours of the mountains, which makes it look like a dragon. The pea, flower-cow, and sparrow belong to other texts."),
        ("Where are the eastern and western ends of the Great Wall?", "Shanhai Pass in the east and Jiayu Pass in the west", ["The Summer Palace in the east and the Terracotta Army in the west", "Tiandu Peak in the east and the Qiantang River in the west", "Yan'an in the east and Shenyang in the west"], "The text says that the wall runs from Shanhai Pass to Jiayu Pass. The Summer Palace and Terracotta Army appear in later lessons."),
        ("What can you see up close on the wall?", "Huge stone blocks, parapets, lookout openings, and embrasures", ["A passage just wide enough for a small boat", "A tiny skylight", "A square hat"], "Parapets, lookout openings, and embrasures are parts of the wall. The passage and skylight are from Grade 4, Semester 2."),
        ("What is the author mainly conveying about the Great Wall?", "Its grandeur reflects the wisdom and labor of the people who built it", ["Nüwa built it from five-colored stones", "A clumsy big tiger climbed out of it", "It exists only in myths, not in the real world"], "The text moves from a distant view to close-up details, then reflects on the people who built it. The wall is not a myth."),
    ],
)

K(
    "g4a_yi", "Reading “The Summer Palace”", "Reading Comprehension", 4, "上", 6, "reasoning",
    "Follow the route through the Long Corridor, Longevity Hill, and Kunming Lake. This is a full lesson in Grade 4, Semester 1, distinct from the Grade 4, Semester 2, writing sample with the same title.",
    "yd_34",
    [
        ("What route does the lesson follow through the Summer Palace?", "First the Long Corridor, then Longevity Hill, and then Kunming Lake", ["The Terracotta Army first, then Shanhai Pass", "Before the tide arrives, then as it comes in", "The old sparrow swoops down first, then the dog retreats"], "The text moves from place to place: the Long Corridor, the Tower of Buddhist Incense, Kunming Lake, and the Seventeen-Arch Bridge. The warriors, tide, and sparrow are from other lessons."),
        ("What is special about the Long Corridor?", "It is very long, and each beam has different paintings", ["Every beam shows the same square hat", "A row of terracotta warriors stands on it", "It was repaired with five-colored stones"], "Thousands of paintings are all different. Flowers and trees line one side, and Kunming Lake lies on the other."),
        ("What can be seen from Longevity Hill?", "Kunming Lake is still like a mirror, and the Seventeen-Arch Bridge looks like a rainbow", ["A white line of surf on the Qiantang River", "Pangu holding up the heavens and earth", "A spinning top on the ice"], "The Tower of Buddhist Incense is on the hill, with the lake and bridge below. The white line is the tide; the spinning top appears in Unit 7."),
        ("What can both this lesson and “The Great Wall” be used to introduce?", "A Chinese World Heritage Site", ["Two fairy tales by Andersen", "Two frontier poems by Wang Changling", "A sparrow"], "One text describes a wall and the other a garden. Both are places worth introducing to others."),
    ],
)

K(
    "g4a_qin", "Reading “The Terracotta Army”", "Reading Comprehension", 4, "上", 6, "reasoning",
    "Understand the informational text: the terracotta warriors unearthed near Qin Shi Huang's mausoleum are monumental in scale and include generals, soldiers, and many distinct expressions.",
    "yd_34",
    [
        ("Where were the terracotta warriors unearthed?", "Near Qin Shi Huang's mausoleum in Shaanxi", ["By the Qiantang River in Hangzhou", "On Tiandu Peak in Huangshan", "At the Italian parliament"], "They were found in pits near Qin Shi Huang's mausoleum. The tide, Tiandu Peak, and the meeting with Fico belong to other texts."),
        ("What is the overall impression of the terracotta army?", "It is monumental in scale and includes many types of figures", ["There is only one figure, indistinguishable from the others", "Every figure was made by the square-hat shop", "They are all woven from pea shoots"], "Rows upon rows include generals, infantry, cavalry, and other figures."),
        ("What are the figures' expressions like?", "They are all different; some bow slightly, while others gaze intently", ["Every figure has the same face", "They are all asleep with their eyes closed", "They all wag their tails in the grass"], "The text describes varied expressions, like an underground army. The flower-cow wags its tail in a modern poem."),
        ("Why does the author call the terracotta army a precious cultural heritage?", "It reveals an army from more than two thousand years ago and is rare in the world", ["It flies at night using ultrasound", "It is the stars Ba Jin saw at sea", "It is a sparrow that fell from a nest"], "The phrase “unparalleled in the world” refers to its scale and craftsmanship. Ultrasound, stars, and sparrows are from other texts."),
    ],
)

K(
    "g4a_yd6", "Language Workshop 6: Be a Young Tour Guide", "Writing Skills", 4, "上", 6, "procedural",
    "The oral task “Be a Young Tour Guide” asks students to explain a place's features clearly and emphasize key details. The writing task “Chinese World Heritage” can describe the Great Wall, the Summer Palace, or the Terracotta Army in the order they are seen, rather than listing names alone.",
    "xz_34",
    [
        ("Which response clearly explains a place, as a young tour guide should?", "From far away the Great Wall looks like a dragon; up close it is made of stone blocks and stretches from Shanhai Pass to Jiayu Pass", ["This is a place.", "It looks nice.", "The words “world heritage”."], "Its appearance, materials, and endpoints help listeners follow the explanation. Simply saying it looks nice is not enough."),
        ("Which sentence sounds like a tour script for the Summer Palace?", "Please follow me through the Long Corridor, then up Longevity Hill to see Kunming Lake and the 17-arch bridge", ["The Summer Palace.", "I have been there.", "There are things there."], "Name the sights in route order. A place name alone does not tell listeners what they will see."),
        ("What is a suitable approach for writing about “Chinese World Heritage”?", "Choose one site and describe its scale, appearance, and the feature you most want to introduce, in order", ["Copy the names of the Great Wall, Summer Palace, and Terracotta Army on one line and write nothing else", "Switch to writing about a clumsy big tiger", "Write only today's menu"], "The topic is cultural heritage. Listing three names or switching to another lesson does not introduce a site."),
        ("What should a tour guide avoid?", "Not knowing where the place is or having any key details to share", ["State the name, then describe its most distinctive feature", "Guide listeners along the route in the order shown in the text", "Prepare to answer one or two questions people may ask"], "A guide should help others understand. If the guide is unsure, the listeners will be even more confused."),
    ],
)

K(
    "g4a_niu", "Reading “The Cow and the Goose”", "Reading Comprehension", 4, "上", 7, "reasoning",
    "Understand how the narrator is initially afraid of geese, then learns to judge for themself after Uncle Jin Kui catches one.",
    "yd_34",
    [
        ("What did people say about geese at first?", "Geese think people are smaller than they are, so they dare to bully them", ["Geese run away whenever they see people", "Geese are as gentle as cows", "Geese cannot honk"], "People said cows think humans are larger than cows, while geese think humans are smaller than geese."),
        ("What does Uncle Jin Kui do when the goose chases the narrator?", "He grabs the goose and says it is not frightening", ["He runs away with the narrator", "He tells the narrator to apologize to the goose", "He puts the goose in the cowshed and ignores it"], "Uncle Jin Kui catches the goose, and it is no longer so boastful."),
        ("What does the narrator learn from the incident?", "Do not rely only on what others say; judge for yourself", ["Geese really are stronger than people", "Always run away from animals", "Cows and geese are the same animal"], "Although the goose sees people as small, people are actually stronger. The narrator reaches this understanding firsthand."),
        ("Why does the text contrast cows and geese?", "A saying can make people afraid, but seeing the facts can change their minds", ["To explain how to raise geese", "To show where a cow's eyes are", "To say Uncle Jin Kui cannot swim"], "Fear should not depend only on a saying passed along by others."),
    ],
)

K(
    "g4a_lao", "Reading “A Clumsy Big Tiger”", "Reading Comprehension", 4, "上", 7, "reasoning",
    "Understand Ye Zhishan's account of playing a tiger: classmates say a tiger must perform a somersault, the teacher says it is unnecessary, the audience laughs during the performance, and the narrator still wonders why.",
    "yd_34",
    [
        ("Who wrote “A Clumsy Big Tiger,” and what is it about?", "Ye Zhishan; he describes playing a tiger in a class performance", ["Gao Hongbo; he writes about spinning a top", "Ren Rongrong; he writes about Uncle Jin Kui catching a goose", "Turgenev; he writes about an old sparrow protecting its young"], "This is Ye Zhishan's recollection. The spinning top, cow and goose, and sparrow belong to other texts."),
        ("What does a classmate say during rehearsal?", "If he cannot do a tiger's somersault, he cannot play a tiger", ["He acts fiercer than a real tiger", "He should play a pea instead", "He should climb Tiandu Peak"], "A tiger's somersault is a tumbling move. The teacher says the actor does not need it to play a tiger."),
        ("What happens during the actual performance?", "The audience bursts into laughter, and he feels clumsy", ["It is so quiet you can hear a pin drop", "Everyone tells him to fill the sea", "They mistake him for a terracotta warrior"], "He climbs onto the stage and growls. The audience laughs; his face burns, and later he cannot even remember how the performance ended."),
        ("What does he still wonder after the performance?", "Why must an actor do a tiger's somersault to play a tiger, and why did the audience laugh when he did not do one?", ["He was the best actor and should have won a prize", "The laughter means he looked like Sun Bin", "Next time he should play the Great Wall"], "The text ends with these two questions. It does not say that he became an actor."),
    ],
)

K(
    # Keep 冰尜儿 and 人不可貌相，海水不可斗量: these are the assessed Chinese vocabulary and idiom.
    "g4a_tuo", "Reading “The Spinning Top”", "Reading Comprehension", 4, "上", 7, "reasoning",
    "Understand Gao Hongbo's childhood story about spinning tops: his hometown calls one 冰尜儿, and an unattractive little top from his uncle defeats a larger one.",
    "yd_34",
    [
        ("Who wrote “The Spinning Top,” and what is the hometown word for a spinning top?", "Gao Hongbo; 冰尜儿", ["Ye Zhishan; tiger's somersault", "Fabre; a home", "Ba Jin; stars"], "冰尜儿 means a top spun on ice. A tiger's somersault is a move used in a tiger performance."),
        ("What does the top from the uncle look like?", "Turned from wood, round and smooth like a duck egg, but not attractive", ["Glittering gold and bigger than all the others", "A real sparrow", "A square hat"], "Compared with the handsome tops, it looks ordinary. The narrator is initially embarrassed by it."),
        ("What happens when the tops compete?", "The small top knocks over the larger one", ["The large top swallows the small one", "Both tops turn into terracotta warriors", "The teacher bans spinning tops"], "The large top charges in, wobbling, but the little one is persistent enough to knock it over."),
        ("What does the author learn from the experience?", "人不可貌相，海水不可斗量 (Do not judge by appearances; the sea cannot be measured with a dipper)", ["A top must be large to win", "You cannot play unless you can do a tiger's somersault", "Good-looking things are always stronger"], "A plain block of wood, like the ugly duckling, can bring victory. Do not judge only by appearances."),
    ],
)

K(
    "g4a_wang", "Classical Text: “Wang Rong Does Not Pick Roadside Plums”", "Reading Comprehension", 4, "上", 7, "reasoning",
    "Understand why Wang Rong does not pick the roadside plums: the tree is full of fruit beside the road, so the plums must be bitter.",
    "yd_34",
    [
        ("What do the children see on the roadside plum tree?", "Fruit so abundant that the branches bend", ["Not a single plum", "All the plums have been picked", "Peaches growing on the tree"], "The source describes a roadside plum tree with so much fruit that its branches bend."),
        ("Why does Wang Rong stay back while everyone else picks the plums?", "No one has picked the fruit despite its being beside the road, so the plums must be bitter", ["The plums belong to someone else", "He is too short to reach them", "He sees a snake in the tree"], "If the roadside fruit were sweet, passersby would already have picked it."),
        ("What happens when someone picks and tastes one?", "It is indeed bitter", ["It is large and sweet", "It is hollow inside", "It tastes both sweet and sour"], "The original text says that they pick one and find it is indeed bitter. Wang Rong's reasoning is correct."),
        ("What quality does the story show in Wang Rong?", "He is observant and logical", ["He dislikes playing with others", "He is stronger than the other children", "He never eats fruit"], "He infers that the fruit is bitter because so many plums remain beside the road. The story is from A New Account of the Tales of the World, not the story of Sima Guang breaking a jar."),
    ],
)

K(
    # Keep the Chinese conjunctions: selecting the correct pairs is the assessed Chinese grammar content.
    "g4a_guan", "Language Workshop 7: Conjunctions 因为…所以… and 虽然…但是…", "Sentences", 4, "上", 7, "procedural",
    "Pair 因为 with 所以 and 虽然 with 但是 rather than mixing them. The oral task “Comforting Someone” asks students to notice distress and respond reassuringly. The writing task “My Heart Pounded” asks them to describe an event that made their heart race and how they felt.",
    "jz_34",
    [
        ("Which pair completes “____ it is raining today, ____ the sports meet has been rescheduled”?", "因为……所以……", ["因为……但是……", "虽然……所以……", "既……但是……"], "Rain is the cause and rescheduling is the result, so use 因为……所以…… (because…so…)."),
        ("Which pair completes “____ the rain is heavy, ____ he still goes to school”?", "虽然……但是……", ["因为……但是……", "虽然……所以……", "如果……但是……"], "Heavy rain and going to school anyway form a contrast, so use 虽然……但是…… (although…but…)."),
        ("Which sentence uses its conjunctions correctly?", "因为 he woke up late, 所以 he was late.", ["因为 he woke up late, 但是 he was late.", "虽然 he woke up late, 所以 he was late.", "因为 he woke up late, and he was late 所以."], "Use 因为 and 所以 for cause and result. 但是 cannot mark the result after 因为."),
        ("Complete “虽然 the problem was difficult, ____ I still finished it.”", "但是", ["所以", "因为", "如果"], "虽然 pairs with 但是. 所以 pairs with 因为."),
    ],
)

K(
    # Keep 我将无我，不负人民: it is the exact quotation whose meaning is assessed.
    "g4a_wuwo", "Reading “I Will Forget Myself and Live Up to the People”", "Reading Comprehension", 4, "上", 8, "reasoning",
    "Understand President Xi Jinping's 2019 meeting with Italian Chamber of Deputies President Roberto Fico. Fico asks how Xi felt when elected president; Xi replies “我将无我，不负人民” (“I will forget myself and live up to the people”) and uses weightlifters to explain carrying the responsibility of building the country.",
    "yd_34",
    [
        ("Where does the meeting take place, and who is the other person?", "At the Italian Chamber of Deputies, with its president Roberto Fico", ["At Dongguan Model School in Shenyang, with Principal Wei", "At Zaoyuan in Yan'an, with an elderly man", "By the Qiantang River, with a tide watcher"], "On the afternoon of March 22, 2019, Fico asks a question near the end of the meeting. Principal Wei appears in the next lesson."),
        ("What does Fico ask?", "How Xi felt when he was elected President of China", ["How to grow the five peas", "How long the Great Wall is", "Whether a tiger can do a somersault"], "Fico adds that he was very excited to become president of the chamber and wonders how Xi felt about leading such a large country."),
        ("What does “我将无我，不负人民” mean in the text?", "Put personal gain aside, place the country and its people first, and live up to their trust", ["Stop doing all work from then on", "Care only about yourself", "Hide fire from humanity"], "“Forget myself” does not mean having no self; it means not seeking personal gain. “Live up to the people” means accepting responsibility."),
        ("Why does the president compare the work to weightlifting?", "With training, one can lift a heavier barbell; united with the people, he can help build the country", ["Weightlifting is more important than being president", "Fico should become a weightlifter", "The terracotta warriors made the barbells"], "Progressing from 50 kilograms to 250 shows that a heavier responsibility can be carried gradually. Confidence comes from effort and solidarity with the people."),
    ],
)

K(
    # Keep 为中华之崛起而读书: the exact pledge is the assessed content.
    "g4a_jueqi", "Reading “Study for China's Rise”", "Reading Comprehension", 4, "上", 8, "reasoning",
    "Understand how the young Zhou Enlai makes his pledge at Dongguan Model School in Shenyang: 为中华之崛起而读书 (“Study for China's rise”).",
    "yd_34",
    [
        ("Which young person makes this pledge, and at which school?", "Zhou Enlai, at Dongguan Model School in Shenyang", ["Sun Bin, at a horse race in Qi", "Wang Rong, beside a roadside plum tree", "President Xi Jinping, at the Italian Chamber of Deputies"], "At about age twelve, Zhou studies in Shenyang. The Fico meeting is in the previous lesson; the horse race and plums are in earlier texts."),
        ("When Principal Wei asks why they study, what does one student say?", "To become wealthy or help their parents keep accounts", ["To fill the Eastern Sea", "To learn a tiger's somersault", "To win a spinning-top contest"], "These answers focus only on oneself or one's family, and the principal is not satisfied."),
        ("How does Zhou Enlai answer?", "为中华之崛起而读书 (Study for China's rise)", ["Race horses for China's rise", "Forget myself and live up to the people", "Do not judge by appearances"], "He answers clearly and firmly. “Rise” means that the Chinese nation should grow strong. The other quotations come from different lessons."),
        ("Why does he make this pledge?", "He sees Chinese people being mistreated in the foreign concession and feels deeply upset", ["Because the plums are bitter", "Because the spinning top wins", "Because the old sparrow swoops down"], "When China is weak, its people can be bullied. Zhou connects his studies with the future of the country."),
    ],
)

K(
    "g4a_yanan", "Reading “Yan'an, I Search for You”", "Reading Comprehension", 4, "上", 8, "reasoning",
    "Understand Qi Nianzeng's poem: like swallows seeking spring, the speaker seeks Yan'an's ideals and spirit, not a return to old buildings or tools.",
    "yd_34",
    [
        ("What kind of work is “Yan'an, I Search for You,” and what does the poet seek?", "A poem; the poet seeks Yan'an", ["An informational text about the Terracotta Army", "A fairy tale about five peas", "A classical text about Wang Rong"], "Images of returning swallows and growing trees are metaphors in the poem. The warriors, peas, and plums belong to other works."),
        ("Which places associated with Yan'an appear in the poem?", "The Yan River, pear blossoms at Zaoyuan, Nanniwan, and Yangjialing", ["The Qiantang River, Tiandu Peak, and the Summer Palace corridor", "The Italian parliament and a school in Shenyang", "A square-hat shop and a cricket's home"], "The river, pear blossoms, Nanniwan, and Yangjialing are memories of Yan'an. The tide and corridor are from earlier texts."),
        ("What does the poet say about modern high-rises and appliances?", "We can leave old thatched huts but remember cave-dwelling kang beds; discard old ox carts but keep the spirit of Pagoda Hill", ["Once high-rises are built, Yan'an can be forgotten", "Appliances matter more than ideals", "A kang bed should be moved to the Qiantang River"], "Material life changes, but the spirit of Yan'an should remain. “Backbone” refers to that upright spirit."),
        ("What does the poet mainly seek in Yan'an?", "Faith, ideals, warmth, and light", ["An unattractive spinning top", "A square hat", "A pea beneath a window"], "The ending repeats the search for faith, golden ideals, bright spring, and a red sun. The top, hat, and pea are from other poems or stories."),
    ],
)

K(
    # Keep the original Chinese verse lines: memorizing their exact wording is the assessed literary content.
    "g4a_liang", "Poem: “Song of Liangzhou”", "Classical Poetry and Prose", 4, "上", 8, "conceptual",
    "Memorize Wang Han's “Song of Liangzhou” and distinguish it from Wang Changling's “Beyond the Frontier.”",
    "gs_34",
    [
        ("What is the next line after “葡萄美酒夜光杯”?", "欲饮琵琶马上催", ["醉卧沙场君莫笑", "秦时明月汉时关", "生当作人杰"], "Just as the speaker is about to drink, the pipa urges the travelers onward. “醉卧沙场” is a later line, and “秦时明月” is from “Beyond the Frontier.”"),
        ("What is the next line after “醉卧沙场君莫笑”?", "古来征战几人回", ["欲饮琵琶马上催", "不教胡马度阴山", "不肯过江东"], "The speaker asks not to be mocked for lying drunk on the battlefield, since few return from war. The line about Yin Mountain is from “Beyond the Frontier”; the line about crossing the Yangtze is from “Summer Quatrain.”"),
        ("Who wrote “Song of Liangzhou” (beginning “葡萄美酒夜光杯”)?", "Wang Han", ["Wang Changling", "Li Qingzhao", "Lu Meipo"], "Wang Han wrote this poem. Wang Changling wrote “Beyond the Frontier”; sharing a surname does not make them the same poet."),
        ("Which line is not from “Song of Liangzhou”?", "秦时明月汉时关", ["葡萄美酒夜光杯", "欲饮琵琶马上催", "醉卧沙场君莫笑"], "“秦时明月” is from Wang Changling's “Beyond the Frontier,” not this poem."),
    ],
)

K(
    # Keep the exact Chinese verse: recalling the original lines is the assessed content.
    "g4a_chu", "Poem: “Beyond the Frontier”", "Classical Poetry and Prose", 4, "上", 8, "conceptual",
    "Memorize Wang Changling's “Beyond the Frontier” and distinguish it from Wang Han's “Song of Liangzhou.”",
    "gs_34",
    [
        ("What is the next line after “秦时明月汉时关”?", "万里长征人未还", ["但使龙城飞将在", "万里长征人未归", "千里长征人未还"], "The poem first says that those on the long expedition have not returned. It is 万里, not 千里, and 未还, not 未归."),
        ("What is the next line after “但使龙城飞将在”?", "不教胡马度阴山", ["万里长征人未还", "不叫胡马度阴山", "葡萄美酒夜光杯"], "If the flying general were here, the northern cavalry would not cross Yin Mountain. The poem uses 不教, not 不叫. “葡萄美酒” is from “Song of Liangzhou.”"),
        ("Who wrote “Beyond the Frontier”?", "Wang Changling", ["Wang Han", "Li Bai", "Du Fu"], "Wang Changling wrote “Beyond the Frontier.” Wang Han wrote “Song of Liangzhou”; they are different poets despite sharing a surname."),
        ("Which line is not from “Beyond the Frontier”?", "醉卧沙场君莫笑", ["秦时明月汉时关", "万里长征人未还", "不教胡马度阴山"], "“醉卧沙场” is from Wang Han's “Song of Liangzhou,” not “Beyond the Frontier.”"),
    ],
)

K(
    # Keep the exact Chinese verse lines: their wording is the assessed literary content.
    "g4a_jie", "Poem: “Summer Quatrain”", "Classical Poetry and Prose", 4, "上", 8, "conceptual",
    "Memorize Li Qingzhao's “Summer Quatrain,” including its references to outstanding people, heroic spirits, and refusing to cross the Yangtze.",
    "gs_34",
    [
        ("What is the next line after “生当作人杰”?", "死亦为鬼雄", ["至今思项羽", "不肯过江东", "死亦为英雄"], "The poem says to live as an outstanding person and die as a heroic spirit. It uses 鬼雄, not 英雄."),
        ("What is the next line after “至今思项羽”?", "不肯过江东", ["生当作人杰", "不肯过江南", "死亦为鬼雄"], "The poet remembers that Xiang Yu refused to flee across the Yangtze to the east. The poem says 江东, not 江南."),
        ("Who wrote “Summer Quatrain”?", "Li Qingzhao", ["Li Bai", "Li Shangyin", "Wang Changling"], "Li Qingzhao wrote this poem. Li Bai is a different poet; Wang Changling wrote “Beyond the Frontier.”"),
        ("What does the poet praise about Xiang Yu?", "Even after defeat, he refused to flee dishonorably", ["He crossed east of the Yangtze and became emperor again", "He wrote “Beyond the Frontier”", "He got drunk on the battlefield"], "Refusing to cross the Yangtze means he would rather die than flee to survive."),
    ],
)

K(
    "g4a_yd8", "Language Workshop 8: Writing a Letter", "Writing Skills", 4, "上", 8, "procedural",
    "Write a letter with a greeting, body, closing, signature, and date. Explain what you want to tell the recipient rather than writing only “hello.”",
    "xz_34",
    [
        ("How should a letter begin?", "Write the recipient's greeting first, then the body", ["Write your own name first, then the recipient's", "Write only the word “letter”", "Put the date at the top and omit the greeting"], "A greeting tells the recipient who the letter is for."),
        ("Which passage sounds like the body of a letter?", "Last week we visited the Great Wall. From far away it looked like a dragon, and I want to tell you what it was like", ["Hello.", "Writing a letter.", "The words “letter body.”"], "The body needs to say something. “Hello” or a title alone does not tell the recipient what happened."),
        ("What usually belongs at the end of a letter?", "A closing, the writer's name, and the date", ["A shopping list with no writer's name", "A poem to memorize, such as “Beyond the Frontier”", "A repeated greeting"], "A closing, signature, and date tell the recipient who wrote the letter and when."),
        ("Which response does not look like a letter?", "It has no greeting or recipient and only copies the text “The Great Wall”", ["Write to a distant classmate about climbing Tiandu Peak", "Write to a family member about the week's most important event", "Thank a teacher for past encouragement"], "A letter is written to a particular person. Without a recipient, copying a text is not a letter."),
    ],
)

# ---------- Grade 4, Semester 2 ----------
# Topics follow the current unified curriculum's common spring 2026 sequence (6-3 system).
# Split each three-poem set into separate poems; combine the three short poems under “Stars”; combine the two classical texts into one lesson.
# Unit 5 has no language-workshop section; keep “A Visit to _____” separate, and do not create topics for the samples “The Summer Palace” and “The Tianshan Mountains in July.”
# Keep “One Hundred Thousand Whys” as a separate reading-for-pleasure topic; merge oral communication, writing, and integrated-study tasks into their corresponding language-workshop topics.
# Grade 3, Semester 1, already includes an excerpt from “The Secret of the Magic Gourd”; use the new key g4b_bao for this book.

K(
    # Keep the original Chinese verse lines: memorizing their exact wording is the assessed literary content.
    "g4b_tian", "Poem: “Pastoral Scenes Through the Four Seasons”", "Classical Poetry and Prose", 4, "下", 1, "conceptual",
    "Memorize Fan Chengda's poem beginning “昼出耘田” and distinguish the timing of fieldwork and flax spinning.",
    "gs_34",
    [
        ("What is the next line after “昼出耘田夜绩麻”?", "村庄儿女各当家", ["童孙未解供耕织", "也傍桑阴学种瓜", "村庄儿女各回家"], "After the adults work in the fields by day and spin flax at night, the poem describes the village children doing their own tasks."),
        ("What is the next line after “童孙未解供耕织”?", "也傍桑阴学种瓜", ["村庄儿女各当家", "也傍桑荫学种瓜", "也傍桑阴学摘瓜"], "The children do not yet understand farming or weaving, but they learn to plant melons under the mulberry trees. The poem says “plant,” not “pick.”"),
        ("Who wrote “Pastoral Scenes Through the Four Seasons” (beginning “昼出耘田”)?", "Fan Chengda", ["Yang Wanli", "Xin Qiji", "Bai Juyi"], "Fan Chengda wrote this pastoral poem. Yang Wanli wrote “Lodging at Xu's Inn in Xinshi.”"),
        ("What kind of work is described in “昼出耘田夜绩麻”?", "Fieldwork by day and flax spinning at night", ["Flax spinning by day and fieldwork at night", "Sleeping by day and planting melons at night", "Watching others work under the mulberry trees"], "昼 means daytime and 夜 means night. The order of fieldwork and flax spinning matters."),
    ],
)

K(
    # Keep the original Chinese verse lines: exact line recall is the assessed content.
    "g4b_xu", "Poem: “Lodging at Xu's Inn in Xinshi”", "Classical Poetry and Prose", 4, "下", 1, "conceptual",
    "Memorize Yang Wanli's “Lodging at Xu's Inn in Xinshi” and distinguish it from the poem about learning to plant melons.",
    "gs_34",
    [
        ("What is the next line after “篱落疏疏一径深”?", "树头新绿未成阴", ["儿童急走追黄蝶", "树头新绿未成荫", "飞入菜花无处寻"], "The fence is sparse, the path is deep, and the trees have not yet formed shade. The children chasing butterflies appear in the third line."),
        ("What is the next line after “儿童急走追黄蝶”?", "飞入菜花无处寻", ["树头新绿未成阴", "飞入菜花无处找", "也傍桑阴学种瓜"], "The butterfly flies into the yellow flowers and can no longer be found. Learning to plant melons is in Fan Chengda's poem."),
        ("Who wrote “Lodging at Xu's Inn in Xinshi”?", "Yang Wanli", ["Fan Chengda", "Xin Qiji", "Du Fu"], "Yang Wanli wrote the poem about chasing a yellow butterfly. Fan Chengda wrote “Pastoral Scenes Through the Four Seasons.”"),
        ("Why is the yellow butterfly hard to find?", "It flies into flowers of the same yellow color", ["It flies out of the poem", "The children stop chasing it", "The flowers are red and the butterfly is white"], "The butterfly and flowers are the same color, so it disappears from view."),
    ],
)

K(
    # Keep 亡赖 and the original Chinese verse lines: their word meaning and exact wording are assessed.
    "g4b_qing", "Song Lyric: “Village Life”", "Classical Poetry and Prose", 4, "下", 1, "conceptual",
    "Memorize Xin Qiji's “Village Life” and know that 亡赖 means “playful” in the poem.",
    "gs_34",
    [
        ("What is the next line after “最喜小儿亡赖”?", "溪头卧剥莲蓬", ["溪头卧剥莲花", "大儿锄豆溪东", "中儿正织鸡笼"], "The youngest child lies beside the stream, peeling a lotus pod, not a lotus flower."),
        ("What does 亡赖 mean in the song lyric?", "Playful", ["Dishonest", "Friendless", "Pitiful"], "Here 亡赖 means playful or mischievous; it does not mean the child has poor character."),
        ("What are the oldest and middle sons doing?", "The oldest hoes beans; the middle son weaves a chicken coop", ["The oldest weaves a chicken coop; the middle son hoes beans", "Both peel lotus pods", "Both are asleep"], "The oldest hoes beans east of the stream, while the middle son weaves a chicken coop."),
        ("What kind of life does the song lyric describe?", "Farm life", ["Life in a palace", "Life on a battlefield", "Life in a classroom"], "Thatched eaves, hoeing beans, chicken coops, and lotus pods all suggest farm life. Xin Qiji wrote the song."),
    ],
)

K(
    "g4b_xiang", "Reading “Country Life”", "Reading Comprehension", 4, "下", 1, "reasoning",
    "Describe the scenes around a country home, both in front and behind the house and by day and night.",
    "yd_34",
    [
        ("What are the vines in front of the house like?", "They climb onto the eaves, with flowers and vines forming a picture", ["They have all withered", "They grow in the river", "They bloom on a palace wall"], "Green vines and leaves and red and green melons decorate the house."),
        ("How do the flowers bloom?", "In seasonal order", ["All at once on the same day every year", "Only on the nighttime tide", "They never bloom again after flowering once"], "The text says flowers bloom according to the seasons, with different flowers in spring and summer."),
        ("Where do people often spend the evening?", "Eating and chatting in front of the house", ["Swimming in the tide", "Inside a coal mine", "On a ship's mast"], "When the katydids begin to call, people eat and chat in the open space in front of the house."),
        ("How does the author describe country homes?", "They have distinctive, charming scenery", ["They look exactly like city buildings", "They have no life in them", "They are suitable only for listing facts in an informational text"], "The front and back of the house each have their own scenes, day and night, making country homes distinctive and charming."),
    ],
)

K(
    "g4b_chuang", "Reading “The Skylight”", "Reading Comprehension", 4, "下", 1, "reasoning",
    "Understand Mao Dun's account of a skylight: after the windows are closed during a storm, the small skylight comforts the children and lets them imagine a wider world from a raindrop or a star.",
    "yd_34",
    [
        ("Who wrote “The Skylight”?", "Mao Dun", ["Chen Zuiyun", "Liu Zhanqiu", "Ba Jin"], "Mao Dun wrote this text. Chen Zuiyun wrote “Country Life,” and Liu Zhanqiu wrote “Peach-Blossom Water in March.”"),
        ("During a summer shower, what is the children's only comfort when they are kept indoors?", "The small skylight", ["The vines climbing onto the eaves", "The peach-blossom water of March", "The Qiantang River tide"], "When the wooden windows are shut, the room feels like a cave. The children can only look outside through the skylight. The vines appear in “Country Life.”"),
        ("What do the children do when they look through the skylight?", "Imagine a wider world from a raindrop or a star", ["Count the panes and think of nothing else", "Imagine a spider trapped in amber", "Assume there is nothing outside and stop imagining"], "Rain, lightning, and stars can all lead their thoughts far away. Imagination reaches beyond what they can actually see."),
        ("Why does the text say the inventor of the skylight deserves thanks?", "The children can see “something” in “nothing” and “reality” in “the unreal”", ["A skylight can replace every lamp", "Children no longer need to read", "A skylight is used to store melons"], "They may see very little, but what they imagine feels vivid and expansive. That is the text's point."),
    ],
)

K(
    "g4b_tao", "Reading “Peach-Blossom Water in March”", "Reading Comprehension", 4, "下", 1, "reasoning",
    "Understand how Liu Zhanqiu describes March's peach-blossom water as spring's harp and mirror, expressing affection for the spring stream.",
    "yd_34",
    [
        ("Who wrote “Peach-Blossom Water in March”?", "Liu Zhanqiu", ["Mao Dun", "Chen Zuiyun", "Ai Qing"], "Liu Zhanqiu wrote this prose poem. Mao Dun wrote “The Skylight.”"),
        ("What does the text compare March's peach-blossom water to?", "Spring's harp and spring's mirror", ["Amber containing a fly", "A skylight that shows only raindrops", "A wall keeping children outside"], "The sound of the water is like music, and the surface is like a mirror. Amber and the skylight are from other texts."),
        ("What does “harp” mainly describe?", "The sound of flowing water", ["A real harp at the bottom of the river", "Children taking lessons by the river", "Raindrops hitting a skylight"], "The water sometimes sounds louder and sometimes softer, blending with village sounds like a harp."),
        ("What does “mirror” mainly describe?", "The river reflecting swallows, willow branches, and people at the water's edge", ["Dark water that reflects nothing", "The author criticizing the noisy spring stream", "An icy surface people cannot approach"], "The mirror refers to reflections on the water. The text praises the stream rather than complaining about its sound."),
    ],
)

K(
    # Keep the Chinese characters and their components: identifying these forms and meanings is the assessed content.
    "g4b_pian", "Language Workshop 1: Phono-Semantic Characters: 清, 晴, 情, 请", "Character and Writing Skills", 4, "下", 1, "conceptual",
    "Distinguish 清, 晴, 情, and 请 by their semantic components; all share the phonetic component 青. The oral task “Retelling” asks students to convey what they heard without omitting key points or adding their own words. The writing task “My Happy Place” asks them to describe a place and what they do there.",
    "sz_34",
    [
        ("Which character is related to water?", "清 (clear)", ["晴 (sunny)", "情 (feelings)", "请 (please)"], "清 uses the water component 氵. 晴 uses the sun component 日, 情 uses the heart component 忄, and 请 uses the speech component 讠."),
        ("Which Chinese character is used to write “sunny”?", "晴 (sunny)", ["清 (clear)", "情 (feelings)", "请 (please)"], "晴天 (sunny day) is related to the sun, so it uses 日."),
        ("Which character completes the Chinese word 事____ (affair/matter)?", "情 (feelings)", ["清 (clear)", "晴 (sunny)", "请 (please)"], "事情 (affair) and 心情 (mood) relate to feelings, so they use the heart component 忄."),
        ("Which character completes the Chinese word ____客 (invite a guest)?", "请 (please)", ["清 (clear)", "晴 (sunny)", "情 (feelings)"], "请客 means inviting a guest, which uses language; 请 has the speech component 讠."),
    ],
)

K(
    "g4b_huo", "Reading “Amber”", "Reading Comprehension", 4, "下", 2, "reasoning",
    "Understand how the text uses a spider and fly preserved in amber to infer what happened long ago.",
    "yd_34",
    [
        ("What is trapped inside the amber?", "A fly and a spider", ["A fish and a bird", "Two five-colored stones", "A plum"], "The spider is about to pounce on the fly when resin drips down and traps them together."),
        ("Where does the resin come from?", "A pine tree", ["The sea", "The spider's mouth", "A fisherman's boat"], "The sun is hot, and resin seeps from the pine tree, dripping onto the fly and spider."),
        ("Who discovers the piece of amber?", "A fisherman and his son", ["Nüwa", "Ximen Bao", "Wang Rong"], "Long afterward, the child steps on it at the beach, and the fisherman recognizes it as amber."),
        ("How is the story mainly constructed?", "By inferring events from what is preserved in the amber", ["The author witnesses the scene from ten thousand years ago", "The fly writes the story itself", "It has nothing to do with science and is only a myth"], "No one saw the original scene. The text uses the two insects in the amber to infer what might have happened."),
    ],
)

K(
    "g4b_kong", "Reading “Dinosaurs Take to the Sky”", "Reading Comprehension", 4, "下", 2, "reasoning",
    "Understand the informational text: one branch of dinosaurs evolved into birds over a long period, supported by fossil evidence rather than myth.",
    "yd_34",
    [
        ("What is the text mainly explaining?", "One branch of dinosaurs evolved into birds over a long period", ["All dinosaurs flew into the sky on the same day", "Birds and dinosaurs are unrelated", "Nüwa shaped birds from five-colored stones"], "Not every dinosaur could fly. One branch gradually evolved into birds."),
        ("What important evidence do scientists find?", "Dinosaur fossils with feather impressions in western Liaoning", ["Amber containing a fly and a spider", "Moon rocks brought back by Shenzhou 5", "Plums left unpicked beside a road"], "The feather impressions show that some dinosaurs had feathers. The amber contains a spider and a fly."),
        ("Which statement correctly describes the evolution in the text?", "It took a long time as bodies became lighter and forelimbs gradually became wings", ["A Tyrannosaurus grew wings overnight", "Dinosaurs becoming birds is only a story, not science", "Fossils prove that dinosaurs never had feathers"], "The transition to birds took a long time. The text explains it with fossils, not myth."),
        ("What do this text and “Amber” have in common?", "Both infer the distant past from physical evidence that remains", ["Both are about a fly", "Both are poems by Fan Chengda", "Both require memorizing the source text"], "One uses insects in amber and the other uses dinosaur fossils. Both draw inferences from what remains."),
    ],
)

K(
    "g4b_na", "Reading “Nanotechnology Is All Around Us”", "Reading Comprehension", 4, "下", 2, "reasoning",
    "Know that a nanometer is extremely small, that nanotechnology is already used in everyday items such as refrigerators and clothing, and that some applications remain future possibilities.",
    "yd_34",
    [
        ("How long is one nanometer?", "One-billionth of a meter; extremely small", ["As long as a chopstick", "As long as a river", "As long as Earth's diameter"], "The text says one nanometer is one-billionth of a meter. It cannot be seen with the naked eye or an ordinary microscope."),
        ("Why does the text compare a ping-pong ball with Earth?", "To show that a nanometer is unimaginably small", ["To show that a nanometer is larger than Earth", "To say ping-pong balls are made of nanometers", "To say Earth is a refrigerator"], "Putting a one-nanometer ball on a ping-pong ball is compared with putting the ping-pong ball on Earth. The comparison is about smallness, not size."),
        ("Which example is already used in daily life in the text?", "A refrigerator's nanocoating can kill bacteria and remove odors, keeping food and vegetables fresh longer", ["People have already traveled to space on a carbon-nanotube elevator", "Nanotechnology is the feathers on dinosaurs", "Nanotechnology appears only in myths"], "The antibacterial coating is an existing example. A carbon-nanotube elevator is a future possibility, not something already built."),
        ("What does “Nanotechnology Is All Around Us” mean?", "The technology is already used in everyday items such as clothing and refrigerators, so it is close to daily life", ["Nanomaterials are large enough to see easily", "Nanotechnology exists only in laboratories and is never used at home", "It was created by a magic gourd"], "The examples from daily life show that science and technology are not far removed from us."),
    ],
)

K(
    "g4b_qian", "Reading “The Millennium Dream Comes True Today”", "Reading Comprehension", 4, "下", 2, "reasoning",
    "Understand China's dream of spaceflight, from the ancient experiment of Wan Hu to Dong Fang Hong 1 and Yang Liwei's journey into space.",
    "yd_34",
    [
        ("Which ancient attempt at flight is described in the text?", "In the Ming dynasty, Wan Hu strapped rockets to a chair and tried to fly", ["Yang Liwei aboard Shenzhou 5", "Dinosaurs evolving into birds", "Che Yin reading by firefly light"], "Wan Hu is the ancient attempt described in the text. Yang Liwei is a modern astronaut, not an ancient figure."),
        ("What was China's first artificial Earth satellite called?", "Dong Fang Hong 1", ["Shenzhou 5", "The Normandy", "The Mary"], "Dong Fang Hong 1 was a satellite. Shenzhou 5 was a later crewed spacecraft; the Normandy is a ship in another text."),
        ("Who was the first Chinese astronaut to enter space?", "Yang Liwei", ["Wan Hu", "Huang Jiguang", "Halwei"], "Yang Liwei traveled into space aboard Shenzhou 5. Wan Hu's legendary attempt in ancient times did not succeed."),
        ("What does “The Millennium Dream Comes True Today” mean?", "China's long-held dream of spaceflight is realized in the present day", ["The dream lasted only one night", "Spaceflight has still not been achieved", "It is the dream of dinosaurs flying into the sky"], "The text traces the dream from ancient hopes to crewed spaceflight and says it was realized in modern times. Dinosaur evolution is covered in the previous lesson."),
    ],
)

K(
    # Keep the Chinese characters and example words: their pronunciations in context are the assessed content.
    "g4b_cuo", "Language Workshop 2: Pronunciations of 假, 散, 便, and 发", "Character and Writing Skills", 4, "下", 2, "conceptual",
    "Choose the reading of 假, 散, 便, and 发 from the word in which each appears. The oral task “Share the News” asks students to explain when, where, and what happened. The writing task “My Creative Idea” asks them to imagine boldly and explain the idea clearly.",
    "sz_34",
    [
        ("In 放假 (school vacation), how is 假 pronounced?", "jià", ["jiǎ", "jiā", "xià"], "放假 and 假期 use jià. 真假 and 假话 use jiǎ."),
        ("In 散步 (take a walk), how is 散 pronounced?", "sàn", ["sǎn", "sān", "shàn"], "散步 and 分散 use sàn. 散文 and 松散 use sǎn."),
        ("In 便宜 (inexpensive), how is 便 pronounced?", "pián", ["biàn", "piàn", "bián"], "便宜 uses pián. 方便 and 便利 use biàn."),
        ("In 头发 (hair), how is 发 pronounced?", "fà", ["fā", "fǎ", "bà"], "头发 and 理发 use fà. 发现 and 出发 use fā."),
    ],
)

K(
    # Keep the Chinese characters and example words: distinguishing their written forms is the assessed content.
    "g4b_xing", "Language Workshop 2: Similar-Looking Characters: 幕, 慕, 暮, 墓", "Character and Writing Skills", 4, "下", 2, "conceptual",
    "Choose 幕, 慕, 暮, or 墓 by its component. This topic is grouped with the pronunciation of polyphonic characters in Language Workshop 2.",
    "sz_34",
    [
        ("Which character completes 夜____ (night falls)?", "幕", ["慕", "暮", "墓"], "夜幕 means nightfall; 幕 has 巾 (cloth) at the bottom. 羡慕 means envy and has 心 at the bottom."),
        ("Which character completes 羡____ (envy)?", "慕", ["幕", "暮", "墓"], "羡慕 describes a feeling of longing and has 心 at the bottom, not 日."),
        ("Which character completes 日____ (dusk)?", "暮", ["幕", "慕", "墓"], "日暮 means dusk and has 日 at the bottom. 墓 (grave) has 土."),
        ("Which character completes 坟____ (grave)?", "墓", ["暮", "慕", "幕"], "坟墓 is related to earth and has 土 at the bottom. Do not confuse it with 日暮."),
    ],
)

K(
    "g4b_wan", "Reading for Pleasure: “One Hundred Thousand Whys”", "Reading Comprehension", 4, "下", 2, "conceptual",
    "Read popular science to find scientific answers to “why” questions rather than treating myths as explanations.",
    "yd_34",
    [
        ("What kind of books are included in “One Hundred Thousand Whys”?", "Popular science books that answer many kinds of “why” questions", ["Only a copy of today's class schedule", "A blank notebook", "A chart of multiplication facts"], "These books use science to explain questions. A blank notebook and multiplication chart do not fit."),
        ("What is the main difference between this reading and a fairy tale?", "Look for facts and scientific causes rather than how a magic gourd grants wishes", ["Both consist only of poems to memorize", "Popular science books cannot include questions", "Fairy tales must be written as lab reports"], "A magic gourd granting wishes is imaginary. Questions about the sun, dinosaurs, or the body belong in popular science."),
        ("If you want to know “Why can birds fly?”, what is a good way to read?", "Check the contents or questions, then read the part that explains the cause", ["Look only at the cover color and close the book", "Replace the answer with Jingwei carrying wood and stones", "Skip the text and count the pages"], "Reading with a question in mind helps you find the explanation. Replacing a cause with a myth is not the book's answer."),
        ("Which activity does not fit this reading-for-pleasure topic?", "Replace all the scientific explanations with made-up myths and claim that is what the book says", ["Explain one question and the book's answer", "Look up something you do not understand", "Write down a question that interests you"], "You may ask your own questions, but do not change the book's explanation and claim that was the author's meaning."),
    ],
)

K(
    # Keep the original Chinese poem lines: recalling their exact wording is the assessed literary content.
    "g4b_fan", "Three Short Poems: “Stars”", "Reading Comprehension", 4, "下", 3, "reasoning",
    "Read Bing Xin's three poems in “Stars”: No. 71 recalls scenes on her mother's lap, No. 131 addresses the sea, and No. 159 describes seeking her mother's embrace during inner turmoil.",
    "yd_34",
    [
        ("Who wrote all three short poems in “Stars”?", "Bing Xin", ["Ai Qing", "Dai Wangshu", "Sergei Yesenin"], "Ai Qing wrote “Green,” Yesenin wrote “The Birch,” and Dai Wangshu wrote “When the Weather Clears.” These three poems are by Bing Xin."),
        ("In “Stars” No. 71, which three scenes are unforgettable?", "月明的园中，藤萝的叶下，母亲的膝上", ["大海的波涛，星星的光，花的香", "天上的风雨，鸟的巢，母亲的怀", "雪中的白桦，雨后的小径，绿色的风"], "No. 71 recalls being with her mother. The sea appears in No. 131, and seeking an embrace appears in No. 159."),
        ("In “Stars” No. 159, where does the speaker go when inner storms arrive?", "Into her mother's embrace", ["Into a bird's nest", "Into the sea's waves", "Under the wisteria leaves, never to come out"], "When storms come in the sky, birds hide in their nests. When inner storms come, the poet seeks her mother's embrace. These images should not be swapped."),
        ("To whom does “Stars” No. 131 repeatedly address questions?", "The sea: the stars have light, the flowers have fragrance, and the poet's thoughts carry the sea's sound", ["Her mother, about the three remembered scenes", "The birch, about snow outside the window", "A giant who refuses to share a garden"], "“Which star has no light? Which flower has no fragrance?” The questions are addressed to the sea."),
    ],
)

K(
    "g4b_lv", "Reading “Green”", "Reading Comprehension", 4, "下", 3, "reasoning",
    "Understand how Ai Qing depicts green in the rain as abundant and vivid, with all the shades crowding together.",
    "yd_34",
    [
        ("Who wrote “Green”?", "Ai Qing", ["Lao She", "Feng Zikai", "Su Shi"], "Ai Qing wrote this poem. Lao She wrote “Cat”; they are different authors."),
        ("How does the poet imagine that the green appeared?", "As if a bottle of green ink had been overturned", ["Someone painted the sky black with a brush", "Only one leaf is green", "Snow covered all the green"], "The poem imagines an overturned bottle of green ink, with green everywhere."),
        ("What does “all the green gathered together” mean?", "There is so much green that it crowds, overlaps, and interweaves", ["Only one drop of green remains", "Green and red have switched places", "The wind has blown all the green away"], "Crowding, overlapping, and crossing describe the richness and abundance of green."),
        ("What color are the wind and rain in the poem?", "Green", ["Only black", "Only white", "Colorless"], "The wind is green, and the rain is green too. The whole poem centers on green."),
    ],
)

K(
    "g4b_bai", "Reading “The Birch”", "Reading Comprehension", 4, "下", 3, "reasoning",
    "Understand Yesenin's description of the birch outside the window, as if coated in silver frost and draped in snow, expressing admiration throughout.",
    "yd_34",
    [
        ("Who wrote “The Birch”?", "Sergei Yesenin", ["Ai Qing", "Bing Xin", "Dai Wangshu"], "Yesenin wrote this poem. Ai Qing wrote “Green”; the poem's all-over greenery should not be attributed to the birch."),
        ("What does the birch outside the window look like?", "As if coated in silver frost and draped in snow", ["An overturned bottle of green ink", "Peach-blossom water in March", "A tiny skylight"], "The fuzzy branches and snow-embroidered fringe emphasize its whiteness. The green-ink image is from “Green.”"),
        ("What does this poem focus on?", "A birch covered with snow", ["Green crowding together everywhere", "White daisies on a path after rain", "Memories on a mother's lap"], "The title is “The Birch.” Green, daisies, and a mother's lap are from other poems."),
        ("How does the poet feel about the tree?", "Admiring; the tree is described as beautiful", ["Annoyed that it blocks the window", "Eager to cut it down for firewood", "Merely explaining how to sell the wood"], "Silver frost, an embroidered fringe, and tassels are images of praise, not dislike."),
    ],
)

K(
    "g4b_jing", "Reading “When the Weather Clears”", "Reading Comprehension", 4, "下", 3, "reasoning",
    "Understand Dai Wangshu's invitation to walk along a path after rain and observe a white daisy that is no longer timid and a butterfly shaking off raindrops.",
    "yd_34",
    [
        ("Who wrote “When the Weather Clears”?", "Dai Wangshu", ["Sergei Yesenin", "Bing Xin", "Ai Qing"], "Dai Wangshu wrote this poem. Yesenin wrote “The Birch,” and Bing Xin wrote “Stars.”"),
        ("Where does the poet invite the reader to go?", "For a walk along a small path", ["Lie in a boat and squeeze through a narrow passage", "Stay in a closed room and look only through a skylight", "Block gunfire on a battlefield"], "After the weather clears, the poet invites the reader to walk barefoot on the path and see the world after rain."),
        ("What is the little white daisy like in the poem?", "After the rain, it is no longer timid and slowly lifts its head", ["Covered in snow like silver frost", "Withered and never blooming again", "Growing outside a wall built by a giant"], "The daisy is no longer timid after the rain. Silver frost appears in “The Birch.”"),
        ("What is the main difference between this poem and “The Birch”?", "One invites readers to see a path after rain; the other describes a birch in snow", ["They describe the same tree", "Both are Bing Xin's “Stars”", "Both must be read as classical prose"], "One is lively after rain, and the other is snowy and white. They also have different authors."),
    ],
)

K(
    # Keep 严格, 严厉, and 严密: selecting the correct Chinese word for each context is the assessed content.
    "g4b_pei", "Language Workshop 3: Collocations with 严格, 严厉, and 严密", "Vocabulary", 4, "下", 3, "conceptual",
    "Choose 严格, 严厉, or 严密 according to the noun or phrase that follows; they are not interchangeable. The integrated task “Step Through the Gate of Poetry” asks students to collect and read poems and possibly prepare a recitation.",
    "cy_34",
    [
        ("Which Chinese word best describes strict requirements for homework?", "严格 (strict)", ["严厉 (stern)", "严密 (tight)", "严肃 (serious)"], "Use 严格 for requirements and rules. 严厉 usually describes an attitude; 严密 describes an organization or defense."),
        ("Which Chinese word best describes a stern facial expression?", "严厉 (stern)", ["严密 (tight)", "严格 (strict)", "严肃 (serious)"], "Use 严厉 for an expression or attitude. 严密 does not describe a facial expression."),
        ("Which Chinese word best describes a tightly organized defense?", "严密 (tight)", ["严厉 (stern)", "严格 (strict)", "严重 (serious)"], "Use 严密 for a defense or organization with no gaps."),
        ("Which sentence uses the word naturally?", "His tone is 严厉 (stern).", ["His attitude is 严密 (tight).", "The defense is 严厉 (stern).", "The teacher makes 严密 (tight) demands of us."], "Attitudes take 严厉, defenses take 严密, and requirements take 严格. Swapping them makes the collocation incorrect."),
    ],
)

K(
    "g4b_mao", "Reading “Cat”", "Reading Comprehension", 4, "下", 4, "reasoning",
    "Understand Lao She's cat as both eccentric and endearing, with the month-old kitten even more mischievous.",
    "yd_34",
    [
        ("Who wrote “Cat”?", "Lao She", ["Feng Zikai", "Ai Qing", "Lu Xun"], "Lao She wrote this text. Feng Zikai wrote “The White Goose.”"),
        ("Why is the cat described as eccentric?", "It is quiet yet playful, gentle when happy, and silent when unhappy", ["It always has the same expression", "It cannot catch mice", "It is more haughty than a goose"], "The text describes the cat through several pairs of seemingly opposite behaviors."),
        ("What does the month-old kitten like to play with?", "Feathers, balls of string—almost anything", ["Only a fish, nothing else", "Eating with the white goose", "Lying still without moving"], "The kitten is still unsteady on its feet but already treats everything in the yard as a toy."),
        ("What does the author's description of the cat's mischief express?", "Affection for the cat", ["A wish to get rid of it", "Annoyance that it causes trouble at home", "A belief that it should change all its habits"], "The more mischievous the cat seems, the more the author's affection comes through. The detail would not be so warm if the author disliked it."),
    ],
)

K(
    "g4b_muji", "Reading “The Hen”", "Reading Comprehension", 4, "下", 4, "reasoning",
    "Understand Lao She's changing view of a hen: at first he dislikes its noisy, bullying behavior, but later respects its protection of the chicks.",
    "yd_34",
    [
        ("Who wrote “The Hen”?", "Lao She", ["Feng Zikai", "Ai Qing", "Ye Shengtao"], "Lao She also wrote “Cat.” Feng Zikai wrote “The White Goose”; do not confuse the authors."),
        ("How does the author feel about the hen at the beginning?", "He dislikes it", ["He admires it from the first line", "He has never noticed it", "He thinks it is a haughty white goose"], "He first describes its noisy calls and bullying behavior, saying he has always disliked it."),
        ("Why does he later stop disliking the hen?", "As a mother, it is responsible, loving, brave, and hardworking", ["It learns to sleep with its eyes closed like a cat", "It stops calling and is no longer frightening", "It drives all the chicks away"], "Its vigilance, feeding, and protection of the chicks change his view. At the end, he says he cannot dislike it anymore."),
        ("Which was an original reason for disliking the hen, rather than a later behavior?", "Its endless calls and bullying of weaker animals", ["Keeping watch so other animals stay away from the chicks", "Teaching the chicks to find food and avoid danger", "Enduring hardship to protect its young"], "The noisy, bullying behavior appears early as a reason for dislike. Protecting the chicks later earns respect."),
    ],
)

K(
    "g4b_e", "Reading “The White Goose”", "Reading Comprehension", 4, "下", 4, "reasoning",
    "Understand how Feng Zikai conveys the white goose's haughtiness through its calls, gait, and eating habits.",
    "yd_34",
    [
        ("Who wrote “The White Goose”?", "Feng Zikai", ["Lao She", "Ye Shengtao", "Guo Moruo"], "Feng Zikai wrote this text. Lao She wrote “Cat.”"),
        ("What is the white goose's most prominent trait?", "Haughtiness", ["Timidity", "Silence; it never calls", "A light, catlike gait"], "The author says the goose's haughtiness is visible from every angle in its posture."),
        ("What is unusual about how the goose eats?", "It insists on being served and eats in a very methodical way", ["It carries its own food from the kitchen", "It takes one bite and leaves", "It shares a bowl with a dog and never calls"], "It is very dignified while eating and requires someone to stand beside it and serve it."),
        ("What feeling does the author's description of its haughtiness convey?", "He finds it amusing and likes it", ["He plans to sell it", "He is afraid to look at it", "He is only describing a dish"], "Its deliberate eating and stretched neck are amusing, but the writing conveys affection."),
    ],
)

K(
    # Keep the Chinese word pairs: identifying their positive or negative connotations is the assessed vocabulary content.
    "g4b_cai", "Language Workshop 4: Positive and Negative Connotations", "Vocabulary", 4, "下", 4, "conceptual",
    "Distinguish approving and critical words, such as 团结/勾结 (unite/conspire) and 果断/武断 (decisive/arbitrary). The writing task “My Animal Friend” asks students to describe an animal's traits using words with the appropriate connotation.",
    "cy_34",
    [
        ("Which word has a positive connotation?", "团结 (unite)", ["勾结 (conspire)", "阴谋 (plot)", "狡猾 (sly)"], "团结 means joining together for a good purpose. 勾结, 阴谋, and 狡猾 have negative connotations."),
        ("Which word has a negative connotation?", "武断 (arbitrary)", ["果断 (decisive)", "坚强 (strong)", "诚实 (honest)"], "武断 means making a subjective decision without listening to others. 果断 is a positive trait."),
        ("Which word completes “He is very ____ in his work, and his colleagues trust him”?", "果断 (decisive)", ["武断 (arbitrary)", "狡猾 (sly)", "勾结 (conspiring)"], "If colleagues trust him, choose the positive word 果断."),
        ("Which sentence uses a word with the right connotation?", "The students 团结 (unite) to clean the schoolyard.", ["The students 勾结 (conspire) to clean the schoolyard.", "He 坚强 (strongly) deceived everyone.", "He 诚实 (honestly) hid his mistake."], "Cleaning the schoolyard is positive, so use 团结. 勾结 is not appropriate here."),
    ],
)

K(
    "g4b_hai", "Reading “Sunrise at Sea”", "Reading Comprehension", 4, "下", 5, "reasoning",
    "Understand Ba Jin's time-ordered observations of sunrise from a ship: the sun rises slowly, and sunlight rims dark clouds with gold.",
    "yd_34",
    [
        ("Who wrote “Sunrise at Sea”?", "Ba Jin", ["Ye Shengtao", "Lao She", "Feng Jicai"], "Ba Jin wrote this text. Ye Shengtao wrote “A Record of Jinhua's Double Dragon Cave.”"),
        ("Where does the author watch the sunrise?", "On a ship", ["Inside Double Dragon Cave", "At Furong Tower", "In the Giant's Garden"], "He gets up early and waits for the sun on a ship, not inside a cave."),
        ("What is the sunrise like?", "The sun rises slowly from the sea, very red, as if carrying something heavy", ["It jumps to the top of the sky at once", "It stays hidden behind clouds", "It comes through a cave passage"], "The text describes the sun rising little by little, with a lovely red color."),
        ("What does the author see when there are clouds?", "Sunlight rims the dark clouds with gold, a magnificent sight", ["Clouds block the sun forever, so there is no sunrise", "The clouds are green like the wind in Ai Qing's poem", "Two dragons on a cave ceiling"], "A cloudy sunrise can also be spectacular. The dragons appear in another travel essay."),
    ],
)

K(
    "g4b_long", "Reading “A Record of Jinhua's Double Dragon Cave”", "Reading Comprehension", 4, "下", 5, "reasoning",
    "Follow Ye Shengtao's travel essay from the road to the outer cave, narrow passage, and inner cave. Know that travelers must lie on their backs in a small boat to pass through the narrow passage.",
    "yd_34",
    [
        ("Who wrote “A Record of Jinhua's Double Dragon Cave”?", "Ye Shengtao", ["Ba Jin", "Lao She", "Mao Dun"], "Ye Shengtao wrote this travel essay. Ba Jin wrote “Sunrise at Sea.”"),
        ("Which sequence matches the text?", "See the azaleas and tung trees on the way, enter the outer cave, pass through the narrow passage, and reach the inner cave", ["Go to the inner cave first, then return to the sea for sunrise", "Stand at the entrance briefly and finish the essay", "Describe Kunming Lake before the Long Corridor"], "The route proceeds through the road, entrance, outer cave, passage, and inner cave. The Long Corridor and Kunming Lake are in the writing sample “The Summer Palace.”"),
        ("How do people pass through the narrow opening?", "They lie on their backs in a small boat so it can squeeze through", ["Stand on a large ship and watch the sunrise", "Climb onto the roof through a skylight", "Carry a load along a zigzag mountain path"], "The opening is just wide enough for a small boat. Lying down makes the cave ceiling seem close to the nose."),
        ("What can be seen in the inner cave?", "Stalactites and stalagmites; the ceiling resembles a dragon", ["A white line of surf on the Qiantang River", "A red sun rising over the sea", "A hen with a group of chicks"], "The inner cave is very dark; workers need lamps to see the formations. The “two dragons” in the name refer to the shapes on the ceiling."),
    ],
)

K(
    "g4b_ren", "Writing: “A Visit to _____”—Describe What You See and Do", "Writing Skills", 4, "下", 5, "application",
    "Describe sights and actions in the order of a visit. The samples “The Summer Palace” and “The Tianshan Mountains in July” follow routes through corridors, hills, lakes, snowy peaks, streams, and wildflowers. They are models, not separate lesson topics.",
    "xz_34",
    [
        ("Which sentence vividly describes a view during a visit?", "Flowers and trees line one side of the Long Corridor, Kunming Lake lies on the other, and paintings continue one after another", ["I went out.", "The Summer Palace.", "It was nice there."], "The sample “The Summer Palace” follows the sights in order. “I went out” alone does not let readers picture the place."),
        ("Which sentence describes squeezing through a narrow passage in detail?", "I lay on my back in the small boat, pressed my shoulder against its side, and inched forward", ["I entered the cave.", "The cave was narrow.", "I was brave."], "Lying down, pressing against the boat, and inching forward are successive actions. Saying only “entered” or “was brave” leaves out the process."),
        ("What is a good way to write a travel account in order?", "Describe the flowers on the way, then the entrance, then what you see inside the cave", ["Start with arriving home for dinner and leave out the route and cave", "Write only a general feeling and no sights", "Combine three places into “They were all nice”"], "Readers should be able to follow the route. Without describing what was seen, the travel account has not developed beyond its title."),
        ("What are “The Summer Palace” and “The Tianshan Mountains in July” in this writing task?", "Models for describing sights and experiences in order, not separate texts to memorize", ["Poems that must be memorized", "Texts only about numbers, unrelated to scenery", "Texts unrelated to travel writing"], "The Tianshan sample also follows a route past snowy peaks, streams, and wildflowers. Both model a writing technique rather than stand-alone lessons."),
    ],
)

K(
    "g4b_nang", "Two Classical Stories", "Reading Comprehension", 4, "下", 6, "reasoning",
    "Understand “Reading by Firefly Light” and “Grinding an Iron Pestle into a Needle”: Che Yin puts fireflies in a gauze bag for light, and an elderly woman grinds an iron pestle into a needle; both stories emphasize persistence.",
    "yd_34",
    [
        ("Che Yin's family is poor. What does he use for light while reading at night?", "Fireflies in a gauze bag", ["A purchased oil lamp", "A pile of burning wood", "He reads only when the moon is brightest"], "Because the family rarely has oil, he puts fireflies in a thin gauze bag in summer."),
        ("What is a gauze bag in this story?", "A thin, light-colored pouch", ["An iron lamp", "A very thick book", "A neighbor's window"], "The gauze bag is thin and lets light through, so fireflies inside can illuminate the page."),
        ("What is the elderly woman doing in “Grinding an Iron Pestle into a Needle”?", "Grinding an iron rod into a needle", ["Turning a needle into an iron rod", "Giving a needle to a passerby", "Telling someone to stop grinding"], "She says that with enough effort, even an iron pestle can be ground into a needle."),
        ("What do the two stories have in common?", "Persist even when conditions are difficult", ["Do not read if you have no lamp", "An iron rod is already a needle", "Reading requires an expensive lamp"], "One finds a way to light a book, and the other keeps grinding iron into a needle. Both show persistence."),
    ],
)

K(
    # Keep the exact Chinese sentence from the lesson: recalling this quotation is the assessed content.
    "g4b_yu", "Reading “Little Hero Yu Lai”", "Reading Comprehension", 4, "下", 6, "reasoning",
    "Understand the main events in Yu Lai's story: he swims well, protects his schoolbook, and outwits the enemy.",
    "yd_34",
    [
        ("What is Yu Lai especially good at?", "Swimming", ["Climbing", "Horseback riding", "Drawing"], "Yu Lai grows up by the Huixiang River and swims very well."),
        ("What sentence do Yu Lai and the other children read at night school?", "我们是中国人，我们爱自己的祖国", ["Three bowls do not cross the ridge", "The River God still needs a bride", "With enough effort, anything is possible"], "The sentence is written on the blackboard or in the book and stays with Yu Lai. The other sayings come from different texts."),
        ("What does Yu Lai do with his schoolbook when the enemy searches for it?", "He hides and protects it so the enemy cannot find it", ["He hands it to the enemy", "He reads it aloud to the enemy", "He throws it into the stove"], "He hides the book instead of giving it to the enemy."),
        ("After villagers hear gunshots, what do they later discover?", "Yu Lai is alive and surfaces from the water", ["He has handed over the book", "He never knew how to swim", "The book frightens the enemy away"], "People think he has died, but later see his little head emerge from the Huixiang River."),
    ],
)

K(
    "g4b_nan", "Reading “The Boy in Our Family”", "Reading Comprehension", 4, "下", 6, "reasoning",
    "Understand Wang Anyi's portrait of her sister's young son: his interest in food, desire to do things independently, and calmness when facing challenges.",
    "yd_34",
    [
        ("Who wrote “The Boy in Our Family”?", "Wang Anyi", ["Lao She", "Cao Wenxuan", "Guan Hua"], "Wang Anyi wrote this text. Cao Wenxuan wrote “Reed-Flower Shoes,” and Guan Hua wrote “Little Hero Yu Lai.”"),
        ("Who is the “boy” in the title?", "The author's sister's son, a young child", ["Huang Jiguang", "Captain Halwei", "Yu Lai's night-school teacher"], "The boy is not an adult. The author watches him gradually grow into a capable young person."),
        ("Which event shows his desire to be independent?", "He goes shopping and pays by himself without a companion", ["He asks an adult to carry him everywhere", "He leaves every task to a magic gourd", "He hides and never answers when called"], "Shopping and paying on his own show his desire for independence."),
        ("What aspects of the boy does the text mainly describe?", "His interest in food, desire for independence, and calmness under challenge", ["Only his exam scores", "Only how he swims across the Huixiang River", "Only how he weaves reed-flower shoes in the snow"], "Food, independence, and calmness are the main aspects. Swimming belongs to Yu Lai, and selling shoes belongs to Qing Tong."),
    ],
)

K(
    "g4b_luhua", "Reading “Reed-Flower Shoes”", "Reading Comprehension", 4, "下", 6, "reasoning",
    "Understand Cao Wenxuan's story about Qing Tong: he weaves shoes from reed flowers, sells them in town in the snow, and eventually gives away the pair he is wearing.",
    "yd_34",
    [
        ("Who wrote “Reed-Flower Shoes,” and who is the story about?", "Cao Wenxuan; Qing Tong", ["Wang Anyi; her sister's son", "Guan Hua; Yu Lai", "Lao She; a hen"], "The story is from Cao Wenxuan's “Bronze and Sunflower.” Do not confuse Qing Tong with Yu Lai or the boy in the previous lesson."),
        ("What are the shoes woven from?", "Reed flowers", ["Silk", "Steel", "Lotus leaves"], "Reed flowers are light and soft, making warm shoes. They are named in the title."),
        ("Why does he take the shoes to town to sell in the snow?", "To earn money to help his family", ["They are too warm, and he does not want them", "The teacher requires a handmade item", "He wants to give them to the enemy searching the house"], "His family needs money, so he sensibly goes out to sell the shoes in the snow."),
        ("What happens to the last pair he is wearing?", "He takes them off and sells them too, then walks home barefoot in the snow", ["He keeps them for winter and sells none", "Yu Lai hides them in the Huixiang River", "They turn into a ship's lifeboat"], "The buyer wants the pair on his feet. He takes them off and walks home barefoot."),
    ],
)

K(
    # Keep 「」: these Chinese corner quotation marks are the punctuation being assessed; all surrounding prose is translated.
    "g4b_yin", "Language Workshop 6: Dialogue and Quotation Marks", "Sentences", 4, "下", 6, "procedural",
    "Place Chinese quotation marks and punctuation correctly when the dialogue tag comes before or after the spoken words. The oral task “Secrets of Getting Along with Friends” asks how students maintain friendships. The writing task “I Learned to _____” asks them to explain the learning process.",
    "jz_34",
    [
        ("Which sentence places the Chinese quotation marks correctly?", "Mom said:「It's time to do homework.」", ["Mom said: It's time to do homework.", "「Mom said: It's time to do homework.」", "Mom said:「It's time to do homework.」."], "When the dialogue tag comes first, put the spoken words inside the quotation marks, including the final period."),
        ("When the dialogue tag comes after the spoken words, which sentence is correct?", "「I'll help you.」Xiaoming said.", ["「I'll help you.」. Xiaoming said.", "I'll help you.「Xiaoming said.」", "「I'll help you. Xiaoming said.」"], "Put the spoken words first, keep the period inside the quotation marks, and then identify the speaker. Do not put the dialogue tag inside the same pair."),
        ("What is the function of Chinese double quotation marks here?", "To mark the words spoken by a character", ["To replace every period", "To mark only poem titles", "To show that the speaker is loud"], "Here, the quotation marks identify spoken words."),
        ("Which sentence clearly separates two speakers' words?", "Dad asked:「Have you finished your homework?」I replied:「Yes, I have.」", ["Dad asked have you finished your homework I replied yes I have.", "「Dad asked I replied.」", "Have you finished your homework yes I have."], "Give each speaker's words their own pair of quotation marks so readers do not confuse them."),
    ],
)

K(
    # Keep the original Chinese verse lines: memorizing exact wording is the assessed literary content.
    "g4b_fu", "Poem: “Seeing Xin Jian Off at Furong Tower”", "Classical Poetry and Prose", 4, "下", 7, "conceptual",
    "Memorize Wang Changling's “Seeing Xin Jian Off at Furong Tower” and do not mix its lines with “Beyond the Frontier,” by the same poet.",
    "gs_34",
    [
        ("What is the next line after “寒雨连江夜入吴”?", "平明送客楚山孤", ["洛阳亲友如相问", "一片冰心在玉壶", "秦时明月汉时关"], "After a night of cold rain, the poet sees a lonely mountain while seeing off his guest at dawn. “秦时明月” is from “Beyond the Frontier.”"),
        ("What is the next line after “洛阳亲友如相问”?", "一片冰心在玉壶", ["一片冰心在玉湖", "平明送客楚山孤", "不教胡马度阴山"], "The poet asks his friend to tell their Luoyang friends that his heart is as clear as ice in a jade pot. “不教胡马” is also from “Beyond the Frontier.”"),
        ("Who wrote “Seeing Xin Jian Off at Furong Tower”?", "Wang Changling", ["Wang Han", "Li Bai", "Fan Chengda"], "Both this poem and “Beyond the Frontier” are by Wang Changling, but they are different poems. Wang Han wrote “Song of Liangzhou.”"),
        ("What does “一片冰心在玉壶” express?", "The speaker's heart remains pure", ["The jade pot contains real ice, so the guest cannot leave", "He plans to stay in Luoyang", "He wants his friend to bring back wine"], "The ice and jade pot symbolize purity; they do not describe the weather."),
    ],
)

K(
    # Keep the original Chinese verse lines: exact recall is the assessed literary content.
    "g4b_sai", "Poem: “Frontier Song”", "Classical Poetry and Prose", 4, "下", 7, "conceptual",
    "Memorize Lu Lun's “Frontier Song” beginning “月黑雁飞高” and do not mix it with Wang Changling's farewell poem.",
    "gs_34",
    [
        ("What is the next line after “月黑雁飞高”?", "单于夜遁逃", ["大雪满弓刀", "平明送客楚山孤", "只留清气满乾坤"], "The wild geese fly high in the dark because the enemy leader has fled during the night. “大雪满弓刀” is the fourth line."),
        ("What is the next line after “欲将轻骑逐”?", "大雪满弓刀", ["单于夜遁逃", "一片冰心在玉壶", "朵朵花开淡墨痕"], "The general prepares to pursue with light cavalry, and snow has covered the bows and swords. The ice-in-a-jade-pot image is from a farewell poem."),
        ("Who wrote “Frontier Song” (beginning “月黑雁飞高”)?", "Lu Lun", ["Wang Changling", "Wang Mian", "Fan Chengda"], "Lu Lun wrote this poem. Wang Changling wrote “Seeing Xin Jian Off at Furong Tower” and “Beyond the Frontier”; Wang Mian wrote “Ink Plum.”"),
        ("What scene does the poem describe?", "Pursuing an enemy who fled during a snowy night", ["Seeing a friend off to Luoyang at dawn", "Using ink plum blossoms to express one's character", "Children chasing a butterfly into a field of flowers"], "Darkness, escape, light cavalry, bows, and swords describe a nighttime frontier pursuit. The farewell and plum poems are separate works."),
    ],
)

K(
    # Keep the original Chinese verse lines: their exact wording is the assessed literary content.
    "g4b_mei", "Poem: “Ink Plum”", "Classical Poetry and Prose", 4, "下", 7, "conceptual",
    "Memorize Wang Mian's “Ink Plum” and understand that “不要人夸好颜色” rejects praise for appearance in favor of inner character.",
    "gs_34",
    [
        ("What is the next line after “我家洗砚池头树”?", "朵朵花开淡墨痕", ["只留清气满乾坤", "一片冰心在玉壶", "也傍桑阴学种瓜"], "The plum blossoms beside the ink-washing pond are faint like traces of ink. “只留清气” is the fourth line."),
        ("What is the next line after “不要人夸好颜色”?", "只留清气满乾坤", ["朵朵花开淡墨痕", "平明送客楚山孤", "大雪满弓刀"], "The speaker does not need praise for appearance and hopes instead that a refined spirit will remain in the world."),
        ("Who wrote “Ink Plum”?", "Wang Mian", ["Wang Changling", "Lu Lun", "Xin Qiji"], "Wang Mian wrote this poem about plum blossoms. Wang Changling wrote the farewell poem, and Lu Lun wrote the frontier poem."),
        ("What does “只留清气满乾坤” mean?", "Do not seek outward beauty; leave behind a refined character", ["The ink really smells good and deserves praise", "The poet dislikes the plum blossoms for being too pale", "He wants his friend to bring wine back to Luoyang"], "The faint ink-plum color is a metaphor for a person's integrity, not wine or a complaint about the flower."),
    ],
)

K(
    "g4b_huang", "Reading “Huang Jiguang”", "Reading Comprehension", 4, "下", 7, "reasoning",
    "Understand how Huang Jiguang blocks the enemy's gunfire with his chest during the Battle of Triangle Hill.",
    "yd_34",
    [
        ("Which battle does Huang Jiguang fight in?", "The Battle of Triangle Hill", ["The Battle of Langya Mountain", "The Battle of Red Cliffs", "The Meeting at Mianchi"], "The text describes the Battle of Triangle Hill during the Korean War. Langya Mountain appears in another lesson."),
        ("When the advance is blocked, what does he ask the political officer to do?", "Give him the mission of destroying the enemy's firing point", ["Let him retreat first", "Send him back for a schoolbook", "Ask him to deliver a message to the River God"], "Enemy machine-gun fire pins the soldiers down, so he asks to take the mission himself."),
        ("How does he finally complete the mission?", "He blocks the enemy's gun with his chest", ["He bends the gun barrel with a rock", "He asks a plane to bomb the firing point", "He negotiates with the enemy"], "After running out of ammunition and being badly wounded, he throws himself over the gun."),
        ("What does the text mainly show about Huang Jiguang?", "He risks his life for victory in battle", ["He only shouts slogans and takes no action", "He leaves the battle partway through", "He gives the mission to someone else"], "Requesting the mission, crawling forward, and blocking the gun all show his courage and sacrifice."),
    ],
)

K(
    "g4b_nuo", "Reading “The Wreck of the Normandy”", "Reading Comprehension", 4, "下", 7, "reasoning",
    "Understand Victor Hugo's story of Captain Halwei: after the ship is struck, he orders women to leave first and remains on the bridge as the ship sinks.",
    "yd_34",
    [
        ("Who wrote “The Wreck of the Normandy”?", "Victor Hugo", ["Guan Hua", "Feng Jicai", "Ba Jin"], "Victor Hugo wrote this story. Guan Hua wrote “Little Hero Yu Lai,” and Feng Jicai wrote “The Mountain Porters.”"),
        ("Who is in command when the ship is in danger?", "Captain Halwei", ["Huang Jiguang", "Yang Liwei", "Wang Bao"], "Halwei is the captain of the Normandy. Huang Jiguang fights at Triangle Hill, not aboard this ship."),
        ("How does he organize people after the ship is struck?", "He keeps everyone calm, sends women to the lifeboats first, and has the crew stay behind", ["He sends the crew away first and leaves passengers aboard", "He orders everyone to jump into the sea and abandons the ship", "He boards a lifeboat first"], "He maintains order and evacuates passengers first. He does not leave with them."),
        ("What happens to Captain Halwei as the ship sinks?", "He stands on the bridge and sinks with the ship", ["He escapes on the last lifeboat", "He blocks an enemy machine gun with his chest", "He becomes sea foam and searches for a prince"], "He fulfills his duty without making a gesture. Blocking the gun is Huang Jiguang; becoming sea foam is the little mermaid."),
    ],
)

K(
    "g4b_tiao", "Reading “The Mountain Porters”", "Reading Comprehension", 4, "下", 7, "reasoning",
    "Understand Feng Jicai's account of porters on Mount Tai: they walk a zigzag route without stopping and often arrive before tourists.",
    "yd_34",
    [
        ("Who wrote “The Mountain Porters”?", "Feng Jicai", ["Ye Shengtao", "Ba Jin", "Victor Hugo"], "Feng Jicai wrote this text. Ye Shengtao wrote about Double Dragon Cave, and Ba Jin wrote “Sunrise at Sea.”"),
        ("Why do the porters take a zigzag route up the mountain?", "It lets them carry heavy loads, even though the route is longer", ["They have lost their way", "Walking straight up and down is easier, so they avoid it", "The cave passage is just wide enough for a small boat"], "The route resembles a folding ruler and is about twice as long as the tourists' route, but it lets the porters carry heavy goods."),
        ("Compared with tourists, what often happens?", "The porters keep moving and arrive first", ["They always come last", "They must throw away their loads to walk", "They never climb mountains"], "Tourists travel light but stop often. The porters keep going, so they are not slower."),
        ("What does the author do later?", "He paints a porter and hangs the picture by his desk to remind himself to keep moving forward", ["He throws the painting into Double Dragon Cave", "He switches to writing about a goose eating", "He announces that climbing is useless"], "He keeps the painting in view to remember the porter's lesson."),
    ],
)

K(
    "g4b_yd7", "Language Workshop 7: Self-Introduction and Self-Portrait", "Writing Skills", 4, "下", 7, "procedural",
    "A self-introduction should help someone who has never met you remember who you are and what makes you distinctive. The writing task “My Self-Portrait” asks for appearance, personality, or an event that reveals a trait.",
    "xz_34",
    [
        ("Which self-introduction gives a clear picture?", "I'm Lin. I speak quickly, love drawing, and often sketch classmates during breaks", ["I am a student.", "Hello, everyone.", "I'm fine; I have nothing to say."], "A name plus a memorable trait makes an introduction useful. Saying only that you are a student could describe anyone."),
        ("Which sentence sounds like a self-portrait?", "A tuft of hair on my forehead never stays flat, and I smooth it whenever I get nervous", ["I am a person.", "The words “self-portrait.”", "Someone is excellent, but the writer never says who"], "A self-portrait should describe visible traits of the writer. Vague statements and a title alone are not enough."),
        ("How is a written self-portrait different from an oral self-introduction?", "An introduction is spoken; a self-portrait puts personal traits into a written passage", ["Both may include only a name", "A self-portrait cannot be about yourself", "A self-introduction must be a poem"], "One is spoken and the other is written. Writing calls for specific details about appearance and events."),
        ("Which response does not fit this writing task?", "It describes how brave a classmate is throughout, but never includes the writer", ["Describe your gritted teeth while running", "Describe your eyes narrowing when you smile", "Use a small event to show your impatience"], "The self-portrait should focus on the writer. Writing only about someone else becomes a different kind of character essay."),
    ],
)

K(
    "g4b_bao", "Reading “The Secret of the Magic Gourd” (Excerpt)", "Reading Comprehension", 4, "下", 8, "reasoning",
    "Read the Grade 4, Semester 2, excerpt narrated by Wang Bao: his grandmother trades stories for his cooperation, and Zhang San and Li Si get whatever they wish after receiving a magic gourd. When Wang Bao faces a problem, he hopes to get one too. The Grade 3 excerpt shows him getting the gourd; this lesson focuses on the stories and his longing.",
    "yd_34",
    [
        ("Who wrote this Grade 4 excerpt, and who narrates it?", "Zhang Tianyi wrote it; Wang Bao tells his own story in the first person", ["Andersen wrote it; the little mermaid narrates", "Oscar Wilde wrote it; the giant narrates", "Cao Wenxuan wrote it; Qing Tong narrates"], "Zhang Tianyi is the author. Wang Bao says he is a Young Pioneer, not a supernatural being."),
        ("What is the arrangement between the grandmother and the boy?", "Whenever she wants him to do something, she first tells him a story about a magic gourd", ["He cannot eat after a story", "She can tell only the story of grinding an iron pestle into a needle", "He may sell reed-flower shoes only after telling a story"], "He first hears a story before washing his feet or changing clothes. His grandmother tells a different story each time."),
        ("What is special about the magic gourd in the grandmother's stories?", "Whoever gets one can have whatever they wish for", ["It repairs the collapsed sky", "It stops a hen from calling", "It is a pair of reed-flower shoes that can be sold"], "Zhang San meets an immortal, and Li Si visits the Dragon Palace; both get everything they want."),
        ("Why does Wang Bao keep thinking about a magic gourd in the excerpt?", "He gets stuck on arithmetic, his sunflower grows poorly, and he quarrels with a classmate; he hopes a gourd could solve each problem at once", ["He has already switched to someone else's test paper", "He uses a magic gourd to block enemy gunfire", "He grinds the gourd into a needle"], "This lesson is about wishing for a solution. The problems after he gets the gourd appear later in the book, which readers can explore on their own."),
    ],
)

K(
    "g4b_ju", "Reading “The Giant's Garden”", "Reading Comprehension", 4, "下", 8, "reasoning",
    "Understand that winter remains in the garden after the giant builds a wall to keep children out, and spring returns only when the children come back.",
    "yd_34",
    [
        ("What does the giant see when he returns to his garden?", "Children playing inside", ["A flood", "Only a white goose", "Ximen Bao repairing a canal"], "The children used to love playing in the garden. The giant becomes angry when he sees them."),
        ("How does the giant treat the children?", "He drives them out, builds a wall, and posts a “No Entry” sign", ["He invites them to visit every day", "He plants trees with them", "He gives them the garden"], "He forbids the children to enter. After the wall is built, spring leaves the garden too."),
        ("Why is it always winter in the garden?", "After the children are driven out, spring refuses to return", ["The giant locks the sun indoors", "The north wind tears up the calendar", "Flowers never bloom"], "The peach trees refuse to flower, and snow and frost remain. A tree blossoms only after a child slips in."),
        ("What is the story's message?", "Selfishness leaves a place cold; sharing brings spring", ["Building walls is the best form of gardening", "Winter is better for growing flowers than spring", "Children should not look at flowers"], "The giant finally tears down the wall, and the garden becomes a playground for the children again."),
    ],
)

K(
    "g4b_hainv", "Reading “The Little Mermaid”", "Reading Comprehension", 4, "下", 8, "reasoning",
    "Understand Andersen's story of the little mermaid: she rescues a prince, trades her voice to a witch for legs, and ultimately spares the prince and becomes sea foam.",
    "yd_34",
    [
        ("Who wrote “The Little Mermaid”?", "Andersen", ["Oscar Wilde", "Zhang Tianyi", "Victor Hugo"], "Andersen wrote this fairy tale. Oscar Wilde wrote “The Giant's Garden,” and Zhang Tianyi wrote “The Secret of the Magic Gourd.”"),
        ("Whom does the little mermaid rescue?", "A prince who falls into the sea", ["A child driven out by a giant", "Captain Halwei", "A mountain porter"], "The prince falls into the sea, and the little mermaid carries him to the surface. The captain and porter are in other stories."),
        ("What does she give the witch in exchange for legs?", "Her beautiful voice; afterward every step feels like walking on knives", ["A pair of reed-flower shoes", "Her chest to block gunfire", "A piece of amber containing a spider"], "She loses her voice and walking hurts terribly, but she still wants to become human and stay near the prince."),
        ("What does she do after the prince is with someone else?", "She does not harm him and becomes sea foam", ["She turns the prince into a giant", "She builds a wall to keep him out", "She leaves the sea in a magic gourd"], "Her sisters give her a knife, but she does not stab the prince and chooses to spare him."),
    ],
)

K(
    "g4b_yd8", "Language Workshop 8: Reimagining a Story", "Writing Skills", 4, "下", 8, "procedural",
    "A reimagined story borrows familiar characters for new events without reversing the original message or copying the text unchanged.",
    "xz_34",
    [
        ("Which response is a reimagined story?", "After the giant removes the wall, another child is afraid to enter, so the giant personally leads the child into the garden", ["Copy “The Giant's Garden” from beginning to end", "Write a shopping list unrelated to the giant or children", "Write only the title “Reimagining a Story”"], "The character is still the giant, but the event is new. Copying the original or changing to an unrelated subject is not a reimagining."),
        ("In a reimagining of “Reading by Firefly Light,” which choice reverses the character?", "Che Yin finds reading too tiring, releases the fireflies, and never reads again", ["One night his bag tears, so he finds another way to keep reading", "He teaches a neighbor who cannot afford lamp oil to use fireflies", "He keeps reading despite difficult conditions"], "A reimagining can add a new obstacle, but it should not turn him into someone who gives up reading."),
        ("Which statement correctly distinguishes reimagining from copying?", "Reimagining borrows familiar characters for a new plot; copying reproduces the text", ["A reimagining must replace every character with a stranger", "A copied story may change the ending and claim that was the author's meaning", "A reimagining cannot use any original character names"], "The characters are familiar to readers, but the events should be new. A character should not suddenly become someone else."),
        ("What can you ask yourself when reviewing a reimagined story?", "Without seeing the names, can readers recognize the character and tell what new event happens?", ["How many commas are there?", "Can I remove all new events and keep only the original sentences?", "Does it matter what the characters do as long as it is long enough?"], "Readers should recognize the character and notice what has been reimagined. If only the original lines remain, it is still a copy."),
    ],
)
