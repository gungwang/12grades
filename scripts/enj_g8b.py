# -*- coding: utf-8 -*-
"""Grade 8, second semester. The unit sequence follows the commonly used People's Education Press Go for it! table of contents; unit names and volume placement remain to be verified."""
from en_tx import V, P, G, F, R


def q(prompt, answer, wrongs, expl):
    return ("c", prompt, answer, wrongs, expl)


V("vo_health", "Health Problems", 8, "Second semester", 1,
  "Recognize the words headache, stomachache, fever, and cough.",
  [("headache", "pain in the head"), ("stomachache", "pain in the stomach"), ("fever", "a high body temperature"), ("cough", "a cough")], "vocab8")

G("gr_should8", "Using Should for Advice", 8, "Second semester", 1,
  "Use should or shouldn't to give advice.", "modal", [
    q("You should go to a doctor. Which sentence is correct?", "You should see a doctor.",
      ["You should to see a doctor.", "You should sees a doctor.", "You should seeing a doctor."],
      "Use the base form of the verb after should."),
    q("You shouldn't eat so much. Which sentence is correct?", "You shouldn't eat so much.",
      ["You shouldn't to eat so much.", "You shouldn't eats so much.", "You don't should eat so much."],
      "Use the base form of the verb after shouldn't."),
    q("She has a toothache. Which piece of advice is appropriate?", "She should see a dentist.",
      ["She should sees a dentist.", "She should to see a dentist.", "She should seeing a dentist."],
      "Use should see."),
    q("What does should express in these sentences?", "Advice",
      ["A fact in the past", "An action in progress", "A completed action"],
      "Use should to tell someone what would be a good idea to do."),
])

F("fu_health", "Checking on Someone's Health", 8, "Second semester", 1,
  "Ask someone what is wrong and give simple advice.", "func_life", [
    q("A classmate looks unwell. Which question is appropriate?", "What's the matter?",
      ["What's the matter yesterday happened?", "What the matter is you?", "How the matter are you?"],
      "Use What's the matter? to ask what is wrong."),
    q("You have a headache. What should you say?", "I have a headache.",
      ["I have headache.", "I has a headache.", "I have an headache."],
      "Say have a headache."),
    q("The other person has a fever, and you suggest lying down. Which sentence is appropriate?", "You should lie down and rest.",
      ["You should lies down and rest.", "You should to lie down and rest.", "You should lying down and rest."],
      "Use should lie."),
    q("The other person says, 'I have a cough.' You want to ask how long it has lasted. Which question is appropriate?", "How long have you had it?",
      ["How long did you had it tomorrow?", "How far have you had it?", "How often you have it yesterday now?"],
      "Use How long to ask about duration."),
])

R("rw_health", "Reading Health Advice", 8, "Second semester", 1,
  "Read a dialogue and identify the symptoms and advice.", "read_detail", [
    q("Ben has a stomachache. The doctor says he should not eat cold food. What is wrong with him?", "A stomachache",
      ["A headache", "A cough", "A toothache"], "He has a stomachache."),
    q("Ben has a stomachache. The doctor says he should not eat cold food. What does the doctor advise him to do?", "Avoid cold food",
      ["Eat more ice cream", "Go running", "Do not rest"], "The doctor says he should not eat cold food."),
    q("Lisa has a fever and a cough. She should drink more water. What should she do?", "Drink more water",
      ["Drink less water", "Eat more candy", "The passage does not say"], "She should drink more water."),
    q("Lisa has a fever and a cough. Which sentence matches the passage?", "Lisa has both a fever and a cough.",
      ["Lisa only has a headache.", "Lisa should not drink water.", "Ben has a fever in this sentence."],
      "She has both a fever and a cough."),
])

V("vo_vol", "Volunteer Service", 8, "Second semester", 2,
  "Recognize the words volunteer, lonely, sign, and notice.",
  [("volunteer", "a person who works without pay"), ("lonely", "sad because of being alone"), ("sign", "a board that gives information"), ("notice", "a short written announcement")], "vocab8")

G("gr_purpose", "Infinitives to Express Purpose", 8, "Second semester", 2,
  "Use to plus the base form of a verb to explain the purpose of an action.", "to_ing", [
    q("I went to the park to volunteer. Which sentence is correct?", "I went to the park to volunteer.",
      ["I went to the park for volunteer.", "I went to the park volunteering.", "I went to the park to volunteering."],
      "To volunteer expresses the purpose."),
    q("She put up a notice to find helpers. Which sentence is correct?", "She put up a notice to find helpers.",
      ["She put up a notice find helpers.", "She put up a notice to found helpers.", "She put up a notice for find helpers."],
      "To find expresses the purpose."),
    q("What does to do express when it appears later in a sentence?", "Purpose",
      ["Past time", "An object of comparison", "A passive action"],
      "An infinitive can explain why an action is done."),
    q("They raise money to help the poor. Which sentence is correct?", "They raise money to help the poor.",
      ["They raise money help the poor.", "They raise money to helping the poor.", "They raise money for to help the poor."],
      "To help states the purpose."),
])

F("fu_help", "Offering to Help", 8, "Second semester", 2,
  "Offer help and say what you can do.", "func_plan", [
    q("You want to say that you could hand out food. Which sentence is appropriate?", "I could give out food.",
      ["I could to give out food.", "I could giving out food.", "I could gave out food."],
      "Use the base form of the verb after could."),
    q("You want to ask whether someone would like to volunteer. Which question is appropriate?", "Would you like to help?",
      ["Would you like helping out yesterday?", "Do you would like to help?", "Would you like help?"],
      "Ask, 'Would you like to help?'"),
    q("Which sentence clearly describes what lonely older people need?", "They need someone to talk to.",
      ["They need someone talk to.", "They need someone to talking to.", "They need someone for talk."],
      "Use someone to talk to."),
    q("What does 'I'll help to clean up the park' do?", "Offers to help clean up the park",
      ["Refuse to clean", "Ask where the park is", "Compare two parks"],
      "'I'll help to' expresses willingness to help."),
])

R("rw_help", "Reading About Volunteer Work", 8, "Second semester", 2,
  "Read a notice and identify when the activity takes place and what volunteers need to do.", "read_detail", [
    q("We need volunteers to clean up the city park on Saturday. Please call Mr. Li. What do the volunteers need to do?", "Clean up the city park",
      ["Build a hospital", "Sell tickets", "Drive a car"], "They will clean up the city park."),
    q("We need volunteers to clean up the city park on Saturday. What day is the activity?", "Saturday",
      ["Sunday", "Monday", "Friday"], "It takes place on Saturday."),
    q("Anna wants to help. She will give out notices after school. What will she do after school?", "Hand out notices",
      ["Clean her room", "Go to the doctor", "Stay at home"], "She will give out notices."),
    q("Anna wants to help. She will give out notices after school. Which sentence matches the passage?", "Anna will hand out notices after school.",
      ["Anna will not help.", "The park clean-up is on Monday.", "Mr. Li will give out food at the hospital."],
      "She will give out notices after school."),
])

V("vo_chore", "Household Chores", 8, "Second semester", 3,
  "Recognize the words chore, rubbish, fold, and sweep.",
  [("chore", "a small job done around the home"), ("rubbish", "waste material"), ("fold", "bend something over itself"), ("sweep", "clean with a broom")], "vocab8")

G("gr_could", "Using Could for Polite Requests", 8, "Second semester", 3,
  "Make polite requests with Could you please.", "modal", [
    q("Could you please clean your room? Which sentence is correct?", "Could you please clean your room?",
      ["Could you please to clean your room?", "Could you please cleaning your room?", "Could you please cleaned your room?"],
      "Use the base form of the verb after Could you please."),
    q("Which response agrees to a request?", "Yes, sure.",
      ["Yes, I could please.", "No, here you are not doing.", "Yes, I couldn't do it gladly."],
      "Yes, sure expresses agreement."),
    q("You do not want to take out the rubbish. Which sentence is correct?", "I don't want to take out the rubbish.",
      ["I don't want take out the rubbish.", "I don't want to taking out the rubbish.", "I doesn't want to take out the rubbish."],
      "Use want to take."),
    q("How is Could you please different from Can you?", "It is more polite",
      ["Can only be used for the past", "Must be followed by -ing", "Cannot be used to make requests"],
      "Could makes a request more polite."),
])

F("fu_chore", "Making Polite Requests", 8, "Second semester", 3,
  "Ask someone to do a chore and respond politely.", "func_life", [
    q("You want to ask your younger brother to fold the clothes. Which sentence is appropriate?", "Could you please fold the clothes?",
      ["Could you please folds the clothes?", "Could you please to fold the clothes?", "Do you could fold the clothes?"],
      "Use Could you please fold."),
    q("You are doing homework and cannot sweep the floor. What should you say?", "Sorry, I am doing my homework.",
      ["Sorry, I do my homework now yesterday.", "Sorry, I doing my homework.", "Sorry, I am do my homework."],
      "Am doing describes an action in progress."),
    q("What does 'Could I go out for dinner?' do?", "Asks permission to go out for dinner",
      ["Tell someone to cook", "Describe last night's dinner", "Compare two restaurants"],
      "Use Could I to ask for permission."),
    q("You agree to let your younger brother borrow your bike. Which response is appropriate?", "Yes, you can. But please return it later.",
      ["Yes, you could please return yesterday.", "No, you can take it and never say.", "Yes, you can returns it."],
      "After agreeing, you can add a request to return it later."),
])

R("rw_chore", "Reading a Chores Dialogue", 8, "Second semester", 3,
  "Read a dialogue and identify who needs to do each chore.", "read_detail", [
    q("Mom: Could you please sweep the floor? Peter: Sure. What does Mom ask Peter to do?", "Sweep the floor",
      ["Take out the rubbish", "Fold the clothes", "Wash the dishes"], "She asks him to sweep the floor."),
    q("Mom: Could you please sweep the floor? Peter: Sure. Does Peter agree?", "Yes",
      ["No", "He has not answered yet", "He asks Mom to do it"], "Sure expresses agreement."),
    q("Lucy has to fold the clothes and take out the rubbish. She will not wash the car. Does she have to wash the car?", "No",
      ["Yes", "She only has to wash the car", "The passage does not say"], "She will not wash the car."),
    q("Lucy has to fold the clothes and take out the rubbish. Which sentence matches the passage?", "Lucy will fold the clothes.",
      ["Lucy will wash the car.", "Peter will not sweep the floor.", "Lucy does not take out the rubbish."],
      "Folding the clothes is one of her chores."),
])

V("vo_mood", "Feelings and Stress", 8, "Second semester", 4,
  "Recognize the words pressure, argue, nervous, and proper.",
  [("pressure", "a feeling of stress"), ("argue", "speak angrily because of disagreement"), ("nervous", "worried or afraid"), ("proper", "right or suitable")], "vocab8")

G("gr_although", "Although for Contrast", 8, "Second semester", 4,
  "Use although to connect contrasting ideas, and do not use it together with but.", "clause_adv", [
    q("Although he was tired, he finished his homework. Which sentence is correct?", "Although he was tired, he finished his homework.",
      ["Although he was tired, but he finished his homework.", "Although he was tired, so he finished his homework.", "Although he is tired, he finished his homework yesterday without a tense."],
      "Do not use although and but together."),
    q("Although she was nervous, she still went on stage. Which sentence is correct?", "Although she was nervous, she went on the stage.",
      ["Although she was nervous, but she went on the stage.", "Although she nervous, she went on the stage.", "Although she was nervous, she goes on the stage yesterday."],
      "Follow Although with the result; do not add but."),
    q("Which word is closest in meaning to although?", "Although / even though",
      ["Because", "So", "Unless"],
      "Although introduces a contrast."),
    q("Which sentence uses although correctly?", "Although they argue, they still love each other.",
      ["Although they argue, but they still love each other.", "Although they argue, so they still love each other.", "But although they argue, they still love."],
      "Keep although and remove but."),
])

F("fu_advice8", "Giving Advice with Why Don't You", 8, "Second semester", 4,
  "Give advice using Why don't you or Why not.", "func_plan", [
    q("You want to suggest that someone talk to their parents. Which sentence is appropriate?", "Why don't you talk to your parents?",
      ["Why don't you to talk to your parents?", "Why not you talk to your parents?", "Why don't you talking to your parents?"],
      "Use the base form of the verb after Why don't you."),
    q("What does 'Why not write him a letter?' do?", "Suggests writing a letter",
      ["Ask the price of a letter", "Describe a letter that has already been written", "Refuse to write a letter"],
      "Use Why not plus the base form of a verb to give advice."),
    q("You think the other person should calm down first. Which sentence is appropriate?", "You should calm down first.",
      ["You should to calm down first.", "You should calms down first.", "You should calming down first."],
      "Use should calm."),
    q("You want to say that you are under too much pressure. Which sentence is appropriate?", "I have too much pressure.",
      ["I have too many pressure.", "I have too much pressures.", "I has too much pressure."],
      "Pressure is uncountable here, so use too much."),
])

R("rw_letter8", "Reading an Advice Letter", 8, "Second semester", 4,
  "Read a short letter and identify the problem and the advice.", "read_detail", [
    q("Dear Linda, I argued with my parents. I feel nervous. What should I do? What is the writer's problem?", "The writer argued with their parents and feels nervous",
      ["The writer got a perfect score on an exam", "The writer volunteered at a park", "The writer has a fever"], "The writer argued with their parents and feels nervous."),
    q("Linda says: Why don't you talk to them? Although you are upset, they love you. What does Linda advise?", "Talk to them",
      ["Stop speaking to them", "Leave home", "Keep arguing with them"], "She asks the writer to talk to them."),
    q("Although you are upset, they love you. What else does this sentence say?", "Even though you are upset, they still love you",
      ["They do not love you", "You are not upset", "Linda is nervous"], "Although introduces a contrast; their love remains true."),
    q("Linda says: Why don't you talk to them? Which sentence matches the reply?", "Linda advises a talk with the parents.",
      ["Linda tells the writer to argue again.", "The writer is not nervous.", "The parents do not love the writer."],
      "The advice is to talk to them."),
])

V("vo_storm", "Rainstorms", 8, "Second semester", 5,
  "Recognize the words rainstorm, alarm, flashlight, and wind.",
  [("rainstorm", "a storm with heavy rain"), ("alarm", "a device that gives a warning or wakes someone"), ("flashlight", "a portable electric light"), ("wind", "moving air")], "vocab8")

G("gr_pasting", "Past Continuous", 8, "Second semester", 5,
  "Use was or were plus a verb ending in -ing to describe an action in progress at a time in the past.", "pastcont", [
    q("I was reading at eight last night. Which sentence is correct?", "I was reading at eight last night.",
      ["I was read at eight last night.", "I were reading at eight last night.", "I reading at eight last night."],
      "Use was reading with I."),
    q("They were sleeping at that time. Which sentence is correct?", "They were sleeping at that time.",
      ["They was sleeping at that time.", "They were sleep at that time.", "They sleeping at that time."],
      "Use were sleeping with they."),
    q("What is the structure of the past continuous?", "Was or were plus a verb ending in -ing",
      ["Did plus the base verb", "Have plus a past participle", "Will plus the base verb"],
      "Use was or were plus a verb ending in -ing."),
    q("She wasn't watching TV then. Which sentence is correct?", "She wasn't watching TV then.",
      ["She wasn't watch TV then.", "She weren't watching TV then.", "She not watching TV then."],
      "Use wasn't watching."),
])

G("gr_whenwhile", "When and While", 8, "Second semester", 5,
  "Use when to connect a short action and while to connect an action in progress.", "pastcont", [
    q("I was reading when the rainstorm came. Which sentence is correct?", "I was reading when the rainstorm came.",
      ["I was reading when the rainstorm was come.", "I read when the rainstorm was coming at that long time only.", "I was read when the rainstorm came."],
      "The arrival of the storm is a short action, so use when; use the past continuous for reading."),
    q("My brother was watching TV while I was sleeping. Which sentence is correct?", "While I was sleeping, my brother was watching TV.",
      ["While I slept a short knock, my brother was watching TV.", "While I was sleep, my brother was watching TV.", "While I was sleeping, my brother watched TV for a long time in the same pattern."],
      "Two actions happening over the same period can both use the past continuous, with while introducing one of them."),
    q("What does came describe in 'when the rainstorm came'?", "A short, sudden action",
      ["A long-standing habit", "A future plan", "A present state"],
      "Came describes the moment the rainstorm arrived."),
    q("Which sentence uses while appropriately?", "While Mary was calling, the bell rang.",
      ["While the bell rang for one second, Mary was calling all night without while.", "While Mary called once, the bell was ringing for hours in this beginner pattern.", "While the bell rang, Mary was call."],
      "Use while before the longer action, was calling."),
])

F("fu_storm", "Describing Actions in Progress", 8, "Second semester", 5,
  "Ask what someone was doing at a particular time in the past.", "func_life", [
    q("You want to ask what someone was doing when the rainstorm arrived. Which question is appropriate?", "What were you doing when the rainstorm came?",
      ["What were you do when the rainstorm came?", "What did you doing when the rainstorm came?", "What were you doing when the rainstorm comes?"],
      "Use were you doing; use came in the when-clause."),
    q("You were taking a shower at that time. What should you say?", "I was taking a shower.",
      ["I was take a shower.", "I were taking a shower.", "I taking a shower."],
      "Use was taking."),
    q("What does 'While the wind was blowing, I felt scared' mean?", "I felt scared while the wind was blowing",
      ["The wind has not started yet", "I will be scared tomorrow", "I did not feel scared"],
      "While shows that the fear occurred during the period of wind."),
    q("Your alarm did not ring. Which sentence is appropriate?", "My alarm did not go off.",
      ["My alarm did not went off.", "My alarm was not go off.", "My alarm not went off."],
      "Use did not go off."),
])

R("rw_storm", "Reading a Rainstorm Story", 8, "Second semester", 5,
  "Read a story and identify what people were doing when the rainstorm arrived.", "read_detail", [
    q("When the rainstorm came, Ben was reading. His sister was sleeping. What was Ben doing when the storm arrived?", "Reading",
      ["Sleeping", "Taking a shower", "Sweeping the floor"], "Ben was reading."),
    q("When the rainstorm came, Ben was reading. His sister was sleeping. What was his sister doing?", "Sleeping",
      ["Reading", "Watching the news", "Cooking"], "She was sleeping."),
    q("While the wind was blowing, the lights went out. Mom was making dinner. What was Mom doing when the lights went out?", "Making dinner",
      ["Sleeping", "Reading a newspaper", "At the park"], "Mom was making dinner."),
    q("While the wind was blowing, the lights went out. Which sentence matches the passage?", "The lights went out while the wind was blowing.",
      ["The lights went out before there was any wind.", "Ben was sleeping when the rainstorm came.", "Mom was reading in the park."],
      "The lights went out while the wind was blowing."),
])

V("vo_story", "Story Vocabulary", 8, "Second semester", 6,
  "Recognize the words emperor, stupid, stone, and weak.",
  [("emperor", "the ruler of an empire"), ("stupid", "not intelligent"), ("stone", "a small piece of rock"), ("weak", "not strong")], "vocab8")

G("gr_unless", "Unless for Conditions", 8, "Second semester", 6,
  "Use unless to mean if not; use the simple present tense in the unless-clause.", "clause_adv", [
    q("You will be late unless you hurry. Which sentence is correct?", "You will be late unless you hurry.",
      ["You will be late unless you will hurry.", "You will be late unless you hurried yesterday.", "You are late unless you will hurry tomorrow."],
      "Use hurry in the unless-clause and will be in the main clause."),
    q("Which phrase is closest in meaning to unless?", "If not",
      ["Because", "Although", "So that"],
      "Unless means if not."),
    q("We cannot move the stone unless he helps. Which sentence is correct?", "We cannot move the stone unless he helps.",
      ["We cannot move the stone unless he will help.", "We cannot move the stone unless he help.", "We could not move the stone unless he helps tomorrow in the past."],
      "Use unless he helps."),
    q("Which sentence is closest in meaning to 'If you do not try, you will not win'?", "You will not win unless you try.",
      ["You will not win unless you will try.", "You will win unless you try.", "Unless you try, you will win."],
      "Unless you try means if you do not try."),
])

G("gr_sothat", "So That for Purpose", 8, "Second semester", 6,
  "Use so that to express purpose; the clause often includes can or could.", "clause_adv", [
    q("He got up early so that he could catch the bus. Which sentence is correct?", "He got up early so that he could catch the bus.",
      ["He got up early so that he catch the bus.", "He got up early to that he could catch the bus.", "He got up early so that he can caught the bus."],
      "Use so that he could catch."),
    q("What does so that express in this sentence?", "Purpose",
      ["Concession", "Comparison", "Passive voice"],
      "So that introduces the intended result."),
    q("She left a note so that her parents could see it. Which sentence is correct?", "She left a note so that her parents could see it.",
      ["She left a note so that her parents can saw it.", "She left a note for that her parents could see it.", "She left a note so that her parents see it yesterday."],
      "Use could see."),
    q("Which phrase can introduce a purpose clause?", "so that",
      ["as tall as", "more than", "ever since"],
      "Follow so that with a complete purpose clause."),
])

F("fu_story", "Retelling a Story", 8, "Second semester", 6,
  "Retell the characters and events of a story using the simple past tense.", "func_life", [
    q("Which sentence is a suitable opening for a story?", "Once upon a time, there was an old man.",
      ["Once upon a time, there is an old man yesterday.", "Once upon a time, there were an old man.", "Once upon a time, there was a old man."],
      "Use there was an old man."),
    q("The old man kept trying to move the mountain. Which sentence is appropriate?", "The old man kept trying to move the mountain.",
      ["The old man kept try to move the mountain.", "The old man kept to trying move the mountain.", "The old man kept trying move the mountain."],
      "Use kept trying to move."),
    q("Other people thought this was foolish. Which sentence is appropriate?", "Other people thought it was stupid.",
      ["Other people thought it is stupid yesterday.", "Other people think it was stupid now past.", "Other people thought it were stupid."],
      "Use thought it was stupid."),
    q("You want to say that he did not give up. Which sentence is appropriate?", "He did not give up.",
      ["He did not gave up.", "He did not giving up.", "He not gave up."],
      "Use did not give up."),
])

R("rw_story", "Reading a Myth", 8, "Second semester", 6,
  "Read a story and identify what the characters did.", "read_detail", [
    q("An old man tried to move the mountains. His family kept working every day. What did the old man try to do?", "Move the mountains",
      ["Build a palace", "Find an emperor", "Leave the village"], "He tried to move the mountains."),
    q("An old man tried to move the mountains. His family kept working every day. What did his family do?", "They kept working every day",
      ["They gave up at once", "They watched without helping", "They moved away"], "They kept working every day."),
    q("A god thought the man was weak, but he sent two gods to help. Who came to help?", "Two gods",
      ["The emperor", "The neighbors", "No one"], "Two gods came to help."),
    q("A god thought the man was weak, but he sent two gods to help. Which sentence matches the story?", "The gods came to help the man.",
      ["The man gave up at once.", "The family never worked.", "The god refused to help."],
      "The god sent two gods to help."),
])

V("vo_geo", "Geography Vocabulary", 8, "Second semester", 7,
  "Recognize the words desert, ocean, ancient, and protect.",
  [("desert", "a large, dry area of land"), ("ocean", "a very large body of salt water"), ("ancient", "belonging to a very long time ago"), ("protect", "keep safe from harm")], "vocab8")

G("gr_high", "Choosing Comparatives and Superlatives", 8, "Second semester", 7,
  "Choose the comparative for two items and the superlative for three or more.", "compare", [
    q("Qomolangma is the highest mountain in the world. Which sentence is correct?", "Qomolangma is the highest mountain in the world.",
      ["Qomolangma is the higher mountain in the world.", "Qomolangma is highest mountain in the world.", "Qomolangma is the most high mountain in the world."],
      "Use the highest when comparing it with all mountains in the world."),
    q("This river is longer than that one. Which sentence is correct?", "This river is longer than that one.",
      ["This river is the longest than that one.", "This river is more long than that one.", "This river is longer that that one."],
      "Use longer than to compare two things."),
    q("Which form is used to compare three or more things?", "The superlative",
      ["The positive form without the", "Only the comparative form with than", "The past tense"],
      "Use the superlative to compare three or more things."),
    q("Which sentence compares two things?", "The Pacific Ocean is larger than the Atlantic Ocean.",
      ["The Pacific Ocean is the largest ocean in the world.", "The Pacific Ocean is large.", "Oceans are blue."],
      "Larger than compares two oceans."),
])

F("fu_fact", "Stating Geographic Facts", 8, "Second semester", 7,
  "State facts about the size and height of geographic features.", "func_view", [
    q("You want to say that this desert is very large. Which sentence is appropriate?", "This desert is very large.",
      ["This desert is very larger.", "This desert is the larger.", "This desert are very large."],
      "Use the base form large to state a fact without making a comparison."),
    q("You want to ask which mountain is the highest in the world. Which question is appropriate?", "What is the highest mountain in the world?",
      ["What is the higher mountain in the world?", "What is highest mountain in the world?", "What is the most high mountain in the world?"],
      "Use the highest."),
    q("You want to say that people should protect the ocean. Which sentence is appropriate?", "We should protect the ocean.",
      ["We should to protect the ocean.", "We should protects the ocean.", "We should protecting the ocean."],
      "Use should protect."),
    q("What does 'It is 8,848.86 meters high' describe?", "Its height",
      ["Its age", "Its population", "Its ticket price"],
      "Meters high expresses height."),
])

R("rw_fact", "Reading a Geography Passage", 8, "Second semester", 7,
  "Read a short geography passage and identify the highest or longest feature.", "read_detail", [
    q("Qomolangma is the highest mountain in the world. It is higher than any other mountain. What is it?", "The highest mountain in the world",
      ["A river", "A desert", "An ocean"], "It is the highest mountain."),
    q("The Nile is the longest river in the world. The Amazon is shorter than the Nile. Which river is shorter?", "The Amazon",
      ["The Nile", "They are the same length", "Qomolangma"], "The Amazon is shorter."),
    q("The Sahara is a great desert. We should protect the animals there. What should we do?", "Protect the animals there",
      ["Leave all deserts", "Move the rivers", "The passage does not say"], "We should protect the animals there."),
    q("The Nile is the longest river in the world. Which sentence matches the passage?", "No river in this text is longer than the Nile.",
      ["The Amazon is longer than the Nile.", "Qomolangma is a river.", "The Sahara is an ocean."],
      "The Nile is the longest river mentioned."),
])

R("rw_cloze8", "Completing a Passage with the Correct Word", 8, "Second semester", 7,
  "Choose a word that fits the meaning and grammar of the context.", "read_cloze", [
    q("Tom ___ to the library yesterday. He read an old book about the ocean. Which word fits the blank?", "went",
      ["goes", "going", "will go"],       "Yesterday calls for the past tense went."),
    q("The Sahara is one of ___ deserts in the world. Which phrase fits the blank?", "the biggest",
      ["bigger", "big", "the bigger"],       "Use the plus a superlative after one of."),
    q("Mary was reading ___ the rainstorm came. Which word fits the blank?", "when",
      ["but", "unless", "so that"],       "Use when for the arrival of a short action."),
    q("We should ___ the animals in the desert. They are in danger. Which word fits the blank?", "protect",
      ["protected", "protecting", "to protect"],       "Use the base form protect after should."),
])

V("vo_book", "Books and Reading", 8, "Second semester", 8,
  "Recognize the words treasure, island, classic, and page.",
  [("treasure", "a valuable collection of objects"), ("island", "land surrounded by water"), ("classic", "a well-known work of lasting value"), ("page", "one side of a sheet in a book")], "vocab8")

G("gr_pp", "Present Perfect", 8, "Second semester", 8,
  "Use have or has plus a past participle for events completed by the present.", "perfect", [
    q("I have already read this book. Which sentence is correct?", "I have already read this book.",
      ["I have already readed this book.", "I has already read this book.", "I have already reading this book."],
      "Use have read; the past participle of read has the same spelling as the base form."),
    q("She has already seen this film. Which sentence is correct?", "She has already seen the film.",
      ["She has already saw the film.", "She have already seen the film.", "She has already see the film."],
      "Use has seen."),
    q("What is the structure of the present perfect?", "Have or has plus a past participle",
      ["Was plus a verb ending in -ing", "Will plus the base verb", "Did plus the base verb"],
      "Use have or has plus a past participle."),
    q("They have not found the treasure yet. Which sentence is correct?", "They have not found the treasure yet.",
      ["They have not find the treasure yet.", "They has not found the treasure yet.", "They have not founded the treasure yet."],
      "Use have not found."),
])

G("gr_yet", "Already and Yet", 8, "Second semester", 8,
  "Use already in affirmative sentences and yet in questions and negative sentences.", "perfect", [
    q("I have already finished my homework. Which sentence is correct?", "I have already finished my homework.",
      ["I have yet finished my homework.", "I already have finished my homework yesterday.", "I have finished already my homework yet."],
      "Use already in affirmative sentences."),
    q("Have you read Treasure Island yet? Which sentence is correct?", "Have you read Treasure Island yet?",
      ["Have you read Treasure Island already yet?", "Did you have read Treasure Island yet?", "Have you readed Treasure Island yet?"],
      "Use yet at the end of a question."),
    q("He has not come back yet. Which sentence is correct?", "He has not come back yet.",
      ["He has not come back already.", "He has not came back yet.", "He not has come back yet."],
      "Use yet in negative sentences."),
    q("In which type of sentence is already commonly used?", "An affirmative sentence",
      ["Only in the past continuous", "Only in an if-clause", "Only before a superlative"],
      "Already is often used in affirmative present-perfect sentences."),
])

F("fu_book", "Talking About Books You Have Read", 8, "Second semester", 8,
  "Ask whether someone has read a book yet.", "func_plan", [
    q("You want to ask whether someone has read this classic. Which question is appropriate?", "Have you read this classic yet?",
      ["Did you have read this classic yet?", "Have you read this classic yesterday?", "Have you readed this classic yet?"],
      "Use Have you read ... yet?"),
    q("You have just finished reading it. What should you say?", "Yes, I have already finished it.",
      ["Yes, I have yet finished it.", "Yes, I already finished it tomorrow.", "Yes, I has already finished it."],
      "Say, Yes, I have already finished it."),
    q("You have not reached page 20 yet. Which sentence is appropriate?", "I have not reached page 20 yet.",
      ["I have not reach page 20 yet.", "I has not reached page 20 yet.", "I did not have reached page 20 yet."],
      "Use have not reached ... yet."),
    q("What is asked by 'What book have you read?'", "Which books you have read",
      ["What book you are writing", "What book you will buy tomorrow", "How many pages the book has"],
      "Have you read asks about books read up to now."),
])

R("rw_book", "Reading About Books", 8, "Second semester", 8,
  "Read a record of reading and determine who has finished the book.", "read_detail", [
    q("Amy has already read Treasure Island. Pete has not finished it yet. Who has finished it?", "Amy",
      ["Pete", "Both of them", "Neither of them"], "Amy has already read it."),
    q("Amy has already read Treasure Island. Pete has not finished it yet. Has Pete finished it?", "No",
      ["Yes", "He has read it twice", "The passage does not say"], "He has not finished it yet."),
    q("The book is a classic. It is about a boy and treasure on an island. What is the book about?", "A boy and treasure on an island",
      ["A modern city", "How to cook", "A rainstorm"], "It is about treasure on an island."),
    q("Pete has not finished it yet. Which sentence matches the reading record?", "Pete is still reading the book.",
      ["Pete has already finished the book.", "Amy has not started.", "The book is not about an island."],
      "Not finished yet means he has not completed it."),
])

V("vo_museum", "Experiences at Museums", 8, "Second semester", 9,
  "Recognize the words camera, progress, unusual, and collect.",
  [("camera", "a device for taking photographs"), ("progress", "improvement or forward movement"), ("unusual", "not ordinary or common"), ("collect", "bring things together")], "vocab8")

G("gr_ever", "Ever and Never", 8, "Second semester", 9,
  "Use ever to ask whether something has happened before and never to say that it has not happened at any time.", "perfect", [
    q("Have you ever been to a museum? Which sentence is correct?", "Have you ever been to a museum?",
      ["Have you never been to a museum as a yes-no with ever?", "Did you ever been to a museum?", "Have you ever went to a museum?"],
      "Use Have you ever been."),
    q("I have never taken the subway. Which sentence is correct?", "I have never taken the subway.",
      ["I have never took the subway.", "I have ever taken the subway to mean never.", "I has never taken the subway."],
      "Use have never taken."),
    q("In which type of sentence does ever commonly appear?", "A question",
      ["Only before a superlative", "Only in an imperative", "Only with yesterday"],
      "Use Have you ever to ask about experiences."),
    q("She has never used this camera. Which sentence is correct?", "She has never used this camera.",
      ["She has never use this camera.", "She have never used this camera.", "She has ever used this camera to mean not."],
      "Use has never used."),
])

G("gr_been", "Been and Gone", 8, "Second semester", 9,
  "Distinguish has been to (visited and returned) from has gone to (went and has not returned yet).", "perfect", [
    q("She is not here now; she went to the library. Which sentence is correct?", "She has gone to the library.",
      ["She has been to the library and is still there now.", "She has went to the library.", "She has gone the library."],
      "Use has gone to when the person is still away."),
    q("He visited Shanghai and returned last week. Which sentence is correct?", "He has been to Shanghai.",
      ["He has gone to Shanghai and is back home now.", "He has been in Shanghai for a finished trip last week without been.", "He has went to Shanghai."],
      "Use has been to when the person has visited and returned."),
    q("Has she gone to the museum? If the answer is yes, where is she now?", "At the museum; she has not returned yet",
      ["At home", "She has returned", "She has never been there"],
      "Gone means the person is still there."),
    q("Which sentence means that someone visited a place and has returned?", "They have been to the science museum.",
      ["They have gone to the science museum.", "They have went to the science museum.", "They have been the science museum."],
      "Have been to describes an experience, with the person back now."),
])

F("fu_ever", "Asking About Places Visited", 8, "Second semester", 9,
  "Ask about someone's experiences and say where you have been.", "func_plan", [
    q("You want to ask whether someone has been to an amusement park. Which question is appropriate?", "Have you ever been to an amusement park?",
      ["Have you ever gone to an amusement park and come back in the same word?", "Did you ever been to an amusement park?", "Have you ever be to an amusement park?"],
      "Use Have you ever been to."),
    q("You have been there, and you went last year. What should you say?", "Yes, I have. I went there last year.",
      ["Yes, I have gone there and I am back.", "Yes, I went there next year.", "Yes, I have never been there last year."],
      "First answer with have, then use went to give the past time."),
    q("When do you say 'Me neither'?", "When someone says they have never done something and you have not either",
      ["The other person has been there, and you have too", "You are leaving now", "You are declining an invitation"],
      "Neither means not either."),
    q("You want to say that it was an unusual experience. Which sentence is appropriate?", "It was an unusual experience.",
      ["It was an unusual experiences.", "It were an unusual experience.", "It was a unusual experience."],
      "Use an unusual experience."),
])

R("rw_museum", "Reading About Museum Visits", 8, "Second semester", 9,
  "Read about experiences and distinguish between having visited a place and still being there.", "read_detail", [
    q("Kate has been to the science museum. She took photos there last month. Is she still at the museum now?", "No, she has returned",
      ["She is still at the museum", "She has never been there", "The passage does not say she visited"], "She has been there and took photos last month."),
    q("Leo has gone to the film museum. He is not at home. Where is Leo?", "At the film museum",
      ["At home", "At the science museum", "At school"], "He has gone and is away from home."),
    q("Kate has never been to a space museum. Has she visited a space museum?", "No",
      ["Yes", "She went with Leo", "She went last week"], "She has never been there."),
    q("Leo has gone to the film museum. Which sentence matches the passage?", "Leo is away at the film museum.",
      ["Leo has come back home.", "Kate is at the film museum now.", "Kate has been to a space museum."],
      "Gone means he has not returned yet."),
])

V("vo_own", "Old Possessions and Memories", 8, "Second semester", 10,
  "Recognize the words scarf, soft, yard, and honest.",
  [("scarf", "a piece of cloth worn around the neck"), ("soft", "not hard"), ("yard", "an outdoor area next to a house"), ("honest", "truthful and fair")], "vocab8")

G("gr_since", "For and Since", 8, "Second semester", 10,
  "Use for with a duration and since with a starting point in the past.", "perfect", [
    q("I have owned this bike for three years. Which sentence is correct?", "I have had this bike for three years.",
      ["I have had this bike since three years.", "I have bought this bike for three years.", "I have had this bike for three years ago."],
      "For three years is a duration. Have had can be used with for."),
    q("I have lived here since 2019. Which sentence is correct?", "I have lived here since 2019.",
      ["I have lived here for 2019.", "I have lived here since three years.", "I lived here since 2019 and I do not live here now."],
      "Since 2019 gives the starting point."),
    q("What usually follows for?", "A duration",
      ["A year in the past", "A day of the week used as a starting point", "A superlative"],
      "For three years and for two hours are durations."),
    q("He has been ill since Monday and is still ill. Which sentence is correct?", "He has been ill since Monday.",
      ["He has been ill for Monday.", "He was ill since Monday and he is well now in this sentence.", "He has been ill since three days."],
      "Since Monday marks a starting point that continues to now."),
])

F("fu_since", "Talking About How Long You Have Owned Something", 8, "Second semester", 10,
  "Ask how long someone has owned an item and answer the question.", "func_plan", [
    q("You want to ask how long someone has owned this scarf. Which question is appropriate?", "How long have you had this scarf?",
      ["How long have you bought this scarf?", "How long did you have this scarf next year?", "How long have you has this scarf?"],
      "Use have you had for something continuing to the present, not have you bought."),
    q("You have owned it for two years. What should you say?", "I have had it for two years.",
      ["I have had it since two years.", "I have bought it for two years.", "I had it for two years and I sold it."],
      "Use for two years."),
    q("What does 'Since when have you lived in this yard?' ask?", "When you started living in this yard",
      ["How large the yard is", "Whether you lived there yesterday", "Whether the yard is soft"],
      "Since when asks for the starting time."),
    q("You want to say that the teddy bear is soft and old. Which sentence is appropriate?", "The bear is soft and old.",
      ["The bear is soft and old for since.", "The bear are soft and old.", "The bear is a old soft."],
      "Use is soft and old."),
])

R("rw_since", "Reading About Old Possessions", 8, "Second semester", 10,
  "Read a memory and identify how long an item has been owned and why it matters.", "read_detail", [
    q("I have had this scarf for three years. My grandma made it. Who made the scarf?", "His grandmother",
      ["His mother", "A classmate", "A shopkeeper"], "His grandmother made it."),
    q("I have had this scarf for three years. How long has the person owned it?", "Three years",
      ["Three months", "Since yesterday", "The passage does not say"], "It has been owned for three years."),
    q("Jeff has owned the bike since he was ten. He still rides it. Does he still ride it?", "Yes",
      ["He has already sold it", "He never owned it", "He rode it only before age ten"], "He still rides it."),
    q("Jeff has owned the bike since he was ten. Which sentence matches the passage?", "Jeff got the bike when he was ten and still has it.",
      ["Jeff has had the bike for ten days only.", "Jeff sold the bike.", "The scarf is three days old."],
      "He has owned it since he was ten and still rides it."),
])
