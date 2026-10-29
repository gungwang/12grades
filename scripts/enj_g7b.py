# -*- coding: utf-8 -*-
"""Grade 7, second semester. Common unit sequence for the People's Education Press Go for it! series; unit names and semester placement are to be verified."""
from en_tx import V, P, G, F, R

# "下" is a parser-structural semester code; retain it in catalog entries.

def q(prompt, answer, wrongs, expl):
    return ("c", prompt, answer, wrongs, expl)


V("vo_talent", "Talents and Clubs", 7, "下", 1,
  "Recognize guitar, chess, club, and dance.",
  [("guitar", "guitar"), ("chess", "chess"), ("club", "club"), ("dance", "dance")], "vocab7")

G("gr_can7", "Modal Verb Can", 7, "下", 1,
  "Use can and can't to talk about abilities.", "modal", [
    q("How do you say \"I can play the guitar\"?", "I can play the guitar.",
      ["I can to play the guitar.", "I can plays the guitar.", "I can play guitar the."],
      "Use the base form of a verb after can; musical instruments usually take the."),
    q("How do you say \"She cannot play chess\"?", "She can't play chess.",
      ["She can't plays chess.", "She can not to play chess.", "She doesn't can play chess."],
      "Use the base form play after can't."),
    q("What is the correct short affirmative answer to \"Can you swim?\"?", "Yes, I can.",
      ["Yes, I do.", "Yes, I can swim yes.", "Yes, I am."], "Answer a question with can using can."),
    q("How do you ask whether he can dance?", "Can he dance?",
      ["Does he can dance?", "Can he dances?", "Is he can dance?"], "Move can to the beginning and use the base form."),
])

F("fu_club", "Talking about Talents and Clubs", 7, "下", 1,
  "Ask about someone's abilities and say which club you want to join.", "func_school", [
    q("How would you ask someone whether they can draw?", "Can you draw?",
      ["Do you can draw?", "Can you draws?", "Are you can draw?"], "Can you draw asks about ability."),
    q("How would you say that you want to join the music club?", "I want to join the music club.",
      ["I want join the music club.", "I want to join the music clubbing.", "I wants to join the music club."],
      "Want to join means to want to become a member."),
    q("Someone asks, \"Can you play the piano?\" You cannot. How should you answer?", "No, I can't.",
      ["No, I don't.", "No, I am not.", "No, I can."], "The negative short answer to can is No, I can't."),
    q("What does \"What club do you want to join?\" ask?", "Which club you want to join",
      ["Whether you can swim", "Where the club is", "How much the guitar costs"], "What club asks which club."),
])

R("rw_ad", "Reading a Club Advertisement", 7, "下", 1,
  "Read a club advertisement and identify the abilities it requires.", "read_detail", [
    q("Music Club. Can you sing or dance? Come and join us. Call Mr. Brown. What abilities does the club want?", "Singing or dancing",
      ["Playing chess", "Playing soccer", "Drawing"], "It says sing or dance."),
    q("Music Club. Can you sing or dance? Come and join us. Call Mr. Brown. Who should you contact?", "Mr. Brown",
      ["Mr. Green", "Gina", "Tom"], "It says Call Mr. Brown."),
    q("We need students for the chess club. Can you play chess? What ability do the students need?", "They need to be able to play chess",
      ["Play the guitar", "Swim", "Speak English"], "Play chess means to play chess."),
    q("We need students for the chess club. Can you play chess? Which statement matches the advertisement?", "The club wants students who can play chess.",
      ["The club wants singers.", "Students must play the guitar.", "The club is only for teachers."],
      "The advertisement is looking for students who can play chess."),
])

V("vo_daily", "Daily Routines", 7, "下", 2,
  "Recognize shower, exercise, quarter, and homework.",
  [("shower", "shower"), ("exercise", "exercise"), ("quarter", "quarter"), ("homework", "homework")], "vocab7")

G("gr_clock", "Telling Time", 7, "下", 2,
  "Tell the time using past, to, and numbers.", "question", [
    q("How do you say 6:15?", "a quarter past six",
      ["a quarter to six", "six past a quarter", "half past six"], "Fifteen minutes past the hour is a quarter past."),
    q("How do you say 6:30?", "half past six",
      ["half to six", "six half", "a quarter past six"], "Thirty minutes past the hour is half past."),
    q("How do you say 6:45?", "a quarter to seven",
      ["a quarter past seven", "seven to a quarter", "half to seven"], "Fifteen minutes before seven is a quarter to seven."),
    q("What does \"What time do you get up?\" ask?", "What time you get up",
      ["Where you get up", "Why you get up", "Who you get up with"], "What time asks about a specific time."),
])

G("gr_often", "Adverbs of Frequency", 7, "下", 2,
  "Choose among always, usually, sometimes, and never according to frequency.", "present", [
    q("He exercises every day. Which word fits best?", "always",
      ["never", "sometimes", "seldom only once"], "Use always for something done every day."),
    q("How do you say that she is never late?", "She is never late.",
      ["She never is late.", "She is late never.", "She never late."],
      "Put the adverb after be: is never."),
    q("What does usually mean in \"I usually do my homework at 7\"?", "Usually",
      ["Never", "Every time without exception", "Only on weekends"], "Usually means usually."),
    q("Which list orders the adverbs from most frequent to least frequent?", "always, usually, sometimes, never",
      ["never, sometimes, usually, always", "usually, never, always, sometimes", "sometimes, always, never, usually"],
      "Always is the most frequent and never the least frequent."),
])

F("fu_time7", "Talking about Daily Routines", 7, "下", 2,
  "Ask and say what time daily activities happen.", "func_school", [
    q("How would you ask someone what time they go to school?", "What time do you go to school?",
      ["What time does you go to school?", "What time do you goes to school?", "When time do you go to school?"],
      "Use What time do you with you."),
    q("How do you say that you get up at 6:30?", "I get up at half past six.",
      ["I get up in half past six.", "I gets up at half past six.", "I get up on half past six."],
      "Use at before a time, and use I get up."),
    q("What does \"When do you usually exercise?\" ask?", "When you usually exercise",
      ["Whether you can exercise", "Where you exercise", "How much exercise costs"], "When and usually ask about the usual time."),
    q("How would you say that he usually does his homework in the evening?", "He usually does his homework in the evening.",
      ["He usually do his homework in the evening.", "He usually does his homework on the evening.", "He usually does his homeworks in the evening."],
      "Use does with he, homework is uncountable, and say in the evening."),
])

R("rw_day7", "Reading a Daily Schedule", 7, "下", 2,
  "Read a short passage about routines and identify the times.", "read_detail", [
    q("Scott gets up at 6:00. He exercises at 6:30. He goes to school at 7:15. What time does he exercise?", "6:30",
      ["6:00", "7:15", "8:00"], "He exercises at 6:30."),
    q("Scott gets up at 6:00. He exercises at 6:30. He goes to school at 7:15. What time does he go to school?", "7:15",
      ["6:00", "6:30", "7:45"], "He goes to school at 7:15."),
    q("Mary usually does her homework at 7:00 in the evening. She never watches TV on school nights. Does she watch TV on school nights?", "No, never",
      ["Yes, always", "Yes, sometimes", "Only for half an hour"], "It says she never watches TV on school nights."),
    q("Mary usually does her homework at 7:00 in the evening. Which statement matches the passage?", "Mary usually does homework at seven in the evening.",
      ["Mary never does homework.", "Mary does homework at seven in the morning.", "Mary gets up at 7:00."],
      "At 7:00 in the evening means at seven o'clock at night."),
])

V("vo_trans7", "Transportation", 7, "下", 3,
  "Recognize train, subway, bike, and bus.",
  [("train", "train"), ("subway", "subway"), ("bike", "bike"), ("bus", "bus")], "vocab7")

G("gr_howfar", "Asking about Transportation with How", 7, "下", 3,
  "Use how, how long, and how far to ask about transportation, travel time, and distance.", "question", [
    q("How would you ask someone how they get to school?", "How do you get to school?",
      ["How does you get to school?", "How do you gets to school?", "How you get to school?"],
      "Use How do you get with you."),
    q("How would you say that the distance is about 10 kilometers?", "It is about ten kilometers.",
      ["It are about ten kilometers.", "It is about ten kilometer.", "It is about ten kilometers far."],
      "Use it is; the plural of kilometer is kilometers. Do not add far after a specific distance."),
    q("What does \"How long does it take?\" ask?", "How much time it takes",
      ["How far away it is", "How to get there", "Where it is"], "How long asks about duration."),
    q("How do you say that she walks to school?", "She walks to school.",
      ["She goes to school by foot.", "She walk to school.", "She walks to school by foot."],
      "Use walks to school or goes to school on foot; by foot is not standard, and do not combine it with walks to."),
])

F("fu_trans7", "Talking about How You Get to School", 7, "下", 3,
  "Say how you get to school and how long it takes.", "func_life", [
    q("How would you say that you take the subway to school?", "I take the subway to school.",
      ["I by the subway to school.", "I take the subway to school by.", "I takes the subway to school."],
      "Say I take the subway."),
    q("How would you ask how far the school is?", "How far is it from your home to school?",
      ["How long is it from your home to school?", "How far it is from your home to school?", "How old is it from your home to school?"],
      "Use How far to ask about distance."),
    q("What does \"It takes me 20 minutes\" mean?", "It takes me 20 minutes",
      ["The school is 20 kilometers away.", "I have 20 bicycles.", "I am 20 years old."], "Take plus an amount of time describes how long something takes."),
    q("How would you say that he rides his bike to school?", "He rides his bike to school.",
      ["He ride his bike to school.", "He rides his bike by bike.", "He by bike to school."],
      "Say He rides his bike; do not add by bike as well."),
])

R("rw_trans7", "Reading about Transportation", 7, "下", 3,
  "Read a passage about travel and identify the transportation method and travel time.", "read_detail", [
    q("Lisa lives 5 kilometers from school. She rides her bike. It takes her 15 minutes. How does she get to school?", "By bike",
      ["By subway", "By train", "On foot"], "Rides her bike means travels by bicycle."),
    q("Lisa lives 5 kilometers from school. She rides her bike. It takes her 15 minutes. About how long does the trip take?", "15 minutes",
      ["5 minutes", "50 minutes", "15 kilometers"], "15 minutes is a duration; 5 kilometers is a distance."),
    q("Tom takes the bus. The bus ride takes about 20 minutes. What transportation does Tom use?", "A bus",
      ["A bicycle", "A train", "A subway"], "It says he takes the bus."),
    q("Tom takes the bus. The bus ride takes about 20 minutes. Which statement matches the passage?", "Tom's bus ride is about 20 minutes.",
      ["Tom walks for 20 minutes.", "Tom lives 20 kilometers away.", "Tom rides a bike."],
      "It says the bus ride takes about 20 minutes."),
])

V("vo_rule7", "School-Rules Vocabulary", 7, "下", 4,
  "Recognize rule, hallway, fight, and uniform.",
  [("rule", "rule"), ("hallway", "hallway"), ("fight", "fight"), ("uniform", "uniform")], "vocab7")

G("gr_imp7", "Imperatives", 7, "下", 4,
  "Use affirmative and negative imperatives to give commands.", "sentence", [
    q("How do you say \"Do not eat in class\"?", "Don't eat in class.",
      ["Not eat in class.", "Don't eating in class.", "Doesn't eat in class."],
      "Form a negative imperative with Don't and the base form of a verb."),
    q("How do you say \"Please be on time\"?", "Please be on time.",
      ["Please is on time.", "Please to be on time.", "Please being on time."],
      "Use the base form be after please."),
    q("Which sentence is an imperative?", "Listen to the teacher.",
      ["She listens to the teacher.", "Does she listen to the teacher?", "She is listening to the teacher."],
      "An imperative omits the subject and begins with a base-form verb."),
    q("What does \"Don't run in the hallways\" mean?", "Do not run in the hallways",
      ["Please run in the hallways.", "She does not run in the hallways.", "There are no rules in the hallways."], "Don't run is a negative command."),
])

G("gr_must7", "Must and Have To", 7, "下", 4,
  "Use must and have to to express obligation, and can't to express prohibition.", "modal", [
    q("How do you say that we must be quiet in the library?", "We must be quiet in the library.",
      ["We must are quiet in the library.", "We must to be quiet in the library.", "We must quiet in the library."],
      "Use the base form be after must."),
    q("How do you say that he has to get up early?", "He has to get up early.",
      ["He have to get up early.", "He has to gets up early.", "He must to get up early."],
      "Use has to with he, followed by a base-form verb."),
    q("How do you say that listening to music in class is not allowed?", "We can't listen to music in class.",
      ["We can't to listen to music in class.", "We don't can listen to music in class.", "We can't listening to music in class."],
      "Use the base form listen after can't."),
    q("What do must and have to both express?", "Obligation",
      ["Possibility", "A past habit", "An action in progress"], "Both express something that is required."),
])

F("fu_rule7", "Stating Rules", 7, "下", 4,
  "Say what students must and must not do at school.", "func_school", [
    q("How would you tell new students not to fight in the hallways?", "Don't fight in the hallways.",
      ["Not fight in the hallways.", "Doesn't fight in the hallways.", "Fight don't in the hallways."],
      "Use Don't fight to state the rule."),
    q("How would you say that students must wear the school uniform?", "Students must wear the school uniform.",
      ["Students must wears the school uniform.", "Students must to wear the school uniform.", "Students wear must the school uniform."],
      "Must wear means required to wear."),
    q("The teacher is saying no in response to \"Can we eat in the classroom?\" What is the correct answer?", "No, you can't.",
      ["No, you don't.", "No, you aren't eat.", "Yes, you can't."], "Refuse with No, you can't."),
    q("What does \"We have to be on time\" mean?", "We must be on time",
      ["We may be late.", "We are being on time.", "Being on time is optional."], "Have to expresses an obligation."),
])

R("rw_rule7", "Reading School Rules", 7, "下", 4,
  "Read several school rules and identify what is and is not allowed.", "read_detail", [
    q("Rules: Don't arrive late. Don't run in the hallways. We must wear uniforms. Are students allowed to arrive late?", "No",
      ["Yes", "Only on Mondays", "The passage does not say"], "Don't arrive late means students must not be late."),
    q("Rules: Don't arrive late. Don't run in the hallways. We must wear uniforms. What must students wear?", "Uniforms",
      ["Sneakers", "Hats", "Short skirts"], "Wear uniforms means wear school uniforms."),
    q("Students can't eat in class. They can eat in the dining hall. Where can they eat?", "In the dining hall",
      ["In class", "In the hallway", "In the library"], "The dining hall is where they can eat."),
    q("Students can't eat in class. They can eat in the dining hall. Which statement matches the passage?", "Students cannot eat in class.",
      ["Students can eat in class.", "Students must run in the hallways.", "Students arrive late every day."],
      "It says they cannot eat in class."),
])

V("vo_animal7", "Animals", 7, "下", 5,
  "Recognize tiger, elephant, panda, and koala.",
  [("tiger", "tiger"), ("elephant", "elephant"), ("panda", "panda"), ("koala", "koala")], "vocab7")

G("gr_why7", "Why and Because", 7, "下", 5,
  "Ask questions with Why and answer with because.", "clause_adv", [
    q("How do you ask why someone likes pandas?", "Why do you like pandas?",
      ["Why you like pandas?", "Why does you like pandas?", "Why do you likes pandas?"],
      "Use Why do you like with you."),
    q("How do you say \"Because they are cute\"?", "Because they are cute.",
      ["Because they is cute.", "So they are cute.", "Why they are cute."],
      "Use because to give a reason; say they are cute."),
    q("What does \"Why does she like koalas?\" ask?", "Why she likes koalas",
      ["Where she sees koalas", "What koalas eat", "Whether she can draw koalas"], "Why asks about a reason."),
    q("Which sentence is correct?", "I like elephants because they are smart.",
      ["I like elephants because they is smart.", "I like elephants so they are smart.", "Because I like elephants they are smart."],
      "The correct sentence uses because they are smart."),
])

G("gr_desc", "Descriptive Adjectives", 7, "下", 5,
  "Use adjectives to describe animals and choose the correct form of be.", "present", [
    q("How do you say that pandas are black and white?", "Pandas are black and white.",
      ["Pandas is black and white.", "Pandas are black white.", "Panda are black and white."],
      "Use are with the plural subject pandas."),
    q("How do you say that the elephant is friendly?", "The elephant is friendly.",
      ["The elephant are friendly.", "The elephant is friend.", "The elephant is friendlyly."],
      "Use is with the singular noun; friendly is the adjective."),
    q("What does kind mean?", "Kind",
      ["Scary", "Lazy", "From the south"], "Kind can describe someone or something as kind."),
    q("Which sentence means \"Tigers are a little scary\"?", "Tigers are kind of scary.",
      ["Tigers are a kind of scary.", "Tigers is kind of scary.", "Tigers are kind scary of."],
      "Kind of means somewhat and comes before an adjective."),
])

F("fu_zoo", "Talking about Animals", 7, "下", 5,
  "Ask where an animal comes from, which animals someone likes, and why.", "func_life", [
    q("How would you ask someone why they like elephants?", "Why do you like elephants?",
      ["Why are you like elephants?", "Why do you likes elephants?", "What do you like elephants?"],
      "Why do you like asks for a reason."),
    q("How would you say that pandas come from China?", "Pandas are from China.",
      ["Pandas is from China.", "Pandas are from the China.", "Panda are from China."],
      "Use are from with a plural subject."),
    q("What does \"Where are lions from?\" ask?", "Where lions come from",
      ["Why lions are cute", "What lions are eating", "How much lions cost"], "Where ... from asks about origin."),
    q("How would you say that koalas are very lazy?", "Koalas are very lazy.",
      ["Koalas is very lazy.", "Koalas are very lazily.", "Koalas very are lazy."],
      "Use are with the adjective lazy."),
])

R("rw_zoo7", "Reading Animal Descriptions", 7, "下", 5,
  "Read an animal description and identify its origin and characteristics.", "read_detail", [
    q("Pandas are from China. They are black and white. They are kind of shy. Where are pandas from?", "China",
      ["Australia", "South Africa", "India"], "It says from China."),
    q("Pandas are from China. They are black and white. They are kind of shy. What are they like?", "They are a little shy",
      ["They are very scary.", "They are lazy.", "They are friendly and the passage says they like fighting."], "Kind of shy means a little shy."),
    q("Koalas are from Australia. They sleep all day. People think they are lazy. Where are koalas from?", "Australia",
      ["China", "The United States", "The United Kingdom"], "It says from Australia."),
    q("Koalas are from Australia. They sleep all day. Which statement matches the passage?", "Koalas sleep during the day.",
      ["Koalas are from China.", "Koalas never sleep.", "Koalas are black and white."],
      "It says they sleep all day."),
])

V("vo_now", "Activities in Progress", 7, "下", 6,
  "Recognize newspaper, soup, movie, and just.",
  [("newspaper", "newspaper"), ("soup", "soup"), ("movie", "movie"), ("just", "just; only")], "vocab7")

G("gr_ing7", "Forming the Present Continuous", 7, "下", 6,
  "Use am, is, or are with a verb ending in -ing to describe an action in progress.", "continuous", [
    q("How do you say that he is watching TV?", "He is watching TV.",
      ["He watching TV.", "He is watch TV.", "He are watching TV."],
      "Form the present continuous with is and watching."),
    q("How do you say that they are eating dinner?", "They are eating dinner.",
      ["They are eat dinner.", "They is eating dinner.", "They eating dinner."],
      "Use They are eating."),
    q("How do you ask whether she is reading a book?", "Is she reading a book?",
      ["Does she reading a book?", "Is she read a book?", "Does she reads a book now?"],
      "Move is before the subject and keep reading in the -ing form."),
    q("What is the -ing form of swim?", "swimming",
      ["swiming", "swimminging", "swim"], "For a stressed closed syllable ending in one consonant, double the final consonant before adding -ing."),
])

F("fu_now", "Asking What Someone Is Doing", 7, "下", 6,
  "Ask someone on the phone what they are doing.", "func_life", [
    q("How would you ask someone what they are doing now?", "What are you doing?",
      ["What do you doing?", "What are you do?", "What is you doing?"],
      "Say What are you doing?"),
    q("How do you say that you are drinking soup?", "I am drinking soup.",
      ["I drinking soup.", "I am drink soup.", "I is drinking soup."],
      "Use I am drinking."),
    q("Is Mary talking on the phone? She is reading a newspaper. What should you answer?", "No, she is reading a newspaper.",
      ["Yes, she is reading a newspaper.", "No, she reading a newspaper.", "No, she does read a newspaper."],
      "Say no to show she is not on the phone, then say she is reading."),
    q("Someone invites you to the movies, but you are doing homework. What can you say to explain that you cannot go?", "I am doing my homework.",
      ["I do my homework every day.", "I am do my homework.", "I does my homework."],
      "Use am doing for an action happening now."),
])

R("rw_now7", "Reading about Actions in Progress", 7, "下", 6,
  "Read a passage in the present continuous and identify what each person is doing.", "read_detail", [
    q("It is Sunday morning. Tom is reading a newspaper. His mother is making soup. What is Tom doing?", "Reading a newspaper",
      ["Making soup", "Watching a movie", "Talking on the phone"], "It says he is reading a newspaper."),
    q("It is Sunday morning. Tom is reading a newspaper. His mother is making soup. What is his mother doing?", "Making soup",
      ["Reading a newspaper", "Watching TV", "Doing homework"], "It says she is making soup."),
    q("Gina is talking on the phone. She is not watching the movie. Is Gina watching the movie?", "No",
      ["Yes", "She is watching it with Tom", "The passage does not say"], "It says she is not watching the movie."),
    q("Gina is talking on the phone. She is not watching the movie. Which statement matches the passage?", "Gina is using the phone.",
      ["Gina is watching a movie.", "Gina is making soup.", "Gina is reading a newspaper."],
      "Talking on the phone means using the phone."),
])

V("vo_weather7", "Weather", 7, "下", 7,
  "Recognize rain, windy, cloudy, and sunny.",
  [("rain", "rain; to rain"), ("windy", "windy"), ("cloudy", "cloudy"), ("sunny", "sunny")], "vocab7")

G("gr_excl", "Exclamatory Sentences", 7, "下", 7,
  "Form exclamatory sentences with What and How.", "sentence", [
    q("How do you say \"What a cold day!\"?", "What a cold day it is!",
      ["What cold day it is!", "How a cold day it is!", "What a cold day is it?"],
      "Use What a before a singular count noun, and put the subject it before is."),
    q("How do you say \"The weather is so nice!\"?", "How nice the weather is!",
      ["What nice the weather is!", "How a nice the weather is!", "How nice is the weather!"],
      "Put an adjective after How, and keep statement word order."),
    q("What does \"What a sunny day!\" express?", "What a sunny day it is",
      ["Go outside on a sunny day.", "What day of the week is it?", "Where is the sun?"], "What a sunny day expresses excitement about the sunny weather."),
    q("Which sentence is exclamatory?", "How windy it is!",
      ["It is windy.", "Is it windy?", "It is not windy."], "How plus an adjective with statement word order forms an exclamation."),
])

F("fu_weather7", "Talking about the Weather", 7, "下", 7,
  "Ask about the weather and describe rain or sunshine in progress.", "func_life", [
    q("How would you ask about the weather in Beijing?", "How is the weather in Beijing?",
      ["What is the weather in Beijing?", "How is the weather in Beijing is?", "What weather is it in Beijing does?"],
      "How is the weather in Beijing is a common question."),
    q("How do you say that it is raining in Beijing?", "It is raining in Beijing.",
      ["It is rain in Beijing.", "It raining in Beijing.", "Beijing is raining."],
      "Use It is raining to describe rain in progress."),
    q("Someone says, \"It is sunny.\" You think the weather is lovely. What can you say?", "What a fine day!",
      ["What fine day!", "How a fine day!", "What a fine day it are!"],
      "Say What a fine day!"),
    q("What is another way to ask \"How is the weather?\"?", "What's the weather like?",
      ["What's the weather is like?", "How the weather is?", "What does the weather like?"],
      "What's the weather like and How is the weather mean the same thing."),
])

R("rw_weather7", "Reading a Weather Report", 7, "下", 7,
  "Read a short weather report and identify the weather in different places.", "read_detail", [
    q("It is sunny in Shanghai. It is raining in Beijing. It is windy in Guangzhou. What is the weather like in Beijing?", "It is raining",
      ["Sunny", "Windy", "Cloudy"], "It says it is raining in Beijing."),
    q("It is sunny in Shanghai. It is raining in Beijing. It is windy in Guangzhou. Where is it windy?", "Guangzhou",
      ["Shanghai", "Beijing", "All three cities"], "It says it is windy in Guangzhou."),
    q("What a cold day in Harbin! People are wearing sweaters. What are people in Harbin wearing?", "Sweaters",
      ["Skirts", "School uniforms", "Short socks"], "It says they are wearing sweaters."),
    q("What a cold day in Harbin! People are wearing sweaters. Which statement matches the passage?", "It is cold in Harbin.",
      ["It is hot in Harbin.", "People are wearing skirts.", "It is raining in Harbin."],
      "The passage says it is a cold day and does not mention rain."),
])

V("vo_place", "Places", 7, "下", 8,
  "Recognize hospital, bank, hotel, and street.",
  [("hospital", "hospital"), ("bank", "bank"), ("hotel", "hotel"), ("street", "street")], "vocab7")

G("gr_there7", "There Is and There Are", 7, "下", 8,
  "Use There is and There are to describe what is in a place.", "there_prep", [
    q("How do you say there is a bank nearby?", "There is a bank near here.",
      ["There are a bank near here.", "There have a bank near here.", "There is bank near here."],
      "Use There is with the singular noun bank."),
    q("How do you say there are two hotels on this street?", "There are two hotels on this street.",
      ["There is two hotels on this street.", "There are two hotel on this street.", "There have two hotels on this street."],
      "Use There are with the plural noun hotels."),
    q("What is the correct affirmative answer to \"Is there a hospital near here?\"?", "Yes, there is.",
      ["Yes, there are.", "Yes, it is.", "Yes, there has."], "Answer Is there with Yes, there is."),
    q("Which sentence is correctly negative?", "There isn't a post office on this street.",
      ["There isn't any post office are on this street.", "There aren't a post office on this street.", "There not a post office on this street."],
      "Use There isn't with a singular noun."),
])

F("fu_way7", "Asking for and Giving Directions", 7, "下", 8,
  "Ask for directions and give them using across from and next to.", "func_life", [
    q("How would you ask whether there is a hospital nearby?", "Is there a hospital near here?",
      ["Are there a hospital near here?", "Is there hospital near here?", "Does there a hospital near here?"],
      "Say Is there a hospital."),
    q("How would you say that the bank is opposite the hotel?", "The bank is across from the hotel.",
      ["The bank is across to the hotel.", "The bank across from the hotel.", "The bank is across from hotel the."],
      "Across from means opposite."),
    q("What does \"Where is the pay phone?\" ask?", "Where the pay phone is",
      ["How much the pay phone costs", "What brand the pay phone is", "Whose pay phone it is"], "Where asks about location."),
    q("How would you say that the post office is next to the bank?", "The post office is next to the bank.",
      ["The post office is next the bank.", "The post office next to the bank.", "The post office is next to bank the."],
      "Next to means beside."),
])

R("rw_way7", "Reading Directions", 7, "下", 8,
  "Read directions and identify where places are.", "read_detail", [
    q("The hotel is on Center Street. The bank is across from the hotel. The hospital is next to the bank. Where is the bank?", "Across from the hotel",
      ["Inside the hospital", "Beyond the end of Center Street", "Next to the post office, which the passage does not mention"], "It says across from the hotel."),
    q("The hotel is on Center Street. The bank is across from the hotel. The hospital is next to the bank. Where is the hospital relative to the bank?", "Next to the bank",
      ["Across from the bank", "Inside the hotel", "Above the bank"], "It says next to the bank."),
    q("Go along Bridge Street and turn left. The park is on the right. Which side is the park on?", "The right",
      ["The left", "Across the street", "Under the bridge"], "On the right means to the right."),
    q("Go along Bridge Street and turn left. The park is on the right. Which statement matches the directions?", "You turn left to find the park.",
      ["You turn right at once and the park is on the left.", "The park is on Bridge Street and you do not turn.", "The park is next to a hospital in this text."],
      "It says to turn left and that the park is on the right. The passage does not mention a hospital."),
])

V("vo_look", "Appearance", 7, "下", 9,
  "Recognize height, heavy, glasses, and handsome.",
  [("height", "height"), ("heavy", "heavy"), ("glasses", "glasses"), ("handsome", "handsome")], "vocab7")

G("gr_look", "Describing Appearance", 7, "下", 9,
  "Use be, have, and wear to describe appearance.", "present", [
    q("How do you say that he is tall?", "He is tall.",
      ["He has tall.", "He is a tall.", "He wears tall."], "Use be with an adjective for height, not have."),
    q("How do you say that she has long hair?", "She has long hair.",
      ["She is long hair.", "She has long hairs.", "She is has long hair."],
      "Use has to describe someone's hair; hair is usually uncountable."),
    q("How do you say that he wears glasses?", "He wears glasses.",
      ["He wears glass.", "He is wear glasses.", "He wears a glasses."],
      "Glasses is plural and does not take a."),
    q("What does \"What does he look like?\" ask?", "What he looks like",
      ["What he likes", "Whether he looks like he is reading", "Where he is from"], "Look like asks about appearance, not preference."),
])

F("fu_look", "Asking What Someone Looks Like", 7, "下", 9,
  "Ask about and describe a person's appearance.", "func_life", [
    q("How would you ask what your teacher looks like?", "What does your teacher look like?",
      ["What does your teacher like?", "What is your teacher look like?", "How does your teacher look like?"],
      "Use What does ... look like to ask about appearance. What does he like asks about preferences."),
    q("How would you say that he is of medium height?", "He is of medium height.",
      ["He has of medium height.", "He is medium height of.", "He is of medium high."],
      "Of medium height means neither tall nor short."),
    q("What does \"She has curly hair\" mean?", "She has curly hair",
      ["She is tall.", "She wears glasses.", "She is thin."], "Curly hair means hair that curls."),
    q("How would you say that the boy is thin and handsome?", "The boy is thin and handsome.",
      ["The boy is thin and handsome hair.", "The boy has thin and handsome.", "The boy are thin and handsome."],
      "Use is followed by both adjectives."),
])

R("rw_look", "Reading Appearance Descriptions", 7, "下", 9,
  "Read an appearance description and identify a person's features.", "read_detail", [
    q("My friend Jack is tall and thin. He has short black hair. He wears glasses. Does Jack wear glasses?", "Yes",
      ["No", "Only at school; the passage does not say", "The passage says he does not"], "It says he wears glasses."),
    q("My friend Jack is tall and thin. He has short black hair. What is his hair like?", "Short and black",
      ["Long and curly", "Short and blond", "He has no hair"], "It says short black hair."),
    q("Lisa is of medium height. She has long curly hair. She is a little heavy. Is Lisa heavy or thin?", "A little heavy",
      ["Very thin", "Her height is described, but not her weight", "The passage does not mention her weight"], "A little heavy means somewhat heavy."),
    q("Lisa is of medium height. She has long curly hair. Which statement matches the passage?", "Lisa's hair is long and curly.",
      ["Lisa is very short.", "Lisa has short hair.", "Lisa wears glasses in this text."],
      "It says long curly hair. The passage does not mention glasses."),
])

V("vo_noodle", "Foods for Ordering", 7, "下", 10,
  "Recognize noodle, mutton, cabbage, and dumpling.",
  [("noodle", "noodle"), ("mutton", "mutton"), ("cabbage", "cabbage"), ("dumpling", "dumpling")], "vocab7")

G("gr_would7", "Would Like", 7, "下", 10,
  "Use would like to order food and distinguish between some and any.", "modal", [
    q("How do you say that you would like a bowl of beef noodles?", "I would like a bowl of beef noodles.",
      ["I would like a bowl of beef noodle.", "I would like to a bowl of beef noodles.", "I like would a bowl of beef noodles."],
      "Use a noun directly after would like; noodles is usually plural."),
    q("How do you ask someone what they would like?", "What would you like?",
      ["What would you like to?", "What do you would like?", "What would you like it?"],
      "Say What would you like?"),
    q("Which sentence correctly offers dumplings?", "Would you like some dumplings?",
      ["Would you like any dumplings?", "Would you like some dumpling?", "Do you would like some dumplings?"],
      "Questions with would like are offers, so some is commonly used."),
    q("She would like mutton cabbage dumplings. What filling would she like?", "Mutton and cabbage",
      ["Beef", "Cabbage only, with no meat", "Fish"], "Mutton cabbage means mutton and cabbage."),
])

F("fu_order", "Ordering Food", 7, "下", 10,
  "Order food in a restaurant and ask about available varieties.", "func_life", [
    q("The waiter asks, \"May I take your order?\" You want noodles. What should you say?", "I'd like beef noodles, please.",
      ["I like beef noodles every day.", "I would like to beef noodles.", "I'd like beef noodle, please."],
      "Use I'd like to order, and use the plural noodles."),
    q("How would you ask which kind of dumplings someone would like?", "What kind of dumplings would you like?",
      ["What kind of dumplings would you like to?", "What kind dumplings you like?", "How kind of dumplings would you like?"],
      "What kind of asks which type."),
    q("What does \"Are there any vegetables in the soup?\" ask?", "Whether there are vegetables in the soup",
      ["How much the soup costs", "Whether you would like soup", "Who made the soup"], "Are there any asks whether something is present."),
    q("What does \"A large bowl, please\" mean?", "Please give me a large bowl",
      ["Please give me a small bowl", "No bowl, please", "The bowl is under the table"], "A large bowl means a large serving."),
])

R("rw_order", "Reading a Food-Ordering Conversation", 7, "下", 10,
  "Read a restaurant conversation and identify the food and serving size.", "read_detail", [
    q("Waiter: What would you like? Tom: I'd like a large bowl of mutton noodles. What kind of noodles does Tom want?", "Mutton noodles",
      ["Beef noodles", "Cabbage noodles", "Egg noodles"], "He asks for mutton noodles."),
    q("Waiter: What would you like? Tom: I'd like a large bowl of mutton noodles. What size bowl does he want?", "A large bowl",
      ["A small bowl", "A medium bowl", "No bowl"], "He asks for a large bowl."),
    q("Gina would like some cabbage dumplings. She would not like any meat. Does Gina want meat?", "No",
      ["She wants mutton.", "She wants beef.", "The passage does not say."], "She would not like any meat."),
    q("Gina would like some cabbage dumplings. Which statement matches the passage?", "Gina wants cabbage dumplings.",
      ["Gina wants mutton dumplings.", "Gina wants a bowl of soup only.", "Gina does not want dumplings."],
      "She wants cabbage dumplings."),
])

V("vo_trip7", "Trip Activities", 7, "下", 11,
  "Recognize museum, farm, fire, and flower.",
  [("museum", "museum"), ("farm", "farm"), ("fire", "fire; blaze"), ("flower", "flower")], "vocab7")

G("gr_was7", "Was and Were", 7, "下", 11,
  "Use was and were to talk about the past.", "past", [
    q("How do you say that yesterday's school trip was great?", "The school trip was great.",
      ["The school trip were great.", "The school trip is great yesterday.", "The school trip was greated."],
      "Use was with a singular subject in the past, not is with yesterday."),
    q("How do you say that the farmers were friendly?", "The farmers were friendly.",
      ["The farmers was friendly.", "The farmers were friend.", "The farmers are friendly yesterday."],
      "Use were with a plural subject in the past."),
    q("What is the correct negative answer to \"Was the weather good?\"?", "No, it wasn't.",
      ["No, it weren't.", "No, it didn't.", "No, it isn't."], "Answer Was the weather with it wasn't."),
    q("What is the correct affirmative answer to \"Were there any cows?\"?", "Yes, there were.",
      ["Yes, there was.", "Yes, there are.", "Yes, they were cows yes."], "Answer Were there with Yes, there were."),
])

G("gr_ed", "Regular Verb Past Tense", 7, "下", 11,
  "Form the past tense of regular verbs.", "past", [
    q("What is the past tense of play?", "played",
      ["plaied", "playd", "playing"], "Usually, add -ed directly."),
    q("What is the past tense of stop?", "stopped",
      ["stoped", "stopping", "stops"], "Double the final consonant in a stressed closed syllable before adding -ed."),
    q("What is the past tense of study?", "studied",
      ["studyed", "studed", "studies"], "For a consonant + y, change y to i and add -ed."),
    q("How do you say that we visited a museum yesterday?", "We visited a museum yesterday.",
      ["We visit a museum yesterday.", "We visited a museum yesterdayed.", "We visiting a museum yesterday."],
      "Use the past-tense verb visited with yesterday."),
])

P("ph_ed", "Pronunciation of Past-Tense -ed", 7, "下", 11,
  "Distinguish whether -ed is pronounced /t/, /d/, or /ɪd/.", "edsound", [
    q("In which word is -ed pronounced /ɪd/?", "visited",
      ["played", "stopped", "cleaned"], "In visited, -ed follows /t/ and is pronounced /ɪd/."),
    q("Which word has the same -ed pronunciation as stopped?", "watched",
      ["played", "lived", "needed"], "The -ed ending in stopped and watched is pronounced /t/."),
    q("Which word has the same -ed pronunciation as played?", "cleaned",
      ["stopped", "watched", "visited"], "The -ed ending in played and cleaned is pronounced /d/."),
    q("How is the ending of needed pronounced?", "/ɪd/",
      ["/t/", "/d/", "It is silent"], "Needed ends in /d/, so -ed is pronounced /ɪd/."),
])

F("fu_trip7", "Talking about a Trip", 7, "下", 11,
  "Ask how a trip was and say what happened.", "func_plan", [
    q("How would you ask someone how their school trip was?", "How was your school trip?",
      ["How is your school trip yesterday?", "How were your school trip?", "What was your school trip like did?"],
      "Say How was your school trip?"),
    q("How do you say that the trip was interesting?", "It was interesting.",
      ["It were interesting.", "It was interest.", "It is interesting yesterday."],
      "Say It was interesting."),
    q("You saw some cows. How should you answer \"Did you see any cows?\"?", "Yes, I did.",
      ["Yes, I do.", "Yes, I saw.", "Yes, I was."], "Answer a question with Did using did."),
    q("How would you say that we milked a cow?", "We milked a cow.",
      ["We milk a cow yesterday.", "We milked a cow yesterdayed.", "We milking a cow."],
      "Milk is milked in the past tense."),
])

R("rw_diary", "Reading a Trip Diary", 7, "下", 11,
  "Read a trip diary and identify the activities and feelings.", "read_detail", [
    q("June 5th. The trip was great. We visited a farm. We milked a cow and saw many flowers. Where did they go?", "A farm",
      ["A museum", "A fire station", "A school"], "It says they visited a farm."),
    q("June 5th. The trip was great. We visited a farm. We milked a cow and saw many flowers. How was the trip?", "It was great",
      ["It was terrible", "It was okay", "The passage does not say"], "It says the trip was great."),
    q("The weather was bad. It rained. We did not take any photos. Did they take photos?", "No",
      ["They took many.", "They only took pictures of flowers.", "The passage does not say."], "It says they did not take any photos."),
    q("The weather was bad. It rained. Which statement matches the diary?", "It rained and the weather was bad.",
      ["The weather was great.", "They took many photos.", "They milked a cow in this text."],
      "The diary says the weather was bad and it rained. This passage does not mention milking a cow."),
])

V("vo_wknd", "Weekend Activities", 7, "下", 12,
  "Recognize lake, beach, badminton, and visitor.",
  [("lake", "lake"), ("beach", "beach"), ("badminton", "badminton"), ("visitor", "visitor")], "vocab7")

G("gr_did7", "Questions with Did", 7, "下", 12,
  "Use Did to ask about the past and use the base form of the verb.", "past", [
    q("How do you ask whether someone played badminton last weekend?", "Did you play badminton last weekend?",
      ["Did you played badminton last weekend?", "Do you played badminton last weekend?", "Did you played badminton last weekend now?"],
      "Use the base form play after Did."),
    q("What is the correct negative answer to \"Did he go to the beach?\"?", "No, he didn't.",
      ["No, he didn't went.", "No, he doesn't.", "No, he wasn't go."],
      "Use the short answer No, he didn't; do not add another verb."),
    q("How do you say that she did not go to the lake?", "She didn't go to the lake.",
      ["She didn't went to the lake.", "She doesn't went to the lake.", "She didn't goes to the lake."],
      "Use the base form go after didn't."),
    q("What does \"What did you do last weekend?\" ask?", "What you did last weekend",
      ["What you will do next weekend", "What you usually do on weekends", "What you are doing now"], "Did with a past-time expression asks about a completed action."),
])

G("gr_irr7", "Irregular Verb Past Tense", 7, "下", 12,
  "Form the past tense of go, see, have, do, and read.", "past", [
    q("What is the past tense of go?", "went",
      ["goed", "goes", "going"], "The past tense of go is went."),
    q("What is the past tense of see?", "saw",
      ["seed", "seen", "sawed"], "The past tense of see is saw."),
    q("The past-tense spelling of read is the same as the base form. Which sentence is correct?", "I read an interesting book last night.",
      ["I readed an interesting book last night.", "I reads an interesting book last night.", "I reading an interesting book last night."],
      "The past tense of read is still spelled read, not readed."),
    q("How do you say that we had a good time?", "We had a good time.",
      ["We haved a good time.", "We has a good time yesterday.", "We had a good time yesterdayed."],
      "The past tense of have is had."),
])

F("fu_wknd", "Talking about Last Weekend", 7, "下", 12,
  "Ask and talk about what happened last weekend.", "func_plan", [
    q("How would you ask someone what they did last weekend?", "What did you do last weekend?",
      ["What did you did last weekend?", "What do you do last weekend?", "What did you last weekend?"],
      "Say What did you do?"),
    q("How do you say that you went to the beach?", "I went to the beach.",
      ["I goed to the beach.", "I go to the beach last weekend.", "I went to the beach yesterday now."],
      "Went is the past tense of go."),
    q("What does \"Who did you go with?\" ask?", "Who you went with",
      ["Where you went", "How you got there", "What day you went"], "Who ... with asks about a companion."),
    q("How do you say that the visitors played badminton?", "The visitors played badminton.",
      ["The visitors play badminton last Sunday.", "The visitors played badminton yesterdayed.", "The visitors plaied badminton."],
      "Played is the past tense of play."),
])

R("rw_wknd", "Reading a Weekend Diary", 7, "下", 12,
  "Read a weekend diary and identify activities and companions.", "read_detail", [
    q("On Saturday morning I went to the lake with my father. We went fishing. Who went with the writer on Saturday morning?", "The writer's father",
      ["The writer's mother", "A classmate", "A visitor"], "The writer went with my father."),
    q("On Saturday morning I went to the lake with my father. We went fishing. What did they do?", "They went fishing",
      ["They played badminton", "They went to the beach", "They visited a farm"], "It says they went fishing."),
    q("On Sunday Lisa stayed at home and read a book. She did not play badminton. Did she play badminton?", "No",
      ["Yes", "She played with her father.", "The passage does not say."], "It says she did not play badminton."),
    q("On Sunday Lisa stayed at home and read a book. Which statement matches the diary?", "Lisa read at home on Sunday.",
      ["Lisa went to the lake on Sunday.", "Lisa played badminton.", "Lisa did not read."],
      "It says she stayed at home and read a book."),
])
