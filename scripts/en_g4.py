# -*- coding: utf-8 -*-
"""Grade 4, fall and spring. Common PEP unit order for students who started English in Grade 3; book assignment to be verified."""
from en_tx import V, S, P, G, F, R

# "上"/"下" are term tokens consumed by the topic helpers and stay unchanged.
# ---------- Grade 4, fall ----------

S("ph_ae", "a-e pronunciation", 4, "上", 1,
  "Recognize the a-e sound in words such as cake, name, face, and make.",
  "a-e pronunciation", ["cake", "name", "face", "make"], ["cat", "bag", "map", "hat"], "magic_e")

V("vo_class", "Classroom items", 4, "上", 1,
  "Read and recognize classroom, window, door, and blackboard.",
  [("classroom", "classroom"), ("window", "window"), ("door", "door"), ("blackboard", "blackboard")])

G("gr_lets", "Making suggestions with Let's", 4, "上", 1,
  "Understand and use Let's to suggest doing something together.", "lets", [
    ("c", "Which sentence suggests opening the book together?", "Let's open the book.",
     ["Let open the book.", "Let's opens the book.", "Let is open the book."], "Use Let's followed by the base form of a verb to make a suggestion."),
    ("c", "What does \"Let's clean the classroom.\" do?", "Suggests cleaning the classroom together",
     ["Ask where the classroom is", "Say who owns the classroom", "Ask how many classrooms there are"], "Let's makes a suggestion to do something together."),
    ("c", "Which sentence is a correct suggestion?", "Let's go.",
     ["Let's goes.", "Let we go.", "Let's going."], "Use the base form go after Let's."),
    ("c", "What does \"Let's be friends.\" mean?", "Let's be friends.",
     ["We are not friends", "Are you my friend?", "He is a friend"], "\"Let's be friends\" suggests becoming friends."),
])

F("fu_class", "Classroom suggestions", 4, "上", 1,
  "Use Let's to suggest turning on the light, closing the door, cleaning the blackboard, and other classroom actions.", "func_place", [
    ("c", "Which sentence suggests cleaning the blackboard together?", "Let's clean the blackboard.",
     ["Let's open the door.", "Let's close the window.", "Let's sit down."], "A blackboard is called a blackboard."),
    ("c", "What does \"Let's open the door.\" suggest doing?", "Open the door",
     ["Close the door", "Open the window", "Clean the blackboard"], "Open the door means to open the door."),
    ("c", "What does \"Close the window, please.\" mean?", "Please close the window",
     ["Please open the window", "Please open the door", "Please sit down"], "Close the window means to shut the window."),
    ("c", "What does \"We have a new classroom.\" mean?", "We have a new classroom",
     ["We have a new blackboard", "Please open the door", "Let's be friends"], "Classroom means a room for classes."),
])

R("rw_class", "Reading a classroom notice", 4, "上", 1,
  "Read a short classroom notice and identify what needs to be done.", "read_short", [
    ("c", "Read: \"Let's clean the classroom. Open the door, please.\" What action is suggested first?", "Clean the classroom",
     ["Close the door", "Open the window", "Sit down"], "The first sentence says to clean the classroom."),
    ("c", "Read: \"The window is blue. The door is yellow.\" What color is the door?", "Yellow",
     ["Blue", "Green", "Red"], "The text says the door is yellow."),
    ("c", "Read: \"This is our classroom. We have a big blackboard.\" Which sentence matches the passage?", "Our classroom has a big blackboard.",
     ["Our classroom has no blackboard.", "The window is black.", "The door is blue."], "The passage says, \"We have a big blackboard.\""),
    ("c", "Read: \"Let's close the window.\" Which sentence has the same meaning?", "Let's close the window.",
     ["Let's open the window.", "Let's open the door.", "Let's clean the blackboard."], "Close the window means to shut the window."),
])

S("ph_ie", "i-e pronunciation", 4, "上", 2,
  "Recognize the i-e sound in words such as like, kite, five, and bike.",
  "i-e pronunciation", ["like", "kite", "five", "bike"], ["big", "pig", "sit", "fish"], "magic_e")

V("vo_bag", "School supplies", 4, "上", 2,
  "Read and recognize schoolbag, pencil, ruler, and eraser.",
  [("schoolbag", "schoolbag"), ("pencil", "pencil"), ("ruler", "ruler"), ("eraser", "eraser")])

F("fu_bag", "Talking about school supplies", 4, "上", 2,
  "Use I have and What is in your schoolbag? to talk about school supplies.", "func_place", [
    ("c", "Which question asks what is in someone's schoolbag?", "What is in your schoolbag?",
     ["Where is your schoolbag?", "What colour is your schoolbag?", "Who is your schoolbag?"], "Ask what is inside with \"What is in ...?\""),
    ("c", "I have a pencil and a ruler. What is in the schoolbag?", "A pencil and a ruler",
     ["A pencil and an eraser", "A ruler and an eraser", "Only a pencil"], "A pencil is a pencil, and a ruler is a ruler."),
    ("c", "Put your eraser in the schoolbag. What should be put in the schoolbag?", "An eraser",
     ["A pencil", "A ruler", "A book"], "Eraser means an eraser."),
    ("c", "Which sentence means \"I have a ruler\"?", "I have a ruler.",
     ["I have an eraser.", "I have a pencil.", "I have a schoolbag."], "Ruler means a ruler."),
])

R("rw_bag", "Reading about school supplies", 4, "上", 2,
  "Read sentences about school supplies and identify the items and colors.", "read_short", [
    ("c", "Read: \"I have a new schoolbag. It is black.\" What color is the schoolbag?", "Black",
     ["Blue", "Yellow", "Green"], "The text says, \"It is black.\""),
    ("c", "Read: \"What is in your schoolbag? A pencil and an eraser.\" What is inside?", "A pencil and an eraser",
     ["A ruler and a book", "Only a pencil", "Only an eraser"], "The text says, \"A pencil and an eraser.\""),
    ("n", "Read: \"I have three pencils and one ruler.\" How many pencils are there?", 3, "There are three pencils."),
    ("c", "Read: \"The ruler is blue. The eraser is white.\" Which sentence matches the text?", "The ruler is blue.",
     ["The ruler is white.", "The eraser is blue.", "The schoolbag is blue."], "The text says the ruler is blue."),
])

S("ph_oe", "o-e pronunciation", 4, "上", 3,
  "Recognize the o-e sound in words such as nose, note, home, and rose.",
  "o-e pronunciation", ["nose", "note", "home", "rose"], ["dog", "box", "hot", "not"], "magic_e")

V("vo_friend", "Describing friends", 4, "上", 3,
  "Read and recognize friend, strong, quiet, and friendly.",
  [("friend", "friend"), ("strong", "strong"), ("quiet", "quiet"), ("friendly", "friendly")])

G("gr_has", "He has and I have", 4, "上", 3,
  "Use I have to say what you have, and He has or She has to say what someone else has.", "present_basic", [
    ("c", "He ____ a new pen. Which word belongs in the blank?", "has",
     ["have", "is", "are"], "Use has after he."),
    ("c", "Which sentence is correct?", "She has a bag.",
     ["She have a bag.", "She has are a bag.", "She having a bag."], "Use has after she."),
    ("c", "I ____ a ruler. Which word belongs in the blank?", "have",
     ["has", "am", "is"], "Use have after I."),
    ("c", "What does \"He has glasses.\" mean?", "He has glasses",
     ["He does not have glasses", "He is glasses", "The glasses have him"], "Has glasses means owns or wears glasses."),
])

F("fu_friend", "Introducing a friend", 4, "上", 3,
  "Use He is and He has to describe what a friend looks like.", "func_daily", [
    ("c", "Which sentence describes a strong friend?", "He is strong.",
     ["He is quiet.", "He is friendly.", "He is tall."], "Strong means strong."),
    ("c", "\"She is friendly.\" How is she?", "She is friendly",
     ["She is quiet", "She is strong", "She is short"], "Friendly means kind and pleasant."),
    ("c", "What does \"What is his name?\" ask?", "What his name is",
     ["Where he is", "What he has", "Where he is from"], "\"What is his name?\" asks for a name."),
    ("c", "Which sentence means the same as \"My friend is quiet.\"?", "My friend is quiet.",
     ["My friend is strong.", "My friend is friendly.", "My friend is tall."], "Quiet means not noisy."),
])

R("rw_friend", "Reading a friend's description", 4, "上", 3,
  "Read a short description of a friend and identify the person's name and traits.", "read_short", [
    ("c", "Read: \"I have a friend. He is strong. His name is John.\" What is the friend's name?", "John",
     ["Mike", "Amy", "Sarah"], "The passage says his name is John."),
    ("c", "Read: \"She is quiet and friendly.\" Which sentence matches the passage?", "She is quiet and friendly.",
     ["She is strong and tall.", "She is not friendly.", "He is quiet."], "The passage says quiet and friendly about she."),
    ("c", "Read: \"He has a blue bag.\" What does he have?", "A blue bag",
     ["A red bag", "Glasses", "A ruler"], "The passage says he has a blue bag."),
    ("c", "Read: \"My friend is Amy. She has long hair.\" Who has long hair?", "Amy",
     ["John", "Mike", "Chen Jie"], "Amy is the friend, and she has long hair."),
])

S("ph_ue", "u-e pronunciation", 4, "上", 4,
  "Recognize the u-e sound in words such as use, cute, tube, and huge.",
  "u-e pronunciation", ["use", "cute", "tube", "huge"], ["fun", "run", "cup", "sun"], "magic_e")

V("vo_home", "Rooms at home", 4, "上", 4,
  "Read and recognize bedroom, kitchen, bathroom, and study.",
  [("bedroom", "bedroom"), ("kitchen", "kitchen"), ("bathroom", "bathroom"), ("study", "study")])

G("gr_isin", "Using is and are to say where people are", 4, "上", 4,
  "Use is or are with in to say which room one person or several people are in.", "be", [
    ("c", "She ____ in the kitchen. Which word belongs in the blank?", "is",
     ["am", "are", "be"], "Use is with she."),
    ("c", "Which sentence means \"He is in the study\"?", "He is in the study.",
     ["He are in the study.", "He am in the study.", "He be in the study."], "Use is after he."),
    ("c", "What does \"Where is she?\" ask?", "Where she is",
     ["Who she is", "What she likes", "What she has"], "\"Where is she?\" asks about a location."),
    ("c", "They ____ in the bedroom. Which word belongs in the blank?", "are",
     ["is", "am", "be"], "Use are with they."),
])

F("fu_home", "Asking which room a family member is in", 4, "上", 4,
  "Use Where is to ask which room a family member is in at home.", "func_place", [
    ("c", "Which question asks where Mom is?", "Where is my mother?",
     ["Who is my mother?", "What is my mother?", "How is my mother?"], "Use Where is to ask about a location."),
    ("c", "\"She is in the kitchen.\" Where is she?", "In the kitchen",
     ["In the bedroom", "In the bathroom", "In the study"], "Kitchen means a room for cooking."),
    ("c", "Where does \"Go to the bathroom.\" tell someone to go?", "To the bathroom",
     ["To the study", "To the kitchen", "To the bedroom"], "Bathroom means a room with a bath or toilet."),
    ("c", "What does \"Is she in the study?\" ask?", "Is she in the study?",
     ["Is she in the kitchen?", "Who owns the study?", "How big is the study?"], "Study means a room for reading or working."),
])

R("rw_home", "Reading about locations at home", 4, "上", 4,
  "Read a short passage and identify which room each person is in.", "read_short", [
    ("c", "Read: \"My father is in the study. My mother is in the kitchen.\" Where is the father?", "In the study",
     ["In the kitchen", "In the bedroom", "In the bathroom"], "The passage says the father is in the study."),
    ("c", "Read: \"The cat is in the bedroom.\" Which sentence matches the text?", "The cat is in the bedroom.",
     ["The cat is in the kitchen.", "The cat is in the study.", "Mom is in the bedroom."], "The passage says the cat is in the bedroom."),
    ("c", "Read: \"Where is Amy? She is in the bathroom.\" Where is Amy?", "In the bathroom",
     ["In the study", "In the kitchen", "In the bedroom"], "The passage says Amy is in the bathroom."),
    ("c", "Read: \"They are in the living room.\" Which word means the people being talked about?", "They",
     ["She", "He", "It"], "They refers to more than one person."),
])

S("ph_longe", "Long e sound", 4, "上", 5,
  "Recognize the long e sound in he, she, me, and we.",
  "Long e sound", ["he", "she", "me", "we"], ["ten", "pen", "red", "leg"], "magic_e")

V("vo_dinner", "Dinner foods", 4, "上", 5,
  "Read and recognize beef, chicken, noodles, and soup.",
  [("beef", "beef"), ("chicken", "chicken"), ("noodles", "noodles"), ("soup", "soup")])

F("fu_would", "Making meal offers with Would you like", 4, "上", 5,
  "Invite someone to have something with Would you like some, and accept with Yes, please.", "func_place", [
    ("c", "Which question asks someone if they would like some soup?", "Would you like some soup?",
     ["Do you like some soup?", "Where is the soup?", "I like soup."], "Use Would you like some to offer something."),
    ("c", "\"Would you like some beef?\" If you want some, what should you say?", "Yes, please.",
     ["No, I do not.", "Yes, I do.", "Here you are."], "A common way to accept an offer is Yes, please."),
    ("c", "\"What would you like?\" If you want noodles, what should you say?", "I would like some noodles.",
     ["I would like some soup.", "I would like some beef.", "I would like some chicken."], "Noodles are called noodles."),
    ("c", "What does \"Help yourself.\" mean at a meal?", "Please help yourself to the food",
     ["Please sit down", "Please open the door", "Please look at the blackboard"], "\"Help yourself\" invites someone to take food."),
])

R("rw_dinner", "Reading a dinner conversation", 4, "上", 5,
  "Read a dinner conversation and identify the food someone wants.", "read_short", [
    ("c", "Read: \"Would you like some soup? Yes, please.\" Does the person want soup?", "Yes",
     ["No", "It is not stated", "The person wants rice"], "The response is Yes, please."),
    ("c", "Read: \"I would like some noodles and beef.\" What does the person want?", "Noodles and beef",
     ["Soup and chicken", "Only noodles", "Only beef"], "The passage says noodles and beef."),
    ("c", "Read: \"Dinner is ready. Have some chicken.\" Which sentence matches the text?", "Please have some chicken.",
     ["Please have some soup.", "Dinner is not ready yet.", "Please have some noodles."], "The text says, \"Have some chicken.\""),
    ("c", "Read: \"Sarah says, 'I would like some soup.'\" What does Sarah want?", "Soup",
     ["Beef", "Chicken", "Noodles"], "Sarah asks for soup."),
])

V("vo_job", "Jobs", 4, "上", 6,
  "Read and recognize doctor, nurse, driver, and farmer.",
  [("doctor", "doctor"), ("nurse", "nurse"), ("driver", "driver"), ("farmer", "farmer")])

G("gr_job", "Asking about jobs with his and her", 4, "上", 6,
  "Use What is his job? to ask about someone's job, and his or her to identify whose family member is meant.", "pronoun", [
    ("c", "Which question asks what his job is?", "What is his job?",
     ["What is he job?", "Where is his job?", "Who is his job?"], "Ask about someone's job with What is his job?"),
    ("c", "\"He is a doctor.\" What is his job?", "Doctor",
     ["Nurse", "Driver", "Farmer"], "Doctor means a medical professional."),
    ("c", "\"My father is a driver.\" What is Dad's job?", "Driver",
     ["Doctor", "Nurse", "Farmer"], "Driver means a person who drives."),
    ("c", "Which sentence means \"Her mother is a nurse\"?", "Her mother is a nurse.",
     ["His mother is a nurse.", "Her mother is a doctor.", "His father is a nurse."], "Use her for a female person; nurse means a medical worker."),
])

F("fu_job", "Introducing family members' jobs", 4, "上", 6,
  "Use My father is a ... to describe a family member's job.", "func_daily", [
    ("c", "Which sentence says that an uncle is a farmer?", "My uncle is a farmer.",
     ["My uncle is a doctor.", "My uncle is a nurse.", "My uncle is a driver."], "Farmer means someone who works on a farm."),
    ("c", "What does \"Is this your baby brother?\" ask?", "Is this your younger brother?",
     ["Is this your father?", "Is this your uncle?", "Is this your aunt?"], "A baby brother is a younger brother."),
    ("c", "Which sentence means the same as \"She is a nurse.\"?", "She is a nurse.",
     ["She is a doctor.", "He is a nurse.", "She is a driver."], "She refers to a female person, and a nurse is a medical worker."),
    ("c", "What does \"What is your aunt's job?\" ask?", "What job your aunt has",
     ["What job your father has", "Where your mother is", "How old you are"], "An aunt is a parent's sister; job means occupation."),
])

R("rw_job", "Reading about family members' jobs", 4, "上", 6,
  "Read a short passage about family members and identify who does each job.", "read_short", [
    ("c", "Read: \"This is my father. He is a doctor.\" What is the father's job?", "Doctor",
     ["Nurse", "Driver", "Farmer"], "The passage says he is a doctor."),
    ("c", "Read: \"My mother is a nurse. My uncle is a driver.\" Who is the driver?", "The uncle",
     ["The mother", "The father", "The aunt"], "The passage says the uncle is a driver."),
    ("c", "Read: \"She is a farmer.\" Which sentence matches the text?", "She is a farmer.",
     ["He is a farmer.", "She is a doctor.", "She is a nurse."], "The passage says she is a farmer."),
    ("c", "Read: \"His father is a doctor. Her mother is a teacher.\" Whose father is a doctor?", "His father",
     ["Her father", "His mother", "Her mother"], "His father refers to the father of a male person."),
])

# ---------- Grade 4, spring ----------

V("vo_school", "Places at school", 4, "下", 1,
  "Read and recognize school, playground, library, and computer.",
  [("school", "school"), ("playground", "playground"), ("library", "library"), ("computer", "computer")])

G("gr_floor", "Floors and ordinal numbers", 4, "下", 1,
  "Use on the first floor and on the second floor to say where a place is.", "when_ord", [
    ("n", "The library is on the second floor. Which floor is the library on?", 2, "Second means the second floor."),
    ("c", "Which floor is the first floor?", "The first floor",
     ["The second floor", "The third floor", "The fourth floor"], "First means number one."),
    ("c", "Which question asks where the teachers' office is?", "Where is the teachers' office?",
     ["What is the teachers' office?", "Who is the teachers' office?", "How is the teachers' office?"], "Use Where is to ask about a location."),
    ("c", "What does \"It is on the first floor.\" say?", "It is on the first floor",
     ["It is on the second floor", "It is on the playground", "It is in the library"], "The first floor is the first level of a building."),
])

F("fu_school", "Asking for places at school", 4, "下", 1,
  "Use Where is to ask where the playground and library are at school.", "func_place", [
    ("c", "Which question asks where the library is?", "Where is the library?",
     ["Where is the playground?", "Where is the classroom?", "Do you have a library?"], "Library means a place to borrow books."),
    ("c", "\"The playground is on the first floor.\" Which floor is the playground on?", "The first floor",
     ["The second floor", "The third floor", "The fourth floor"], "The first floor is the first level of a building."),
    ("c", "What does \"Do you have a computer room?\" ask?", "Do you have a computer room?",
     ["Where is the computer room?", "Do you like computers?", "Who owns the computer?"], "Do you have asks whether someone has something."),
    ("c", "Which sentence means the same as \"This is my school.\"?", "This is my school.",
     ["This is my classroom.", "This is the library.", "This is the playground."], "School means a place where students learn."),
])

R("rw_school", "Reading a school directory", 4, "下", 1,
  "Read descriptions of places at school and identify their locations and floors.", "read_short", [
    ("c", "Read: \"The library is on the second floor.\" Which floor is the library on?", "The second floor",
     ["The first floor", "The third floor", "The fourth floor"], "The passage says the library is on the second floor."),
    ("c", "Read: \"We have a big playground.\" Which sentence matches the passage?", "We have a big playground.",
     ["We do not have a playground.", "The library is big.", "The playground is on the second floor."], "The passage says there is a big playground."),
    ("c", "Read: \"The computer room is next to the library.\" Where is the computer room?", "Next to the library",
     ["On the playground", "In the classroom", "Behind the door on the first floor"], "Next to the library gives its location. The text does not state the floor."),
    ("c", "Read: \"Classroom 2 is on the first floor.\" Which floor is Classroom 2 on?", "The first floor",
     ["The second floor", "The third floor", "The fourth floor"], "It is on the first floor; 2 is the classroom number, not the floor."),
])

V("vo_timew", "Daily activities", 4, "下", 2,
  "Read and recognize breakfast, lunch, dinner, and music.",
  [("breakfast", "breakfast"), ("lunch", "lunch"), ("dinner", "dinner"), ("music", "music")])

G("gr_time", "Asking and telling the time", 4, "下", 2,
  "Use What time is it? to ask the time and answer with a phrase such as It is 6 o'clock.", "number_q", [
    ("c", "Which question asks what time it is now?", "What time is it?",
     ["What time it is?", "How many time is it?", "Where is the time?"], "Ask the time with What time is it?"),
    ("c", "\"It is 6 o'clock.\" What time is it?", "6 o'clock",
     ["5 o'clock", "7 o'clock", "9 o'clock"], "It is 6 o'clock gives the time as six."),
    ("c", "\"It is time for lunch.\" What is it time to do?", "Eat lunch",
     ["Eat breakfast", "Eat dinner", "Have music class"], "Lunch is the midday meal."),
    ("c", "\"It is 7 o'clock. It is time for breakfast.\" Which meal should be eaten?", "Breakfast",
     ["Lunch", "Dinner", "Afternoon tea"], "Breakfast is the morning meal."),
])

F("fu_time", "Talking about the time and daily activities", 4, "下", 2,
  "Use It is time for to say when it is time to eat or go to class.", "func_daily", [
    ("c", "It is 9 o'clock and it is time for music class. Which sentence says this?", "It is 9 o'clock. It is time for music.",
     ["It is 9 o'clock. It is time for lunch.", "It is 6 o'clock. It is time for breakfast.", "It is 12 o'clock. It is time for dinner."],
     "Music is the subject, and the time must match 9 o'clock."),
    ("c", "What time is it? If it is noon, which answer is correct?", "It is 12 o'clock.",
     ["It is 10 o'clock.", "It is 2 o'clock.", "It is 8 o'clock."], "Say It is 12 o'clock for twelve."),
    ("c", "\"It is time for English.\" Which class is it time for?", "English",
     ["Music", "Math", "Physical education"], "English is the name of the subject."),
    ("c", "\"Hurry up! It is time for school.\" What is the speaker reminding someone to do?", "Go to school",
     ["Eat dinner", "Go to bed", "Go home"], "Time for school means it is time to go to school."),
])

R("rw_time", "Reading daily schedules", 4, "下", 2,
  "Read a short passage and identify when each activity happens.", "read_short", [
    ("c", "Read: \"It is 7 o'clock. It is time for breakfast.\" What should someone do at 7?", "Eat breakfast",
     ["Eat lunch", "Eat dinner", "Have music class"], "The passage says it is time for breakfast."),
    ("c", "Read: \"It is 12 o'clock. Have some lunch.\" What time is lunch?", "12 o'clock",
     ["7 o'clock", "6 o'clock", "9 o'clock"], "The passage says it is 12 o'clock."),
    ("n", "Read: \"Music is at 9 o'clock.\" What time is music class?", 9, "The passage says it is at 9 o'clock."),
    ("c", "Read: \"It is 6 o'clock. It is time for dinner.\" Which sentence matches the passage?", "It is time for dinner at 6 o'clock.",
     ["It is time for breakfast at 6 o'clock.", "It is time for dinner at 7 o'clock.", "It is time for music class at 6 o'clock."], "The passage says 6 o'clock and dinner."),
])

V("vo_weather", "Weather", 4, "下", 3,
  "Read and recognize warm, cold, cool, and hot.",
  [("warm", "warm"), ("cold", "cold"), ("cool", "cool"), ("hot", "hot")])

G("gr_weather", "Describing the weather with It is", 4, "下", 3,
  "Use What is the weather like? to ask about the weather and answer with It is plus a weather word.", "be", [
    ("c", "Which question asks about the weather?", "What is the weather like?",
     ["What is the weather is?", "How the weather like?", "Where is the weather?"], "Ask about the weather with What is the weather like?"),
    ("c", "\"It is cold.\" What is the weather like?", "It is cold",
     ["It is hot", "It is warm", "It is cool"], "Cold means low in temperature."),
    ("c", "\"It is sunny in Beijing.\" What is the weather like in Beijing?", "Sunny",
     ["Rainy", "Snowy", "Windy"], "Sunny means bright with sunshine."),
    ("c", "Which sentence means \"It is hot today\"?", "It is hot today.",
     ["It is cold today.", "It is cool today.", "It is warm today."], "Hot means high in temperature."),
])

F("fu_weather", "Talking about weather and giving suggestions", 4, "下", 3,
  "Use the weather to suggest activities, for example, It is warm. We can fly a kite.", "func_daily", [
    ("c", "It is very cold outside. Which sentence says this?", "It is cold outside.",
     ["It is hot outside.", "It is warm outside.", "It is cool outside."], "Cold means low in temperature."),
    ("c", "\"It is warm. We can fly a kite.\" Why can they fly a kite?", "Because the weather is warm",
     ["Because it is cold", "Because it is raining", "Because it is nighttime"], "It is warm describes the weather."),
    ("c", "What does \"Can I go outside?\" ask?", "May I go outside?",
     ["What is the weather like?", "What time is it?", "Do you like cold weather?"], "Go outside means to go outdoors."),
    ("c", "\"It is hot. Have some water.\" What does the speaker suggest?", "Drink some water",
     ["Put on a coat", "Fly a kite", "Close the window"], "Have some water suggests drinking water."),
])

R("rw_weather", "Reading a weather report", 4, "下", 3,
  "Read a short passage that names cities and weather, then answer based on the text.", "read_short", [
    ("c", "Read: \"It is cold and snowy in Harbin.\" What is the weather like in Harbin?", "Cold and snowy",
     ["Hot", "Warm", "Only windy"], "The passage says it is cold and snowy."),
    ("c", "Read: \"It is sunny in Beijing. It is rainy in Shanghai.\" Which city is rainy?", "Shanghai",
     ["Beijing", "Harbin", "Both cities"], "The passage says it is rainy in Shanghai."),
    ("c", "Read: \"It is warm today. Let's fly a kite.\" Which sentence matches the passage?", "It is warm today, and the speaker suggests flying a kite.",
     ["It is cold today.", "It is raining today.", "The speaker suggests staying inside."], "The passage says it is warm and suggests flying a kite."),
    ("c", "Read: \"Here is the world weather. It is cool in London.\" What is the weather like in London?", "Cool",
     ["Hot", "Cold", "Snowy"], "Cool means a little cold."),
])

V("vo_farm", "Farm", 4, "下", 4,
  "Read and recognize tomato, potato, horse, and cow.",
  [("tomato", "tomato"), ("potato", "potato"), ("horse", "horse"), ("cow", "cow")])

G("gr_these", "These are and Those are", 4, "下", 4,
  "Use These are for several things nearby and Those are for several things farther away.", "pointer", [
    ("c", "Which sentence points to several ducks nearby?", "These are ducks.",
     ["This is ducks.", "These is ducks.", "That are ducks."], "Use These are for nearby plural things."),
    ("c", "What does \"Those are horses.\" mean?", "Those horses are far away",
     ["This horse is nearby", "These horses are nearby", "That horse is far away"], "Those are refers to more than one thing farther away."),
    ("c", "In \"These are potatoes,\" what does potatoes show?", "Plural",
     ["Singular", "A person's name", "A color"], "Potatoes is the plural form of potato."),
    ("c", "Which sentence describes more than one cow?", "These are cows.",
     ["That is a cow.", "This is a cow.", "It is a cow."], "These are cows uses a plural noun."),
])

F("fu_farm", "Talking about farm animals and vegetables", 4, "下", 4,
  "Use Are these to ask whether several nearby things are a particular vegetable or animal.", "func_place", [
    ("c", "Which question asks about the nearby tomatoes?", "Are these tomatoes?",
     ["Are these potatoes?", "Is this a horse?", "Are these cows?"], "Tomatoes are the fruit of tomato plants."),
    ("c", "\"Are these horses?\" If they are, what is the correct answer?", "Yes, they are.",
     ["Yes, it is.", "No, it is not.", "Yes, these is."], "The affirmative answer to Are these ...? is Yes, they are."),
    ("c", "\"Those are cows.\" What is far away?", "Cows",
     ["Horses", "Potatoes", "Tomatoes"], "Cows are female cattle."),
    ("c", "\"The potatoes are big.\" What is big?", "The potatoes",
     ["The tomatoes", "The horses", "The cows"], "The sentence says the potatoes are big."),
])

R("rw_farm", "Reading about a farm", 4, "下", 4,
  "Read a short passage about a farm and identify the animals or vegetables described.", "read_short", [
    ("c", "Read: \"These are tomatoes. They are red.\" What are the nearby things?", "Tomatoes",
     ["Potatoes", "Horses", "Cows"], "The passage says they are tomatoes."),
    ("c", "Read: \"Those are horses. They are brown.\" What color are the horses?", "Brown",
     ["Red", "Green", "Yellow"], "The passage says the horses are brown, not black."),
    ("n", "Read: \"I see seventeen cows and eleven horses.\" How many cows are there?", 17, "The passage says there are seventeen cows."),
    ("c", "Read: \"The potatoes are big. The tomatoes are small.\" Which sentence matches the passage?", "The potatoes are big, and the tomatoes are small.",
     ["The potatoes are small, and the tomatoes are big.", "The potatoes and tomatoes are the same size.", "Their sizes are not stated."], "The passage says the potatoes are big and the tomatoes are small."),
])

V("vo_clothes", "Clothes", 4, "下", 5,
  "Read and recognize shirt, dress, skirt, and pants. Pants is a plural noun.",
  [("shirt", "shirt"), ("dress", "dress"), ("skirt", "skirt"), ("pants", "pants")])

G("gr_whose", "Whose and possessive nouns", 4, "下", 5,
  "Use Whose and the possessive 's to ask and say who owns an item of clothing.", "lets", [
    ("c", "Which question asks who owns this hat?", "Whose hat is this?",
     ["Who hat is this?", "Where hat is this?", "What hat is this?"], "Use Whose to ask about ownership."),
    ("c", "\"It is Amy's dress.\" Who owns the dress?", "Amy",
     ["Mike", "The teacher", "Me"], "Amy's shows that the dress belongs to Amy."),
    ("c", "What does \"Whose pants are these?\" ask?", "Who owns these pants",
     ["What color the pants are", "How much the pants cost", "Where the pants are"], "Whose pants asks who owns the pants."),
    ("c", "\"This is Chen Jie's skirt.\" Who owns the skirt?", "Chen Jie",
     ["Amy", "John", "Sarah"], "Chen Jie's shows that the skirt belongs to Chen Jie."),
])

F("fu_clothes", "Talking about clothes", 4, "下", 5,
  "Use Whose and I like to talk about clothes.", "func_daily", [
    ("c", "Which sentence says that you like this skirt?", "I like this skirt.",
     ["I like this shirt.", "I like this dress.", "I like these pants."], "Skirt means a garment worn from the waist down."),
    ("c", "\"Whose shirt is this?\" If it belongs to Mike, what is the answer?", "It is Mike's.",
     ["It is Amy's.", "It is Sarah's.", "It is Chen Jie's."], "Use Mike's to show that it belongs to Mike."),
    ("c", "\"These pants are Zhang Peng's.\" Who owns the pants?", "Zhang Peng",
     ["Amy", "Sarah", "John"], "Zhang Peng's shows that the pants belong to Zhang Peng."),
    ("c", "What does \"Put on your shirt.\" mean?", "Put on your shirt",
     ["Take off your skirt", "Whose pants are these?", "I like this dress"], "Put on your shirt tells someone to wear a shirt."),
])

R("rw_clothes", "Reading about who owns each item", 4, "下", 5,
  "Read sentences about clothes and identify their owners.", "read_short", [
    ("c", "Read: \"This is Amy's dress. It is red.\" Who owns the dress?", "Amy",
     ["Mike", "John", "Sarah"], "The passage says it is Amy's dress."),
    ("c", "Read: \"Whose pants are these? They are Zhang Peng's.\" Who owns the pants?", "Zhang Peng",
     ["Amy", "Chen Jie", "The teacher"], "The answer in the passage is Zhang Peng's."),
    ("c", "Read: \"I like that green skirt.\" What color is the skirt?", "Green",
     ["Red", "Blue", "Yellow"], "The passage describes a green skirt."),
    ("c", "Read: \"My shirt is white. Sarah's shirt is blue.\" Whose shirt is blue?", "Sarah's",
     ["Mine", "Amy's", "Mike's"], "The passage says Sarah's shirt is blue."),
])

V("vo_shop", "Items in a shop", 4, "下", 6,
  "Read and recognize glove, scarf, umbrella, and sunglasses.",
  [("glove", "glove"), ("scarf", "scarf"), ("umbrella", "umbrella"), ("sunglasses", "sunglasses")])

G("gr_price", "Asking prices with How much", 4, "下", 6,
  "Use How much is or How much are to ask about prices.", "number_q", [
    ("c", "Which question asks how much this shirt costs?", "How much is this shirt?",
     ["How many is this shirt?", "How old is this shirt?", "How tall is this shirt?"], "Use How much to ask about a price."),
    ("n", "The sunglasses are 50 yuan. How much do they cost?", 50, "The sentence says 50 yuan."),
    ("c", "The gloves are 8 yuan. How much do they cost?", "8 yuan",
     ["7 yuan", "18 yuan", "80 yuan"], "The sentence says 8 yuan."),
    ("c", "What does \"How much is it?\" ask?", "How much it costs",
     ["How much it weighs", "How tall it is", "How many there are"], "How much asks about a price."),
])

F("fu_shop", "Shopping in a store", 4, "下", 6,
  "Use Can I help you? and How much to complete a simple shopping conversation.", "func_place", [
    ("c", "Which sentence does a shop assistant often use to greet a customer?", "Can I help you?",
     ["How old are you?", "Where are you from?", "Let's clean the room."], "Shop assistants often say Can I help you?"),
    ("c", "Which sentence means \"This scarf is pretty\"?", "This scarf is pretty.",
     ["This umbrella is pretty.", "These gloves are pretty.", "These sunglasses are pretty."], "Scarf means a long piece of cloth worn around the neck."),
    ("c", "\"How much is this umbrella?\" If it costs 15 yuan, what is the answer?", "It is 15 yuan.",
     ["It is 50 yuan.", "They are 8 yuan.", "It is 5 yuan."], "Use It is for one umbrella; the price is 15 yuan."),
    ("c", "What does \"They are too expensive.\" mean?", "They cost too much",
     ["They are very cheap", "I want to buy them", "They cost 10 yuan"], "Too expensive means costing too much."),
])

R("rw_price", "Reading price tags", 4, "下", 6,
  "Read sentences with shop prices and identify each item and its cost.", "read_short", [
    ("c", "Read: \"The scarf is 20 yuan. The umbrella is 15 yuan.\" How much is the scarf?", "20 yuan",
     ["15 yuan", "50 yuan", "8 yuan"], "The passage says the scarf costs 20 yuan."),
    ("n", "Read: \"The sunglasses are 50 yuan.\" How much do the sunglasses cost?", 50, "The passage says 50 yuan."),
    ("c", "Read: \"Can I help you? The gloves are 8 yuan.\" Which sentence matches the text?", "The gloves cost 8 yuan.",
     ["The gloves cost 15 yuan.", "The umbrella costs 8 yuan.", "The scarf costs 8 yuan."], "The passage says the gloves cost 8 yuan."),
    ("c", "Read: \"The umbrella is cheap. It is 10 yuan.\" What is the umbrella like?", "It is cheap and costs 10 yuan",
     ["It is expensive and costs 50 yuan", "It is cheap and costs 20 yuan", "Its price is not stated"], "Cheap means not expensive; the price is 10 yuan."),
])
