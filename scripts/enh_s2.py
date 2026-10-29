# -*- coding: utf-8 -*-
"""People's Education Press (2019), Selective Compulsory Course 2. Unit names follow the commonly used table of contents; book numbering needs verification."""
from enh_tx import V, P, G, F, R, q


def load():
    V("vo_lab", "Scientific Research", 14, 1,
      "Recognize and understand hypothesis, experiment, data, and evidence.",
      [("hypothesis", "proposed explanation"), ("experiment", "test"), ("data", "information"), ("evidence", "supporting facts")], "vo_life")

    V("vo_theory2", "Scientific Conclusions", 14, 1,
      "Recognize and understand conclude, variable, sample, and method.",
      [("conclude", "draw a conclusion"), ("variable", "factor"), ("sample", "sample"), ("method", "method")], "vo_life")

    G("gr_subnow", "Subjunctive Mood", 14, 1,
      "Use If I were and would + base form to express a hypothetical situation contrary to present facts.", "subj", [
        q("Contrary to present facts: If I were you, I would check the data first. Which sentence is correct?", "If I were you, I would check the data",
          "If I am you, I would check the data", "If I were you, I will check the data",
          "If I were you, I checked the data",
          "For a present counterfactual, use were in the if-clause and would + base form in the main clause."),
        q("If she ___ more evidence, she would be more certain. Which word completes the blank?", "had",
          "has", "have", "will have", "Use the past-tense form had in a present counterfactual if-clause."),
        q("Which sentence is a present counterfactual?", "If he knew the method, he would help us",
          "If he knows the method, he will help us", "If he knew the method, he helps us",
          "If he knows the method, he would help us",
          "Knew pairs with would help to show that he does not know it now."),
        q("If I ___ a larger sample, I would trust the result. Which word completes the blank?", "had",
          "have", "has", "am having", "Use had in the if-clause and would trust in the main clause."),
      ])

    G("gr_butfor", "But for and the Subjunctive", 14, 1,
      "Use But for to mean “if it were not for” and pair it with would have done or would do.", "subj", [
        q("How can I say that I would have failed without your help?", "But for your help, I would have failed",
          "But for your help, I failed", "But for your help, I would fail yesterday",
          "But for your help, I had failed",
          "Use would have failed for a past counterfactual."),
        q("But for the evidence, we ___ still unsure. Which word completes the blank to show we would still be unsure now?", "would be",
          "would have been yesterday only", "are", "were be", "The result is in the present, so use would be."),
        q("Which sentence uses but for for a past counterfactual?", "But for the experiment, they would have chosen the wrong method",
          "But for the experiment, they chose the wrong method", "But for the experiment, they will choose",
          "But for the experiment, they had chose",
          "Would have chosen describes a result contrary to what actually happened in the past."),
        q("In this kind of sentence, what does but for mean?", "If it were not for", "Because it happened", "After", "Except for an item on a list",
          "But for your help means if it were not for your help."),
      ], "inferred")

    F("fu_sci", "Explaining a Scientific Hypothesis", 14, 1,
      "Explain a hypothesis, the evidence for it, and what remains uncertain.", "fu_argue", [
        q("Which sentence says that more evidence would make us more certain?", "If we had more evidence, we would be more certain",
          "If we have more evidence, we would be more certain", "If we had more evidence, we are more certain",
          "If we would have more evidence, we are certain",
          "For a present counterfactual, pair had with would be."),
        q("Which sentence says that the conclusion would be different without that experiment?", "But for that experiment, the conclusion would be different",
          "But for that experiment, the conclusion is different in the past wish", "Experiment but for different is",
          "Would be the conclusion but for real",
          "But for paired with would be expresses a hypothetical absence."),
        q("Which sentence points out that the data are insufficient?", "The data are not enough to support the hypothesis",
          "The data are not enough to support the hpyothesis", "The data are not enough to support the hypotheiss", "The data are not enough to support the hyothesis",
          "Are not enough to support limits the conclusion."),
        q("Which sentence recommends controlling the variables first?", "We should control the variables first",
          "Control should the variables we", "We should controlled the variables first", "We should to control the variables first",
          "Should control introduces a recommended next step."),
      ])

    _s = "If the team had a larger sample, they would trust the result more. But for one failed experiment, they would have published the paper last month. The data are useful, but they do not prove the whole hypothesis."
    R("rw_sci", "Reading a Science Passage", 14, 1,
      "Identify the claim, the evidence still needed, and the limits the author leaves implicit.", "rw_argue", [
        q(_s + " If the sample had been larger, what would they have done?", "Trusted the result more", "Given up immediately", "Stopped experimenting", "Published already",
          "Would trust the result more describes a hypothetical outcome."),
        q(_s + " If it had not been for the failed experiment, what would they have done last month?", "Published the paper", "Increased the sample size", "Proved the whole hypothesis", "Stopped the research",
          "The passage says they would have published the paper last month."),
        q(_s + " What can the data prove now?", "They still cannot prove the whole hypothesis", "They have proved everything", "They are completely useless", "They replace the experiment",
          "The passage says the data do not prove the whole hypothesis."),
        q(_s + " Which best captures the author's argument?", "The data are useful but still do not prove the whole hypothesis",
          "The experiment failed, so the data are useless", "The paper has already been published", "The sample is already large enough",
          "Useful, but they do not prove qualifies the claim."),
      ])

    R("wr_sci", "Writing an Experiment Review", 14, 1,
      "Choose sentences that include the required points in a review.", "rw_write_s", [
        q("Key points: a larger sample would increase confidence; without the failed experiment, they would have published last month; the data still do not prove the whole hypothesis. Which sentence includes all three?",
          "If they had a larger sample they would trust it more, but for the failed experiment they would have published, and the data do not prove the whole hypothesis",
          "The sample is small", "The experiment failed", "Data can be useful",
          "All three points must be included."),
        q("Which sentence in the review expresses a present counterfactual?", "If I were on the team, I would repeat the test",
          "If I am on the team, I would repeat the test", "If I were on the team, I will repeat the test",
          "If I were on the team, I repeated the test",
          "Were pairs with would repeat."),
        q("Which sentence would make a suitable opening for the review?", "The hypothesis is interesting but not fully proved",
          "The hypothesis is interest but not fully proved", "The hypothesis is itneresting but not fully proved", "The hypothesis is interestnig but not fully proved",
          "A review can begin by stating a limitation: not fully proved."),
        q("Which sentence uses But for to talk about the past?", "But for the error, they would have finished",
          "But for the error, they finished", "But for the error, they finish tomorrow",
          "But for the error, they had finish",
          "Would have finished refers to a past counterfactual."),
      ])

    V("vo_exchange", "Cross-Cultural Communication", 14, 2,
      "Recognize and understand exchange, abroad, adapt, and homesick.",
      [("exchange", "communication"), ("abroad", "in another country"), ("adapt", "adjust"), ("homesick", "missing home")], "vo_life")

    V("vo_host", "Host Families", 14, 2,
      "Recognize and understand host, custom, misunderstand, and fluent.",
      [("host", "host"), ("custom", "tradition"), ("misunderstand", "misinterpret"), ("fluent", "fluent")], "vo_life")

    G("gr_subpast", "Past Counterfactuals", 14, 2,
      "Use had + past participle in the if-clause and would have + past participle in the main clause.", "subj", [
        q("If I had tried harder to adapt, I would have had fewer misunderstandings. Which sentence is correct?",
          "If I had adapted faster, I would have had fewer misunderstandings",
          "If I adapted faster, I would have had fewer misunderstandings",
          "If I had adapted faster, I would have less misunderstandings",
          "If I have adapted faster, I would have fewer misunderstandings",
          "For a past counterfactual, pair had adapted with would have had. Fewer modifies the countable noun misunderstandings."),
        q("If she ___ abroad earlier, she would have been more fluent. Which words complete the blank?", "had gone",
          "went", "has gone", "would go", "Use had gone in the if-clause."),
        q("Which sentence describes a past counterfactual?", "If he had asked his host, he would have avoided the mistake",
          "If he asked his host, he would avoid the mistake now", "If he had asked, he will avoid it",
          "If he asks, he would have avoided it",
          "Had asked pairs with would have avoided."),
        q("If they ___ the custom, they would not have been so homesick. Which words complete the blank?", "had understood",
          "understood", "understand", "have understood", "Use had understood in a past-counterfactual if-clause."),
      ])

    G("gr_mixsub", "Mixed-Time Counterfactuals", 14, 2,
      "Use had + past participle for a past if-clause and would + base form for a present main-clause result.", "subj", [
        q("If I had followed my host's advice, I would be more fluent now. Which sentence is correct?",
          "If I had followed the advice, I would be more fluent now",
          "If I had followed the advice, I would have been more fluent now",
          "If I followed the advice, I would be more fluent now",
          "If I had followed the advice, I am more fluent now",
          "The if-clause refers to the past and the main clause to the present, so use had followed with would be now."),
        q("If she had stayed abroad, she ___ the language now. Which words complete the blank?", "would speak",
          "would have spoken", "spoke", "had spoken", "Now signals a present result, so use would speak."),
        q("Which sentence uses mixed-time counterfactuals?", "If he had learned the custom then, he would not feel confused now",
          "If he had learned the custom, he would not have felt confused then",
          "If he learned the custom, he would not feel confused",
          "If he learns the custom, he will not feel confused",
          "Then appears in the if-clause and now in the main clause, so the time references differ."),
        q("When the main clause includes now, which verb form is more common?", "would + base form", "would have + past participle", "simple present", "had + past participle",
          "Use would do for a present result, not would have done."),
      ], "inferred")

    F("fu_bridge", "Comparing Cultural Differences", 14, 2,
      "Compare cultural customs and explain what would have happened if someone had known about them.", "fu_argue", [
        q("Which sentence says that asking the host would have prevented the misunderstanding?",
          "If I had asked my host, I would not have misunderstood the custom",
          "If I asked my host, I would not have misunderstood", "If I had asked, I will not misunderstand",
          "If I have asked, I would not misunderstood",
          "For a past counterfactual, pair had asked with would not have misunderstood."),
        q("Which sentence says that knowing the custom would make someone feel less homesick now?",
          "If I had known the custom, I would not feel so homesick now",
          "If I had known the custom, I would not have felt homesick now",
          "If I knew the custom then, I feel fine now", "Had known I, I am not homesick",
          "A past condition with a present result takes would not feel now."),
        q("Which sentence politely admits that the speaker is not yet fluent enough?", "I am not fluent yet, so I may misunderstand",
          "I am not fluent yet, so I may misunderstanded", "I am not fluent yet, so I may to misunderstand", "I is not fluent yet, so I may misunderstand",
          "So connects the reason with a possible misunderstanding."),
        q("Which sentence recommends that exchange students learn about local customs first?", "Exchange students should learn local customs first",
          "Should learn customs students exchange", "Exchange students should learned local customs first", "Exchange students should to learn local customs first",
          "Should learn is used to make a recommendation."),
      ])

    _e = "If Lin had asked her host, she would not have worn the wrong clothes to the dinner. If she had known that custom, she would feel less embarrassed now. She is still learning, and her host is patient."
    R("rw_bridge", "Reading a Cross-Cultural Passage", 14, 2,
      "Infer what happened in the past and which feelings remain in the present.", "rw_infer", [
        q(_e + " If she had asked her host, what would she have avoided?", "Wearing the wrong clothes to dinner", "Feeling embarrassed ever since", "Learning the language", "Meeting a patient host",
          "Would not have worn the wrong clothes describes something she could have avoided."),
        q(_e + " What might she feel now?", "Less embarrassed if she had known the custom", "No longer homesick at all", "No longer learning", "Impatient with her host",
          "Would feel less embarrassed now describes a present result."),
        q(_e + " What is her host like?", "Patient", "Very angry", "Away from home", "Unable to speak the local language", "The passage says her host is patient."),
        q(_e + " Which statement is a fact rather than a hypothetical situation?", "She is still learning, and her host is patient",
          "She asked her host", "She did not wear the wrong clothes", "She is not embarrassed at all now",
          "The last sentence states facts. The first two are if-conditions."),
      ])

    R("wr_bridge", "Writing a Cultural Reflection", 14, 2,
      "Choose a reflection sentence that includes the required points.", "rw_write_s", [
        q("Key points: asking at the time would have prevented the clothing mistake; knowing the custom would mean less embarrassment now; the host is patient. Which sentence includes all three?",
          "If I had asked I would not have worn the wrong clothes, if I had known the custom I would feel less embarrassed now, and my host is patient",
          "I wore the wrong clothes", "I feel embarrassed", "My host is kind",
          "All three points must be included."),
        q("Which sentence correctly describes a past counterfactual in the reflection?", "If I had listened, I would have avoided the mistake",
          "If I listened, I would have avoided the mistake", "If I had listened, I will avoid the mistake",
          "If I have listened, I would avoided the mistake",
          "Had listened pairs with would have avoided."),
        q("Which sentence would make a suitable opening for the reflection?", "I misunderstood a custom at dinner",
          "I misunderstood an custom at dinner", "I msiunderstood a custom at dinner", "I miunderstood a custom at dinner",
          "A reflection can begin by stating what happened."),
        q("Which sentence uses mixed-time counterfactuals?", "If I had prepared, I would be calmer now",
          "If I had prepared, I would have been calmer then", "If I prepared, I would be calmer",
          "If I prepare, I will be calmer",
          "Had prepared refers to the past, while would be now refers to the present."),
      ])

    V("vo_dish", "Food Culture", 14, 3,
      "Recognize and understand recipe, ingredient, flavour, and appetite.",
      [("recipe", "cooking instructions"), ("ingredient", "component"), ("flavour", "taste"), ("appetite", "desire to eat")], "vo_life")

    V("vo_spice", "Table Manners", 14, 3,
      "Recognize and understand spice, banquet, chopstick, and manner.",
      [("spice", "seasoning"), ("banquet", "feast"), ("chopstick", "chopstick"), ("manner", "etiquette")], "vo_life")

    G("gr_subfut", "Future Counterfactuals", 14, 3,
      "Use should or were to + base form for hypothetical situations contrary to future facts.", "subj", [
        q("If tomorrow's banquet were cancelled, we would eat at home. Which sentence is correct?",
          "If the banquet should be cancelled, we would eat at home",
          "If the banquet will be cancelled, we would eat at home",
          "If the banquet should be cancelled, we will eat at home",
          "If the banquet is cancelled, we would eat at home",
          "A future counterfactual can use should be cancelled with would eat."),
        q("If it ___ to snow tomorrow, the outdoor meal would stop. Which word completes the blank?", "were",
          "was", "is", "will be", "Were to snow describes an unlikely future event."),
        q("Which sentence describes an unlikely future situation?", "If I were to forget the recipe, I would use a simpler one",
          "If I forget the recipe, I will use a simpler one", "If I forgot the recipe yesterday, I used another",
          "If I am to forget, I would used one",
          "Were to forget pairs with would use to express a future hypothetical."),
        q("If she should miss the banquet, she ___. Which words complete the blank?", "would be upset",
          "will be upset", "was upset", "had been upset", "Use would be upset in the main clause."),
      ])

    G("gr_asif", "The Subjunctive after As If", 14, 3,
      "Use the past tense or had + past participle after as if to suggest that something is not true.", "subj", [
        q("He talks about this dish as if he were a cook. Which sentence is correct if this is not true now?", "He talks as if he were a cook",
          "He talks as if he is a cook in a false way that still uses is", "He talks as if he is being a real cook now true",
          "He talks as if he had been a cook tomorrow",
          "When the idea is contrary to the present, use were after as if."),
        q("She looked at the table as if she had just seen a very spicy dish. Which sentence is correct?", "She looked as if she had seen a very hot dish",
          "She looked as if she saw a very hot dish tomorrow", "She looked as if she has seen a hot dish",
          "She looked as if she sees a hot dish",
          "Use had seen to describe something that seems to have already happened."),
        q("Which sentence suggests that something is not actually true?", "He eats as if he had never tasted spice",
          "He eats as he tastes spice every day", "As if he tastes, he eats real spice", "He eats if as he tasted",
          "Had never tasted suggests that he has tried spice, even though he acts as if he has not."),
        q("When an as if clause is contrary to present facts, which form of be is often used?", "were", "is", "been", "being",
          "Were is often used for a present counterfactual."),
      ])

    F("fu_foods", "Comparing Foods", 14, 3,
      "Compare different dishes and describe personal taste preferences.", "fu_desc", [
        q("Which sentence says that this dish tastes as if it had no salt?", "This dish tastes as if it had no salt",
          "This dish tastes as if it has no salt and that is the true recipe we measured",
          "Tastes as if had it no salt", "Salt as if the dish no",
          "As if it had no salt means that it tastes as though it contains no salt."),
        q("Which sentence says that the recipe would change if this spice were unavailable?",
          "If the spice should be unavailable, I would change the recipe",
          "If the spice will be unavailable, I would change the recipe",
          "If the spice should be unavailable, I will change the recipe",
          "If the spice unavailable, I would changed",
          "Should be unavailable pairs with would change."),
        q("Which sentence describes a table manner involving chopsticks?", "It is good manners not to point with chopsticks",
          "It are good manners not to point with chopsticks", "It is good manners not to point with cohpsticks", "It is good manners not to point with chopstikcs",
          "It is good manners not to is used to describe etiquette."),
        q("Which sentence says that this dish may improve your appetite?", "The flavour may improve your appetite",
          "The flavour may improved your appetite", "Improve may the flavour you", "The flavour may to improve your appetite",
          "May improve describes a possible effect."),
      ])

    _d = "The banquet included a mild soup and a spicy fish. Lin ate as if she had never tasted that spice. If the fish should be too hot, she would drink some soup."
    R("rw_food", "Reading a Passage about Food", 14, 3,
      "Infer what as if suggests about reality and identify plans that have not yet happened.", "rw_infer", [
        q(_d + " What was served at the banquet?", "Mild soup and spicy fish", "Dessert only", "No fish", "Chopsticks only",
          "The passage mentions a mild soup and a spicy fish."),
        q(_d + " What does as if suggest about Lin and the spice?", "She may have tried it before but reacts as if she had not", "She is a cook", "She does not eat", "The soup is spicy",
          "As if she had never tasted it suggests that she seems not to have tried it before."),
        q(_d + " If the fish should be too spicy, what would she do?", "Drink some soup", "Leave the banquet", "Order another fish", "Point at someone with chopsticks",
          "The passage says she would drink some soup."),
        q(_d + " Which statement is still hypothetical rather than something that has already happened?", "If the fish should be too spicy, she would drink soup",
          "There was soup and fish at the banquet", "She has already eaten", "The passage contains no hypothetical situation",
          "If the fish should be too hot is still a hypothetical condition."),
      ])

    R("wr_food", "Writing a Food Description", 14, 3,
      "Choose a description that includes the required points.", "rw_write_s", [
        q("Key points: there was soup and spicy fish; she acted as if she had never tried the spice; if it were too hot, she would drink soup. Which sentence includes all three?",
          "There was soup and spicy fish, she ate as if she had never tasted the spice, and if it should be too hot she would drink soup",
          "There was soup", "The fish was spicy", "Soup is mild",
          "All three points must be included."),
        q("Which sentence uses as if to describe something that seems to have already happened?", "He smiled as if he had found a new flavour",
          "He smiled as if he finds a new flavour tomorrow", "He smiled as if he has found a flavour",
          "As if smiled he had found",
          "Had found describes something that seems to have already been discovered."),
        q("Which sentence would make a suitable opening for the description?", "This paragraph describes one banquet",
          "This paragraph describe one banquet", "This praagraph describes one banquet", "This paragrpah describes one banquet",
          "A description can begin with This paragraph describes."),
        q("Which sentence describes an unlikely future situation?", "If the soup were to run out, we would cook noodles",
          "If the soup runs out, we will cook noodles", "If the soup ran out yesterday, we cooked noodles",
          "Were the soup runs out, we cook",
          "Were to run out pairs with would cook."),
      ])

    V("vo_rail", "Long-Distance Travel", 14, 4,
      "Recognize and understand rail, carriage, scenery, and delay.",
      [("rail", "railway"), ("carriage", "train car"), ("scenery", "landscape along the way"), ("delay", "late arrival")], "vo_life")

    V("vo_scenery", "Travel Impressions", 14, 4,
      "Recognize and understand boundless, frost, awesome, and cross.",
      [("boundless", "limitless"), ("frost", "ice crystals"), ("awesome", "impressive"), ("cross", "pass over")], "vo_life")

    G("gr_wish", "The Subjunctive after Wish", 14, 4,
      "Use the past tense after wish for a present counterfactual and had + past participle for a past counterfactual.", "subj", [
        q("I wish I were on that train now, but I am not. Which sentence is correct?", "I wish I were on that train",
          "I wish I am on that train", "I wish I were on that train and I really am", "I wish I had been on that train now as a present fact",
          "Use were after wish for a present counterfactual."),
        q("Which sentence expresses regret about missing the train?", "She wishes she had not missed the train",
          "She wishes she did not missed the train", "She wishes she has not missed the train",
          "She wishes she missed not the train",
          "Use had not missed for a past counterfactual."),
        q("I wish the delay ___ shorter. Which word completes the blank for a present delay?", "were",
          "is", "had been", "will be", "Use were to wish that the present situation were different."),
        q("Which sentence expresses regret about something that has already happened?", "I wish I had taken more photos",
          "I wish I took more photos now", "I wish I take more photos", "I wish I have more photos",
          "Had taken expresses regret about not taking more photos at the time."),
      ])

    G("gr_ifonly", "The Subjunctive after If Only", 14, 4,
      "Use If only with the past tense or had + past participle to express a strong wish.", "subj", [
        q("If only I could see that boundless plain now. Which sentence is correct?", "If only I could see the boundless plain",
          "If only I can see the boundless plain", "If only I could saw the plain", "If only can I see the plain",
          "If only expresses an unrealizable present wish; use could see."),
        q("Which sentence expresses regret about not bringing a coat?", "If only I had brought a coat",
          "If only I brought a coat", "If only I have brought a coat", "If only had I brought a coat as a question",
          "Use had brought for a past counterfactual."),
        q("If only the train ___ on time now. Which word completes the blank?", "were",
          "is", "had been", "will be", "Use were to wish that the train were on time now."),
        q("Which sentence expresses regret about the past?", "If only we had crossed the mountain before the frost",
          "If only we crossed the mountain now", "If only we cross the mountain", "If only do we cross",
          "Had crossed refers to something that did not happen in the past."),
      ])

    P("ph_tonehs", "Using Intonation to Express Attitude", 14, 4,
      "Identify whether rising pitch, falling pitch, or stress conveys hesitation, surprise, or emphasis.", "attitude", [
        q("What is Really? with a clearly rising intonation most likely to express?", "Surprise", "Complete agreement and an end to the topic", "Word stress", "No attitude",
          "A rising intonation on Really often expresses surprise."),
        q("In Well... I am not sure, what does a drawn-out Well with a slight rise most likely express?", "Hesitation",
          "An angry command", "A cheerful end to the conversation", "Emphasis that the train has arrived", "A drawn-out Well often expresses hesitation."),
        q("In I DID see the frost, what does stressing DID most likely express?", "Emphasis that the speaker really did see it",
          "Denial of having seen it", "A question about whether the other person saw it", "Irrelevance to the topic",
          "Stressing did emphasizes the verb to show that it really happened."),
        q("Which pronunciation is a more polite way to say that you did not hear clearly?", "Sorry? with rising intonation", "Sorry with a heavy falling tone and an abrupt stop",
          "Say every word angrily", "Do not say Sorry at all",
          "Sorry with rising intonation is often used to ask someone to repeat themselves and sounds more polite than a blunt falling tone."),
      ])

    F("fu_trip2", "Describing a Journey", 14, 4,
      "Describe scenery along the way and express regret or wishes.", "fu_desc", [
        q("Which sentence says that the speaker wishes they were on the train now?", "I wish I were on the train",
          "I wish I am on the train", "Wish I were I am really there", "I wish I had been now as a fact",
          "Use were after wish to show that the speaker is not on the train now."),
        q("Which sentence expresses a wish that the speaker had photographed the frost?", "If only I had photographed the frost",
          "If only I photographed the frost", "If only I have photographed the frost", "Photographed if only I had",
          "Had photographed expresses regret about not taking the photo at the time."),
        q("Which sentence describes a boundless plain?", "The plain looked boundless",
          "The plain looked buondless", "The plain looked boundlses", "The plain looked bondless",
          "Looked boundless describes the scenery."),
        q("Which sentence politely expresses disappointment about a delayed train?", "I am sorry the train is delayed",
          "I is sorry the train is delayed", "He is sorry the train is delayed", "I am sorry the train is dleayed",
          "I am sorry is a polite way to express disappointment."),
      ])

    _r = "The train crossed a boundless plain at dawn. Lin wishes she had sat by the window, because she missed the frost. If only the delay had been shorter."
    R("rw_rail", "Reading a Travel Passage", 14, 4,
      "Infer what Lin regrets and which statement is only a wish.", "rw_infer", [
        q(_r + " What did the train cross at dawn?", "A boundless plain", "A city", "A wetland", "A laboratory",
          "The passage says a boundless plain at dawn."),
        q(_r + " What does Lin regret?", "Not sitting by the window and missing the frost", "Not taking the train", "The delay being too short", "The plain being too small",
          "Wishes she had sat by the window shows that she did not sit there."),
        q(_r + " What does If only express a wish for?", "A shorter delay", "A smaller plain", "Not seeing the frost", "Cancelling dawn",
          "The wish is that the delay had been shorter."),
        q(_r + " Which event actually happened?", "The train crossed the plain", "She sat by the window", "The delay was short", "She photographed the frost",
          "The first sentence states a fact. The next two state wishes."),
      ])

    R("wr_rail", "Writing a Travel Email", 14, 4,
      "Choose an email sentence that includes the required points.", "rw_write_s", [
        q("Key points: crossing a plain at dawn; regretting not sitting by the window; wishing the delay had been shorter. Which sentence includes all three?",
          "We crossed a plain at dawn, I wish I had sat by the window, and if only the delay had been shorter",
          "We crossed a plain", "I like windows", "Trains can be late",
          "All three points must be included."),
        q("Which sentence expresses regret in the email?", "I wish I had brought a camera",
          "I wish I brought a camera now for the past", "I wish I have brought a camera", "Wish I had I brought",
          "Had brought expresses regret about not bringing a camera at the time."),
        q("Which sentence would make a suitable opening for the email?", "I am writing to tell you about the journey",
          "I am write to tell you about the journey", "I am writing to telling you about the journey", "I am writing to tells you about the journey",
          "An email can begin with I am writing to tell you."),
        q("Which sentence uses If only to express a present wish?", "If only the train were here now",
          "If only the train had arrived yesterday as a wish about now using had for present",
          "If only the train is here", "If only is the train here",
          "Were here now expresses a wish that the train is not here now."),
      ])

    V("vo_aid", "First Aid", 14, 5,
      "Recognize and understand first aid, bleed, bandage, and choke.",
      [("first aid", "emergency care"), ("bleed", "lose blood"), ("bandage", "dressing"), ("choke", "be unable to breathe")], "vo_life")

    V("vo_wound", "Treating Injuries", 14, 5,
      "Recognize and understand wound, swelling, pressure, and ambulance.",
      [("wound", "injury"), ("swelling", "inflammation"), ("pressure", "force"), ("ambulance", "emergency vehicle")], "vo_life")

    G("gr_suggest", "Subjunctive after Suggestions and Orders", 14, 5,
      "Use should + base form after suggest, insist, or order; should may be omitted.", "subj", [
        q("The doctor recommended that she rest. Which sentence is correct?", "The doctor suggested that she should rest",
          "The doctor suggested that she rests", "The doctor suggested that she rested tomorrow as a fact",
          "The doctor suggested her to rest that",
          "Use should rest after suggest, though should can be omitted; do not use rests."),
        q("The nurse insisted that the boy ___ still. Which word completes the blank?", "stay",
          "stays", "stayed", "to stay", "Use the base form stay after insist."),
        q("Which sentence is correct?", "They ordered that the wound be cleaned",
          "They ordered that the wound was cleaned", "They ordered that the wound is cleaned",
          "They ordered the wound cleaned that be",
          "Be cleaned can follow order; it is equivalent to should be cleaned."),
        q("What can happen to should after suggest?", "It can be omitted, but the verb stays in the base form", "It must change to the past tense", "It must change to -ing", "It cannot appear in the clause",
          "Should can be omitted, but the verb remains in the base form."),
      ])

    G("gr_otherwise", "Counterfactuals with Otherwise", 14, 5,
      "Use otherwise to mean “if not” and pair it with would have done.", "subj", [
        q("He was bleeding; otherwise, he would not have called an ambulance. Which sentence is correct?",
          "He was bleeding; otherwise he would not have called an ambulance",
          "He was bleeding; otherwise he would not call an ambulance yesterday",
          "He was bleeding; otherwise he did not call", "Otherwise he would not have called, and he was not bleeding",
          "Otherwise with would not have called expresses a past counterfactual."),
        q("She pressed the wound. Otherwise it ___ worse. Which words complete the blank to show it would have become more serious?", "would have got",
          "got", "would get yesterday", "had got", "Use would have got for a past result that was avoided."),
        q("Which sentence uses otherwise for a counterfactual?", "He knew first aid; otherwise the boy would have choked",
          "He knew first aid; otherwise the boy choked", "Otherwise the boy choked because he knew first aid",
          "He knew first aid otherwise would choked",
          "Would have choked describes an outcome that did not actually happen."),
        q("In these sentences, what does otherwise mean?", "If not", "Therefore, as a fact", "Inside", "More than",
          "Otherwise means if the preceding situation had not occurred."),
      ], "inferred")

    F("fu_aid", "Explaining First-Aid Steps", 14, 5,
      "Explain how to stop bleeding step by step and recommend when to call an ambulance.", "fu_argue", [
        q("Which sentence gives the first step of applying pressure to a wound?", "First, put pressure on the wound",
          "First, put perssure on the wound", "First, put pressrue on the wound", "First, put prssure on the wound",
          "First introduces the step."),
        q("Which sentence reports the doctor's order to clean the wound?", "The doctor ordered that the wound be cleaned",
          "The doctor ordered that the wound was cleaned", "The doctor ordered the wound to was clean",
          "Ordered that was the wound cleaned",
          "Use be cleaned after order that."),
        q("Which sentence says that things would have been worse otherwise?", "Apply a bandage; otherwise the bleeding would have continued",
          "Apply a bandage; otherwise the bleeding continued as the real result of applying it",
          "Otherwise continued the bleeding because of the bandage", "Would have the bleeding otherwise real",
          "Otherwise with would have continued describes what would have happened without the bandage."),
        q("Which sentence recommends getting help immediately if someone is choking?", "If someone is choking, call an ambulance at once",
          "Choking call someone if an ambulance", "If someone is choke, call an ambulance at once", "If someone is choking, call an abmulance at once",
          "Call an ambulance is a clear recommendation."),
      ])

    _a = "The coach suggested that the student sit down. He put pressure on the wound and then used a bandage. Otherwise the bleeding would have become dangerous. An ambulance arrived ten minutes later."
    R("rw_aid", "Reading a First-Aid Passage", 14, 5,
      "Identify the steps already taken, the recommendation, and the outcome ruled out by otherwise.", "rw_argue", [
        q(_a + " What did the coach suggest that the student do?", "Sit down", "Keep running", "Drive himself", "Remove the bandage",
          "The passage says the coach suggested that the student sit down."),
        q(_a + " Which two actions did he take next?", "Apply pressure to the wound and then use a bandage", "Just wait", "Make the student run", "Cancel the ambulance",
          "He put pressure on the wound and then used a bandage."),
        q(_a + " What does otherwise indicate was avoided?", "The bleeding becoming dangerous", "The ambulance arriving", "The student sitting down", "Using a bandage",
          "Would have become dangerous is a dangerous outcome that did not happen."),
        q(_a + " Which event is a fact?", "The ambulance arrived ten minutes later", "The bleeding became dangerous", "No bandage was used", "The coach told him to keep running",
          "The last sentence reports the fact that the ambulance arrived."),
      ])

    R("wr_aid", "Writing First-Aid Steps", 14, 5,
      "Choose step instructions that include the required points.", "rw_write_s", [
        q("Key points: recommend sitting down; apply pressure and use a bandage; otherwise, the bleeding would have become dangerous. Which sentence includes all three?",
          "The coach suggested that he sit down, pressure and a bandage were used, and otherwise the bleeding would have become dangerous",
          "He sat down", "A bandage was used", "Ambulances are fast",
          "All three points must be included."),
        q("Which sentence correctly reports an instruction in the steps?", "They insisted that the patient stay awake",
          "They insisted that the patient stayed awake", "They insisted that the patient stays awake",
          "They insisted the patient to stay that",
          "Use the base form stay after insist."),
        q("Which sentence would make a suitable opening for the steps?", "Follow these steps when someone is bleeding",
          "Follow these steps when someone is bleed", "Follow these steps when someone is beleding", "Follow these steps when someone is bleednig",
          "Instructions can begin with Follow these steps."),
        q("Which sentence uses otherwise for a counterfactual?", "Keep the patient warm; otherwise he would have got worse",
          "Keep the patient warm; otherwise he got worse", "Otherwise he got worse because you kept him warm",
          "Would have he got otherwise real",
          "Would have got worse describes an outcome that did not happen after keeping him warm."),
      ])
