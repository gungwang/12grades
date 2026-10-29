# -*- coding: utf-8 -*-
"""Grade 3, Books 1 and 2. Book 1 follows the 2025 autumn revision of the unified 6-3 curriculum; Book 2 follows the 2026 spring revision, lesson by lesson."""
from zh_lib import K

# Exact Chinese glyphs and terms, radical glyphs, patterned words, idioms, and quoted poetry or classical-text phrases below are retained only as assessed content; surrounding prose is translated.
# The "上"/"下" semester values are parser-required tokens consumed by K.
# ---------- Grade 3, Book 1 ----------
# 2025 autumn revision (6-3 system). Unit 2 poems: "Looking at Dongting Lake," "Mountain Walk," and "What I Saw at Night"; "To Liu Jingwen" is no longer included.
# Unit 3 focuses on prediction: "The Old House That Never Fell Down," "The Stubborn Tortoise," and "The Dog That Learned to Bark."
# Unit 4 features fairy tales: "The Secret of the Magic Gourd" (excerpt), "A Trip Inside the Cow's Stomach," and "A Piece of Cheese"; "The Tree of Last Year" is no longer included.
# Unit 5 includes "The Bird That Brought Us a Boat," "The Golden Meadow," and the writing task "A Colorful World Through Our Eyes"; there is no language arts review.
# Unit 6 includes "The Rich Xisha Islands," "A Seaside Town," "Beautiful Xiaoxing'anling," and "Hong Kong, the Pearl of the Orient."
# Unit 7 includes the poems "Deer Enclosure," "Looking at Tianmen Mountain," and "Drinking by the Lake After Rain"; it also features "The Sounds of Nature" and "An Endless Book."
# Unit 8 includes "Sima Guang," "Determined to Succeed," "The Operating Table Is the Battlefield," and "A Coarse-Porcelain Bowl"; "The Sparrow" is no longer included.

K(
    "g3a_da", "Reading: “The Primary School Under the Big Green Tree”", "Reading Comprehension", 3, "上", 1, "reasoning",
    "Understand that this is a frontier school where children from different ethnic groups study together.",
    "yd_34",
    [
        ("In what kind of place is the school in the passage?", "On the frontier", ["In the center of a busy city", "In a fishing village on an island", "In a private school with only one courtyard"], "The passage describes it as a beloved frontier school."),
        ("What is special about the children who attend the school?", "Children from several ethnic groups study together", ["All the children belong to one ethnic group", "They are all teachers from elsewhere", "There are no students"], "Han, Dai, Jingpo, and other children walk the same road to school."),
        ("Where do the children often play after class?", "Under a large green tree", ["In a well", "Beside a jar", "Under the sea"], "The shade of the large green tree and the phoenix bamboo is where they play and dance."),
        ("What is most memorable about this school?", "Children from different ethnic groups learn and play together", ["There are no classes", "No one speaks to anyone else", "There are teachers but no students"], "The children wear bright clothes and study together in the same classroom."),
    ],
)

K(
    "g3a_hua", "Reading: “The School of Flowers”", "Reading Comprehension", 3, "上", 1, "reasoning",
    "Read Rabindranath Tagore's prose poem: flowers go to school underground, take a holiday when it rains, and hurry back to their mothers in the sky.",
    "yd_34",
    [
        ("Who wrote “The School of Flowers”?", "Rabindranath Tagore", ["Zhang Tianyi", "Ye Shengtao", "Gianni Rodari"], "Tagore wrote this poem. Zhang Tianyi wrote “The Secret of the Magic Gourd,” and Gianni Rodari wrote “The Dog That Learned to Bark.”"),
        ("Where does the speaker imagine the flowers go to school?", "An underground school", ["The primary school under the big green tree", "A teacher's private school", "A classroom above the stars"], "The flowers do their lessons underground with the door closed. The stars' home is their home, not their school."),
        ("What does the teacher do when the flowers want to come out before the rain?", "Makes them stand in the corner", ["Gives them an immediate holiday", "Takes them to find their mothers in the sky", "Lets them dance under the big green tree"], "They are not allowed out during lessons. They get a holiday when the rain comes."),
        ("Where do the flower children hurry after school is canceled?", "To the place where the stars live, to find their mothers", ["To ask a teacher a question at a private school", "To see fish in the Xisha Islands", "Into a cow's stomach"], "They rush out in purple, yellow, and white clothes with their arms raised because they have mothers of their own."),
    ],
)

K(
    "g3a_dong", "Reading: “Ask When You Don't Understand”", "Reading Comprehension", 3, "上", 1, "reasoning",
    "Understand how Sun Yat-sen asked his teacher when he did not understand something as a child, and how the teacher praised him.",
    "yd_34",
    [
        ("Which curious child appears in the passage?", "Sun Yat-sen", ["Sima Guang", "Vladimir Lenin", "Cao Chong"], "The passage is about Sun Yat-sen studying at a private school as a boy."),
        ("How did the teacher have the students read?", "They repeated the words together, nodding along", ["They discussed the meaning first", "They read silently and were not allowed to speak", "They stopped reading when they went home"], "At the time, the students did not understand the sentences; they only repeated them together after the teacher."),
        ("What did Sun Yat-sen do that surprised his classmates?", "He stood up and asked the teacher what a sentence meant", ["He closed his book and left", "He jumped into a water jar", "He told others not to ask questions"], "The classmates were stunned because students usually did not interrupt the teacher."),
        ("How did the teacher respond?", "He said it was good to ask when you don't understand", ["He said questions should be punished", "He said books only need to be memorized", "He said no one could ask again"], "The teacher praised him: learning means asking, and asking helps you understand."),
    ],
)

K(
    "g3a_yinxu", "Language Arts Unit 1: Alphabetical Dictionary Lookup", "Character Recognition and Writing", 3, "上", 1, "procedural",
    "When the pronunciation is known, look up a word by the first letter of its syllable. In the speaking task “My Summer Vacation,” clearly describe one thing you did; in “Guess Who,” let others guess from a person's traits without naming them.",
    "sz_34",
    [
        ("You know that “花” is pronounced huā. Which lookup method should you use first?", "Alphabetical lookup by pronunciation", ["Lookup by radical", "Start flipping from the last page", "Look only at the illustrations"], "When you know the pronunciation, use alphabetical lookup; use the radical method when you do not."),
        ("For “花 huā,” which letter should you look under?", "The letter H", ["The letter F", "The letter U", "The letter A"], "The pinyin for “花” is huā. Use the first letter, h, and look under H."),
        ("For “山 shān,” which letter should you look under?", "The letter S", ["The letter H", "The letter C", "The letter Z"], "The initial in “山” is sh, and alphabetical lookup uses its first letter, s. Do not choose a different letter because sh is retroflex."),
        ("What is the first step in alphabetical lookup?", "Find the first letter of the syllable", ["Count the strokes in the radical", "Turn the dictionary upside down", "Guess a completely different pronunciation"], "Alphabetical lookup follows letter order: find the first letter, then look for the syllable in that section."),
    ],
)

K(
    "g3a_cha", "Language Arts Unit 1: Dictionary Lookup by Radical", "Character Recognition and Writing", 3, "上", 1, "procedural",
    "For an unfamiliar character, find its radical and then count the remaining strokes. This method is taught alongside alphabetical lookup in Unit 1.",
    "sz_34",
    [
        ("Which radical is used to look up “河” by radical?", "Water radical (氵)", ["可", "口", "木"], "The water radical 氵 is on the left of “河”; 可 is the other component, not the radical."),
        ("Which radical is used to look up “草” by radical?", "Grass radical (艹)", ["早", "日", "木"], "The grass radical 艹 is at the top of “草”; 早 is not its radical."),
        ("Which radical is used to look up “打”?", "Hand radical (扌)", ["丁", "口", "木"], "The hand radical 扌 is used for “打.” 丁 is a phonetic component, not the radical to look up."),
        ("Which lookup method is better when you do not know a character's pronunciation?", "Lookup by radical", ["Alphabetical lookup", "Flip through the dictionary at random from the back", "Guess a pronunciation and write it down"], "Alphabetical lookup requires knowing the pronunciation. For an unfamiliar character, start with its radical."),
    ],
)

K(
    "g3a_dongting", "Poem: “Looking at Dongting Lake”", "Poetry", 3, "上", 2, "conceptual",
    "Recite Liu Yuxi's poem and understand that the lake is compared to a silver plate and Junshan to a green snail.",
    "gs_34",
    [
        ("What is the next line after “湖光秋月两相和”?", "潭面无风镜未磨", ["遥望洞庭山水翠", "白银盘里一青螺", "潭面无风镜已磨"], "The lake and autumn moon blend together; the next line compares the still lake to an unpolished bronze mirror."),
        ("What is the next line after “遥望洞庭山水翠”?", "白银盘里一青螺", ["潭面无风镜未磨", "孤帆一片日边来", "淡妆浓抹总相宜"], "The next line compares the lake and mountain to a silver plate and a green snail. The line about a lone sail is from “Looking at Tianmen Mountain”; the line about makeup is about West Lake."),
        ("Who wrote “Looking at Dongting Lake”?", "Liu Yuxi", ["Li Bai", "Su Shi", "Du Mu"], "Liu Yuxi wrote this poem. Li Bai wrote “Looking at Tianmen Mountain,” Su Shi wrote about West Lake, and Du Mu wrote “Mountain Walk.”"),
        ("In “白银盘里一青螺,” what is compared to a green snail?", "Junshan in Lake Dongting", ["The entire surface of Lake Dongting", "The autumn moon", "A fishing boat"], "The silver plate represents the calm lake, and the green snail represents Junshan. The autumn moon appears in the first line."),
    ],
)

K(
    "g3a_shan", "Poem: “Mountain Walk”", "Poetry", 3, "上", 2, "conceptual",
    "Recite Du Mu's poem and learn that “坐” means “because” and “红于” means “redder than.”",
    "gs_34",
    [
        ("What is the next line after “远上寒山石径斜”?", "白云生处有人家", ["停车坐爱枫林晚", "霜叶红于二月花", "白云深处有人家"], "The standard textbook line is “白云生处有人家.” The lines about stopping the carriage and frost-covered leaves come later."),
        ("What is the next line after “停车坐爱枫林晚”?", "霜叶红于二月花", ["白云生处有人家", "霜叶红如二月花", "远上寒山石径斜"], "The speaker stops because he loves the evening maple grove. The next line says the frost-covered leaves are redder than flowers in February."),
        ("Who wrote “Mountain Walk”?", "Du Mu", ["Du Fu", "Li Bai", "Su Shi"], "Du Mu wrote this poem. Du Fu wrote “Quatrain”; do not confuse the two poets because they share a surname."),
        ("What does “坐” mean in “停车坐爱枫林晚”?", "Because", ["Sit down", "A seat", "Ride"], "Here, “坐” means “because.” The poet stops because he loves the evening view of the maple grove."),
    ],
)

K(
    "g3a_yeshu", "Poem: “What I Saw at Night”", "Poetry", 3, "上", 2, "conceptual",
    "Recite Ye Shaoweng's poem and learn that “促织” means “cricket” and “客情” is the feeling of being away from home.",
    "gs_34",
    [
        ("What is the next line after “萧萧梧叶送寒声”?", "江上秋风动客情", ["知有儿童挑促织", "夜深篱落一灯明", "江上秋风动客愁"], "The leaves bring a chill, and the autumn wind stirs the traveler's homesickness. The lines about children catching crickets and a lamp come later."),
        ("What is the next line after “知有儿童挑促织”?", "夜深篱落一灯明", ["江上秋风动客情", "夜深篱落一灯灭", "霜叶红于二月花"], "Children are catching crickets, and a lamp shines by the fence. The line about frost-covered leaves is from “Mountain Walk.”"),
        ("Who wrote “What I Saw at Night”?", "Ye Shaoweng", ["Lu You", "Yang Wanli", "Du Mu"], "Ye Shaoweng wrote this poem. Du Mu wrote “Mountain Walk,” and Yang Wanli wrote about West Lake's lotus flowers."),
        ("What does “促织” refer to in the poem?", "A cricket", ["Cloth woven on a loom", "A maple leaf", "A parasol tree"], "Catching “促织” means catching crickets. The poet sees a lamp by the fence and realizes children are catching them."),
    ],
)

K(
    "g3a_jin", "Reading: “The Cement Road Covered with Golden Palms”", "Reading Comprehension", 3, "上", 2, "reasoning",
    "Read Zhang Qiusheng's story: after a night of wind and rain, parasol leaves like golden palms cover the cement road.",
    "yd_34",
    [
        ("What covers the cement road?", "Fallen parasol leaves that look like golden palms", ["Golden snow", "Small fans made of ginkgo leaves", "Seashells"], "The parasol leaves lie flat on the road, like palms. The fan-shaped ginkgo leaves are from “Autumn Rain.”"),
        ("What is the weather like when the speaker leaves for school?", "It has rained, and the sky is beginning to clear", ["It is still snowing heavily", "There has been no wind or rain all day", "It is still the middle of the night"], "After a night of autumn wind and rain, the sky clears by school time, leaving wet leaves on the road."),
        ("What color are the speaker's rain boots, and how does the speaker walk?", "Reddish brown; carefully, counting the leaves one by one", ["White; running with eyes closed", "Blue; sweeping all the leaves into a ditch", "No shoes; deliberately crushing the leaves"], "The reddish-brown boots hop like little birds among the golden leaves. The speaker looks at and counts them rather than damaging them."),
        ("What does the speaker do with the first leaf picked up?", "Keeps it safely in a schoolbag", ["Throws it into a pond", "Sticks it on the beach", "Burns it immediately"], "The speaker likes the leaf and puts it in the schoolbag to keep it safe."),
    ],
)

K(
    "g3a_qiu", "Reading: “Autumn Rain”", "Reading Comprehension", 3, "上", 2, "reasoning",
    "Notice the colors, scents, and coolness brought by the rain that unlocks autumn.",
    "yd_34",
    [
        ("What does the passage compare autumn rain to?", "A key", ["A sun", "A sparrow", "A boat"], "The passage says autumn rain is a key that opens the door to autumn."),
        ("What colors are the ginkgo and maple leaves in the passage?", "The ginkgo leaves are yellow, and the maple leaves are red", ["The ginkgo leaves are red, and the maple leaves are yellow", "Both are green", "Both turn white"], "Yellow ginkgo leaves look like fans, and red maple leaves look like stamps."),
        ("What scents does the autumn rain bring?", "Sweet scents like pineapple and pear", ["Only the smell of gunpowder", "The salty smell of the sea", "The icy smell of winter"], "The passage describes ripening fruit, with sweet pineapple and fragrant pears."),
        ("What does “gently, gently” tell you about the rain?", "It brings autumn quietly and softly", ["It falls hard and loudly", "It smashes the door", "It roars only at night"], "Autumn rain gently opens the door and brings coolness and tenderness."),
    ],
)

K(
    "g3a_ting", "Reading: “Listen to the Sounds of Autumn”", "Reading Comprehension", 3, "上", 2, "reasoning",
    "Distinguish the rustle of yellow leaves saying goodbye from the cricket's chirp as it leaves the balcony; autumn's sounds also live in grain and sweat.",
    "yd_34",
    [
        ("What sound does “rustle” represent in the poem?", "The tree shakes its arms as the yellow leaves say goodbye", ["A cricket flutters its wings", "Waves crash on the beach", "A stone breaks a water jar"], "The yellow leaves leave the branches with a goodbye. The cricket's sound comes later."),
        ("What is the cricket's chirp described as?", "A songlike tune bidding farewell to the balcony", ["The yellow leaves' goodbye", "The geese's warm message", "A song of harvest"], "The cricket flutters its wings to say goodbye to the balcony. The geese bring messages, and the autumn wind brings a song."),
        ("What do the geese and the autumn wind each bring?", "The geese scatter messages, and the wind brings a song of harvest", ["Neither makes a sound", "The geese bring maple leaves, and the wind only breaks the lake surface", "The wind sings the cricket's song while the geese say goodbye"], "Rows of geese chase the clouds while gusts of autumn wind sweep across the fields; their sounds differ."),
        ("Where else can the sounds of autumn be heard in the poem?", "In every leaf, flower, drop of sweat, and grain of rice", ["Only in musical instruments", "Only in summer cicadas", "There are no sounds to hear in autumn"], "Fallen leaves, flowers, sweat, and ripened grain all hold autumn's sounds. The poem invites everyone to listen."),
    ],
)

K(
    "g3a_ri", "Writing: Keeping a Diary", "Writing Basics", 3, "上", 2, "procedural",
    "Start a diary with the date, day of the week, and weather, then describe what you actually saw, heard, and thought that day.",
    "xz_34",
    [
        ("What should usually be written on the first line of a diary entry?", "The date, day of the week, and weather", ["Only an exclamation mark", "The ending first", "An imagined event no one saw"], "First tell the reader the date, day, and weather, then describe what happened."),
        ("Which example sounds most like a diary entry?", "October 8, Monday, sunny. Parasol leaves covered the cement road, and I picked one up and put it in my schoolbag.", ["The leaves are beautiful.", "I did not go outside, but I think it rained.", "Leaves."], "Describe something you actually saw that day. Simply saying “beautiful” does not tell the reader what you saw."),
        ("How should a diary describe something you saw?", "Record what you actually saw and thought in the order it happened", ["Write only the words “very good”", "Describe something unseen as if you saw it", "Leave out the date so no one knows when it happened"], "A diary should be truthful and show the sequence of events. Do not claim to have seen something you did not see."),
        ("Which content is unsuitable for a diary?", "Claiming to have seen something that you did not see", ["Rain wet the fallen leaves today", "I tucked a leaf into a book", "The sky cleared after school"], "Wet leaves, putting a leaf in a book, and clearing weather are all things you can describe. A diary should not invent something you did not see."),
    ],
)

K(
    "g3a_abb", "Language Arts Unit 2: ABB and AABB Word Patterns", "Vocabulary", 3, "上", 2, "conceptual",
    "Recognize the patterns in words such as “绿油油,” “红彤彤,” and “整整齐齐,” and understand how repetition affects meaning.",
    "cy_34",
    [
        ("Which word follows the ABB pattern?", "绿油油", ["整整齐齐", "高低", "绿油"], "“绿油油” repeats the last character twice after the first. “整整齐齐” follows the AABB pattern."),
        ("Which word follows the AABB pattern?", "整整齐齐", ["红彤彤", "整齐齐", "齐整整齐"], "“整齐” becomes “整整齐齐” when repeated. “红彤彤” follows the ABB pattern."),
        ("What is “绿油油” commonly used to describe?", "Very green grass or leaves", ["A very green stone", "Very green snow", "Very green ink"], "“绿油油” describes fresh, vivid green plants."),
        ("Which phrase uses the reduplicated form correctly?", "The discussion was lively (热热闹闹)", ["The discussion was lively (热闹闹)", "The discussion was lively (热热热闹)", "The discussion was lively (闹热热热)"], "The word “热闹” is repeated as “热热闹闹.” Do not omit a character or change the order."),
    ],
)

K(
    "g3a_lao", "Reading: “The Old House That Never Fell Down”", "Reading Comprehension", 3, "上", 3, "reasoning",
    "Make predictions while reading: the old house repeatedly agrees to help a cat, a hen, and a little spider.",
    "yd_34",
    [
        ("What does the old house plan to do at the beginning of the story?", "Fall down because it is very old", ["Immediately build a new high-rise", "Run to the river", "Drive all the animals away"], "The old house says it is time for it to fall down; its windows and doors are old."),
        ("Who first asks the old house to stay up for one more night?", "A little cat", ["A little spider", "An old hen", "A large ox"], "The cat asks the house to wait because it is very windy outside. The hen and spider arrive later."),
        ("Why does the hen ask the old house not to fall down yet?", "She wants to hatch her chicks inside", ["She wants to knock the house down", "She is only passing by", "She wants to take the window apart"], "The hen asks the house to wait a few more weeks until her chicks hatch."),
        ("What is a good way to read a story like this?", "Predict who might ask for help next, based on what has happened", ["Close the book and stop reading", "Remember only the last sentence", "Ignore the title and earlier events"], "After the cat and hen arrive, you can predict that another animal may ask the old house to wait."),
    ],
)

K(
    "g3a_jiang", "Reading: “The Stubborn Tortoise”", "Reading Comprehension", 3, "上", 3, "reasoning",
    "Read Michael Ende's fairy tale: Tortoise Tao Tao sets out for the Lion King's wedding and keeps her decision despite others' advice.",
    "yd_34",
    [
        ("Whose wedding is Tao Tao traveling to attend?", "The wedding of the twenty-eighth Lion King", ["A spider's wedding", "A snail's wedding", "A tiger's wedding"], "After hearing that the twenty-eighth Lion King invited the animals to a celebration, she decides to set out."),
        ("What does Tao Tao say when the spider laughs at her slow pace and urges her to go home?", "“I'm sorry, but my decision cannot be changed.”", ["“Then I'll go home right away.”", "“Please carry me there.”", "“I never wanted to go to the wedding.”"], "She looks at her short, sturdy legs and says she will arrive on time. She repeats this response later."),
        ("What does she do when the snail tells her she is going the wrong way?", "She thanks the snail, turns around, and keeps walking step by step", ["She gives up immediately", "She argues with the snail and stops", "She sits by a pond and says she has arrived"], "She thanks the snail for the directions and does not change her decision because she took a wrong turn."),
        ("Which celebration does she eventually reach?", "The wedding of the twenty-ninth Lion King", ["The twenty-eighth Lion King's wedding on the original day", "None; she turns back halfway", "A battlefield where the tiger and lion fight"], "The twenty-eighth Lion King's wedding has already passed. She keeps going and reaches the twenty-ninth Lion King's wedding."),
    ],
)

K(
    "g3a_gou", "Reading: “The Dog That Learned to Bark”", "Reading Comprehension", 3, "上", 3, "reasoning",
    "Read Gianni Rodari's fairy tale: a dog that cannot bark learns to crow, then to call like a cuckoo; the story leaves several endings for readers to predict.",
    "yd_34",
    [
        ("Why does the dog try to learn how to call?", "It has never heard a dog bark where it lives and people laugh at it", ["It dislikes barking and wants to stop", "A fox orders it not to bark", "It already knows how to bark and is only playing"], "It cannot make the sounds of a dog, cat, cow, or horse. Others criticize it, but it does not know what a proper dog bark sounds like."),
        ("Who does the dog meet after it learns to crow from the rooster?", "A fox, which thinks it is a rooster and laughs when it sees a dog", ["A hunter, who mistakes it for a lion", "A fox who invites the cuckoo for lunch", "A calf who immediately learns to bark"], "After the dog learns to crow convincingly, the fox arrives with cutlery, expecting rooster for lunch. It is disappointed and laughs at the dog."),
        ("What almost happens when the dog learns the cuckoo's “cuckoo” call?", "A hunter mistakes it for a bird and nearly shoots it", ["The fox takes it as an apprentice", "It immediately learns to bark", "The hunter recognizes it as a dog and rewards it"], "The cuckoo call attracts a hunter. After a gunshot, the frightened dog runs away."),
        ("What does the story leave open after describing the dog's two lessons?", "Several possible endings for readers to predict from the earlier events", ["One fixed ending that cannot be reconsidered", "A poem everyone must memorize", "An observation chart"], "The possible endings include meeting a calf or farmer, or hearing a dog bark. Predictions should build on the dog's two earlier lessons."),
    ],
)

K(
    "g3a_yd3", "Language Arts Unit 3: Continuing a Story", "Writing Basics", 3, "上", 3, "procedural",
    "Continue from the existing plot without changing a character's personality. In the speaking task “The Story Behind a Name,” explain the name's origin or meaning.",
    "xz_34",
    [
        ("Which continuation fits “The Old House That Never Fell Down”?", "Another animal arrives for help and asks the old house to wait", ["The house suddenly flies to the Xisha Islands to fish", "The story turns into a poem-memorization exercise", "The house never appears after the first sentence"], "The animals who arrive ask the old house to wait. Continue that plot instead of switching to a different story."),
        ("Which continuation matches Tao Tao's character in “The Stubborn Tortoise”?", "She keeps going and says her decision cannot be changed, even when others persuade her", ["She listens to the spider and goes home for good", "She becomes an ant captain and carries cheese", "She sits down and says she is good at giving up"], "Tao Tao keeps persevering. If she gives up immediately, she no longer acts like the stubborn tortoise."),
        ("Which response clearly explains the story behind a name?", "My name is Lin. Dad used the “Lin” from Grandma's name and hopes I will be full of life like a forest.", ["My name is Lin.", "A name is just a name.", "I will not say my name; I will only say I ate noodles today."], "Explain who chose the name, which character they used, and what they hoped for. Simply giving a name does not tell its story."),
        ("What is most important when continuing a story?", "Continue from what has happened and keep the characters consistent", ["Reject the entire plot and still call it a continuation", "Write only a title", "Turn the story into a copied character list"], "A continuation carries the story forward rather than starting a new one. It should preserve the characters and earlier events."),
    ],
)

K(
    "g3a_bao", "Reading: “The Secret of the Magic Gourd” (Excerpt)", "Reading Comprehension", 3, "上", 4, "reasoning",
    "Read an excerpt from Zhang Tianyi's fairy tale: after hearing his grandmother's stories, Wang Bao wants a gourd that can provide whatever he wishes for.",
    "yd_34",
    [
        ("Who wrote this excerpt, and who is the main character?", "Zhang Tianyi; the main character is Wang Bao", ["Rabindranath Tagore; the main character is Tao Tao", "Gianni Rodari; the main character is a little dog", "Ye Shengtao; the main character is a scarecrow"], "Zhang Tianyi wrote “The Secret of the Magic Gourd.” The child who wants the gourd is Wang Bao."),
        ("What is special about the gourd in Grandma's stories?", "It gives its owner whatever they want", ["It can knock down the old house", "It teaches a dog to bark", "It is a piece of cheese that must be carried away"], "The magic gourd grants wishes. Wang Bao cannot stop thinking about it after hearing the story."),
        ("Why does Wang Bao want the gourd so much?", "He thinks he will not have to work hard if he has it", ["He wants to break a jar to rescue someone", "He wants to spread it on the cement road", "He wants to give it to the Lion King as a wedding gift"], "He envies the idea of getting what he wants without working. This is his own wish, not an instruction from his grandmother."),
        ("How does Wang Bao eventually get the magic gourd in the excerpt?", "He keeps thinking about it by the river and later finds a gourd that answers him", ["Sima Guang pulls it out of a jar", "The ant captain gives it to him", "His grandmother buys it in the Xisha Islands"], "Wang Bao keeps thinking about the gourd; the story continues when he finds one and begins talking with it."),
    ],
)

K(
    "g3a_niu", "Reading: “A Trip Inside the Cow's Stomach”", "Reading Comprehension", 3, "上", 4, "reasoning",
    "Understand how Redhead is swallowed by a cow, how Bluetop encourages him from outside, and how he is finally coughed out.",
    "yd_34",
    [
        ("What kind of animals are Redhead and Bluetop?", "Two crickets", ["Two little birds", "Two cows", "Two little fish"], "Bluetop and Redhead are friends, and both are crickets."),
        ("How does Redhead get inside the cow's stomach?", "The cow eats the grass and swallows him with it", ["He decides to go on a trip inside", "Bluetop pushes him inside", "He crawls in through the cow's nose"], "Redhead is on a blade of grass when the cow swallows the grass and the insect together."),
        ("How does Bluetop help Redhead inside the cow?", "He encourages him from outside and explains that cows chew cud", ["He jumps inside too", "He chases the cow away and leaves", "He tells Redhead to stay inside forever"], "Bluetop is frightened but calls out instructions and gives Redhead courage."),
        ("How does Redhead finally get out?", "The cow sneezes him out", ["He bites through the cow's stomach", "Bluetop pulls him out", "He stays inside"], "After traveling through the cow's stomach, Redhead returns to the grass with the cow's sneeze."),
    ],
)

K(
    "g3a_nai", "Reading: “A Piece of Cheese”", "Reading Comprehension", 3, "上", 4, "reasoning",
    "Understand that the ant captain forbids sneaking a bite, does not eat any cheese himself, and later gives the fallen crumb to the smallest ant.",
    "yd_34",
    [
        ("What does the ant captain first tell everyone to do after finding the cheese?", "Carry the cheese into the nest", ["Eat it all on the spot", "Give it to the Lion King", "Throw it into the river"], "The cheese is meant to be carried back. The captain leads the move instead of starting a meal."),
        ("What rule does the captain make?", "No one may sneak a bite, including the captain", ["The smallest ant must eat first", "The captain may eat, but no one else may", "Anyone may eat food that falls"], "The rule applies to every ant, including the captain."),
        ("What does the smallest ant do after a little cheese falls off?", "Stares at it and drools", ["Eats the entire piece immediately", "Tells everyone to stop carrying it", "Takes the crumbs to a cow"], "The young ant wants the fallen piece, and the captain notices."),
        ("What does the captain eventually do with the piece of cheese?", "Gives it to the smallest ant, eats none himself, and leads the others to carry the cheese into the nest", ["Eats it first and lets everyone fight over the rest", "Throws the whole piece away", "Declares that sneaking bites is now allowed"], "He realizes the small ant needs strength to carry things and gives it the piece. The rule still stands, and he does not eat any."),
    ],
)

K(
    "g3a_yd4", "Language Arts Unit 4: Make Up a Fairy Tale", "Writing Basics", 3, "上", 4, "procedural",
    "Create a fairy tale with imagined characters, a problem, and what happens afterward.",
    "xz_34",
    [
        ("Which opening sounds like the beginning of a fairy tale?", "A little ant finds a piece of talking cheese, and the cheese says it wants to go home", ["Today is Monday and the weather is sunny.", "Cheese. Ant.", "I want to make up a story, but there are no characters."], "In fairy tales, things that cannot really speak often talk. A date or two isolated words do not begin a story."),
        ("Which one does not sound like a fairy tale?", "Copying today's homework without adding anything imagined", ["A magic gourd grants Wang Bao's wishes", "A cricket travels through a cow's stomach", "An old house agrees to help animals"], "Copying homework describes a real task. The magic gourd, the trip inside a cow, and the talking house are imagined."),
        ("What makes a fairy tale complete?", "Describe the characters, the problem they face, and what happens next", ["Only give a name", "Start with the ending and omit what happened before", "Switch to unrelated characters in every sentence"], "Readers need to know who is involved, what happens, and how it turns out. Changing to an unrelated story makes the tale fall apart."),
        ("How does “Make Up a Fairy Tale” differ from the reading-club activity that follows?", "Here you invent a story; in the reading club you read fairy tales written by others", ["Both activities only copy a character list", "A fairy tale cannot include animals", "The reading club requires changing the ending to its opposite"], "Making up a tale uses your imagination; reading means exploring books such as Hans Christian Andersen's fairy tales or “The Scarecrow.”"),
    ],
)

K(
    "g3a_le", "Reading Club: “In That Wonderful Kingdom”", "Reading Comprehension", 3, "上", 4, "conceptual",
    "This reading club focuses on fairy tales, including Hans Christian Andersen's stories and Ye Shengtao's “The Scarecrow,” an imagined world.",
    "yd_34",
    [
        ("What kind of books are read in “In That Wonderful Kingdom”?", "Fairy tales, such as Andersen's stories and “The Scarecrow”", ["Only today's class schedule", "A blank notebook", "A multiplication table"], "Fairy tales contain imagined people and events. “The Scarecrow” is Ye Shengtao's fairy tale; a blank notebook and a multiplication table are not."),
        ("Why is it called a wonderful kingdom?", "The stories include extraordinary events that do not happen in everyday life, like a world of imagination", ["Readers have to memorize country names", "It contains only real experiment notes", "There are no stories in the kingdom"], "A magic gourd grants wishes, and a cricket travels inside a cow—these are not everyday events."),
        ("What should you be able to describe after reading a fairy tale?", "Who encountered what, and what made it wonderful", ["Only how thick the book is", "Change the ending and claim that was the author's meaning", "Only the cover's color"], "Understanding the characters and plot means entering this world. Reversing the story does not preserve the original."),
        ("Why can “The Secret of the Magic Gourd” be read here too?", "It is an imagined fairy tale in which a magic gourd grants wishes", ["It is a classical prose essay", "It only teaches dictionary lookup", "It is a poem about Lake Dongting"], "Wang Bao's magic gourd is part of a fairy tale. Dictionary lookup and “Looking at Dongting Lake” are not stories for this activity."),
    ],
)

K(
    "g3a_niao", "Reading: “The Bird That Brought Us a Boat”", "Reading Comprehension", 3, "上", 5, "reasoning",
    "Study how the author observes the kingfisher's colors and fishing movements.",
    "yd_34",
    [
        ("What kind of bird is riding on the boat?", "A kingfisher", ["A sparrow", "A swallow", "An oriole"], "The speaker's mother identifies the colorful bird as a kingfisher."),
        ("What does the author notice first about the kingfisher?", "The colors of its feathers and its long red beak", ["Its age", "Its name and color", "That it is sleeping underwater"], "The author sees emerald feathers, a little blue on the wings, and a long red beak."),
        ("How does the kingfisher catch fish?", "It dives suddenly into the water and flies back to the boat", ["It waits on the boat for a fish to jump up", "It asks a fisherman to catch one", "It only flies in the sky and never touches the water"], "It watches the surface, suddenly dives, and flies up with a small fish in its beak."),
        ("What is the most useful observation technique in this passage?", "Describe the colors and movements that you observe, step by step", ["Only write “the bird is beautiful”", "Write about the boat without looking at the bird", "Describe something unseen as if you saw it"], "The author describes the bird's appearance and then its fishing movements, both directly observed."),
    ],
)

K(
    "g3a_cao", "Reading: “The Golden Meadow”", "Reading Comprehension", 3, "上", 5, "reasoning",
    "Read Prishvin's story: the meadow looks golden when dandelions open and turns green again when they close.",
    "yd_34",
    [
        ("Who wrote “The Golden Meadow”?", "Mikhail Prishvin", ["Rabindranath Tagore", "Zhang Tianyi", "Zhu Weizhi"], "Prishvin wrote this story about a meadow of dandelions. Tagore wrote “The School of Flowers,” and Zhu Weizhi wrote “An Endless Book.”"),
        ("When does the meadow look golden?", "When the dandelions are open, often around midday", ["All day long", "Only at midnight", "In the morning when the flowers are closed"], "When the flowers open, the meadow turns golden. They close in the morning and evening, and the meadow looks green again."),
        ("Why does the meadow turn green in the morning and evening?", "The dandelion flowers have closed", ["Someone has dyed the grass green", "All the dandelions have withered", "Green rain has fallen"], "The grass itself does not change color. Open flowers look golden; closed flowers reveal the green grass."),
        ("What did the speaker and his brother do, and what did they later discover?", "They blew dandelion seeds; later they noticed the flowers change at different times of day", ["They fed dandelions to a kingfisher", "They observed once and decided the color never changes", "They flattened the meadow to make it look better"], "They first played for fun, then observed the meadow in the morning, at midday, and in the evening and noticed the flowers opening and closing."),
    ],
)

K(
    "g3a_bin", "Writing: “A Colorful World Through Our Eyes”", "Writing Basics", 3, "上", 5, "procedural",
    "Describe something you observed, including its colors, appearance, and changes over time; do not simply call it beautiful.",
    "xz_34",
    [
        ("Which description of something in front of you is clearer?", "At noon the meadow is golden and the dandelions are open; by evening they close and the meadow turns green again.", ["The world is beautiful.", "I did not see it, but it must look nice.", "A meadow."], "Describe the colors and changes you actually saw. Saying only that it is beautiful does not explain why."),
        ("Which sentence describes an observed bird?", "Its feathers are emerald green, its wings have a little blue, and it has a long red beak.", ["This bird is beautiful.", "Birds can fly.", "I like birds."], "The colors and body parts describe what was seen. “It can fly” and “I like birds” do not show what this bird looks like."),
        ("How should you describe the same thing when observing it over time?", "Record how it changes at different times, such as morning, noon, and evening", ["Only write “it is beautiful”", "Mix several days together so the sequence is unclear", "Claim to have watched it for a long time without going to see it"], "Changes happen over time. Do not describe a color you did not observe as if you saw it."),
        ("Which approach does not fit this writing task?", "Describe a color you did not see as if you had seen it", ["Describe a leaf's color and shape", "Describe a bird diving into the water", "Describe how a meadow differs in the morning and at noon"], "Leaves, fishing, and a meadow changing color are all observations. Claiming to have seen something you did not see is not truthful."),
    ],
)

K(
    "g3a_de", "Writing: “A Colorful World Through Our Eyes” — 的, 地, and 得", "Sentences", 3, "上", 5, "procedural",
    "Choose the Chinese particles 的, 地, or 得 according to whether the following element is a noun, verb, or complement.",
    "jz_34",
    [
        ("In “beautiful ____ flower,” which Chinese particle completes the phrase?", "的", ["地", "得", "底"], "Use 的 before a noun, such as “flower.”"),
        ("In “walk ____ slowly,” which Chinese particle fits the blank?", "地", ["的", "得", "底"], "Use 地 before a verb, as in “walk.”"),
        ("In “jump up ____ happily,” which Chinese particle fits the blank?", "得", ["的", "地", "底"], "得 is followed by a complement that describes the degree of an action or state."),
        ("In “He runs ____ very fast,” which Chinese particle fits the blank?", "得", ["的", "地", "底"], "“Very fast” describes how he runs, so use 得."),
    ],
)

K(
    "g3a_xisha", "Reading: “The Rich Xisha Islands”", "Reading Comprehension", 3, "上", 6, "reasoning",
    "Learn about the Xisha Islands' natural resources in the order of sea water, seabed, beach, and islands.",
    "yd_34",
    [
        ("Why does the seawater around the Xisha Islands have so many colors?", "The seabed has both high cliffs and deep valleys, so the water varies in depth", ["Paint was spread on the sea", "The water is only a deep black", "There is no sunlight"], "The water ranges from deep blue to pale green and apricot because the seabed is uneven."),
        ("What can be found on the seabed?", "Coral, sea cucumbers, lobsters, and schools of fish", ["Only sand", "Only one kind of shrimp", "No living things"], "The passage says the seabed is full of water and fish, with coral, sea cucumbers, and lobsters."),
        ("What can be seen on the beach?", "Many shells and eggs laid by sea turtles", ["Thick snow", "Maple and ginkgo leaves", "An old well"], "The beach has many kinds of shells, and sea turtles lay their eggs there."),
        ("Which parts of the Xisha Islands does the passage describe?", "The water, seabed, beaches, and birds on the islands", ["Only the weather", "Only one boat", "Snow from winter to summer"], "It describes the water's colors, then the seabed and beach, and finally the birds, showing the area's beauty and natural abundance."),
    ],
)

K(
    "g3a_haibin", "Reading: “A Seaside Town”", "Reading Comprehension", 3, "上", 6, "reasoning",
    "First read about the beach and boats along the coast, then about the town's courtyards, parks, and clean streets.",
    "yd_34",
    [
        ("Which place does the passage describe first, and which comes later?", "The coast first, then the town", ["Only the town, with no sea", "Snow in Xiaoxing'anling first, then the sea", "One boat from beginning to end"], "The sea, beach, and fishing boats come first. The courtyards, parks, and streets describe the town."),
        ("What is easy to see on the beach?", "Shells of many colors and boats on the water", ["Thick snow", "Maple leaves covering the ground", "A broken water jar"], "Many shells cover the beach, and fishing and transport boats travel on the sea."),
        ("What are the banyan trees in the town's park like?", "Large green velvet umbrellas with stone benches beneath them", ["Golden palms spread on a cement road", "Sunlight like sharp swords", "Green snails in a silver plate"], "The dense banyan leaves provide shade, and people rest on the stone benches below."),
        ("How does the passage describe the town's streets, and how does it characterize the town?", "They are paved with fine sand and kept very clean; the town is beautiful and tidy", ["Covered in fallen leaves and never swept", "Covered in thick snow", "There is a sea but no street"], "The sand crunches underfoot. Residents keep the streets so clean that not a leaf can be seen."),
    ],
)

K(
    "g3a_xingan", "Reading: “Beautiful Xiaoxing'anling”", "Reading Comprehension", 3, "上", 6, "reasoning",
    "Explore Xiaoxing'anling through spring, summer, autumn, and winter: dense foliage fills the forest in summer, and autumn brings wild grapes, hazelnuts, and ginseng.",
    "yd_34",
    [
        ("In what order does the passage describe Xiaoxing'anling?", "Spring, summer, autumn, and winter", ["Summer only", "From the sea to the beach", "From morning until noon"], "Each of the four seasons is described. The passage is not limited to one season or organized as coast and town."),
        ("What is the forest like in summer?", "Dense foliage, morning fog, and sunlight piercing the treetops like swords", ["All leaves have fallen, leaving only snow", "The forest has moved to the beach", "New shoots appear and fawns stroll beside a stream"], "New shoots and fawns by a stream describe spring. In summer, dense leaves fill the forest."),
        ("What does the forest offer people in autumn?", "Wild grapes, hazelnuts, and medicinal plants such as ginseng", ["Only thick snow", "Sea turtle eggs", "A key that opens the door to autumn"], "Sweet-and-sour wild grapes, fragrant crunchy hazelnuts, and valuable ginseng are autumn's produce."),
        ("How does the passage describe Xiaoxing'anling overall?", "Beautiful in every season, like a great garden and a vast treasure house", ["Only winter is worth seeing", "There are no trees or animals", "It is the same place as the seaside town"], "Spring brings new shoots, summer deep shade, autumn fruit, and winter snow and animals preparing for the cold. Its abundant resources make it a treasure house."),
    ],
)

K(
    "g3a_xiang", "Reading: “Hong Kong, the Pearl of the Orient”", "Reading Comprehension", 3, "上", 6, "reasoning",
    "Understand why Hong Kong is compared to a pearl through its global marketplace, food, and tourist attractions.",
    "yd_34",
    [
        ("What does the passage compare Hong Kong to?", "A shining pearl on China's southern coast", ["A green snail on a silver plate", "A key that opens autumn", "A piece of cheese that is impossible to carry"], "The pearl suggests that Hong Kong is both bright and important. The green snail refers to Junshan in “Looking at Dongting Lake.”"),
        ("Which aspects of Hong Kong does the passage mainly describe?", "Its global marketplace, food, and tourist attractions", ["Winter snow only", "A primary school only", "Sea water, seabed, and sea turtles"], "Goods come from many places, the food offers many regional flavors, and the city has well-known attractions. The Xisha Islands passage is organized by parts of the sea."),
        ("What can visitors see when the passage describes tourism and night views?", "Beaches and parks, with dazzling lights at night", ["Frost-covered leaves across the mountains", "Grass inside a cow's stomach", "A broken water jar"], "People visit the coast and parks. After dark, lights across the harbor and streets shine together."),
        ("What is the purpose of this description?", "To show that Hong Kong is prosperous and beautiful, like a treasured pearl", ["Hong Kong has only one kind of food", "Hong Kong is in the middle of Lake Dongting", "It snows all year in Hong Kong"], "The marketplace, food, and night views all show a bright, lively city."),
    ],
)

K(
    "g3a_yd6", "Language Arts Unit 6: “This Place Is Beautiful”", "Writing Basics", 3, "上", 6, "procedural",
    "Describe what makes one place beautiful. You can organize it by aspects, as in the readings, and make each aspect specific.",
    "xz_34",
    [
        ("For “This Place Is Beautiful,” which paragraph stays focused on one place?", "The seaside town's streets are paved with fine sand and swept so clean that not a leaf can be seen.", ["This place is beautiful, very beautiful, extremely beautiful.", "Street. Soccer. Noodles.", "The streets are beautiful. The Xisha fish are beautiful too. The moon over Dongting Lake is beautiful too."], "The first paragraph describes one town's streets. Repeating “beautiful” or switching places leaves the reader unsure what you are describing."),
        ("Which sentence does not describe the beauty specifically?", "This place is beautiful.", ["Red and yellow shells cover the beach.", "The banyan tree is like a large green velvet umbrella.", "In the morning, fog rises from the valley."], "“Beautiful” is only an opinion. Shell colors, the tree's shape, and valley fog describe what can be seen."),
        ("How can you describe a place like the passage about the Xisha Islands?", "Organize the description by aspects, all focused on the same place", ["Write only an exclamation mark", "Describe a place you have never visited as if you saw it", "Switch to an unrelated place in every sentence"], "The water, seabed, and beach are different aspects of the Xisha Islands. You can divide the description into aspects without changing locations."),
        ("What question can you ask when revising this piece?", "Can a reader tell where it is and what is beautiful without seeing the title?", ["How many commas are there?", "Is it enough to use the word “beautiful” in the first sentence?", "Does it matter if every sentence is out of order?"], "If the sentences could describe any place, they do not yet show what is special about this one."),
    ],
)

K(
    "g3a_lu", "Poem: “Deer Enclosure”", "Poetry", 3, "上", 7, "conceptual",
    "Recite Wang Wei's poem and learn that an empty mountain is not silent, and “返景” is reflected evening sunlight.",
    "gs_34",
    [
        ("What is the next line after “空山不见人”?", "但闻人语响", ["返景入深林", "复照青苔上", "但见人语响"], "No one is seen, but the sound of voices can be heard. The lines about reflected light and moss come later. The poem uses “闻” (“hear”), not “见” (“see”)."),
        ("What is the next line after “返景入深林”?", "复照青苔上", ["但闻人语响", "复照青苔下", "空山不见人"], "The evening sunlight reaches into the forest and shines on the moss. The line about hearing voices is the second line."),
        ("Who wrote “Deer Enclosure”?", "Wang Wei", ["Li Bai", "Du Fu", "Meng Haoran"], "Wang Wei wrote this poem. Li Bai wrote “Looking at Tianmen Mountain”; do not confuse them because both wrote about mountains."),
        ("What does “返景” mean in this poem?", "Reflected evening sunlight", ["The scenery on the way home", "A deer running", "New leaves appearing in spring"], "Here, 景 means sunlight. Evening light enters the deep forest and falls on the moss. Deer Enclosure is a place name, not a scene with a deer."),
    ],
)

K(
    "g3a_wang", "Poem: “Looking at Tianmen Mountain”", "Poetry", 3, "上", 7, "conceptual",
    "Recite Li Bai's poem and learn that the Chu River is the Yangtze and the green river water turns back here.",
    "gs_34",
    [
        ("What is the next line after “天门中断楚江开”?", "碧水东流至此回", ["两岸青山相对出", "孤帆一片日边来", "碧水东流到此回"], "The river flows east and turns back here. The textbook version says “至此回.”"),
        ("What is the next line after “两岸青山相对出”?", "孤帆一片日边来", ["碧水东流至此回", "天门中断楚江开", "孤帆一片月边来"], "The green mountains rise opposite each other, and a lone sail approaches from the sunlit horizon."),
        ("Who wrote “Looking at Tianmen Mountain”?", "Li Bai", ["Du Fu", "Du Mu", "Su Shi"], "Li Bai wrote this poem. Du Mu wrote “Mountain Walk”; do not confuse the two."),
        ("Which river does “楚江” refer to in this poem?", "The Yangtze River", ["The Yellow River", "West Lake", "Lake Dongting"], "The Chu River flowing between Tianmen Mountain's cliffs is the Yangtze. Lake Dongting appears in “Looking at Dongting Lake,” and West Lake appears in poems about Hangzhou."),
    ],
)

K(
    "g3a_hu", "Poem: “Drinking by the Lake After Rain”", "Poetry", 3, "上", 7, "conceptual",
    "Recite Su Shi's poem about West Lake and distinguish it from Yang Wanli's poem about its lotus flowers.",
    "gs_34",
    [
        ("What is the next line after “水光潋滟晴方好”?", "山色空蒙雨亦奇", ["欲把西湖比西子", "淡妆浓抹总相宜", "接天莲叶无穷碧"], "The lake is beautiful in sunshine, and the misty mountains are wonderful in rain. The line about lotus leaves is by Yang Wanli."),
        ("What is the next line after “欲把西湖比西子”?", "淡妆浓抹总相宜", ["山色空蒙雨亦奇", "映日荷花别样红", "风光不与四时同"], "West Lake is beautiful in both sun and rain, like Xi Shi, who looks lovely with either subtle or heavy makeup."),
        ("Who wrote this poem?", "Su Shi", ["Yang Wanli", "Du Fu", "Li Bai"], "Su Shi wrote “Drinking by the Lake After Rain.” Yang Wanli wrote “Leaving Jingci Temple at Dawn to See Lin Zifang Off.”"),
        ("Who is “西子”?", "Xi Shi", ["A fisherman by West Lake", "The poet", "Hui Chong"], "“西子” refers to the ancient beauty Xi Shi, whom the poet uses as a comparison for West Lake."),
    ],
)

K(
    "g3a_sheng", "Reading: “The Sounds of Nature”", "Reading Comprehension", 3, "上", 7, "reasoning",
    "Understand that wind, water, and animals are all musicians in nature.",
    "yd_34",
    [
        ("What does the passage call the wind?", "A musician", ["A painter", "A stonemason", "A tailor"], "The wind plays music in the forest, so the passage calls it a musician of nature."),
        ("How do the sounds of water change?", "Sometimes gentle, sometimes powerful", ["Always one loud sound", "Water makes no sound", "Only rain counts as music"], "A stream murmurs, a river rushes, and the sea surges; water can play different melodies."),
        ("What are the animals' sounds described as?", "Another concert", ["Useless noise", "Only birds can call; insects cannot", "Unrelated to music"], "Birdsong, insect calls, and animal sounds create another concert in nature."),
        ("Why does the author describe these sounds?", "Nature's sounds are diverse and worth listening to carefully", ["Nature has no sounds", "It is best to cover your ears", "Only musical instruments make sounds"], "Wind, water, and animals each have their own sounds. Listen closely and you can hear their beauty."),
    ],
)

K(
    "g3a_dushu", "Reading: “An Endless Book”", "Reading Comprehension", 3, "上", 7, "reasoning",
    "Read Zhu Weizhi's story: nature is an endless picture book filled with sparrows, eagles, ants, bamboo, and palms.",
    "yd_34",
    [
        ("What does “An Endless Book” refer to?", "Nature", ["A thick list of vocabulary characters", "A passage about Hong Kong's night view only", "An invitation to the Lion King's wedding"], "The passage calls nature an endless picture book and a book that can never be fully read."),
        ("What impressions do the sparrow, eagle, and ants give?", "The sparrow is delightful, the eagle is strong and fierce, and the ants are brave and loyal", ["All three are frightening", "The eagle is delightful, and the sparrow is in a battle", "The ants glide in circles, and the eagle moves house"], "Sparrows chatter and hop; an eagle swoops down; ants move in an orderly line and fight bravely."),
        ("Which two plants near the author's house are favorites?", "Bamboo and palm trees", ["Only sea cucumbers and coral", "Maples and ginkgo trees", "London plane trees"], "Bamboo shoots grow quickly after rain, and bamboo leaves whisper. Palm leaves resemble large fans reflected in the pond."),
        ("Why does the author call this book endless?", "Every living thing is different, with endless mysteries and pleasures to discover", ["The pages are too thick and the print too small", "Nature has only one color", "All its mysteries are revealed after one look"], "Flowers, trees, fruit, birds, and insects are all different. Careful observation always reveals something new."),
    ],
)

K(
    "g3a_yd7", "Language Arts Unit 7: “I Have an Idea”", "Writing Basics", 3, "上", 7, "procedural",
    "State the problem you observed, then explain a solution and your reasons. In the speaking task “Small Things Around Us,” clearly describe what happened.",
    "xz_34",
    [
        ("Which example clearly explains an idea?", "The reading corner is too crowded. I suggest adding a shelf and separating storybooks from science books so they are easier to find.", ["I have an idea.", "The idea is good.", "Books. Soccer. Noodles."], "It includes the problem, solution, and reason. Simply saying you have an idea does not explain what should change."),
        ("What is missing from “Everyone should make a change”?", "What should change and why", ["The location of Lake Dongting", "What Sima Guang broke", "The poet's name"], "An idea should address a specific situation. A lake or poet is not missing from this writing task."),
        ("Which example clearly describes what happened in a small everyday event?", "Yesterday my classmate picked up the pencil they had knocked off my desk and sharpened it for me.", ["Something small happened.", "The small event was good.", "I will state only the conclusion, not what happened."], "The listener needs to know who did what. Saying only that it was good leaves the event unclear."),
        ("How can you make an idea convincing?", "State the problem you observed, then give your solution and reasons", ["Do not describe the problem; say everyone else is wrong", "Claim that something nonexistent happens every day", "Give an unrelated solution without an explanation"], "Reasons should relate to a real event. An idea is not convincing if it describes something that never happened as a daily occurrence."),
    ],
)

K(
    "g3a_si", "Classical Text: “Sima Guang”", "Reading Comprehension", 3, "上", 8, "reasoning",
    "Use the notes to understand how Sima Guang broke a water jar to save a friend: a 瓮 is a large jar, and Guang struck it with a stone.",
    "yd_34",
    [
        ("What does a child fall into?", "A large jar", ["A well", "A river", "A cow's stomach"], "A child climbs onto a jar, slips, and falls into the water. A 瓮 is a large jar with a narrow opening."),
        ("What do the other children do?", "They all run away in fright", ["They all jump into the jar", "They break the jar with a stone", "They push the jar over"], "The classical text says that everyone leaves; they run away."),
        ("How does Sima Guang save the child?", "He breaks the jar with a stone, and the water flows out", ["He jumps into the jar", "He calls an adult after the child is already lost", "He covers the jar"], "Guang strikes and breaks the jar with a stone; the water pours out, and the child survives. He does not jump into the jar."),
        ("In the classical phrase “光持石击瓮破之,” what does “之” refer to?", "The jar", ["The stone", "The child who ran away", "Sima Guang himself"], "The phrase means that he broke the jar; “之” refers to the jar mentioned earlier."),
    ],
)

K(
    "g3a_zheng", "Reading: “Determined to Succeed”", "Reading Comprehension", 3, "上", 8, "reasoning",
    "Understand Tong Dizhou's two achievements: proving himself in secondary school and later separating a frog egg's outer membrane while studying abroad, bringing honor to China.",
    "yd_34",
    [
        ("Whose story does the passage tell?", "The biologist Tong Dizhou", ["Norman Bethune", "Zhao Yiman", "Sima Guang"], "Both achievements in the passage are Tong Dizhou's. Bethune worked at an operating table, and Zhao Yiman is associated with a coarse porcelain bowl."),
        ("How does he respond when he falls behind in his first term of secondary school?", "He studies hard, catches up in every subject, and earns a perfect score in geometry", ["He drops out and never studies again", "He asks someone else to take his exams", "He hides his report card"], "The principal plans to make him repeat or leave school. Tong studies early under streetlights and improves within six months."),
        ("What does he achieve the second time he is determined to succeed?", "While abroad, he separates the outer membrane of a frog egg, an experiment his professor had failed to complete for years", ["He breaks a jar to save a friend", "He works beside an operating table for sixty-nine hours", "He returns a coarse porcelain bowl to a soldier"], "The egg is tiny, about the size of a millet grain, and has a thin membrane. He succeeds through repeated practice."),
        ("Who does Tong's determination serve in each story?", "First himself, then the people of China", ["The Lion King both times", "China the first time, then giving up on his studies", "Both times he wants a magic gourd"], "He believes that hard work can help him do what others can do. Later, when foreign classmates look down on Chinese students, he decides to bring honor to his country."),
    ],
)

K(
    "g3a_zhen", "Reading: “The Operating Table Is the Battlefield”", "Reading Comprehension", 3, "上", 8, "reasoning",
    "Understand how Bethune treated the operating table as a doctor's post during the Battle of Qihui and worked continuously for sixty-nine hours.",
    "yd_34",
    [
        ("Who keeps performing surgery in the passage?", "Dr. Norman Bethune", ["Tong Dizhou", "Zhao Yiman", "Sima Guang"], "Bethune was a Canadian doctor who treated the wounded during the Battle of Qihui."),
        ("As the battle becomes more dangerous, what does he say when the health minister asks him to leave?", "“The operating table is a doctor's post. Soldiers do not leave their posts, and neither can I.”", ["“The surgery can wait; I will go somewhere safe.”", "“I cannot perform surgery.”", "“Leave all the wounded in the fire.”"], "He considers saving the wounded part of the battle. Some wounded people can be evacuated, but he stays."),
        ("What conditions does he work in?", "Smoke and shrapnel fill the air around the temple, but he calmly removes shrapnel", ["The battlefield has been quiet for three days", "He tells stories to classmates in a classroom", "He stops whenever a shell explodes"], "The danger highlights his refusal to leave. An assistant extinguishes a fire that lands nearby, and Bethune continues working."),
        ("How long does the Battle of Qihui last, and how long does he work without stopping?", "The battle lasts three days and nights; he works beside the operating table for sixty-nine hours", ["The battle lasts an hour, and he works for an hour", "The battle lasts three days, and he immediately leaves", "He works for sixty-nine days before the battle begins"], "The passage gives precise times. When the battle ends in victory, he has worked beside the operating table for sixty-nine hours."),
    ],
)

K(
    "g3a_wan", "Reading: “A Coarse-Porcelain Bowl”", "Reading Comprehension", 3, "上", 8, "reasoning",
    "Understand how Zhao Yiman and the soldiers share a coarse porcelain bowl and how she gives her meal to a sick young messenger.",
    "yd_34",
    [
        ("What object is central to the passage, and who is it about?", "A coarse porcelain bowl; the anti-Japanese heroine Zhao Yiman", ["A magic gourd; Wang Bao", "A piece of cheese; the ant captain", "A large jar; Sima Guang"], "The bowl is a key object. Zhao Yiman uses it to eat and to care for the soldiers."),
        ("What does she do after the messenger brings her a soldier's bowl?", "She asks the messenger to return the bowl", ["She breaks it immediately", "She forbids the soldiers to use bowls", "She locks it away forever"], "The soldiers need their bowls. She does not want them to go without one for her sake."),
        ("When the bowl returns to her, what does she do at mealtime?", "Puts some food back in the pot and eats the same amount as the soldiers", ["Eats a double portion and gives the soldiers leftovers", "Lets the messenger eat while she watches", "Throws all the food away"], "She accepts the bowl because everyone insists, but still eats no more than the soldiers."),
        ("What does she do with her food when the young messenger becomes ill?", "Gives her food to him", ["Sends the sick person to carry wounded soldiers at the front", "Puts the bowl away so no one can eat", "Gives the bowl only to the Lion King"], "She cares about the soldiers more than herself. The ordinary bowl shows that she shares both hardship and good fortune with them."),
    ],
)

K(
    "g3a_yd8", "Language Arts Unit 8: “An Unforgettable Experience”", "Writing Basics", 3, "上", 8, "procedural",
    "Describe an experience clearly and explain why it was memorable. In the speaking task “Asking for Help,” explain what you do not understand and thank the person who helps.",
    "xz_34",
    [
        ("Which passage sounds most like “An Unforgettable Experience”?", "During a relay race, the baton slipped in my hand and my classmate shouted, “Hold on!” I still remember the moment I crossed the finish line.", ["That time was unforgettable.", "Memorable. Very memorable. Extremely memorable.", "Relay. Noodles. Poetry."], "It describes what happened and the moment that stayed in the writer's mind. Repeating “memorable” does not tell the reader what happened."),
        ("Which sentence does not describe the experience specifically?", "That experience was unforgettable.", ["The baton slipped in my hand during the handoff.", "My classmate's voice was louder than the whistle.", "My heart kept pounding after I crossed the finish line."], "The slipping baton, shouted words, and pounding heart are details. Saying only that it was unforgettable leaves the story empty."),
        ("What is a good way to ask someone for help?", "Explain what you do not understand, listen to the answer, and say thank you", ["Do not state the problem; say the other person should know", "Interrupt as soon as the person starts speaking", "Change the answer to its opposite and claim that was what they meant"], "Tell the person what you are asking. Interrupting or changing the answer is not asking for help."),
        ("How can you review this piece of writing?", "After reading it, ask whether someone can follow what happened and why it was memorable", ["Count only the word “really”", "Delete everything except “memorable”", "Use the same sentences for any event"], "If the same sentences fit any other event, the experience has not been described yet."),
    ],
)

# ---------- Grade 3, Book 2 ----------
# 2026 spring revision (6-3 system). Unit 2 includes “The Wolf That Wagged Its Tail,” not “The Pot and the Iron Pot.”
# Unit 3 includes “The Undersea World,” “The Mason Bee,” and “The Little Shrimp”; Unit 4 includes poems and “The Invention of Paper,” “The Zhaozhou Bridge,” and “A Painting Famous Around the World.”
# Unit 5 includes “Mr. Carrot's Long Mustache,” “I Turned into a Tree,” and the writing task “Wonderful Imagination”; there is no language arts review.
# “The Clock of Flowers,” “Bees,” “The Other Side of the Universe,” “The Haircut Master,” and “The Hat Shop” are no longer included.

K(
    "g3b_jue", "Poem: “Quatrain” — “Beautiful Mountains and Rivers in Spring”", "Poetry", 3, "下", 1, "conceptual",
    "Recite Du Fu's five-character “Quatrain” and distinguish it from his seven-character poem about two orioles.",
    "gs_34",
    [
        ("What is the next line after “迟日江山丽”?", "春风花草香", ["泥融飞燕子", "沙暖睡鸳鸯", "两个黄鹂鸣翠柳"], "“迟日江山丽” is followed by “春风花草香.” The lines about thawing mud and warm sand come later; the line about two orioles is from another poem."),
        ("What is the next line after “泥融飞燕子”?", "沙暖睡鸳鸯", ["春风花草香", "一行白鹭上青天", "窗含西岭千秋雪"], "The thawed mud brings swallows, and the warm sand is where mandarin ducks sleep."),
        ("Who wrote the “Quatrain” that begins “迟日江山丽”?", "Du Fu", ["Du Mu", "Li Bai", "Su Shi"], "Both poems titled “Quatrain” are by Du Fu. Du Mu wrote “Mountain Walk” and “Qingming.”"),
        ("Which line belongs to this five-character “Quatrain,” not the poem about two orioles?", "沙暖睡鸳鸯", ["一行白鹭上青天", "门泊东吴万里船", "窗含西岭千秋雪"], "“沙暖睡鸳鸯” is from the same poem as “迟日江山丽.” The lines about egrets, boats, and snowy peaks belong to the seven-character poem."),
    ],
)

K(
    "g3b_hui", "Poem: “Huichong's Spring River at Dusk”", "Poetry", 3, "下", 1, "conceptual",
    "Recite Su Shi's poem inspired by Huichong's painting and distinguish the poet from the painter.",
    "gs_34",
    [
        ("What is the next line after “竹外桃花三两枝”?", "春江水暖鸭先知", ["蒌蒿满地芦芽短", "正是河豚欲上时", "春江水暖鹅先知"], "The next line says that the ducks are the first to sense the warming river. The mugwort and pufferfish appear later. It is ducks, not geese."),
        ("What is the next line after “蒌蒿满地芦芽短”?", "正是河豚欲上时", ["春江水暖鸭先知", "竹外桃花三两枝", "正是河豚欲下时"], "Mugwort covers the ground and the reed shoots are still short; it is the season when pufferfish swim upstream."),
        ("Who wrote this poem?", "Su Shi", ["Huichong", "Du Fu", "Du Mu"], "Huichong was the painter. Su Shi wrote the poem inspired by the painting “Spring River at Dusk.”"),
        ("What does “春江水暖鸭先知” mean?", "Ducks in the water are the first to feel the river warm up", ["Geese on the shore know first", "Pufferfish report the weather", "Peach blossoms warm the water"], "Ducks swim in the river, so they are the first to feel the spring water warming."),
    ],
)

K(
    "g3b_qu", "Poem: “On the Road to Sanqu”", "Poetry", 3, "下", 1, "conceptual",
    "Recite Zeng Ji's poem and distinguish its four or five oriole calls from the two orioles in Du Fu's poem.",
    "gs_34",
    [
        ("What is the next line after “梅子黄时日日晴”?", "小溪泛尽却山行", ["绿阴不减来时路", "添得黄鹂四五声", "春风花草香"], "The plum-ripening season brings sunny days. When the stream ends, the traveler takes a mountain path. The lines about shade and orioles come later."),
        ("What is the next line after “绿阴不减来时路”?", "添得黄鹂四五声", ["小溪泛尽却山行", "梅子黄时日日晴", "两个黄鹂鸣翠柳"], "There is as much shade on the return as on the way out, with four or five more oriole calls. “Two orioles sing among green willows” is from another Du Fu poem."),
        ("Who wrote “On the Road to Sanqu”?", "Zeng Ji", ["Zeng Gong", "Du Fu", "Su Shi"], "Song-dynasty poet Zeng Ji wrote this poem. Zeng Gong was a different writer. Du Fu wrote “Quatrain,” and Su Shi wrote “Huichong's Spring River at Dusk.”"),
        ("Which line belongs to “On the Road to Sanqu,” not Du Fu's seven-character “Quatrain”?", "添得黄鹂四五声", ["两个黄鹂鸣翠柳", "一行白鹭上青天", "窗含西岭千秋雪"], "The line about four or five oriole calls describes sounds heard along the mountain path. The lines about willows, egrets, and western peaks are from Du Fu's seven-character poem."),
    ],
)

K(
    "g3b_yan", "Reading: “Swallows”", "Reading Comprehension", 3, "下", 1, "reasoning",
    "Notice the swallows' feathers, wings, and tails, and the comparison of wires to a musical staff.",
    "yd_34",
    [
        ("Which three features of the swallow does the passage describe?", "Its feathers, wings, and tail", ["Its beak, claws, and eyes", "Only its color, not its shape", "Lotus leaves, flowers, and seedpods"], "It has glossy black feathers, graceful light wings, and a tail like scissors."),
        ("What is the swallow's tail compared to?", "Scissors", ["A musical staff", "A large round plate", "A small fan"], "The tail is compared to scissors. The musical staff comparison is for the wires."),
        ("What are the wires and the swallows perched on them compared to?", "A musical staff and notes", ["Scissors and a ribbon", "A large plate and a white lotus", "A key and a door"], "The thin wires look like a staff, and the swallows perched on them become notes in a song about to be played."),
        ("Where do the swallows arrive from, bringing life to spring?", "The south", ["The seabed", "Inside a cow's stomach", "The snow-covered western peaks"], "In March, swallows arrive from the south and join the lively spring scene."),
    ],
)

K(
    "g3b_he", "Reading: “Lotus Flowers”", "Reading Comprehension", 3, "下", 1, "reasoning",
    "Notice the appearance of the lotus leaves and flowers, and how the speaker imagines becoming a lotus flower.",
    "yd_34",
    [
        ("What are the lotus leaves like in the passage?", "Crowded together like large, bright-green plates", ["Sparse like a few needles", "Golden like small fans", "Red like stamps"], "The leaves crowd together like large green plates. The fan-shaped leaves belong to the ginkgo trees in “Autumn Rain.”"),
        ("How do the white lotus flowers grow?", "They emerge between the large leaves", ["They are all submerged", "They grow on tree branches", "They are all buds and never open"], "Some flowers are opening, some are fully open, and others are still buds; they all emerge between the leaves."),
        ("What does the speaker suddenly imagine?", "That they have become a lotus flower", ["That they have become a little fish", "That they have left the pond and gone home", "That they have become the painter's brush"], "The speaker imagines being a lotus flower dressed in snow-white clothes."),
        ("What do the dragonfly and little fish do in the speaker's imagination?", "Tell the speaker about the joy of flying and last night's dream", ["Pick all the lotus flowers", "Go inside a cow's stomach", "Break a jar on the shore"], "When the wind stops, the dragonfly tells of the joy of flying in the morning, and the fish tells of a dream from the night before."),
    ],
)

K(
    "g3b_kun", "Reading: “Insect Notes”", "Reading Comprehension", 3, "下", 1, "reasoning",
    "Read four short pieces by Wang Zengqi and distinguish compound eyes, ladybugs, rhinoceros beetles, and grasshoppers from Fabre's separate piece about mason bees.",
    "yd_34",
    [
        ("Who wrote “Insect Notes”?", "Wang Zengqi", ["Jean-Henri Fabre", "Bing Xin", "Xiao Hong"], "Wang Zengqi wrote these notes. Fabre wrote the later piece about mason bees. Bing Xin wrote “Soap Bubbles,” and Xiao Hong wrote “Fire Clouds.”"),
        ("What are an insect's compound eyes like?", "They are made up of many small eyes", ["One eye exactly like a human's", "A hard shell on the wings", "A horn on its head"], "A compound eye consists of many small eyes. A dragonfly's large eyes are compound eyes; the rhinoceros beetle has a horn on its head."),
        ("Which insect is nicknamed “Ladybug” in the passage?", "A ladybird beetle", ["A grasshopper", "A mason bee", "A rhinoceros beetle"], "Ladybugs are also called ladybird beetles. Some eat aphids and are beneficial, while the twenty-eight-spotted ladybird that eats potato leaves is a pest."),
        ("Which pair of grasshopper wings is used for flying?", "The thin pair at the back that flaps", ["The hard protective pair at the front", "The horn on its head", "The tiny units in its compound eyes"], "The front pair protects the body; the back pair is used for flying. The horn belongs to a rhinoceros beetle."),
    ],
)

K(
    "g3b_bi", "Language Arts Unit 1: Similes and Personification", "Sentences", 3, "下", 1, "procedural",
    "Distinguish a simile such as “like a large plate” from personification such as “the dragonfly tells me.” The speaking task is to plan a spring outing; in “My Plant Friend,” describe an observed plant using a simile or personification.",
    "jz_34",
    [
        ("What figure of speech appears in “The lotus leaves are like large, bright-green plates”?", "Simile", ["Personification", "Rhetorical question", "Parallelism"], "The leaves are compared to plates, so this is a simile. A plate cannot speak, so the leaves are not personified."),
        ("What figure of speech appears in “A little fish swims below and tells me about its dream last night”?", "Personification", ["Simile", "Hyperbole without a human action", "A list of numbers"], "Fish cannot speak. Giving the fish the human action of telling a story is personification."),
        ("Which sentence uses a simile?", "Dewdrops are like clear beads.", ["The flowers nod to me in the wind.", "The grass pokes its head out of the soil.", "The spring breeze gently wakes the willow."], "The dewdrops are compared to beads. Nodding, poking out a head, and waking someone are examples of personification."),
        ("Which sentence uses personification?", "The spring breeze gently wakes the willow.", ["The willow branches are like green ribbons.", "The lotus leaves are like large plates.", "The sun is like a red ball."], "A breeze cannot wake someone; describing it as doing so is personification. The ribbons, plates, and ball are similes."),
    ],
)

K(
    "g3b_shou", "Reading: “Waiting by a Stump for a Rabbit”", "Reading Comprehension", 3, "下", 2, "reasoning",
    "Use the notes to understand how a man from the state of Song waits by a stump for another rabbit and becomes a laughingstock.",
    "yd_34",
    [
        ("How does the rabbit die?", "It runs into a stump and breaks its neck", ["A farmer shoots it with an arrow", "A wolf carries it off", "It jumps into a large jar"], "The rabbit runs into a stump and dies from a broken neck. The word “stump” means the base of a tree."),
        ("What does the farmer do after finding the rabbit?", "Puts down his tools and waits by the stump all day", ["Lets the rabbit go and keeps farming", "Pulls out the stump", "Explains the story to the people of Song"], "He drops his plow and waits for another rabbit, hoping to get one for free."),
        ("What happens?", "No more rabbits come, and the people of Song laugh at him", ["He finds a rabbit every day", "His crops grow better", "A sheep runs out of the stump"], "He cannot get another rabbit, and the people of Song laugh at him. He neglects his crops too."),
        ("What lesson does the story teach?", "Do not rely on one lucky accident and refuse to work or change your approach", ["Waiting by a stump is the hardest work", "Rabbits come every day", "Waiting is better than farming"], "Finding a rabbit by chance once does not mean it will happen again. Getting something for nothing is unreliable."),
    ],
)

K(
    "g3b_lang", "Reading: “The Wolf That Wagged Its Tail”", "Reading Comprehension", 3, "下", 2, "reasoning",
    "Read Yan Wenjing's fable: a wolf trapped in a pit pretends to be a dog, wags its tail to fool an old goat, and eventually reveals its aggression.",
    "yd_34",
    [
        ("Who falls into a pit and asks for help?", "A wolf", ["A real dog", "An old goat", "A little chicken"], "The wolf cannot climb out, so it asks a passing goat for help. The chicken is an excuse it invents."),
        ("How does the wolf pretend to be a dog?", "It claims to be loyal and tame and wags its stiff tail vigorously", ["It immediately admits it is a wolf", "It pushes the old goat into the pit", "It waits by a stump for a rabbit"], "It claims it jumped into the pit to save a chicken and wags its tail to prove it is a dog. A dog's tail is soft; the wolf's tail is stiff."),
        ("Why does the old goat refuse to rescue it?", "The goat recognizes the vicious wolf from its lies and stiff tail", ["The goat cannot speak", "The pit actually contains a chicken", "The wolf has already climbed out"], "The goat says that no matter how well the wolf wags its tail, it is still vicious. The wolf bares its teeth and reveals its true nature."),
        ("What lesson does the fable teach?", "Do not be fooled by sweet words or a false appearance; look at someone's true nature", ["Every animal that wags its tail is a good dog", "Every trapped animal should be rescued", "The old goat should not ask questions"], "A disguise and a wagging tail cannot hide harmful actions. Trusting too easily can lead to deception."),
    ],
)

K(
    "g3b_lu", "Reading: “The Deer's Antlers and Legs”", "Reading Comprehension", 3, "下", 2, "reasoning",
    "Understand that the deer admires its antlers and dislikes its legs, but the legs save it from a lion while the beautiful antlers nearly cause its capture.",
    "yd_34",
    [
        ("What does the deer like and dislike about itself by the pond?", "It likes its beautiful antlers and dislikes its slender legs", ["It likes its legs and dislikes its antlers", "It likes the lion's mane", "It thinks its antlers and legs are both useless"], "It calls its antlers elegant but thinks its legs are thin and ugly."),
        ("What helps the deer run quickly when the lion chases it?", "The four slender legs it dislikes", ["The antlers on its head", "The pond water", "The branches in the tree"], "Its legs carry it far ahead of the lion. Its antlers do not help it run."),
        ("Why is the deer nearly caught later?", "Its antlers become caught in a branch", ["Its legs suddenly break", "It stops to praise the lion", "The pond floods the path"], "While admiring itself, the deer catches its beautiful antlers in a branch and is held back as the lion comes closer."),
        ("What does the deer finally understand?", "Its ugly legs save it, while its beautiful antlers nearly cost it its life", ["Both its antlers and legs should be cut off", "It should rely only on the lion for protection", "A beautiful appearance is always useful"], "Do not judge usefulness only by appearance. Something you dislike may be valuable."),
    ],
)

K(
    "g3b_chi", "Reading: “The Pond and the River”", "Reading Comprehension", 3, "下", 2, "reasoning",
    "Read Krylov's fable: the pond seeks comfort and eventually dries up, while the river keeps flowing and remains useful.",
    "yd_34",
    [
        ("How does the pond feel about the river?", "It thinks the river rushes all day and should relax like the pond", ["It praises the river for resting well", "It asks the river to wait by a stump", "It thinks the river has already dried up"], "The pond thinks lying in soft mud is most comfortable and asks when the river will ever rest."),
        ("Why does the river refuse to stop?", "Water stays fresh by flowing, and the river has work to do for people", ["It is afraid the pond will laugh at it", "It is waiting for a rabbit", "It can no longer flow"], "The river says still water spoils. By flowing, it can irrigate fields, carry things, and be remembered."),
        ("What happens to them after many years?", "The pond fills with silt and dries up, while the river keeps flowing and is praised", ["Both dry up", "The pond becomes an ocean and the river disappears", "They lie down and sleep together"], "The pond that seeks only comfort gradually fills with mud. The river remains known because it continues to work."),
        ("Who wrote this fable, and what is its lesson?", "Krylov; do not seek comfort alone and refuse to work", ["Yan Wenjing; wagging a tail proves goodness", "Han Feizi; waiting by a stump is the hardest work", "Aesop; beautiful antlers are most useful"], "Krylov wrote “The Pond and the River.” Its lesson is that life should keep moving and contributing instead of seeking comfort alone."),
    ],
)

K(
    "g3b_cheng", "Language Arts Unit 2: “守株待兔” and “亡羊补牢”", "Vocabulary", 3, "下", 2, "conceptual",
    "Explain “守株待兔,” “亡羊补牢,” and “揠苗助长” without reversing their lessons. The speaking task is giving advice; the writing task is describing a picture.",
    "cy_34",
    [
        ("Who is criticized by the idiom “守株待兔”?", "Someone who relies on luck and clings to one accidental success", ["Someone who repairs a pen as soon as a sheep is lost", "Someone who tests the depth for themselves", "Someone who waters seedlings on time"], "“守株待兔” describes someone who stops working after one lucky find and waits for it to happen again."),
        ("What does “亡羊补牢” mean?", "It is not too late to fix a problem after something goes wrong", ["Ignore a lost sheep", "Tear down the sheep pen", "Wait by a tree for the sheep to return"], "After losing a sheep, the person repairs the pen so no more are lost. It means timely correction can still help."),
        ("Which idiom fits “pulling seedlings taller, only to make them wither”?", "揠苗助长", ["亡羊补牢", "守株待兔", "坐井观天"], "“揠苗助长” means rushing against natural rules and making things worse. “坐井观天” means having a narrow view."),
        ("A friend advises you to quickly correct a mistake you have already made. Which idiom fits best?", "亡羊补牢", ["守株待兔", "揠苗助长", "坐井观天"], "“亡羊补牢” best describes timely correction. “守株待兔” and “揠苗助长” describe unhelpful behavior."),
    ],
)

K(
    "g3b_kuai", "Reading Club: “Small Stories, Big Lessons”", "Reading Comprehension", 3, "下", 2, "conceptual",
    "Read fables in this reading club. The stories are short, and readers should explain the lesson after reading.",
    "yd_34",
    [
        ("What kind of books are read in “Small Stories, Big Lessons”?", "Fables", ["A copied class schedule", "A blank book with no words", "A multiplication table"], "“Waiting by a Stump for a Rabbit,” Aesop's fables, and Krylov's fables are short stories with lessons. A blank book and a multiplication table are not."),
        ("After reading a story like “Waiting by a Stump for a Rabbit,” what should you explain?", "The lesson of the story", ["How tall the stump is", "What color the rabbit is", "How many punctuation marks there are"], "The important part of a short story with a big lesson is the lesson. Remembering only the rabbit's color misses the point."),
        ("Which way of reading fits this activity?", "Explain the lesson in your own words and tell it to someone else", ["Look only at the cover and say you have finished", "Reverse the lesson and claim that is the author's meaning", "Close the book whenever an animal appears"], "After understanding a story, you should be able to explain it. Reversing the lesson changes the fable."),
        ("Why are Krylov's fables suitable for this reading club?", "Each is a short story with its own lesson", ["They contain only today's news", "They only teach papermaking", "They are maps without stories"], "“The Pond and the River” is one such fable. News, papermaking, and maps are not the stories for this activity."),
    ],
)

K(
    "g3b_hai", "Reading: “The Undersea World”", "Reading Comprehension", 3, "下", 3, "reasoning",
    "Understand that the seabed is not silent: it has sounds, and marine animals move in different ways.",
    "yd_34",
    [
        ("Are there sounds under the sea?", "Yes. Animals make many different sounds", ["There is no sound at all", "Only boats make sounds", "Only people speak underwater"], "Some sounds resemble buzzing bees, chirping birds, barking dogs, or even snoring."),
        ("How do sea cucumbers move?", "They crawl by contracting their muscles, moving about four meters per hour", ["They swim dozens of kilometers per hour", "They spray water backward to move quickly", "They stand still on a boat"], "Sea cucumbers move slowly. Barracudas can swim dozens of kilometers per hour."),
        ("How do squid and octopuses move backward quickly?", "They suddenly jet water forward and are pushed back by the reaction force", ["They are pushed by sea cucumbers", "They hold onto a barracuda's tail", "They climb onto the beach and jump"], "They expel water forward, which propels their bodies backward."),
        ("How does the passage describe the seabed?", "It has unusual scenery and abundant resources", ["It has no life or light", "It is exactly like dry land", "It has only one kind of fish"], "The seabed has mountains, valleys, and plant life like forests and grasslands, and animals move in different ways."),
    ],
)

K(
    "g3b_shi", "Reading: “The Mason Bee”", "Reading Comprehension", 3, "下", 3, "reasoning",
    "Understand Fabre's experiment to test whether mason bees find their way home without relying on memory: carry them far away, mark them, and see which ones return.",
    "yd_34",
    [
        ("Who wrote this passage?", "Jean-Henri Fabre", ["Wang Zengqi", "Bing Xin", "Xiao Hong"], "Fabre recorded this experiment. Wang Zengqi wrote “Insect Notes,” not this experiment."),
        ("What hypothesis does Fabre test?", "Mason bees do not rely on memory to find their way home", ["Mason bees cannot find their way at all", "Mason bees can build the Zhaozhou Bridge", "Mason bees stay in the hive and never leave"], "He observes that the bees return after collecting honey and suspects they do not memorize their route. The experiment tests that idea."),
        ("How is the experiment carried out?", "Put the bees in a paper bag, carry them about four kilometers to an unfamiliar place, mark them white, and release them", ["Open the bag at the hive entrance", "Cut off their wings before releasing them", "Take them to the seabed"], "His younger daughter waits by the hive. Releasing bees far away in unfamiliar surroundings can show whether they retrace a memorized route."),
        ("What does the experiment show?", "Many marked bees return, suggesting they use a special ability rather than memory to navigate", ["Not one bee returns", "The white mark guides them by itself", "Bees can only fly forward and cannot return"], "At least fifteen of about twenty bees return home. They still find the hive despite unfamiliar scenery along the way."),
    ],
)

K(
    "g3b_xia", "Reading: “The Little Shrimp”", "Reading Comprehension", 3, "下", 3, "reasoning",
    "Understand how the narrator and A-Cheng raise stream shrimp in a jar under a grape trellis and observe the differences among them.",
    "yd_34",
    [
        ("Where is the shrimp jar kept?", "Under a grape trellis in the yard, where it collects rainwater in summer", ["In an underwater valley", "Beside a beehive", "Under the Zhaozhou Bridge"], "Sunlight filters through the trellis and makes the water look like round mirrors. The unused jar is a good place to raise shrimp."),
        ("How do newly grown shrimp differ from the “old shrimp”?", "Young shrimp are transparent like glass; older ones are grayish, with mud and moss on their backs and tails", ["Both are golden yellow", "The old ones are transparent, and the young ones are covered in moss", "Neither has a shell"], "The passage uses color and mud to distinguish their ages. The transparent shrimp are young; the older ones are nicknamed “old shrimp.”"),
        ("What do the shrimp do when a small bamboo twig touches them while they are resting?", "They jump away, waving their long legs and opening and closing their claws", ["They remain completely still", "They immediately build a house on shore", "They jet water and swim backward four kilometers"], "Their legs, claws, antennae, and eyes all move. This is their reaction to being disturbed, not Fabre's bee experiment."),
        ("Why do more little shrimp appear in the jar later?", "Larger shrimp carry many round eggs under their bodies, which soon hatch", ["A-Cheng brings a basket from the sea every day", "Fallen leaves turn into shrimp", "Mason bees lay eggs in the jar"], "The author catches larger shrimp and sees eggs underneath. Fallen leaves from the trellis also collect in the jar, with small shrimp gathering beneath them."),
    ],
)

K(
    "g3b_yd3", "Language Arts Unit 3: “I Did a Small Experiment”", "Writing Basics", 3, "下", 3, "procedural",
    "Describe a small experiment in order: what you prepared, what you did, what changed, and the result.",
    "xz_34",
    [
        ("Which sequence clearly describes a small experiment?", "First list the materials, then the steps, next the observations, and finally the result", ["Give the result first, add what you ate yesterday, and only then list the materials", "Write only “It was fun”", "Describe the steps in reverse order"], "As in “The Mason Bee,” an experiment should show what happened first and what came next. A sudden detail about food makes the process confusing."),
        ("Which paragraph stays focused on the experiment of a seed sprouting?", "I put a bean on wet cotton and sprinkled it with water each day. On the third day, it split and a tiny shoot appeared.", ["I put a bean on wet cotton. Yesterday I scored a goal in soccer.", "Beans. Soccer. Noodles.", "The shoot is pretty. Math problems are hard."], "The first paragraph describes how this bean sprouts. Switching to soccer or math leaves the experiment."),
        ("What should you do with a sentence in an experiment log that is unrelated to the experiment?", "Delete or revise it so every sentence supports the experiment", ["Add more sentences without checking whether they relate", "Rename the experiment after the unrelated event", "Keep only the unrelated sentence"], "A clear process avoids extra details that distract from the experiment."),
        ("What is missing from “I did an experiment. It was fun”?", "The steps and observations; readers cannot tell what you did", ["A map", "The poet's name", "The bridge railing"], "“Fun” is only a feeling. Include the materials, procedure, changes, and result to explain the experiment."),
    ],
)

K(
    "g3b_yuan", "Poem: “New Year's Day”", "Poetry", 3, "下", 4, "conceptual",
    "Recite Wang Anshi's poem and learn that “屠苏” is a wine and that new peach charms replacing old ones are an early form of spring couplets.",
    "gs_34",
    [
        ("What is the next line after “爆竹声中一岁除”?", "春风送暖入屠苏", ["千门万户曈曈日", "总把新桃换旧符", "春风送暖入屠城"], "Firecrackers mark the passing of the old year as people drink Tusu wine. The lines about every household come later."),
        ("What is the next line after “千门万户曈曈日”?", "总把新桃换旧符", ["春风送暖入屠苏", "爆竹声中一岁除", "总把新符换旧桃"], "Sunlight reaches every household, and people replace old peach charms with new ones. Do not reverse “new peach” and “old charm.”"),
        ("Who wrote “New Year's Day”?", "Wang Anshi", ["Du Fu", "Du Mu", "Su Shi"], "Wang Anshi wrote this poem. Du Mu wrote “Qingming”; do not confuse the two."),
        ("What does “屠苏” refer to in the poem?", "A kind of wine", ["A kind of firecracker", "A peach charm", "A door"], "People traditionally drank Tusu wine at New Year. The spring breeze brings warmth into the cup."),
    ],
)

K(
    "g3b_qing", "Poem: “Qingming”", "Poetry", 3, "下", 4, "conceptual",
    "Recite Du Mu's poem and distinguish its author from Du Fu; understand that Xinghua Village is where the inn is, not the inn itself.",
    "gs_34",
    [
        ("What is the next line after “清明时节雨纷纷”?", "路上行人欲断魂", ["借问酒家何处有", "牧童遥指杏花村", "路上行人欲断肠"], "In the Qingming rain, travelers on the road feel heartbroken. The question about finding an inn comes later."),
        ("What is the next line after “借问酒家何处有”?", "牧童遥指杏花村", ["路上行人欲断魂", "清明时节雨纷纷", "牧童遥指杏花酒"], "The traveler asks where to find an inn, and the shepherd points toward Xinghua Village."),
        ("Who wrote “Qingming”?", "Du Mu", ["Du Fu", "Li Bai", "Wang Anshi"], "Du Mu wrote both “Qingming” and “Mountain Walk.” Du Fu did not write this poem."),
        ("What is Xinghua Village, which the shepherd points to?", "A village with an inn", ["The poet's hometown", "A snowy western peak", "Tianmen Mountain"], "The traveler wants a place to shelter from the rain and have a drink; the shepherd points to the village where an inn is located."),
    ],
)

K(
    "g3b_jiu", "Poem: “Thinking of My Brothers in Shandong on the Ninth Day of the Ninth Month”", "Poetry", 3, "下", 4, "conceptual",
    "Recite Wang Wei's poem for the Double Ninth Festival and learn that “山东” refers to the region east of Mount Hua, not today's Shandong Province.",
    "gs_34",
    [
        ("What is the next line after “独在异乡为异客”?", "每逢佳节倍思亲", ["遥知兄弟登高处", "遍插茱萸少一人", "春风送暖入屠苏"], "Alone in a foreign place, the traveler misses family even more during festivals. The lines about climbing high and carrying dogwood come later; Tusu wine appears in “New Year's Day.”"),
        ("What is the next line after “遥知兄弟登高处”?", "遍插茱萸少一人", ["每逢佳节倍思亲", "独在异乡为异客", "遍插茱萸少两人"], "The poet imagines his brothers climbing high and wearing dogwood at Double Ninth, with himself as the one person missing."),
        ("Who wrote “Thinking of My Brothers in Shandong on the Ninth Day of the Ninth Month,” and what festival is it?", "Wang Wei; the Double Ninth Festival", ["Wang Anshi; Spring Festival", "Du Mu; Qingming", "Wang Zhihuan; Mid-Autumn Festival"], "Wang Wei's poem is for Double Ninth. Spring Festival appears in “New Year's Day,” and Du Mu wrote “Qingming.” Wang Zhihuan wrote “Ascending Stork Tower.”"),
        ("What does “山东” in the title refer to?", "The region east of Mount Hua, near the poet's home", ["Today's Shandong Province", "Xinghua Village", "A bridge in Bianjing"], "In the Tang dynasty, “山东” often meant east of Mount Hua. Wang Wei is thinking of his brothers there, not using the modern provincial name."),
    ],
)

K(
    "g3b_zhi", "Reading: “The Invention of Paper”", "Reading Comprehension", 3, "下", 4, "reasoning",
    "Learn that before paper was widely used, people wrote on oracle bones, bamboo, wood, and silk; paper became inexpensive and convenient after Cai Lun improved papermaking in the Eastern Han dynasty.",
    "yd_34",
    [
        ("Before paper was widely used, where did people write?", "On turtle shells and animal bones, bamboo and wooden strips, and expensive silk", ["Only on modern computers", "Only on the railings of the Zhaozhou Bridge", "On white paper before paper was invented"], "Earlier writing was carved on oracle bones or cast into bronze. Bamboo slips were heavy, and silk was expensive."),
        ("What did Cai Lun do?", "He improved papermaking in the Eastern Han by building on earlier experience", ["Designed the Zhaozhou Bridge in the Sui dynasty", "Painted “Along the River During the Qingming Festival” in the Northern Song", "First saw tree bark in the Tang dynasty"], "About 1,900 years ago, Cai Lun improved papermaking. He was neither the bridge builder Li Chun nor the painter Zhang Zeduan."),
        ("What materials did Cai Lun mainly use to make paper?", "Tree bark, hemp fibers, old cloth, and worn fishing nets", ["Gold and pearls", "A single turtle shell", "Lotus leaves and swallow feathers"], "These materials were easy to obtain, so the resulting paper was inexpensive and convenient for writing."),
        ("What changed after papermaking was improved?", "Paper became affordable and useful, and later spread to many places", ["People stopped writing", "Silk became cheaper than paper", "Writing returned to oracle bones"], "Paper is easy to write on and carry. This important ancient Chinese invention later influenced other countries."),
    ],
)

K(
    "g3b_zhao", "Reading: “The Zhaozhou Bridge”", "Reading Comprehension", 3, "下", 4, "reasoning",
    "Learn that the Zhaozhou Bridge is a stone arch bridge designed by Li Chun in the Sui dynasty, with smaller arches above the main arch and no piers below.",
    "yd_34",
    [
        ("Who designed and helped build the Zhaozhou Bridge?", "Li Chun, a stonemason of the Sui dynasty", ["Sima Guang of the Song dynasty", "Li Bai of the Tang dynasty", "Cao Cao of the Han dynasty"], "Also called Anji Bridge, the Zhaozhou Bridge was designed by Sui stonemason Li Chun."),
        ("Are there piers beneath the bridge?", "No. It has one large arch and no piers", ["It has many piers", "It is supported by wooden posts", "It floats on the water"], "The bridge is built entirely of stone, with one large arch and no piers beneath it."),
        ("Why are there smaller arches above the main arch?", "They reduce the weight, let floodwater pass, and add beauty", ["To provide homes for people", "They were carved randomly because there was not enough stone", "The small arches cannot let water through"], "There are two small arches on each side above the main arch. This design was an innovation in bridge building."),
        ("What is carved on the railings?", "Dragons", ["Lotus flowers and swallows", "Sparrows", "Jujube pits"], "The railings have detailed dragon carvings, some intertwined and others baring their claws."),
    ],
)

K(
    "g3b_ming", "Reading: “A Painting Famous Around the World”", "Reading Comprehension", 3, "下", 4, "reasoning",
    "Learn that this is Zhang Zeduan's Northern Song painting “Along the River During the Qingming Festival,” depicting lively life along the Bian River in Bianjing.",
    "yd_34",
    [
        ("What is the painting described in the passage called?", "“Along the River During the Qingming Festival”", ["“Huichong's Spring River at Dusk”", "A design for the Zhaozhou Bridge", "A map showing only one bridge"], "The world-famous painting shows the busy Northern Song capital during the Qingming Festival. Huichong's painting is the one Su Shi wrote about in another lesson."),
        ("Who painted it?", "Zhang Zeduan of the Northern Song dynasty", ["Li Chun of the Sui dynasty", "Cai Lun of the Eastern Han", "Du Fu of the Tang dynasty"], "Zhang Zeduan was a Northern Song painter. Li Chun built a bridge, and Cai Lun improved papermaking; neither painted this work."),
        ("Whose lives does the painting mainly depict?", "People from all walks of life along the Bian River in the capital Bianjing", ["One little shrimp only", "Sea cucumbers under the sea only", "A wolf that fell into a pit"], "The streets show farmers, boatmen, merchants, officials, and scholars. Nearly every occupation appears."),
        ("What is one especially lively scene in the painting, and where is the painting kept today?", "A large boat is about to pass under a bridge as people help; it is kept at the Palace Museum in Beijing", ["The boat has sunk underwater; the painting is under the Zhaozhou Bridge", "The bridge is empty; Cai Lun still has the painting", "The painter gave it to a shepherd"], "The boatmen lower the mast as people watch from above and below the bridge. The long scroll is now housed at the Palace Museum in Beijing."),
    ],
)

K(
    "g3b_yd4", "Language Arts Unit 4: Traditional Chinese Festivals", "Reading Comprehension", 3, "下", 4, "reasoning",
    "Match this unit's poems to their festivals: New Year's Day is Spring Festival, Qingming is Tomb-Sweeping Day, and the ninth day of the ninth month is Double Ninth.",
    "yd_34",
    [
        ("Which festival is described in “New Year's Day”?", "Spring Festival, on the first day of the lunar year", ["Tomb-Sweeping Day", "Double Ninth Festival", "Mid-Autumn Festival"], "Firecrackers, Tusu wine, and replacing old peach charms all mark the arrival of a new year."),
        ("Which festival is described in “Thinking of My Brothers in Shandong on the Ninth Day of the Ninth Month,” and what do people often do?", "Double Ninth Festival; climb to high places and wear dogwood", ["Spring Festival; set off firecrackers and drink Tusu wine", "Tomb-Sweeping Day; look for an inn in the rain", "Dragon Boat Festival; race dragon boats"], "The ninth day of the ninth month is Double Ninth. The poem describes brothers climbing high and wearing dogwood."),
        ("Which pair shows customs of the Dragon Boat Festival?", "Eat zongzi and race dragon boats", ["Eat mooncakes and admire the moon", "Drink Tusu wine and replace peach charms", "Climb high and wear dogwood"], "Zongzi and dragon-boat racing are Dragon Boat Festival customs. Mooncakes belong to Mid-Autumn, Tusu wine to Spring Festival, and dogwood to Double Ninth."),
        ("What is a suitable way to study traditional Chinese festivals?", "Choose one festival and explain its date, customs, and related poems", ["Assign Qingming rain to Spring Festival", "Say dragon-boat racing is a Double Ninth custom", "Write only the festival's name, not what people do"], "The date, customs, and poem should all belong to the same festival; do not mix them up."),
    ],
)

K(
    "g3b_hulu", "Reading: “Mr. Carrot's Long Mustache”", "Reading Comprehension", 3, "下", 5, "reasoning",
    "Understand how Mr. Carrot's mustache keeps growing after jam sticks to it and becomes useful to others along the way.",
    "yd_34",
    [
        ("Why does Mr. Carrot's mustache grow longer?", "Jam sticks to it, and it keeps growing the next day", ["He waters it every day like a seedling", "A lion chases him and scares it longer", "Cai Lun makes him a mustache from tree bark"], "Once jam sticks to the mustache, it does not stop growing. This is imagination, not gardening."),
        ("What does a little boy use the long mustache for?", "A kite string", ["A pier for the Zhaozhou Bridge", "A fishing net hung underwater", "A stump to wait beside for rabbits"], "The mustache trails behind Mr. Carrot, and the boy holds it to fly his kite."),
        ("What does Mrs. Bird use the mustache for?", "A clothesline for diapers", ["Food in the nest", "A fishing rod", "A stone arch bridge"], "As the mustache keeps growing, Mrs. Bird uses it as a line to hang diapers on."),
        ("What is wonderful about this story?", "A mustache keeps growing and helps other people along the way", ["It only records how to grow carrots", "The mustache never changes", "It takes place in a real laboratory"], "The jam, kite string, and clothesline all depend on the growing mustache. A real mustache would not grow this way."),
    ],
)

K(
    "g3b_shu", "Reading: “I Turned into a Tree”", "Reading Comprehension", 3, "下", 5, "reasoning",
    "Understand how Yingying turns into a tree and her mother begins a picnic in its branches.",
    "yd_34",
    [
        ("Why does Yingying wish to turn into a tree?", "So her mother cannot find her and she can keep playing outside", ["She wants to give her mother shade from the rain", "She dislikes her name", "There is homework to do in the tree"], "She is having fun and does not want her mother to call her home, so she wishes she could become a tree."),
        ("Who first comes under the tree after she transforms?", "Her mother", ["A tailor", "Sima Guang", "A sparrow"], "Her mother arrives with a basket to look for Yingying but does not recognize the tree as her daughter."),
        ("What does her mother do in the tree?", "Finds food in a bird's nest and eats with the little animals", ["Cuts down the tree", "Reads classical prose to the tree", "Makes Yingying turn back immediately"], "Her mother climbs the tree, finds food in a nest, and eats with the little animals. Yingying watches hungrily."),
        ("What is wonderful about the story's imagination?", "A child really turns into a tree but cannot keep the secret", ["It only records real steps for planting a tree", "Yingying stays in a classroom throughout", "Nothing happens in the tree"], "The child becoming a tree and her mother's picnic in its branches are imagined events, all centered on the transformation."),
    ],
)

K(
    "g3b_duan", "Writing: “Wonderful Imagination”", "Writing Basics", 3, "下", 5, "procedural",
    "Imagine an unusual event boldly, but keep the writing focused on that one idea instead of suddenly switching to unrelated content.",
    "xz_34",
    [
        ("For “A Pencil's Dream,” which paragraph stays focused on one idea?", "The pencil dreams it becomes a boat and delivers letters across the gridlines of a workbook river.", ["The pencil dreams it becomes a boat. I ate noodles for dinner yesterday.", "Dreams. Math. Soccer.", "Pencil. Noodles. Recess."], "The first paragraph describes one dream. Switching to dinner or math leaves the central idea."),
        ("What should you do if a paragraph contains a sentence unrelated to the imagined event?", "Delete or revise it so every sentence supports the main idea", ["Add as many sentences as possible, regardless of the idea", "Change the main idea to match the unrelated sentence", "Keep only the unrelated sentence"], "Staying focused means preventing extra details from taking the paragraph off course."),
        ("Which idea is a good focus for an imaginative story?", "Mr. Carrot's mustache keeps growing and helps others along the way", ["Today", "Things", "Beautiful"], "A specific focus tells readers what the story imagines. “Today” and “things” are too broad."),
        ("How can you check whether your imaginative paragraph is clear?", "After reading it, ask whether every sentence describes the unusual event", ["Count the commas only", "Check whether the first sentence is long", "Put every sentence in a random order"], "If some sentences describe a different event, the paragraph loses focus."),
    ],
)

K(
    "g3b_mo", "Reading: “Ink Wash Painting of Childhood”", "Reading Comprehension", 3, "下", 6, "reasoning",
    "Read Zhang Jilou's three short poems: fishing by a stream, playing in a river, and picking mushrooms in the woods.",
    "yd_34",
    [
        ("Who wrote “Ink Wash Painting of Childhood,” and what are its three poems about?", "Zhang Jilou; the stream, the river, and the woods", ["Bing Xin; the street, stream, and river", "Xiao Hong; the stream only", "Fabre; mason bees, shrimp, and grasshoppers"], "The poems describe fishing by a stream, swimming in a river, and a pine grove after rain. Bing Xin wrote “Soap Bubbles.”"),
        ("In “By the Stream,” what can be seen before the splash?", "A red dragonfly perched on a fishing rod above a calm stream", ["Children are already splashing one another in the river", "Mushrooms in the pine grove are wearing hats", "Soap bubbles are flying into the sky"], "The willow reflects in the stream, turning the water green with shadows. A red dragonfly still rests on the rod, and no fish has bitten yet."),
        ("What does “fish and laughter bounce across the grass” describe?", "A fish has been caught, and the child laughs with delight", ["A shrimp is angry in a jar", "A sparrow flies back to its branch", "A shepherd points toward Xinghua Village"], "A splash breaks the reflections. The quiet stream suddenly has a fish and laughter."),
        ("What does the phrase “water hyacinth” in quotation marks refer to?", "A child who swims well and dives into the water", ["A real aquatic plant", "The red dragonfly on a fishing rod", "A little mushroom in the woods"], "The river poem describes children playing like a flock of ducks. The one who dives and reappears with shining teeth is a child, not a plant."),
    ],
)

K(
    "g3b_fei", "Reading: “Soap Bubbles”", "Reading Comprehension", 3, "下", 6, "reasoning",
    "Read Bing Xin's “Soap Bubbles” and notice their lightness, roundness, and beauty.",
    "yd_34",
    [
        ("Who wrote “Soap Bubbles”?", "Bing Xin", ["Xiao Hong", "Jean-Henri Fabre", "Ye Shengtao"], "Bing Xin wrote “Soap Bubbles.” Xiao Hong wrote “Fire Clouds.”"),
        ("What are the soap bubbles blown by the children like?", "Light and round, with beautiful colors in the sunlight", ["Heavy and square", "They fall into the dirt and never rise", "Only black"], "The bubbles are light, clear, and transparent; they float slowly in the breeze and show beautiful colors."),
        ("How do the children feel as the bubbles rise?", "They hope the bubbles will fly high but worry they will burst", ["They hope the bubbles burst immediately", "They do not look at them", "They are happy only when they stomp on them"], "The passage shows the children gazing up and following the bubbles, feeling both proud and worried."),
        ("Why does the author describe the bubbles in such detail?", "To express the beauty and tenderness of a childhood game", ["To explain how to make soap", "To describe how rain falls", "To teach papermaking"], "This passage recalls childhood. Though small, the bubbles hold the children's happiness."),
    ],
)

K(
    "g3b_que", "Reading: “The Sparrow”", "Reading Comprehension", 3, "下", 6, "reasoning",
    "Understand how Lenin notices that a sparrow with a dark red breast is missing and how a boy later returns it to its branch.",
    "yd_34",
    [
        ("How many sparrows originally live in the birch tree, and what color are their breasts?", "Three: two pink and one dark red", ["One, entirely white", "Two, both dark red", "Five, all gray"], "Lenin visits the three sparrows every day. The missing one has a dark red breast."),
        ("What seems unusual about the boy when he talks about the sparrow?", "He looks down and answers vaguely, as if he knows more than he says", ["He loudly says he ate the bird", "He finds the bird before Lenin and immediately confesses", "He has never visited the park"], "Lenin asks whether he has seen the bird. The boy says no but appears uneasy."),
        ("Why does Lenin not scold the boy directly?", "He trusts the boy to understand and asks whether the sparrow will return", ["He does not notice that the bird is missing", "He throws the boy out of the park", "He thinks the bird flew south for winter, unrelated to the boy"], "Lenin cares about whether the sparrow can return. By not exposing the boy, he leaves him a chance to correct his mistake."),
        ("What is on the branch the next day?", "The dark-red-breasted sparrow has returned, and the boy says it was there a moment ago", ["None of the three sparrows return", "Lenin puts the bird in a cage", "The boy says he never saw it, and it has not returned"], "The bird is back in the birch tree. The boy admits quietly that it was just there, and Lenin understands that he made things right."),
    ],
)

K(
    "g3b_xin", "Reading: “I Cannot Break My Promise”", "Reading Comprehension", 3, "下", 6, "reasoning",
    "Understand how Song Qingling remembers she promised to teach Xiaozhen to fold a flower basket and keeps her promise instead of going to see pigeons.",
    "yd_34",
    [
        ("Who is the “I” in the passage, and to whom does she keep her promise?", "Song Qingling; she keeps her promise to Xiaozhen", ["Lenin; he keeps a promise to the sparrow", "Yingying; she keeps a promise to her mother", "Cai Lun; he keeps a promise to Li Chun"], "One morning, the Song family prepares to go out. Their second daughter, Song Qingling, remembers her promise to Xiaozhen from the day before."),
        ("What does she especially want to do at first?", "Visit her uncle to see his pigeons; he has offered to give her one", ["Go to the park to find the sparrow", "Visit sea cucumbers under the sea", "Teach Xiaozhen to fold a paper boat instead of a flower basket"], "She looks forward to seeing the pigeons with pointed beaks and red eyes, but she already has another promise."),
        ("What do her parents suggest, and how does she respond?", "They suggest teaching Xiaozhen another day; she says she has remembered the promise and cannot break it", ["They decide to stay and wait for Xiaozhen too", "She immediately goes with them to her uncle's house", "She says promises do not count"], "Her father takes her hand to leave, and her mother suggests apologizing to Xiaozhen later. Qingling pulls her hand back and insists on staying."),
        ("Xiaozhen does not arrive. How does Qingling feel?", "She is bored at home but does not regret keeping her promise", ["She regrets not seeing the pigeons", "She blames Xiaozhen for making her wait", "She decides never to make another promise"], "Xiaozhen still has not come back by lunchtime. Qingling says she does not regret staying because she kept her promise."),
    ],
)

K(
    "g3b_yd6", "Language Arts Unit 6: “People Around Us with Distinctive Traits”", "Writing Basics", 3, "下", 6, "procedural",
    "Describe a distinctive trait of someone you know and illustrate it with a specific event instead of piling up adjectives.",
    "xz_34",
    [
        ("Which paragraph describes a person's distinctive trait more clearly?", "My younger brother is always in a hurry. His shoelaces are still untied, but he has already dashed onto the playground.", ["My brother is good, very good, extremely good.", "Brother. Playground. Yesterday's noodles.", "My desk mate is a person."], "Show impatience through a visible action. Repeating “good” does not tell readers what is special."),
        ("Which sentence does not describe the trait specifically?", "Grandma is very kind.", ["Grandma gives me the biggest strawberry.", "My brother runs outside without tying his shoelaces.", "Xiaohua cannot hear the radio while reading, even when it is loud."], "“Very kind” is only an opinion. Giving away a strawberry, running with untied shoes, and not hearing the radio are specific events."),
        ("If you plan to write about “the class storyteller” but describe what they ate for lunch, is that appropriate?", "No. Lunch is unrelated to the person's trait and should be removed or revised", ["Yes. More sentences always show more traits", "Yes. What they eat is their only trait", "No. A description can include only a person's name"], "Someone may do many things, but the details in the piece should support the trait you are describing."),
        ("How can you check whether the writing shows a distinctive trait?", "Ask whether readers can tell what the person is like without seeing the name", ["Count how many times you used “very”", "Check whether the first sentence has a comma", "Change the order of events"], "If the same description fits anyone, the person's distinctive trait is not clear yet."),
    ],
)

K(
    "g3b_huo", "Reading: “Fire Clouds”", "Reading Comprehension", 3, "下", 7, "reasoning",
    "Read Xiao Hong's “Fire Clouds” and notice how quickly the colors and shapes change.",
    "yd_34",
    [
        ("Who wrote “Fire Clouds”?", "Xiao Hong", ["Bing Xin", "Ye Shengtao", "Jean-Henri Fabre"], "Xiao Hong wrote “Fire Clouds.” Bing Xin wrote “Soap Bubbles.”"),
        ("What happens to the animals on the ground when the fire clouds appear?", "A white dog turns red, and a red rooster turns gold", ["They all turn blue", "They hide in the sea", "Their colors do not change"], "The sunset glow shines down and changes the colors of the dog and rooster."),
        ("Why does the passage describe the fire clouds' colors?", "They are numerous and change quickly", ["Fire clouds are only red", "The colors change only once an hour", "The sky remains gray"], "The clouds shift from bright red and gold to purple-yellow and gray-lily shades, changing from moment to moment."),
        ("What happens to the shapes of the horse, dog, and lion in the clouds?", "They quickly become unclear and change into other shapes", ["They stay motionless in the sky", "They fall to the ground and become real animals", "They turn into the Zhaozhou Bridge"], "The fire-cloud shapes also change quickly. The horse-shaped cloud soon becomes hard to recognize."),
    ],
)

K(
    "g3b_bao", "Reading: “Before the Storm”", "Reading Comprehension", 3, "下", 7, "reasoning",
    "Follow events before and after the wind rises and notice how the weather, animals, and people behave unusually.",
    "yd_34",
    [
        ("What is the first weather change before the storm arrives?", "The air grows stuffy, clouds cover the sun, and strange dark clouds spread across the sky", ["The sun gets brighter, and the sky turns bluer", "It immediately snows all day", "The sky remains cloudless"], "The trees and grass grow dim. The air feels oppressive before the wind rises, unlike the red glow of fire clouds."),
        ("How do the cows, horses, birds, and insects react?", "The cows and horses grow restless, birds and insects hide, and branches and leaves become still", ["They all run to watch the fire clouds", "The cows and horses keep grazing quietly", "The insects fly four kilometers away for an experiment"], "The cow lowers its head, and the horse swishes its tail and breathes heavily. Then everything falls silent, even the leaves."),
        ("What do people do?", "They hurry to gather their things and get home before the thunderstorm", ["They go outside to fly kites", "They stand on the beach to look at sea cucumbers", "They ignore the storm and keep sleeping"], "Lightning is already warning them, and people in the village know the storm is near."),
        ("How do the wind and thunder arrive?", "A cool breeze comes first, then strong wind, a brief lull, and finally rumbling thunder", ["There is no wind or thunder at all", "The thunder stops before the dark clouds appear", "The breeze continues until the next day"], "The passage presents the breeze as the first warning. Strong wind ruffles the chickens' feathers, and thunder announces the storm."),
    ],
)

K(
    "g3b_miao", "Reading: “Our Wonderful World”", "Reading Comprehension", 3, "下", 7, "reasoning",
    "Read Peter Seymour's passage and distinguish the wonders of the sky from those of the earth.",
    "yd_34",
    [
        ("Who wrote this passage?", "The British writer Peter Seymour", ["Xiao Hong", "Bing Xin", "Jean-Henri Fabre"], "Peter Seymour wrote “Our Wonderful World.” Xiao Hong wrote “Fire Clouds”; do not confuse the authors."),
        ("Which two aspects of the world does the author describe?", "The sky and the earth", ["Only the seabed", "Only one stone bridge", "Only one storm"], "The passage introduces the world's wonders, describes the sky and earth separately, and then draws them together."),
        ("Which changes in the sky does the passage describe?", "Sunrise, clouds, sunset, and stars", ["Only one color at noon", "Only a reflection of the Zhaozhou Bridge", "Lotus flowers covering the sky"], "The sun rises in the morning, clouds change shape, evening light appears at sunset, and stars come out at night."),
        ("What is the main idea to understand after reading?", "Careful observation reveals endless wonders in the sky and on the earth", ["The world has only one color", "People have already seen every wonder", "Clear descriptions do not require observation"], "The earth includes growing plants, colorful fruit, summer shade, autumn leaves, and winter ice and snow. Careful observation reveals many wonders."),
    ],
)

K(
    "g3b_yd7", "Language Arts Unit 7: The Giant Panda, a National Treasure", "Writing Basics", 3, "下", 7, "procedural",
    "Introduce giant pandas by describing their appearance, diet, habitat, and why they are considered a national treasure.",
    "xz_34",
    [
        ("Which paragraph introduces giant pandas by separate aspects?", "Their bodies are white, with black eye patches, ears, and legs. They love bamboo and live in China's mountains.", ["Giant pandas are cute, very cute, extremely cute.", "Giant pandas. Yesterday's soccer. Noodles.", "They live under the sea and mainly eat sea cucumbers."], "Appearance, diet, and habitat all describe pandas. Repeating “cute” tells readers little, and sea cucumbers are not their food."),
        ("Which sentence wrongly gives a giant panda another animal's traits?", "It has a tail like scissors and sings on an electric wire.", ["It has black patches around its eyes.", "It holds bamboo and eats slowly.", "It is a national treasure of China."], "The scissor-like tail belongs to the swallow in “Swallows.” Do not assign a swallow's traits to a panda."),
        ("Why include details such as “loves bamboo” and “black and white”?", "They tell readers what the animal looks like and how it lives", ["To reach a word count", "To change the subject to fire clouds", "To show that it lives in the sea"], "An introduction should include details that distinguish the subject. Simply calling it cute is not enough."),
        ("How can you check this introduction?", "See whether it covers appearance, habits, and why the animal is precious", ["Check only whether it mentions noodles", "Count the exclamation marks", "Replace “giant panda” with any animal without changing a sentence"], "If the same sentences fit any animal, these aspects have not been described specifically."),
    ],
)

K(
    "g3b_mao", "Reading: “The Slow Tailor and the Impatient Customer”", "Reading Comprehension", 3, "下", 8, "reasoning",
    "Understand how one person is impatient for clothes while the tailor works slowly, creating a long and funny wait.",
    "yd_34",
    [
        ("What are the customer and tailor like?", "The customer is impatient, and the tailor is slow", ["Both are impatient", "The customer is slow, and the tailor is impatient", "Neither has a personality"], "The title pairs their traits: the tailor is slow, while the customer is in a hurry."),
        ("What does the customer ask for at first?", "A newly made padded coat as soon as possible", ["To look at the fabric again next year", "Only to chat with the tailor", "For the tailor to make a pair of shoes first"], "The impatient customer keeps urging the tailor, saying the coat is needed soon."),
        ("How does the tailor respond to each reminder?", "He agrees readily but continues to work slowly", ["He finishes it that night", "He refuses the job", "He makes the customer sew it"], "He says “Certainly,” but does not hurry. The more the customer urges him, the longer the wait becomes."),
        ("What makes the story funny?", "The impatient customer and slow tailor never get in sync", ["They calculate the price incorrectly", "The tailor cannot speak", "The customer turns into a tree"], "One person wants the coat immediately, while the other never rushes. Their conflicting personalities create the humor."),
    ],
)

K(
    "g3b_lou", "Reading: “The Leaky Roof” (漏)", "Reading Comprehension", 3, "下", 8, "reasoning",
    "Understand how a tiger and a thief both mistake “漏” for a monster, although the old woman means that the roof is leaking.",
    "yd_34",
    [
        ("What does the old woman mean by “漏”?", "The roof is leaking", ["A monster named “漏”", "The tiger's name", "The thief's nickname"], "The old couple says they fear “漏” more than wolves or tigers. They mean rain leaking through the roof."),
        ("Who mistakes “漏” for a frightening monster?", "The tiger and the thief", ["Only the old woman", "Only the old man", "The donkey and the mouse"], "The thief on the roof and the tiger outside the donkey shed both hear the word and imagine a monster more frightening than themselves."),
        ("After the thief falls onto the tiger's back, what do they each think?", "The tiger thinks “漏” has arrived, while the thief thinks “漏” is carrying him away", ["They recognize each other and go home together", "The old woman is riding the tiger", "The thief drives the tiger out of the village"], "The terrified tiger runs, and the frightened thief clings tightly. Each mistakes the other for “漏.”"),
        ("What makes the story funny?", "They both fear “漏,” which is not a monster, and scare each other away", ["“漏” really eats the house", "The tiger and thief become friends and repair the roof", "The old woman really releases a monster"], "The misunderstanding frightens both the thief and the tiger. The real “漏” is only a leaking roof."),
    ],
)

K(
    "g3b_zao", "Reading: “The Jujube Pit” (枣核)", "Reading Comprehension", 3, "下", 8, "reasoning",
    "Understand how Zaohé, a child the size of a jujube pit, helps his family and recovers the livestock that were taken.",
    "yd_34",
    [
        ("Why is the child named “枣核” (“Jujube Pit”)?", "His parents wished for even a child as small as a jujube pit, and that is how small he was when he was born", ["He loves eating jujubes", "He looks like a bridge", "The county magistrate names him"], "The couple longs for a child. When one the size of a jujube pit is born, they give him that name."),
        ("Does Zaohé grow bigger as he gets older?", "No. He stays tiny but works hard and helps his parents", ["He becomes a giant", "He turns into a tree", "He stays small and cannot help at all"], "He grows older without changing size. Though small, he is willing to work."),
        ("How does he recover the livestock after it is taken away?", "He hides in a donkey's ear, follows the officials, and drives the ox and donkey back", ["He asks the tiger and thief to fight", "He becomes the county magistrate", "He waits beside a stump"], "Officials take the village's oxen and donkeys. Zaohé is small enough to hide in an ear without being noticed."),
        ("What is the main lesson of the story?", "A small person can accomplish great things; do not judge by size", ["Short people should do nothing", "The magistrate likes children as small as a jujube pit", "Livestock will return to the village on their own"], "Zaohé brings the livestock back and stops the people who bullied the villagers from returning. Ability is not determined by size."),
    ],
)

K(
    "g3b_yd8", "Language Arts Unit 8: Storytelling Club", "Writing Basics", 3, "下", 8, "procedural",
    "When telling a story, explain who encountered what and what makes it funny. In “What a Wonderful Imagination,” imagine boldly but keep the story understandable.",
    "xz_34",
    [
        ("At a storytelling club, which way of telling “The Leaky Roof” is clear?", "First explain that the old woman fears a leaking roof, then tell how the tiger and thief mistake each other for a monster", ["Only mention an old woman", "Begin with the tiger running away without explaining “漏”", "Say that Zaohé and the tailor are the same tiger"], "Listeners need the characters, misunderstanding, and outcome. Dropping in one name does not begin a story."),
        ("Which opening is more suitable for “What a Wonderful Imagination”?", "The tailor's needle pierces the cloth, and it turns into a talking bird.", ["The weather is nice today.", "Cloth. Needle. Bird.", "I want to write a story but have not decided who it is about."], "The first sentence already introduces a strange change, so listeners know where the imagination begins. “The weather is nice” is not yet unusual."),
        ("An imaginative story is fun, but halfway through it switches to an unrelated event. Is that a good idea?", "No. Keep the whole story focused on the same unusual event", ["Yes. The more often it switches, the funnier it is", "Yes. Listeners do not need to know the ending", "No. An imaginative story cannot include animals"], "“The Leaky Roof” is funny because the misunderstanding about “漏” continues throughout. An unfocused story loses its humor."),
        ("After hearing someone's story, which response shows that you listened carefully?", "Say who did what and what you found most interesting", ["Only say that you did not listen", "Reverse the story and claim that is what the storyteller meant", "Remember only the storyteller's clothing color"], "A storytelling club is about telling and listening clearly. Changing the plot means it is no longer the same story."),
    ],
)
