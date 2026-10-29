# -*- coding: utf-8 -*-
"""People's Education Press (2019), Compulsory Book 3. Unit names follow common tables of contents; book assignment to be verified."""
from enh_tx import V, P, G, F, R, q


def load():
    V("vo_fest", "Festivals", 12, 1,
      "Read and recognize festival, lantern, firework, and feast.",
      [("festival", "festival"), ("lantern", "lantern"), ("firework", "firework"), ("feast", "feast")], "vo_soc")

    V("vo_custom", "Ways to celebrate", 12, 1,
      "Read and recognize celebrate, origin, lunar, and decorate.",
      [("celebrate", "celebrate"), ("origin", "origin"), ("lunar", "related to the moon"), ("decorate", "decorate")], "vo_soc")

    G("gr_prep2", "Prepositional phrases as adverbials", 12, 1,
      "Identify prepositional phrases and determine whether they indicate time, place, or manner.", "sent", [
        q("They meet on Lunar New Year's Eve. What is the function of on Lunar New Year's Eve?", "A prepositional phrase used as an adverbial of time",
          "The subject", "The predicate", "The object complement", "On introduces a time expression, and the whole phrase functions as an adverbial."),
        q("Which one is a prepositional phrase?", "in the town square", "the town square", "celebrate happily", "very bright",
          "In is a preposition followed by a noun phrase."),
        q("She wrote the cards with great care. What does with great care express?", "Manner",
          "The subject", "The name of a festival", "A subordinate clause", "The with-phrase describes how she wrote the cards."),
        q("In which sentence does the prepositional phrase function as an adverbial of place?", "The feast is held in the hall",
          "The feast is delicious", "Held the feast they", "Delicious is the feast very",
          "In the hall tells where the feast is held."),
      ], "inferred")

    G("gr_used3", "Used to and be used to", 12, 1,
      "Distinguish used to do for past habits from be used to doing for being accustomed to something.", "tense", [
        q("I used to set off fireworks, but I don't anymore. Which sentence is correct?", "I used to set off fireworks",
          "I am used to set off fireworks", "I use to set off fireworks", "I am used setting fireworks",
          "Use used to followed by the base form of a verb for a past habit."),
        q("She is already accustomed to getting up early to see the lantern display. Which sentence is correct?", "She is used to getting up early for the lantern show",
          "She is used to get up early for the lantern show", "She used to getting up early",
          "She uses to getting up early",
          "Use be used to followed by a verb ending in -ing to describe being accustomed to something."),
        q("There used to ___ a temple here. Which word belongs in the blank?", "be",
          "being", "been", "was", "Used to is followed by the base form be."),
        q("Which sentence describes a past habit that no longer continues?", "People used to make lanterns at home",
          "People are used to making lanterns at home", "Lanterns are used to light the street",
          "The street is used to lanterns",
          "Used to make describes a past habit; be used to making means being accustomed to making them now."),
      ], "inferred")

    P("ph_pausehs", "Pausing between sense groups", 12, 1,
      "Pause between sense groups in longer sentences instead of separating every word.", "link", [
        q("On New Year's Eve, families share a feast. Where should the slash go for a natural pause?",
          "After Eve", "After On", "After share", "After every word",
          "On New Year's Eve is a time expression that forms one sense group; a pause can follow it."),
        q("Which reading shows pauses between sense groups?", "the long festival / in our town",
          "the / long / festival / in / our / town", "Insert a strong stop between festival and in", "Pause only after the article",
          "The noun phrase the long festival stays together, with a pause between phrases."),
        q("What is the purpose of pausing between sense groups?", "Read related words together as one group",
          "Make every consonant disappear", "Remove sentence-final intonation", "Read the whole sentence as one word",
          "Pauses separate sense groups instead of breaking apart every word."),
        q("After the fireworks, we went home. After which word is the first pause most natural?", "fireworks",
          "After", "we", "went", "After the fireworks is a time expression; a short pause can follow it."),
      ])

    F("fu_fest", "Talking about festivals", 12, 1,
      "Introduce a festival's origins and celebrations, and express an opinion about it.", "fu_view", [
        q("Which sentence introduces watching lanterns at the Lantern Festival?", "During the Lantern Festival people watch lanterns",
          "During the Lantern Fsetival people watch lanterns", "During the Lantern Festiavl people watch lanterns", "During the Lantern Fetival people watch lanterns",
          "During the Lantern Festival introduces when the activity happens."),
        q("Which sentence says that someone used to celebrate the festival with their grandparents?", "I used to spend the festival with my grandparents",
          "I am used to spend the festival", "Used to spending I the festival", "Spend used I am",
          "Use used to spend for a past habit."),
        q("Which sentence says that the festival's origin is connected to the moon?", "The origin of the festival is connected with the moon",
          "The origin of the festival is cnonected with the moon", "The origin of the festival is connecetd with the moon", "The origin of the festival is conected with the moon",
          "The phrase is connected with explains what the origin relates to."),
        q("Which sentence suggests decorating the classroom with lanterns?", "Let's decorate the classroom with lanterns",
          "Let's to decorate the classroom with lanterns", "Let's used to decorating", "Let's decorate the calssroom with lanterns",
          "Use Let's decorate to make a suggestion."),
      ])

    _f = "The Lantern Festival comes after the Lunar New Year. Families used to make lanterns at home. Now many people watch fireworks in the square and then share a small feast."
    R("rw_fest", "Reading about a festival", 12, 1,
      "Read a short passage about a festival and identify past and present celebrations.", "rw_detail", [
        q(_f + " When is the Lantern Festival?", "After the Lunar New Year", "Before the Lunar New Year", "On the Mid-Autumn Festival", "The time is not stated",
          "The passage says it comes after the Lunar New Year."),
        q(_f + " What did people use to do?", "Make lanterns at home", "Set off fireworks in the square", "Go running", "Write blogs",
          "The passage says they used to make lanterns at home."),
        q(_f + " What do many people do in the square now?", "Watch fireworks", "Make lanterns", "Repair a city wall", "Protect antelopes",
          "The passage says they watch fireworks in the square."),
        q(_f + " Which sentence matches the passage?", "Families used to make lanterns at home",
          "Families are used to make lanterns", "The festival comes before the Lunar New Year",
          "Nobody shares a feast",
          "Used to make describes the past habit of making lanterns."),
      ])

    R("wr_fest", "Writing a festival description", 12, 1,
      "Choose sentences that include the required details in a festival description.", "rw_write", [
        q("Required details: The Lantern Festival comes after New Year; people used to make lanterns and now watch fireworks. Which sentence includes all three?",
          "The Lantern Festival comes after the New Year, people used to make lanterns, and now they watch fireworks",
          "The Lantern Festival is old", "People watch fireworks", "Lanterns are red",
          "All three details must be included."),
        q("Which sentence correctly describes a past habit in the festival description?", "Children used to guess lantern riddles",
          "Children are used to guess lantern riddles", "Children use to guess lantern riddles",
          "Children used to guessing lantern riddles",
          "Use used to followed by the base form guess for a past habit."),
        q("Which sentence is suitable as the first sentence of the description?", "Let me introduce a festival in my hometown",
          "Let me introduce an festival in my hometown", "Let me itnroduce a festival in my hometown", "Let me introdcue a festival in my hometown",
          "A description can begin with Let me introduce."),
        q("Which sentence contains a prepositional phrase of place?", "We have the feast in the town square",
          "We have the feast happily", "The feast is delicious", "Have we the feast",
          "In the town square functions as an adverbial of place."),
      ])

    V("vo_moral", "Moral qualities", 12, 2,
      "Read and recognize virtue, honest, generous, and responsible.",
      [("virtue", "virtue"), ("honest", "honest"), ("generous", "generous"), ("responsible", "responsible")], "vo_soc")

    V("vo_virtue", "Good deeds", 12, 2,
      "Read and recognize kindness, respect, duty, and courage.",
      [("kindness", "kindness"), ("respect", "respect"), ("duty", "duty"), ("courage", "courage")], "vo_soc")

    G("gr_toattr", "Infinitives as modifiers and objects", 12, 2,
      "Use infinitives as modifiers or objects.", "toinf", [
        q("I have a duty ___ the guests. Which word belongs in the blank to say that I am responsible for helping?", "to help",
          "helping", "help", "helped", "Use to help after duty as a modifier."),
        q("She decided ___ the truth. Which word belongs in the blank?", "to tell",
          "telling", "tell", "told", "Use to tell as the object of decided."),
        q("Which sentence is correct?", "He is a person to respect",
          "He is a person respecting to", "He is a person respect", "He is a person to respected",
          "To respect modifies person."),
        q("We hope ___ more kindness. Which word belongs in the blank?", "to see",
          "seeing", "see", "seen", "Use to see as the object of hope."),
      ])

    G("gr_topurp", "Infinitives as adverbials of purpose", 12, 2,
      "Use in order to or to do to express purpose.", "toinf", [
        q("She stayed ___ the old man. Which word belongs in the blank to express that she stayed in order to help?", "to help",
          "helping", "help", "helped", "To help functions as an adverbial of purpose."),
        q("Which sentence expresses purpose?", "He got up early in order to catch the first bus",
          "He got up early catching the bus yesterday", "In order to catch, the bus got up",
          "He got up early to caught the bus",
          "In order to catch explains why he got up early."),
        q("___ honest, she told the teacher. Which opening belongs in the blank?", "To be",
          "Being to", "Be", "Been", "To be honest is an adverbial phrase that explains why she told the teacher."),
        q("In which sentence is the infinitive not expressing purpose?", "I want to leave",
          "I came to leave a message", "I opened the door to let her in", "She studied hard to pass",
          "In want to leave, the infinitive is the object. The infinitives in the other three sentences express purpose."),
      ])

    F("fu_moral", "Evaluating actions", 12, 2,
      "Evaluate whether an action is honest and responsible, and explain why.", "fu_view", [
        q("Which sentence praises a classmate for honestly returning a wallet?", "It was honest of you to return the wallet",
          "It not was honest of you to return the wallet", "It was hnoest of you to return the wallet", "It was honset of you to return the wallet",
          "It was honest of you to is used to praise someone."),
        q("Which sentence says that someone stayed in order to help?", "I stayed in order to help",
          "I stayed in order to helping", "I stayed helping to in order", "Help stayed I",
          "In order to help expresses purpose."),
        q("Which sentence says that respecting others is a virtue?", "Respect for others is a virtue",
          "Respect for others is an virtue", "Rsepect for others is a virtue", "Respcet for others is a virtue",
          "Is a virtue is used to make a statement about something."),
        q("A classmate admits a mistake, and you think that was responsible. What could you say?", "That was responsible of you",
          "That was rseponsible of you", "That was responsilbe of you", "That was reponsible of you",
          "That was responsible of you expresses approval."),
      ])

    _o = "After the trip, Mei found a wallet on the bus. She stayed there to wait for the owner. Her teacher said it was responsible of her to return it."
    R("rw_moral", "Reading about a good deed", 12, 2,
      "Read a short account and identify what the person did and how the teacher evaluated it.", "rw_main", [
        q(_o + " What did Mei find on the bus?", "A wallet", "A lantern", "A medal", "A book of poems",
          "The passage says she found a wallet."),
        q(_o + " Why did she stay?", "To wait for the owner", "To ride to the last stop", "To set off fireworks", "The reason is not stated",
          "The passage says she stayed to wait for the owner."),
        q(_o + " What did the teacher think of her?", "Returning the wallet was responsible", "She should not have interfered", "She should have kept the wallet", "The teacher did not comment",
          "The passage says it was responsible of her to return the wallet."),
        q(_o + " Which best describes the author's attitude?", "The author approves of Mei's action", "The author criticizes Mei for interfering", "The author only describes the bus", "The author worries that the owner spent the money but does not evaluate Mei",
          "The teacher's comment is approving, and the account does not criticize Mei."),
      ])

    R("wr_moral", "Writing a short review", 12, 2,
      "Choose the sentence that includes the required points in a short review.", "rw_write", [
        q("Required points: found a wallet, waited for its owner, and the teacher called the action responsible. Which sentence includes all three?",
          "Mei found a wallet, waited for the owner, and her teacher said she was responsible",
          "Mei found a wallet", "The bus was crowded", "Teachers are busy",
          "All three required points must be included."),
        q("Which sentence correctly uses an infinitive of purpose in the review?", "She went back to return the wallet",
          "She went back to returned the wallet", "She went back returning the wallet yesterday's purpose",
          "To returned the wallet she went",
          "Use the base form return after to."),
        q("Which sentence is suitable as the first sentence of the review?", "Mei made a choice that shows kindness",
          "Mei made a choice that show kindness", "Mei made an choice that shows kindness", "Mei made a choice that shows knidness",
          "A review can begin by pointing out that Mei made a choice."),
        q("In which sentence does the infinitive modify a noun?", "She had a chance to help",
          "She had a chance helping to", "To help she chance had", "Help to chance a she",
          "To help modifies chance."),
      ])

    V("vo_region", "Cultural diversity", 12, 3,
      "Read and recognize diversity, ethnic, region, and minority.",
      [("diversity", "diversity"), ("ethnic", "related to an ethnic group"), ("region", "region"), ("minority", "minority group")], "vo_soc")

    V("vo_ethnic", "Cultural customs", 12, 3,
      "Read and recognize costume, cuisine, belief, and greeting.",
      [("costume", "costume"), ("cuisine", "cuisine"), ("belief", "belief"), ("greeting", "greeting")], "vo_soc")

    G("gr_report", "Reported speech", 12, 3,
      "Change direct speech into reported speech, adjusting pronouns, time expressions, and tenses.", "reported", [
        q("Change \"He said, 'I am tired.'\" to reported speech. Which sentence is correct?", "He said that he was tired",
          "He said that I am tired", "He said that he is tired now yesterday", "He said me tired",
          "Said is in the past tense, so I am changes to he was in reported speech."),
        q("She said, \"I will visit you tomorrow.\" Which sentence correctly reports this?",
          "She said that she would visit me the next day",
          "She said that she will visit you tomorrow", "She said that I would visit you tomorrow",
          "She said that she visits me tomorrow",
          "Will changes to would, tomorrow to the next day, and you changes to me for this listener."),
        q("Tom said, \"We saw a festival yesterday.\" Which sentence is correct?",
          "Tom said that they had seen a festival the day before",
          "Tom said that we saw a festival yesterday", "Tom said that they saw a festival tomorrow",
          "Tom said that they have seen a festival yesterday",
          "Saw shifts back to had seen, and yesterday changes to the day before."),
        q("How can \"May I use your pen?\" be reported to someone else?", "She asked if she could use my pen",
          "She asked if she can use your pen", "She asked that use your pen", "She said me to pen",
          "Use asked if to report a request; may changes to could."),
      ])

    G("gr_thatomit", "Omitting that in reported speech", 12, 3,
      "Omit that after said while keeping statement word order.", "reported", [
        q("Which sentence is still correct when that is omitted?", "He said he was ready",
          "He said was he ready", "He said that was he ready", "He said he is ready yesterday",
          "That can be omitted after said, but the word order remains he was ready."),
        q("She told me ___ she liked the costume. Which word can go in the blank?", "that",
          "what", "which", "who", "That introduces the object clause after told me and can also be omitted."),
        q("Which sentence has incorrect word order?", "He said that was the food delicious",
          "He said the food was delicious", "He said that the food was delicious", "He told me the food was delicious",
          "Reported speech uses statement word order: the food was delicious."),
        q("They said they ___ the greeting the day before. Which word belongs in the blank?", "had learned",
          "have learned", "learn", "are learning", "After said, learned shifts back to had learned."),
      ], "inferred")

    F("fu_culture", "Comparing cultural differences", 12, 3,
      "Compare clothing, food, and greetings in different regions while remaining polite.", "fu_view", [
        q("Which sentence says that the clothing in this region differs from that in the speaker's hometown?", "The costumes in this region are different from those in my hometown",
          "The costumes in this region are different of those in my hometown", "The costumes in this region are dfiferent from those in my hometown", "The costumes in this region are differnet from those in my hometown",
          "Use different from to make a comparison."),
        q("Which sentence correctly reports the guide's words, \"I like this cuisine\"?", "The guide said that he liked that cuisine",
          "The guide said that I like this cuisine", "The guide said that he likes this cuisine tomorrow",
          "The guide told that like he cuisine",
          "In reported speech, I like changes to he liked."),
        q("Which sentence politely asks whether photos may be taken of a belief or custom?", "Could you tell me if I may take photos",
          "Could you tell me if I may taked photos", "Could you tell me if I may to take photos", "Could you tell me if I may take pohtos",
          "Could you tell me if is a polite way to ask."),
        q("Which sentence says that a different greeting does not mean less respect?", "A different greeting does not mean less respect",
          "A different greeting doe not mean less respect", "A dfiferent greeting does not mean less respect", "A differnet greeting does not mean less respect",
          "Does not mean is used to clarify an idea."),
      ])

    _c = "The guide said that the costumes were made by a local minority group. He also said they had learned the dance the year before. Visitors may watch, but they should ask before taking photos."
    R("rw_culture", "Reading about cultural customs", 12, 3,
      "Read a short cultural description and identify who made the costumes and the rules for taking photos.", "rw_detail", [
        q(_c + " Who made the costumes?", "A local minority group", "The guide", "The visitors", "The passage does not say",
          "The passage says they were made by a local minority group."),
        q(_c + " When did they learn the dance?", "The year before", "That day", "The following year", "Ten years later",
          "The passage says they had learned it the year before."),
        q(_c + " What should visitors do before taking photos?", "Ask first", "Take photos right away", "Put on the costumes", "Leave",
          "The passage says visitors should ask before taking photos."),
        q(_c + " Which sentence matches the passage?", "Visitors should ask before taking photos",
          "Visitors must take photos", "The guide made the costumes", "The dance will be learned next year",
          "The rule is to ask before taking photos."),
      ])

    R("wr_culture", "Writing cultural notes", 12, 3,
      "Choose a sentence that includes the required details in cultural notes and uses reported speech.", "rw_write", [
        q("Required details: a local group made the costumes, the dance was learned the year before, and visitors should ask before taking photos. Which sentence includes all three?",
          "The costumes were made by a local group, they had learned the dance the year before, and visitors should ask before taking photos",
          "The costumes are colourful", "The dance is long", "Visitors like photos",
          "All three required details must be included."),
        q("Which sentence correctly reports the guide's words, \"We made these costumes\"?",
          "The guide said that they had made those costumes",
          "The guide said that we made these costumes", "The guide said that they make these costumes tomorrow",
          "The guide said that made they costumes",
          "After said, we made changes to they had made."),
        q("Which sentence is suitable as the first sentence of the notes?", "Today I learned about a local ethnic group",
          "Today I learned about an local ethnic group", "Today I laerned about a local ethnic group", "Today I learend about a local ethnic group",
          "The notes can begin with Today I learned about."),
        q("Which sentence remains correct when that is omitted?", "He said the food was special",
          "He said was the food special", "He said that was the food special", "He said the food is special yesterday",
          "After omitting that, keep statement word order: the food was special."),
      ])

    V("vo_space", "Space exploration", 12, 4,
      "Read and recognize astronaut, orbit, rocket, and universe.",
      [("astronaut", "astronaut"), ("orbit", "orbit"), ("rocket", "rocket"), ("universe", "universe")], "vo_soc")

    V("vo_planet", "Spaceflight", 12, 4,
      "Read and recognize planet, satellite, gravity, and mission.",
      [("planet", "planet"), ("satellite", "satellite"), ("gravity", "gravity"), ("mission", "mission")], "vo_soc")

    G("gr_toform", "Infinitives as subjects and subject complements", 12, 4,
      "Use an infinitive as the subject or complement, or use it as a formal subject.", "toinf", [
        q("___ a rocket is difficult. Which form belongs in the blank to make an infinitive the subject?", "To launch",
          "Launch", "Launching to", "Launched", "Use To launch as the subject at the beginning of the sentence."),
        q("Which sentence uses it as a formal subject?", "It is hard to leave the planet",
          "To leave the planet is hard it", "Hard is to leave it the planet", "It hard to leave",
          "It is the formal subject; to leave the planet is the actual subject."),
        q("Her dream is ___ an astronaut. Which form belongs in the blank?", "to become",
          "becoming to", "become", "became", "Use to become as the complement of dream."),
        q("Which sentence is correct?", "It takes years to train for a mission",
          "It takes years train for a mission", "It takes years to trained for a mission",
          "Takes it years to train for a mission",
          "In It takes years to train, to train is the actual subject."),
      ])

    G("gr_bare", "Infinitives without to", 12, 4,
      "Omit to after verbs such as make, let, see, and hear, and restore it in passive constructions.", "toinf", [
        q("The teacher made us ___ the report. Which form belongs in the blank?", "rewrite",
          "to rewrite", "rewriting", "rewrote", "Omit to from the infinitive after make plus an object."),
        q("Which sentence is correct?", "We were made to check the data",
          "We were made check the data", "We were made checking the data", "We made to were check",
          "Use make someone do in the active voice, but restore to in the passive: were made to check."),
        q("I saw the rocket ___. Which form means that I saw the rocket rise and does not use to?", "rise",
          "to rise", "rose", "risen", "Omit to from the infinitive used as an object complement after see."),
        q("Which sentence must keep to?", "It is important to wear a helmet",
          "Let me wear a helmet", "I heard her sing", "They made him wait",
          "Do not omit to after important. To can be omitted after let, hear, and make."),
      ], "inferred")

    F("fu_space", "Talking about space missions", 12, 4,
      "Describe planned or intended space missions.", "fu_plan", [
        q("Which sentence says that becoming an astronaut is difficult?", "It is difficult to become an astronaut",
          "Difficult to become is it an astronaut", "Become an astronaut difficult", "It difficult become",
          "It is difficult to become uses it as a formal subject."),
        q("Which sentence says that the teacher made the students look up information about a satellite?", "The teacher made us check the satellite data",
          "The teacher made us to check the satellite data", "The teacher made us checking data",
          "Made the teacher us to check",
          "Use the base form check after made us."),
        q("Which sentence says that the mission is to enter orbit?", "The mission is to enter orbit",
          "The mission is enter to orbit", "Orbit is to mission", "To enter orbit the mission is it",
          "Use to enter orbit as the subject complement."),
        q("Which sentence invites classmates to watch a rocket launch together?", "Shall we watch the rocket launch",
          "Shall we watch the rcoket launch", "Shall we watch the rocekt launch", "We watched tomorrow",
          "Use Shall we watch to make an invitation."),
      ])

    _s = "It is not easy to become an astronaut. The next mission is to test a new satellite. Our teacher made us read a short article about gravity."
    R("rw_space", "Reading about space exploration", 12, 4,
      "Read a short passage about space and summarize the mission and the teacher's instructions.", "rw_main", [
        q(_s + " Is it easy to become an astronaut?", "No, it is not easy", "Yes, it is very easy", "The passage does not say", "Only children find it easy",
          "The passage says it is not easy."),
        q(_s + " What is the next mission?", "Test a new satellite", "Land on the Sun", "Remove gravity", "Repair a lantern",
          "The passage says the mission is to test a new satellite."),
        q(_s + " What did the teacher ask the students to do?", "Read a short article about gravity", "Launch a rocket", "Remove a helmet", "Write a code",
          "The passage says the teacher made them read a short article about gravity."),
        q(_s + " Which sentence matches the passage?", "The teacher made the students read an article",
          "The teacher made the students to read an article", "Becoming an astronaut is easy",
          "The mission is to close the school",
          "Do not use to after made us read."),
      ])

    R("wr_space", "Writing space notes", 12, 4,
      "Choose sentences that include the required details in space notes.", "rw_write", [
        q("Required points: becoming an astronaut is difficult, the mission is to test a satellite, and the teacher asked the students to read. Which sentence includes all three?",
          "It is not easy to become an astronaut, the mission is to test a satellite, and the teacher made us read",
          "It is not easy", "Satellites are useful", "We like space",
          "All three required points must be included."),
        q("Which sentence correctly uses a formal subject in the notes?", "It takes courage to join a mission",
          "It takes courage join a mission", "Takes it courage to join", "Courage takes to join it a mission",
          "It takes courage to join is the complete construction."),
        q("Which sentence is suitable as the title of the notes?", "What I learned about the mission",
          "What I laerned about the mission", "What I learend about the mission", "What I lerned about the mission",
          "The title can be What I learned about the mission."),
        q("Which sentence correctly restores to in the passive voice?", "We were made to rewrite the notes",
          "We were made rewrite the notes", "We were made rewriting the notes", "Were made we rewrite to",
          "Use to rewrite after were made."),
      ])

    V("vo_money", "Money and value", 12, 5,
      "Read and recognize value, wealth, loan, and bargain.",
      [("value", "value"), ("wealth", "wealth"), ("loan", "loan"), ("bargain", "a good deal")], "vo_soc")

    V("vo_worth", "Spending choices", 12, 5,
      "Read and recognize worth, budget, debt, and charity.",
      [("worth", "having value"), ("budget", "budget"), ("debt", "debt"), ("charity", "charity")], "vo_soc")

    G("gr_modperf", "Modal verbs with have done", 12, 5,
      "Use must, could, or should with have done to make judgments about the past or express regret.", "modal", [
        q("The bag is no longer on the table. Which sentence says she must have taken it?", "She must have taken it",
          "She must take it", "She must has taken it", "She must had taken it",
          "Use must have taken for a confident inference about the past."),
        q("He could have asked for help at the time, but he did not. Which sentence is correct?", "He could have asked for help",
          "He could ask for help yesterday now", "He could has asked for help", "He can have asked tomorrow",
          "Use could have asked for something that was possible but did not happen."),
        q("Which sentence says that someone should not have borrowed so much money?", "You should not have borrowed so much",
          "You should not borrowed so much", "You should not have borrow so much",
          "You must not to have borrowed",
          "Use should not have borrowed to express regret or criticism about a past action."),
        q("Which sentence expresses an uncertain possibility about the past?", "The wallet could have been lost on the bus",
          "The wallet must be on the bus now", "The wallet can lost", "The wallet should loses",
          "Could have been lost expresses a possibility about the past."),
      ])

    G("gr_wouldrather", "The subjunctive with would rather", 12, 5,
      "Use would rather with the past tense to express a wish contrary to present facts.", "modal", [
        q("Which sentence says that I would prefer you to tell me the truth now?", "I would rather you told me the truth now",
          "I would rather you tell me the truth now", "I would rather you to tell me",
          "I would rather you had tell me now",
          "Use the past-tense told after would rather for a wish about the present."),
        q("Which sentence says that someone wishes they had not bought it?", "I would rather I had not bought it",
          "I would rather I did not bought it", "I would rather not buying it yesterday",
          "I would rather I buy it not",
          "Use had not bought for a wish contrary to a past fact."),
        q("She would rather ___ at home than go out. Which word belongs in the blank?", "stay",
          "staying", "to stay", "stayed", "Use the base form stay after would rather, as in stay rather than go."),
        q("Which sentence uses the past tense in the clause after would rather?", "I would rather you came tomorrow",
          "I would rather to come tomorrow", "I would rather coming tomorrow", "I rather would you to come",
          "Came is the past-tense form in the clause and expresses a wish."),
      ], "inferred")

    F("fu_money", "Talking about value and spending", 12, 5,
      "Share opinions about spending, budgeting, and charity, and explain the reasons.", "fu_view", [
        q("Which sentence says that a bargain is not worth buying?", "This bargain is not worth buying",
          "This bargain is not worth to buy", "Worth buying is not this", "This bragain is not worth buying",
          "Use a verb ending in -ing after worth."),
        q("Which sentence says that the wallet must have been left on the bus?", "You must have left the wallet on the bus",
          "You must leave the wallet on the bus yesterday", "You must had left the wallet",
          "Must have you left the wallet",
          "Use must have left to make an inference about the past."),
        q("Which sentence suggests making a budget before taking out a loan?", "You should make a budget before you take a loan",
          "You should have make a budget tomorrow", "You should maked a budget before you take a loan", "You should to make a budget before you take a loan",
          "Use You should make a budget to give advice."),
        q("Which sentence says that giving some money to charity is more valuable?", "Giving some money to charity is of greater value",
          "Giving some money to cahrity is of greater value", "Giving some money to chartiy is of greater value", "Giving some money to chrity is of greater value",
          "Is of greater value compares the value of two choices."),
      ])

    _y = "Tom bought a coat because it looked like a bargain. Later he found a hole in it. His sister said he should have checked the pockets and kept to his budget."
    R("rw_money", "Reading about a purchase", 12, 5,
      "Read an account of a purchase and identify the sister's advice and the lesson implied by the author.", "rw_detail", [
        q(_y + " Why did Tom buy the coat?", "It looked like a bargain", "It was expensive", "His sister told him to buy it", "It had no holes",
          "The passage says it looked like a bargain."),
        q(_y + " What did he find later?", "A hole", "A loan", "A medal", "A ticket",
          "The passage says he found a hole."),
        q(_y + " What did his sister think he should have done?", "Checked the pockets and kept to his budget", "Bought another coat", "Donated the coat", "Nothing",
          "The passage says he should have checked the pockets and kept to his budget."),
        q(_y + " Which sentence matches the passage?", "He should have checked the coat",
          "He must check the coat tomorrow in the past", "The coat had no hole", "His sister bought the coat",
          "Should have checked describes something that ought to have been done but was not."),
      ])

    R("wr_money", "Writing a reflection on spending", 12, 5,
      "Choose the sentence that includes the required details in a reflection on spending.", "rw_write", [
        q("Required details: it looked like a bargain, it later had a hole, and it should have been checked. Which sentence includes all three?",
          "It looked like a bargain, but there was a hole, and I should have checked it",
          "It looked cheap", "There was a hole", "Budgets are useful",
          "All three required details must be included."),
        q("Which sentence correctly says that someone should not have taken out the loan?", "I should not have taken the loan",
          "I should not took the loan", "I should not have take the loan", "I must not to have take",
          "Should not have taken expresses regret about borrowing."),
        q("Which sentence is suitable as the first sentence of a reflection?", "I learned a lesson about value",
          "I learned an lesson about value", "I laerned a lesson about value", "I learend a lesson about value",
          "A reflection can begin with I learned a lesson."),
        q("Which sentence says the speaker wishes they had not bought the coat?", "I would rather I had not bought the coat",
          "I would rather I did not bought the coat", "I would rather not buying the coat yesterday",
          "Rather I would bought not",
          "Use had not bought for a wish contrary to a past fact."),
      ])
