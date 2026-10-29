# -*- coding: utf-8 -*-
"""People's Education Press (2019), Optional Compulsory Book 3. Unit names follow the commonly used table of contents; book assignment pending verification."""
from enh_tx import V, G, F, R, q


def load():
    V("vo_art", "Art", 15, 1,
      "Recognize sculpture, gallery, exhibition, and visual.",
      [("sculpture", "sculpture"), ("gallery", "art gallery"), ("exhibition", "exhibition"), ("visual", "visual")], "vo_mind")

    V("vo_gallery", "Art Criticism", 15, 1,
      "Recognize brush, canvas, realistic, and abstract.",
      [("brush", "brush"), ("canvas", "canvas"), ("realistic", "realistic"), ("abstract", "abstract")], "vo_mind")

    G("gr_invneg", "Inversion after Negative Adverbs", 15, 1,
      "Use partial inversion when a negative adverb appears at the beginning of a sentence.", "invert", [
        q("Never ___ such a sculpture. Which form means that I have never seen one?", "have I seen",
          "I have seen", "did I saw", "I saw", "When “Never” begins the sentence, use “have I seen.”"),
        q("Which sentence uses inversion correctly?", "Seldom does she miss an exhibition",
          "Seldom she does miss an exhibition", "Seldom does she misses an exhibition",
          "Seldom misses she an exhibition",
          "With “Seldom” at the beginning, put “does” before the subject and use the base verb “miss.”"),
        q("Little ___ the painter was so young. Which form completes the sentence?", "did we know",
          "we knew", "we did know", "knew we", "When “Little” begins the sentence, use “did we know.”"),
        q("Which sentence does not use inversion and therefore does not fit after a negative word at the beginning?", "I have never seen the canvas",
          "Never have I seen the canvas", "Rarely do we see such colours", "Not until then did he speak",
          "In “I have never seen,” the negative word is in the middle, so there is no inversion at the beginning."),
      ])

    G("gr_hardly", "Inversion with hardly", 15, 1,
      "Use “Hardly had ... when” to express that one event happened immediately after another.", "invert", [
        q("Hardly ___ the gallery when the talk began. Which form completes the sentence?", "had we entered",
          "we had entered", "did we enter", "have we entered", "After “Hardly” at the beginning, use “had we entered,” followed by “when.”"),
        q("Which sentence is correct?", "Hardly had she finished the painting when the visitors arrived",
          "Hardly she had finished the painting when the visitors arrived",
          "Hardly had she finished the painting than the visitors arrived",
          "Hardly finished she the painting when visitors",
          "Use “Hardly had ... when,” not “than.”"),
        q("No sooner ___ down than the lights went out. Which form completes the sentence?", "had the artist sat",
          "the artist had sat", "did the artist sat", "sat the artist",
          "After “No sooner,” use “had the artist sat,” followed by “than.”"),
        q("Which tense is usually used in the when-clause of a “Hardly” inversion?", "Simple past", "Future", "Present perfect", "Base form",
          "“When the visitors arrived” uses the simple past."),
      ])

    F("fu_art", "Describing Artworks", 15, 1,
      "Describe a painting or sculpture and say whether it is realistic or abstract.", "fu_desc", [
        q("Which sentence says that you have never seen a sculpture like this, using inversion?", "Never have I seen such a sculpture",
          "Never I have seen such a sculpture", "Seen have I never such", "Never saw I have such",
          "“Never have I seen” uses partial inversion."),
        q("Which sentence says the talk began as soon as we entered the gallery?", "Hardly had we entered the gallery when the talk began",
          "Hardly we had entered the gallery when the talk began",
          "Hardly had we entered the gallery than the talk began", "Entered hardly we when began",
          "Hardly had we entered when."),
        q("Which sentence says that the painting is abstract?", "The painting is abstract rather than realistic",
          "The painting are abstract rather than realistic", "The painting is abstract rather than raelistic", "The painting is abstract rather than realisitc",
          "“Rather than” contrasts two styles."),
        q("Which sentence is a suitable first step for looking at an exhibition?", "First, look at the whole canvas",
          "First, look at the whole cnavas", "Look whole the canvas first does", "First, look at the whole canavs",
          "Use “First” to introduce the first step."),
      ])

    _a = "Never have I seen such bright colours. Hardly had we entered the gallery when a guide began to explain the sculpture. The painting is abstract, while the statue is realistic."
    R("rw_art", "Reading About Art", 15, 1,
      "Infer how the painting and statue differ and identify the sentence that uses inversion.", "rw_infer", [
        q(_a + " How did the author feel about the colours?", "I had never seen such vivid colours", "They seemed too dark", "The author did not see them", "The author only liked the statue",
          "Never have I seen such bright colours."),
        q(_a + " When did the explanation begin?", "As soon as they entered the gallery", "After they left", "The next day", "There was no explanation",
          "Hardly had we entered when a guide began."),
        q(_a + " How do the painting and statue differ?", "The painting is abstract, while the statue is realistic", "Both are abstract", "Both are realistic", "The passage does not compare them",
          "abstract, while the statue is realistic."),
        q(_a + " Which sentence uses inversion?", "Never have I seen such bright colours",
          "The painting is abstract", "The statue is realistic", "A guide began to explain",
          "“Never have I seen” places the auxiliary before the subject."),
      ])

    R("wr_art", "Writing an Exhibition Note", 15, 1,
      "Choose a note that includes all the required points.", "rw_write_s", [
        q("Key points: never seen these colours before; the talk began as soon as they entered; the painting is abstract and the statue is realistic. Which sentence includes all three?",
          "Never have I seen such colours, hardly had we entered when the talk began, and the painting is abstract while the statue is realistic",
          "The colours are bright", "The guide spoke", "I like art",
          "All three points must be included."),
        q("Which sentence correctly uses negative-adverb inversion in a note?", "Rarely do we see this kind of brushwork",
          "Rarely we do see this kind of brushwork", "Rarely does we see this kind", "See we rarely this kind",
          "In “Rarely do we see,” the verb stays in its base form."),
        q("Which sentence is suitable as the first sentence of a note?", "This note records one visit to a gallery",
          "This note record one visit to a gallery", "This note records one visit to an gallery", "This note rceords one visit to a gallery",
          "A note can begin with “This note records ...”."),
        q("Which sentence uses “Hardly” correctly?", "Hardly had the talk ended when we left",
          "Hardly the talk had ended when we left", "Hardly had the talk ended than we left",
          "Hardly ended the talk when we",
          "Use “Hardly had ... when.”"),
      ])

    V("vo_lifestyle", "Healthy Living", 15, 2,
      "Recognize lifestyle, stress, routine, and balance.",
      [("lifestyle", "lifestyle"), ("stress", "stress"), ("routine", "daily routine"), ("balance", "balance")], "vo_mind")

    V("vo_stressw", "Mind and Body Habits", 15, 2,
      "Recognize anxiety, nutrition, sufficient, and refresh.",
      [("anxiety", "anxiety"), ("nutrition", "nutrition"), ("sufficient", "enough"), ("refresh", "restore energy")], "vo_mind")

    G("gr_invonly", "Inversion with only, so, and neither", 15, 2,
      "Use inversion when a sentence begins with only plus an adverbial, so, or neither.", "invert", [
        q("Only then ___ how tired he was. Which form completes the sentence?", "did he realise",
          "he realised", "he did realise", "realised he", "When “Only then” begins a sentence, use “did he realise.”"),
        q("I need sufficient sleep. The other person does too. Which response is correct?", "So do I",
          "So I do", "So did I am", "Neither do I", "Use “So do I” to agree that you also need sufficient sleep. “So I do” emphasizes that you really do; it is not inverted."),
        q("He cannot keep the routine. She cannot either. Which sentence is correct?", "Neither can she",
          "Neither she can", "So can she", "Neither can't she",
          "Use “Neither can she” to agree with a negative statement."),
        q("Which sentence is correct?", "Only after a walk did she feel refreshed",
          "Only after a walk she felt refreshed", "Only after a walk did she felt refreshed",
          "Only she felt refreshed after a walk as inversion",
          "When “Only after a walk” is moved to the beginning, use “did she feel.”"),
      ])

    G("gr_invthere", "Inversion with there and Place Phrases", 15, 2,
      "Begin a sentence with there or a place adverb and put the subject after the verb.", "invert", [
        q("There ___ a quiet garden behind the gym. Which form completes the sentence?", "stands",
          "stand", "standing", "is stand", "The subject “a quiet garden” is singular, so use “stands.”"),
        q("Which sentence uses inversion?", "In front of the library stands an old tree",
          "An old tree stands in front of the library", "Stands in front an old tree the",
          "In front of the library an old tree stands it",
          "The place phrase begins the sentence, and “stands” comes before the subject."),
        q("On the wall ___ two posters about nutrition. Which form completes the sentence?", "hang",
          "hangs", "hanging", "is hang", "The subject “two posters” is plural, so use “hang.”"),
        q("What typically begins this type of inverted sentence?", "A place phrase or there", "A negative person's name", "only plus a subject", "so plus an adjective",
          "A place adverbial or “there” moves to the beginning, and the subject follows the verb."),
      ], "inferred")

    F("fu_healths", "Discussing Healthy Habits", 15, 2,
      "Discuss stress, sleep, and nutrition, and give advice supported by reasons.", "fu_argue", [
        q("Which sentence says that he did not realise his stress until then?", "Only then did he realise his stress",
          "Only then he realised his stress", "Then only realised he stress", "Did he realise only then not",
          "Only then did he realise."),
        q("Someone says they need sufficient sleep. You do too. What should you say?", "So do I",
          "So I do if you mean I really do and the grammar is the short answer of agreement wait no",
          "Neither do I", "So did sleep I",
          "Agree with the other person's need by saying “So do I.”"),
        q("Which sentence says there is a tree in front of the library, using inversion?", "In front of the library stands an old tree",
          "In front of the library an old tree stands quietly as normal order", "Stands an old tree front in",
          "There stand an old tree",
          "With a place phrase at the beginning, the verb comes before the singular subject. “There stand” does not agree with a singular subject."),
        q("Which sentence recommends using a walk to reduce anxiety?", "A short walk can refresh you and reduce anxiety",
          "A short walk can refreshed you and reduce anxiety", "A short walk can to refresh you and reduce anxiety", "A short walk can rferesh you and reduce anxiety",
          "“Can refresh” gives the reason for the recommendation."),
      ])

    _h = "Only after he changed his routine did Tom sleep well. He says he needs sufficient nutrition, and so does his sister. Behind the dormitory stands a garden where they walk."
    R("rw_healths", "Reading About Healthy Habits", 15, 2,
      "Identify the result of changing a habit and the person referred to by so-inversion.", "rw_argue", [
        q(_h + " When did Tom finally sleep well?", "After changing his routine", "Before changing it", "Only while eating in the garden", "The passage does not say",
          "Only after he changed his routine."),
        q(_h + " What does Tom's sister also need?", "Sufficient nutrition, like Tom", "No nutrition", "Only a walk", "He does not have a sister",
          "“So does his sister” refers to the earlier statement that he needs sufficient nutrition."),
        q(_h + " What is behind the dormitory?", "A garden", "A hospital", "An abstract painting", "Nothing", "The passage says a garden stands behind the dormitory."),
        q(_h + " Which sentence uses inversion after “only”?", "Only after he changed his routine did Tom sleep well",
          "He says he needs sufficient nutrition", "Behind the dormitory stands a garden", "They walk in the garden",
          "“Did Tom sleep” is inverted because the “only” adverbial comes first."),
      ])

    R("wr_healths", "Writing Health Advice", 15, 2,
      "Choose advice that includes all the required points.", "rw_write_s", [
        q("Key points: he slept well only after changing his routine; his sister also needs nutrition; there is a garden behind the dormitory. Which sentence includes all three?",
          "Only after he changed his routine did he sleep well, so does his sister need good nutrition, and behind the dormitory stands a garden",
          "He sleeps well", "His sister is busy", "Gardens are quiet",
          "All three points must be included."),
        q("Which sentence correctly uses inversion after “only” in advice?", "Only by walking did she reduce her anxiety",
          "Only by walking she reduced her anxiety", "Only by walking did she reduced her anxiety",
          "Reduced she only by walking",
          "Use “Only by walking did she reduce ...”."),
        q("Which sentence is suitable as the first sentence of advice?", "A balanced routine can reduce stress",
          "A balanced routine can reduced stress", "A balanced routine can to reduce stress", "A blaanced routine can reduce stress",
          "Advice can begin with a general point."),
        q("Someone says they cannot go to bed early. You cannot either. Which sentence is correct?", "Neither can I",
          "So can I", "Neither I can", "Neither can't I",
          "Use “Neither can I” to agree with a negative statement."),
      ])

    V("vo_climate", "Environmental Protection", 15, 3,
      "Recognize climate, carbon, emission, and renewable.",
      [("climate", "climate"), ("carbon", "carbon"), ("emission", "emission"), ("renewable", "renewable")], "vo_mind")

    V("vo_pollute", "Pollution", 15, 3,
      "Recognize pollution, drought, policy, and sustainable.",
      [("pollution", "pollution"), ("policy", "policy"), ("sustainable", "sustainable"), ("melt", "melt")], "vo_mind")

    G("gr_cleft", "Cleft Sentences", 15, 3,
      "Use it is or it was, the emphasized element, and that or who to form a cleft sentence.", "emph", [
        q("The policy, not the slogan, changed the emissions. Which sentence correctly emphasizes the policy?", "It is the policy that changes the emissions",
          "It is the policy which changes the emissions as a cleft", "It was the policy what changed",
          "That it is the policy changes",
          "Use “It is ... that” to form a cleft sentence."),
        q("Lin submitted the report yesterday. Which sentence correctly emphasizes Lin?", "It was Lin who submitted the report",
          "It was Lin which submitted the report", "It was Lin whom submitted the report",
          "It was Lin submitted the report",
          "Use who or that to emphasize a person; do not omit it."),
        q("She found the problem in the lab. Which sentence correctly emphasizes the place?", "It was in the lab that she found the problem",
          "It was in the lab where she found the problem", "It was in the lab which she found the problem",
          "It was the lab where she found as if it were only a relative clause without It was matching",
          "To emphasize a place adverbial, use “It was in the lab that,” not “where.”"),
        q("What should remain after removing “It is” or “It was” and “that” from a cleft sentence?", "A complete sentence",
          "Only a noun", "A question", "A sentence with no verb",
          "Removing the frame from “It was Lin that submitted it” leaves the complete sentence “Lin submitted it.”"),
      ])

    G("gr_cleftvs", "Cleft Sentences and Relative Clauses", 15, 3,
      "Distinguish cleft sentences using “It is ... that” from easily confused relative clauses.", "emph", [
        q("Which sentence is a cleft sentence?", "It was the drought that forced them to move",
          "It is a policy that few people like", "It is a problem which we can solve",
          "The policy that he wrote is new",
          "After removing “It was” and “that,” “the drought forced them to move” is still complete, so it is a cleft sentence."),
        q("Which sentence contains a relative clause?", "It is a report that explains carbon emissions",
          "It was carbon that the report explained", "It is today that the policy starts",
          "It was she who wrote the report",
          "In “a report that explains,” that is the subject of the relative clause; removing the whole clause would not leave a complete sentence."),
        q("It was in 2020 ___ the emissions fell. Which word completes this cleft sentence emphasizing time?", "that",
          "when", "which", "where", "Use “that,” not “when,” even when a cleft sentence emphasizes time."),
        q("What is one way to identify a cleft sentence?", "The sentence remains complete after removing “It is” or “It was” and “that”",
          "Every sentence with “that” has a relative clause", "Every sentence beginning with “It” is emphatic", "It must use “which”",
          "A cleft sentence can be reduced to a complete ordinary sentence."),
      ], "inferred")

    F("fu_env", "Discussing Environmental Policy", 15, 3,
      "Discuss emissions, drought, and policy, and emphasize the factor that actually makes a difference.", "fu_argue", [
        q("Which sentence emphasizes that renewable energy reduced emissions?", "It is renewable energy that reduces the emissions",
          "It is renewable energy which reduces the emissions in a cleft", "Renewable energy that it is reduces",
          "It is renewable energy what reduces",
          "Use “that” in a cleft sentence."),
        q("Which sentence says that drought forced people to move?", "It was the drought that forced people to move",
          "It was the drought which forced people as a relative only", "The drought it was forced people",
          "Forced the drought people that",
          "Use “It was the drought that forced ...”."),
        q("Which sentence recommends that the policy be sustainable?", "The policy should be sustainable",
          "The policy should be ssutainable", "The policy should be sustainalbe", "The policy should be sutainable",
          "Use “should be sustainable” to express a recommendation."),
        q("Which sentence emphasizes a time and distinguishes a cleft sentence from a relative clause?", "It was last winter that the ice melted faster",
          "It was a winter that nobody liked", "Last winter melted the ice", "It was last winter when the ice as a cleft wrongly",
          "Use “that,” not “when,” to emphasize a time in a cleft sentence."),
      ])

    _e = "It is the new policy that cuts carbon emissions. It was the long drought that made the lake smaller. Renewable energy is useful, but the policy decides how fast it is used."
    R("rw_env", "Reading About the Environment", 15, 3,
      "Identify the factor the author believes is decisive, along with the claim and supporting evidence.", "rw_argue", [
        q(_e + " What is cutting carbon emissions?", "The new policy", "Drought", "The lake", "The passage does not say", "The passage says the new policy cuts emissions."),
        q(_e + " What made the lake smaller?", "A long drought", "The new policy", "Renewable energy", "There was no cause",
          "It was the long drought that made the lake smaller."),
        q(_e + " What does the author say determines how quickly renewable energy is used?", "Policy", "Only the weather", "The lake itself", "Nothing determines it",
          "the policy decides how fast."),
        q(_e + " Which statement best matches the passage's argument?", "Renewable energy is useful, but policy determines how quickly it is adopted",
          "Drought is more useful than policy", "Emissions are no longer connected to policy", "The policy caused the lake to shrink",
          "The claim is that renewable energy is useful, but policy determines the pace of its use."),
      ])

    R("wr_env", "Writing an Environmental Comment", 15, 3,
      "Choose a comment that includes all the required points.", "rw_write_s", [
        q("Key points: policy cuts emissions; drought shrank the lake; policy determines the pace. Which sentence includes all three?",
          "It is the policy that cuts emissions, it was the drought that made the lake smaller, and the policy decides the speed",
          "The policy is new", "The lake is smaller", "Energy is renewable",
          "All three points must be included."),
        q("Which sentence correctly emphasizes a person in a comment?", "It was Dr Lin who explained the data",
          "It was Dr Lin which explained the data", "It was Dr Lin whom explained the data",
          "It was Dr Lin explained the data",
          "Use “who” or “that” to emphasize a person."),
        q("Which sentence is suitable as the first sentence of a comment?", "The evidence points to policy, not only to weather",
          "The evidence point to policy, not only to weather", "The eivdence points to policy, not only to weather", "The evidecne points to policy, not only to weather",
          "A comment can begin by stating its main argument."),
        q("Which sentence is a cleft sentence rather than a relative clause?", "It was in this town that the emissions fell",
          "It is a town that suffers from pollution", "The town that we visited is small",
          "Pollution which we measured is high",
          "After removing “It was” and “that,” add “in” to make “this town ... the emissions fell” complete; “in this town the emissions fell” is a complete sentence, so this is a cleft emphasizing place."),
      ])

    V("vo_brave", "Adversity", 15, 4,
      "Recognize adversity, courage, survive, and despair.",
      [("adversity", "adversity"), ("courage", "courage"), ("survive", "survive"), ("despair", "despair")], "vo_mind")

    V("vo_survive", "Perseverance", 15, 4,
      "Recognize perseverance, crew, hope, and ordeal.",
      [("perseverance", "perseverance"), ("crew", "crew"), ("hope", "hope"), ("ordeal", "ordeal")], "vo_mind")

    G("gr_doemph", "Emphasis with do", 15, 4,
      "Use do, does, or did to emphasize a verb and show that something really happened or is true.", "emph", [
        q("She really survived the ordeal. Which sentence correctly emphasizes the verb?", "She did survive the ordeal",
          "She did survived the ordeal", "She does survived the ordeal", "Did she survive the ordeal as a statement of emphasis without inversion question mark only",
          "Use the base form “survive” after “did.”"),
        q("I really hope they are safe. Which sentence is correct?", "I do hope they are safe",
          "I do hoped they are safe", "I does hope they are safe", "Hope do I they are",
          "Use “do hope” with the subject “I.”"),
        q("Which sentence emphasizes the verb?", "The crew did reach the island",
          "It was the crew that reached the island", "The crew reached the island", "Did the crew reach the island",
          "“Did reach” uses an auxiliary to emphasize the verb. “It was the crew that” emphasizes the subject."),
        q("When “does” is used for emphasis, what form does the following verb take?", "Base form", "Third-person singular", "Past tense", "Past participle",
          "“Does” already marks the third person, so the following verb stays in its base form, as in “hope.”"),
      ])

    G("gr_invif", "Inversion without if", 15, 4,
      "Omit if from a conditional sentence and move had, were, or should to the beginning.", "invert", [
        q("If they had known the danger, they would have changed course. Which sentence correctly omits “if”?",
          "Had they known the danger, they would have changed course",
          "Had they known the danger, they would change course yesterday",
          "If had they known the danger, they would have changed",
          "Did they know the danger, they would have changed",
          "“Had they known” is equivalent to “If they had known.”"),
        q("Were I in their place, I ___ the same. Which form completes this sentence about the present?", "would do",
          "would have done", "did", "had done", "“Were I” describes an unreal present, so the main clause uses “would do.”"),
        q("Which sentence omits “if”?", "Should the storm return, we would stay on the island",
          "If the storm should return, we would stay", "The storm should return and we stay",
          "Return the storm if we would",
          "“Should the storm return” is an inversion that omits “if.”"),
        q("Which if-clause is equivalent to “Had I listened”?", "If I had listened",
          "If I listened", "If I have listened", "If had I listened",
          "“Had I listened” corresponds to “If I had listened.”"),
      ])

    F("fu_adv", "Discussing Adversity", 15, 4,
      "Explain how people face hardship and emphasize what they actually did.", "fu_argue", [
        q("Which sentence emphasizes that the crew really reached the island?", "The crew did reach the island",
          "The crew did reached the island", "Reached did the crew", "The crew does reached",
          "“Did reach” emphasizes the verb."),
        q("Which sentence says they would have changed course if they had known, while omitting “if”?",
          "Had they known, they would have changed course",
          "Had they known, they changed course", "If had they known, they would have changed",
          "Known had they, they would changed",
          "“Had they known” is equivalent to “If they had known.”"),
        q("Which sentence says that perseverance gave them hope?", "Perseverance gave them hope",
          "Preseverance gave them hope", "Gave perseverance them", "Perseveracne gave them hope",
          "“Gave them hope” describes the effect of perseverance."),
        q("Which cleft sentence emphasizes courage rather than luck?", "It was courage that kept them going",
          "It was courage which kept them going as a cleft", "Courage that it was kept",
          "It was courage what kept",
          "Use “It was courage that ...” to emphasize courage."),
      ])

    _d = "Had the crew lost hope, they would not have survived. They did keep a small fire at night. It was perseverance that carried them through the ordeal."
    R("rw_adv", "Reading About Adversity", 15, 4,
      "Infer which statement is hypothetical and which fact the author emphasizes.", "rw_infer", [
        q(_d + " If the crew had lost hope, what would have happened?", "They would not have survived", "They would still have made a fire", "Their perseverance would have disappeared", "The passage says they lost hope",
          "“Would not have survived” describes a hypothetical result."),
        q(_d + " What did the crew really do at night?", "Keep a small fire burning", "Leave the island", "Give up", "Do nothing",
          "“Did keep a small fire” emphasizes that they really kept the fire burning."),
        q(_d + " What does the author emphasize as carrying them through the ordeal?", "Perseverance", "Luck", "The fire alone", "Despair",
          "It was perseverance that carried them."),
        q(_d + " Which statement describes a fact that happened?", "They kept a fire burning at night", "They lost hope", "They did not survive", "Perseverance had no effect",
          "“Did keep” states a fact; “Had the crew lost hope” is hypothetical."),
      ])

    R("wr_adv", "Writing a Reading Response", 15, 4,
      "Choose a response that includes all the required points.", "rw_write_s", [
        q("Key points: they would not have survived without hope; they really kept a fire at night; perseverance carried them through. Which sentence includes all three?",
          "Had they lost hope they would not have survived, they did keep a fire, and it was perseverance that carried them",
          "They kept a fire", "Hope matters", "The ordeal was long",
          "All three points must be included."),
        q("Which sentence correctly omits “if” in a reading response?", "Were I there, I would try to help",
          "Were I there, I would have tried tomorrow as now", "If were I there, I would try",
          "Was I there, I would try",
          "“Were I there” is equivalent to “If I were there.”"),
        q("Which sentence is suitable as the first sentence of a reading response?", "The story shows courage in adversity",
          "The story show courage in adversity", "The story shows courage in avdersity", "The story shows courage in adverstiy",
          "A reading response can begin by stating the theme."),
        q("Which sentence uses do to emphasize the verb?", "I do admire their perseverance",
          "It is perseverance that I admire", "I admire their perseverance", "Do I admire their perseverance",
          "“Do admire” emphasizes the verb. “Do I admire” is a question, not emphasis."),
      ])

    V("vo_poemw", "Poetry", 15, 5,
      "Recognize poem, rhyme, verse, and imagery.",
      [("poem", "poem"), ("rhyme", "rhyme"), ("verse", "line of poetry"), ("imagery", "imagery")], "vo_mind")

    V("vo_rhyme", "Poetry Appreciation", 15, 5,
      "Recognize metaphor, rhythm, recite, and emotion.",
      [("metaphor", "metaphor"), ("rhythm", "rhythm"), ("recite", "recite"), ("emotion", "emotion")], "vo_mind")

    G("gr_ellip", "Ellipsis", 15, 5,
      "Omit repeated verbs while retaining to in an infinitive.", "ellip", [
        q("I wanted to recite the poem, and he wanted ___. Which word completes the sentence?", "to",
          "to recite the poem again in full", "recite", "/",
          "Keep “to” when an infinitive is omitted."),
        q("Which sentence uses ellipsis correctly?", "She can recite, and so can he",
          "She can recite, and so he", "She can recite, and so can", "She can, and he can recite so",
          "“So can he” omits “recite.”"),
        q("He didn't join the reading, but I wanted him ___. Which word completes the sentence?", "to",
          "to join", "join", "joining", "“Wanted him to” can omit the following “join,” but “to” must remain. Leaving only “to” completes the ellipsis."),
        q("In which sentence should “to” not be omitted?", "I asked her to, but she refused",
          "I can swim and she can too", "He is tired and she is too", "Some stayed and others left",
          "Keep “to” in “asked her to.” The other sentences omit a repeated verb or predicate adjective and do not contain “to.”"),
      ])

    G("gr_ellipcmp", "Ellipsis in Comparisons", 15, 5,
      "Omit repeated predicates in comparisons without confusing the things being compared.", "ellip", [
        q("This poem is harder to recite than that one. Which sentence is correct?", "This poem is harder to recite than that one is",
          "This poem is harder to recite than that one", "This poem is more harder to recite than that",
          "This poem is harder to recite than recite that one",
          "“Than that one is” omits “hard”; the comparison is with another poem."),
        q("She reads better than before. Which sentence is correct?", "She reads better than she did before",
          "She reads better than before she did the poem", "She reads more better than she did",
          "She reads better than did",
          "In “than she did before,” “did” stands for “read.”"),
        q("Which sentence makes the comparison clear?", "The rhythm is stronger than the imagery is",
          "The rhythm is stronger than the imagery", "Stronger the rhythm is than", "The rhythm is more strong than imagery is it",
          "“Than the imagery is” clearly compares rhythm and imagery."),
        q("What is the main purpose of ellipsis in a comparison?", "Avoid repeating a verb or adjective already used", "Turn the sentence into an inverted question", "Remove the thing being compared", "Emphasize a hypothetical",
          "Ellipsis avoids repetition, but the comparison still needs to be clear."),
      ], "inferred")

    F("fu_poem", "Discussing Poetry", 15, 5,
      "Describe a poem's imagery and rhythm and compare two poems.", "fu_desc", [
        q("Which sentence says that you also want to recite, omitting the repeated verb?", "She wants to recite, and I want to as well",
          "She wants to recite, and I want as well", "She wants to recite, and I want to recite to",
          "Want to I and she recite",
          "Keep “to” in “I want to” and omit “recite.”"),
        q("Which sentence says that this poem has a stronger rhythm than the other one?", "This poem has a stronger rhythm than that one does",
          "This poem has a stronger rhythm than that one", "This poem has more stronger rhythm than that",
          "Stronger has this poem than does",
          "“Than that one does” stands for “than that one has a strong rhythm.”"),
        q("Which sentence says that a metaphor conveys the poem's emotion?", "The metaphor carries the emotion of the verse",
          "The metaphor carrie the emotion of the verse", "The mteaphor carries the emotion of the verse", "The metapohr carries the emotion of the verse",
          "“Carries the emotion” explains the metaphor's effect."),
        q("Your friend can recite the verse, and you can too. Which sentence uses ellipsis correctly?", "He can recite the verse, and so can I",
          "He can recite the verse, and so I", "He can recite, and so can", "So can I recite he",
          "“So can I” omits “recite the verse.”"),
      ])

    _p = "The first poem is harder to recite than the second is. Lin wanted to try the long verse, and her friend wanted to as well. Its imagery is quiet, but the rhythm is strong."
    R("rw_poem", "Reading About Poetry", 15, 5,
      "Infer which poem is harder and identify the omitted verb.", "rw_infer", [
        q(_p + " Which poem is harder to recite?", "The first poem", "The second poem", "They are equally difficult", "The passage does not compare them",
          "The first poem is harder ... than the second."),
        q(_p + " What does the friend also want to do?", "Try the long poem", "Give up reciting", "Rewrite the rhythm", "Look only at the imagery",
          "“Wanted to as well” omits “try the long verse.”"),
        q(_p + " What are the imagery and rhythm like?", "The imagery is quiet, and the rhythm is strong", "Both are quiet", "The rhythm is weak", "There is no imagery",
          "imagery is quiet, but the rhythm is strong."),
        q(_p + " What is omitted after “wanted to”?", "Try the long poem", "Be harder than the second poem", "Have a strong rhythm", "Nothing is omitted",
          "“And her friend wanted to” continues the earlier phrase “wanted to try the long verse.”"),
      ])

    R("wr_poem", "Writing a Poetry Review", 15, 5,
      "Choose a review sentence that includes all the required points.", "rw_write_s", [
        q("Key points: the first poem is harder to recite; the friend also wants to try the long poem; the imagery is quiet but the rhythm is strong. Which sentence includes all three?",
          "The first is harder to recite than the second is, her friend wanted to try the long verse too, and the imagery is quiet but the rhythm is strong",
          "The first poem is hard", "Her friend likes poetry", "Rhythm matters",
          "All three points must be included."),
        q("Which sentence correctly uses ellipsis with an infinitive in a review?", "I hoped to read it aloud, and she hoped to as well",
          "I hoped to read it aloud, and she hoped as well", "I hoped to, and she hoped recite",
          "Hoped to she and I",
          "Keep “to” in “hoped to.”"),
        q("Which sentence is suitable as the first sentence of a review?", "The poem uses quiet imagery and a strong rhythm",
          "The poem uses quiet imagery and an strong rhythm", "The poem uses quiet iamgery and a strong rhythm", "The poem uses quiet imagrey and a strong rhythm",
          "A review can begin by summarizing the imagery and rhythm."),
        q("Which sentence makes the comparison clear?", "She recites more clearly than she did last year",
          "She recites more clearly than last year she did the poem better", "She recites more clearer than she did",
          "More clearly she recites than did",
          "In “than she did last year,” “did” stands for “recited.”"),
      ])
