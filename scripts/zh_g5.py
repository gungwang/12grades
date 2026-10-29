# -*- coding: utf-8 -*-
"""Grade 5, fall and spring. Fall follows the 2026 national textbook sequence (six-three system); spring follows the current/commonly used 2026 spring sequence."""
from zh_lib import K

# "上" and "下" are term identifiers passed to K and must remain for the topic builder.
# ---------- Grade 5, fall ----------
# Follow the 2026 fall national textbook sequence (six-three system).
# Combine The Cowherd and the Weaver Girl (Parts 1 and 2) into one topic; split the three poems in Unit 4 into separate topics.
# Split the three poems in Unit 7 into separate topics. Unit 5 has no language-practice section; list the "Introduce an Object" writing task separately.
# Do not create standalone topics for the sample texts "The Whale" and "Making a Wind Vane." List the reading-club story "Once Upon a Time, There Was a Mountain" separately.
# List the speaking and writing tasks "My Favorite Possession," "A Caricature of My Teacher," and "What I Want to Tell You" separately; include the others in the corresponding language-practice section.
# Exclude older-edition texts "Birds' Paradise," "Paving Stones," "The Squirrel," "The Island," "Moonlight," "Song of Everlasting Sorrow," and "My Everlasting Fruit."
# Also exclude "Excellent Beyond Words" and "Terrible Beyond Words." Move "The Egret" to Unit 7 and "The Old Summer Palace" to Unit 4.

K(
    "g5a_gui", "Reading The Osmanthus Rain", "Reading Comprehension", 5, "上", 1, "reasoning",
    "Understand Qi Jun's childhood memories of shaking osmanthus flowers and watching them fall like rain.",
    "yd_56",
    [
        ("What does The Osmanthus Rain refer to?", "Flowers falling when the osmanthus tree is shaken, like rain", ["A real summer downpour", "An umbrella made of osmanthus flowers", "Water collected in the yard"], "The flowers fall on the author's hair and clothes, so she calls it osmanthus rain."),
        ("How does the narrator feel while shaking the osmanthus tree?", "Happy and eager for more flowers to fall", ["Afraid the flowers will fall", "Unwilling to help", "Only wanting to cut the tree down"], "Shaking the flowers is a joy for the child, who hugs the tree and shakes it hard."),
        ("What else can osmanthus flowers be used for at home?", "Making osmanthus cakes and giving some away", ["They can only be looked at, not collected", "They can be used for writing", "They can be fed to horses"], "The mother collects the flowers to make cakes and share with others. They are useful as well as beautiful."),
        ("After leaving home, what does the author remember when she smells osmanthus?", "The osmanthus rain of her childhood and hometown", ["The Qiantang River tide", "The fire at the Old Summer Palace", "A monkey on a boat"], "The scent of osmanthus is tied to childhood. This is a story about remembering one's hometown, written by Qi Jun."),
    ],
)

K(
    "g5a_luo", "Reading Peanuts", "Reading Comprehension", 5, "上", 1, "reasoning",
    "Understand Xu Dishan's use of peanuts to show that people should be useful rather than care only about appearances.",
    "yd_56",
    [
        ("Who wrote Peanuts?", "Xu Dishan", ["Qi Jun", "Liang Qichao", "Guo Moruo"], "Peanuts was written by Xu Dishan. Qi Jun wrote The Osmanthus Rain."),
        ("How are peanuts different from peaches, pomegranates, and apples?", "Peanuts grow underground instead of displaying their fruit on branches", ["Peanuts grow on the highest branches", "Peanuts cannot be eaten", "Peanuts bloom only at night and produce no fruit"], "The father says that peaches and the other fruits hang high on branches, while peanuts grow close to the ground."),
        ("What kind of person does the father hope his children will become?", "A useful person who helps others, not someone concerned only with appearances", ["Someone who likes to show off", "Someone who never works", "Someone concerned only with appearance"], "This is the most important point in the father's words in the text."),
        ("When does the mother suggest holding the harvest festival?", "After the peanuts have been harvested", ["Before the seeds are planted", "Before the peanuts bear fruit", "On the day the family moves away"], "They plant, harvest, and taste the peanuts before discussing how to live."),
    ],
)

K(
    "g5a_zhen", "Reading The Pearl Bird", "Reading Comprehension", 5, "上", 1, "reasoning",
    "Understand how Feng Jicai describes the birds gradually growing closer to people: from the cage to the desk, and finally to his shoulder. Trust can create a beautiful relationship.",
    "yd_56",
    [
        ("Who wrote The Pearl Bird?", "Feng Jicai", ["Xu Dishan", "Qi Jun", "Guo Moruo"], "The Pearl Bird was written by Feng Jicai. Xu Dishan wrote Peanuts, and Qi Jun wrote The Osmanthus Rain."),
        ("How do the birds initially behave toward the narrator?", "They are afraid of people and stay in the cage", ["They immediately land on someone's shoulder", "They fly out the window and never return", "They eat all the peanuts"], "When the friend first gives them to the author, they hide in the cage. They grow closer later."),
        ("What does the bird eventually do to show that it trusts the narrator?", "It lands on his shoulder and falls asleep", ["It breaks out of the cage", "It shakes flowers from an osmanthus tree", "It asks the father to discuss peanuts at the desk"], "The shoulder is very close to a person. The bird's willingness to sleep there shows real trust."),
        ("What does the idea that trust can create a beautiful world mean?", "People can feel safe and happy together when they trust each other", ["Keeping a bird locked up makes everything better", "People do not need to be kind to animals", "A beautiful world exists only in myths"], "The person respects the bird and does not disturb it, so it chooses to come closer. Trust goes both ways."),
    ],
)

K(
    "g5a_jing", "Writing: My Favorite Possession", "Writing Fundamentals", 5, "上", 1, "application",
    "Write about something you treasure: describe what it looks like, clearly recount how you got it or an event connected to it, and explain why it matters to you. Simply saying that you like it is not enough.",
    "xz_56",
    [
        ("When writing about a favorite possession, how can you make the events clear?", "Describe step by step how you got it and how you later used it", ["Only say that you liked it afterward", "Write only the title", "Put the result first and then stop"], "The reader should be able to follow the events, not just see the conclusion."),
        ("In a story called My Little Desk Lamp, which sentence describes an event?", "On moving day, Grandma wrapped it in an old towel and put it in my schoolbag.", ["The lamp is beautiful.", "I have a lamp.", "The words favorite possession."], "Wrapping it and putting it in the schoolbag show what happened. Saying it is beautiful or that you have one does not describe an event."),
        ("Which structure is more complete?", "Describe what it looks like, how it came to you, and why you treasure it", ["Write only the result", "Use each paragraph for an unrelated event", "Do not explain your connection to the item"], "The description, events, and feelings should connect to make the possession meaningful."),
        ("Which sentence describes events in detail?", "I held the handlebars, pushed off with my foot, and the bike rolled forward a little.", ["I learned to ride a bike.", "Riding a bike is difficult.", "The vehicle is a bicycle."], "Held, pushed off, and rolled forward are a sequence of actions. Simply saying that you learned does not describe the process."),
    ],
)

# The Chinese glyphs below are the assessed pronunciation targets; only these forms remain untranslated.
K(
    "g5a_yin", "Language Practice 1: Commonly Misread Characters", "Character Recognition and Writing", 5, "上", 1, "conceptual",
    "Pronounce commonly misread characters correctly instead of guessing from one component. For the class-agreement speaking task, make each rule specific and achievable rather than writing only a vague goal such as being united.",
    "sz_56",
    [
        ("How is the character 傍 pronounced?", "bàng", ["páng", "bāng", "pàng"], "The assessed pronunciation is bàng; do not guess from a phonetic component."),
        ("How is the character 羡 pronounced?", "xiàn", ["yán", "xiān", "yàn"], "The assessed pronunciation is xiàn."),
        ("How is the character 差 pronounced in the word meaning uneven?", "cī", ["chà", "chā", "chāi"], "In the word meaning uneven, 差 is pronounced cī; in the word meaning almost, it is pronounced chà."),
        ("How is the character 脆 pronounced?", "cuì", ["wēi", "cuī", "chuì"], "The assessed pronunciation is cuì."),
    ],
)

K(
    "g5a_di", "Reading Tunnel Warfare in Central Hebei", "Reading Comprehension", 5, "上", 2, "reasoning",
    "Understand the tunnels on the Central Hebei Plain: they provided shelter, routes, and ways to fight, as well as devices such as decoy tunnels and air vents.",
    "yd_56",
    [
        ("Where did tunnel warfare mainly take place?", "The Central Hebei Plain", ["Mianchi in the State of Qin", "The Qiantang River", "The Old Summer Palace"], "Central Hebei is in the middle of Hebei Province. The text describes tunnels used there during the War of Resistance against Japan."),
        ("How did the tunnels help in battle?", "They sheltered people, allowed them to move around, and helped them attack the enemy", ["They could store peanuts but could not shelter people", "They were used only to shake osmanthus flowers", "They were used only to park a ship"], "There were many entrances and connected routes, making the tunnels difficult for the enemy to understand."),
        ("What was the purpose of a decoy tunnel?", "To make enemy soldiers who entered take the wrong route", ["To send messages and fresh air to friendly forces", "To store food only", "To let egrets nest inside"], "It looked like a route but led to a dead end or trap. Air vents were used for ventilation."),
        ("What is the main idea of the text?", "The people of Central Hebei devised a clever and effective way to use tunnels during the war", ["The tunnels were magical caves from a myth", "The tunnels moved faster than cheetahs", "The tunnels were a stage built by Mei Lanfang"], "The text describes the tunnels' design, devices, and uses; it is not a fairy tale."),
    ],
)

K(
    "g5a_jiang", "Reading The General and the Prime Minister Make Peace", "Reading Comprehension", 5, "上", 2, "reasoning",
    "Retell the story of Lin Xiangru and Lian Po through the return of the jade, the meeting at Mianchi, and Lian Po's apology.",
    "yd_56",
    [
        ("Lin Xiangru took the He Shi Bi jade to Qin. What happened to it?", "He sent it back to Zhao with his men", ["He gave it to the Qin king, and Zhao received nothing", "Lian Po seized it", "It fell into the Mianchi pond"], "Lin Xiangru saw that the Qin king was insincere and arranged for the jade to be returned to Zhao. This is the story of returning the jade intact."),
        ("At the meeting in Mianchi, why did Lin Xiangru insist that the Qin king beat a drum?", "The Qin king had made the Zhao king play the se, so Lin Xiangru defended the Zhao king's dignity", ["He wanted to hear the Qin king sing", "Lian Po asked him to do it", "The drum was another name for the jade"], "The Qin king had recorded that the Zhao king played the se. Lin Xiangru risked his life to make the Qin king beat a drum for the Zhao king too."),
        ("Why did Lian Po later carry thorn branches to apologize?", "He realized Lin Xiangru had yielded for Zhao and that he himself was wrong", ["Lin Xiangru ordered soldiers to capture him", "The Qin king told him to apologize", "He wanted to get the jade back"], "To apologize, Lian Po took off his shirt, carried thorn branches, and went to Lin Xiangru's home."),
        ("In the title, who are the general and the prime minister?", "Lian Po is the general, and Lin Xiangru is the prime minister", ["Lin Xiangru is the general, and Lian Po is the prime minister", "Both men are generals of the Qin king", "The Zhao king is the general, and the Qin king is the prime minister"], "Lian Po was a senior general of Zhao, and Lin Xiangru later became a high-ranking official. Their reconciliation helped stabilize Zhao."),
    ],
)

K(
    "g5a_lie", "Reading What Is Faster Than a Cheetah?", "Reading Comprehension", 5, "上", 2, "reasoning",
    "Understand how this informational text compares speeds: cheetahs are fast, but peregrine falcons, aircraft, rockets, and meteoroids are faster; light is fastest.",
    "yd_56",
    [
        ("Why does the text begin with a cheetah?", "To show that cheetahs are fast, but that some things are even faster", ["To show that cheetahs are the slowest animals", "To show that cheetahs fought in tunnels", "To say that a cheetah is light"], "The text first establishes that cheetahs are fast, then compares them with faster things."),
        ("In the text, what is faster than a jet aircraft?", "A rocket", ["A person walking", "A turtle crawling on the ground", "A stationary rock"], "The comparisons move toward greater speed. A person, turtle, or rock cannot come after an aircraft in this sequence."),
        ("What does the text identify as the fastest thing known so far?", "Light", ["A cheetah", "The He Shi Bi jade", "Wind in a tunnel"], "The comparisons end with light, which has the greatest speed."),
        ("What method does the text mainly use?", "Comparing the speeds of several things", ["Telling only a myth", "Reciting only a poem", "Describing only how a ship sank"], "The title signals a comparison. Myths, poems, and shipwrecks are covered in other lessons."),
    ],
)

K(
    "g5a_nuo", "Reading The Wreck of the Normandy", "Reading Comprehension", 5, "上", 2, "reasoning",
    "Understand Victor Hugo's story of Captain Halway, who sends the women to safety after the ship is struck and remains on the bridge as it sinks.",
    "yd_56",
    [
        ("Who wrote The Wreck of the Normandy?", "Victor Hugo", ["Xu Dishan", "Feng Jicai", "Liang Qichao"], "This story was written by Victor Hugo. Xu Dishan wrote Peanuts, and Feng Jicai wrote The Pearl Bird."),
        ("Who was the captain in charge during the disaster?", "Captain Halway", ["Lin Xiangru", "Lian Po", "Mei Lanfang"], "Halway was the captain of the Normandy. Lin Xiangru and Lian Po appear in The General and the Prime Minister Make Peace."),
        ("How did he organize the evacuation after the ship was struck?", "He kept order, sent the women to the lifeboats first, and had the crew follow", ["He sent the crew away first and left the passengers aboard", "He ordered everyone to jump into the sea and abandoned the ship", "He boarded a lifeboat first"], "He kept order and rescued the passengers first. He did not leave with them."),
        ("What happened to Halway as the ship sank?", "He stood on the bridge and sank with the ship", ["He escaped in the last lifeboat", "He went to make the Qin king beat a drum", "He sailed the ship into a tunnel in Central Hebei"], "He fulfilled his duty as captain and did not escape. The drum and tunnel belong to other lessons."),
    ],
)

K(
    "g5a_hua", "Writing: A Caricature of My Teacher", "Writing Fundamentals", 5, "上", 2, "application",
    "Write about a teacher's most distinctive trait using a specific event, not vague praise. Here, caricature means emphasizing a trait; it does not mean drawing a comic.",
    "xz_56",
    [
        ("Which sentence captures a teacher's distinctive trait in a caricature?", "When she gets excited while teaching, she swings her chalk and always gets a white mark on her sleeve", ["The teacher is very good.", "The word caricature.", "We have a teacher."], "The white mark on her sleeve is a visible habit. Saying only that she is good could describe anyone."),
        ("Which idea does not fit this writing task?", "Writing only about how a cheetah is slower than light, without mentioning the teacher", ["The math teacher always draws the equals sign slowly and neatly", "The language teacher taps the desk lightly while reading aloud", "The PE teacher gives short, loud commands when students line up"], "The topic is a teacher. A comparison of speeds from an informational text would be off topic."),
        ("How should you choose material for writing about a teacher?", "Choose an event that shows the teacher's distinctive trait", ["Copy the same vague praise for every teacher", "Write only the school's name", "Write news unrelated to the teacher"], "The details should support the trait."),
        ("Which sentence is vague?", "The teachers at our school are very, very good.", ["Before asking a question, he always pushes his glasses up.", "When collecting homework, she waits at the door for the last student.", "When he reads a poem aloud, he holds the final word steadily."], "Very good does not say what is good about them. The other sentences describe specific actions."),
    ],
)

# The Han characters below are the assessed polyphonic pronunciation targets.
K(
    "g5a_duo", "Language Practice 2: Polyphonic Characters", "Character Recognition and Writing", 5, "上", 2, "conceptual",
    "Pronounce polyphonic characters correctly in context, including their less common readings.",
    "sz_56",
    [
        ("How is the character 强 pronounced in the word meaning reluctantly?", "qiǎng", ["qiáng", "jiàng", "qiāng"], "In the word meaning reluctantly, it is pronounced qiǎng; in powerful it is qiáng, and in stubborn it is jiàng."),
        ("How is the character 鲜 pronounced in the phrase meaning little-known?", "xiǎn", ["xiān", "xiàn", "qiǎn"], "In the phrase meaning little-known, it is pronounced xiǎn; in fresh, it is xiān."),
        ("How is the character 弹 pronounced in the word for ammunition?", "dàn", ["tán", "dān", "tàn"], "In words for bullets and ammunition, it is pronounced dàn; in words for playing an instrument or elasticity, it is tán."),
        ("How is the character 模 pronounced in the word meaning appearance?", "mú", ["mó", "mò", "mé"], "In words meaning appearance or mold, it is pronounced mú; in model or imitate, it is mó."),
    ],
)

# The Han idioms below are the assessed vocabulary; surrounding prose is translated.
K(
    "g5a_cheng", "Language Practice 2: Using Idioms", "Vocabulary", 5, "上", 2, "conceptual",
    "Choose idioms that fit the context and distinguish four-character expressions with opposite or easily confused meanings.",
    "cy_56",
    [
        ("Which idiom describes persisting until a task is complete?", "坚持不懈", ["半途而废", "三心二意", "守株待兔"], "坚持不懈 means persisting. 半途而废 and 三心二意 describe failing to finish or being halfhearted."),
        ("Which idiom means focusing wholeheartedly while studying?", "专心致志", ["心不在焉", "东张西望", "走马观花"], "专心致志 means concentrating. 心不在焉 means not paying attention."),
        ("Which sentence uses its idiom correctly?", "He crammed the night before the exam: 临阵磨枪.", ["He reviews every day, so he is 临阵磨枪.", "He prepared well in advance, so he is 临阵磨枪.", "He finished planning a month early, so he is 临阵磨枪."], "临阵磨枪 means preparing in a hurry at the last minute. Reviewing every day does not fit."),
        ("What is the difference between 亡羊补牢 and 守株待兔?", "One means taking timely action to fix a problem; the other means waiting idly for luck", ["Both praise hard work", "Both are about sheep", "They mean exactly the same thing"], "亡羊补牢 emphasizes that it is still possible to fix a problem; 守株待兔 criticizes expecting a reward without effort."),
    ],
)

K(
    "g5a_hai", "Reading The Hunter and Hailebu", "Reading Comprehension", 5, "上", 3, "reasoning",
    "Understand how Hailebu reveals a secret and turns to stone to save his neighbors from disaster.",
    "yd_56",
    [
        ("Who was the little white snake Hailebu rescued?", "The Dragon King's daughter", ["The Queen Mother of the West", "The Weaver Girl", "A child from the village"], "The little white snake was the Dragon King's daughter, so the king wanted to reward Hailebu."),
        ("What could the stone in his mouth do, and what was forbidden?", "It let him understand animals, but he could not tell anyone what he heard", ["It could turn stones into gold, and he could talk freely", "He had to tell everyone what he heard", "It let him understand only birds, with no other restriction"], "The Dragon King warned that if Hailebu revealed the secret, he would turn to stone."),
        ("What did Hailebu hear the animals say?", "A mountain would collapse, a flood would come, and the village would be submerged", ["The jade was in Qin", "The tide would not come until tomorrow", "The stone could be given away"], "The birds warned of a disaster. Hailebu urged the villagers to leave, but they did not believe him."),
        ("Why did Hailebu eventually turn to stone?", "He revealed the secret so that everyone would believe him", ["The stone exploded by itself", "He refused to leave the village", "The Dragon King punished him for hunting"], "He chose to turn to stone rather than leave the disaster unexplained. The villagers then left and remembered him."),
    ],
)

K(
    "g5a_niu", "Reading The Cowherd and the Weaver Girl", "Reading Comprehension", 5, "上", 3, "reasoning",
    "Understand how the Milky Way separates the Cowherd and the Weaver Girl and how magpies build a bridge for them to meet on the seventh day of the seventh lunar month. Parts 1 and 2 are one topic.",
    "yd_56",
    [
        ("What did the old ox do to help the Cowherd marry?", "It told him the Weaver Girl would descend from heaven and where to find her robe", ["It sent the Weaver Girl back to heaven", "It drew the Milky Way", "It taught him to shoot arrows"], "The talking ox told the Cowherd when the Weaver Girl would descend and how to find her robe."),
        ("How did the Queen Mother of the West separate the couple?", "She took the Weaver Girl back to heaven and drew the Milky Way with her hairpin", ["She made them keep living in the cowshed", "She sent magpies to fill in the Milky Way", "She turned the Cowherd to stone"], "The Milky Way separates them. The Cowherd follows wearing the ox's hide, but still cannot cross. Hailebu is the one who turns to stone."),
        ("On what day can they meet?", "The seventh day of the seventh lunar month", ["The first day of the first lunar month", "The eighteenth day of the eighth lunar month", "The Qingming Festival"], "Magpies form a bridge on the seventh day of the seventh lunar month so the couple can meet."),
        ("What type of story is this?", "A folktale", ["An informational text", "A classical Chinese essay", "A lab report"], "The Cowherd and the Weaver Girl is a folktale passed down orally. The Hunter and Hailebu is also a folktale, but their plots should not be mixed up."),
    ],
)

K(
    "g5a_xin", "Language Practice 3: Retelling a Story", "Writing Fundamentals", 5, "上", 3, "procedural",
    "A retelling uses familiar folktale characters in a new plot without reversing the original lesson or copying the text word for word. When telling a folktale aloud, make the time, place, and main events clear so listeners can follow.",
    "xz_56",
    [
        ("Which example is a retelling with a new plot?", "After Hailebu turns to stone, the villagers return each year and something new happens", ["Copy The Hunter and Hailebu from beginning to end", "Write a shopping list unrelated to Hailebu or the Cowherd", "Write only the four words retelling a story"], "The character is still Hailebu, but the event is new. Copying the original or changing to an unrelated subject is not a retelling."),
        ("When retelling The Cowherd and the Weaver Girl, which version reverses a character's nature?", "The Cowherd decides the Weaver Girl is too much trouble, sells the ox, and never sees her again", ["The magpie bridge breaks, but they find another way to meet", "The old ox's message helps them through another difficulty", "They refuse to forget each other across the Milky Way"], "A retelling can add new problems, but should not make the Cowherd abandon the Weaver Girl. That would change who he is in the story."),
        ("Which statement correctly distinguishes a retelling from copying?", "A retelling creates a new plot with familiar characters; copying reproduces the original text", ["A retelling must replace every character with a stranger", "A copy can freely change the ending and claim that was the author's meaning", "A retelling cannot use any original character names"], "Borrow familiar characters but create a new plot; do not make them suddenly act like different people."),
        ("What can you ask yourself when checking a retelling?", "Can readers identify the character without the name and see what new event happens?", ["How many commas are there?", "Can you delete the new events and keep only the original sentences?", "Does the character's behavior matter as long as the story is long enough?"], "Readers should recognize the character and see what has changed. If only the original sentences remain, it is still a copy."),
    ],
)

K(
    "g5a_shan", "Reading Club: Once Upon a Time, There Was a Mountain", "Reading Comprehension", 5, "上", 3, "conceptual",
    "This reading club focuses on Chinese folktales. They often begin with a traditional story opening and express hopes and feelings passed down orally, rather than recording scientific experiments.",
    "yd_56",
    [
        ("What type of books are suggested by the traditional opening Once upon a time, there was a mountain?", "Chinese folktales such as The Hunter and Hailebu and The Cowherd and the Weaver Girl", ["Only a copy of today's class schedule", "A blank notebook", "A manual containing only speed tables"], "That opening is commonly used in folktales. A blank notebook or manual is not part of this reading."),
        ("What is the main difference between these stories and What Is Faster Than a Cheetah?", "These are orally transmitted stories, not comparisons of speed", ["Both are only about memorizing poems", "Folktales cannot have characters", "Informational texts must describe magpies building a bridge"], "Cheetahs, rockets, and light are part of an explanation; Hailebu turning to stone and the Cowherd and Weaver Girl are folktales. Do not mix the genres."),
        ("After reading a folktale, what should you be able to describe?", "Who did what and what people in the story hoped for", ["Only how thick the book is", "Change the ending into a lab report and claim that was the author's meaning", "Only the cover color"], "Rescue, reunion, and justice express different hopes. Turning a folktale into an experiment changes its genre."),
        ("Which approach does not fit this reading club?", "Rewrite every folktale as a scientific law and claim that was what people in the past meant", ["Describe the characters and events after reading", "Write down a story that interests you", "Read more stories like The Hunter and Hailebu and The Cowherd and the Weaver Girl"], "Readers may ask their own questions, but should not replace a folktale with a conclusion from another subject."),
    ],
)

# The Chinese verse lines and quotations below are the assessed source text; surrounding prose is translated.
K(
    "g5a_shi", "Reading the poem To My Son", "Classical Chinese Poetry and Prose", 5, "上", 4, "conceptual",
    "Memorize Lu You's poem To My Son, including its lines about national reunification and addressing his father, without changing the wording.",
    "gs_56",
    [
        ("Which line follows 死去元知万事空?", "但悲不见九州同", ["王师北定中原日", "但悲不见九州空", "家祭无忘告乃翁"], "The poet grieves that he did not live to see the nation reunified. The other lines are not the next line."),
        ("Which line follows 王师北定中原日?", "家祭无忘告乃翁", ["死去元知万事空", "家祭无忘告乃父", "家祭勿忘告乃翁"], "He hopes that after the lost land is recovered, his family will tell his father at the ancestral rites. The poem says 乃翁, not 乃父."),
        ("Who wrote To My Son?", "Lu You", ["Lin Sheng", "Gong Zizhen", "Du Fu"], "Lu You wrote this poem to his son. Lin Sheng wrote Inscribed at an Inn in Lin'an."),
        ("What weighs most heavily on the poet's mind?", "That he did not live to see the nation reunified", ["There was not enough food for the family rites", "His son could not write poems", "The performances at Hangzhou"], "He can accept that everything else is gone, but not that he will miss the country's reunification. The Hangzhou performances appear in Inscribed at an Inn in Lin'an."),
    ],
)

K(
    "g5a_lin", "Reading Inscribed at an Inn in Lin'an", "Classical Chinese Poetry and Prose", 5, "上", 4, "conceptual",
    "Memorize Lin Sheng's poem Inscribed at an Inn in Lin'an, distinguish Hangzhou from Bianzhou, and do not mix its lines with To My Son.",
    "gs_56",
    [
        ("Which line follows 山外青山楼外楼?", "西湖歌舞几时休", ["暖风熏得游人醉", "直把杭州作汴州", "但悲不见九州同"], "The poet first asks when the performances at West Lake will end. The line about warm breezes is third; the line about the nine provinces is from To My Son."),
        ("Which line follows 暖风熏得游人醉?", "直把杭州作汴州", ["西湖歌舞几时休", "直把汴州作杭州", "直把杭州当汴州"], "The poet criticizes people for treating Hangzhou as if it were the former capital, Bianzhou. The order must not be reversed."),
        ("Who wrote Inscribed at an Inn in Lin'an?", "Lin Sheng", ["Lu You", "Gong Zizhen", "Li Bai"], "Lin Sheng wrote this poem. Lu You wrote To My Son; they are different poets."),
        ("What does 直把杭州作汴州 criticize?", "Forgetting the lost homeland and enjoying life in Hangzhou", ["The buildings in Hangzhou are not tall enough", "Bianzhou is better than Hangzhou for viewing West Lake", "Visitors cannot write poems"], "Bianzhou was a lost capital. Treating Hangzhou as Bianzhou means forgetting that the north had not been recovered."),
    ],
)

K(
    "g5a_gong", "Reading Miscellaneous Poems Written in the Year Jihai", "Classical Chinese Poetry and Prose", 5, "上", 4, "conceptual",
    "Memorize Gong Zizhen's poem beginning 九州生气恃风雷, including its images of silence and recruiting talent without rigid rules.",
    "gs_56",
    [
        ("Which line follows 九州生气恃风雷?", "万马齐喑究可哀", ["我劝天公重抖擞", "但悲不见九州同", "直把杭州作汴州"], "Without thunder and wind, everything is oppressively quiet. The line about the nine provinces is from To My Son; Hangzhou is from Inscribed at an Inn in Lin'an."),
        ("Which line follows 我劝天公重抖擞?", "不拘一格降人才", ["万马齐喑究可哀", "不拘一格降人材", "家祭无忘告乃翁"], "The poet hopes heaven will renew its energy and send talent without restricting it to one type. The poem uses 人才, not 人材."),
        ("Who wrote the poem beginning 九州生气恃风雷?", "Gong Zizhen", ["Lu You", "Lin Sheng", "Liang Qichao"], "Gong Zizhen wrote this poem. Lu You wrote To My Son, Lin Sheng wrote Inscribed at an Inn in Lin'an, and Liang Qichao wrote On Young China."),
        ("What does 万马齐喑 mean in the poem?", "Talent is suppressed and everything is silent", ["All the horses are literally mute and cannot pull carts", "The performances in Hangzhou are too noisy", "A battle is taking place at the Old Summer Palace"], "万马齐喑 is a metaphor for a stifling silence. The poet hopes talent will be welcomed without rigid restrictions."),
    ],
)

K(
    "g5a_shao", "Reading an Excerpt from On Young China", "Reading Comprehension", 5, "上", 4, "reasoning",
    "Understand the relationship between young people and the nation in Liang Qichao's On Young China, and identify its author correctly.",
    "yd_56",
    [
        ("Which line follows 少年智则国智?", "少年富则国富", ["少年强则国强", "少年独立则国独立", "少年自由则国自由"], "The original moves from wisdom to prosperity and then strength; strength follows prosperity."),
        ("Who wrote On Young China?", "Liang Qichao", ["Lu You", "Gong Zizhen", "Lin Sheng"], "This essay was written by Liang Qichao. Lu You, Gong Zizhen, and Lin Sheng wrote poems in this unit."),
        ("In whom does the author place China's future?", "Young people", ["Older people", "People from other countries", "People from the past"], "少年强则国强 emphasizes the role of the younger generation."),
        ("What does 少年强则国强 mean?", "When young people strive to achieve, the nation becomes strong", ["When the nation is strong, young people no longer need to study", "Only older people determine the nation's future", "Young people have no connection to their country"], "The line uses 则 to show that the condition of young people affects the nation."),
    ],
)

K(
    "g5a_yuan", "Reading The Destruction of the Old Summer Palace", "Reading Comprehension", 5, "上", 4, "reasoning",
    "Understand the layout and collections of the Old Summer Palace and why its destruction was an immeasurable loss.",
    "yd_56",
    [
        ("What kinds of buildings were in the Old Summer Palace?", "It had grand halls, countryside scenes, and Western-style views", ["Only one small hut", "Only Western buildings, with no Chinese architecture", "Only modern apartment buildings"], "The text describes a royal garden with scenes representing famous places as well as Western-style views."),
        ("What else did the garden contain?", "Precious historical artifacts and works of calligraphy and painting", ["Only ordinary bricks", "Hailebu's stone", "The He Shi Bi jade and thorn branches"], "The garden held valuable historical artifacts, gold, silver, and jewels. The stone and thorn branches belong to other stories."),
        ("Who destroyed the Old Summer Palace?", "The Anglo-French allied forces set it on fire", ["The garden workers demolished it themselves", "An earthquake collapsed it", "The army of Zhao"], "In 1860, the Anglo-French allied forces entered the palace, looted it, and then set it on fire."),
        ("Why does the author call this an immeasurable loss?", "It was a loss to both Chinese and world culture", ["Only a few trees were lost, so it did not matter", "The palace had no value", "The fire burned only one room"], "The text says at both the beginning and end that the destruction was an immeasurable loss to cultural history."),
    ],
)

K(
    "g5a_mei", "Reading Mei Lanfang Grows a Beard to Take a Stand", "Reading Comprehension", 5, "上", 4, "reasoning",
    "Understand how Peking opera artist Mei Lanfang grew a beard and refused to perform for the invaders during the war, even selling his house and pretending to be ill rather than taking the stage.",
    "yd_56",
    [
        ("What was Mei Lanfang's profession, and why did he usually not grow a beard?", "He was a Peking opera artist who played female roles; a beard would prevent him from playing a woman", ["He was a general of Zhao, and his beard was part of his armor", "He was a palace worker, and his beard got in the way of bricks", "He was the captain of the Normandy, and his beard could be used as a rope"], "Dan roles are female characters in opera. Growing a beard was a declaration that he would no longer perform."),
        ("Why did he grow a beard?", "To show his determination not to perform for the Japanese invaders", ["To make his beard longer than everyone else's", "The theater required him to grow one", "To put out the fire at the Old Summer Palace"], "After every excuse had been used, growing a beard became a silent protest."),
        ("How did he persist when he had no income?", "He sold his house to live on rather than perform", ["He immediately shaved and performed to earn money", "He sold the house to the invaders for a ticket", "He asked Lian Po to sing for him"], "He refused to perform even when theater owners offered favorable terms."),
        ("What did he do after the war ended?", "He shaved and returned to the stage", ["He kept his beard for the rest of his life and never performed again", "He went to Central Hebei to build tunnels", "He returned the He Shi Bi jade to Zhao"], "He grew the beard to refuse performances. After victory, he returned to his art."),
    ],
)

# The Han terms below are the assessed vocabulary items; surrounding text is translated.
K(
    "g5a_ci", "Language Practice 4: Inferring Word Meaning from Context", "Vocabulary", 5, "上", 4, "conceptual",
    "Use context to infer the meanings of key words. In the writing task My Hometown Twenty Years from Now, describe specific changes rather than simply saying that the hometown improved.",
    "cy_56",
    [
        ("What does 估量 mean in the phrase for an immeasurable loss?", "Estimate how great the loss is", ["Measure the garden's length", "Hide the artifacts", "Put out the fire"], "不可估量 means too great to estimate; it does not mean measuring with a ruler."),
        ("What does 众星拱月 describe in the text?", "Many smaller gardens surrounding the Old Summer Palace", ["Stars falling into a lake", "The moon being higher than the halls", "Visitors surrounding a tree"], "The locations of the Old Summer Palace and nearby gardens resemble stars surrounding the moon."),
        ("What is 玲珑剔透 suitable for describing?", "A delicate, airy building or work of art", ["A large fire", "A thick city wall", "A flat playground"], "玲珑剔透 describes something so finely made that light seems to pass through it. It does not describe a fire or a wall."),
        ("What is a good way to understand these words?", "Return to the passage and see what each word describes", ["Look only at the first character", "Replace the word with its opposite and call that the definition", "Ignore the sentence and choose the rarest dictionary meaning"], "不可估量 and 众星拱月 are difficult to understand without the passage about the Old Summer Palace."),
    ],
)

K(
    "g5a_tai", "Reading The Sun", "Reading Comprehension", 5, "上", 5, "reasoning",
    "Understand this informational text: the Sun is very far away and extremely hot, yet closely connected to human life. This unit has no language-practice section.",
    "yd_56",
    [
        ("Which features of the Sun does the text describe first?", "Its distance, size, and high temperature", ["Only that it can sing", "Only the scent of osmanthus", "Only the captain's duties"], "Far away, large, and hot describe the Sun itself; the text then explains its relationship with people."),
        ("What would happen to the weather and crops without the Sun?", "There would be no wind, clouds, rain, or snow, and crops could not grow", ["Crops would glow by themselves", "Rain would grow from underground", "Cheetahs would create the wind"], "Sunlight is connected to wind and rain, and crops need sunlight to grow."),
        ("How are energy sources such as coal and oil related to the Sun?", "Ancient plants stored the Sun's energy, and those plants later became these fuels", ["They are pieces that fell from the Sun", "They are artifacts from the Old Summer Palace", "They formed from Hailebu's stone"], "Plants grow using sunlight and can become these energy sources after being buried underground."),
        ("What is the text mainly explaining?", "The close relationship between the Sun and human life", ["The Sun is slower than a cheetah", "The Sun is a poem", "The Sun is Mei Lanfang's beard"], "The text covers the Sun's features and its relationship with people. Poems and growing a beard belong to other lessons."),
    ],
)

K(
    "g5a_jin", "Reading The Pyramids", "Reading Comprehension", 5, "上", 5, "reasoning",
    "Understand this informational text about the Egyptian pyramids: they were tombs for ancient pharaohs, were enormous, and were difficult to build.",
    "yd_56",
    [
        ("In which country are the pyramids, and what were they used for?", "They are in Egypt and served as tombs for ancient pharaohs", ["They are tunnels used in battles in Central Hebei", "They are towers in Hangzhou for viewing West Lake", "They are storehouses for the jade in Zhao"], "These triangular structures are tombs of ancient Egyptian kings. The tunnels, West Lake, and jade appear in other lessons."),
        ("What does the text emphasize about the pyramids?", "They are enormous, built from many giant stones, and still inspire awe", ["They can move by themselves", "They are pieces that fell from the Sun", "They are seven-character poems"], "Their scale and the difficulty of construction are the main points."),
        ("What should readers focus on in this text?", "The different aspects used to describe the structure", ["It asks readers to recite To My Son", "It gives a new ending to The Cowherd and the Weaver Girl", "It only teaches readers to shake osmanthus flowers"], "An informational text has an order and describes aspects such as appearance, use, and construction."),
        ("What do this text and The Sun have in common?", "Both are informational texts that describe a subject by its features", ["Both are folktales", "Both require readers to play a female opera role", "Both describe a captain sinking with a ship"], "One describes the Sun and the other the pyramids. Their methods are similar, but their subjects differ."),
    ],
)

K(
    "g5a_jie", "Writing: Introducing an Object", "Writing Fundamentals", 5, "上", 5, "application",
    "Introduce an object by describing it from several clear angles. The sample text The Whale covers size, species, food, and habits; Making a Wind Vane gives the materials and steps. Both are examples, not standalone lessons. This unit has no language-practice section.",
    "xz_56",
    [
        ("Which sentence explains that a whale is not a fish?", "A whale breathes with lungs and is a mammal, not a fish that breathes with gills", ["A whale is large.", "There are whales in the sea.", "Introduce an object."], "The sample The Whale describes breathing and classification. Saying only that it is large does not establish its features."),
        ("When writing about making a wind vane, which approach clearly explains the steps?", "List the materials, then explain in order how to cut, sew, and attach them", ["It is finished.", "A wind vane.", "It is fun."], "Making a Wind Vane is organized by steps. Without materials and sequence, another person could not make it."),
        ("Which approach is suitable for introducing an object?", "Choose several aspects and explain each clearly in turn", ["Use only one word in each sentence", "Describe an unobserved feature as if it were proven", "Switch among three unrelated objects in one paragraph"], "A clear set of aspects helps readers understand the object. Unsupported claims should not be presented as facts."),
        ("What role do The Whale and Making a Wind Vane play in this writing task?", "They are examples that teach how to introduce a subject, not separate texts to memorize", ["Both must be memorized as poems", "Both are myths unrelated to informational writing", "Each must be made into its own lesson topic"], "One introduces an animal and the other explains a process. They teach writing methods rather than forming standalone lessons."),
    ],
)

K(
    "g5a_mu", "Reading A Mother's Deep Love", "Reading Comprehension", 5, "上", 6, "reasoning",
    "Understand Liang Xiaosheng's story of a mother working in a noisy factory who still gives her child money to buy a book.",
    "yd_56",
    [
        ("Who wrote A Mother's Deep Love?", "Liang Xiaosheng", ["Wu Guanzhong", "Bing Xin", "Liu Yang"], "This is a memoir by Liang Xiaosheng. Wu Guanzhong wrote Father's Love in a Boat, and Bing Xin wrote Memories of Reading."),
        ("Why does the child ask the mother for money?", "To buy a book the child has wanted to read for a long time", ["To repair the Normandy", "To visit the pyramids in Egypt", "To buy a stone for Hailebu"], "The family is not well-off, but the child still asks for money to buy the book."),
        ("Where is the mother working at the time?", "In a very noisy factory workshop, doing difficult, tiring work", ["Reading in a quiet library", "Shaking flowers under an osmanthus tree", "Directing a shipwreck from the bridge"], "The factory setting shows how hard it is for her to earn money."),
        ("How does the child feel after the mother gives the money?", "Moved and close to tears", ["Angry that the amount is too small", "Throws the money away and never buys the book", "Immediately challenges Lian Po to a fight"], "The money was hard to earn, which makes the child feel moved, not angry or ready to fight."),
    ],
)

K(
    "g5a_fu", "Reading Father's Love in a Boat", "Reading Comprehension", 5, "上", 6, "reasoning",
    "Understand how Wu Guanzhong uses his uncle's small fishing boat to recall the money and nighttime journeys his father sacrificed for his education.",
    "yd_56",
    [
        ("Who wrote Father's Love in a Boat?", "Wu Guanzhong", ["Liang Xiaosheng", "Liu Yang", "Lao She"], "This is a memoir by Wu Guanzhong. Liang Xiaosheng wrote A Mother's Deep Love."),
        ("Whose small fishing boat appears in the text?", "The uncle's", ["The school's", "A large boat the father had just bought", "A classmate's"], "The family was poor and did not own a large boat. The father used his uncle's small boat to take the child to school and home."),
        ("What did the father buy for the child after selling cocoons?", "Loquats and a few eggs", ["A new schoolbag and a car", "A large boat", "A box of paints"], "He spent money he could hardly spare to buy loquats for the child. The eggs were for the journey."),
        ("Why is the small fishing boat called Father's Love in a Boat?", "It carries memories of the father's many trips and the money he saved for his child", ["The father built a warship by hand", "The father is a boatman, and the text only describes his job", "The boat was later given to the school"], "The boat, mending a quilt, and buying loquats all appear in memories connected with that boat."),
    ],
)

K(
    "g5a_hang", "Reading an Astronaut's Letter to Her Children", "Reading Comprehension", 5, "上", 6, "reasoning",
    "Understand astronaut Liu Yang's letter to her children before the Shenzhou 14 mission: she is both a mother and a soldier, and her children are both her armor and her vulnerability.",
    "yd_56",
    [
        ("Who wrote this letter, and to whom?", "Astronaut Liu Yang wrote it to her children", ["Halway wrote it to passengers", "Liang Qichao wrote it to young people", "Mei Lanfang wrote it to a theater"], "Before the Shenzhou 14 mission, she wrote the letter to her children in Jiuquan."),
        ("Why did she not let her children see her off at the launch site?", "Her children were both her strength and her vulnerability, and seeing them would make it harder to leave", ["Letters are not allowed at the launch site", "The children could not walk yet", "The letter was for a teacher, not her children"], "Armor represents strength, while a vulnerability is something one cares deeply about. She is both a mother and a soldier going on a mission."),
        ("What advice does the mother give her children in the letter?", "Have dreams, face difficulties, study, exercise, and care for family members", ["Sail a boat into a tunnel", "Put out the fire at the Old Summer Palace", "Grow a beard and perform opera"], "She cares about her family and hopes her children will grow up. Sailing, firefighting, and opera belong to other lessons."),
        ("What do this letter, A Mother's Deep Love, and Father's Love in a Boat all describe?", "Parents' love for their children, expressed in different ways", ["All three compare a cheetah's speed with light", "All three explain how the pyramids were built", "All three ask readers to memorize To My Son"], "One parent gives money for a book, another rows a boat to school, and another writes before a mission. The loving actions differ."),
    ],
)

K(
    "g5a_shuo", "Writing: What I Want to Tell You", "Writing Fundamentals", 5, "上", 6, "application",
    "Write to a parent or another older family member. Describe what you want to say and how you felt at the time. You may express thanks, apologize, or share something left unsaid; do not write only 'Thank you.'",
    "xz_56",
    [
        ("Which passage best fits What I Want to Tell You?", "Mom, that day in the factory when you slipped me the money, I still remember that the edge of the bill felt warm.", ["Thank you.", "What I want to tell you.", "Parents' love."], "Include both an event and how you felt. Saying only thank you or repeating the title does not tell the reader what you mean."),
        ("Which idea is off topic?", "Describe the height of the pyramids without mentioning yourself or the person you are writing to", ["Share something you have wanted to tell your father", "Explain why you wrongly blamed your mother", "Thank your father for mending a quilt"], "The topic is something you want to tell another person. Describing a landmark alone leaves that person out."),
        ("Which approach makes what you want to say more specific?", "Describe what happened and what you thought at the time", ["Use only the word you in every sentence", "Copy another student's essay and change the name", "Write only about the weather, not the person"], "Include both the event and your feelings. A form of address without a real event is still empty."),
        ("What can you ask yourself when reviewing this writing?", "Will the reader know which event I am talking about and how I felt?", ["Is the word count high enough?", "Can I avoid all forms of address?", "Can I turn it into an informational text comparing speeds?"], "Include both a person and an event. Without them, the title has no substance."),
    ],
)

# The Han characters below are the assessed written-form choices; only these glyphs remain untranslated.
K(
    "g5a_xing", "Language Practice 6: Similar-Looking Characters", "Character Recognition and Writing", 5, "上", 6, "conceptual",
    "Choose the characters 戴, 载, and 裁 by meaning rather than guessing from their components. In the speaking task on parental love, connect your ideas to this unit's texts instead of simply repeating that parents love you.",
    "sz_56",
    [
        ("Which character completes the phrase for putting on a hat?", "戴", ["载", "裁", "栽"], "Use 戴 for wearing something on the head. Use 载 for loading or recording, and 裁 for cutting."),
        ("Which character completes the word meaning to record?", "载", ["戴", "裁", "栽"], "Use 载 in the word meaning to record. Do not write 戴."),
        ("Which character completes the word meaning to cut fabric for clothing?", "裁", ["戴", "载", "栽"], "Use 裁 for cutting fabric; 栽 is used for planting."),
        ("Which pair of characters and meanings is correct?", "戴 means respect in 爱戴; 载 means load in 装载", ["载 means respect in 爱载; 戴 means load in 装戴", "裁 means respect in 爱裁; 裁 means load in 装裁", "戴 means respect in 爱戴; 裁 means load in 装裁"], "Use 戴 in 爱戴 for respect and 载 in 装载 for loading. The other combinations are incorrect."),
    ],
)

# The Chinese verse lines below are the assessed source text; surrounding prose is translated.
K(
    "g5a_qiu", "Reading the poem Autumn Evening in the Mountains", "Classical Chinese Poetry and Prose", 5, "上", 7, "conceptual",
    "Memorize Wang Wei's poem Autumn Evening in the Mountains, including its empty mountain, clear spring, and washerwomen, without mixing it with lines from the poem about a night mooring.",
    "gs_56",
    [
        ("Which line follows 空山新雨后?", "天气晚来秋", ["明月松间照", "清泉石上流", "夜半钟声到客船"], "Rain has just fallen on the empty mountain, and evening brings autumn. The line about moonlight among pines comes third; the line about a boat is from Night Mooring at Maple Bridge."),
        ("Which line follows 明月松间照?", "清泉石上流", ["竹喧归浣女", "明月松间照水", "江枫渔火对愁眠"], "The moon shines among the pines, and the spring flows over the stones. The washerwomen appear in the next couplet; the fishing lights are from Night Mooring at Maple Bridge."),
        ("Which line follows 竹喧归浣女?", "莲动下渔舟", ["清泉石上流", "莲动下渔船", "夜半钟声到客船"], "The bamboo rustles as the washerwomen return; the lotus leaves move as a fishing boat passes. The poem says 渔舟, not 渔船."),
        ("Who wrote Autumn Evening in the Mountains?", "Wang Wei", ["Zhang Ji", "Han Yu", "Lu You"], "Wang Wei wrote this landscape poem. Zhang Ji wrote Night Mooring at Maple Bridge, and Han Yu wrote Early Spring, Presented to Assistant Zhang of the Ministry of Water."),
    ],
)

K(
    "g5a_feng", "Reading Night Mooring at Maple Bridge", "Classical Chinese Poetry and Prose", 5, "上", 7, "conceptual",
    "Memorize Zhang Ji's poem Night Mooring at Maple Bridge, including its fishing lights, midnight, and passenger boat, without changing the wording.",
    "gs_56",
    [
        ("Which line follows 月落乌啼霜满天?", "江枫渔火对愁眠", ["姑苏城外寒山寺", "江枫鱼火对愁眠", "月落乌啼霜满地"], "The speaker lies awake with the fishing lights before him. 鱼火 is an incorrect character; the line about Hanshan Temple is third."),
        ("Which line follows 姑苏城外寒山寺?", "夜半钟声到客船", ["江枫渔火对愁眠", "夜半钟声到客舟", "半夜钟声到客船"], "The midnight bell reaches the passenger boat. The poem uses 夜半, not 半夜, and 客船, not 客舟."),
        ("Who wrote Night Mooring at Maple Bridge?", "Zhang Ji", ["Wang Wei", "Han Yu", "Lu You"], "Zhang Ji wrote this poem. Wang Wei wrote Autumn Evening in the Mountains; do not confuse them because both describe nighttime."),
        ("Why is the poet unable to sleep?", "He is troubled by homesickness and hears the bell from Hanshan Temple", ["He is fishing from the boat", "The bell rings only in the morning, so he has woken up", "Frost covers the sky, so he is running on the shore"], "The line about facing the fishing lights describes a traveler's sorrow. The midnight bell emphasizes that he cannot sleep."),
    ],
)

K(
    "g5a_zao", "Reading Early Spring, Presented to Assistant Zhang", "Classical Chinese Poetry and Prose", 5, "上", 7, "conceptual",
    "Memorize Han Yu's poem about early spring, including its images of fine rain and grass that seems to disappear when approached. Do not mix it with the autumn or night-mooring poems.",
    "gs_56",
    [
        ("Which line follows 天街小雨润如酥?", "草色遥看近却无", ["最是一年春好处", "草色遥看近还无", "空山新雨后"], "From far away, the grass looks green; up close, it is barely visible. 空山新雨后 is from Autumn Evening in the Mountains."),
        ("Which line follows 最是一年春好处?", "绝胜烟柳满皇都", ["草色遥看近却无", "绝胜烟柳满皇城", "夜半钟声到客船"], "The early days of spring are better than the later season when willows fill the capital. The poem says 皇都, not 皇城."),
        ("Who wrote this poem?", "Han Yu", ["Wang Wei", "Zhang Ji", "Gong Zizhen"], "Han Yu wrote the poem for Assistant Zhang of the Ministry of Water. Wang Wei and Zhang Ji wrote the other two poems in this lesson."),
        ("What season's grass is described by 草色遥看近却无?", "Early spring, when it has just appeared and is hard to see up close", ["Late autumn, when the grass has all turned yellow", "Frost on a boat at night", "Performances beside West Lake"], "Grass looks like this in early spring. Late autumn, frost, and performances are not part of this poem."),
    ],
)

K(
    "g5a_xue", "Reading The First Snow", "Reading Comprehension", 5, "上", 7, "reasoning",
    "Understand Jun Qing's description of heavy snow in Jiaodong: the snowfall is dynamic, the snow-covered scene is still, and the snow benefits the wheat.",
    "yd_56",
    [
        ("Who wrote The First Snow, and where does it take place?", "Jun Qing; the Jiaodong region", ["Guo Moruo; a story about an egret", "Wang Wei; autumn rain in the mountains", "Zhang Ji; nighttime at Maple Bridge"], "This essay was written by Jun Qing. The egret, autumn evening, and night mooring appear in other lessons."),
        ("What does the author mainly describe while it is snowing?", "Heavy snow in motion, with sounds and actions", ["The snow has stopped and the roads are completely cleared", "An egret standing motionless in the snow", "Han Yu counting grass in the street"], "The swirling snow describes an ongoing snowfall."),
        ("What does the author mainly describe after the snow stops?", "A white, quiet landscape at rest", ["Snow still pelting a boat", "A captain sinking with a ship", "Machines in a workshop"], "The landscape looks covered in white and is so quiet that small sounds can be heard. Distinguish movement from stillness."),
        ("Why does the author say this snow is good?", "Snow benefits the wheat and brings hope for a good harvest", ["It can rebuild the Old Summer Palace", "It travels faster than light", "It is Hailebu transformed"], "The idea is that auspicious snow promises a good harvest. Rebuilding the palace, comparing speed, and turning to stone belong to other lessons."),
    ],
)

K(
    "g5a_bai", "Reading The Egret", "Reading Comprehension", 5, "上", 7, "reasoning",
    "Understand Guo Moruo's description of the egret: its coloring and shape are perfectly balanced, making the bird itself seem like a poem.",
    "yd_56",
    [
        ("Who wrote The Egret?", "Guo Moruo", ["Jun Qing", "Xu Dishan", "Wang Wei"], "The Egret was written by Guo Moruo. Jun Qing wrote The First Snow, and Xu Dishan wrote Peanuts."),
        ("Why does the author say the egret's body is just the right size?", "Adding a little would make it too long; taking a little away would make it too short", ["It is the largest bird", "It cannot fly", "Its color changes every day"], "The author considers its coloring and proportions perfectly balanced."),
        ("Why are cranes, spoonbills, and herons mentioned in the text?", "To compare them with the egret and highlight its elegance", ["To show that they are the same species as egrets", "To show that egrets cannot stand in water", "To replace the egret in the title"], "The crane seems stiff, while the spoonbill and heron seem too large. The comparison highlights the egret's balance."),
        ("What does the idea that the egret itself is a poem mean?", "Its colors, outline, and movements are beautiful", ["The egret can recite poems", "The egret cannot fly and can only write", "No egret appears in the poem"], "The author says it does not sing, yet its whole form resembles a delicate poem."),
    ],
)

# The Chinese phrases below are the specific redundancy and word-choice targets; surrounding prose is translated.
K(
    "g5a_bing", "Language Practice 7: Editing Sentences", "Sentence Structure", 5, "上", 7, "procedural",
    "Identify incorrect word pairings and redundancy, and choose corrected sentences. In the writing task My Favorite Season, describe the season's scenery and your feelings rather than only saying that you like spring.",
    "jz_56",
    [
        ("Which sentence has no error?", "A bird sings in a tree.", ["I spent 大概 half an hour 左右.", "He put on a hat and a backpack.", "I could not help but couldn't resist laughing."], "大概 and 左右 are redundant; a backpack is not worn on the head; 忍不住 and 不禁 repeat the same idea."),
        ("In a sentence meaning that someone is about twelve years old, 大约 and 左右 are both used. Which edit is correct?", "Keep either 大约 or 左右, but not both", ["Keep 大约 and 左右 together", "Move 左右 before 大约 and keep both", "Use both 大约 and 左右 at the beginning"], "Keep either 大约 or 左右. Using both is redundant."),
        ("In a sentence meaning that someone put on clothes, a hat, and a backpack, which Chinese verb is misused?", "穿", ["Clothing cannot be worn", "The sentence is too short", "The weather is not mentioned"], "穿 is used for clothes; 戴 is used for a hat, and 背 is used for a backpack."),
        ("Which sentence removes the repeated expressions for laughing?", "After hearing the story, I could not help laughing.", ["After hearing the story, I could not help but couldn't resist laughing.", "After hearing the story, I spent about a while or so laughing.", "After hearing it, I couldn't help but couldn't resist laughing."], "忍不住 already means unable to stop oneself, so 不禁 is unnecessary."),
    ],
)

# The quoted Chinese sayings below are the assessed source text; explanatory prose is translated.
K(
    "g5a_gu", "Reading What the Ancients Said About Reading", "Reading Comprehension", 5, "上", 8, "reasoning",
    "Understand three short texts: a saying from the Analects, Zhu Xi's three kinds of attention, and Zeng Guofan's three qualities for study.",
    "yd_wenyan",
    [
        ("In which book does 敏而好学，不耻下问 appear, and what does it mean?", "The Analects; be eager to learn and not ashamed to ask questions", ["Zhu Xi's three kinds of attention; only ask a teacher", "Zeng Guofan's letters; having a goal means there is no need to ask", "To My Son; only ask one's child"], "This is the first passage, from the Analects. 下问 means asking someone who knows less."),
        ("What are Zhu Xi's 三到, and which one matters most?", "心到、眼到、口到; 心到 matters most", ["手到、脚到、口到; 脚到 matters most", "有志、有识、有恒; 有恒 matters most", "智、富、强; 富 matters most"], "Without attention of the mind, moving the eyes and mouth is not enough to remember. 有志、有识、有恒 comes from Zeng Guofan."),
        ("Which three qualities did Zeng Guofan say a reader needs?", "有志、有识、有恒; none can be missing", ["Having a goal is enough; knowledge and perseverance are optional", "Only being able to recite Night Mooring at Maple Bridge", "Only growing a beard"], "志 means having an aim, 识 means understanding, and 恒 means perseverance. All three are needed."),
        ("What does 知之为知之，不知为不知 mean?", "Say that you know when you know, and that you do not know when you do not; that is wisdom", ["Pretend to know even when you do not", "Never say when you know something", "Only teachers are allowed not to know"], "This saying comes from the Analects. Pretending to know is not wisdom."),
    ],
)

# The quoted Chinese summary below is the assessed wording from the source text.
K(
    "g5a_yi", "Reading Memories of Reading", "Reading Comprehension", 5, "上", 8, "reasoning",
    "Understand Bing Xin's recollections of reading from childhood: reading is good, read more, and read good books.",
    "yd_56",
    [
        ("Who wrote Memories of Reading?", "Bing Xin", ["Zhu Xi", "Zeng Guofan", "Joan Aiken"], "Bing Xin wrote about her own reading experiences. Zhu Xi and Zeng Guofan appear in What the Ancients Said About Reading."),
        ("When she first read Romance of the Three Kingdoms as a child, how did her experience change?", "At first she did not understand much, but later the book became more enjoyable", ["She could recite the whole book immediately", "She never read another book afterward", "She looked only at the cover"], "She skipped parts she did not understand and gradually became absorbed in the book."),
        ("Which three phrases summarize her reading experience?", "读书好，多读书，读好书", ["Pay attention with the mind, eyes, and mouth", "Have an aim, understanding, and perseverance", "When young people are wise, the nation is wise"], "These three phrases express Bing Xin's own experience. The three kinds of attention are Zhu Xi's, and the three qualities are Zeng Guofan's."),
        ("How is this text different from What the Ancients Said About Reading?", "This text recalls one person's reading experience; the other presents advice from the ancients", ["Both are poems by Han Yu", "Both only describe the pyramids", "Both require readers to grow a beard"], "One is a memoir, while the other presents principles in classical writing. They are different works."),
    ],
)

K(
    "g5a_zou", "Reading A Book Is a Traveler's Companion", "Reading Comprehension", 5, "上", 8, "reasoning",
    "Understand Joan Aiken's idea: if she could take only one thing to a deserted island, she would take a book, which can be reread like a friend who never grows tiresome.",
    "yd_56",
    [
        ("Who wrote A Book Is a Traveler's Companion?", "Joan Aiken", ["Bing Xin", "Zhu Xi", "Liang Xiaosheng"], "This text was written by Joan Aiken. Bing Xin wrote Memories of Reading."),
        ("If the author went to a deserted island, what would she most want to take?", "A book", ["A cheetah", "A pyramid", "The Normandy"], "The title treats a book as a companion."),
        ("Why can a book be a companion?", "It can be reread, and each reading can reveal something new", ["It must be thrown away after one reading", "It can only be used as a pillow", "It runs faster than light"], "A new perspective or image can make the same book feel fresh again."),
        ("What is the main idea of the text?", "A book is a companion for a journey and is worth rereading", ["Only classical texts count as books", "Once you have read many books, you should stop reading", "No words can exist on a deserted island"], "A book can travel with you anywhere; reading it once does not have to be the end."),
    ],
)

K(
    "g5a_tui", "Language Practice 8: Recommending a Book", "Writing Fundamentals", 5, "上", 8, "procedural",
    "When recommending a book, give its title, summarize it, mention what moved you most, and explain why it is worth reading. Do not only say that it is good.",
    "xz_56",
    [
        ("Which passage sounds like a book recommendation?", "Memories of Reading describes Bing Xin's childhood reading and may inspire readers to find a book they truly enjoy", ["This book is good.", "Recommend a book.", "Book."], "Include the title and some content or a reason. Saying only that it is good does not tell readers which book or why."),
        ("What is a suitable approach to recommending a book?", "Use one or two events from the book to explain what makes it good", ["Copy the entire book from beginning to end", "Omit the title and only say to read it", "Turn the review into a shopping list"], "Give specific details without copying the whole book. A recommendation without a title is incomplete."),
        ("Which idea does not fit this writing task?", "Write only about how much snow fell, without naming any book", ["Describe the scene you remember most from The Hunter and Hailebu", "Explain why A Book Is a Traveler's Companion made you want to read it again", "Say that a classmate enjoyed the book after you lent it to them"], "The task is to recommend a book. A description of snow alone leaves out the book."),
        ("What can you ask yourself when checking this writing?", "Will readers know which book I recommend and why it is worth reading?", ["Is the word count high enough?", "Can I avoid naming the book?", "Can I turn it into a math problem?"], "Include the book's title and reasons. Without a book and a reason, it is not a recommendation."),
    ],
)

# ---------- Grade 5, spring ----------
# Follow the current/commonly used 2026 spring national textbook sequence (six-three system).
# Split each of the three poems in Units 1 and 4 into separate topics.
# Unit 3 is the integrated Chinese-character study "Exploring the Kingdom of Chinese Characters"; it has no language-practice section.
# Unit 5 has no language-practice section; list the writing task "Describe a Person's Distinctive Traits" separately.
# Do not create standalone topics for the sample texts My Friend Rongrong and The Young Goalkeeper and His Spectators.
# Unit 7's Pyramid topics cover Evening Glow over the Pyramids and The Incomprehensible Pyramids; keep them separate from the informational text in fall.
# List the reading club "Read Classical Masterpieces, Savor a Hundred Lives" separately.
# Include speaking tasks in their related language-practice sections or writing tasks; exclude the out-of-sequence poem Song of the Wandering Son.

# The Chinese poem lines below are the assessed source text; surrounding prose is translated.
K(
    "g5b_za", "Reading the poem Four Seasons: Pastoral Scenes, No. 31", "Classical Chinese Poetry and Prose", 5, "下", 1, "conceptual",
    "Review Fan Chengda's poem Four Seasons: Pastoral Scenes, No. 31. Remember its lines about daytime fieldwork, nighttime weaving, and learning to plant melons; do not mix it with the poems about children playing with ice or a village at dusk. The poem was already taught in Grade 4, spring.",
    "gs_56",
    [
        ("In Grade 5, spring, which of the three poems is Fan Chengda's Four Seasons: Pastoral Scenes, No. 31?", "昼出耘田夜绩麻", ["稚子金盆脱晓冰", "草满池塘水满陂", "篱落疏疏一径深"], "No. 31 begins with 昼出耘田. The line about melting ice is from Children Playing with Ice, the pond is from Village at Dusk, and the hedge is from Lodging at Xinshi."),
        ("Which line follows 昼出耘田夜绩麻?", "村庄儿女各当家", ["也傍桑阴学种瓜", "童孙未解供耕织", "彩丝穿取当银钲"], "After the day's fieldwork and nighttime weaving, the poem describes each family member's work. The line about planting melons is fourth; the silver gong is from Children Playing with Ice."),
        ("Which line does not belong to Four Seasons: Pastoral Scenes, No. 31?", "短笛无腔信口吹", ["昼出耘田夜绩麻", "童孙未解供耕织", "也傍桑阴学种瓜"], "短笛无腔信口吹 is from Village at Dusk. The lines about fieldwork, weaving, and planting melons belong to No. 31."),
        ("What does 童孙未解供耕织，也傍桑阴学种瓜 describe?", "A child who does not yet know farming or weaving but learns to plant melons in the shade of a mulberry tree", ["A child turning ice into a silver gong", "A shepherd boy playing a flute on an ox", "A child chasing a yellow butterfly into a field of flowers"], "The child is learning to plant melons. Playing with ice, flute music, and chasing butterflies are from other poems."),
    ],
)

K(
    "g5b_zhi", "Reading Children Playing with Ice", "Classical Chinese Poetry and Prose", 5, "下", 1, "conceptual",
    "Memorize Yang Wanli's poem Children Playing with Ice. Remember the silver gong and glass, not a silver bell or colored glaze, and do not mix it with lines about fieldwork or a village at dusk.",
    "gs_56",
    [
        ("Which line follows 稚子金盆脱晓冰?", "彩丝穿取当银钲", ["敲成玉磬穿林响", "彩丝穿取当银钟", "忽作玻璃碎地声"], "The child threads a string through the ice and uses it as a silver gong. The poem does not say silver bell."),
        ("Which line follows 敲成玉磬穿林响?", "忽作玻璃碎地声", ["彩丝穿取当银钲", "忽作琉璃碎地声", "忽作玻璃碎地响"], "The ice suddenly breaks with a sound like shattering glass. The poem says 玻璃, not 琉璃."),
        ("Who wrote Children Playing with Ice?", "Yang Wanli", ["Lei Zhen", "Fan Chengda", "Lu You"], "Yang Wanli wrote this poem. Lei Zhen wrote Village at Dusk, and Fan Chengda wrote Four Seasons: Pastoral Scenes, No. 31."),
        ("What happens to the ice at the end of Children Playing with Ice?", "It breaks", ["It remains as a silver gong", "It is put into a box", "It turns into a jade chime"], "The line about glass shattering describes the ice suddenly breaking."),
    ],
)

K(
    "g5b_cun", "Reading Village at Dusk", "Classical Chinese Poetry and Prose", 5, "下", 1, "conceptual",
    "Memorize Lei Zhen's poem Village at Dusk, including the lines about lying across an ox and casually playing a flute. Do not mix it with the poems about ice or fieldwork.",
    "gs_56",
    [
        ("Which line follows 草满池塘水满陂?", "山衔落日浸寒漪", ["牧童归去横牛背", "短笛无腔信口吹", "山衔落日浸寒波"], "The setting sun sinks into the cold ripples as if held by the mountain. The shepherd boy appears in the third line. The poem says 寒漪."),
        ("Which line follows 牧童归去横牛背?", "短笛无腔信口吹", ["草满池塘水满陂", "短笛无腔信口哼", "牧童归去骑牛背"], "The shepherd boy lies across the ox and casually plays a short flute. The poem says 横, not 骑, and 吹, not 哼."),
        ("Who wrote Village at Dusk?", "Lei Zhen", ["Yang Wanli", "Fan Chengda", "Wang Wei"], "Lei Zhen wrote Village at Dusk. Yang Wanli wrote Children Playing with Ice, and Fan Chengda wrote Four Seasons: Pastoral Scenes, No. 31."),
        ("Which line does not belong to Village at Dusk?", "彩丝穿取当银钲", ["草满池塘水满陂", "山衔落日浸寒漪", "短笛无腔信口吹"], "彩丝穿取当银钲 is from Children Playing with Ice."),
    ],
)

K(
    "g5b_zu", "Reading Grandfather's Garden", "Reading Comprehension", 5, "下", 1, "reasoning",
    "Understand how Xiao Hong describes the squash, butterflies, and narrator as free in her grandfather's garden.",
    "yd_56",
    [
        ("Which book contains Grandfather's Garden?", "Tales of Hulan River", ["Romance of the Three Kingdoms", "Water Margin", "Dawn Blossoms Plucked at Dusk"], "This chapter is from Xiao Hong's Tales of Hulan River, not a classical novel."),
        ("What are the squash and cucumbers like in the garden?", "They can climb onto a trellis if they want; everything is free", ["Grandfather pulls them all out", "They can only grow in pots", "None of them can bear fruit"], "The author describes the plants as growing however they like; the bees and butterflies are free too."),
        ("What foolish thing does the narrator do while working with Grandfather?", "She leaves foxtail grass, mistaking it for grain", ["She sells the garden", "She locks Grandfather outside", "She does not touch anything all day"], "Grandfather weeds, and the narrator weeds too, but mistakes foxtail grass for grain. Grandfather does not scold her."),
        ("What is the strongest feeling in this text?", "Freedom and happiness", ["Nervously preparing for an exam", "The garden being swept away in a flood", "Grandfather forbidding the narrator to enter"], "Napping in the sun, playing, and following along with the weeding all show carefree happiness."),
    ],
)

# The quoted Chinese phrase below is the assessed source wording.
K(
    "g5b_yue", "Reading The Moon Is Brightest at Home", "Reading Comprehension", 5, "下", 1, "reasoning",
    "Understand how Ji Xianlin uses the moon to express homesickness: no matter how large the moon elsewhere is, the small moon at home feels closer. The title comes from a Du Fu line.",
    "yd_56",
    [
        ("Who wrote The Moon Is Brightest at Home?", "Ji Xianlin", ["Xiao Hong", "Chen Huiying", "Du Fu"], "This essay was written by Ji Xianlin. Du Fu wrote the line 月是故乡明, but he did not write this essay."),
        ("Whose poem does the title phrase 月是故乡明 come from?", "Du Fu", ["A new poem by Ji Xianlin", "Yang Wanli", "Lei Zhen"], "Du Fu's poem Remembering My Brothers on a Moonlit Night includes the line 月是故乡明. The essay uses it to express homesickness."),
        ("Why does the author remember the moon at home after seeing moons in many places?", "The moon at home is connected to childhood and feels closest to him", ["The moon at home is larger than the Sun", "He has never left his hometown", "There is no moon anywhere else"], "Even after seeing large moons elsewhere, he feels they cannot compare with the small moon at home."),
        ("How is this text different from Grandfather's Garden?", "This text uses the moon to express homesickness; the other describes carefree childhood play in a garden", ["Both are about the same garden written by Xiao Hong", "Both describe only plum blossoms", "Both are seven-character poems"], "One is about homesickness and the moon; the other is about a childhood garden. They are different works."),
    ],
)

K(
    "g5b_hun", "Reading The Spirit of the Plum Blossom", "Reading Comprehension", 5, "下", 1, "reasoning",
    "Understand Chen Huiying's portrait of her grandfather: although he lives overseas, his heart is with China, and he sees the plum blossom as a symbol of national character.",
    "yd_56",
    [
        ("Who wrote The Spirit of the Plum Blossom?", "Chen Huiying", ["Ji Xianlin", "Xiao Hong", "Feng Jicai"], "Chen Huiying wrote this story about her grandfather. Ji Xianlin wrote about the moon, and Xiao Hong wrote about a garden."),
        ("Why does the grandfather value plum blossoms so highly?", "They bloom with greater spirit in the cold, like the character of the Chinese people", ["They are the best-tasting flowers", "They can borrow one hundred thousand arrows", "They grow only abroad and have no connection to him"], "The flowers bloom with more spirit under wind and snow. He values this strength, not their taste."),
        ("What does the grandfather give his granddaughter when she returns to China?", "A cherished ink painting of plum blossoms, to remind her of the flowers and that she is Chinese", ["He tells her to sell the painting", "He tells her to give it to Zhou Yu", "He tells her to throw it into the sea"], "The painting is precious to him. Giving it to her passes this spirit to the next generation."),
        ("Where does the grandfather's heart remain?", "He lives overseas, but his heart is with China", ["He follows the child back to Grandfather's Garden", "He goes to fight a tiger at Jingyang Ridge", "He is a gondolier in Venice"], "Living in another country, he cries when he reads poems about home. The plum blossom's spirit represents China in his heart."),
    ],
)

K(
    "g5b_zhang", "Writing: The Moment I Grew Up", "Writing Fundamentals", 5, "下", 1, "application",
    "Describe a moment when you suddenly felt grown up. Make the place, actions, and change in your feelings clear. For the speaking task about an older person's childhood, ask specific questions and listen without interrupting.",
    "xz_56",
    [
        ("Which passage best fits The Moment I Grew Up?", "The day Grandma had a fever, I made porridge and brought it to her. After she took a bite, I felt I was no longer only someone being cared for.", ["I grew up.", "The words that moment.", "Childhood is wonderful."], "Describe both the event and the change in your feelings. Simply saying that you grew up does not let readers see it."),
        ("Which idea does not fit this writing task?", "Writing only about Fan Chengda's fieldwork without describing a moment from your own life", ["Describe the first time you pulled your younger sibling away from the road", "Admit that you broke a cup instead of blaming someone else", "Leave a light on for your father when he comes home late"], "The topic is a moment when you grew up. A description of an ancient poet farming leaves out your own experience."),
        ("Which sentence describes a moment in detail?", "I held the payment slip, stood at the counter twice, and handed over the money on my third try.", ["I became brave.", "That moment, I grew up.", "The word counter."], "Standing twice and handing it over on the third try lets readers see the process. Simply saying brave is a conclusion."),
        ("Which question would be useful when asking an older person about childhood?", "What is one childhood event you remember best, and who was there?", ["Was your childhood good?", "Please recite a poem.", "How do you write the word childhood?"], "Ask about a specific event and people. A broad question about whether it was good can be difficult to answer."),
    ],
)

# The Han characters below are the assessed pronunciation targets; only these glyphs remain untranslated.
K(
    "g5b_cuo", "Language Practice 1: Commonly Misread Characters", "Character Recognition and Writing", 5, "下", 1, "conceptual",
    "Pronounce 削, 骨, 血, and 处 correctly in different words instead of guessing from a component.",
    "sz_56",
    [
        ("How is 削 pronounced in the word for sharpening a pencil?", "xiāo", ["xuē", "xiào", "qiāo"], "In words for peeling fruit or sharpening a pencil, it is pronounced xiāo; in exploitation, it is xuē."),
        ("How is 骨 pronounced in the word for a flower bud?", "gū", ["gǔ", "gú", "hú"], "In the word for a flower bud, it is pronounced gū; in bone or backbone, it is gǔ."),
        ("How is 血 commonly pronounced in casual speech when saying that someone is bleeding?", "xiě", ["xuè", "xuě", "xiè"], "In casual speech about bleeding, it is often xiě; in blood or blood vessels, it is xuè."),
        ("How is 处 pronounced in the word meaning to handle or deal with?", "chǔ", ["chù", "cù", "chú"], "In words meaning to handle or punish, it is pronounced chǔ; in everywhere or place, it is chù."),
    ],
)

K(
    "g5b_cao", "Reading Borrowing Arrows with Straw Boats", "Reading Comprehension", 5, "下", 2, "reasoning",
    "Understand how Zhuge Liang makes a military pledge to Zhou Yu and uses straw boats to obtain arrows from Cao Cao. The story is from Romance of the Three Kingdoms.",
    "yd_56",
    [
        ("To whom did Zhuge Liang make the military pledge?", "Zhou Yu", ["Cao Cao", "Lu Su", "Liu Bei"], "Zhou Yu challenged him to make arrows, so Zhuge Liang made the pledge to Zhou Yu."),
        ("How did Zhuge Liang 'borrow' the arrows?", "He used straw boats in heavy fog to make Cao Cao's army fire arrows at them", ["Lu Su gave him the arrows", "Zhou Yu delivered one hundred thousand arrows", "The soldiers made them overnight"], "The boats were covered with straw bundles. Cao Cao did not dare to send out troops, so he ordered archers to shoot toward the river."),
        ("What did Lu Su do in this plan?", "Prepared the boats and straw bundles as Zhuge Liang asked and kept the plan secret", ["Told Zhou Yu the plan", "Went to Cao Cao's camp to take the arrows", "Opposed the military pledge"], "Lu Su helped with the preparations and did not reveal the plan to Zhou Yu."),
        ("Why did Zhuge Liang order the boats to turn around on the return trip?", "So the straw bundles on the other side could also collect arrows", ["To chase Cao Cao", "The arrows had already fallen into the water", "Zhou Yu told him to return immediately"], "After one side filled up, turning the boats let the other side collect more arrows."),
    ],
)

K(
    "g5b_gang", "Reading Jingyang Ridge", "Reading Comprehension", 5, "下", 2, "reasoning",
    "Understand how Wu Song ignores the warning about crossing Jingyang Ridge after three bowls, crosses anyway, and kills a tiger. The story is from Water Margin.",
    "yd_56",
    [
        ("What warning is written on the inn's sign?", "No crossing the ridge after three bowls", ["There are no tigers on the ridge", "Do not pay for the wine", "Jingyang Ridge is closed"], "The innkeeper says not to cross after three bowls because there is a tiger on the ridge."),
        ("What does Wu Song do after hearing that there is a tiger?", "He does not believe it and continues across the ridge", ["He stays at the inn immediately", "He asks the innkeeper to take him across", "He takes another route"], "He thinks the innkeeper is trying to keep customers there and does not believe the tiger is real."),
        ("What happens to the tiger on the ridge?", "Wu Song kills it", ["It injures Wu Song and runs away", "It falls into a pit by itself", "A hunter kills it earlier"], "After his staff breaks, Wu Song holds the tiger down and eventually kills it."),
        ("What quality of Wu Song does the story emphasize?", "Bravery", ["Timidity", "He can drink but cannot act", "He follows every warning from the innkeeper"], "Crossing the ridge and fighting the tiger show his bravery. He did not follow the innkeeper's advice to stay."),
    ],
)

K(
    "g5b_hou", "Reading The Monkey King Is Born", "Reading Comprehension", 5, "下", 2, "reasoning",
    "Understand how the stone monkey emerges from a magical rock, jumps through a waterfall, and discovers the Water-Curtain Cave. The story is from Journey to the West.",
    "yd_56",
    [
        ("Where does the stone monkey come from?", "A magical rock splits open", ["A peach", "A seashell", "A fairy shapes it by hand"], "The magical rock splits, produces a stone egg, and the egg becomes the stone monkey."),
        ("How does the monkey discover the Water-Curtain Cave?", "It jumps through the waterfall", ["It walks into a cave along a mountain path", "Another monkey tells it about the cave", "It falls into the cave from the sky"], "The monkey is the first to jump through the waterfall and see the cave inside."),
        ("Why do the other monkeys later accept it as their king?", "It dares to jump through the waterfall first and invites the others inside", ["It drives all the other monkeys away", "It brings a royal seal from heaven", "The waterfall appoints it king"], "It explores the cave and says that whoever can enter may be king, so the others accept it."),
        ("What does the Water-Curtain Cave look like from the outside?", "A waterfall", ["A wooden door", "A stone bridge", "A peach tree"], "The waterfall covers the cave entrance and looks like a curtain of water."),
    ],
)

K(
    "g5b_hong", "Reading Spring Fun in the Red Chamber", "Reading Comprehension", 5, "下", 2, "reasoning",
    "Understand the kite-flying scene from A Dream of Red Mansions: Baoyu, Daiyu, and others fly kites in the garden. It is not the same story as borrowing arrows, fighting a tiger, or the birth of the stone monkey.",
    "yd_56",
    [
        ("Which book contains Spring Fun in the Red Chamber?", "A Dream of Red Mansions", ["Romance of the Three Kingdoms", "Water Margin", "Journey to the West"], "The kite-flying episode is from A Dream of Red Mansions. The straw boats, tiger fight, and stone monkey are from the other books."),
        ("What are the characters mainly doing in this lesson?", "Flying kites in a garden", ["Borrowing arrows from straw boats", "Fighting a tiger at Jingyang Ridge", "Jumping through a waterfall to find the Water-Curtain Cave"], "The springtime fun is kite-flying. Borrowing arrows, fighting a tiger, and the cave are from other stories."),
        ("What happens to some of the kites in the text?", "Their strings break and they fly away", ["Cao Cao shoots all of them down", "They turn into tigers", "None of them get into the air"], "Some kites rise into the sky and fly away when their strings break. This is not about arrows or tigers."),
        ("How is this text different from The Monkey King Is Born?", "One describes kite-flying in A Dream of Red Mansions; the other describes the stone monkey's birth in Journey to the West", ["Both show Sun Wukong flying a kite", "Both are from Water Margin", "Both were written by Zhuge Liang"], "They are from different books and describe different events. Do not confuse them because both have lively scenes."),
    ],
)

K(
    "g5b_gan", "Writing: A Reading Response", "Writing Fundamentals", 5, "下", 2, "application",
    "Write a reading response by naming the text, briefly describing its events, and focusing on your own reaction. Do not copy the entire text.",
    "xz_56",
    [
        ("Which passage sounds like a reading response?", "After reading Borrowing Arrows with Straw Boats, I remembered how Zhuge Liang planned for the fog and the boats. I should also think through difficulties before acting.", ["The four words Borrowing Arrows with Straw Boats.", "This book is good.", "Zhou Yu."], "Include the title and your own thought. Saying only that it is good does not explain why."),
        ("What should you never do in a reading response?", "Copy the whole text without adding any personal reaction", ["Briefly name the text", "Explain what you found moving about a character", "Connect it to a similar event in your life"], "Copying the text is still copying. A reading response should include your reaction."),
        ("Which idea is off topic?", "A response titled Reading Jingyang Ridge that only explains how to raise silkworms", ["Describe Wu Song's bravery and recall a time you were afraid to admit something", "Write about a time you ignored advice, like Wu Song crossing the ridge", "Say that you want to tell the story to a younger sibling"], "Your response should connect to the text. Silkworm raising is unrelated to fighting a tiger."),
        ("What can you ask yourself when reviewing a reading response?", "Can readers identify the text and understand my own ideas?", ["Have I copied every word from the book?", "Have I avoided writing any personal reaction?", "Can I turn it into a shopping list?"], "Include both the title and your ideas. A copy or vague statements alone are not a complete response."),
    ],
)

# The Han idioms below are the assessed vocabulary; surrounding prose is translated.
K(
    "g5b_cheng", "Language Practice 2: Using Idioms", "Vocabulary", 5, "下", 2, "conceptual",
    "Use idioms in suitable sentences. The textbook-play speaking task is included here: identify the characters and act out the main events instead of simply reading the text aloud.",
    "cy_56",
    [
        ("Which idiom describes Zhuge Liang's clever plan for the fog and arrows?", "神机妙算", ["完好无缺", "半途而废", "守株待兔"], "神机妙算 describes a clever, accurate plan. 完好无缺 means undamaged."),
        ("Which idiom describes arrows that are not damaged?", "完好无缺", ["神机妙算", "头破血流", "三心二意"], "The arrows on the straw bundles are undamaged. 神机妙算 describes a person's plan, not the arrows."),
        ("Which sentence uses its idiom correctly?", "Zhou Yu admired Zhuge Liang's 神机妙算.", ["This arrow is 神机妙算 and did not break.", "He used 完好无缺 to describe a plan that went wrong.", "The fog was 完好无缺, so there were no boats."], "A person can be 神机妙算. 完好无缺 does not describe making a mistake."),
        ("Who is the best fit for the idiom 负荆请罪?", "Lian Po apologizing to Lin Xiangru", ["Zhuge Liang borrowing arrows from Cao Cao", "Wu Song apologizing to a tiger", "Sun Bin surrendering to King Wei of Qi"], "Lian Po carries thorn branches to apologize. Borrowing arrows, fighting a tiger, and horse racing do not fit this idiom."),
    ],
)

K(
    "g5b_du", "Reading Club: Classical Masterpieces and Life's Many Flavors", "Reading Comprehension", 5, "下", 2, "conceptual",
    "This reading club focuses on Chinese classical novels. The lessons about borrowing arrows, Jingyang Ridge, the birth of the Monkey King, and kite flying in the Red Chamber come from Romance of the Three Kingdoms, Water Margin, Journey to the West, and A Dream of Red Mansions.",
    "yd_56",
    [
        ("What kind of books are suggested by the reading-club theme about classical masterpieces and life's many flavors?", "Chinese classical novels such as Romance of the Three Kingdoms, Water Margin, Journey to the West, and A Dream of Red Mansions", ["Only a copy of today's class schedule", "A manual that only describes the height of the pyramids", "Only the poem Children Playing with Ice"], "All four are long novels. A schedule, a manual, and a short poem are not part of this reading."),
        ("Which novel contains the story of borrowing arrows with straw boats?", "Romance of the Three Kingdoms", ["Water Margin", "Journey to the West", "A Dream of Red Mansions"], "Zhuge Liang borrows arrows in Romance of the Three Kingdoms. The tiger fight is in Water Margin."),
        ("Which novel contains the story at Jingyang Ridge?", "Water Margin", ["Romance of the Three Kingdoms", "Journey to the West", "A Dream of Red Mansions"], "Wu Song fights the tiger in Water Margin. The stone monkey is from Journey to the West, and kite flying is from A Dream of Red Mansions."),
        ("What shows that you have understood what you read?", "Identify what the characters did and reflect on your own response", ["Remember only how thick the book is", "Treat all four novels as one story", "Ignore the plot and look only at the cover color"], "Understand the characters and plot before reflecting on them. Looking only at thickness or color does not mean you have read the book."),
    ],
)

# The Han characters below are the assessed examples for inferring meaning from radicals.
K(
    "g5b_han", "Integrated Study: Chinese Characters Are Interesting", "Character Recognition and Writing", 5, "下", 3, "conceptual",
    "Use radicals to infer a character's meaning and category. This is a strategy practiced in the integrated study of Chinese characters. This unit has no language-practice section.",
    "sz_56",
    [
        ("江, 河, 湖, and 海 share the water radical. What are they generally related to?", "Water", ["Trees", "Metal", "Speech"], "Characters with the water radical are often related to water."),
        ("What does the radical in 铜, 铁, and 银 suggest?", "Metal", ["Water", "Hand movements", "Grass"], "Characters with the metal radical are often related to metal."),
        ("What does the 言 radical in 订, 记, and 讨 suggest?", "Language", ["Walking", "Buildings", "Illness"], "Characters with the speech radical are often related to speaking and language."),
        ("What is useful when you see an unfamiliar character?", "Look at its radical, then use the context", ["Look only at the last stroke", "Ignore all radicals", "Choose any pronunciation and treat it as the meaning"], "A radical can suggest a category, and context can help confirm the meaning."),
    ],
)

# The Han character forms below are the assessed examples of pictographs and associative compounds.
K(
    "g5b_xiang", "Integrated Study: I Love Chinese Characters", "Character Recognition and Writing", 5, "下", 3, "conceptual",
    "Distinguish pictographs, which resemble what they represent, from associative compounds, which combine meanings. This unit has no language-practice section.",
    "sz_56",
    [
        ("What type of characters are 日 and 月?", "Pictographs", ["Associative compounds", "Arbitrary circles rather than characters", "Antonyms"], "The ancient forms of 日 and 月 resemble the Sun and moon, so they are pictographs."),
        ("In 休, a person rests against a tree. What type of character is it?", "An associative compound", ["A pictograph", "A polyphonic character", "A homophone"], "The parts 人 and 木 combine to express rest, so 休 is an associative compound rather than a picture of one object."),
        ("Why is 明 an associative compound?", "日 and 月 combine to mean brightness", ["Its shape looks like an eye", "It is pronounced exactly like 日", "It has only one radical"], "Two light-giving characters combine to express brightness. This is an associative compound."),
        ("Which statement is correct?", "A pictograph resembles an object; an associative compound combines meanings", ["The two methods are identical", "Associative compounds cannot be divided into parts", "Pictographs must always be left-right structures"], "Decide whether the whole character resembles an object or whether its parts each contribute meaning."),
    ],
)

# The Chinese verse lines below are the assessed source text; surrounding prose is translated.
K(
    "g5b_cong", "Reading the poem Joining the Army", "Classical Chinese Poetry and Prose", 5, "下", 4, "conceptual",
    "Memorize Wang Changling's poem Joining the Army, beginning with Qinghai's long clouds. Do not mix it with Out of the Frontier Pass or the other poems in this lesson.",
    "gs_56",
    [
        ("Which line follows 青海长云暗雪山?", "孤城遥望玉门关", ["黄沙百战穿金甲", "不破楼兰终不还", "秦时明月汉时关"], "Long clouds darken the snowy mountains, with a lonely fort looking toward Yumen Pass. 秦时明月汉时关 is from Out of the Frontier Pass."),
        ("Which line follows 黄沙百战穿金甲?", "不破楼兰终不还", ["孤城遥望玉门关", "不教胡马度阴山", "万里长征人未还"], "After countless battles, the armor is worn through by sand; the soldiers will not return until Loulan is defeated. The other two lines are from Out of the Frontier Pass."),
        ("Who wrote both Joining the Army and Out of the Frontier Pass?", "Wang Changling", ["Wang Changling wrote one, and Wang Han wrote the other", "Li Bai wrote both", "Du Fu wrote one, and Lu You wrote the other"], "Wang Changling wrote both frontier poems, but their lines should not be mixed. Wang Han wrote Song of Liangzhou."),
        ("Which line belongs to Joining the Army rather than Out of the Frontier Pass?", "不破楼兰终不还", ["秦时明月汉时关", "万里长征人未还", "但使龙城飞将在"], "Loulan and Yumen Pass appear in Joining the Army; the flying general and Yin Mountain are in Out of the Frontier Pass."),
    ],
)

K(
    "g5b_xiao", "Reading the poem A Feeling on a Cool Autumn Dawn Outside the Fence", "Classical Chinese Poetry and Prose", 5, "下", 4, "conceptual",
    "Memorize Lu You's poem: the 30,000-li river is the Yellow River, the 5,000-ren mountain is Mount Hua, and the people in the occupied land still look south for the royal army. Do not mix it with To My Son or Joining the Army.",
    "gs_56",
    [
        ("Which line follows 三万里河东入海?", "五千仞岳上摩天", ["遗民泪尽胡尘里", "五千仞岳上摩云", "南望王师又一年"], "The river is the Yellow River and the mountain is Mount Hua, rising toward the sky. 遗民泪尽胡尘里 is third; 摩云 is not the line."),
        ("Which line follows 遗民泪尽胡尘里?", "南望王师又一年", ["三万里河东入海", "不破楼兰终不还", "初闻涕泪满衣裳"], "The people in the occupied land look forward to the Song army year after year. The Loulan line is from Joining the Army; the line about tears on clothes is from On Hearing the Army Reclaim Henan and Hebei."),
        ("Who wrote this poem?", "Lu You", ["Wang Changling", "Du Fu", "Fan Chengda"], "Lu You wrote the poem about going out at an autumn dawn. Wang Changling wrote Joining the Army, and Du Fu wrote On Hearing the Army Reclaim Henan and Hebei."),
        ("What feeling is expressed by 南望王师又一年?", "The people in the occupied land have waited another year, and the Song army has still not arrived", ["The land has been recovered, so they are happy to return home", "A child is playing with ice in a golden basin", "A shepherd boy is playing a flute on an ox"], "又一年 means they are still waiting. The joy after the recovery is in Du Fu's poem, not this one."),
    ],
)

K(
    "g5b_wen", "Reading On Hearing the Army Reclaim Henan and Hebei", "Classical Chinese Poetry and Prose", 5, "下", 4, "conceptual",
    "Memorize Du Fu's poem: on hearing that Jibei has been recovered, the poet cries with joy and wants to return home at once. In this context, 妻子 means wife and children. Do not confuse it with Lu You's poem about waiting for the royal army.",
    "gs_56",
    [
        ("Which line follows 剑外忽传收蓟北?", "初闻涕泪满衣裳", ["漫卷诗书喜欲狂", "初闻涕泪满衣襟", "南望王师又一年"], "On first hearing the news, the poet cries until his clothes are wet. 喜欲狂 is the fourth line; 南望王师 is from Lu You's poem."),
        ("In 却看妻子愁何在, who does 妻子 refer to?", "His wife and children", ["Only his wife, not his children", "Only his son", "Du Fu's friends"], "In this poem 妻子 refers to the wife and children. 愁何在 means the sorrow is gone."),
        ("Who wrote On Hearing the Army Reclaim Henan and Hebei?", "Du Fu", ["Lu You", "Wang Changling", "Li Bai"], "Du Fu is overjoyed to hear that the army has recovered the lost land. Lu You wrote about people still waiting for the royal army."),
        ("How do the feelings in this poem differ from those in A Feeling on a Cool Autumn Dawn Outside the Fence?", "This poem expresses joy at the news of recovery; the other shows people still waiting year after year", ["Both poems have the same mood and are about playing with ice", "Both describe fighting a tiger", "This one is about borrowing arrows, and the other is about flying kites"], "One brings good news, while the other still looks south in hope. Both mention tears, but for different reasons."),
    ],
)

# The quoted Chinese line below is the assessed source text; surrounding prose is translated.
K(
    "g5b_an", "Reading Loyal Bones Rest Under Green Hills Everywhere", "Reading Comprehension", 5, "下", 4, "reasoning",
    "Understand how Chairman Mao, after his son Mao Anying died in Korea, grieved but still decided to bury him there.",
    "yd_56",
    [
        ("Who died in Korea in this text?", "Mao Anying", ["Liu Bocheng", "Fang Zhimin", "Wu Song"], "Chairman Mao receives the news that his son Mao Anying has died. Liu Bocheng is the patient in The God of War."),
        ("What does Chairman Mao finally decide to do with Mao Anying's remains?", "Agree to bury him in Korea", ["Insist that he be taken home immediately", "Refuse to believe the news", "Ask him to borrow arrows from straw boats"], "The idea of loyal bones resting under green hills means that a fallen soldier may be buried where he fought."),
        ("What does 青山处处埋忠骨，何须马革裹尸还 mean here?", "The loyal dead can be buried in the hills where they fought; their remains need not be wrapped in horsehide and taken home", ["All remains must be brought back to their hometown", "No one has ever been buried in green hills", "Horsehide is a kind of food"], "Wrapping a body in horsehide means bringing it home. The line says this is not always necessary."),
        ("What feelings does the text show Chairman Mao experiencing?", "He is a father who has lost his son, yet puts the larger cause ahead of his grief", ["He does not care and acts as if nothing happened", "He is only a boatman", "He is operating on a wounded soldier"], "His grief is real, and so is his decision. The operation on Liu Bocheng is in a different story."),
    ],
)

K(
    "g5b_jun", "Reading The God of War", "Reading Comprehension", 5, "下", 4, "reasoning",
    "Understand how Liu Bocheng refuses anesthesia and is called a god of war by Dr. Walker.",
    "yd_56",
    [
        ("Who is the soldier having the operation?", "Liu Bocheng", ["Huang Jiguang", "Lian Po", "Wu Song"], "Liu Bocheng has an injured right eye and refuses anesthesia. Huang Jiguang is a hero who blocked a gun barrel, not the main character here."),
        ("Why does he refuse anesthesia?", "He wants to keep his mind clear", ["The hospital has no medicine", "Dr. Walker forbids it", "His eye is not actually injured"], "As a soldier, he worries that anesthesia will affect his mind. He does not make a sound during the operation."),
        ("How many cuts does Dr. Walker count during the operation?", "Seventy-two", ["Seven", "Twelve", "None"], "Liu Bocheng counts too. Walker says there are seventy-two cuts."),
        ("Why does Walker call him a god of war?", "He endures a severe injury without anesthesia, showing extraordinary willpower", ["He has the highest military rank", "He speaks German", "The operation is unsuccessful"], "Walker says he is like a talking steel plate, worthy of being called a god of war."),
    ],
)

K(
    "g5b_pin", "Reading Integrity in Poverty", "Reading Comprehension", 5, "下", 4, "reasoning",
    "Understand how, after Fang Zhimin is captured, the enemy searches for wealth but finds that he has accumulated no personal property. His simple life reflects a revolutionary's integrity.",
    "yd_56",
    [
        ("Who wrote Integrity in Poverty?", "Fang Zhimin", ["Liu Bocheng", "Ji Xianlin", "Feng Jicai"], "Fang Zhimin wrote about his own capture. Liu Bocheng appears in The God of War."),
        ("What does the enemy hope to find when searching him?", "Gold and valuables", ["A poem", "A small boat", "An ink painting of plum blossoms"], "They assume that someone who held a high position must carry money. They do not find the valuables they expect."),
        ("Although he handled a great deal of money, how did he live?", "He spent the money on the revolution, lived simply, and accumulated no personal wealth", ["He exchanged all the money for gold and hid it at home", "He admits he never handled money", "He lent the money to Cao Cao to make arrows"], "Handling money does not mean owning it. That is the point of the text."),
        ("What does integrity in poverty mean in this text?", "A simple, honest life that helps a revolutionary withstand hardship", ["Being unable to do anything", "Having no family", "Refusing to work"], "Living simply is not a flaw. Fang Zhimin sees it as part of a revolutionary's character."),
    ],
)

K(
    "g5b_ta", "Writing: He ____", "Writing Fundamentals", 5, "下", 4, "application",
    "Complete the title with an action or change, such as He laughed, He froze, or He understood. Use actions and speech before and after to show the change instead of merely copying the title.",
    "xz_56",
    [
        ("Which completion of He ____ can lead to a writing piece?", "He hesitated", ["He did", "The weather did", "The textbook did"], "Complete the blank with a change in a person's behavior. Weather and textbooks are not the person in the title."),
        ("Which passage best shows that he understood?", "His younger brother cleaned up the broken cup himself. He stood at the doorway for a long time, then said, 'I'll do it next time.'", ["He understood.", "The words he understood.", "Today is Monday."], "Picking up the cup, standing for a while, and saying those words make the change visible. Simply saying that he understood is vague."),
        ("Which idea does not fit this writing task?", "Writing only about Fan Chengda's fieldwork without describing a moment from your own life", ["Describe Grandpa standing up after hearing good news", "Describe a classmate biting their lip when falling behind", "Describe leaving a light on for Dad when he comes home late"], "The topic is a moment of personal change. Writing only about an ancient poet farming leaves out the writer."),
        ("Which sentence describes a moment in detail?", "I gripped the payment slip, stood at the counter twice, and handed over the money on my third try.", ["I became brave.", "That moment, I grew up.", "The word counter."], "Standing twice and handing over the money on the third try lets readers see the process. Simply saying brave is a conclusion."),
    ],
)

# The Han expressions below are the assessed vocabulary; surrounding prose is translated.
K(
    "g5b_ci", "Language Practice 4: Words for Describing People", "Vocabulary", 5, "下", 4, "conceptual",
    "Choose words that describe expressions and actions, and do not confuse praise with criticism. These words will be useful in later character descriptions. Unit 5 has no language-practice section, so the vocabulary is included here.",
    "cy_56",
    [
        ("Which expression describes someone making a decisive, admirable choice?", "斩钉截铁", ["犹豫不决", "东张西望", "漫不经心"], "斩钉截铁 describes speaking or acting decisively. 犹豫不决 means the opposite."),
        ("Which expression describes someone watching with full attention?", "目不转睛", ["视而不见", "闭目养神", "左顾右盼"], "目不转睛 means keeping one's eyes fixed on something. 视而不见 means seeing something but acting as if one did not."),
        ("Which sentence uses its expression appropriately?", "He clenched his fists; his eyes were 目光炯炯.", ["He clenched his fists and looked distracted, so he was firmly determined.", "He said his sleeping friend was 目不转睛.", "He kept changing his mind, though his friend described him as 斩钉截铁."], "A clenched fist and a 目光炯炯 gaze show strength. Someone asleep is not watching without blinking."),
        ("Which word criticizes someone for deciding without thinking?", "武断", ["果断", "坚定", "认真"], "武断 is critical. 果断, 坚定, and 认真 are usually praise."),
    ],
)

K(
    "g5b_renwu", "Reading A Set of Character Portraits", "Reading Comprehension", 5, "下", 5, "reasoning",
    "Understand three character sketches: Xiao Gazi and Pang Dun'er in Wrestling, Xiangzi in He Is Like a Sturdy Tree, and Yan Jiansheng in Two Stalks of Lamp Grass. The three excerpts form one topic.",
    "yd_56",
    [
        ("Who competes with Pang Dun'er in Wrestling, and what happens?", "Xiao Gazi circles his opponent trying to gain an advantage, but is thrown down", ["Wu Song throws a tiger down", "Xiangzi throws a cart down", "Yan Jiansheng wins two stalks of lamp grass"], "Xiao Gazi is from the story The Young Soldier Zhang Ga. He circles and hooks with his leg, but Pang Dun'er throws him."),
        ("Who is described in He Is Like a Sturdy Tree?", "Xiangzi; the author is Lao She", ["Xiao Gazi; the author is Xu Guangyao", "Yan Jiansheng; the author is Wu Jingzi", "Brush Master Li; the author is Feng Jicai"], "Lao She uses a tree to describe Xiangzi's sturdy, upright build. The other characters are from different excerpts."),
        ("Why does Yan Jiansheng hold up two fingers as he is dying?", "There are two stalks of lamp grass burning, and he worries about the wasted oil", ["He wants two more bowls of rice", "He wants to leave two sons behind", "He is counting two horse-race wins"], "He dies only after Zhao removes one stalk. The detail shows his stinginess. The story is from The Scholars."),
        ("What do the three excerpts teach about character writing?", "Use an action, appearance, or small detail to make a person vivid", ["Use the same vague phrase for everyone", "Memorize poems instead of describing people", "Give all three characters the same name"], "The wrestling, tree, and lamp grass each focus on one revealing detail. Vague words could describe anyone."),
    ],
)

K(
    "g5b_shua", "Reading Brush Master Li", "Reading Comprehension", 5, "下", 5, "reasoning",
    "Understand Feng Jicai's Brush Master Li: if a speck of white appears on his black clothes, he refuses payment. The white spot his apprentice Cao Xiaosan sees is actually a tiny burn hole from a cigarette.",
    "yd_56",
    [
        ("What rule does Brush Master Li follow while working?", "If a white speck appears on his black clothes, he will not accept payment", ["His clothes must be covered in white specks before the job is done", "He paints walls only at night", "He must fight a tiger before painting"], "A white speck is the flaw he refuses to allow. The story was written by Feng Jicai."),
        ("What does Cao Xiaosan think when he sees a white speck on his master's clothes?", "He thinks the master's skill is a lie", ["He thinks it is a piece of gold", "He immediately throws away his master's clothes", "He decides it is a tiger's footprint"], "He came to find out whether the master's reputation was true. When the speck appears, he doubts him."),
        ("What is the white speck actually?", "A small cigarette burn that reveals the white undershirt", ["White paint showing that the job failed", "A raindrop", "A grain of rice"], "The hole was burned, not caused by paint. The master's rule was not broken."),
        ("What does the story mainly show about Brush Master Li?", "His painting skill is exceptional, and he is confident in it", ["He cannot paint walls", "He is afraid of black clothes", "He is the innkeeper at Jingyang Ridge"], "After painting an entire wall, his black clothes are still clean. That is the proof of his skill."),
    ],
)

K(
    "g5b_ren", "Writing: Show a Person's Distinctive Traits", "Writing Fundamentals", 5, "下", 5, "application",
    "Write about a person's most distinctive trait and show it through a specific event rather than simply saying that the person is good. The sample texts My Friend Rongrong and The Young Goalkeeper and His Spectators are examples of technique, not standalone lessons. This unit has no language-practice section.",
    "xz_56",
    [
        ("Which sentence captures the trait of someone who is skilled at painting walls?", "With each stroke, the wall became smooth and bright, yet no white speck appeared on his black clothes.", ["He is a good person.", "The words master painter are easy to write.", "There is a wall on the wall."], "The smooth, bright wall and spotless clothes show the skill. Saying only that someone is good could describe anyone."),
        ("Which sentence is vague?", "My deskmate is very, very good.", ["When he lends me an eraser, he even blows off the dust.", "He is always the last to leave after classroom duty.", "He pronounces every word clearly when reading aloud."], "Very good does not explain what is good. The other sentences describe specific actions."),
        ("How should you choose material when writing about someone?", "Choose an event that shows the person's distinctive trait", ["Describe every strength with the same vague sentence", "Write only the person's name and age", "Write about something unrelated to the person"], "The details should support the trait. A name and age do not show one."),
        ("What role do My Friend Rongrong and The Young Goalkeeper and His Spectators play in this writing task?", "They are examples for learning how to show a trait, not separate texts to study", ["They are two poems to memorize", "They are manuals unrelated to describing people", "They must be copied from beginning to end"], "One describes a friend's habits; the other describes a goalkeeper. They teach writing techniques rather than forming separate lessons."),
    ],
)

# The quoted Chinese lines below are the assessed source text; surrounding prose is translated.
K(
    "g5b_mao", "Reading The Spear and the Shield", "Reading Comprehension", 5, "下", 6, "reasoning",
    "Understand why a seller who boasts about both his spear and his shield cannot answer a question.",
    "yd_wenyan",
    [
        ("How does the seller first praise his shield?", "He says nothing can pierce it", ["It can pierce anything", "It is as sharp as his spear", "Someone gave it to him"], "The source text says, 吾盾之坚，物莫能陷也."),
        ("How does he then praise his spear?", "He says it can pierce anything", ["Nothing can pierce it", "It is stronger than the shield", "It is already broken"], "The source text says, 吾矛之利，于物无不陷也."),
        ("Someone asks him to use his spear to pierce his shield. Why can he not answer?", "His two claims cannot both be true", ["He did not hear the question", "The spear and shield are not nearby", "Someone else answers for him"], "The shield is said to stop everything, while the spear is said to pierce everything. The claims contradict each other."),
        ("What does 其人弗能应 mean?", "The man cannot answer", ["The man answers immediately", "The man sells the spear", "The man admits the shield is better"], "弗能应 means being unable to respond. The story is from Han Feizi."),
    ],
)

K(
    "g5b_sai", "Reading Tian Ji's Horse Race", "Reading Comprehension", 5, "下", 6, "reasoning",
    "Understand how Sun Bin changes the order of the horses so Tian Ji wins two races and loses one. This classical text retells the same event studied in Grade 4.",
    "yd_wenyan",
    [
        ("Who gives Tian Ji the strategy?", "Sun Bin", ["Sun Wu", "Lin Xiangru", "Zhuge Liang"], "Sun Bin realizes the horses' abilities are close enough for a different order to work. Sun Wu and Sun Bin are different people."),
        ("How do Tian Ji's horses compare with King Wei of Qi's horses?", "Each of Tian Ji's three ranks is slightly weaker", ["Each rank is much faster", "Tian Ji has only one horse", "All of Tian Ji's horses are faster"], "Within each rank, Tian Ji's horse is slightly weaker, so he used to lose."),
        ("How does Sun Bin tell Tian Ji to arrange the races?", "Use the lower-ranked horse against the king's best, then the best against the middle, and the middle against the lowest", ["Keep the original order for all three races", "Use only the best horse", "Ask King Wei to replace his horses first"], "Tian Ji loses once with the lower-ranked horse, then wins the next two races."),
        ("What is the result of the races?", "Tian Ji wins two and loses one, so he wins overall", ["Tian Ji loses all three", "Each side wins once", "The race is canceled"], "Losing one race and winning two still gives Tian Ji the overall victory."),
    ],
)

K(
    "g5b_tiao", "Reading The Jump", "Reading Comprehension", 5, "下", 6, "reasoning",
    "Understand why the captain uses a gun to make a boy jump into the water after he climbs the mast.",
    "yd_56",
    [
        ("How does the boy get to the top of the mast?", "He climbs up step by step while chasing a monkey", ["The captain carries him up", "He climbs the mast from the sea", "A sailor pulls him up with a rope"], "The monkey hangs his hat high on the mast, and he follows it. The story was written by Leo Tolstoy."),
        ("Why does the captain aim a gun at the boy?", "To order him to jump into the sea immediately", ["To shoot the boy down", "To shoot the monkey", "To scare the sailors on deck"], "Climbing higher or falling from the crossbar could be fatal; jumping into the sea gives others a chance to rescue him."),
        ("Which action does the captain not take?", "Climb the mast and carry the boy down", ["Aim a gun to make the boy jump into the water", "Jump into the sea to rescue the boy", "Order the boy to jump into the sea"], "The captain does not climb up and carry the boy down; he makes him jump."),
        ("What does the captain's decision show?", "He can make a quick judgment in an emergency", ["He does not know whether the boy can swim", "He is only pretending to scare the boy", "He draws the gun to punish the boy"], "Jumping into the sea offers a better chance of survival than falling from the mast."),
    ],
)

K(
    "g5b_tan", "Writing: A Magical Expedition", "Writing Fundamentals", 5, "下", 6, "application",
    "Write an imagined expedition step by step: where you go, what difficulty you face, and how someone solves it. You may invent events, but do not skip straight to saying that you won.",
    "xz_56",
    [
        ("Which passage sounds like an expedition?", "The opening was only wide enough for one person to turn sideways. I held the flashlight in my mouth, and loose stones suddenly shifted under my feet.", ["We went on an expedition.", "The expedition was magical.", "The two words magical expedition."], "Turning sideways, holding a flashlight, and slipping stones let readers follow the action. Simply saying that the group went does not begin the journey."),
        ("An expedition can be imaginary, but what should you avoid?", "Introducing a difficulty and then immediately saying, 'Then we won,' without showing what happened", ["Describe the danger they faced", "Describe the solution someone proposed", "Describe how they left at the end"], "The events may be invented, but each step should connect. Skipping the difficulty makes the expedition feel unreal."),
        ("Which idea does not fit this writing task?", "Writing only about how to shorten sentences, without beginning an expedition", ["Describe how the team calls to one another after getting lost on a mountain", "Describe how they tie a broken part of a raft back together while crossing a river", "Describe checking the water and flashlight before entering a cave"], "The topic is an expedition. Writing only about sentence shortening leaves the characters at the starting point."),
        ("What can you learn from The Jump for this writing task?", "Describe clearly what the characters do when danger appears", ["An expedition must include a captain with a gun", "An expedition cannot include any difficulties", "Copy The Jump word for word"], "The lesson is to make the characters' actions in an emergency specific, not to copy the text or avoid danger."),
    ],
)

# Chinese sentence examples below are the assessed source material for shortening and expanding.
K(
    "g5b_suo", "Language Practice 6: Shortening and Expanding Sentences", "Sentence Structure", 5, "下", 6, "procedural",
    "When shortening a sentence, keep who did what; when expanding one, add suitable detail without changing its main meaning. The practice section also includes terms for ages twenty and thirty; here the focus is sentence length.",
    "jz_56",
    [
        ("Which is a shortened version of 可爱的熊猫在竹林里慢慢地吃鲜嫩的竹子?", "熊猫吃竹子。", ["可爱的熊猫。", "慢慢地吃。", "竹林很美。"], "Keep the core of the sentence: who did what. 可爱, 慢慢, and 鲜嫩 are modifiers."),
        ("What is the core of 红红的太阳从东方慢慢升起来?", "太阳升起来。", ["红红的太阳。", "从东方慢慢。", "太阳很红。"], "太阳 is who or what; 升起来 is what it does. 红红 and 慢慢 are modifiers that can be removed."),
        ("Which expansion of 燕子飞 keeps the original meaning?", "活泼的小燕子在空中飞来飞去。", ["燕子停在树上不飞了。", "燕子变成了老鹰。", "燕子两个字很好听。"], "An expansion can add a description or place, but it cannot change flying to stopping or replace the bird."),
        ("Which approach is incorrect when shortening a sentence?", "Delete who did what and keep only an adjective", ["Remove modifiers such as lovely or slowly", "Keep the action", "Keep the main person or thing"], "Without the core, the sentence is incomplete. Modifiers can be removed, but the main structure must remain."),
    ],
)

K(
    "g5b_wei", "Reading The Gondolas of Venice", "Reading Comprehension", 5, "下", 7, "reasoning",
    "Understand how Mark Twain describes the shape of the gondolas, the boatmen's skill, and the quiet of the night.",
    "yd_56",
    [
        ("Who wrote The Gondolas of Venice?", "Mark Twain", ["Leo Tolstoy", "Karel Čapek", "Mu Qing"], "Mark Twain wrote this text. Tolstoy wrote The Jump, and Čapek wrote The Country of Pastures."),
        ("What role do gondolas play in Venice?", "They are a main form of transportation", ["They are only for tourists to photograph; local people do not use them", "They have all been replaced by bridges", "They appear only at night"], "The canals are like streets, and gondolas are like cars elsewhere."),
        ("What does the text compare the gondola to?", "A canoe, a crescent moon, and a water snake", ["A white warhorse", "A stone bridge", "A banyan tree"], "It is narrow and deep like a canoe, curves upward at both ends like a crescent moon, and moves lightly like a water snake."),
        ("What happens in Venice after the theaters let out late at night?", "The boats moor and the city gradually becomes quiet", ["More boats appear and the city stays noisy all night", "All the canal water drains away", "The boatmen begin racing"], "The boats stop, the splashing water grows quiet, and old Venice goes to sleep."),
    ],
)

K(
    "g5b_chang", "Reading The Country of Pastures", "Reading Comprehension", 5, "下", 7, "reasoning",
    "Understand Karel Čapek's description of Dutch pastures: cattle, horses, and sheep relax by day, and the land becomes quiet at night. The text repeatedly says, This is the real Holland.",
    "yd_56",
    [
        ("Where does The Country of Pastures take place, and who wrote it?", "Holland; it was written by Karel Čapek", ["Venice; it was written by Mark Twain", "Egypt; it was written by Mu Qing", "Central Hebei; it was written by someone else"], "Pastures, canals, and herds of cattle describe Holland. Gondolas are in Venice, and pyramids are in Egypt."),
        ("Which sentence appears repeatedly in the text?", "This is the real Holland", ["This is the real Venice", "Loyal bones rest under green hills everywhere", "We will not return until Loulan is defeated"], "The sentence closes several pasture scenes. The other lines come from different texts or poems."),
        ("What is the pasture mainly like during the day?", "Cattle, horses, and sheep are relaxed, like a quiet painting", ["All the animals crowd onto gondolas to race", "The pasture is completely covered by a desert", "There are pyramids but no cattle or sheep"], "Black-and-white cows, horses, and sheep each relax in their own way. Gondolas and pyramids are from other lessons."),
        ("What happens to the pasture at night?", "The animals rest, and everything becomes quiet", ["More gondolas appear and the city stays noisy all night", "The herd goes to borrow arrows on a straw boat", "All the lamps turn into golden towers"], "The daytime calm settles into quiet at night. The noisy scene is Venice before the theaters let out, not this text's ending."),
    ],
)

K(
    "g5b_jinzi", "Reading Evening Glow over the Pyramids and The Incomprehensible Pyramids", "Reading Comprehension", 5, "下", 7, "reasoning",
    "The Grade 5 spring unit includes two texts: Mu Qing's essay Evening Glow over the Pyramids describes the golden sunset, while The Incomprehensible Pyramids uses pictures and numbers to explain the Great Pyramid of Giza. Do not confuse them with the informational text in Grade 5, fall.",
    "yd_56",
    [
        ("Which two texts are included in the Grade 5 spring pyramid unit?", "Evening Glow over the Pyramids and The Incomprehensible Pyramids", ["Only the fall text that describes a tomb by topic", "The Gondolas of Venice and The Country of Pastures", "Borrowing Arrows with Straw Boats and Jingyang Ridge"], "The unit includes two texts. The fall pyramid text is a separate informational piece; the gondolas and pasture texts are other lessons in this unit."),
        ("What does Evening Glow over the Pyramids describe, and who wrote it?", "The pyramids glowing gold at sunset; it was written by Mu Qing", ["Gondolas shaped like crescent moons; Mark Twain", "Cattle in Holland; Karel Čapek", "The moon at home; Ji Xianlin"], "The fields, desert, and river are all gilded by the sun, making the pyramids seem cast from gold. This is Mu Qing's essay."),
        ("How does The Incomprehensible Pyramids present the Great Pyramid of Giza?", "With pictures and numbers about its location, scale, and careful construction", ["As a seven-character poem", "As a story about a captain ordering a boy to jump", "As a grandfather giving away an ink painting"], "This noncontinuous text uses pictures, data, and brief explanations. Poems, the jump, and the plum blossom are other lessons."),
        ("Why are the spring texts different from the fall text called The Pyramids?", "The fall text describes the tomb by topic; the spring unit has a sunset essay and a separate illustrated informational text", ["Both are the same passage written by Mu Qing", "Both describe nighttime in Venice", "The spring unit has no pyramids, only gondolas"], "The titles both mention pyramids, but the texts use different forms. The fall text is not called Evening Glow over the Pyramids."),
    ],
)

K(
    "g5b_chan", "Writing: China's World Heritage Sites", "Writing Fundamentals", 5, "下", 7, "application",
    "Choose a World Heritage site in China and describe where it is, what it looks like, and why it matters. The speaking task, Be a Young Tour Guide, is included here: explain it in an order that makes sense to someone who has never visited.",
    "xz_56",
    [
        ("Which place is suitable for this writing task?", "The Great Wall", ["A pasture in Holland", "A gondola in Venice", "A pyramid in Egypt"], "The Great Wall is in China and is a World Heritage site. The pasture, gondola, and Egyptian pyramid are not Chinese sites."),
        ("Which passage sounds like an introduction?", "The Great Wall follows the ridgeline. From the wall, one side drops steeply while watchtowers stand in the distance.", ["The heritage site is good.", "China's World Heritage.", "The words young tour guide."], "Include the place and what it looks like. Saying only that it is good does not identify what is being introduced."),
        ("How should a young tour guide explain a site?", "In order: where it is, what it looks like, and why it is worth seeing", ["Say welcome and stop", "Present something unseen as a measurement you personally made", "Switch to an unrelated joke"], "Guide visitors through the explanation. Do not present unsupported numbers as measurements."),
        ("Which idea does not fit this writing task?", "Write only about cows grazing in Holland without mentioning a Chinese heritage site", ["Describe what the Forbidden City looks like from outside", "Explain why the Terracotta Army's formation makes people stop and look", "Describe which part of the Great Wall you point out first as a guide"], "The topic is a World Heritage site in China. Writing only about Holland's cows would belong to The Country of Pastures."),
    ],
)

# The Chinese sentence examples below are the assessed source material for descriptive writing.
K(
    "g5b_se", "Language Practice 7: Describing Scenes with Color", "Sentence Structure", 5, "下", 7, "procedural",
    "Use color to describe a scene concretely, as in Evening Glow over the Pyramids. The section also includes Weng Juan's poem Village in April; this practice focuses on color.",
    "jz_56",
    [
        ("Why does Evening Glow over the Pyramids repeat the color gold?", "It links the fields, desert, river, and pyramids under the sunset in one golden scene", ["Gold can be borrowed to make arrows", "The author does not know other words", "The gondolas of Venice are golden horses"], "Repeating the same color connects the scene. The arrows and gondolas are unrelated distractors."),
        ("Which sentence uses color to describe a scene concretely?", "墙是白的，台阶是白的，连栏杆也是白的。", ["The place is beautiful.", "The words scene and scenery.", "White sounds pleasant."], "The color white is applied to the wall, steps, and railing. Saying only that it is beautiful gives no color detail."),
        ("Which sentence does not apply color to a scene?", "我喜欢颜色。", ["草地绿得发亮，溪水也绿得发亮。", "傍晚的云从金黄变成浅紫。", "雪停以后，屋顶、树枝、车道都白了。"], "I like colors does not say what color anything is. The other sentences describe colors in scenes."),
        ("Which approach is not suitable when using color to describe a scene?", "Put five unrelated things in one sentence, with colors that do not match them", ["Repeat the same color for one scene", "Say what the lighting was like", "Describe the color first, then your reaction"], "Color should fit the scene. Unrelated details make the image feel scattered."),
    ],
)

# The quoted Chinese passages and characters below are the assessed source text and wordplay.
K(
    "g5b_yang", "Reading The Yang Family's Son", "Reading Comprehension", 5, "下", 8, "reasoning",
    "Understand the child in A New Account of Tales of the World: Kong Junping jokes about his surname using yangmei fruit, and the child responds politely with a peacock pun.",
    "yd_wenyan",
    [
        ("What does 孔君平诣其父，父不在，乃呼儿出 mean?", "Kong Junping visits; the father is away, so he calls the child out", ["Kong Junping is away, and the father goes to find him", "The child visits Kong Junping", "The two go horse racing"], "诣 means to visit someone. Because the father is away, Kong meets the child."),
        ("Kong Junping points to yangmei fruit and says 此是君家果. What is he doing?", "Joking about the character 杨, which appears in the fruit name and the child's surname", ["He truly believes yangmei grows in the Kong family's yard", "He tells the child to throw away the fruit", "He is testing the child's ability to recite a poem"], "杨梅 and 杨氏 share the character 杨. It is a joke, not a mistake about the fruit."),
        ("How does the child respond?", "He says he has not heard of a peacock belonging to someone surnamed Kong", ["He agrees that yangmei belongs to the Kong family", "He cries and runs away", "He invites Kong Junping to fight a tiger"], "The character 孔 in peacock matches Kong Junping's surname. 未闻 means not having heard of something."),
        ("What shows that the child is 甚聪惠?", "He understands the joke and responds politely with a matching wordplay", ["He refuses to bring out fruit", "He is older than Kong Junping", "He cannot say a word"], "惠 means clever. Offering fruit shows courtesy, and answering quickly shows wit. The story is from A New Account of Tales of the World."),
    ],
)

K(
    "g5b_shou", "Reading The Five Fingers", "Reading Comprehension", 5, "下", 8, "reasoning",
    "Understand Feng Zikai's description of the five fingers: each has its own form and use, and they work best together. The thumb is the hardest-working.",
    "yd_56",
    [
        ("Who wrote The Five Fingers, and what does the text describe?", "Feng Zikai; the different forms and uses of the five fingers on one hand", ["Ji Xianlin; five moons", "Mu Qing; five pyramids", "Mark Twain; five gondolas"], "The text describes each finger separately. The moon, pyramids, and gondolas are from other lessons."),
        ("Which finger is described as the hardest-working?", "The thumb", ["The little finger", "Only the ring finger does no work", "All five fingers are identical"], "The thumb is sturdy and not especially attractive, but often does the dirty, difficult work."),
        ("Why does the author say the five fingers need to work together?", "Each has weaknesses, and they can accomplish tasks together", ["Four can be cut off and only one kept", "They become stronger when separated", "Fingers never need to cooperate"], "One finger alone cannot do everything a hand does. The text emphasizes cooperation."),
        ("What can this text and A Set of Character Portraits teach together?", "Show each distinct trait instead of describing everyone with a vague phrase", ["When describing people, write only about their hands", "Give all five fingers the same name", "Make the traits as vague as possible"], "The thumb works hard, and each other finger has its own use. Their differences matter."),
    ],
)

K(
    "g5b_tong", "Reading A Childhood Discovery", "Reading Comprehension", 5, "下", 8, "reasoning",
    "Understand Fyodorov's childhood account: he thinks human development in the embryo repeats the course of biological evolution, then is misunderstood by a teacher when he wants to laugh in class.",
    "yd_56",
    [
        ("Who wrote A Childhood Discovery?", "Fyodorov", ["Feng Zikai", "Xiao Hong", "Ji Xianlin"], "Fyodorov wrote about a discovery from his childhood. Feng Zikai wrote The Five Fingers."),
        ("What does the narrator think he has discovered?", "Human development in the embryo seems to repeat the process of biological evolution", ["The Water-Curtain Cave", "That arrows can be borrowed with straw boats", "That only one stalk of lamp grass may be lit"], "He thinks development repeats a journey from simple life to humans. The other discoveries belong to other stories."),
        ("Why does the biology teacher send him outside?", "He remembers his discovery and cannot stop himself from smiling, so the teacher thinks he is misbehaving", ["He lends his textbook to Cao Cao", "He fights a tiger in class", "He refuses to read any word"], "He laughs because he remembers the discovery. The teacher interprets it as misbehavior; they understand the situation differently."),
        ("How does he later think about being punished?", "He humorously comforts himself that the discovery was worth the punishment", ["He never returns to school", "He thinks the teacher made the discovery for him", "He describes the teacher as a god of war"], "The humor is that the event has already happened, yet he still values the discovery more than avoiding punishment."),
    ],
)

K(
    "g5b_man", "Writing: A Lesson from a Cartoon", "Writing Fundamentals", 5, "下", 8, "application",
    "First describe who is in the cartoon and what they are doing, then explain the lesson it suggests. The lesson must connect to the image. This is different from the fall writing task about a teacher's caricature.",
    "xz_56",
    [
        ("What should you do first when writing a lesson from a cartoon?", "Clearly describe who is in the image and what they are doing", ["Ignore the image and write an unrelated moral", "Write only the word lesson", "Color over the cartoon"], "Readers have not seen the original. Without describing the image, the lesson has no context."),
        ("Which passage best fits this writing task?", "The person in the cartoon looks only at a phone and misses the peel on the ground. It reminds me to look both ways when crossing the street.", ["The cartoon is good.", "A lesson.", "Today's weather."], "Describe the image first, then the lesson it suggests. Saying only that it is good does not tell readers what it shows."),
        ("How should the lesson connect to the image?", "It should come from what the cartoon shows, not be added as an unrelated idea", ["It can be completely unrelated to the people in the image", "The word count is enough; there is no need to mention the image", "Copy The Jump as the lesson"], "The image is the source of the lesson. Copying another text does not explain this cartoon."),
        ("How is this different from the fall writing task about a teacher's caricature?", "The fall task describes a teacher's traits; this one interprets an image and explains its lesson", ["Both ask you to draw a teacher as a tiger", "Neither asks you to describe an image", "This one must describe the same teacher again"], "Both titles use the idea of a cartoon, but the tasks differ: one describes a person, the other explains an interpretation of an image."),
    ],
)

# The quoted Chinese sayings below are the assessed source text; surrounding prose is translated.
K(
    "g5b_yan", "Language Practice 8: Sayings to Remember", "Classical Chinese Poetry and Prose", 5, "下", 8, "conceptual",
    "Understand sayings about valuing justice, showing compassion, and avoiding unjust actions. The speaking task about telling jokes is included here: tell the full story so listeners can understand what is funny.",
    "gs_56",
    [
        ("What does 君子喻于义，小人喻于利 mean?", "A noble person values justice; a petty person values profit", ["A noble person values only money", "A petty person does not care about profit", "Both lines praise making money"], "喻 means to understand or value. Justice and profit are contrasted. The saying is from the Analects."),
        ("How do 君子坦荡荡 and 小人长戚戚 differ?", "One describes an open, calm mind; the other describes constant worry and resentment", ["Both describe being very tall", "坦荡荡 means crying, and 戚戚 means laughing", "They mean exactly the same thing"], "坦荡荡 means calm and open. 戚戚 means anxious and troubled; do not reverse them."),
        ("What does 多行不义，必自毙 mean?", "A person who commits many unjust acts will eventually bring about their own ruin", ["The more unjust acts, the better", "Self-destruction means receiving a reward", "The saying encourages wrongdoing"], "自毙 means to bring about one's own downfall. This is a warning, not encouragement."),
        ("What does 恻隐 mean in 恻隐之心，仁之端也?", "Feeling compassion when seeing another person suffer", ["Being happy when another person suffers", "Caring only about one's own interests", "Refusing to help anyone"], "恻隐 means compassion or unwillingness to see suffering. Mencius says it is the beginning of benevolence."),
    ],
)
