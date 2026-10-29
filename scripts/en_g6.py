# -*- coding: utf-8 -*-
"""Grade 6, Books 1 and 2. A common unit sequence for the People's Education Press PEP series starting in Grade 3; book assignment pending verification."""
from en_tx import V, P, G, F, R, X

# "上" and "下" are parser-required semester tokens passed to the topic constructors below.
# ---------- Grade 6, Book 1 ----------

V("vo_city", "Places in the City", 6, "上", 1,
  "Recognize hospital, cinema, bookstore, and post office.",
  [("hospital", "hospital"), ("cinema", "movie theater"), ("bookstore", "bookstore"), ("post office", "post office")])

G("gr_turn", "Turn Left, Turn Right, and Go Straight", 6, "上", 1,
  "Use “Turn left,” “Turn right,” and “Go straight” to give directions.", "func_out", [
    ("c", "Which sentence says, “Turn left at the bookstore”?", "Turn left at the bookstore.",
     ["Turn right at the bookstore.", "Go straight at the bookstore.", "Turn bookstore left."], "The phrase for turning left is “Turn left.”"),
    ("c", "What does “Where is the hospital?” ask?", "Where the hospital is",
     ["Who the hospital belongs to", "What is in the hospital", "How to get to the movie theater"], "“Where is” asks about a location."),
    ("c", "What does “Go straight” mean?", "Go straight",
     ["Turn left", "Turn right", "Stop"], "“Go straight” means to continue straight ahead."),
    ("c", "At the cinema, which way should you go if someone says, “Turn right”?", "Turn right",
     ["Turn left", "Go straight", "Turn around"], "“Turn right” means to turn to the right."),
])

F("fu_way", "Asking for and Giving Directions", 6, "上", 1,
  "Ask for directions with “How can I get to ...?” and say that one place is nearby with “next to.”", "func_out", [
    ("c", "Which sentence asks how to get to the hospital?", "How can I get to the hospital?",
     ["Where is a turn left?", "What is the hospital like?", "When is the hospital?"], "Ask for directions with “How can I get to ...?”"),
    ("c", "The bookstore is next to the cinema. Where is the bookstore?", "Next to the movie theater",
     ["Inside the hospital", "Far across from the post office", "Inside the school"], "“Next to the cinema” means beside the movie theater."),
    ("c", "If someone says, “Turn left at the post office,” which way should you go?", "Turn left",
     ["Turn right", "Go straight", "Stop"], "“Turn left” gives the direction."),
    ("c", "If it is nearby, how should you answer “Is it far?”?", "No. It is near.",
     ["Yes. It is far.", "Turn right.", "Go to the hospital."], "“Near” means close, so answer “No.”"),
])

R("rw_way", "Understanding Directions", 6, "上", 1,
  "Read a passage with directions and identify the route.", "read_text", [
    ("c", "Read: Go straight. Turn left at the bookstore. The hospital is on the right. Which way should you go at the bookstore?", "Turn left",
     ["Turn right", "Stop", "Turn around"], "The passage says, “Turn left at the bookstore.”"),
    ("c", "Read: The cinema is next to the hospital. Where is the cinema?", "Next to the hospital",
     ["Inside the bookstore", "Inside the post office", "Far from the hospital"], "The passage says it is next to the hospital."),
    ("c", "Read: How can I get to the post office? Turn right at the cinema. Where should you turn right to get to the post office?", "At the cinema",
     ["At the bookstore", "At the hospital", "At the school"], "The passage says, “Turn right at the cinema.”"),
    ("c", "Read: It is not far. Go straight and you can see it. Which sentence matches the passage?", "It is not far; go straight and you will see it.",
     ["It is far, so turn left.", "Turn left at the bookstore.", "The hospital is on the right."], "The passage says it is not far and to go straight."),
])

V("vo_trans", "Transportation", 6, "上", 2,
  "Recognize bus, plane, ship, and train.",
  [("bus", "bus"), ("plane", "plane"), ("ship", "ship"), ("train", "train")])

G("gr_must", "must and Traffic Rules", 6, "上", 2,
  "Use “must” and “Do not” to state traffic rules.", "modal_imp", [
    ("c", "Which sentence means, “You must stop”?", "You must stop.",
     ["You must stops.", "You are must stop.", "You stop must."], "After “must,” use the base form “stop.”"),
    ("c", "Do not go at a red light. What should you do when the light is red?", "Do not go",
     ["You may go", "You must run", "Turn left"], "“Do not go” means you must not proceed."),
    ("c", "We must look right before crossing. Which way must we look before crossing the road?", "Right",
     ["Left", "Up", "Behind"], "The sentence says to look right."),
    ("c", "What does “I must pay attention to the traffic lights” mean?", "I must watch the traffic lights carefully",
     ["I do not need to look at the lights", "The traffic lights are at the bookstore", "I cannot read the traffic lights"], "“Must pay attention to the traffic lights” expresses an obligation."),
])

F("fu_come", "Describing How You Travel", 6, "上", 2,
  "Use “I come to school by ...” to describe how you get to school.", "func_out", [
    ("c", "Which sentence says that you ride a bicycle to school?", "I come to school by bike.",
     ["I come to school by bus.", "I come to school by train.", "I come to school by plane."], "Say “by bike” for traveling by bicycle."),
    ("c", "What does “How do you come to school?” ask?", "How you get to school",
     ["Where the school is", "Whether you have to stop", "Whether you like buses"], "“How do you come ...?” asks about the way someone travels."),
    ("c", "I usually walk. How does this person usually get to school?", "On foot",
     ["By bus", "By train", "By plane"], "“Walk” means to go on foot."),
    ("c", "Slow down and stop at a yellow light. What should you do at a yellow light?", "Slow down and stop",
     ["Speed up and go through", "Ignore the light", "Run"], "The instruction is to slow down and stop."),
])

R("rw_traffic", "Understanding Traffic Rules", 6, "上", 2,
  "Read a passage about traffic and identify the rules it describes.", "read_text", [
    ("c", "Read: I come to school by bus. Amy says, “I come by bike.” How does Amy get to school?", "By bike",
     ["By bus", "On foot", "By train"], "The quotation says, “I come by bike.”"),
    ("c", "Read: Do not go at a red light. You must stop. What must you do at a red light?", "Stop",
     ["Go", "Run", "Turn left"], "The passage says you must stop."),
    ("c", "Read: In China, people drive on the right. Which side of the road do people drive on in China?", "The right side",
     ["The left side", "The middle", "The passage does not say"], "The passage says people drive on the right."),
    ("c", "Read: Some children come by subway. Which sentence matches the passage?", "Some children come by subway.",
     ["All the children walk.", "The children come by plane.", "The children do not come to school."], "The passage says some children come by subway."),
])

V("vo_plan", "Weekend Plans", 6, "上", 3,
  "Recognize film, trip, supermarket, and dictionary.",
  [("film", "movie"), ("trip", "trip"), ("supermarket", "supermarket"), ("dictionary", "dictionary")])

G("gr_going", "be going to: the Simple Future", 6, "上", 3,
  "Use am, is, or are going to for plans and future actions.", "future", [
    ("c", "Which sentence means, “I plan to take a trip”?", "I am going to take a trip.",
     ["I am go to take a trip.", "I going to take a trip.", "I are going to take a trip."], "Use “am going to” with “I.”"),
    ("c", "What does “What are you going to do?” ask?", "What you plan to do",
     ["What you are doing now", "What you did yesterday", "What you can do"], "“Going to” asks about a plan."),
    ("c", "She is going to see a film. What does she plan to do?", "See a movie",
     ["Buy a dictionary", "Go to the supermarket", "Visit her grandparents"], "The sentence says she is going to see a film."),
    ("c", "We are going to the supermarket. Where do we plan to go?", "The supermarket",
     ["The movie theater", "The bookstore", "The hospital"], "The sentence names the supermarket."),
])

F("fu_plan", "Talking About Plans", 6, "上", 3,
  "Use be going to to talk about weekend plans.", "func_out", [
    ("c", "Which sentence says you plan to take a trip tomorrow?", "I am going to take a trip tomorrow.",
     ["I am going to see a film tomorrow.", "I am going to the supermarket tomorrow.", "I am going to buy a dictionary tomorrow."], "Use “take a trip” to talk about traveling."),
    ("c", "What does “What are you going to do this weekend?” ask?", "What you plan to do this weekend",
     ["What you are doing this weekend", "What you did last weekend", "What you do every day"], "“This weekend” with “going to” refers to a plan."),
    ("c", "He is going to buy a dictionary. What is he going to buy?", "A dictionary",
     ["A movie ticket", "A trip ticket", "Bread from the supermarket"], "The sentence says he is going to buy a dictionary."),
    ("c", "What does “Have a good time!” mean?", "I hope you have fun",
     ["You must stop", "Please keep to the right", "This is too expensive"], "“Have a good time” is a wish for someone to enjoy themselves."),
])

R("rw_plan", "Understanding Weekend Plans", 6, "上", 3,
  "Read a passage about plans and identify who plans to do what.", "read_text", [
    ("c", "Read: I am going to see a film. Amy is going to the supermarket. Where is Amy going?", "The supermarket",
     ["The movie theater", "The bookstore", "The hospital"], "The passage says Amy is going to the supermarket."),
    ("c", "Read: We are going to take a trip next week. Which sentence matches the passage?", "We are going to take a trip next week.",
     ["We are traveling now.", "We traveled last week.", "We are not going on a trip."], "The passage says they are going to take a trip next week."),
    ("c", "Read: Mike is going to buy a dictionary this evening. What is Mike going to buy tonight?", "A dictionary",
     ["A movie ticket", "Bread", "A map"], "The passage says he is going to buy a dictionary."),
    ("c", "Read: Sarah says, “I am going to read a book.” What is Sarah going to do?", "Read a book",
     ["See a movie", "Go to the supermarket", "Take a trip"], "The quotation says she is going to read a book."),
])

V("vo_hobby", "Hobbies", 6, "上", 4,
  "Recognize hobby, hiking, puzzle, and dancing.",
  [("hobby", "hobby"), ("hiking", "hiking"), ("puzzle", "puzzle"), ("dancing", "dancing")])

G("gr_does", "does and Third-Person Singular", 6, "上", 4,
  "Use does in questions and add s or es to the verb in third-person singular statements.", "present3", [
    ("c", "____ he live in China? Which word completes the question?", "Does",
     ["Do", "Is", "Are"], "Use “Does” in a simple-present question with “he.”"),
    ("c", "Which sentence is correct?", "He lives in China.",
     ["He live in China.", "He living in China.", "He does lives in China."], "Change “live” to “lives” after “he.”"),
    ("c", "Does she like dancing? Which is the correct affirmative answer?", "Yes, she does.",
     ["Yes, she do.", "Yes, she is.", "Yes, she likes."], "The affirmative answer to “Does ...?” is “Yes, she does.”"),
    ("c", "What does “What are his hobbies?” ask?", "What hobbies he has",
     ["Where he lives", "What job he has", "What he plans to do"], "“Hobbies” means activities someone enjoys."),
])

F("fu_pen", "Talking About Pen Pals and Hobbies", 6, "上", 4,
  "Use “I have a pen pal” and “He likes ...” to introduce a pen pal.", "func_out", [
    ("c", "Which sentence says that you have a pen pal?", "I have a pen pal.",
     ["I have a puzzle.", "I like hiking.", "I am dancing."], "A pen pal is a friend you write to."),
    ("c", "He likes hiking. What does he like?", "Hiking",
     ["Puzzles", "Dancing", "Singing"], "The sentence says he likes hiking."),
    ("c", "What does “Does your pen pal live in Sydney?” ask?", "Whether your pen pal lives in Sydney",
     ["Whether your pen pal likes dancing", "Whether you have a puzzle", "Whether you plan to take a trip"], "The question asks whether the pen pal lives in Sydney."),
    ("c", "She likes doing word puzzles. What does she like doing?", "Word puzzles",
     ["Hiking", "Dancing", "Swimming"], "“Word puzzles” are puzzles made with words."),
])

R("rw_pen", "Understanding a Pen Pal's Introduction", 6, "上", 4,
  "Read a passage about a pen pal and identify where the person lives and what they enjoy.", "read_text", [
    ("c", "Read: I have a pen pal. He lives in Canada. He likes hiking. Where does the pen pal live?", "Canada",
     ["China", "Australia", "The United Kingdom"], "The passage says he lives in Canada."),
    ("c", "Read: Amy likes dancing and doing word puzzles. Which sentence matches the passage?", "Amy likes dancing and doing word puzzles.",
     ["Amy likes hiking.", "Amy lives in Canada.", "Amy does not like dancing."], "The passage says she likes dancing and doing word puzzles."),
    ("c", "Read: Does he like puzzles? Yes, he does. Does he like puzzles?", "Yes",
     ["No", "It does not say", "He only likes hiking"], "He answers, “Yes, he does.”"),
    ("c", "Read: Her hobby is hiking. What is her hobby?", "Hiking",
     ["Dancing", "Word puzzles", "Singing"], "The passage says her hobby is hiking."),
])

V("vo_job6", "More Jobs", 6, "上", 5,
  "Recognize factory, worker, postman, and businessman.",
  [("factory", "factory"), ("worker", "worker"), ("postman", "mail carrier"), ("businessman", "businessman")])

G("gr_work", "What Does He Do?", 6, "上", 5,
  "Ask about someone's job with “What does he do?” and use “works” to describe where they work.", "present3", [
    ("c", "What does “What does he do?” ask?", "What job he has",
     ["What he is doing now", "What he likes doing", "What he did yesterday"], "“What does he do?” asks about someone's job."),
    ("c", "He works in a factory. Where does he work?", "In a factory",
     ["At a post office", "At a hospital", "At a school"], "“Factory” means a place where goods are made."),
    ("c", "Which sentence is correct?", "She works at sea.",
     ["She work at sea.", "She working at sea.", "She does works at sea."], "Use “works” after “she.”"),
    ("c", "My uncle is a postman. What is his job?", "Mail carrier",
     ["Businessman", "Worker", "Fisherman"], "A postman delivers mail."),
])

F("fu_work", "Describing Jobs and Workplaces", 6, "上", 5,
  "Introduce a family member's job with “He is a ...” and “He works ...”.", "func_out", [
    ("c", "Which sentence says that your mother is a businesswoman?", "My mother is a businesswoman.",
     ["My mother is a postman.", "My mother is a worker.", "My mother is a factory."], "A woman who runs or works in a business is a businesswoman."),
    ("c", "What does “Where does he work?” ask?", "Where he works",
     ["Who he is", "What he likes", "What he plans to do"], "The question asks about his workplace."),
    ("c", "He is a fisherman. He works at sea. Where does he work?", "At sea",
     ["In a factory", "At a post office", "At a hospital"], "The sentence says he works at sea."),
    ("c", "She works in a university. Where does she work?", "At a university",
     ["In a factory", "At sea", "At a post office"], "A university is a place of higher education."),
])

R("rw_work", "Understanding a Passage About Jobs", 6, "上", 5,
  "Read a passage about jobs and identify who does what and where they work.", "read_text", [
    ("c", "Read: My father is a worker. He works in a factory. Where does the father work?", "In a factory",
     ["At a post office", "At sea", "At a university"], "The passage says he works in a factory."),
    ("c", "Read: My aunt is a businesswoman. She works in a university. What is her job?", "Businesswoman",
     ["Worker", "Mail carrier", "Fisherman"], "Her job is businesswoman; the university is her workplace."),
    ("c", "Read: He is a postman. He works in a post office. Which sentence matches the passage?", "He is a mail carrier and works at a post office.",
     ["He is a worker.", "He works in a factory.", "He works at sea."], "The passage says he is a postman and works in a post office."),
    ("c", "Read: John wants to be a coach. What does John want to be?", "A coach",
     ["Businessman", "Mail carrier", "Fisherman"], "The passage says he wants to be a coach."),
])

V("vo_feel", "Feelings", 6, "上", 6,
  "Recognize angry, afraid, sad, and happy.",
  [("angry", "angry"), ("afraid", "afraid"), ("sad", "sad"), ("happy", "happy")])

G("gr_should", "should for Giving Advice", 6, "上", 6,
  "Use should with the base form of a verb to give advice.", "modal_imp", [
    ("c", "Which sentence means, “You should see a doctor”?", "You should see a doctor.",
     ["You should sees a doctor.", "You are should see a doctor.", "You see should a doctor."], "Use the base form “see” after “should.”"),
    ("c", "What does “I feel ill” mean?", "I do not feel well",
     ["I am very happy", "I am very angry", "I am very afraid"], "“Ill” means unwell."),
    ("c", "What is “You should wear warm clothes” doing?", "Giving advice",
     ["Describing the past", "Asking about a price", "Asking for directions"], "Use “should” to give advice."),
    ("c", "What does “Do not be sad” mean?", "Do not feel sad",
     ["Do not feel angry", "Do not be afraid", "Do not be happy"], "“Sad” means unhappy."),
])

F("fu_feel", "Asking How Someone Feels and Giving Advice", 6, "上", 6,
  "Ask “How do you feel?” and use should to offer advice.", "func_out", [
    ("c", "Which question asks someone how they feel?", "How do you feel?",
     ["What are you going to do?", "Where does he work?", "How do you come to school?"], "Ask “How do you feel?” to ask about someone's feelings."),
    ("c", "I am angry. How does this person feel?", "Angry",
     ["Afraid", "Sad", "Happy"], "The sentence says the person is angry."),
    ("c", "You should take a deep breath. What does this sentence advise?", "Take a deep breath",
     ["See a doctor", "Wear warm clothes", "Count to ten"], "“Take a deep breath” means to breathe in slowly and deeply."),
    ("c", "The mouse is afraid of the cat. How does the mouse feel about the cat?", "Afraid",
     ["Angry", "Happy", "Sad"], "“Afraid of” means frightened by something."),
])

R("rw_feel", "Understanding Feelings and Advice", 6, "上", 6,
  "Read a passage and identify people's feelings and the advice they receive.", "read_text", [
    ("c", "Read: Sarah is sad. She should talk to her friends. How does Sarah feel?", "Sad",
     ["Angry", "Afraid", "Happy"], "The passage says Sarah is sad."),
    ("c", "Read: I am ill. I should see a doctor. Which sentence matches the passage?", "I do not feel well and should see a doctor.",
     ["I am very happy.", "I should not see a doctor.", "I am afraid of cats."], "The passage says the speaker is ill and should see a doctor."),
    ("c", "Read: He is angry. He should take a deep breath. What should he do?", "Take a deep breath",
     ["Take a trip", "Buy a dictionary", "Ride a bicycle"], "The passage advises him to take a deep breath."),
    ("c", "Read: The cat is happy. The mouse is afraid. Who is happy?", "The cat",
     ["The mouse", "The doctor", "Both of them"], "The passage says the cat is happy."),
])

# ---------- Grade 6, Book 2 ----------

P("ph_tone", "Intonation in Statements and Questions", 6, "下", 1,
  "General questions usually have rising intonation; statements, commands, and wh-questions usually have falling intonation.", "tone", [
    ("c", "What intonation is usually used for a yes-or-no question?", "Rising intonation",
     ["Falling intonation", "Falling, then rising, then falling", "No intonation"], "Yes-or-no questions such as “Do you like apples?” usually have rising intonation."),
    ("c", "What intonation is usually used when reading the statement “I am ten”?", "Falling intonation",
     ["Rising intonation", "A rise to the highest pitch", "No intonation"], "Statements usually have falling intonation."),
    ("c", "What intonation is usually used when reading the command “Open the door”?", "Falling intonation",
     ["Rising intonation", "Rising, then falling, then rising", "No intonation"], "Commands usually have falling intonation."),
    ("c", "What intonation is usually used for “Where is the cat?”?", "Falling intonation",
     ["Rising intonation", "Only rising intonation", "No intonation"], "Wh-questions beginning with “Where” usually have falling intonation."),
])

V("vo_measure", "Height and Weight", 6, "下", 1,
  "Recognize metre, kilogram, size, and heavy.",
  [("metre", "meter"), ("kilogram", "kilogram"), ("size", "size"), ("heavy", "heavy")])

G("gr_comp", "Comparative Adjectives", 6, "下", 1,
  "Form the comparative adjectives taller, longer, and heavier from tall, long, and heavy.", "compare", [
    ("c", "What is the comparative form of “tall”?", "taller",
     ["more tall", "tallest", "tallier"], "The comparative form of “tall” is “taller.”"),
    ("c", "Which sentence is correct?", "He is taller.",
     ["He is more taller.", "He is tallier.", "He is more tall."], "Do not add “more” before “taller.”"),
    ("c", "What is the comparative form of “long”?", "longer",
     ["more long", "longest", "longger"], "The comparative form of “long” is “longer.”"),
    ("c", "What is the comparative form of “heavy”?", "heavier",
     ["more heavy", "heavyler", "heavyer"], "The comparative form of “heavy” is “heavier.”"),
])

G("gr_than", "Comparisons with than", 6, "下", 1,
  "Compare two things using a comparative adjective followed by than.", "compare", [
    ("c", "Which sentence makes a correct comparison?", "I am taller than you.",
     ["I am more taller than you.", "I am taller then you.", "I am tall than you."], "Use “taller than” to compare two people."),
    ("c", "Amy is 1.5 metres tall. John is 1.6 metres tall. Who is taller?", "John",
     ["Amy", "They are the same height", "There is not enough information"], "1.6 is greater than 1.5, so John is taller."),
    ("n", "Zhang Peng weighs 48 kilograms. Sarah weighs 42 kilograms. How many kilograms does the heavier person weigh?", 48,
     "48 is greater than 42, so the heavier person weighs 48 kilograms."),
    ("c", "This dinosaur is bigger than that one. What is being compared?", "Which one is bigger",
     ["Which one is taller", "Which one is heavier", "Which one is older"], "“Bigger” means larger."),
])

F("fu_tall", "Asking About Height", 6, "下", 1,
  "Ask about height and weight with “How tall are you?” and “How heavy are you?”", "func_out", [
    ("c", "Which question asks how tall someone is?", "How tall are you?",
     ["How old are you?", "How heavy are you?", "How much is it?"], "Ask “How tall are you?” to find out someone's height."),
    ("c", "What does “I am 1.6 metres tall” describe?", "A height of 1.6 metres",
     ["A weight of 1.6 kilograms", "An age of 16 years", "A shoe size of 36"], "Metres are used to describe height."),
    ("c", "If you weigh 40 kilograms, how should you answer “How heavy are you?”?", "I am 40 kilograms.",
     ["I am 1.5 metres.", "I am 12 years old.", "I am size 36."], "Use kilograms to describe weight."),
    ("c", "Your feet are bigger than mine. What is being compared?", "The size of the feet",
     ["Height", "Weight", "Age"], "“Feet” and “bigger” show that foot size is being compared."),
])

R("rw_cmp", "Understanding Comparisons", 6, "下", 1,
  "Read a passage with comparisons and use the numbers to decide who is taller or heavier.", "read_text", [
    ("c", "Read: Amy is 1.5 metres tall. John is 1.6 metres tall. John is taller than Amy. Who is taller?", "John",
     ["Amy", "They are the same height", "The passage does not compare them"], "1.6 is greater than 1.5, and the passage says John is taller."),
    ("n", "Read: The dinosaur is 4 metres tall. The boy is 1 metre tall. How tall is the dinosaur in metres?", 4, "The passage says it is 4 metres tall."),
    ("c", "Read: Sarah weighs 42 kilograms. Zhang Peng weighs 48 kilograms. Who is heavier?", "Zhang Peng",
     ["Sarah", "They weigh the same", "It is not possible to tell"], "48 is greater than 42."),
    ("c", "Read: My shoes are size 37. Yours are size 35. Which sentence matches the passage?", "My shoes are size 37, and yours are size 35.",
     ["My shoes are size 35.", "Our shoes are the same size.", "The sizes are not given."], "The passage gives shoe sizes 37 and 35."),
])

G("gr_past", "Past Tense of Regular Verbs", 6, "下", 2,
  "Form the past tense of clean, watch, and stay: cleaned, watched, and stayed.", "past", [
    ("c", "What is the past tense of “clean”?", "cleaned",
     ["cleans", "cleaning", "clean"], "The regular verb “clean” has the past-tense form “cleaned.”"),
    ("c", "Which sentence means, “I cleaned my room last weekend”?", "I cleaned my room last weekend.",
     ["I clean my room last weekend.", "I cleaning my room last weekend.", "I cleans my room last weekend."], "Use the past-tense form “cleaned” with “last weekend.”"),
    ("c", "Which verb is “watched” the past tense of?", "watch",
     ["wash", "walk", "want"], "“Watched” comes from “watch.”"),
    ("c", "I stayed at home. When did this happen?", "In the past",
     ["It is happening now", "It will happen later", "It is a daily habit"], "“Stayed” is a past-tense form."),
])

G("gr_did", "Questions with Did", 6, "下", 2,
  "Use did followed by a base-form verb to ask about the past.", "past", [
    ("c", "____ you clean your room? Which word completes this question about the past?", "Did",
     ["Do", "Does", "Are"], "Use “Did” to ask about the past."),
    ("c", "Did you watch TV? Which is the correct affirmative answer?", "Yes, I did.",
     ["Yes, I do.", "Yes, I was.", "Yes, I watched."], "The affirmative answer to “Did ...?” is “Yes, I did.”"),
    ("c", "Which sentence is correct?", "Did he wash his clothes?",
     ["Did he washed his clothes?", "Does he washed his clothes?", "Did he washes his clothes?"], "Use the base form “wash” after “Did.”"),
    ("c", "What does “I did not stay at home” mean?", "I did not stay at home",
     ["I stayed at home", "I am staying at home", "I will stay at home"], "“Did not stay” means the person did not stay there in the past."),
])

F("fu_weekend", "Talking About Last Weekend", 6, "下", 2,
  "Use “What did you do last weekend?” to talk about a past weekend.", "func_out", [
    ("c", "Which question asks what someone did last weekend?", "What did you do last weekend?",
     ["What do you do on the weekend?", "What are you going to do?", "What are you doing?"], "Ask “What did you do last weekend?” about the past."),
    ("c", "I cleaned my room and watched TV. Which two things did I do?", "Clean my room and watch TV",
     ["Wash clothes and sleep", "Only clean my room", "Only watch TV"], "The sentence says “cleaned my room and watched TV.”"),
    ("c", "Did you wash your clothes? If you did, how should you answer?", "Yes, I did.",
     ["Yes, I do.", "Yes, I was.", "No, I did not wash do."], "The affirmative answer to “Did ...?” is “Yes, I did.”"),
    ("c", "I stayed at home all weekend. Where was this person over the weekend?", "At home",
     ["At the park", "At the hospital", "On a trip"], "The sentence says the person stayed at home."),
])

R("rw_weekend", "Understanding a Last-Weekend Diary", 6, "下", 2,
  "Read a diary in the past tense and identify what the writer did.", "read_text", [
    ("c", "Read: Last weekend I cleaned my room. I did not watch TV. Did this person watch TV?", "No",
     ["Yes", "Only for a little while", "The passage does not say"], "The passage says the person did not watch TV."),
    ("c", "Read: Amy washed her clothes on Saturday. Which sentence matches the diary?", "Amy washed her clothes on Saturday.",
     ["Amy watched TV on Saturday.", "Amy did not wash her clothes.", "Amy washed her clothes on Sunday."], "The diary says she washed her clothes on Saturday."),
    ("c", "Read: Did you stay at home? Yes, I did. Did this person stay at home?", "Yes",
     ["No", "They went to the park", "There is no answer"], "The answer is “Yes, I did.”"),
    ("c", "Read: I watched a film on Sunday. What did the person do on Sunday?", "Watch a movie",
     ["Clean the room", "Wash clothes", "Take a trip"], "The passage says the person watched a film."),
])

G("gr_irr", "Past Tense of Irregular Verbs", 6, "下", 3,
  "Recognize the past-tense forms went, saw, and ate for go, see, and eat.", "past", [
    ("c", "What is the past tense of “go”?", "went",
     ["goed", "goes", "going"], "The past tense of “go” is “went.”"),
    ("c", "What is the past tense of “see”?", "saw",
     ["seed", "seen", "seeed"], "The past tense of “see” is “saw.”"),
    ("c", "Which sentence is correct?", "I went to the park.",
     ["I goed to the park.", "I go to the park yesterday.", "I going to the park yesterday."], "Use “went” to say that someone went somewhere in the past."),
    ("c", "What is the past tense of “eat”?", "ate",
     ["eated", "eats", "eating"], "The past tense of “eat” is “ate.”"),
])

F("fu_trip", "Talking About Places You Visited", 6, "下", 3,
  "Ask where someone went in the past with “Where did you go?”", "func_out", [
    ("c", "Which question asks where someone went?", "Where did you go?",
     ["Where do you go?", "Where are you going?", "Where did you went?"], "Ask “Where did you go?” about a past trip."),
    ("c", "I went to Xinjiang. Where did I go?", "Xinjiang",
     ["Beijing", "Shanghai", "Hainan"], "The sentence says the speaker went to Xinjiang."),
    ("c", "What does “What did you do there?” ask?", "What you did there",
     ["Where you will go", "What you are doing now", "Whether you like that place"], "It asks what someone did there in the past."),
    ("c", "I saw grapes and ate good food. What did I do?", "See grapes and eat delicious food",
     ["Only go to the park", "Wash clothes", "Watch a movie"], "The sentence says the speaker saw grapes and ate good food."),
])

R("rw_trip", "Understanding a Travel Diary", 6, "下", 3,
  "Read a travel diary and find where the writer went and what they saw.", "read_text", [
    ("c", "Read: I went to Hainan. I saw the beach. Where did the writer go?", "Hainan",
     ["Xinjiang", "Beijing", "Shanghai"], "The passage says the writer went to Hainan."),
    ("c", "Read: We ate fresh food and took pictures. Which sentence matches the diary?", "We ate fresh food and took pictures.",
     ["We did not eat anything.", "We went to school.", "We washed our clothes."], "The diary says they ate fresh food and took pictures."),
    ("c", "Read: Where did you go? I went to a forest. What kind of place did the person visit?", "A forest",
     ["A beach", "A hospital", "A store"], "The answer says the person went to a forest."),
    ("c", "Read: I saw a mule. It was interesting. What did the writer see?", "A mule",
     ["A horse", "A cat", "A dog"], "A mule is the animal the writer saw."),
])

V("vo_change", "Past and Present", 6, "下", 4,
  "Recognize ago, different, active, and Internet.",
  [("ago", "ago"), ("different", "different"), ("active", "active"), ("Internet", "Internet")])

G("gr_was", "was and were", 6, "下", 4,
  "Use was and were for past states, and use there was to say that something existed in the past.", "past", [
    ("c", "There ____ no library in my school ten years ago. Which word completes the sentence?", "was",
     ["is", "were", "are"], "Use “There was” with the singular noun “library.”"),
    ("c", "Which sentence means, “I was short before”?", "I was short.",
     ["I were short.", "I was shorted.", "I am short yesterday."], "The past-tense form used with “I” is “was.”"),
    ("c", "They ____ young then. Which word completes the sentence?", "were",
     ["was", "are", "is"], "Use “were” with “they” in the past tense."),
    ("c", "What does “There were no computers in the old school” mean?", "There were no computers in the school in the past",
     ["There were computers in the school in the past", "There are no computers in the school now", "The computers are in the library"], "“There were no” means that something did not exist in the past."),
])

F("fu_now", "Comparing the Past and Present", 6, "下", 4,
  "Use “Before, I was ... Now, I am ...” to compare the past and present.", "func_out", [
    ("c", "Which sentence says that someone was quiet before and is active now?", "Before, I was quiet. Now, I am active.",
     ["Before, I am quiet. Now, I was active.", "Before, I were quiet. Now, I am active.", "Now, I was quiet. Before, I am active."], "Use “was” for the past and “am” for the present."),
    ("c", "What does “There was no Internet ten years ago” mean?", "There was no Internet ten years ago",
     ["There is no Internet now", "There was Internet ten years ago", "The Internet is in the library"], "The sentence says there was no Internet ten years ago."),
    ("c", "What does “How did you change?” ask?", "How you have changed",
     ["How tall you are now", "What you did last weekend", "How you get to school"], "“Change” means to become different."),
    ("c", "Now there is a gym. What is there now?", "A gym",
     ["A library", "The Internet", "A computer"], "The sentence says there is a gym now."),
])

R("rw_now", "Understanding Past-and-Present Comparisons", 6, "下", 4,
  "Read a passage comparing the past and present, and distinguish between the two time periods.", "read_text", [
    ("c", "Read: Before, there was no library. Now, there is a big library. Is there a library now?", "Yes",
     ["No", "There is only a gym", "The passage does not say"], "The passage says there is a big library now."),
    ("c", "Read: I was short before. Now I am tall. Which sentence matches the passage?", "I was short before, and now I am tall.",
     ["I was tall before, and now I am short.", "I have always been short.", "I was already tall before."], "The passage says the writer was short before and is tall now."),
    ("c", "Read: There were no computers in my old school. Were there computers in the old school?", "No",
     ["Yes", "There was only one", "The passage says there are none now"], "The passage says there were no computers."),
    ("c", "Read: People did not use the Internet then. Now we use it every day. Do people use the Internet now?", "Yes",
     ["No", "They only use phones", "The passage does not say"], "The passage says people use it every day now."),
])

X("vo_confuse", "Commonly Confused Words: there, its, and too", "Vocabulary", 6, "下", 4, "conceptual",
  "Distinguish there from their, its from it's, and too from two in sentences. This topic is included here for review; the book assignment is pending verification.",
  "confuse", [
    ("c", "____ is a book on the desk. Which word completes the sentence?", "There",
     ["Their", "They are", "Theirs"], "Use “There is” to say that something exists."),
    ("c", "The dog wagged ____ tail. Which word completes the sentence?", "its",
     ["it's", "it is", "its is"], "Use “its” for possession; it has no apostrophe."),
    ("c", "I have two pens. I want one, ____. Which word completes the sentence?", "too",
     ["two", "to", "and"], "Use “too” to mean “also.”"),
    ("c", "____ books are on the desk. Which word means “belonging to them”?", "Their",
     ["There", "They are", "Theirs"], "Use “Their” to show that the books belong to them."),
], conf="exact")

R("rw_letter", "Understanding a Short Letter", 6, "下", 4,
  "Read a short letter and identify its time, place, and event.", "read_write", [
    ("c", "Read the note: Dear Amy, I went to the park last Sunday. I saw a lake. Love, Mike. Where did Mike go last Sunday?", "The park",
     ["A school by the lake", "A hospital", "A supermarket"], "The note says Mike went to the park."),
    ("c", "Read the note: I am going to visit you in June. In which month does the writer plan to visit?", "June",
     ["May", "March", "October"], "The note says “in June.”"),
    ("c", "Which sentence is appropriate at the beginning of a letter?", "Dear Sarah,",
     ["Love, Sarah,", "Yours, Sarah,", "How tall are you, Sarah,"], "A greeting often begins with “Dear” followed by the person's name."),
    ("c", "Read the note: Before, I could not swim. Now I can. Which sentence matches the note?", "I could not swim before, but now I can.",
     ["I could swim before.", "I cannot swim now.", "I plan to go swimming."], "The note says the writer could not swim before but can now."),
])
