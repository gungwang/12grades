# -*- coding: utf-8 -*-
"""People's Education Press (2019), Selective Compulsory English Book 1. Common unit sequence; unit titles and book volume still need verification."""
from enh_tx import V, G, F, R, q


def load():
    V("vo_achieve", "Achievements", 13, 1,
      "Recognize achievement, genius, career, and honour.",
      [("achievement", "achievement"), ("genius", "talent"), ("career", "career"), ("honour", "honour")], "vo_people")

    V("vo_nobel", "Scientists and their contributions", 13, 1,
      "Recognize Nobel, discover, theory, and devote.",
      [("Nobel", "Nobel Prize"), ("discover", "discover"), ("theory", "theory"), ("devote", "devote")], "vo_people")

    G("gr_subjcls", "That-clauses as the subject", 13, 1,
      "Use that-clauses as the subject or use it as a formal subject.", "nouncls", [
        q("___ he refused the prize surprised us. Which word belongs in the blank?", "That",
          "What", "Which", "Who", "Use That when the subject clause is complete and refers to a fact."),
        q("Which sentence uses it as a formal subject?", "It is clear that she devoted her life to research",
          "That is clear she devoted her life", "Clear that she devoted is it", "It clear that she devoted",
          "In It is clear that..., the that-clause is the real subject."),
        q("___ he discovered is still unknown. The clause is missing the thing discovered. Which word belongs in the blank?", "What",
          "That", "Which", "If", "Use What when the clause is missing an object; That cannot fill that role."),
        q("Which sentence is correct?", "That the theory works has been proved",
          "The theory works has been proved", "That the theory works have been proved",
          "Which the theory works has been proved",
          "When a that-clause is the subject, use a singular verb: has."),
      ])

    G("gr_ifsubj", "Whether-clauses as the subject", 13, 1,
      "Use whether-clauses as the subject and keep declarative word order.", "nouncls", [
        q("___ she will accept the honour is unknown. Which word belongs in the blank?", "Whether",
          "If", "That", "What", "Use Whether, not If, to introduce a yes-or-no question in subject position."),
        q("Which sentence has the correct word order?", "Whether he is a genius is not important",
          "Whether is he a genius is not important", "If he is a genius is not important",
          "Whether he a genius is",
          "Use declarative word order in a whether-clause: he is."),
        q("It is uncertain ___ they discovered the cause. Which word belongs in the blank?", "whether",
          "that", "which", "who", "Use whether when it is uncertain whether something happened."),
        q("Which sentence cannot be used as a subject clause at the beginning of a sentence?", "If she will come is unknown",
          "Whether she will come is unknown", "That she will come is certain",
          "What she will say is unknown",
          "If cannot introduce a subject clause placed at the beginning of a sentence."),
      ])

    F("fu_people", "Describing a person's achievements", 13, 1,
      "Describe what a person did in chronological order and give an evaluation.", "fu_desc", [
        q("Which sentence says she devoted her life to research?", "She devoted her life to research",
          "Devoted she life research to", "She not devoted her life to research", "She devoted her life to rseearch",
          "devoted her life to summarizes a person's work."),
        q("Which sentence says it is not yet known whether she will receive the honour?", "Whether she will get the honour is unknown",
          "If she will get the honour is unknown", "Whether will she get the honour is unknown",
          "Unknown whether will she",
          "Use Whether at the beginning of the sentence, with the word order she will get."),
        q("Which sentence gives a conclusion before stating a fact?", "It is clear that his discovery changed medicine",
          "It is clear his discovery changed that", "Clear is that it discovery", "That clear it is",
          "It is clear that introduces an evaluation first."),
        q("Which sentence is suitable as the second step in a chronological account of a person?", "Next, he published the theory",
          "Next, he pbulished the theory", "Published he next the", "Next, he publisehd the theory",
          "Next connects one step to the next."),
      ])

    _p = "Tu Youyou devoted many years to research. It is now clear that her discovery saved a great number of patients. Whether every student knows her story is another question."
    R("rw_people", "Reading a passage about a person", 13, 1,
      "Infer the author's implied attitude and identify stated facts.", "rw_infer", [
        q(_p + " What did she devote many years to?", "research", "performing", "travel", "taking out a loan", "The passage says she devoted many years to research."),
        q(_p + " What did her discovery do?", "save many patients", "cancel the theory", "damage the laboratory", "The passage gives no result",
          "The passage says her discovery saved a great number of patients."),
        q(_p + " Which thing does the author say is still uncertain?", "whether every student knows her story", "whether the discovery was useful", "whether she did research", "whether the patients were saved",
          "Whether every student knows her story indicates that this is uncertain."),
        q(_p + " Which attitude does the author seem to have toward this discovery?", "that it is important", "that it has no value", "suspicion only about the patients", "no attitude",
          "Saving a great number of patients shows that the author considers the discovery important."),
      ])

    R("wr_people", "Writing a biographical sketch", 13, 1,
      "Choose sentences that include the key points of a biographical sketch.", "rw_write_s", [
        q("Key points: years of research, a discovery that saved patients, and not every student knows her. Which sentence includes all three?",
          "She devoted years to research, her discovery saved patients, and whether every student knows her is uncertain",
          "She did research", "Patients recovered", "Students are busy",
          "All three key points must be included."),
        q("Which sentence correctly uses a formal subject to evaluate the discovery?", "It is important that we remember this achievement",
          "It is important we remember that this", "Important that it we remember", "That important is it",
          "Use declarative word order after It is important that."),
        q("Which sentence is suitable as the first sentence of a biographical sketch?", "This paragraph introduces a scientist",
          "This paragraph introduce a scientist", "This paragraph introduces an scientist", "This paragraph itnroduces a scientist",
          "A sketch can begin by saying This paragraph introduces."),
        q("Which sentence has a subject clause introduced by Whether?", "Whether the story is widely known matters",
          "If the story is widely known matters", "Whether is the story known matters", "Matters whether is the story",
          "Use Whether at the beginning, with the word order the story is."),
      ])

    V("vo_robot", "Life in the future", 13, 2,
      "Recognize robot, automatic, predict, and innovation.",
      [("robot", "robot"), ("automatic", "automatic"), ("predict", "predict"), ("innovation", "innovation")], "vo_people")

    V("vo_smart", "Smart devices", 13, 2,
      "Recognize sensor, remote, appliance, and warning.",
      [("sensor", "sensor"), ("remote", "remote"), ("appliance", "household appliance"), ("network", "network")], "vo_people")

    G("gr_predcls", "Predicative clauses", 13, 2,
      "Use that, whether, or question words to introduce predicative clauses.", "nouncls", [
        q("The problem is ___ the sensor fails at night. Which word belongs in the blank?", "that",
          "which", "what", "who", "The clause is complete, so use that in the predicative clause."),
        q("The question is ___ the robot can cook. Which word means whether or not here?", "whether",
          "that", "which", "who", "Use whether to express whether something is true."),
        q("Which sentence has the correct word order?", "That is why the appliance stops",
          "That is why does the appliance stop", "That is why stops the appliance", "Why that is the appliance stops",
          "Use declarative word order in the predicative clause: the appliance stops."),
        q("What I need is ___ the network is stable. Which word belongs in the blank?", "that",
          "what", "which", "if", "The clause after is is complete, so use that."),
      ])

    G("gr_appos", "Appositive clauses", 13, 2,
      "Use that to introduce appositive clauses and distinguish them from relative clauses.", "nouncls", [
        q("The news ___ the robot won a prize is true. The missing word has no role in the clause. Which one belongs in the blank?", "that",
          "which", "what", "who", "The news is a complete fact, so use that to introduce an appositive clause."),
        q("Which sentence contains an appositive clause?", "The fact that the sensor failed surprised them",
          "The sensor that failed was new", "The robot which we bought is small", "The prize which he won is gold",
          "that the sensor failed gives the content of fact; that has no role in the clause."),
        q("Which sentence has a relative clause rather than an appositive clause?", "The report which he wrote is short",
          "The report that he was late is false", "The idea that robots will cook is new",
          "The news that she won is true",
          "In which he wrote, which is the object of wrote, so it is a relative clause."),
        q("We heard the warning ___ the network might break. Which word belongs in the blank?", "that",
          "which", "where", "whom", "Use an appositive clause with that to give the content of the warning."),
      ])

    F("fu_future", "Describing future devices", 13, 2,
      "Explain step by step how a device works.", "fu_desc", [
        q("Which sentence is suitable as the first step in an explanation of how a robot cooks?", "First, the sensor checks the food",
          "First, the snesor checks the food", "First, the senosr checks the food", "First, the sesor checks the food",
          "Use First to begin a sequence of steps."),
        q("Which sentence says that the problem is an unstable network?", "The problem is that the network is not stable",
          "The problem is that is the network not stable", "The problem is why does it stop",
          "Problem that the network",
          "Use that with declarative word order in a predicative clause."),
        q("Which sentence uses an appositive clause to report the content of a message?", "The news that the appliance can be controlled remotely is exciting",
          "The appliance that we bought is remote", "The news which excited us is short",
          "Exciting news is the appliance",
          "that the appliance can be controlled gives the content of the news."),
        q("Which sentence predicts that the innovation will save time?", "I predict that the innovation will save time",
          "I predict that will the innovation save time", "Predict I innovation time", "Save will time that",
          "Use declarative word order after predict that."),
      ])

    _u = "The new robot cooks by itself. The fact that its sensor failed yesterday explains the delay. The question is whether the network can be repaired today."
    R("rw_future", "Reading a passage about future life", 13, 2,
      "Use context to infer what went wrong with the sensor and what the author is still unsure about.", "rw_infer", [
        q(_u + " What does the robot do?", "cook by itself", "repair the network", "write news", "launch a rocket", "The passage says it cooks by itself."),
        q(_u + " Which component failed yesterday?", "the sensor", "the oven door", "the budget", "the lantern", "The passage says its sensor failed."),
        q(_u + " What caused the delay?", "the sensor failure", "the network was already repaired", "the robot cannot cook", "nothing",
          "The fact that its sensor failed explains the delay."),
        q(_u + " What is the author still unsure about?", "whether the network can be repaired today", "whether the robot can cook", "whether the sensor failed yesterday", "whether there was a delay",
          "Whether the network can be repaired is still uncertain."),
      ])

    R("wr_future", "Writing step-by-step instructions", 13, 2,
      "Choose sentences that include the key points of step-by-step instructions.", "rw_write_s", [
        q("Key points: the robot can cook, its sensor failed yesterday, and it is unknown whether the network can be repaired. Which sentence includes all three?",
          "The robot can cook, the sensor failed yesterday, and whether the network can be repaired is unknown",
          "The robot can cook", "Networks are useful", "Yesterday was busy",
          "All three key points must be included."),
        q("Which sentence correctly uses an appositive clause in the explanation?", "The fact that the sensor failed explains the delay",
          "The fact which the sensor failed explains the delay", "The fact that failed the sensor explains",
          "Fact the that sensor failed",
          "Use a that-clause to state the content of fact; that has no role in the clause."),
        q("Which sentence is suitable as the second step?", "Second, check whether the network is on",
          "Second, check wehther the network is on", "Whether check second is", "On the network whether",
          "Second connects to the next step; use declarative word order in the whether-clause."),
        q("Which sentence has a correct predicative clause?", "The problem is that the appliance stops suddenly",
          "The problem is that does the appliance stop", "The problem is why does it stop suddenly",
          "Is the problem that stops it",
          "Use declarative word order in the that-clause: the appliance stops."),
      ])

    V("vo_park", "Parks", 13, 3,
      "Recognize park, wildlife, boundary, and ranger.",
      [("park", "park"), ("boundary", "boundary"), ("ranger", "park ranger"), ("trail", "trail")], "vo_people")

    V("vo_reserve", "Nature conservation", 13, 3,
      "Recognize wetland, species, prohibit, and ecology.",
      [("wetland", "wetland"), ("ecology", "ecology"), ("prohibit", "prohibit"), ("binoculars", "binoculars")], "vo_people")

    G("gr_ingperf", "Perfect -ing forms", 13, 3,
      "Use having done for an action that happened before the main-clause action.", "nonfin", [
        q("___ the trail, they entered the wetland. Which option shows that they finished the trail first?", "Having walked",
          "Walking", "Walked", "To walk", "They walked the trail before entering the wetland, so use Having walked."),
        q("Which sentence shows that one action was completed before another?", "Having closed the gate, the ranger left",
          "Closing the gate, the ranger had already left", "Closed the gate, the ranger leaving",
          "The ranger left, having the gate close",
          "Having closed happened before left."),
        q("___ warned, visitors still fed the birds. Which option shows that they had already been warned?", "Having been",
          "Having", "Been having", "To have", "Use Having been warned to show that they had been warned."),
        q("Which sentence has an -ing clause that does not match its subject?", "Having flown away, the ranger looked up",
          "Having flown away, the birds left the tree", "The ranger, having checked the trail, rested",
          "Having been prohibited, the action stopped",
          "The birds flew away, not the ranger."),
      ])

    G("gr_with", "With + object + complement", 13, 3,
      "Use with followed by an object and a complement to describe an accompanying state.", "nonfin", [
        q("He waited, with the lights ___. Which word means the lights are on?", "on",
          "turned", "to on", "were on", "with the lights on is an absolute construction, with on as the complement."),
        q("With the problem ___, they went on. Which option means the problem had already been solved?", "solved",
          "solving", "solve", "to solving",           "The problem is the thing being solved, so use solved."),
        q("Which sentence is correct?", "She entered with a map in her hand",
          "She entered with a map was in her hand", "She entered with a map being was",
          "With a map was in her hand, she entered",
          "Do not add was after with a map in her hand."),
        q("With the ranger ___ the way, we did not get lost. Which option means the ranger was leading the way?", "leading",
          "led", "lead", "to lead", "The ranger leads the way actively, so use leading."),
      ], "inferred")

    F("fu_park", "Describing park rules", 13, 3,
      "Explain how to visit a park and what is prohibited, in order.", "fu_desc", [
        q("Which sentence says to close the gate before entering the wetland?", "Having closed the gate, enter the wetland quietly",
          "Closing after entered the gate", "Enter, having the gate close later", "Gate closed having enter",
          "Having closed means that the gate is closed first."),
        q("Which sentence says that feeding animals is prohibited?", "Feeding animals is prohibited",
          "Prohibited feeding are animals", "Feeding animals is porhibited", "Feeding animals is prohibietd",
          "Use is prohibited to state that something is forbidden."),
        q("Which sentence describes watching birds with binoculars in hand?", "She watched the birds with binoculars in her hand",
          "She watched with binoculars were in her hand", "With binoculars were, she watched",
          "Binoculars in hand were with",
          "Do not add were after with binoculars in her hand."),
        q("Which sentence says that the boundary has already been marked?", "The boundary has been marked on the map",
          "The boundary has marked the map", "Marked has been the boundary", "Boundary marking the map has",
          "Use has been marked for an action that has already been completed."),
      ])

    _k = "Having checked the map, we followed the trail into the wetland. Feeding birds is prohibited. With the ranger leading us, we stayed inside the boundary."
    R("rw_park", "Reading a passage about a park", 13, 3,
      "Read the passage and distinguish a rule from an action that has already happened.", "rw_argue", [
        q(_k + " What did they do before entering the wetland?", "check the map", "feed the birds", "leave the boundary", "turn off the lights",
          "Having checked the map happened before followed."),
        q(_k + " What is prohibited?", "feeding the birds", "checking the map", "walking the trail", "following the ranger", "The passage says feeding birds is prohibited."),
        q(_k + " Who is leading the way?", "the ranger", "the birds", "the map", "the boundary", "The passage says the ranger is leading them."),
        q(_k + " Which sentence states a rule rather than something that has already happened?", "Do not feed the birds",
          "They have already checked the map", "They have already followed the trail", "The ranger is already leading the way",
          "is prohibited states a rule. Having checked describes an action already completed."),
      ])

    R("wr_park", "Writing visitor instructions", 13, 3,
      "Choose sentences that include the key points of visitor instructions.", "rw_write_s", [
        q("Key points: check the map first, do not feed the animals, and follow the ranger. Which sentence includes all three?",
          "Having checked the map, remember that feeding is prohibited, and follow the ranger",
          "Check the map", "Feeding is bad", "Rangers are helpful",
          "All three key points must be included."),
        q("Which sentence shows that one action is completed before moving on?", "Having read the rules, start along the trail",
          "Reading the rules after you finish the trail first", "Read having the rules, start",
          "The trail having read you",
          "Having read means the rules are read first."),
        q("Which sentence is suitable as the title of the instructions?", "How to visit the wetland",
          "How to visiting the wetland", "How to visits the wetland", "How to visit the wteland",
          "Use How to visit for instructions."),
        q("Which sentence uses the with-construction correctly?", "Walk with the map in your pocket",
          "Walk with the map is in your pocket", "With the map is, walk", "Pocket with map is walk",
          "Do not add is after with the map in your pocket."),
      ])

    V("vo_body", "Body language", 13, 4,
      "Recognize gesture, posture, expression, and contact.",
      [("gesture", "gesture"), ("posture", "posture"), ("expression", "expression"), ("contact", "contact")], "vo_people")

    V("vo_gesture", "Facial expressions and distance", 13, 4,
      "Recognize frown, nod, distance, and interpret.",
      [("frown", "frown"), ("nod", "nod"), ("distance", "distance"), ("interpret", "interpret")], "vo_people")

    G("gr_havedone", "Perfect and passive non-finite forms", 13, 4,
      "Use having been done in context to show an action was completed passively before another action.", "nonfin", [
        q("___ by the host, the guests sat down. Which option says they had already been greeted?", "Having been greeted",
          "Having greeted", "Greeted having", "To have greeting",
          "The guests were greeted before they sat down, so use Having been greeted."),
        q("Which sentence shows that someone was asked before answering?", "Having been asked, she nodded",
          "Having asked, she was nodded", "Asked having been, nodded she", "Being ask, she nodded",
          "Having been asked shows that she was asked first."),
        q("The man seemed ___ the gesture. Which option means he seemed to have already misunderstood the gesture?", "to have misunderstood",
          "to misunderstand yesterday", "misunderstanding been", "have misunderstand",
          "Use to have misunderstood for an action that happened before seemed."),
        q("Which sentence reverses the active and passive meanings?", "Having been nodded, the head smiled",
          "Having nodded, he sat down", "Having been shown the sign, she understood",
          "The guest, having been invited, arrived",
          "People nod; a head cannot be nodded and then smile on its own."),
      ])

    G("gr_sense", "Object complements after verbs of perception", 13, 4,
      "Choose the bare infinitive or -ing form after see, hear, and notice.", "nonfin", [
        q("I saw her ___. Which option shows that you saw the whole nodding action?", "nod",
          "to nod", "nodded", "to nodding", "Use the bare infinitive nod after see to describe the whole action."),
        q("I saw her ___ at me when I entered. Which option shows that you saw her frowning as you came in?", "frowning",
          "frown", "to frown", "frowned", "Use frowning to emphasize an action in progress."),
        q("Which sentence is correct?", "We heard someone calling his name",
          "We heard someone to call his name", "We heard someone called to his name",
          "We heard someone to calling",
          "Do not use to call after hear; use calling for an action in progress."),
        q("She was seen entering the room. Which passive sentence is correct?", "She was seen to enter the room",
          "She was seen enter the room", "She was seen entering to the room", "Seen was she enter",
          "In the active see someone do construction, restore to in the passive: was seen to enter."),
      ], "inferred")

    F("fu_body", "Describing body language", 13, 4,
      "Describe a gesture or expression and explain what it may mean.", "fu_desc", [
        q("Which sentence says that a nod often means agreement?", "A nod often means agreement",
          "A nod often mean agreement", "A nod often means argeement", "A nod often means agreemnet",
          "Use means agreement to explain the gesture."),
        q("Which sentence says that you saw her frown once, emphasizing the whole action?", "I saw her frown",
          "I saw her to frown", "I saw her frowned", "Saw I her to frown",
          "Omit to in see her frown."),
        q("Which sentence says the guests sat down after they had been greeted?", "Having been greeted, the guests sat down",
          "Having greeted, the guests were sat by the host", "Greeted having been the guests sat",
          "The guests sat, having greet",
          "Having been greeted shows that they were greeted first."),
        q("Which sentence reminds someone to keep a suitable distance?", "Please keep a comfortable distance",
          "Please keep an comfortable distance", "Keep is an expression", "Please keep a cmofortable distance",
          "Use the imperative Please keep to give a reminder."),
      ])

    _b = "Having been greeted, the guests sat down. I saw the host nod, which I interpreted as agreement. A frown, however, made the speaker keep a greater distance."
    R("rw_body", "Reading a passage about body language", 13, 4,
      "Use context to infer what the nod and frown suggest.", "rw_infer", [
        q(_b + " What happened before the guests sat down?", "They were greeted", "They frowned", "They left", "They nodded to refuse",
          "Having been greeted happened before sat down."),
        q(_b + " What did the author interpret the nod as?", "agreement", "refusal", "too much distance", "a lack of understanding", "The passage says it was interpreted as agreement."),
        q(_b + " What did the frown make the speaker do?", "keep a greater distance", "sit down immediately", "move closer", "start nodding",
          "The passage says to keep a greater distance."),
        q(_b + " What does which most likely refer to in the passage?", "the host's nod", "the guest", "the word distance", "the person who frowned",
          "which I interpreted follows nod and refers to the act of nodding."),
      ])

    R("wr_body", "Writing observation notes", 13, 4,
      "Choose sentences that include the key points of observation notes.", "rw_write_s", [
        q("Key points: they were greeted first, a nod showed agreement, and a frown made the speaker step back. Which sentence includes all three?",
          "Having been greeted they sat down, a nod meant agreement, and a frown made the speaker keep a distance",
          "They sat down", "A nod is a gesture", "Distance matters",
          "All three key points must be included."),
        q("Which sentence says that you saw the whole action?", "I saw her nod once",
          "I saw her to nod once", "I saw her nodded once", "Saw her I to nod",
          "Do not use to in see her nod."),
        q("Which sentence is suitable as the first sentence of the notes?", "I watched how people used gestures",
          "I watched how people used gsetures", "I watched how people used gestuers", "I watched how people used getures",
          "The notes can begin with I watched how."),
        q("Which sentence correctly restores to in the passive?", "He was noticed to leave early",
          "He was noticed leave early", "He was noticed to leaving early", "Noticed was he leave",
          "Use to leave after was noticed."),
      ])

    V("vo_farm", "Agriculture", 13, 5,
      "Recognize agriculture, crop, soil, and harvest.",
      [("agriculture", "agriculture"), ("crop", "crop"), ("soil", "soil"), ("harvest", "harvest")], "vo_people")

    V("vo_crop", "Farming", 13, 5,
      "Recognize fertilizer, irrigation, yield, and organic.",
      [("fertilizer", "fertilizer"), ("irrigation", "irrigation"), ("yield", "yield"), ("organic", "organic")], "vo_people")

    G("gr_topass", "Passive infinitives", 13, 5,
      "Use to be done to describe something that will or should be done.", "nonfin", [
        q("The crops are ___ tomorrow. Which option says they will be harvested tomorrow?", "to be harvested",
          "to harvest", "harvesting", "harvested be", "The crops are harvested by someone, so use to be harvested."),
        q("Which sentence is correct?", "The soil needs to be tested",
          "The soil needs to test", "The soil needs to be test", "The soil needs tested be",
          "The soil is the object being tested, so use to be tested."),
        q("There is a report ___ before Friday. Which option says the report will be completed?", "to be finished",
          "to finish", "finishing", "finished to", "The report is to be completed, so use to be finished as a modifier."),
        q("Which sentence reverses the active and passive meanings?", "The farmer is to be grown by the wheat",
          "The wheat is to be grown by the farmer", "The farmer hopes to grow wheat",
          "The field is to be irrigated",
          "The wheat is grown, not the farmer."),
      ])

    G("gr_abs", "Absolute constructions", 13, 5,
      "Recognize an absolute construction: a noun plus a participle whose logical subject differs from the main clause's subject.", "nonfin", [
        q("Weather ___, we will start the harvest. Which option means that we will start if the weather allows?", "permitting",
          "permitted", "permits", "to permitting", "Weather allows it, so use permitting in this absolute construction."),
        q("The work ___, the farmers went home. Which option says the work had already been completed?", "finished",
          "finishing", "finish", "to finish", "The work is completed, so use finished."),
        q("Which sentence is an absolute construction rather than an ordinary adverbial clause?", "The soil tested, they chose the fertilizer",
          "Having tested the soil, they chose the fertilizer", "Tested by them, the soil was poor",
          "They tested the soil and chose the fertilizer",
          "The logical subject soil in The soil tested differs from the main clause subject they."),
        q("Which sentence is correct?", "Time permitting, we will check the irrigation",
          "Time permitted, we will check if time allows us now as a person", "Permitting time, the clock left",
          "Time permitting we will to check",
          "Time permitting means if time allows."),
      ], "inferred")

    F("fu_farm", "Explaining farming processes", 13, 5,
      "Explain farming steps and give evidence-based opinions about yield and soil.", "fu_argue", [
        q("Which sentence says that the soil needs to be tested?", "The soil needs to be tested",
          "The soil needs to test the farmer", "Tested to be needs the soil", "Soil is testing the lab",
          "needs to be tested describes an action done to the soil."),
        q("Which sentence says that harvesting will begin if the weather allows?", "Weather permitting, we will start the harvest",
          "Weather permitted by us, the sky starts", "Permitting weather we start to", "Harvest permits the weather",
          "Weather permitting is an absolute construction."),
        q("Which sentence says that organic fertilizer may increase the yield?", "Organic fertilizer may increase the yield",
          "Organic fertilizer may increased the yield", "Organic fertilizer may to increase the yield", "Organic fretilizer may increase the yield",
          "may increase presents a possibility supported by evidence."),
        q("Which sentence gives a reason against using too much fertilizer?", "Too much fertilizer can damage the soil",
          "Damage can the soil fertilizer too", "Fertilizer is always harmless", "Soil damages the sentence",
          "can damage gives a reason against over-fertilizing."),
      ])

    _g = "The wheat is to be harvested next week. Soil samples need to be tested first. Weather permitting, the farmers will finish the work in three days."
    R("rw_farm", "Reading a passage about agriculture", 13, 5,
      "Read the passage and identify what must happen first and what still depends on the weather.", "rw_argue", [
        q(_g + " When will the wheat be harvested?", "next week", "yesterday", "in three years", "It will not be harvested", "The passage says next week."),
        q(_g + " What needs to be tested first?", "soil samples", "the weather", "the farmers", "the price of irrigation equipment", "The passage says soil samples need to be tested."),
        q(_g + " What does finishing the work in three days depend on?", "the weather allowing it", "the tests having failed", "the wheat deciding for itself", "nothing",
          "Weather permitting means that it depends on the weather."),
        q(_g + " Which item is acted upon rather than an action initiated by the farmers?", "the soil samples being tested",
          "the farmers finishing the work", "the farmers choosing the date", "The passage has no passive voice",
          "samples need to be tested is passive; farmers will finish is active."),
      ])

    R("wr_farm", "Writing a farming schedule", 13, 5,
      "Choose sentences that include the key points of a farming schedule.", "rw_write_s", [
        q("Key points: harvest next week, test the soil first, and finish in three days if the weather allows. Which sentence includes all three?",
          "The wheat is to be harvested next week, the soil is to be tested first, and weather permitting they will finish in three days",
          "The wheat is ripe", "Soil is important", "Three days is short",
          "All three key points must be included."),
        q("Which sentence correctly uses a passive infinitive in the schedule?", "The field is to be irrigated tonight",
          "The field is to irrigate tonight", "The field is to be irrigate tonight", "Irrigated is to the field be",
          "is to be irrigated means that the field will be irrigated."),
        q("Which sentence is suitable as the first sentence of the schedule?", "Here is the plan for the harvest",
          "Here are the plan for the harvest", "Here is the plan for the hravest", "Here is the plan for the harvset",
          "A schedule can begin with Here is the plan."),
        q("Which sentence is an absolute construction?", "Time permitting, we will test two more fields",
          "Having time, we will test two more fields", "We permit the time to test", "Permitting, time tests us",
          "The subject time in Time permitting differs from the main clause subject we."),
      ])
