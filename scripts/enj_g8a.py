# -*- coding: utf-8 -*-
"""Grade 8, first semester. Common People's Education Press Go for it! sequence; unit titles and book volume still need verification."""
from en_tx import V, P, G, F, R


def q(prompt, answer, wrongs, expl):
    return ("c", prompt, answer, wrongs, expl)


P("ph_link", "Linking consonants to following vowels", 8, "First semester", 1,
  "Recognize when a word ending in a consonant can link to a following word that begins with a vowel.", "link", [
    q("In an apple, which sound can link to the following vowel?", "n and a",
      ["Pronounce a and n separately with stress", "Pause between the two words", "Link only the pple part"],
      "an ends in the consonant n, and apple begins with a vowel, so n can link to the next word."),
    q("Which phrase lets the final consonant of the first word link to the next word?", "look at",
      ["big dog", "stop class", "good time"],
      "look ends in a consonant, and at begins with a vowel. The other phrases pair a consonant with a consonant."),
    q("In the phrase not at all, between which sounds does linking occur?", "between t and a",
      ["between n and o", "add another word after ll", "pause after each of the three words"],
      "The t in at can link to the a in all."),
    q("Which situation commonly allows linking?", "A word ending in a consonant followed by a word beginning with a vowel",
      ["Both words end in a consonant", "Always link after a period", "Stress every syllable"],
      "Linking commonly occurs between a consonant and a vowel."),
])

V("vo_vac", "Vacation destinations", 8, "First semester", 1,
  "Recognize vacation, beach, museum, and mountain.",
  [("vacation", "vacation"), ("beach", "beach"), ("museum", "museum"), ("mountain", "mountain")], "vocab8")

G("gr_past8", "Talking about vacations in the simple past", 8, "First semester", 1,
  "Use the simple past to say where you went on vacation and what you did.", "past", [
    q("I went to Beijing on vacation. Which sentence is correct?", "I went to Beijing on vacation.",
      ["I go to Beijing on vacation last month.", "I goed to Beijing on vacation.", "I went to Beijing on vacation tomorrow."],
      "went is the past tense of go, and the vacation happened in the past."),
    q("She took photos on the beach. Which sentence is correct?", "She took photos on the beach.",
      ["She takes photos on the beach yesterday.", "She taked photos on the beach.", "She took photos on the beach tomorrow."],
      "The past tense of take is took."),
    q("What does 'Where did you go on vacation?' ask?", "Where you went on vacation",
      ["Where you will go on vacation", "Where you are going", "Where you usually go on vacation"],
      "did plus the base verb asks about a past vacation and where you went."),
    q("We didn't go climbing in the mountains. Which sentence is correct?", "We didn't go to the mountains.",
      ["We didn't went to the mountains.", "We don't went to the mountains.", "We didn't goes to the mountains."],
      "Use the base form go after didn't."),
])

F("fu_vac", "Talking about vacation destinations", 8, "First semester", 1,
  "Ask and answer where someone went on vacation.", "func_plan", [
    q("Which question would you use to ask a classmate where they went on vacation?", "Where did you go on vacation?",
      ["Where did you went on vacation?", "Where do you go on vacation yesterday?", "Where did you go on vacation tomorrow?"],
      "Use Where did you go to ask where someone went in the past."),
    q("How would you answer if you went to a museum?", "I went to the museum.",
      ["I go to the museum yesterday.", "I was go to the museum.", "I went the museum."],
      "Follow went to with a place."),
    q("What does 'It was great' describe?", "The experience was great",
      ["Tomorrow will be great", "He doesn't like any place", "He is leaving now"],
      "was shows that the vacation experience was good in the past."),
    q("Which sentence says the food tasted bad?", "The food was terrible.",
      ["The food is terrible yesterday.", "The food were terrible.", "The food was terrible tomorrow."],
      "food refers to the whole thing, so use was."),
])

R("rw_vac", "Reading a vacation passage", 8, "First semester", 1,
  "Read a vacation passage and identify the places and activities.", "read_detail", [
    q("Gina went to the beach on vacation. She swam and took photos. The food was great. Where did she go?", "the beach",
      ["the museum", "the mountains", "school"], "The passage says she went to the beach."),
    q("Gina went to the beach on vacation. She swam and took photos. What did she do?", "swim and take photos",
      ["stay at home", "go climbing", "visit a farm"], "The passage says she swam and took photos."),
    q("Tom stayed at home. He did not go to the museum. He read a book. Did he go to the museum?", "No",
      ["Yes", "He went with Gina", "The passage doesn't say"], "The passage says he did not go to the museum."),
    q("Tom stayed at home. He read a book. Which sentence agrees with the passage?", "Tom read a book at home.",
      ["Tom went to the beach.", "Tom took photos at the museum.", "Tom did not read."],
      "He stayed at home and read a book."),
])

V("vo_habit", "Exercise habits", 8, "First semester", 2,
  "Recognize exercise, hardly ever, twice, and the Internet.",
  [("exercise", "exercise"), ("hardly", "barely"), ("twice", "twice"), ("Internet", "the Internet")], "vocab8")

G("gr_howoften", "Asking about frequency with How often", 8, "First semester", 2,
  "Use How often to ask about frequency and answer with once, twice, or hardly ever.", "question", [
    q("Which question asks how often someone exercises?", "How often do you exercise?",
      ["How often you exercise?", "How long do you exercise once?", "How far do you exercise?"],
      "How often asks about frequency; use the auxiliary do after it."),
    q("How would you say that you exercise twice a week?", "I exercise twice a week.",
      ["I exercise two time a week.", "I exercise twice week.", "I exercise a twice week."],
      "twice a week means two times each week."),
    q("What does hardly ever mean?", "almost never",
      ["every day", "three times a week", "only yesterday"], "hardly ever describes a very low frequency."),
    q("She uses the Internet every day. What does this tell us?", "She goes online every day",
      ["She hardly ever goes online", "She goes online once a week", "She didn't go online yesterday"], "every day means each day."),
])

F("fu_habit", "Talking about exercise frequency", 8, "First semester", 2,
  "Ask about other people's habits and describe how often you do something.", "func_life", [
    q("A doctor asks how often you exercise. Which question is this?", "How often do you exercise?",
      ["How old do you exercise?", "What time is exercise yesterday?", "How many exercise are you?"],
      "Use How often to ask about the frequency of a habit."),
    q("How would you say that you hardly ever drink milk?", "I hardly ever drink milk.",
      ["I hardly ever drank milk tomorrow.", "I hard ever drink milk.", "I hardly ever drinking milk."],
      "Place hardly ever before the main verb."),
    q("What does the answer 'Three times a week' mean?", "three times a week",
      ["three o'clock", "three kilometers", "three people"], "times a week tells how many times something happens each week."),
    q("Which sentence would you use to suggest that someone exercise more?", "You should exercise more.",
      ["You should exercises more.", "You should to exercise more.", "You should exercising more."],
      "Use the base form of the verb after should."),
])

R("rw_habit", "Reading an exercise survey", 8, "First semester", 2,
  "Read a survey and identify who exercises the most.", "read_detail", [
    q("Jack exercises every day. Mary exercises twice a week. Peter hardly ever exercises. Who exercises every day?", "Jack",
      ["Mary", "Peter", "no one"], "The passage says Jack exercises every day."),
    q("Jack exercises every day. Mary exercises twice a week. Peter hardly ever exercises. Who hardly ever exercises?", "Peter",
      ["Jack", "Mary", "all three equally"], "The passage says Peter hardly ever exercises."),
    q("Mary uses the Internet once a week. She reads books every night. How often does she go online?", "once a week",
      ["every day", "hardly ever", "twice a week"], "The passage says once a week."),
    q("Mary uses the Internet once a week. She reads books every night. Which sentence agrees with the passage?", "Mary reads every night.",
      ["Mary never reads.", "Mary uses the Internet every day.", "Mary hardly ever reads."],
      "The passage says she reads books every night."),
])

P("ph_plos", "Incomplete plosion", 8, "First semester", 3,
  "Recognize when the first of two adjacent plosive sounds is not fully released.", "plosion", [
    q("In sit down, which sound is often not fully released?", "the t in sit",
      ["the n in down", "the s in sit", "the d in down"],
      "The t is followed by the plosive d, so t is often not fully released."),
    q("Which phrase contains incomplete plosion?", "good time",
      ["my apple", "to a park", "an old man"],
      "The d in good and the t in time are both plosives; when they are adjacent, the first is not fully released."),
    q("In big kite, where does incomplete plosion occur?", "between g and k",
      ["between b and i", "between k and i", "after the final e"],
      "The g in big and the k in kite are adjacent plosives."),
    q("When does incomplete plosion usually occur?", "When two plosive sounds are adjacent",
      ["A vowel is followed by a period", "A word has only one syllable", "The sentence ends with rising intonation"],
      "The second plosive affects the first, so the first is often not fully released."),
])

V("vo_person", "Personality adjectives", 8, "First semester", 3,
  "Recognize outgoing, serious, loud, and quiet.",
  [("outgoing", "outgoing"), ("serious", "serious"), ("loud", "loud"), ("quiet", "quiet")], "vocab8")

G("gr_comp8", "Comparative adjectives", 8, "First semester", 3,
  "Form comparatives with -er and more.", "compare", [
    q("What is the comparative form of tall?", "taller",
      ["more tall", "tallest", "more taller"], "Add -er to the one-syllable adjective tall."),
    q("What is the comparative form of outgoing?", "more outgoing",
      ["outgoinger", "more outgoinger", "outgoingest"], "Put more before the multisyllabic adjective outgoing."),
    q("What is the comparative form of good?", "better",
      ["gooder", "more good", "best"], "The comparative form of good is better."),
    q("Which sentence uses a comparative?", "Tom is quieter than Sam.",
      ["Tom is quiet.", "Tom is the quietest boy.", "Tom is a quiet boy in Class 2."],
      "quieter is the comparative form of quiet."),
])

G("gr_than8", "Comparing with than", 8, "First semester", 3,
  "Use than to compare two people or things.", "compare", [
    q("She is more outgoing than her sister. Which sentence is correct?", "She is more outgoing than her sister.",
      ["She is more outgoinger than her sister.", "She is outgoing than her sister.", "She is more outgoing that her sister."],
      "Use than after more outgoing."),
    q("My hair is shorter than hers. Which sentence is correct?", "My hair is shorter than hers.",
      ["My hair is more short than hers.", "My hair is shorter that hers.", "My hair is short than hers."],
      "shorter than compares two things."),
    q("Which sentence compares two people?", "Paul is taller than his brother.",
      ["Paul is tall.", "Paul is a student.", "Paul likes basketball."],
      "taller than shows that Paul is taller."),
    q("Which question asks who is taller between two people?", "Who is taller, Tom or Jack?",
      ["Who is tallest, Tom or Jack?", "Who is more taller, Tom or Jack?", "Who is the taller than Tom or Jack?"],
      "Use the comparative taller for two people, not the superlative."),
])

F("fu_cmp", "Comparing two people", 8, "First semester", 3,
  "Describe differences in two people's personalities or appearance.", "func_life", [
    q("Which sentence says that your friend is more serious than you?", "My friend is more serious than me.",
      ["My friend is seriouser than me.", "My friend is more seriouser than me.", "My friend more serious than me."],
      "The comparative form of serious is more serious."),
    q("Someone asks Is Tara more outgoing than Tina? If you agree, how should you answer?", "Yes, she is.",
      ["Yes, she does.", "Yes, she can.", "Yes, she more."],
      "The question uses is, so the affirmative short answer is Yes, she is."),
    q("Which sentence says that both people are quiet?", "They are both quiet.",
      ["They are both quieter than.", "They both is quiet.", "They are both more quiet than."],
      "both means the two people; than is not needed here."),
    q("Which question asks about a difference?", "How are you different from your sister?",
      ["How old is the classroom?", "What time is different yesterday?", "Where is than?"],
      "Use different from to ask how someone differs from another person."),
])

R("rw_cmp", "Reading comparisons between people", 8, "First semester", 3,
  "Read a comparison and determine who is taller and who is more outgoing.", "read_detail", [
    q("Tara is taller than Tina. Tina is more outgoing than Tara. Who is taller?", "Tara",
      ["Tina", "They are the same height", "The passage doesn't say"], "The passage says Tara is taller than Tina."),
    q("Tara is taller than Tina. Tina is more outgoing than Tara. Who is more outgoing?", "Tina",
      ["Tara", "They are equally outgoing", "the teacher"], "The passage says Tina is more outgoing."),
    q("Paul is quieter than his brother. His brother is louder. Who is quieter?", "Paul",
      ["his brother", "They are both loud", "The passage doesn't say"], "The passage says Paul is quieter."),
    q("Paul is quieter than his brother. Which sentence agrees with the passage?", "Paul's brother is louder than Paul.",
      ["Paul is louder than his brother.", "Paul is more outgoing than his brother.", "They are the same."],
      "His brother is louder, which means he is less quiet than Paul."),
])

V("vo_town", "Town facilities", 8, "First semester", 4,
  "Recognize theater, screen, seat, and service.",
  [("theater", "theater"), ("screen", "screen"), ("seat", "seat"), ("service", "service")], "vocab8")

G("gr_super", "Superlative adjectives", 8, "First semester", 4,
  "Use superlatives to compare three or more people or things.", "compare", [
    q("Tom is the tallest of the three boys. Which sentence is correct?", "Tom is the tallest of the three boys.",
      ["Tom is the taller of the three boys.", "Tom is tallest of the three boys.", "Tom is the most tall of the three boys."],
      "Use the tallest when comparing three or more."),
    q("What is the superlative form of popular?", "the most popular",
      ["the popularer", "the most popularer", "popularest"],
      "Put the most before a multisyllabic adjective."),
    q("What is the superlative form of good?", "best",
      ["goodest", "most good", "better"], "The superlative form of good is best."),
    q("Which sentence uses a superlative?", "This is the best theater in town.",
      ["This theater is better than that one.", "This theater is good.", "This is a theater."],
      "the best is a superlative."),
])

F("fu_best", "Talking about the best places", 8, "First semester", 4,
  "Ask and answer whether a place is the best.", "func_life", [
    q("Which question asks which theater has the most comfortable seats?", "Which theater has the most comfortable seats?",
      ["Which theater has the comfortablest seats?", "Which theater has more comfortable seats of all?", "Which theater has the most comfortable seatest?"],
      "The superlative form of comfortable is the most comfortable."),
    q("How would you say that it has the biggest screen?", "It has the biggest screen.",
      ["It has the most big screen.", "It has the bigger screen of all the town.", "It has biggest screen."],
      "The superlative form of big is the biggest."),
    q("What does 'What's the best movie theater?' ask?", "Which movie theater is the best?",
      ["Where is the movie theater?", "How much are the tickets?", "What did you watch yesterday?"],
      "the best asks which one is the best among three or more."),
    q("Which sentence says that the service is the worst?", "It has the worst service.",
      ["It has the most bad service.", "It has the worse service of all.", "It has the baddest service."],
      "The superlative form of bad is worst."),
])

R("rw_best", "Reading a theater description", 8, "First semester", 4,
  "Read a town description and identify the best facilities.", "read_detail", [
    q("Town Cinema has the biggest screen. It has the most comfortable seats. Which theater has the biggest screen?", "Town Cinema",
      ["the school", "home", "The passage doesn't say"], "The passage says Town Cinema has the biggest screen."),
    q("Town Cinema has the biggest screen. It has the most comfortable seats. How are the seats?", "the most comfortable",
      ["the fewest", "worse than the others", "The passage doesn't say"], "The passage says it has the most comfortable seats."),
    q("Movie World is the cheapest, but the service is the worst. Which theater is the cheapest?", "Movie World",
      ["Town Cinema", "They cost the same", "The passage doesn't say"], "The passage says Movie World is the cheapest."),
    q("Movie World is the cheapest, but the service is the worst. Which sentence agrees with the passage?", "Movie World has the worst service.",
      ["Movie World has the best service.", "Town Cinema is the cheapest.", "The seats are the worst."],
      "Movie World is cheap, but its service is the worst."),
])

V("vo_show", "TV programs", 8, "First semester", 5,
  "Recognize sitcom, news, educational, and cartoon.",
  [("sitcom", "sitcom"), ("news", "news"), ("educational", "educational"), ("cartoon", "cartoon")], "vocab8")

G("gr_to", "Infinitives as objects", 8, "First semester", 5,
  "Use to plus the base form of a verb after want, plan, hope, and expect.", "to_ing", [
    q("I want to watch the news. Which sentence is correct?", "I want to watch the news.",
      ["I want watch the news.", "I want watching the news.", "I want to watching the news."],
      "Use to watch after want."),
    q("She plans to study medicine. Which sentence is correct?", "She plans to study medicine.",
      ["She plans study medicine.", "She plans studying medicine.", "She plan to study medicine."],
      "Add s to plan, then use to study."),
    q("Which form should follow hope?", "to + base verb",
      ["a verb ending in -ing", "the past tense", "a plural noun"],
      "Use hope to do something."),
    q("They expect to arrive tomorrow. Which sentence is correct?", "They expect to arrive tomorrow.",
      ["They expect arriving tomorrow.", "They expect arrive tomorrow.", "They expect to arrived tomorrow."],
      "Use expect to arrive."),
])

F("fu_show", "Talking about programs you want to watch", 8, "First semester", 5,
  "Say what program you want to watch and ask what someone else thinks.", "func_plan", [
    q("Which question would you use to invite someone to watch a sitcom?", "Do you want to watch a sitcom?",
      ["Do you want watch a sitcom?", "Do you want to watching a sitcom?", "Are you want to watch a sitcom?"],
      "Use Do you want to watch."),
    q("How would you say that you think the news is educational?", "I think the news is educational.",
      ["I think the news are educational.", "I think the news is education.", "I am think the news is educational."],
      "news is the name of a program here, so use is educational."),
    q("What does 'What do you think of talk shows?' ask?", "What do you think of talk shows?",
      ["What time are the talk shows?", "Do you want to be a host?", "Who owns the talk shows?"],
      "Use What do you think of to ask for an opinion."),
    q("Which sentence says that you can't stand the program?", "I can't stand it.",
      ["I can't stand watch it.", "I can't stands it.", "I am can't stand it."],
      "You can put it directly after can't stand."),
])

R("rw_show", "Reading about program choices", 8, "First semester", 5,
  "Read a conversation and identify who wants to watch what.", "read_detail", [
    q("Lisa wants to watch a cartoon. Tom plans to watch the news. Who wants to watch a cartoon?", "Lisa",
      ["Tom", "They both want to watch the news", "the teacher"], "The passage says Lisa wants to watch a cartoon."),
    q("Lisa wants to watch a cartoon. Tom plans to watch the news. What does Tom plan to watch?", "the news",
      ["a cartoon", "a sitcom", "a sports program"], "The passage says Tom plans to watch the news."),
    q("Gina hopes to watch an educational sitcom. She does not like scary shows. Does she like scary shows?", "No",
      ["Yes", "She watches them only on weekends", "The passage doesn't say"], "The passage says she does not like scary shows."),
    q("Gina hopes to watch an educational sitcom. Which sentence agrees with the passage?", "Gina hopes to watch a sitcom.",
      ["Gina wants to watch the news.", "Gina likes scary shows.", "Gina plans to watch a cartoon."],
      "The passage says she hopes to watch an educational sitcom."),
])

V("vo_job8", "Career plans", 8, "First semester", 6,
  "Recognize scientist, engineer, pilot, and college.",
  [("scientist", "scientist"), ("engineer", "engineer"), ("pilot", "pilot"), ("college", "college")], "vocab8")

G("gr_going8", "Using be going to for plans", 8, "First semester", 6,
  "Use be going to to talk about a plan that has already been decided.", "future", [
    q("I am going to study computer science. Which sentence is correct?", "I am going to study computer science.",
      ["I am going study computer science.", "I going to study computer science.", "I am go to study computer science."],
      "Use the base form of the verb after am going to."),
    q("She is going to be an engineer. Which sentence is correct?", "She is going to be an engineer.",
      ["She is going to be a engineer.", "She are going to be an engineer.", "She is going to is an engineer."],
      "engineer begins with a vowel sound, so use an. Use the base form be."),
    q("They are not going to go to college. Which sentence is correct?", "They are not going to go to college.",
      ["They are not going to goes to college.", "They not going to go to college.", "They are not go to college."],
      "Form the negative with be not going to."),
    q("What does be going to mainly express here?", "a plan that has already been decided",
      ["a past habit", "an action in progress", "a guess about the past"],
      "Use be going to to talk about plans."),
])

F("fu_dream", "Talking about future plans", 8, "First semester", 6,
  "Ask what someone wants to be when they grow up and describe your own plans.", "func_plan", [
    q("Which question asks what someone plans to be when they grow up?", "What are you going to be when you grow up?",
      ["What are you going to be when you grew up?", "What do you going to be when you grow up?", "What are you going be when you grow up?"],
      "Use are you going to be."),
    q("How would you say that you plan to be a pilot?", "I am going to be a pilot.",
      ["I am going to be an pilot.", "I am going to am a pilot.", "I going to be a pilot."],
      "pilot begins with a consonant sound, so use a."),
    q("What does 'How are you going to do that?' ask?", "How you plan to do that",
      ["What you are doing now", "What you did last year", "Where you will go on vacation"],
      "How are you going to asks about the way someone plans to achieve something."),
    q("Which sentence says that you plan to practice more?", "I am going to practice every day.",
      ["I am going to practicing every day.", "I am going practice every day.", "I am going to practiced every day."],
      "Use going to practice."),
])

R("rw_dream", "Reading about plans", 8, "First semester", 6,
  "Read a plan and identify the career and actions.", "read_detail", [
    q("Ken is going to be a scientist. He is going to study hard. What does he plan to be?", "a scientist",
      ["a pilot", "an engineer", "a doctor"], "The passage says he is going to be a scientist."),
    q("Ken is going to be a scientist. He is going to study hard. What does he plan to do?", "study hard",
      ["swim every day", "become a pilot", "stop going to school"], "The passage says he is going to study hard."),
    q("Lucy is going to college. She is not going to be a pilot. Does she plan to be a pilot?", "No",
      ["Yes", "She already is a pilot", "The passage doesn't say"], "The passage says she is not going to be a pilot."),
    q("Lucy is going to college. Which sentence agrees with the passage?", "Lucy is going to go to college.",
      ["Lucy is going to be a pilot.", "Lucy was a scientist.", "Lucy is not going to college."],
      "The passage says she is going to college."),
])

V("vo_future", "Life in the future", 8, "First semester", 7,
  "Recognize robot, pollution, prediction, and future.",
  [("robot", "robot"), ("pollution", "pollution"), ("prediction", "prediction"), ("future", "future")], "vocab8")

G("gr_will", "Using will for the future", 8, "First semester", 7,
  "Use will to make predictions or express a decision made on the spot.", "future", [
    q("People will have robots. Which sentence is correct?", "People will have robots.",
      ["People will has robots.", "People will to have robots.", "People will having robots."],
      "Use the base form have after will."),
    q("There will be less pollution. Which sentence is correct?", "There will be less pollution.",
      ["There will have less pollution.", "There will be less pollution yesterday.", "There will to be less pollution."],
      "Use There will be to say that something will exist."),
    q("I will help you. This is a decision made on the spot. Which sentence is suitable?", "I will help you.",
      ["I will helped you.", "I will to help you.", "I helping you tomorrow now."],
      "will is often used for decisions made on the spot."),
    q("What is the negative form of will?", "will not",
      ["willn't doed", "do will not", "not will to"],
      "will not is often contracted to won't."),
])

F("fu_predict", "Predicting the future", 8, "First semester", 7,
  "Ask what someone thinks about the future and make predictions.", "func_plan", [
    q("Which question asks what the world will be like in 100 years?", "What will the world be like in 100 years?",
      ["What will the world be like 100 years ago?", "What is the world be like in 100 years?", "What will the world like in 100 years?"],
      "in 100 years means 100 years from now, so use will."),
    q("How would you predict that children will study at home?", "Kids will study at home.",
      ["Kids will studies at home.", "Kids will study at home yesterday.", "Kids will to study at home."],
      "Use will study."),
    q("Do you think there will be more trees? If you agree, how should you answer?", "Yes, I think so.",
      ["Yes, I think not so.", "Yes, there was.", "No, I think so there will."],
      "Agree with the prediction by saying Yes, I think so."),
    q("Which sentence says that you disagree?", "No, I don't think so.",
      ["No, I am not think so.", "No, I doesn't think so.", "No, I don't thinks so."],
      "I don't think so means that you disagree."),
])

R("rw_future", "Reading predictions about the future", 8, "First semester", 7,
  "Read a prediction and decide what will happen.", "read_detail", [
    q("In 50 years, people will have robots at home. There will be less pollution. What will people have at home?", "robots",
      ["more pollution", "paper books", "horse-drawn carriages"], "The passage says people will have robots at home."),
    q("In 50 years, people will have robots at home. There will be less pollution. What will happen to pollution?", "less pollution",
      ["There will be more", "It will be exactly the same as now", "The passage doesn't say"], "The passage says there will be less pollution."),
    q("Joe thinks cities will be more crowded. He will live on a space station. Where will he live?", "a space station",
      ["under the sea", "in the countryside", "in a school dormitory"], "The passage says he will live on a space station."),
    q("Joe thinks cities will be more crowded. Which sentence agrees with the passage?", "Joe thinks cities will be more crowded.",
      ["Joe thinks there will be no cities.", "Joe will live on a farm.", "People will not have robots."],
      "The passage says cities will be more crowded."),
])

V("vo_cook", "Cooking vocabulary", 8, "First semester", 8,
  "Recognize yogurt, honey, spoon, and blender.",
  [("yogurt", "yogurt"), ("honey", "honey"), ("spoon", "spoon"), ("blender", "blender")], "vocab8")

G("gr_seq", "Sequence words first, next, then", 8, "First semester", 8,
  "Use sequence words and imperative sentences to explain steps.", "sentence", [
    q("First, peel the bananas. Which sentence is correct?", "First, peel the bananas.",
      ["First, peeling the bananas.", "First, to peel the bananas.", "First, peeled the bananas."],
      "Use the imperative with the base form of the verb to give instructions."),
    q("Then add the honey. Which sentence is correct?", "Then add the honey.",
      ["Then adding the honey.", "Then to add the honey.", "Then added the honey yesterday."],
      "Use the base form of the verb after Then."),
    q("Which word introduces the next step?", "Next",
      ["Yesterday", "Because", "Although"],
      "Next means what comes after this."),
    q("Finally, pour the milk shake into a glass. Which sentence is correct?", "Finally, pour the milk shake into a glass.",
      ["Finally, pours the milk shake into a glass.", "Finally, pouring the milk shake into a glass.", "Finally, to pour the milk shake into a glass."],
      "Use pour in the imperative; do not add s."),
])

F("fu_recipe", "Explaining how to make something", 8, "First semester", 8,
  "Ask how to make a food or drink and explain the steps in order.", "func_life", [
    q("Which question asks how to make a banana milk shake?", "How do you make a banana milk shake?",
      ["How do you makes a banana milk shake?", "How are you make a banana milk shake?", "How did you make a banana milk shake tomorrow?"],
      "Use How do you make."),
    q("How would you say that you need two spoons of honey?", "We need two spoons of honey.",
      ["We need two spoon of honey.", "We need two spoons of honeys.", "We need two spoon honey."],
      "Use two spoons of honey."),
    q("What does 'How much yogurt do we need?' ask?", "How much yogurt is needed",
      ["How to spell yogurt", "Where yogurt is sold", "Who likes yogurt"],
      "How much asks about the amount of an uncountable noun."),
    q("Which sentence tells someone to turn on the blender?", "Turn on the blender.",
      ["Turns on the blender.", "Turning on the blender.", "To turn on the blender."],
      "Use the base form of the verb in the imperative."),
])

R("rw_recipe", "Reading a recipe", 8, "First semester", 8,
  "Read a recipe and identify its ingredients and steps.", "read_detail", [
    q("First, peel two bananas. Next, put them into the blender. Then add honey. What is the first step?", "peel the bananas",
      ["add honey", "open the glass", "pour the milk shake"], "The first step is to peel two bananas."),
    q("First, peel two bananas. Next, put them into the blender. Where do you put the bananas?", "the blender",
      ["a glass", "a spoon", "the refrigerator"], "The passage says to put them into the blender."),
    q("We need one spoon of honey and a cup of yogurt. How much honey is needed?", "one spoon",
      ["one cup", "two spoons", "no honey"], "The recipe calls for one spoon of honey."),
    q("Finally, pour the milk shake into a glass. Which sentence agrees with the recipe?", "The last step is to pour it into a glass.",
      ["The first step is to pour it into a glass.", "We do not use yogurt.", "We peel the honey."],
      "Finally marks the last step."),
])

V("vo_party", "Party activities", 8, "First semester", 9,
  "Recognize invitation, preparation, concert, and available.",
  [("invitation", "invitation"), ("preparation", "preparation"), ("concert", "concert"), ("available", "available")], "vocab8")

G("gr_invite", "Inviting someone with can", 8, "First semester", 9,
  "Invite someone with Can you and respond using a modal verb.", "modal", [
    q("Which sentence invites someone to a party?", "Can you come to my party?",
      ["Can you to come to my party?", "Do you can come to my party?", "Can you coming to my party?"],
      "Use the base form of the verb after Can you."),
    q("You would be happy to go. Which response is correct?", "Sure, I would love to.",
      ["Sure, I would love.", "Sure, I would love coming.", "Sure, I will love to went."],
      "The verb come is omitted after would love to."),
    q("You have to see the doctor that day. Which sentence is correct?", "I have to see the doctor.",
      ["I have to seeing the doctor.", "I has to see the doctor.", "I have see the doctor."],
      "Use the base form of the verb after have to."),
    q("What is 'Can you come to the concert?' mainly doing?", "inviting someone",
      ["asking about the ticket price", "describing the past", "comparing two concerts"],
      "Can you come is commonly used to invite someone."),
])

F("fu_invite", "Accepting or declining an invitation", 8, "First semester", 9,
  "Accept an invitation or explain why you cannot go.", "func_plan", [
    q("Someone invites you for Saturday, and you can go. What should you say?", "Sure. I am available on Saturday.",
      ["Sure. I was available on Saturday tomorrow.", "Sure. I am available in Saturday.", "Sure. I available on Saturday."],
      "Use on Saturday and include am."),
    q("You can't go because you have to prepare for a test. Which response is suitable?", "Sorry, I have to prepare for a test.",
      ["Sorry, I have to preparing for a test.", "Sorry, I has to prepare for a test.", "Sorry, I have prepare for a test."],
      "Use have to prepare."),
    q("Which question asks whether someone is available on Tuesday?", "Are you available on Tuesday?",
      ["Do you available on Tuesday?", "Are you available in Tuesday?", "Are you available at Tuesday?"],
      "Use on before a day of the week and are before available."),
    q("What does I might have to meet my friend mean?", "I may have to meet my friend",
      ["I can definitely come", "I met my friend yesterday", "I don't want any friends"],
      "might have to means may have to."),
])

R("rw_invite", "Reading an invitation", 8, "First semester", 9,
  "Read an invitation and identify the time, place, and who cannot come.", "read_detail", [
    q("Please come to my party on Sunday at 7. It is at my house. What day is the party?", "Sunday",
      ["Saturday", "Monday", "Friday"], "The invitation says on Sunday."),
    q("Please come to my party on Sunday at 7. It is at my house. Where will the party be?", "at my house",
      ["at school", "at a concert", "at a hospital"], "The invitation says it is at my house."),
    q("Anna can come. Jeff has to prepare for a test, so he cannot come. Who can't come?", "Jeff",
      ["Anna", "They can both come", "The passage doesn't say"], "The passage says Jeff cannot come."),
    q("Anna can come. Jeff has to prepare for a test. Which sentence agrees with the invitation?", "Jeff is not available because of a test.",
      ["Anna cannot come.", "The party is on Monday.", "Jeff will come to the party."],
      "Jeff has to prepare for a test, so he cannot come."),
])

P("ph_pause", "Pausing between sense groups", 8, "First semester", 10,
  "Pause at sense-group boundaries instead of splitting a meaningful phrase in the middle.", "pause", [
    q("I went to the park with my father. Which pause is better?", "I went to the park / with my father.",
      ["I went to / the park with my father.", "I / went to the park with my father only after every word", "went to the / park"],
      "to the park is a sense group; avoid pausing after to."),
    q("Which position is not suitable for a pause?", "splitting look at into look / at",
      ["after a period", "after a comma", "at the end of a complete sense group"],
      "look at usually stays together; do not split it in the middle."),
    q("In If it rains, I will stay at home, what can you do at the comma?", "pause",
      ["You must link across it", "You must stress the comma", "You must not take a breath"],
      "A comma often marks the boundary of a sense group."),
    q("Why read aloud with pauses between sense groups?", "to make the meaning clearer",
      ["to stress every letter", "to eliminate all pauses", "to pause only in the middle of words"],
      "Pausing between sense groups helps listeners understand the sentence."),
])

V("vo_advice", "Advice vocabulary", 8, "First semester", 10,
  "Recognize advice, organize, upset, and careless.",
  [("advice", "advice"), ("organize", "organize"), ("upset", "upset"), ("careless", "careless")], "vocab8")

G("gr_if", "If-clauses for conditions", 8, "First semester", 10,
  "Use if-clauses for conditions, with will in the main clause and the simple present in the if-clause.", "clause_adv", [
    q("If it rains tomorrow, I will stay at home. Which sentence is correct?", "If it rains tomorrow, I will stay at home.",
      ["If it will rain tomorrow, I will stay at home.", "If it rains tomorrow, I stayed at home.", "If it rain tomorrow, I will stay at home."],
      "Use rains in the if-clause and will stay in the main clause."),
    q("If you go to the party, you will have a great time. Which sentence is correct?", "If you go to the party, you will have a great time.",
      ["If you will go to the party, you have a great time.", "If you go to the party, you had a great time.", "If you went to the party, you will have a great time tomorrow."],
      "Use go in the if-clause and will have in the main clause."),
    q("When an if-clause refers to the future, which tense does the verb usually take?", "the simple present",
      ["the past perfect", "will + verb", "the past progressive"],
      "The if-clause usually does not use will."),
    q("If he comes, please tell me. Which sentence is correct?", "If he comes, please tell me.",
      ["If he will come, please tell me.", "If he come, please tell me.", "If he comes, please told me."],
      "Use comes after he and tell in the imperative."),
])

F("fu_if", "Giving advice with conditionals", 8, "First semester", 10,
  "Use if-clauses to warn someone about the consequences of an action.", "func_plan", [
    q("Which sentence warns someone that eating too much may make them feel sick?", "If you eat too much, you will feel sick.",
      ["If you will eat too much, you feel sick.", "If you eat too much, you felt sick tomorrow.", "If you eats too much, you will feel sick."],
      "Use eat in the if-clause and will feel in the main clause."),
    q("Which sentence says that the party will be great if you organize it well?", "If you organize it well, the party will be great.",
      ["If you will organize it well, the party is great yesterday.", "If you organize it well, the party was great tomorrow.", "If you organizes it well, the party will be great."],
      "Use the base form organize and will be in the main clause."),
    q("What does 'What will happen if they have the party today?' ask?", "What will happen if the party is held today?",
      ["What party they had yesterday", "Which classroom the party is in", "Who was not invited"],
      "What will happen if asks about a possible result."),
    q("A friend is upset, and you want to suggest leaving a noisy party. Which sentence is suitable?", "If you leave now, you will feel better.",
      ["If you will leave now, you feel better.", "If you leave now, you felt better.", "If you leaving now, you will feel better."],
      "Use the simple present leave in the if-clause and will feel for the result."),
])

R("rw_if", "Reading advice for a party", 8, "First semester", 10,
  "Read some advice and identify the conditions and results.", "read_detail", [
    q("If you wear jeans, the teacher will not let you in. If you take a bus, you will be late. What will happen if you wear jeans?", "The teacher won't let you in",
      ["You will arrive early", "You will get a gift", "The passage doesn't say"], "The passage says the teacher will not let you in."),
    q("If you wear jeans, the teacher will not let you in. If you take a bus, you will be late. What will happen if you take a bus?", "You will be late",
      ["It will be very quiet", "The teacher will praise you", "You will not be late"], "The passage says you will be late."),
    q("If we organize the games well, everyone will have fun. What must happen for everyone to have fun?", "The games must be organized well",
      ["They must wear jeans", "They must be late", "They must not prepare"], "The passage says, If we organize the games well."),
    q("If we organize the games well, everyone will have fun. Which sentence agrees with the passage?", "Good organization will help everyone have fun.",
      ["Everyone will have fun if nobody organizes the games.", "The teacher will let jeans in.", "Taking a bus will make them early."],
      "If the games are organized well, everyone will have fun."),
])
