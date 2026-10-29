# -*- coding: utf-8 -*-
"""Grade 2, both volumes. Volume 1 follows the fall 2025 revised national curriculum (six-three system); Volume 2 follows the spring 2026 revised curriculum and excludes the retired lesson “The Fairy Tale on the Beach”."""
from zh_lib import K

# ---------- Grade 2, Volume 1 ----------
# Fall 2025 revised contents. Unit 3 includes “Rainbow,” “Going to Grandma's House,” and “The Child Who Counted the Stars”;
# Unit 7 poems are “Snow on the River” and “Song of the Chile People”; “Night Lodging at the Mountain Temple” is in Language Workshop 7;
# Unit 8 includes “Compliments,” “The Paper Boat and the Kite,” and “The Happy Stream.”
# Antonyms, radicals, sentence completion, and picture-based writing keep their original keys and are assigned to the corresponding workshops.

# Domain values are machine tokens: zh_lib.K validates them against CRIT, so keep them unchanged.
# Retain Chinese only when a specific character, word, or line is assessed; zh_lib.K stores it as question content.

K(
    "g2a_ke", "Reading: The Little Tadpole Finds Its Mother", "阅读理解", 2, "First semester", 1, "reasoning",
    "Explain in order whom the tadpoles ask first and how they eventually find their mother, the frog.",
    "yd_12",
    [
        ("What does Aunt Carp say the tadpoles' mother looks like?", "Four legs and a wide mouth", ["A long neck and a pointed mouth", "No legs and a round shell", "Two large wings"], "Aunt Carp says their mother has four legs and a wide mouth. Only the turtle has a shell."),
        ("Why do the tadpoles call the turtle “Mother” when they see it?", "It has four legs, so they think it must be their mother", ["It wears a green coat", "It has two large eyes on top of its head", "It says it is a frog"], "They remember only the four legs and call the first turtle they see “Mother.” The turtle tells them it is not their mother."),
        ("What else does their mother look like?", "Large eyes, a green coat, and a white belly", ["A pointed mouth and yellow feathers", "A hard shell and a short tail", "Long whiskers and black wings"], "The turtle tells them that their mother has two large eyes on her head and wears a green coat. The frog also has a snowy-white belly."),
        ("How do the tadpoles' legs and tail change as they become frogs?", "The hind legs grow first, then the front legs, and the tail disappears", ["All four legs grow at once, and the tail remains", "The front legs grow first, and the tail gets longer", "They never grow legs"], "They first grow two hind legs, then two front legs. Their tails gradually disappear, and they become frogs."),
    ],
)

K(
    "g2a_shenme", "Reading: What Am I?", "阅读理解", 2, "First semester", 1, "reasoning",
    "Understand that the speaker is water, which can become clouds, rain, hail, or snow and can be gentle or fierce.",
    "yd_12",
    [
        ("What is the speaker in the story?", "Water", ["Wind", "The sun", "A stone"], "The sun turns water into vapor, then into clouds, rain, hail, and snow. The final line reveals that the speaker is water."),
        ("What do people call the speaker while it floats in the sky?", "A cloud", ["Hail", "Snow", "A machine"], "The cloud wears white or black, then a red cloak at sunrise or sunset. It becomes rain only when it falls."),
        ("What does the speaker do when it is gentle?", "Irrigates fields and powers machines", ["Floods crops and destroys homes", "Attaches seeds to animals", "Hides the sea"], "Irrigating fields and powering machines are helpful. Flooding crops and destroying homes are things it does when fierce."),
        ("What happens when the speaker is fierce?", "It floods crops and destroys homes", ["It sleeps in a pond and strolls in a stream", "It puts on a red cloak", "It carries seeds for people"], "The story calls flooding crops and destroying homes harmful deeds. Sleeping and strolling are ordinary things it does."),
    ],
)

K(
    "g2a_zhiwu", "Reading: Plant Mothers Have Their Ways", "阅读理解", 2, "First semester", 1, "reasoning",
    "Understand that dandelions, cockleburs, and peas disperse their seeds in different ways.",
    "yd_12",
    [
        ("How do dandelions disperse their seeds?", "By wind", ["The sun bursts their pods open", "On animals' fur", "They crawl into the soil"], "A breeze carries the dandelion seeds away."),
        ("How do cockleburs leave the parent plant?", "Their spiky shells cling to animals' fur", ["The wind blows them into the sky", "Their pods split open in the sun", "They float away down a river"], "Cockleburs are covered in prickles. When an animal brushes against one, it clings to the animal's fur."),
        ("How do pea seeds get dispersed?", "The sun dries the pods, which burst and scatter the seeds", ["They cling to birds", "They drift slowly on the wind", "An animal bites the pods open"], "The peas grow inside pods. After the sun dries them, the pods pop open."),
        ("What does the story encourage us to do?", "Observe carefully; plants have many ways to disperse seeds", ["Pick all the seeds", "Remember only dandelions", "Ignore the plants around us"], "The story says plants have many ways to disperse seeds and encourages careful observation."),
    ],
)

K(
    "g2a_yd1", "Language Workshop 1: Interesting Animals", "习作基础", 2, "First semester", 1, "procedural",
    "Describe an interesting feature of an animal. Memorize Wang Anshi's poem “Plum Blossoms.”",
    "xz_12",
    [
        ("Which statement clearly introduces an interesting animal to classmates?", "Giraffes have long necks and can reach leaves high in trees.", ["I like it.", "Animals are nice.", "It's interesting, but I'll keep the rest secret."], "An introduction should name the animal and explain what is interesting about it. Saying only “I like it” or “It's interesting” gives no details."),
        ("Which sentence does not describe an interesting feature of a penguin?", "It is an animal.", ["It waddles as if dressed in black and white.", "When it gets hot, it often sticks out its tongue to cool down.", "It stands in the snow and stretches its neck."], "“It is an animal” gives no details. Its walk, cooling behavior, and posture are interesting features."),
        ("What is the next line after “墙角数枝梅”?", "凌寒独自开", ["为有暗香来", "遥知不是雪", "二月春风似剪刀"], "The plum blossoms bloom alone in the bitter cold. The other two lines come later in the poem; the last option is from a different poem."),
        ("Who wrote “Plum Blossoms,” and why does the speaker know the flowers are not snow?", "Wang Anshi; a faint fragrance drifts over", ["Li Bai; the petals are flying", "Wang Zhihuan; there is snow in the corner", "Liu Zongyuan; the plum blossoms will not open"], "Wang Anshi wrote the poem. The speaker recognizes the blossoms by their faint fragrance."),
    ],
)

K(
    "g2a_du", "Happy Reading: Explore Fairy Tales", "阅读理解", 2, "First semester", 1, "conceptual",
    "Recognize that fairy tales often include talking characters and imagined events, and be ready to retell a favorite story.",
    "yd_12",
    [
        ("What do fairy tales often include?", "Talking animals or imagined adventures", ["A copy of the day's class schedule", "A blank sheet of paper", "A bill with only numbers"], "Fairy tales use imagination to tell stories. A schedule, blank page, or bill is not a fairy tale."),
        ("What can you do after reading a fairy tale you enjoy?", "Tell it to someone else or read it again", ["Close the book and never touch it again", "Change the ending and claim it is the original story", "Remember only the cover's color"], "Reading fairy tales means reading more and sharing stories. Changing the content means it is no longer the original story."),
        ("What is a helpful way to read a fairy tale?", "Think as you read: who did what, and what happened next?", ["Throw away the whole book if you see an unfamiliar word", "Tear the pages out backward from the last one", "Look only at page numbers, not sentences"], "Thinking about what the characters do helps you understand the story."),
        ("Which book belongs in a collection of fairy tales?", "A storybook about an animal's adventures", ["A blank workbook", "A chart of multiplication facts", "A bus ticket"], "This section is for books with stories, not blank workbooks, multiplication charts, or tickets."),
    ],
)

K(
    "g2a_chang", "Character Study: Scene Song", "识字写字", 2, "First semester", 2, "conceptual",
    "Read “Scene Song” and match measure words with a sailboat, warship, harbor, and stone bridge.",
    "sz_12",
    [
        ("Which phrase pairs with “一艘军舰” in the poem?", "一处港湾", ["一条帆船", "一方鱼塘", "一群飞鸟"], "The poem pairs a gull with a sailboat and a warship with a harbor. A sailboat is not paired with the warship."),
        ("Which phrase pairs with “一只海鸥” in the poem?", "一条帆船", ["一处港湾", "一片沙滩", "一座石桥"], "The gull and sailboat appear together. The harbor pairs with the warship, and the stone bridge with the stream."),
        ("Which measure word comes before “石桥” in the poem?", "一座", ["一孔", "一条", "一方"], "The poem says “一道小溪，一座石桥.” The phrase “一方” is used for a fishpond."),
        ("Which pair uses the same measure words as the poem?", "一丛翠竹，一群飞鸟", ["一孔石桥，一条海鸥", "一艘翠竹，一只港湾", "一片沙滩，一条军舰"], "A cluster of bamboo uses 丛, and a flock of birds uses 群. Boats and warships use 艘."),
    ],
)

K(
    "g2a_shu", "Character Study: Tree Song", "识字写字", 2, "First semester", 2, "conceptual",
    "Read “Tree Song” and learn the features of “杨树” (poplar), “榕树” (banyan), “梧桐” (Chinese parasol tree), “枫树” (maple), and “松柏” (pines and cypresses).",
    "sz_12",
    [
        ("What do the leaves of “梧桐” resemble?", "手掌 (a palm)", ["一把伞 (an umbrella)", "一根针 (a needle)", "圆圆的饼 (a round cake)"], "The story compares the leaves of 梧桐 to palms."),
        ("Which tree's leaves turn red in autumn?", "枫树 (maple)", ["松柏 (pines and cypresses)", "榕树 (banyan)", "银杏水杉 (ginkgo and metasequoia)"], "Maple leaves turn red in autumn. 松柏 stay green all year."),
        ("Which trees stay green throughout the year?", "松柏 (pines and cypresses)", ["枫树 (maple)", "梧桐 (Chinese parasol tree)", "木棉 (kapok)"], "松柏 stay green all year; 枫树 leaves turn red in autumn."),
        ("What does “木棉喜暖在南方，桦树耐寒守北疆” mean?", "Different trees suit different places", ["Both trees grow in the north", "Kapok cannot tolerate heat", "Birch grows only in the south"], "Kapok prefers the warm south, while birch can withstand the cold in the north."),
    ],
)

K(
    "g2a_pai", "Character Study: The Clapping Song", "识字写字", 2, "First semester", 2, "conceptual",
    "Read “The Clapping Song” and match its verses about peacocks, geese, pandas, and protecting animals.",
    "sz_12",
    [
        ("What follows “你拍二，我拍二” in the song?", "孔雀锦鸡是伙伴", ["竹林熊猫在嬉戏", "天空雁群会写字", "保护动物是大事"], "Verse 2 names the peacock and golden pheasant. Pandas appear in verse 7, and geese in verse 4."),
        ("Which verse contains “天空雁群会写字”?", "你拍四，我拍四", ["你拍一，我拍一", "你拍六，我拍六", "你拍十，我拍十"], "Verse 4 mentions geese. Verse 6 names songbirds, and verse 10 is about protecting animals."),
        ("What are the pandas doing in the song?", "在竹林里嬉戏", ["在云彩间飞翔", "在丛林里当猛虎", "在海上开军舰"], "The song says the pandas play in the bamboo grove. Eagles are the ones that fly."),
        ("How does the song say people should treat animals?", "保护动物是大事，人和动物是朋友", ["把动物都关进笼子", "只保护锦鸡一种", "动物没有家也没关系"], "The final verses say people and animals are friends, all animals have homes, and protecting animals is important."),
    ],
)

K(
    "g2a_siji", "Character Study: The Farmer's Four Seasons", "识字写字", 2, "First semester", 2, "conceptual",
    "Read “The Farmer's Four Seasons” and distinguish the seasonal scenery and farm work.",
    "sz_12",
    [
        ("What springtime scenes does the poem describe?", "Spring wind blows; flowers bloom, grass grows, butterflies fly, and the wheat seedlings and mulberry leaves thrive", ["Rice is spread out to dry and the grain shines like gold", "The snow has cleared and people put on new padded coats", "People pick mulberry leaves, raise silkworms, and transplant rice"], "Spring brings blossoms, growing grass, and butterflies. Rice harvest is in autumn; tending silkworms and transplanting rice are summer tasks."),
        ("Which season is described by “早起勤耕作，归来戴月光”?", "Summer", ["Spring", "Autumn", "Winter"], "Summer is busy with farm work, so people leave early and return by moonlight."),
        ("In autumn, what is the grain compared to in “稻上场，谷像黄金粒粒香,” and how do the farmers feel?", "Gold; they are physically tired but joyful", ["Snowflakes; they are frightened", "Willow leaves; they stay indoors", "Padded coats; they stop harvesting"], "The poem compares the harvested grain to fragrant golden kernels and contrasts hard work with the farmers' happiness."),
        ("After the year's farm work is done in winter, what are people like?", "They put on new padded coats after the snow clears and smile happily", ["They are still transplanting rice and cannot rest", "Flowers have just bloomed and butterflies are flying", "The wheat seedlings are tender and the mulberry leaves are lush"], "In winter, the snow clears and new padded coats keep everyone warm. The year's farm work is done, and people are smiling."),
    ],
)

K(
    "g2a_fan", "Language Workshop 2: Antonyms", "词语", 2, "First semester", 2, "conceptual",
    "Identify common antonyms and distinguish them from words with similar meanings.",
    "cy_12",
    [
        ("When “高” describes a person's height, what is its antonym?", "矮", ["低一点", "长", "大"], "“高” and “矮” are opposites. “长” is the opposite of “短,” and “大” is the opposite of “小.”"),
        ("What is the antonym of “早”?", "晚", ["迟些", "快", "远"], "“早” and “晚” are opposites. “快” is the opposite of “慢.”"),
        ("What is the antonym of “笑”?", "哭", ["高兴", "喊", "唱"], "“笑” and “哭” are opposites. “高兴” is similar in meaning to “笑,” so it is not an antonym."),
        ("Which pair contains antonyms?", "冷—热", ["冷—凉", "开—张开", "看—瞧"], "“冷” and “热” are opposites. “凉” is similar to “冷,” while “看” and “瞧” are synonyms."),
    ],
)

K(
    "g2a_pian", "Language Workshop 2: Grouping by Radicals", "识字写字", 2, "First semester", 2, "conceptual",
    "Group characters by the wood, grass, water, and foot radicals.",
    "sz_12",
    [
        ("Which radical do “树、林、枝” share?", "木字旁", ["草字头", "三点水", "口字旁"], "The characters “树,” “林,” and “枝” all relate to trees and share the wood radical."),
        ("Which radical do “花、草、苗” share?", "草字头", ["木字旁", "竹字头", "宝盖头"], "The characters “花,” “草,” and “苗” all relate to plants and share the grass radical."),
        ("Which radical group do “河、湖、海” belong to?", "三点水", ["火字旁", "提手旁", "女字旁"], "The characters “河,” “湖,” and “海” all relate to water and use the water radical."),
        ("Which radical do “跑、跳、跃” share?", "足字旁", ["走之底", "提手旁", "单人旁"], "The characters “跑,” “跳,” and “跃” all describe actions involving the feet and share the foot radical."),
    ],
)

K(
    "g2a_caihong", "Reading: Rainbow", "阅读理解", 2, "First semester", 3, "reasoning",
    "Understand that the rainbow after the rain is imagined as a bridge and that the narrator wants to help Dad, Mom, and an older brother.",
    "yd_12",
    [
        ("What is the beautiful bridge in the sky?", "The rainbow that appears after the rain", ["A swing in the tree by the door", "Mom's mirror", "Dad's water jug"], "After the rain, a beautiful bridge appears in the sky. It is a rainbow, not a bridge people can actually walk across."),
        ("How does the narrator want to help Dad?", "Sprinkle water from the bridge so it rains and Dad does not have to carry water to the fields", ["Hang the swing from the bridge", "Give Dad the mirror so he can comb his hair", "Tell Dad to swim in the sea"], "The narrator imagines carrying a watering jug onto the rainbow and making it rain."),
        ("What does the narrator imagine becoming by carrying Mom's mirror onto the bridge?", "An extra moon in the sky, shining while Mom combs her hair", ["A sailboat", "A motionless stone flower", "A blackboard"], "The round mirror looks like a moon. The narrator imagines using it to shine on Mom as she combs her hair."),
        ("What does the story compare the fluttering flower-print skirt to?", "A colorful cloud", ["A water jug", "A stream", "A rice field"], "The skirt flutters from the swing on the rainbow bridge like a colorful cloud. The older brother would be happy to see it."),
    ],
)

K(
    "g2a_waipo", "Reading: A Visit to Grandma's House", "阅读理解", 2, "First semester", 3, "reasoning",
    "Understand that Grandma lives at the foot of a mountain and that the narrator loves the food, activities, and sights there.",
    "yd_12",
    [
        ("What was the narrator's greatest childhood pleasure, and where did Grandma live?", "Visiting Grandma, whose home was at the foot of a mountain", ["Going to school by the sea", "Visiting Huangshan, in the city center", "Looking at the sky from a well, in a tree"], "The story begins by saying that the narrator's greatest childhood pleasure was visiting Grandma, who lived at the foot of a mountain."),
        ("What did the uncle bring back from the mountain, and what did Grandma do?", "Hawthorn berries, persimmons, or chestnuts; she always saved some for the narrator", ["He brought a snowman, which Grandma ate", "He brought textbooks for Grandma to sell", "He brought nothing, and Grandma would not let the narrator in"], "The uncle brought mountain foods. Grandma always saved a share because she cared about the narrator."),
        ("Why were the small songbirds the narrator's favorite treasure?", "The birds raised by hand would not fly away and came to sing on the narrator's hand when called", ["They ate all the seeds", "They lived at the bottom of a well", "They turned into snow in winter"], "On fine days, the small songbirds hopped among the trees. Grandma said they would sing for the narrator."),
        ("How did the aunt decorate herself when she went out in spring?", "She picked wildflowers to wear in her hair or pin to her clothes, filling the air with their fragrance", ["She put on a padded coat to transplant rice", "She locked the birds in a box", "She picked every azalea so no one else could see them"], "Azaleas and other wildflowers bloomed on the hill behind the house. The aunt wore a few, and they smelled wonderful."),
    ],
)

K(
    "g2a_xing", "Reading: The Child Who Counted the Stars", "阅读理解", 2, "First semester", 3, "reasoning",
    "Understand how Zhang Heng counted stars, learned that the Big Dipper circles Polaris, and got up to observe it himself.",
    "yd_12",
    [
        ("Who was the child who counted the stars?", "Zhang Heng, who lived in the Han dynasty", ["Premier Zhou", "Li Bai", "Liu Hulan"], "The story says the child was named Zhang Heng and lived in the Han dynasty. He later became an astronomer."),
        ("How does Zhang Heng answer his grandmother when she says the stars cannot be counted?", "If they can be seen, they can be counted. The stars move, but not randomly.", ["The stars move randomly, so there is no point looking", "The stars never move, so the count never changes", "Grandmother is right, so he stops counting"], "He notices that each star keeps a steady distance from the next, so he believes they can be counted."),
        ("What does Grandfather say about the Big Dipper?", "Its seven stars form a spoon and circle Polaris", ["Its seven stars form a boat and never move", "The Big Dipper is the sun", "Polaris circles the Big Dipper"], "The star at the end of the spoon's bowl is Polaris. The Big Dipper circles it."),
        ("How does Zhang Heng later test what Grandfather told him?", "He wakes several times during the night and sees that the Big Dipper really does move", ["He falls asleep and never looks at the stars again", "He puts the stars in a box", "He asks Grandmother to finish counting them"], "Rather than simply accepting what he hears, he observes the sky himself and confirms it."),
    ],
)

K(
    "g2a_bu", "Language Workshop 3: Complete the Sentences", "句子", 2, "First semester", 3, "procedural",
    "Complete sentences by adding who did what, where, or how.",
    "jz_12",
    [
        ("Which completion makes “弟弟____。” a complete sentence?", "在操场上跑步", ["弟弟", "跑", "操场"], "Add where the younger brother is and what he is doing; do not simply repeat one word."),
        ("Which word best completes “花儿开得____。”?", "很鲜艳", ["很跑步", "一张桌子", "在昨天"], "The blank after 开得 should describe the flowers. “Running,” “a table,” and “yesterday” do not fit."),
        ("Which sentence gives the most complete information?", "小鱼在水里游来游去。", ["小鱼游。", "在水里。", "来游去小鱼。"], "It tells who is doing what, where, and how."),
        ("Which is a complete sentence about dandelions spreading seeds by wind?", "蒲公英靠风传播种子。", ["蒲公英风种子。", "靠传播。", "种子蒲公英。"], "A complete sentence needs a subject and says how or what it does."),
    ],
)

K(
    "g2a_deng", "Poem: Climbing the Stork Tower", "古诗文积累", 2, "First semester", 4, "conceptual",
    "Memorize Wang Zhihuan's “Climbing the Stork Tower” and distinguish “千里目” from “千里眼.”",
    "gs_12",
    [
        ("What is the next line after “白日依山尽”?", "黄河入海流", ["欲穷千里目", "更上一层楼", "黄河入海去"], "The first couplet describes the sun setting behind the mountains and the Yellow River flowing to the sea; the line about seeing farther comes next."),
        ("What is the next line after “欲穷千里目”?", "更上一层楼", ["黄河入海流", "白日依山尽", "更上一层台"], "To see farther, the speaker says, climb one more floor."),
        ("Who wrote “Climbing the Stork Tower”?", "Wang Zhihuan", ["Li Bai", "Du Fu", "Bai Juyi"], "Wang Zhihuan wrote this poem. Li Bai wrote “Viewing the Waterfall at Mount Lu.”"),
        ("What idea does “更上一层楼” express?", "You can see farther from a higher place", ["Taller buildings are dangerous, so do not climb them", "Looking at the Yellow River from a tower is enough", "Go home when the sun sets"], "The poem links climbing higher with seeing farther."),
    ],
)

K(
    "g2a_lu", "Poem: Viewing the Waterfall at Mount Lu", "古诗文积累", 2, "First semester", 4, "conceptual",
    "Memorize Li Bai's “Viewing the Waterfall at Mount Lu” and distinguish “三千尺” from “九天.”",
    "gs_12",
    [
        ("What is the next line after “日照香炉生紫烟”?", "遥看瀑布挂前川", ["飞流直下三千尺", "疑是银河落九天", "遥看瀑布挂前山"], "The first line describes the distant waterfall hanging before the mountain; the next line describes its rushing descent."),
        ("What is the next line after “飞流直下三千尺”?", "疑是银河落九天", ["疑是银河落九川", "白发三千丈", "黄河入海流"], "The waterfall is compared to the Milky Way falling from the heavens. “白发三千丈” is from another poem."),
        ("Who wrote “Viewing the Waterfall at Mount Lu”?", "Li Bai", ["Wang Zhihuan", "Du Fu", "Yang Wanli"], "Li Bai wrote this poem. Wang Zhihuan wrote “Climbing the Stork Tower.”"),
        ("What does “疑是银河落九天” compare the waterfall to?", "The Milky Way falling from the sky", ["Purple mist rising from a mountain peak", "A path on the mountain", "A stream beside the door"], "The poet imagines the waterfall as the Milky Way falling from the heavens. The purple mist appears in the first line."),
    ],
)

K(
    "g2a_huang", "Reading: Strange Rocks of Huangshan", "阅读理解", 2, "First semester", 4, "reasoning",
    "Recognize the shapes of the Flying Peach Rock, Monkey Watching the Sea, Immortal Pointing the Way, and Golden Rooster Calling to Tiandu Peak.",
    "yd_12",
    [
        ("What does the Flying Peach Rock look like?", "A giant peach", ["A monkey", "An immortal", "A golden rooster"], "The rock called Flying Rock looks like a giant peach."),
        ("What does Monkey Watching the Sea look like?", "A monkey crouching and watching a rolling sea of clouds", ["A monkey swimming in the sea", "A golden rooster calling to Tiandu Peak", "An immortal pointing the way"], "The rock resembles a monkey crouching on a peak and gazing at a rolling sea of clouds."),
        ("What is unusual about Immortal Pointing the Way?", "It resembles an immortal stretching out an arm to point ahead", ["A tray of peaches rolling down", "A rooster standing on a peak", "A stone bridge"], "The rock looks like an immortal pointing the way with an outstretched arm."),
        ("Why does the story describe these rocks?", "To show how unusual and interesting Huangshan's rocks are", ["To show that Huangshan has no rocks", "To show that all the rocks look alike", "To show that rocks are taller than mountains"], "Some rocks resemble peaches, monkeys, immortals, or roosters, making them wonderfully unusual."),
    ],
)

K(
    "g2a_riyue", "Reading: Sun Moon Lake", "阅读理解", 2, "First semester", 4, "reasoning",
    "Understand that Sun Moon Lake is in Taiwan and that Guanghua Island separates it into Sun Moon Lake in the north and Moon Lake in the south.",
    "yd_12",
    [
        ("Where is Sun Moon Lake?", "In the mountains of Taiwan", ["Turpan in Xinjiang", "Maoping in Jinggangshan", "Tiandu Peak on Huangshan"], "The story describes Sun Moon Lake as Taiwan's largest lake, in the mountains near Taichung."),
        ("What is the island in the middle called, and how does it divide the lake?", "Guanghua Island. The round northern part is Sun Moon Lake, and the curved southern part is Moon Lake.", ["Flying Peach Rock; both parts are Sun Moon Lake", "Guanghua Island; the north is Moon Lake and the south is Sun Moon Lake", "The Big Dipper; the lake is divided into seven parts"], "The island divides the lake in two: the round side is Sun Moon Lake and the curved side is Moon Lake. Do not reverse north and south."),
        ("How does the story describe the lake at dawn and in light rain?", "A light mist floats over it at dawn; in rain, it seems veiled in gauze", ["The lake is completely dry at dawn", "The rocks turn into peaches when it rains", "Only warships can be seen at dawn"], "Mist, sunshine, and light rain show how the lake changes at different times."),
        ("Why does the story say Sun Moon Lake attracts many people?", "Its beautiful scenery draws visitors from China and abroad", ["People are not allowed to go there", "The lake has no water", "The lake can be seen only in winter"], "Surrounded by mountains and filled with emerald water, the lake is scenic and attracts many visitors."),
    ],
)

K(
    "g2a_pu", "Reading: Grape Valley", "阅读理解", 2, "First semester", 4, "reasoning",
    "Understand that Grape Valley in Turpan, Xinjiang, grows grapes of many colors and dries some of them in special drying rooms to make raisins.",
    "yd_12",
    [
        ("Where is Grape Valley?", "Turpan, Xinjiang", ["Sun Moon Lake in Taiwan", "Jinggangshan in Jiangxi", "Huangshan in Anhui"], "Grape Valley is in Turpan, Xinjiang, not Taiwan or Huangshan."),
        ("What colors are the ripe grapes?", "Red, white, purple, dark red, and pale green, growing in large bunches", ["Only black", "All snowy white", "Colorless because they have not fruited"], "Grapes of many colors hang in large bunches from the trellises."),
        ("How are some of the harvested grapes made into raisins?", "They are taken to drying rooms, where they become colorful, sweet raisins", ["They are scorched in the sun", "They are soaked in a lake", "They are hung on a rainbow"], "The drying rooms have openings in their walls. The grapes slowly become raisins there, and Grape Valley is famous for them."),
        ("Which fruits ripen in Grape Valley in May and in July or August?", "Apricots ripen in May, and grapes ripen in July and August", ["There is only snow in May; apricots ripen in July and August", "There is no fruit in either period", "The raisins are gone in May, and the vines stop fruiting in July and August"], "The Uyghur residents' courtyards have ripe apricots in May and ripe grapes in July and August."),
    ],
)

K(
    "g2a_yd4", "Language Workshop 4: Colors and Similes", "词语", 2, "First semester", 4, "conceptual",
    "Use color words such as snow-white and flame-red, and recognize sentences that compare one thing to another.",
    "cy_12",
    [
        ("What do “雪白、米白、奶白” describe?", "Different shades of white", ["Different shades of red", "Three kinds of animals", "Three mountains"], "“雪” (snow), “米” (rice), and “奶” (milk) modify “白” (white) to describe different shades."),
        ("Which color do “火红、桃红、枣红” describe?", "Red", ["Green", "Blue", "Black"], "“火,” “桃,” and “枣” describe different shades of red. “草绿” and “翠绿” are shades of green."),
        ("What does the sentence “小椅子像翘起尾巴的小猫” compare the chair to?", "A kitten", ["Soldiers lining up", "A blackboard", "A stream"], "The raised back of the chair resembles a kitten's tail. This is a simile."),
        ("What line is often paired with “有山皆图画”?", "无水不文章", ["更上一层楼", "飞流直下三千尺", "独钓寒江雪"], "The pair means that mountains make a picture and water makes a composition. It is a workshop saying, not the next line of a poem."),
    ],
)

K(
    "g2a_jing", "Reading: The Frog in the Well", "阅读理解", 2, "First semester", 5, "reasoning",
    "Understand the frog and bird's disagreement about the size of the sky and why the frog is mistaken.",
    "yd_12",
    [
        ("How big does the frog say the sky is?", "Only as big as the well's opening", ["Boundless", "As large as the sea", "Much smaller than the well"], "The frog sits in the well every day and says the sky is no bigger than the opening."),
        ("What does the bird say the sky is like?", "Vast and boundless", ["Only as big as the well's opening", "As big as the bird's wings", "There is no sky at all"], "The bird has flown more than a hundred miles and says the sky is vast and boundless."),
        ("Why is the frog mistaken?", "It has stayed in the well and seen only a small part of the sky", ["The bird lies to it", "The sky outside the well really is tiny", "It can fly farther than the bird"], "The frog does not believe the bird and asks it to come down. The frog has never gone out to see for itself."),
        ("What kind of person does the idiom “坐井观天” describe?", "Someone with little experience who thinks their limited view is everything", ["Someone who stands high and sees far", "Someone who listens to advice", "Someone who flies outdoors every day"], "The frog sees only the patch of sky above the well and refuses to believe that the sky beyond is vast."),
    ],
)

K(
    "g2a_han", "Reading: The Freezing Bird", "阅读理解", 2, "First semester", 5, "reasoning",
    "Understand how the bird refuses to build a nest and keeps saying it will do so tomorrow until it freezes to death.",
    "yd_12",
    [
        ("What does the magpie urge the freezing bird to do?", "Build a nest while the weather is still good", ["Fly south with it", "Pull out its feathers", "Stay awake at night"], "Winter is coming, so the magpie tells the bird to stop sleeping and hurry to build a nest."),
        ("How does the freezing bird respond?", "It puts things off and says it will build a nest tomorrow", ["It starts building right away", "Its nest is already finished", "It thanks the magpie and starts at once"], "It says it will build the nest tomorrow, then forgets and plays during the day."),
        ("What happens to the freezing bird?", "It freezes to death on a winter night", ["It builds a warm nest", "It flies away with the magpie", "It turns into a phoenix"], "It keeps saying it will do the work tomorrow and eventually freezes in a cliffside crevice."),
        ("What lesson does the story teach?", "Do not put off necessary work; do it in time", ["Playing is more important than building a nest", "Ignore a friend's advice", "There is no need to prepare for winter"], "Putting everything off brings disaster. A good habit is to finish the work today."),
    ],
)

K(
    "g2a_hulu", "Reading: I Want the Gourds", "阅读理解", 2, "First semester", 5, "reasoning",
    "Understand that the gardener watches only the gourds and ignores the leaves, so all the gourds eventually fall off.",
    "yd_12",
    [
        ("What does the gardener like looking at most?", "The little gourds", ["Aphids on the leaves", "The neighbor's advice", "The whole gourd vine"], "He watches the growing gourds every day and hopes they will become large."),
        ("What does he say when aphids appear on the leaves?", "I want the gourds, not the leaves.", ["I should treat the plants right away.", "I need to care for both the leaves and gourds.", "Please ask the neighbor for help."], "The neighbor advises him to treat the pests, but the gardener says a few bugs do not matter and that he wants the gourds."),
        ("What happens to the gourds?", "They all fall off one by one", ["They grow bigger and more numerous", "The leaves recover and more gourds grow", "The aphids fly away by themselves"], "The pests multiply, the small gourds turn yellow, and they all fall off."),
        ("What does the story show?", "Leaves and gourds depend on each other; you cannot focus only on the fruit", ["It does not matter if the leaves have pests", "You should ignore the neighbor", "Gourds do not need leaves"], "If the leaves are neglected, the gourds cannot grow well. Do not focus only on the part you want."),
    ],
)

K(
    "g2a_yd5", "Language Workshop 5: Making a Request", "习作基础", 2, "First semester", 5, "procedural",
    "Explain your reason politely when making a request, and accept a refusal without pressure. Memorize the maxim “Work hard while young, or regret your late start.”",
    "xz_12",
    [
        ("Which sentence politely asks a classmate to switch duty days?", "Could we discuss switching? Something came up at home today; would another day work?", ["You have to switch with me now.", "Say nothing and walk away.", "Loudly order them to agree at once."], "Make a request politely and explain why. Giving orders or staying silent is not a discussion."),
        ("If the other person cannot switch today, what is the best response?", "Say that it is okay and do not pressure them", ["Insist that they cancel their plans", "Angrily repeat that they must switch", "Pretend not to hear and refuse to leave"], "If someone has a problem, accept their refusal without pressuring them."),
        ("Which sentence does not explain what you want to discuss?", "Switch with me.", ["I have not finished this book. Could I borrow it for two more days?", "It's Grandma's birthday, and I'd like to go home early. Could we switch duty days?", "Could you help me with this problem?"], "“Switch with me” does not say what should be switched or why."),
        ("What is the next line after “少年不知勤学苦”?", "老来方知读书迟", ["一日不读十日空", "学海无涯苦作舟", "更上一层楼"], "The couplet says that someone who does not study diligently when young may regret the lost time in old age. The other options are different sayings."),
    ],
)

K(
    "g2a_ba", "Reading: At the Octagonal House", "阅读理解", 2, "First semester", 6, "reasoning",
    "Understand how Chairman Mao wrote by an oil lamp in the Octagonal House in Maoping during the difficult years of the Jinggangshan struggle.",
    "yd_12",
    [
        ("Where is the Octagonal House?", "Maoping Village in Jinggangshan", ["Sun Moon Lake in Taiwan", "Grape Valley in Xinjiang", "Huangshan"], "During the difficult years of the Jinggangshan struggle, Chairman Mao lived in the Octagonal House in Maoping Village. Its roof had eight sides."),
        ("How does Chairman Mao work late on a freezing winter night?", "He writes at a bamboo chair in a thin uniform with a light blanket over him", ["He sleeps under a thick quilt", "He watches a rainbow by the lake", "He transplants rice in a field"], "It is very cold, but he continues writing by the lamp. His thin uniform and light blanket show how difficult the conditions are."),
        ("What does “星星之火” first refer to in the story?", "The small flame of the oil lamp", ["The Big Dipper in the sky", "A campfire", "The midday sun"], "He brightens the wick and gazes at the tiny flame, which is why the story calls it a spark of fire."),
        ("Why does he not notice the blanket slipping off?", "He is absorbed in the lamplight and deep in thought as he writes", ["There is no blanket in the room", "He has already left the Octagonal House", "The lamp is so bright that he wakes up and runs away"], "He holds a pen in one hand and adjusts the wick with the other. He is so absorbed in thought that he does not notice the blanket fall."),
    ],
)

K(
    "g2a_zhu", "Reading: Zhu De's Carrying Pole", "阅读理解", 2, "First semester", 6, "reasoning",
    "Understand how Zhu De carried grain with the soldiers in Jinggangshan and wrote his name on his carrying pole.",
    "yd_12",
    [
        ("Where did Zhu De carry grain with the soldiers?", "Jinggangshan", ["Xishuangbanna", "Huangshan", "The well at Shazhouba"], "Jinggangshan's steep, rugged trails meant people had to carry grain up from the foot of the mountain."),
        ("Why do the soldiers hide Zhu De's carrying pole?", "They worry about him and want to stop him carrying grain", ["The pole is too new to use", "All the grain has already been carried", "They do not recognize Zhu De"], "The soldiers see him carrying grain by day and working at night, so they hide his pole."),
        ("What words are written on the pole when it is returned?", "朱德的扁担", ["Zhu De's note", "Carry the grain", "Jinggangshan"], "He finds another pole and writes “朱德的扁担” on it, so the soldiers cannot hide it again."),
        ("What quality does this story show in Zhu De?", "He shares hardships with the soldiers", ["He only orders others to carry grain", "He refuses to climb the mountain", "He keeps the grain for himself"], "The soldiers are moved when their commander picks up a carrying pole and helps carry grain."),
    ],
)

K(
    "g2a_po", "Reading: An Unforgettable Water-Splashing Festival", "阅读理解", 2, "First semester", 6, "reasoning",
    "Understand how Premier Zhou celebrated the Water-Splashing Festival with the Dai people in 1961.",
    "yd_12",
    [
        ("Who celebrated the Water-Splashing Festival with the Dai people?", "Premier Zhou", ["Chairman Mao", "Zhu De", "Li Bai"], "Premier Zhou visited Xishuangbanna for the 1961 festival and exchanged water splashes and blessings with the people."),
        ("What do people express by splashing water?", "Blessings", ["Anger", "A farewell forever", "A race to see who can run fastest"], "Clean water symbolizes happiness, and splashing it is a way to bless one another."),
        ("What were the phoenix flowers like that day?", "They bloomed bright red, as if welcoming the guests", ["Not a single flower bloomed", "They bloom only in winter", "Everyone picked them all"], "The story uses the bright red phoenix flowers to echo the people's joy at welcoming Premier Zhou."),
        ("Why was that Water-Splashing Festival unforgettable?", "Premier Zhou splashed water and danced with everyone", ["It did not rain that day", "People saw river water for the first time", "The festival was never held again"], "Premier Zhou wore Dai clothing and exchanged water splashes with the people. Their joyful celebration made the day unforgettable."),
    ],
)

K(
    "g2a_hulan", "Reading: Liu Hulan", "阅读理解", 2, "First semester", 6, "reasoning",
    "Understand how Liu Hulan faced the enemy at Yunzhou West, refused to betray other Communist Party members, and was honored by Chairman Mao.",
    "yd_12",
    [
        ("Where does Liu Hulan face the enemy and die bravely?", "Yunzhou West Village", ["The Octagonal House in Jinggangshan", "Xishuangbanna", "Sun Moon Lake in Taiwan"], "The story says the enemy surrounds Yunzhou West Village. Liu Hulan faces them there and refuses to betray others."),
        ("When the enemy asks who else in the village belongs to the Communist Party, how does she answer?", "I am the only one.", ["She gives them everyone's names", "She says she is not a Party member", "She says she does not know where the village is"], "She refuses to give anyone else up and says she is the only one."),
        ("Which statement before the execution blade best shows her resolve?", "Kill me or cut me down as you wish; I am not afraid to die for the Communist Party.", ["I will tell you tomorrow", "I can go with you", "I will hand over everyone in the village"], "The enemy threatens her with the blade. She stands tall, says this, and walks toward it. She is not yet fifteen."),
        ("What inscription does Chairman Mao write in her honor?", "Great in life, glorious in death", ["A single spark can start a prairie fire", "To see a thousand miles, climb one more floor", "Where there is a will, there is a way"], "The inscription honors her as great in life and glorious in death. Do not confuse it with other well-known sayings."),
    ],
)

K(
    "g2a_yd6", "Language Workshop 6: Tell a Story from Pictures", "习作基础", 2, "First semester", 6, "procedural",
    "Tell a story from several pictures in order, explaining who is where and what they are doing. Memorize the saying “Where there is a will, there is a way.”",
    "xz_12",
    [
        ("Which way of telling a picture story is clear?", "Start with what is happening in the first picture, then tell the events in order through the last picture", ["Begin with the last picture and call it the beginning", "Say only that the pictures look nice without naming anyone", "Invent a different, unrelated story for each picture"], "Pictures show events in sequence, so connect them in order. Reversing the sequence or leaving out the characters makes the story hard to follow."),
        ("Which statement does not explain what happens in the pictures?", "Interesting.", ["A rabbit tries to pull up a carrot in a field, cannot do it, and later asks a friend for help.", "Mom wakes him in the morning. He checks the clock, sees he is late, and hurries to school.", "A small tree bends in the wind and rain, so two children straighten it."], "Just one word does not tell the listener who is involved, where they are, or what happens."),
        ("Besides describing what is shown, what else can you do when telling the story?", "Imagine what the characters might say or do next without changing what the pictures show", ["Say that none of the people in the pictures are there", "Repeat the title in every sentence", "Tear the pictures in half and tell only half the story"], "A reasonable addition can make a story fuller, but do not contradict what the pictures show."),
        ("What does “有志者事竟成” mean?", "A determined person who perseveres can accomplish a goal", ["A person with a goal does not need to work", "Once a goal is achieved, there is no need to set another", "Will is the name of an animal"], "The saying comes from the Book of the Later Han. It encourages people to set a goal and keep working toward it."),
    ],
)

K(
    "g2a_jiang", "Poem: Snow on the River", "古诗文积累", 2, "First semester", 7, "conceptual",
    "Memorize Liu Zongyuan's “Snow on the River” and distinguish it from “Song of the Chile People” and “Viewing the Waterfall at Mount Lu.”",
    "gs_12",
    [
        ("What is the next line after “千山鸟飞绝”?", "万径人踪灭", ["孤舟蓑笠翁", "独钓寒江雪", "风吹草低见牛羊"], "The opening describes mountains and paths without people or birds; the fisherman appears later."),
        ("What is the next line after “孤舟蓑笠翁”?", "独钓寒江雪", ["万径人踪灭", "疑是银河落九天", "天似穹庐"], "A lone fisherman in a straw cloak and hat fishes on the snowy river."),
        ("Who wrote “Snow on the River”?", "Liu Zongyuan", ["Li Bai", "Wang Zhihuan", "A Northern Dynasties folk poet"], "Liu Zongyuan wrote “Snow on the River”; Li Bai wrote “Viewing the Waterfall at Mount Lu.”"),
        ("What scene does this poem describe?", "Snow covers the mountains and paths; birds and travelers are gone, leaving only a lone fisherman", ["Wind bends the grass on a plain, revealing cattle and sheep", "Someone can reach out from a tower and pick stars", "The Yellow River flows toward the sea"], "The poem describes mountains without birds and paths without footprints. Do not confuse it with “Song of the Chile People” or “Night Lodging at the Mountain Temple.”"),
    ],
)

K(
    "g2a_chil", "Poem: Song of the Chile People", "古诗文积累", 2, "First semester", 7, "conceptual",
    "Memorize the Northern Dynasties folk song “Song of the Chile People” and learn that “见” in “见牛羊” means “appear.”",
    "gs_12",
    [
        ("What is the next line after “敕勒川，阴山下”?", "天似穹庐，笼盖四野", ["天苍苍，野茫茫", "风吹草低见牛羊", "黄河入海流"], "The sky is first compared to a felt tent covering the open land; the description of the vast sky and plain comes later."),
        ("What is the next line after “天苍苍，野茫茫”?", "风吹草低见牛羊", ["笼盖四野", "天似穹庐", "风吹草低现牛羊"], "When the wind bends the grass, the cattle and sheep appear. The poem uses 见, not 现."),
        ("How was “Song of the Chile People” passed down?", "As a Northern Dynasties folk song", ["It was written by Li Bai", "It was written by Wang Zhihuan", "It was written by Du Fu"], "This is a folk song from the Northern Dynasties, not a Tang dynasty quatrain."),
        ("What does “见” mean in “风吹草低见牛羊,” and how is it pronounced here?", "It means “appear” and is pronounced xiàn", ["It means “to see” and is pronounced jiàn", "It means “to meet”", "It means “opinion”"], "The wind bends the grass and reveals the cattle and sheep. Here, 见 is pronounced xiàn and means “appear.”"),
    ],
)

K(
    "g2a_wu", "Reading: Where Is the Fog?", "阅读理解", 2, "First semester", 7, "reasoning",
    "Understand how the fog acts like a playful child, hiding the sea, coast, and city before hiding itself.",
    "yd_12",
    [
        ("What does the fog hide when it reaches the sea?", "The sea, including the water, boats, and distant objects", ["It plucks the sun and puts it in a pocket", "It carries every snowy mountain home", "It hides only one small stone"], "The fog says it will hide the sea, making the things on it disappear from view."),
        ("What does the fog hide when it reaches the city?", "Houses, streets, trees, bridges, pedestrians, and a little black cat", ["Only textbooks", "It turns the city into Grape Valley", "Nothing; the city becomes clearer"], "The fog covers the things that were visible in the city."),
        ("Whom does the fog say it will hide at the end?", "Itself", ["It hides the sun forever", "It leaves the little black cat outside by itself", "It hides the fisherman in a well"], "From above, the fog says that it is now time to hide itself."),
        ("What happens when the sun comes out?", "The fog disappears, and the sea, coast, and city reappear", ["The fog thickens and nothing reappears", "The city is carried away by the fog", "The fog hides the sun forever"], "When the fog clears, the boats, houses, pedestrians, and little black cat can be seen again."),
    ],
)

K(
    "g2a_xuer", "Reading: The Snow Child", "阅读理解", 2, "First semester", 7, "reasoning",
    "Understand how the Snow Child keeps the little rabbit company, rescues him from a fire, and melts into a cloud.",
    "yd_12",
    [
        ("Who builds the Snow Child?", "The rabbit's mother", ["The little black cat", "The fog", "Zhang Heng"], "The rabbit's mother builds a snow child in the yard to keep the little rabbit company."),
        ("What does the rabbit's mother say before she leaves?", "The Snow Child will stay with the little rabbit, who must not leave the house", ["The little rabbit should go cut firewood on the mountain", "The Snow Child should go swimming in the sea", "They should set the house on fire"], "She asks the Snow Child to keep the rabbit company and tells the little rabbit not to go outside."),
        ("What does the Snow Child do when the house catches fire?", "Rushes inside and carries the little rabbit out", ["Stands outside and watches", "Makes the fire burn even hotter", "Runs into the forest first"], "The little rabbit is asleep. The Snow Child notices the fire and rescues him."),
        ("What happens to the Snow Child?", "He melts into water and becomes a white cloud in the sky", ["He becomes a real rabbit", "He becomes a block of ice that never melts", "He flies away to pick stars"], "After rescuing the little rabbit, the Snow Child is soaked. The cloud the rabbit later sees is the Snow Child."),
    ],
)

K(
    "g2a_yd7", "Language Workshop 7: Night Lodging at the Mountain Temple", "古诗文积累", 2, "First semester", 7, "conceptual",
    "Memorize Li Bai's “Night Lodging at the Mountain Temple” and distinguish “天上人” from “天上神.”",
    "gs_12",
    [
        ("What is the next line after “危楼高百尺”?", "手可摘星辰", ["不敢高声语", "恐惊天上人", "更上一层楼"], "The tower seems so high that its stars could be reached by hand; the line about speaking quietly comes later."),
        ("What is the next line after “不敢高声语”?", "恐惊天上人", ["恐惊天上神", "手可摘星辰", "疑是银河落九天"], "The speaker is afraid that a loud voice might disturb the people in the sky. The poem says “天上人,” not “天上神.”"),
        ("Who wrote “Night Lodging at the Mountain Temple”?", "Li Bai", ["Wang Zhihuan", "Liu Zongyuan", "A Northern Dynasties folk poet"], "Li Bai wrote this poem. Liu Zongyuan wrote “Snow on the River,” and Wang Zhihuan wrote “Climbing the Stork Tower.”"),
        ("Why does the poet avoid speaking loudly?", "The tower seems to reach the sky, and he fears disturbing the people there", ["Someone is sleeping in the temple and the teacher forbids talking", "The stars might fall", "The Yellow River is right below"], "The tower seems high enough to reach the stars, so the poet fears disturbing the people in the sky."),
    ],
)

K(
    "g2a_cheng", "Reading: Compliments", "阅读理解", 2, "First semester", 8, "reasoning",
    "Understand how the hedgehog praises the badger's improving stools and helps him gain confidence.",
    "yd_12",
    [
        ("What is the badger doing when the hedgehog sees him?", "Learning woodworking; he has made three little stools", ["Looking at the sky from a well", "Fishing on a river", "Drying grapes in Grape Valley"], "The stools are still rough, but the hedgehog does not make fun of him."),
        ("How does the hedgehog praise the badger?", "You are really skilled; each stool is better than the last.", ["Your work is terrible. Take it apart and start again.", "Stools have nothing to do with leaves.", "You should stop making things."], "The praise is specific: each stool is better than the last, helping the badger recognize his progress."),
        ("How does the badger change after receiving the compliment?", "He gains confidence, makes a chair later, and gives it to the hedgehog", ["He never does woodworking again", "He burns all the stools", "He hides and sees no one"], "He had been discouraged. The compliment encourages him to continue until he makes a chair."),
        ("After accepting the apple, what does the badger say the compliment has relieved?", "His fatigue from the day", ["The fog in the sky", "The sky above the well", "The words on the carrying pole"], "The hedgehog gives the badger an apple. The badger says the compliment has relieved his fatigue from the day."),
    ],
)

K(
    "g2a_chuan", "Reading: The Paper Boat and the Kite", "阅读理解", 2, "First semester", 8, "reasoning",
    "Understand how the squirrel and bear send each other good wishes by paper boat and kite, then make up after a quarrel.",
    "yd_12",
    [
        ("Where do the squirrel and the bear live?", "The squirrel lives on the mountaintop, and the bear lives at its foot", ["They both live in a well", "The squirrel lives at the foot, and the bear lives on top", "They live in the same house"], "A stream flows down from the mountain past the bear's home, so the paper boat can drift to him."),
        ("What messages do the paper boat and kite carry?", "The boat says “Wishing you happiness”; the kite says “Wishing you joy.”", ["The boat says “Wishing you joy,” and the kite has no message", "Both say “Goodbye”", "The boat says “Great in life, glorious in death”"], "The note on the pinecone says “Wishing you happiness.” The strawberry kite carries “Wishing you joy.”"),
        ("After their quarrel, who first suggests making up, and how?", "The squirrel writes on a paper boat: “If you want to make up, fly a kite.”", ["The bear tears up the boat and never sees the squirrel again", "The squirrel moves away from the mountain", "The bear jumps into the stream and sinks the boat"], "The squirrel cannot see a kite from the mountaintop or a boat in the stream, so he finally writes the message."),
        ("What does the bear do after seeing the message?", "He flies a kite, and they become friends again", ["He hangs the kite in a tree and never takes it down", "He replies that he does not want to make up", "He moves to Grape Valley"], "That evening, the squirrel sees the kite flying, cries with happiness, and puts a paper boat back in the stream."),
    ],
)

K(
    "g2a_he", "Reading: The Happy Stream", "阅读理解", 2, "First semester", 8, "reasoning",
    "Understand how the stream stops complaining after hitting a mountain and continues onward with the spring and waterfall.",
    "yd_12",
    [
        ("Why does the stream cry at first?", "It rushes into a mountain, gets hurt, and complains", ["The spring will not let it pass", "The waterfall freezes it into ice", "The wildflowers will not talk to it"], "The stream sings as it flows, but rushes into a mountain because it is hurrying. It has gotten along with sand and grass, but this time it gets hurt."),
        ("Which line from the mountain encourages the stream?", "Even restless water has strength; why fear a few tumbles?", ["Stop here and never flow again", "The more you complain, the stronger you become", "Calm water is best, so never move forward"], "The mountain points to the spring, which keeps singing and moving forward despite its stumbles."),
        ("Who becomes the stream's friend later?", "The spring and the waterfall", ["The freezing bird and the magpie", "The squirrel and the bear", "The frog and the bird"], "The stream invites the spring to flow with it and sees the waterfall leap down. The three companions continue hand in hand."),
        ("What is the main message of the story?", "Do not only complain when you meet difficulty; courageously moving forward can bring back happiness", ["If you hit a mountain, cry and go back", "The more friends you have, the harder it is to travel together", "Water should always stop in the sand"], "The stream begins with carefree happiness and later finds joy in overcoming difficulty with friends."),
    ],
)

K(
    "g2a_xie", "Language Workshop 8: Write from Pictures", "习作基础", 2, "First semester", 8, "procedural",
    "Write a few connected sentences about a picture, explaining who is where and what they are doing.",
    "xz_12",
    [
        ("Which picture-based paragraph is coherent?", "A rabbit pulls a carrot in a vegetable patch. It pulls hard and finally gets the carrot out.", ["Rabbit. Carrot. Hard.", "Pulled out, rabbit, vegetable patch, finally.", "It pulls hard."], "Say who is doing what and where, then describe the result so the sentences connect."),
        ("Which paragraph does not clearly describe what is happening in the picture?", "Pretty. Happy.", ["A bird sings on a branch, and its song sounds lovely.", "Two children jump rope in a park.", "After the rain, ants carry food outside."], "Just two words do not say who is where or what happens."),
        ("Which sentence best describes a child watering flowers?", "The child carefully waters the roots.", ["The child throws the flowers in the trash.", "The child pours water over their own head and runs away.", "The flowers fly away by themselves."], "Describe the scene shown: the child is watering flowers, not doing the opposite."),
        ("What should you do after writing a few sentences about a picture?", "Read them back to see whether they connect", ["Hand it in after writing one character", "Invent as many events as possible that are not in the picture", "Use only one word in each sentence"], "Rereading can reveal missing steps or events described in the wrong order."),
    ],
)

# ---------- Grade 2, Volume 2 ----------
# Spring 2026 revised national curriculum. Lessons are listed in textbook order; oral communication and writing activities are included in the workshops.
# Lessons retired from the previous edition are omitted.

K(
    "g2b_liu", "Poem: Ode to the Willow", "古诗文积累", 2, "Second semester", 1, "conceptual",
    "Memorize He Zhizhang's “Ode to the Willow” and recognize that “二月春风似剪刀” describes the wind.",
    "gs_12",
    [
        ("What is the next line after “碧玉妆成一树高”?", "万条垂下绿丝绦", ["不知细叶谁裁出", "二月春风似剪刀", "万条垂下绿丝条"], "The willow branches hang like green silk ribbons. The poem uses 绦, meaning “ribbon,” not 条."),
        ("What is the next line after “不知细叶谁裁出”?", "二月春风似剪刀", ["万条垂下绿丝绦", "碧玉妆成一树高", "春风又绿江南岸"], "The poet imagines that February's spring wind is the pair of scissors that cut the slender leaves."),
        ("Who wrote “Ode to the Willow”?", "He Zhizhang", ["Li Bai", "Du Fu", "Gao Ding"], "He Zhizhang wrote “Ode to the Willow.” Gao Ding wrote “Village.”"),
        ("What does “二月春风似剪刀” compare the spring wind to?", "Scissors", ["Jade", "A ribbon", "Slender leaves"], "The spring wind is compared to scissors that cut the willow leaves. Jade describes the whole willow tree."),
    ],
)

K(
    "g2b_cun", "Poem: Village Life", "古诗文积累", 2, "Second semester", 1, "conceptual",
    "Memorize Gao Ding's “Village Life” and distinguish it from He Zhizhang's “Ode to the Willow.”",
    "gs_12",
    [
        ("What is the next line after “草长莺飞二月天”?", "拂堤杨柳醉春烟", ["儿童散学归来早", "忙趁东风放纸鸢", "二月春风似剪刀"], "The poem first describes willows brushing the riverbank in the spring haze; children flying kites appear later."),
        ("What is the next line after “儿童散学归来早”?", "忙趁东风放纸鸢", ["拂堤杨柳醉春烟", "忙趁东风放纸鹞", "草长莺飞二月天"], "The children hurry to fly kites in the east wind after school. 纸鸢 means “kite”; the poem does not say 纸鹞."),
        ("Who wrote “Village Life”?", "Gao Ding", ["He Zhizhang", "Li Bai", "Bai Juyi"], "Gao Ding wrote “Village Life.” He Zhizhang wrote “Ode to the Willow.”"),
        ("What do the children hurry to do after school?", "Fly kites", ["Cut willow leaves", "Pick white lotus flowers", "Climb a tower to watch the Yellow River"], "The poem says the children take advantage of the east wind to fly kites. Cutting willow leaves is an image from “Ode to the Willow.”"),
    ],
)

K(
    "g2b_zhao", "Reading: Looking for Spring", "阅读理解", 2, "Second semester", 1, "reasoning",
    "Understand that the grass, wildflowers, buds, and stream are compared to spring's eyebrows, eyes, musical notes, and song.",
    "yd_12",
    [
        ("Where do the children go to look for spring?", "They take off their padded coats and run into the fields", ["They go build a snowman", "They stay under the covers", "They visit a summer lotus pond"], "They take off their padded coats, rush out of the house, and run into the fields to look for spring."),
        ("What does the story compare the grass poking out of the ground to?", "Spring's eyebrows", ["Spring's eyes", "Spring's musical notes", "Spring's song"], "The grass is like eyebrows; wildflowers are eyes, buds are notes, and the thawing stream is a song."),
        ("Which group contains only signs of spring from the story?", "Grass, wildflowers, buds, and a stream", ["Frost, snow, ice, and north wind", "Lotus flowers, cicadas, and a green sun", "Fallen leaves, geese, and yellow leaves"], "The grass peeks out, wildflowers bloom, trees send out buds, and the stream begins to sing."),
        ("What does comparing spring to a shy girl mean?", "Spring hides, so you have to look carefully for it", ["Spring has already gone away", "Spring is very loud", "Spring appears only at night"], "Spring seems to hide, so the children must search carefully."),
    ],
)

K(
    "g2b_hua", "Reading: The Flower-Covered Path", "阅读理解", 2, "Second semester", 1, "reasoning",
    "Understand how seeds sent by Uncle Giraffe spill along the road and bloom into a flower-covered path the following spring.",
    "yd_12",
    [
        ("Who sends Mr. Mole the package?", "Uncle Giraffe", ["Mrs. Squirrel", "Mrs. Hedgehog", "Mrs. Fox"], "Uncle Giraffe sends the package. Mrs. Squirrel, Mrs. Hedgehog, and Mrs. Fox are the ones who later see the flowers."),
        ("Why is the package empty when it reaches Mrs. Squirrel's house?", "It tore, and its contents spilled along the way", ["Mrs. Squirrel ate everything", "The post office has no such package", "It was an empty sheet of paper all along"], "Mr. Mole is disappointed because the flower seeds spilled along the road."),
        ("Why is the road to Mrs. Squirrel's house covered in flowers the next spring?", "The spilled seeds sprout and bloom", ["Mrs. Hedgehog plants them overnight", "Mrs. Fox buys them in town", "Snowflakes fall on the road and turn into flowers"], "Mrs. Squirrel explains that Uncle Giraffe sent flower seeds the year before."),
        ("What does Mrs. Squirrel call the flower seeds?", "A wonderful gift", ["Useless trash", "A debt-collection letter", "Scissors for pruning willows"], "The flowers bloom in front of everyone's homes, so she calls them a wonderful gift."),
    ],
)

K(
    "g2b_zhi", "Reading: Grandpa Deng Xiaoping Plants a Tree", "阅读理解", 2, "Second semester", 1, "reasoning",
    "Understand how Deng Xiaoping carefully planted a cypress sapling in Temple of Heaven Park on April 5, 1987.",
    "yd_12",
    [
        ("On what date does the tree-planting story take place?", "April 5, 1987", ["January 1, 1985", "October 1, 1978", "June 1, 2000"], "The story opens by calling April 5, 1987, an unforgettable day."),
        ("Where does Grandpa Deng Xiaoping plant a tree?", "Temple of Heaven Park in Beijing", ["Jinggangshan", "Shazhouba", "By West Lake"], "That day, he plants a tree with everyone at Temple of Heaven Park in Beijing."),
        ("What does he carefully choose and plant?", "A healthy cypress sapling", ["A willow branch", "An old tree blown down by the wind", "A potted peony in bloom"], "He chooses a cypress sapling, places it in the hole, and shovels soil around it."),
        ("What does he do when the sapling looks crooked?", "He steps forward and straightens it", ["He says it is no good and walks away", "He pulls it out and throws it away", "He tells someone to fill the hole however they like"], "He steps back to inspect it, says it is not right, and straightens the sapling himself."),
    ],
)

K(
    "g2b_yd1", "Language Workshop 1: Choose the Right Tone", "习作基础", 2, "Second semester", 1, "procedural",
    "Choose a tone that fits the situation. Memorize the first four lines of Bai Juyi's “Farewell on the Ancient Grassland.”",
    "xz_12",
    [
        ("What is the best tone to use when asking someone for help?", "Speak politely and explain what you need", ["Order the person to hurry up", "Turn away without saying anything", "Speak so quietly that no one can hear"], "Use a considerate tone and make the request clear."),
        ("What should you remember when making a request, apologizing, or giving a reminder?", "Use a tone that makes your meaning clear to the other person", ["There is only one acceptable tone", "Changing your tone always reverses the meaning", "Tone matters only when singing"], "Praise, requests, and apologies call for different emphasis and attitudes, which affect how the listener feels."),
        ("What is the next line after “离离原上草”?", "一岁一枯荣", ["春风吹又生", "野火烧不尽", "二月春风似剪刀"], "The grass on the plain withers and grows back every year. “春风吹又生” comes later."),
        ("What is the next line after “野火烧不尽,” and who wrote it?", "春风吹又生; Bai Juyi", ["春风吹又生; He Zhizhang", "一岁一枯荣; Gao Ding", "忙趁东风放纸鸢; Bai Juyi"], "Bai Juyi wrote “Farewell on the Ancient Grassland,” not “Ode to the Willow.”"),
    ],
)

K(
    "g2b_lei", "Reading: Lei Feng, Where Are You?", "阅读理解", 2, "Second semester", 2, "reasoning",
    "Understand that the poem follows a stream and a path to find the good deeds Lei Feng performed.",
    "yd_12",
    [
        ("Whom are the children looking for?", "Lei Feng", ["Cao Chong", "Zhu De", "Premier Zhou"], "The poem asks, “Lei Feng, where are you?” The children follow a stream and a path as they search."),
        ("Why does the stream say it has seen Lei Feng?", "He carried a lost child through the drizzle", ["He swam in the stream", "He filled in the stream", "The stream only heard about him from someone else"], "The stream says Lei Feng passed by yesterday, carrying a lost child through the fine rain."),
        ("What does the winding path remember Lei Feng doing?", "Carrying an elderly woman on his back", ["Cutting down all the trees beside the path", "Hiding in a tree", "Hurrying along without helping anyone"], "The path says Lei Feng passed by yesterday carrying an elderly woman and walking over the thorns."),
        ("What does “Wherever someone needs love, Lei Feng appears there” mean?", "Follow Lei Feng's example and help wherever help is needed", ["Lei Feng lives only beside streams", "There are no good people left", "You can help others only when it rains"], "The poem ends by saying that Lei Feng remains with us whenever someone shows kindness."),
    ],
)

K(
    "g2b_qian", "Reading: The Thousand-Person Cake", "阅读理解", 2, "Second semester", 2, "reasoning",
    "Understand that many people contribute their work to make an ordinary rice cake.",
    "yd_12",
    [
        ("What is the “thousand-person cake” that Dad serves?", "An ordinary rice cake", ["A cake meant for a thousand people", "A stone", "A bowl of sugar"], "Dad serves an ordinary rice cake but calls it a thousand-person cake."),
        ("Where does the rice in the cake come from?", "It is grown by farmers", ["It grows by itself in a shop", "It is made of sugar", "A child draws it"], "Farmers sow and harvest rice, which is then ground into flour for the cake."),
        ("Why is it called a “thousand-person cake”?", "It takes the work of many people to make it", ["It must be cut into a thousand pieces", "Only a thousand people can eat it", "A thousand characters are written on it"], "Growing rice, milling flour, making sugar, printing packaging, and transporting the cake all require people's work."),
        ("What is the main message of the story?", "Ordinary things contain the work of many people", ["One person makes a rice cake in five minutes", "Work does not matter", "Dad is joking; the cake requires no work"], "Behind an ordinary-looking cake is the hard work of many people."),
    ],
)

K(
    "g2b_ruo", "Reading: I Am Not the Weakest", "阅读理解", 2, "Second semester", 2, "reasoning",
    "Understand how Sasha covers a wild rose with his raincoat because he wants to protect someone more vulnerable than himself.",
    "yd_12",
    [
        ("What happens to the family outdoors?", "It suddenly starts to rain", ["The sun grows hotter", "The river dries up at once", "The wild rose brings them a raincoat"], "They are outdoors when the rain begins, and their mother takes out a raincoat."),
        ("In what order is the raincoat passed along?", "Mother gives it to Tolia, who then gives it to Sasha", ["Sasha gives it to Mother, who gives it to the rose", "The wild rose gives it to Tolia first", "No one passes the raincoat"], "Mother hands the coat to Tolia, who then passes it to Sasha."),
        ("What does Sasha do with the raincoat?", "He covers the rain-soaked wild rose with it", ["Throws it into the stream", "Covers only his own head and runs away", "Returns it to the store"], "Sasha does not keep the coat for himself; he spreads it over the wild rose."),
        ("Why does Sasha say he is not the weakest?", "He can protect the wild rose, which is more vulnerable than he is", ["He is older than his mother", "He is not afraid of rain", "He has no younger brother"], "Someone who can protect a more vulnerable being is not the weakest. That is the story's lesson."),
    ],
)

K(
    "g2b_yd2", "Language Workshop 2: Jobs and Sayings", "词语", 2, "Second semester", 2, "conceptual",
    "Recognize occupations such as teacher, architect, and animal keeper; understand the sayings “Give someone a rose, and its fragrance stays on your hand” and “Better to bring coal to someone in the snow than add flowers to a brocade.”",
    "cy_12",
    [
        ("What does “予人玫瑰，手有余香” mean?", "Giving to others can bring joy to you as well", ["You should keep every rose for yourself", "Helping others always brings trouble", "If your hands smell nice, you do not need to wash them"], "Giving someone a rose leaves its fragrance on your hand. The saying is about helping others."),
        ("Which action does “与其锦上添花，不如雪中送炭” value more?", "Helping someone when they are in difficulty", ["Adding a gift when someone already has plenty", "Helping no one", "Offering kind words only at New Year"], "Adding flowers to brocade makes something good even better; giving coal in snow helps someone who is cold and in need."),
        ("Which of these is an occupation?", "Architect", ["Furious", "Overjoyed", "Fragrance left on your hand"], "Architect, teacher, and animal keeper are occupations. Furious and overjoyed describe feelings."),
        ("What does “平时肯帮人，急时有人帮” mean?", "Help others in ordinary times, and they may help you in an emergency", ["Refuse to help in ordinary times, and people will help in an emergency", "Help others only in emergencies", "Helping others has nothing to do with you"], "Like the rose saying, this one is about mutual help."),
    ],
)

K(
    "g2b_shen", "Character Study: Ode to China", "识字写字", 2, "Second semester", 3, "conceptual",
    "Memorize “Ode to China” and understand its references to China, Taiwan, and unity.",
    "sz_12",
    [
        ("What is the next line after “我神州，称华夏”?", "山川美，可入画", ["黄河奔，长江涌", "长城长，珠峰耸", "台湾岛，隔海峡"], "The song first says the country's beautiful mountains and rivers look like a painting, then names the Yellow and Yangtze Rivers."),
        ("What is the next line after “黄河奔，长江涌”?", "长城长，珠峰耸", ["与大陆，是一家", "各民族，情谊浓", "山川美，可入画"], "After the rivers, the song mentions the Great Wall and Mount Everest."),
        ("After “台湾岛，隔海峡,” whom does the song say Taiwan is united with?", "与大陆是一家", ["与黄河是一家", "与珠峰隔海相望、互不相关", "只和长城是一家"], "The song says Taiwan Island is separated by a strait but is one family with the mainland."),
        ("How does the song describe the different ethnic groups?", "情谊浓，齐奋发", ["各自生活，互不往来", "只住在台湾岛上", "都住在长城下面"], "The song says the groups share deep bonds, strive together, and prosper together."),
    ],
)

K(
    "g2b_jie", "Character Study: Traditional Festivals", "识字写字", 2, "Second semester", 3, "conceptual",
    "Match “春节” (Spring Festival), “元宵” (Lantern Festival), “清明” (Qingming), “端午” (Dragon Boat Festival), “七夕” (Qixi), “中秋” (Mid-Autumn Festival), and “重阳” (Double Ninth Festival) with their customs.",
    "sz_12",
    [
        ("Which customs are associated with “端午节” (Dragon Boat Festival)?", "吃粽子、赛龙舟 (eat zongzi and race dragon boats)", ["赏月、吃月饼 (admire the moon and eat mooncakes)", "登高、赏菊 (climb high and admire chrysanthemums)", "看花灯 (view lanterns)"], "Dragon boats and zongzi are associated with the Dragon Boat Festival. Moon-gazing and mooncakes belong to Mid-Autumn Festival."),
        ("What do people often do for “中秋节” (Mid-Autumn Festival)?", "赏月、吃月饼 (admire the moon and eat mooncakes)", ["赛龙舟 (race dragon boats)", "扫墓踏青 (sweep tombs and go on spring outings)", "贴窗花放鞭炮 (put paper-cut decorations on windows and set off firecrackers)"], "People eat mooncakes beneath the full moon on the fifteenth day of the eighth lunar month."),
        ("What do people often do for “清明节” (Qingming)?", "扫墓、踏青 (sweep tombs and go on spring outings)", ["乞巧 (practice needlework for Qixi)", "看花灯 (view lanterns)", "登高插茱萸 (climb high and wear dogwood)"], "At Qingming, people visit ancestors' graves and go outdoors for spring outings. Needlework is associated with Qixi."),
        ("Which customs are associated with “重阳节” (Double Ninth Festival)?", "登高、敬老 (climb high and honor older people)", ["赛龙舟 (race dragon boats)", "贴春联 (put up Spring Festival couplets)", "吃元宵 (eat tangyuan)"], "Double Ninth Festival emphasizes respect for older people and includes autumn outings, chrysanthemum viewing, and climbing high. Couplets are for Spring Festival."),
    ],
)

K(
    "g2b_bei", "Character Study: The Story of “贝”", "识字写字", 2, "Second semester", 3, "conceptual",
    "Understand that shells were once used as currency and that characters related to money often contain the 贝 radical.",
    "sz_12",
    [
        ("What did people once use as money?", "Shells", ["Leaves", "Pebbles", "Snowflakes"], "Seashells were beautiful and hard to find, so people once used them as currency."),
        ("Why do “财、购、贫” all contain the 贝 radical?", "Their meanings relate to money or wealth", ["They all relate to water", "They all have the wood radical", "The 贝 radical indicates color"], "Many characters related to money contain the 贝 radical."),
        ("Which character contains the 贝 radical and relates to goods or money?", "货", ["明", "林", "跑"], "货 means goods and contains 贝. 明 combines sun and moon, 林 uses the wood radical, and 跑 uses the foot radical."),
        ("What does the 贝 radical suggest about “贫”?", "Its meaning relates to possessions or wealth", ["Its meaning relates to the sun", "It must be pronounced bèi", "It is the name of a tree"], "贫 means lacking possessions or wealth. Its 贝 radical is a clue to its meaning."),
    ],
)

K(
    "g2b_mei", "Character Study: Chinese Cuisine", "识字写字", 2, "Second semester", 3, "conceptual",
    "Learn “凉拌” (dress cold), “煎” (pan-fry), “烧” (braise), “烤” (roast), “煮” (boil), “爆” (flash-fry), “炖” (stew), “蒸” (steam), “炸” (deep-fry), and “炒” (stir-fry) through dish names, and distinguish the pronunciations of “炸.”",
    "sz_12",
    [
        ("Which group of dish names appears in the lesson?", "凉拌菠菜、香煎豆腐、红烧茄子", ["火锅、酸辣粉、汤圆", "汉堡、薯条、三明治", "年糕、月饼、粽子"], "The lesson includes these dishes as well as roast duck and boiled fish."),
        ("Which dish is a staple food in the lesson?", "炸酱面", ["葱爆羊肉", "水煮鱼", "小鸡炖蘑菇"], "Steamed dumplings, noodles with soybean paste, millet porridge, and egg fried rice are staples. The other options are main dishes."),
        ("What does “红烧” mean in “红烧茄子”?", "A cooking method", ["The name of a vegetable", "A utensil", "A festival"], "These words—mix, pan-fry, braise, roast, boil, stir-fry quickly, stew, steam, deep-fry, and stir-fry—are cooking methods."),
        ("How is “炸” pronounced in “炸酱面”?", "zhá", ["zhà", "zhā", "zà"], "In the dish name, 炸 is pronounced zhá. In words for an explosion or a bomb, it is pronounced zhà."),
    ],
)

K(
    "g2b_yd3", "Language Workshop 3: Semantic Radicals and the Zodiac", "识字写字", 2, "Second semester", 3, "conceptual",
    "Use the fire, heart, and knife radicals to infer meanings; read descriptive words such as “甜津津” and “香喷喷”; and learn the Chinese zodiac.",
    "sz_12",
    [
        ("What kind of word is “香喷喷,” and what does it describe?", "An ABB-pattern word that describes fragrance", ["An AABB-pattern word for occupations", "The name of a zodiac animal", "A cooking method"], "甜津津、酸溜溜、辣乎乎, and 香喷喷 all follow the ABB pattern and describe a taste or sensation."),
        ("What are characters with the vertical-heart or heart-bottom radical often related to?", "Feelings", ["Knives and scissors", "Fire and heat", "Money"], "Characters such as 情, 想, and 怕 contain a heart radical. Words about knives often use the standing-knife radical."),
        ("What are characters with the 火 or 灬 radical often related to?", "Fire or heat", ["Feelings", "Knives and scissors", "Rivers"], "Words such as 烧, 热, and 煮 relate to fire, not water. The four-dot bottom is a variation of 火."),
        ("In the Chinese zodiac, which animal comes right after “鼠”?", "牛", ["虎", "兔", "龙"], "子鼠、丑牛、寅虎、卯兔: 牛 follows 鼠, not 虎."),
    ],
)

K(
    "g2b_meng", "Reading: Colorful Dreams", "阅读理解", 2, "Second semester", 4, "reasoning",
    "Understand how the narrator uses colored pencils to imagine grass, flowers, and children in a dream.",
    "yd_12",
    [
        ("What does the narrator use to draw a colorful dream?", "A big handful of colored pencils", ["A piece of charcoal", "Colorless water", "The moon at night"], "The colorful dreams come from the pencils lying in the pencil case."),
        ("What colors are the lawn and wildflowers in the dream?", "Green and many different colors", ["All black", "Only white", "Their colors are blown away"], "The colored pencils draw a green lawn, many-colored flowers, and a blue sky."),
        ("What are the children doing in the dream?", "Singing and playing games in the woods", ["Building a snowman in winter", "Breaking every pencil", "Hiding so no one can see the colors"], "The colorful dream contains a lush forest where children play happily."),
        ("What is this children's poem mainly about?", "Beautiful images imagined with colored pencils", ["A colorless night", "How to sharpen pencils", "A dream in which nothing can be seen"], "Color and imagination are the poem's main ideas."),
    ],
)

K(
    "g2b_chuma", "Reading: A Remarkable Horse", "阅读理解", 2, "Second semester", 4, "reasoning",
    "Understand how the mother gives her tired daughter a willow branch as a pretend horse, and the girl runs home by herself.",
    "yd_12",
    [
        ("What happens to the younger sister during the walk?", "She gets tired and wants someone to carry her", ["She runs home ahead of everyone", "She washes a willow branch in the stream", "She helps her mother cut down a tree"], "The younger sister is tired and does not want to go any farther."),
        ("What does the mother pick up beside the road for her?", "A willow branch", ["A real horse", "A bicycle", "A shovel"], "Instead of carrying her, the mother gives her a willow branch."),
        ("What does the girl pretend the willow branch is?", "A horse", ["A stream", "A pair of scissors", "A straw hat"], "She puts the willow branch between her legs and pretends to ride it."),
        ("How does the younger sister get home?", "She rides her pretend horse and runs home by herself", ["She sits beside the road until Dad carries her", "The willow branch walks home alone", "She becomes even more tired"], "The remarkable pretend horse helps the tired girl run all the way home."),
    ],
)

K(
    "g2b_xi", "Reading: The Magpies in the Maple Tree", "阅读理解", 2, "Second semester", 4, "reasoning",
    "Understand how the narrator loves the magpies in a maple tree near the ferry and imagines understanding the magpie mother's and chicks' conversations.",
    "yd_12",
    [
        ("Where does the maple tree grow, and what does it resemble?", "Beside a ferry crossing, like a green sun umbrella", ["In a desert, like a pair of scissors", "At Temple of Heaven Park, like a cypress sapling", "In the snow, like a castle"], "The leafy maple beside the ferry crossing looks like an open sun umbrella."),
        ("What does the narrator call the adult magpie by the nest?", "Auntie Magpie", ["Grandpa Magpie", "Uncle Giraffe", "Mr. Mole"], "Like a character in a fairy tale, the narrator calls her Auntie Magpie."),
        ("What does the narrator call the young magpies in the nest?", "Little Brother Magpies", ["Teacher Magpie", "Customer Magpie", "Postman Magpie"], "The narrator calls the young birds Little Brother Magpies."),
        ("What does Auntie Magpie teach the young birds by the nest?", "To sing and play games", ["To sell a pond", "To plant trees", "To race dragon boats"], "She teaches them to sing and play games, and the narrator imagines understanding them."),
    ],
)

K(
    "g2b_yd4", "Language Workshop 4: Toys and Trustworthiness", "识字写字", 2, "Second semester", 4, "conceptual",
    "Recognize “拨浪鼓” (a rattle drum) and “不倒翁” (a roly-poly toy), pronounce “倒” correctly in context, and learn the sayings “失信不立” and “诚信者，天下之结也.”",
    "sz_12",
    [
        ("How is “倒” pronounced in “不倒翁”?", "dǎo", ["dào", "diào", "dōu"], "An 不倒翁 tips over and then stands back up, so 倒 is pronounced dǎo here."),
        ("How is “倒” pronounced in “把水倒进杯子”?", "dào", ["dǎo", "táo", "dù"], "In phrases for pouring water or turning a vehicle around, 倒 is pronounced dào. The pronunciation depends on the word."),
        ("What does “失信不立” mean?", "Without trustworthiness, you cannot establish yourself", ["Trustworthy people fall down", "It is fine to break your word", "Trust matters only in toy stores"], "The saying comes from the Zuo Tradition. Without trust, a person or undertaking cannot stand."),
        ("What does “诚信者，天下之结也” emphasize?", "Trustworthiness connects people throughout the world", ["Trustworthiness is only a private matter", "People do not need to keep their word", "A knot is the name of a toy"], "The saying comes from Guanzi. Trustworthiness is the bond that brings people together."),
    ],
)

K(
    "g2b_yang", "Reading: Mending the Sheep Pen (亡羊补牢)", "阅读理解", 2, "Second semester", 5, "reasoning",
    "Understand that repairing the sheep pen after losing a sheep is still worthwhile.",
    "yd_12",
    [
        ("Why does the shepherd lose a sheep the first time?", "There is a hole in the pen, and a wolf enters at night", ["The sheep wanders off even though the pen is sound", "He gives a sheep to a neighbor", "The sheep gets too hot in the pen during the day"], "He does not repair the hole, so a wolf slips through and carries off a sheep."),
        ("What does the neighbor urge him to do?", "Repair the sheep pen right away", ["Stop raising sheep", "Leave the hole open", "Wait until every sheep is lost before repairing it"], "The neighbor tells him to fix the pen."),
        ("What does the shepherd think at first?", "The sheep is already lost, so repairing the pen will not help", ["He repairs the pen at once", "He chases the wolf all night", "He follows the advice immediately"], "He thinks repairing the pen will make no difference after the sheep is gone, so he does nothing."),
        ("After losing another sheep the next day, what does he realize?", "It is not too late to repair the pen; he should close the hole", ["He no longer needs to worry about the sheep", "It is better to leave the hole open", "The neighbor is always wrong"], "After losing another sheep, he finally closes the hole. He does not lose any more sheep."),
    ],
)

K(
    "g2b_ya", "Reading: Pulling Up Seedlings to Help Them Grow (揠苗助长)", "阅读理解", 2, "Second semester", 5, "reasoning",
    "Understand how a farmer pulls up his seedlings to make them grow faster, only to cause them to wither.",
    "yd_12",
    [
        ("Why does the farmer pull up the seedlings?", "He thinks they are growing too slowly and wants to help them grow taller faster", ["They have already grown taller than he is", "A neighbor asks him to pull them out", "It is going to rain and flood them"], "He wants the seedlings to grow faster. He checks every day but still thinks they are growing too slowly."),
        ("What does he do?", "He pulls each seedling upward", ["He waters and fertilizes them", "He moves them indoors", "He asks others to wait with him"], "He rushes into the field, pulls the seedlings much taller, and becomes exhausted."),
        ("What does he say when he gets home?", "I helped the seedlings grow taller today.", ["I killed the seedlings today.", "The seedlings grew quickly on their own.", "I should not have pulled them up."], "He does not realize that his actions are harmful and happily tells his family what he has done."),
        ("What happens in the end?", "All the seedlings wither and die", ["They grow into trees overnight", "They grow better than the other field's crops", "Only one seedling withers"], "His son finds that all the seedlings have withered. Going against the way plants grow only makes things worse."),
    ],
)

K(
    "g2b_tao", "Reading: Drawing a Starfruit", "阅读理解", 2, "Second semester", 5, "reasoning",
    "Understand why the narrator draws the starfruit as a five-pointed star when viewing it from the side.",
    "yd_12",
    [
        ("What does the narrator draw the starfruit as?", "A five-pointed star", ["A round apple", "A bird", "An umbrella"], "From a seat near the front and to one side, one end of the starfruit looks like a five-pointed star."),
        ("Why does the narrator's drawing look different from the classmates' drawings?", "The viewing angle is different, so the shape looks different", ["The starfruit changes color", "The narrator cannot see the fruit", "The teacher forbids copying it"], "The same starfruit looks different from the front and from the side."),
        ("How does the teacher ask the class to check?", "Take turns sitting in the narrator's seat and looking", ["Tear up every drawing and redraw the same circle", "Stop looking at the starfruit", "Listen only to the students at the front of the room"], "When they sit in that spot, they also see the fruit as a five-pointed star."),
        ("What do the father and teacher both want the narrator to remember?", "Draw things as they appear", ["If others draw a circle, draw one too", "The less accurate the drawing, the better", "It is fine not to draw what you see"], "Be truthful to what you see. If the fruit looks like a star from your seat, do not change it to match someone else's view."),
    ],
)

K(
    "g2b_ma", "Reading: The Little Horse Crosses the River", "阅读理解", 2, "Second semester", 5, "reasoning",
    "Understand why the old ox says the water is shallow, the squirrel says it is deep, and the little horse tries it for itself.",
    "yd_12",
    [
        ("Why does the little horse need to cross the river?", "To carry half a sack of wheat home", ["To play with the squirrel", "The old ox tells it to cross", "It wants to measure the river"], "The miller asks the little horse to carry the wheat home, but a river blocks the way."),
        ("Why do the old ox and squirrel disagree about the water?", "The tall ox finds it shallow, while the small squirrel finds it deep", ["They are talking about different rivers", "The squirrel has never seen the river", "The old ox wants to trick the horse"], "The water reaches only the old ox's lower legs, but the squirrel is short and once saw a friend swept away."),
        ("What does the mother tell the little horse to do?", "Think for itself and try crossing", ["Listen to the ox, not the squirrel", "Listen to the squirrel and drop the wheat", "Never cross a river"], "The mother says the little horse can find out whether the water is deep or shallow by trying it."),
        ("After the little horse tries, how deep is the river?", "Neither as shallow as the ox said nor as deep as the squirrel said", ["Too deep to cross", "So shallow that its hooves stay dry", "It dries up the next day"], "The water reaches just below the little horse's knees. Other people's experience still needs to be tested for yourself."),
    ],
)

K(
    "g2b_yd5", "Language Workshop 5: Share Your Opinion", "阅读理解", 2, "Second semester", 5, "reasoning",
    "After reading fables and “Drawing a Starfruit,” describe what the characters did before sharing your own view.",
    "yd_12",
    [
        ("What should you explain first when sharing your opinion?", "What someone in the story did, then what you think about it", ["A story unrelated to the text", "Only “I don't know”", "A new title for the story"], "Keep your opinion tied to the text. Describe the action and result first so others know which story you mean."),
        ("Why is it not enough to reduce a lesson to a four-character phrase?", "Others cannot hear your own reasoning", ["Four characters are always more accurate than the story", "That alone proves you finished reading", "You cannot explain a lesson in your own words"], "The idioms 亡羊补牢 and 揠苗助长 each have four characters. Explain in your own words why the lesson matters."),
        ("When discussing “Drawing a Starfruit,” what should you remember?", "Look carefully and describe what you actually see", ["If someone else says it is round, say it is round too", "Make things up even if you have not seen them", "An unusual opinion is best, even if it ignores the story"], "Different angles show different shapes. Speak truthfully about what you see."),
        ("What should you do when a classmate has a different opinion?", "Listen first, then explain your reasons", ["Interrupt immediately", "Pretend to agree and say nothing", "Stop the classmate from speaking"], "Listening before responding helps everyone explain their ideas more clearly."),
    ],
)

K(
    "g2b_jue", "Poem: Quatrain (Two Golden Orioles)", "古诗文积累", 2, "Second semester", 6, "conceptual",
    "Memorize Du Fu's seven-character “Quatrain” and distinguish it from the five-character poem beginning “迟日江山丽.”",
    "gs_12",
    [
        ("What is the next line after “两个黄鹂鸣翠柳”?", "一行白鹭上青天", ["窗含西岭千秋雪", "门泊东吴万里船", "迟日江山丽"], "A line of egrets flying into the sky comes next; the window framing the western mountains and the boat moored by the door follow later. “迟日江山丽” is from another poem."),
        ("What is the next line after “窗含西岭千秋雪”?", "门泊东吴万里船", ["一行白鹭上青天", "两个黄鹂鸣翠柳", "门泊东吴万里帆"], "The window frames snow on the western mountains, and the final line describes a boat bound for Wu. The poem says 船, not 帆."),
        ("Who wrote the seven-character “Quatrain” that begins “两个黄鹂鸣翠柳”?", "Du Fu", ["Li Bai", "He Zhizhang", "Du Mu"], "Du Fu wrote this seven-character quatrain. Du Mu wrote “Mountain Travel” and “Qingming,” so do not confuse poets with the same surname."),
        ("From where does the speaker see the snow in “窗含西岭千秋雪”?", "From a window overlooking snow on the western mountains", ["From a boat on the river", "From a willow tree where orioles are perched", "From the sky where egrets are flying"], "The window frames the distant mountains and their ancient snow. The orioles are in the green willows, and the egrets are in the blue sky."),
    ],
)

K(
    "g2b_xiao", "Poem: Leaving Jingci Temple at Dawn to See Lin Zifang Off", "古诗文积累", 2, "Second semester", 6, "conceptual",
    "Memorize Yang Wanli's poem about West Lake's lotus flowers in June and distinguish it from Su Shi's poetry.",
    "gs_12",
    [
        ("What is the next line after “毕竟西湖六月中”?", "风光不与四时同", ["接天莲叶无穷碧", "映日荷花别样红", "欲把西湖比西子"], "The first couplet says West Lake in June looks different from every other season. The lotus leaves and flowers are described later; the comparison to a beauty comes from Su Shi."),
        ("What is the next line after “接天莲叶无穷碧”?", "映日荷花别样红", ["风光不与四时同", "接天莲叶无穷绿", "小荷才露尖尖角"], "The lotus leaves stretch to the horizon in deep green, and the sunlit flowers are especially red. The poem says 碧, not 绿."),
        ("Who wrote this poem?", "Yang Wanli", ["Su Shi", "Du Fu", "Li Bai"], "Yang Wanli wrote “Leaving Jingci Temple at Dawn to See Lin Zifang Off.” Su Shi wrote “After Rain on the Lake.”"),
        ("In what month does the poem describe West Lake's lotus flowers?", "June", ["The first day of the first lunar month", "The Qingming season", "A Mid-Autumn night"], "The poem begins by placing the scene at West Lake in June. The first lunar month is associated with “New Year's Day,” and Qingming appears in another poem."),
    ],
)

K(
    "g2b_yu", "Reading: Thunderstorm", "阅读理解", 2, "Second semester", 6, "reasoning",
    "Describe the changes before, during, and after the thunderstorm in order.",
    "yd_12",
    [
        ("How do the sky and wind change before the rain begins?", "Dark clouds roll in, and the wind grows stronger", ["The sun turns redder", "A rainbow appears", "The leaves do not move"], "Dark clouds fill the sky, and the wind tosses the tree branches."),
        ("How does the rain fall?", "It grows heavier and eventually pours down", ["A few drops fall and then stop", "A light rain continues without changing", "It rains only far away"], "The rain grows so heavy that the trees and houses outside are hard to see."),
        ("What happens after the rain stops?", "A rainbow appears, and the cicadas and spider come out again", ["Snowflakes fly", "The clouds grow darker", "The frogs hide and fall silent"], "The sun comes out, a rainbow appears, the cicadas call, and the spider returns to its web."),
        ("What sequence should you follow when reading this story?", "Before, during, and after the thunderstorm", ["Only what happens afterward", "Start after the rain and work backward", "Remember only the spider"], "The story follows the events before the rain, during the storm, and after it stops."),
    ],
)

K(
    "g2b_mi", "Reading: If You Lose Your Way Outdoors", "阅读理解", 2, "Second semester", 6, "reasoning",
    "Understand how the sun, Polaris, trees, and snow in ditches can help you find direction.",
    "yd_12",
    [
        ("Where is the sun at midday?", "In the south", ["In the north", "Under the tree roots to the east", "In a ditch to the west"], "At midday, the sun is in the south, and shadows on the ground point north."),
        ("Which direction does Polaris help you find?", "North", ["South", "The direction of sunrise", "The side where snow melts faster"], "Polaris is like a guiding lamp, fixed in the northern sky."),
        ("Which side of a tree has denser branches and leaves?", "The south side", ["The north side", "Directly under the roots", "The ditch water"], "Branches and leaves are denser on the south side and sparser on the north side."),
        ("If clouds and rain hide the sun, what else can help you find direction?", "Tree branches and leaves, or how quickly snow melts on different sides of a ditch", ["Only the color of a watch", "Only the hooks on your shoes", "Only the magpies' calls"], "Trees can help on cloudy days. Differences in how quickly snow melts can also show north and south."),
    ],
)

K(
    "g2b_tai", "Reading: Fun Facts About Life in Space", "阅读理解", 2, "Second semester", 6, "reasoning",
    "Understand why people secure themselves while sleeping in space, use straws to drink, and wear shoes with hooks for walking.",
    "yd_12",
    [
        ("What should you do with your body when sleeping in space?", "Get into a sleeping bag and secure yourself", ["Lie on the floor so you do not float", "Sleep only while standing", "Leave yourself unsecured, as at home"], "People float in space, so they need to strap themselves in while sleeping."),
        ("Why do astronauts often use straws to drink in space?", "Without one, the water would float away", ["Cups are larger than on Earth", "There is no water in space", "Straws are used to secure shoes"], "Water does not stay in a cup by itself; a straw lets astronauts draw it in."),
        ("What is special about shoes for walking inside a space capsule?", "They have hooks on the soles to catch the grid", ["They have wheels on the soles", "Astronauts must go barefoot", "The shoes must be filled with water"], "Without hooks to hold their feet in place, people would float away and be unable to walk."),
        ("What causes these unusual experiences?", "People float in space", ["It rains every day in space", "Trees in space are especially tall", "There is no sun in space"], "Sleeping, drinking, walking, and bathing are all affected by weightlessness, which makes them unusual."),
    ],
)

K(
    "g2b_yd6", "Language Workshop 6: Solar Terms and Questions", "古诗文积累", 2, "Second semester", 6, "conceptual",
    "Memorize the 24 solar terms song, pronounce “处” correctly in “处暑,” and write a “为什么……” question about nature.",
    "gs_12",
    [
        ("What is the next line after “春雨惊春清谷天”?", "夏满芒夏暑相连", ["秋处露秋寒霜降", "冬雪雪冬小大寒", "春风吹又生"], "The first line lists spring solar terms; the next line continues with the summer terms: Start of Summer, Grain Buds, Grain in Ear, Summer Solstice, Minor Heat, and Major Heat."),
        ("What is the next line after “秋处露秋寒霜降”?", "冬雪雪冬小大寒", ["夏满芒夏暑相连", "春雨惊春清谷天", "野火烧不尽"], "Winter follows autumn, with Start of Winter, Minor Snow, Major Snow, Winter Solstice, Minor Cold, and Major Cold."),
        ("How is “处” pronounced in “处暑”?", "chǔ", ["chù, as in “到处”", "chú, not used in this context", "cù, not a reading of this character"], "In 处暑 and 处理, 处 is pronounced chǔ. In 到处 and 处所, it is chù. The 芒 in 芒种 is máng."),
        ("What kind of sentence should you write in the nature-writing activity?", "A question beginning “为什么……” about something you observe", ["Turn all 24 solar terms into one slogan", "Write only an exclamation mark", "Copy a poem you have already memorized"], "The writing prompt is about a question in your mind. Describe what you observe, then ask why."),
    ],
)

K(
    "g2b_xiang", "Reading: The Elephant's Ears", "阅读理解", 2, "Second semester", 7, "reasoning",
    "Understand that the elephant's ears are like fans and that raising them makes him uncomfortable.",
    "yd_12",
    [
        ("What are the elephant's ears like naturally?", "They hang down like fans", ["They stand straight up like a rabbit's ears", "They are too small to see", "They flap constantly"], "The elephant's large ears hang down like fans."),
        ("Why do the small animals say something is wrong with the elephant's ears?", "They think ears should stand up", ["The elephant's ears are too big", "The elephant cannot hear", "There is no hair on the ears"], "The rabbit, lamb, and others have upright ears, so they assume the elephant's ears must be faulty."),
        ("What happens after the elephant raises his ears?", "Bugs fly into them, which bothers him", ["He hears better and never lets them droop again", "His ears stop moving", "The small animals stop visiting"], "When his ears stand up, bugs can fly inside easily. The elephant shakes his head and tries to chase them away."),
        ("What does the elephant eventually understand?", "Other people are themselves, and he is himself; drooping ears are more comfortable", ["If others say to raise them, keep them raised forever", "His ears should be cut off", "Fan-shaped ears are a defect"], "He lets his ears droop again and feels more comfortable. What suits someone else may not suit you."),
    ],
)

K(
    "g2b_zhu", "Reading: The Spider's Shop", "阅读理解", 2, "Second semester", 7, "reasoning",
    "Understand how the spider tries selling masks, scarves, and socks to a hippopotamus, a giraffe, and a centipede.",
    "yd_12",
    [
        ("Why does the spider decide to open a shop?", "It feels lonely and bored waiting on its web for flying insects", ["It already has many customers", "The hippopotamus asks it to open a shop", "It wants to walk in space"], "The spider gets tired of waiting for little insects and decides to open a shop."),
        ("Who comes for a mask, and what happens?", "A hippopotamus; its mouth is so large that weaving the mask takes the whole day", ["A giraffe; its long neck makes the job quick", "A centipede; it has few legs, so weaving is easy", "The hippopotamus buys nothing, and the spider closes immediately"], "The sign says each customer pays one yuan, but the hippopotamus needs a very large, difficult mask."),
        ("Who comes for a scarf, and how long does the spider work?", "A giraffe; it works for a whole week", ["A hippopotamus; it works for one minute", "A centipede; it finishes in an hour", "No customer comes, and the scarf grows by itself"], "The giraffe's neck is as tall as a tree, so the scarf must be very long."),
        ("Who is the third customer, and what does the spider do?", "A centipede with 42 legs; the spider is frightened and runs back to its web", ["The hippopotamus returns, and the spider is delighted", "The giraffe buys socks, making the spider rich", "No customers come, but the spider keeps the shop open"], "The socks seem small, but the centipede has too many feet. The spider hurries back to its web."),
    ],
)

K(
    "g2b_qing", "Reading: The Frog Sells the Pond", "阅读理解", 2, "Second semester", 7, "reasoning",
    "Understand how the frog improves the pond based on others' suggestions and finally decides to keep it.",
    "yd_12",
    [
        ("What does the frog plan to do with the pond at first?", "Sell it", ["Fill it in to make a road", "Invite the spider to open a shop", "Move to Temple of Heaven Park"], "The pond is barren and unpleasant, so the frog calls out that it wants to sell it."),
        ("When animals say there is too little water and the surroundings are bare, what does the frog do?", "Brings in water, plants grass and trees, and makes improvements step by step", ["Gives the pond away immediately without changing anything", "Chases away the animals who offer suggestions", "Drains the pond to make it even drier"], "After each suggestion, the frog works to add what is missing."),
        ("What does the frog decide after the pond improves?", "It is so lovely that the frog will keep it instead of selling it", ["Sell it cheaply to the first passerby", "Keep advertising it without living there", "Pull up all the grass and trees"], "The pond becomes an attractive place to live, so the frog stops trying to sell it."),
        ("What is the main message of this story?", "Taking action can improve a place that was once unpleasant", ["Stop working whenever someone offers advice", "A pond can never be sold", "Other people's suggestions are useless"], "The frog makes one improvement after another until the once-unsellable pond becomes a place it wants to keep."),
    ],
)

K(
    "g2b_chong", "Reading: The Little Caterpillar", "阅读理解", 2, "Second semester", 7, "reasoning",
    "Understand how the little caterpillar patiently does its own work and eventually becomes a butterfly.",
    "yd_12",
    [
        ("How do the other insects see the little caterpillar?", "They think it is slow and cannot do anything", ["They think it is already a butterfly", "They invite it to sell a pond", "They ask it to spin a cocoon with them"], "The other insects fly among the flowers, while the slow-moving caterpillar crawls along and gets laughed at."),
        ("What does the little caterpillar do?", "It does not rush and works carefully each day", ["It competes with others to see who can fly highest", "It stops eating leaves", "It cuts open its cocoon and goes home"], "It knows each step prepares it for what comes later, so it does not panic."),
        ("What does the little caterpillar become?", "A butterfly", ["A spider", "A frog", "A magpie"], "It forms a cocoon and later emerges as a butterfly."),
        ("What does the story teach readers?", "Do not give up because you are slow for now; growing takes time and steady effort", ["The slower you are, the better; there is nothing to do", "Only flying counts as effort", "You can stop learning after becoming a butterfly"], "There is no need to panic. Finish the work you need to do, and change will come in time."),
    ],
)

K(
    "g2b_yd7", "Language Workshop 7: Cleaning Day", "识字写字", 2, "Second semester", 7, "conceptual",
    "Recognize “扫帚” (broom), “抹布” (cleaning cloth), “拖把” (mop), “簸箕” (dustpan), and “水桶” (bucket); name tasks such as “扫地” (sweep), “擦玻璃” (clean windows), “倒垃圾” (empty the trash), and “摆桌椅” (arrange tables and chairs).",
    "sz_12",
    [
        ("Which tool is commonly used to “扫地” (sweep the floor)?", "扫帚 (broom)", ["抹布 (cleaning cloth)", "雨衣 (raincoat)", "柳条 (willow branch)"], "A 扫帚 is used for sweeping; a 抹布 is used for wiping."),
        ("Which tool is commonly used to “擦玻璃” (clean windows)?", "抹布 (cleaning cloth)", ["簸箕 (dustpan)", "水桶盖 (bucket lid)", "拨浪鼓 (rattle drum)"], "A 抹布 can wipe windows and tables. A 簸箕 collects rubbish."),
        ("Which tool is commonly used to collect rubbish?", "簸箕 (dustpan)", ["拖把的绳子 (a mop string)", "七巧板 (a tangram)", "不倒翁 (a roly-poly toy)"], "A 簸箕 and broom work together to collect rubbish."),
        ("Which group consists entirely of cleaning tasks?", "扫地、擦玻璃、倒垃圾、摆桌椅 (sweep, clean windows, empty the trash, and arrange the tables and chairs)", ["Sell masks, knit scarves, and knit socks", "Shoot down the sun, build a boat, and dig a river channel", "Admire the moon, race dragon boats, and practice needlework"], "A thorough cleanup means sweeping the floor, cleaning the windows, emptying the trash, and arranging the tables and chairs."),
    ],
)

K(
    "g2b_yi", "Reading: Hou Yi Shoots Down Nine Suns", "阅读理解", 2, "Second semester", 8, "reasoning",
    "Understand how Hou Yi shoots down nine of ten suns and leaves one in the sky.",
    "yd_12",
    [
        ("How many suns appear in the sky at the beginning of the story?", "Ten", ["One", "Nine", "Two"], "All ten suns scorch the land, withering crops and making life unbearable."),
        ("How many suns does Hou Yi shoot down?", "Nine", ["Ten", "One", "None"], "He leaves the one people still need and shoots down the other nine."),
        ("Why can he not shoot down every sun?", "People still need the remaining sun for light and warmth", ["The suns are too small to hit", "He does not have ten arrows", "The other nine suns set by themselves"], "Without a sun, the world would be dark and cold, so one must remain."),
        ("What harm do the ten suns cause?", "They scorch the land and wither the crops", ["Floodwaters sweep away homes", "The pond cannot be sold", "The caterpillar cannot fly"], "This story is about heat and drought. Flooding is the disaster in “The Great Yu Controls the Flood.”"),
    ],
)

K(
    "g2b_huang", "Reading: The Legend of the Yellow Emperor", "阅读理解", 2, "Second semester", 8, "reasoning",
    "Understand how the Yellow Emperor thinks of a cart after seeing a rolling hat and a boat after seeing a leaf floating on water.",
    "yd_12",
    [
        ("What other name does the Yellow Emperor have in the story?", "Xuanyuan", ["Yu the Great", "Hou Yi", "Lei Feng"], "The story calls him Xuanyuan. Yu the Great and Hou Yi appear in other legends."),
        ("What does he see that gives him the idea to build a cart?", "A hat rolling across the ground in the wind", ["Ants floating on a leaf", "Ten suns appearing together", "A magpie teaching its chicks to sing"], "The hat rolls along, giving him the idea of wheels and a cart."),
        ("What does he see that gives him the idea to build a boat?", "A dry leaf floating on water with an ant on it", ["A hat rolling down a mountain", "A crooked cypress sapling", "A hole in a sheep pen"], "A leaf can float on the surface, so people can travel across a river in a boat."),
        ("What do carts and boats improve?", "Travel on land and water", ["The number of suns in the sky", "The price of the pond", "The magpies' language"], "Carts and boats make long-distance travel and river crossings easier."),
    ],
)

K(
    "g2b_dayu", "Reading: The Great Yu Controls the Flood", "阅读理解", 2, "Second semester", 8, "reasoning",
    "Understand how Yu channels floodwaters through river channels and into the sea.",
    "yd_12",
    [
        ("How do people suffer when the floods spread?", "Fields are submerged and homes are destroyed", ["Ten suns appear everywhere", "The pond sells well", "People only need to close the windows"], "The floodwaters cover fields and destroy homes, leaving people in great distress."),
        ("How is Yu's method different from simply blocking the water?", "Yu channels the water through opened river paths instead of relying only on dams", ["He blocks every outlet too", "He does not lead people in the work", "He directs the floods into people's homes"], "Blocked water can burst through again. Yu cuts through mountains and digs channels to give the floodwater a way out."),
        ("What happens after Yu opens the river channels?", "The floodwater flows into the sea", ["It turns into ten suns", "It stays in a sheep pen", "A spider knits it into a scarf"], "The water stops spreading once it has a route to flow away."),
        ("What do people later call him?", "Yu the Great", ["Xuanyuan", "Hou Yi", "Uncle Lei Feng"], "After the floods recede and people can live in peace, they respectfully call him Yu the Great."),
    ],
)

K(
    "g2b_yd8", "Language Workshop 8: Make Sentences Vivid", "习作基础", 2, "Second semester", 8, "procedural",
    "Use actions to show feelings, narrate a short event in order, and memorize Fan Zhongyan's “The Fisherman on the River.” Speak slowly when recommending a cartoon so others can follow.",
    "xz_12",
    [
        ("What is the next line after “江上往来人”?", "但爱鲈鱼美", ["君看一叶舟", "出没风波里", "映日荷花别样红"], "The poem says people love the delicious bass; the small boat in the wind and waves appears later. The lotus line is by Yang Wanli."),
        ("How is “没” pronounced in “出没风波里”?", "mò", ["méi, as in “没有”", "the second tone of mò", "the fourth tone of méi"], "In 出没, 没 is pronounced mò and means “appear and disappear.” In 没有, it is pronounced méi. Fan Zhongyan wrote the poem."),
        ("Which sentence makes “高兴极了” more vivid?", "他高兴极了，蹦蹦跳跳地跑过去。", ["他高兴极了。", "他高兴高兴极了极了。", "极了高兴他。"], "The workshop pairs an emotion with an action. Bouncing and skipping show how happy the person is; crying can show sadness."),
        ("Which paragraph puts a small event in the correct order?", "我先起床，接着洗脸，然后吃早饭，最后背上书包出门。", ["我出门，然后才起床，接着已经到了学校。", "最后吃饭，先到学校，接着起床。", "书包早饭洗脸出门。"], "First, next, then, and finally should match the order in which the events really happen."),
    ],
)
