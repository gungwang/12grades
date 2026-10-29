# -*- coding: utf-8 -*-
"""Grade 5, first and second semesters. Common unit sequence for the People's Education Press PEP series starting in Grade 3; semester placement is to be verified."""
from en_tx import V, S, P, G, F, R, X

# "上" and "下" are parser-structural semester codes; retain them in catalog entries.
# ---------- Grade 5, first semester ----------

P("ph_blend", "Initial consonant blends bl, cl, and fl", 5, "上", 1,
  "Distinguish the initial consonant blends in black, class, floor, and blue.", "blend", [
    ("c", "Which word begins with bl?", "black",
     ["class", "floor", "green"], "black begins with bl."),
    ("c", "Which word begins with cl?", "class",
     ["black", "blue", "floor"], "class begins with cl."),
    ("c", "Which word begins with fl?", "floor",
     ["black", "class", "blue"], "floor begins with fl."),
    ("c", "Which word begins with the same consonant blend as blue?", "black",
     ["class", "floor", "green"], "blue and black both begin with bl."),
])

V("vo_char", "Personality and Appearance", 5, "上", 1,
  "Recognize old, young, kind, and strict.",
  [("old", "old"), ("young", "young"), ("kind", "kind"), ("strict", "strict")])

G("gr_like_person", "What is he like", 5, "上", 1,
  "Use What is he like? to ask about someone's personality, not what they like.", "present_basic", [
    ("c", "What does \"What is he like?\" ask?", "What kind of person is he?",
     ["What does he like?", "Where is he?", "Who is he?"], "What is he like asks about personality or appearance, not preferences."),
    ("c", "He is kind. What is he like?", "He is kind.",
     ["He is strict.", "He is young.", "He is strong."], "Kind means kind."),
    ("c", "Which sentence means \"She is strict\"?", "She is strict.",
     ["She is kind.", "She is funny.", "She is quiet."], "Strict means strict."),
    ("c", "Miss White is young. What is Miss White like?", "She is young.",
     ["She is old.", "She is kind.", "She is funny."], "Young means young. The sentence does not say she is kind."),
])

F("fu_teacher", "Describing a Teacher", 5, "上", 1,
  "Use He is or She is to describe a teacher's personality.", "func_life", [
    ("c", "How would you say that the music teacher is kind?", "The music teacher is kind.",
     ["The music teacher is strict.", "The music teacher is old.", "The music teacher is young."], "Kind means kind."),
    ("c", "What does \"Who is your English teacher?\" ask?", "Who your English teacher is",
     ["What your English teacher is like", "Whether you like English", "What day you have English"], "Who is asks about a person's identity."),
    ("c", "What does \"She is strict but kind\" mean?", "She is strict but kind.",
     ["She is only young.", "She is not strict.", "She is funny."], "Strict but kind."),
    ("c", "Mr Young is our art teacher. What subject does Mr Young teach?", "Art",
     ["Music", "English", "Math"], "An art teacher teaches art."),
])

R("rw_teacher", "Understanding a Teacher Description", 5, "上", 1,
  "Read short teacher descriptions and identify personality traits.", "read_text", [
    ("c", "Read: Mr Li is our maths teacher. He is tall and strict. What is Mr Li like?", "He is tall and strict.",
     ["He is short and kind.", "He is young and funny.", "The passage only says he is old."], "The passage says tall and strict."),
    ("c", "Read: Miss White is young and kind. Which statement matches the passage?", "Miss White is young and kind.",
     ["Miss White is old and strict.", "Miss White is a male teacher.", "Miss White teaches math."], "It says young and kind; Miss is generally used for a woman."),
    ("c", "Read: I like my Chinese teacher. She is funny. What is the Chinese teacher like?", "She is funny.",
     ["She is strict.", "She is old.", "She is quiet."], "Funny means funny."),
    ("c", "Read: He is old. He is kind. Which statement is in the passage?", "He is old and kind.",
     ["He is young.", "He is strict.", "He is not kind."], "Both old and kind are stated."),
])

V("vo_week", "Days of the Week", 5, "上", 2,
  "Recognize Monday, Tuesday, Wednesday, and Friday.",
  [("Monday", "Monday"), ("Tuesday", "Tuesday"), ("Wednesday", "Wednesday"), ("Friday", "Friday")])

G("gr_haveon", "have and on Mondays", 5, "上", 2,
  "Use I have with a school subject, and use on Mondays to mean every Monday.", "when_ord", [
    ("c", "I ____ Chinese on Mondays. Which word belongs in the blank?", "have",
     ["has", "am", "is"], "Use have after I."),
    ("c", "Which sentence means \"I have Chinese class on Mondays\"?", "I have Chinese on Mondays.",
     ["I has Chinese on Mondays.", "I have Chinese in Mondays.", "I am Chinese on Mondays."], "Use on for days of the week and have after I."),
    ("c", "What is the correct affirmative answer to \"Do you often read books?\"?", "Yes, I do.",
     ["Yes, I does.", "Yes, I am.", "Yes, I have."], "The affirmative answer to Do you is Yes, I do."),
    ("c", "What does \"What do you have on Fridays?\" ask?", "What classes you have on Fridays",
     ["The date on Friday", "What the weather is like on Friday", "Where you are on Friday"], "What do you have on Fridays asks about Friday's classes."),
])

V("vo_weekend_act", "Weekend Activities", 5, "上", 2,
  "Recognize wash, watch, read, and play.",
  [("wash", "wash"), ("watch", "watch"), ("read", "read"), ("play", "play")])

F("fu_often", "Using Often to Talk about Routines", 5, "上", 2,
  "Use often and on the weekend to talk about things you do regularly.", "func_life", [
    ("c", "How would you say that you often read books on Saturdays?", "I often read books on Saturdays.",
     ["I often watch TV on Saturdays.", "I often wash clothes on Saturdays.", "I often play football on Saturdays."], "Read books means to read."),
    ("c", "What does \"What do you do on the weekend?\" ask?", "What you do on the weekend",
     ["What classes you have on Monday", "Which class you like", "What your teacher is like"], "On the weekend means during the weekend."),
    ("c", "What does someone often do on Sundays in \"I often wash my clothes on Sundays\"?", "Wash clothes",
     ["Read books", "Watch TV", "Play football"], "Wash my clothes means wash clothes."),
    ("c", "What is the correct answer if you often play sports?", "Yes, I do.",
     ["Yes, I am.", "Yes, I often do sports am.", "No, I does not."], "The affirmative answer to Do you is Yes, I do."),
])

R("rw_week", "Understanding a Weekly Timetable", 5, "上", 2,
  "Read sentences about classes and identify what is scheduled for each day.", "read_text", [
    ("c", "Read: I have Chinese, English and maths on Mondays. Do I have English on Monday?", "Yes",
     ["No", "Only Chinese", "The passage does not mention Monday"], "The sentence includes English."),
    ("c", "Read: I often read books on the weekend. What do I often do on the weekend?", "Read books",
     ["Wash clothes", "Watch TV", "Play football"], "It says read books."),
    ("c", "Read: We have PE on Fridays. Which day do we have PE?", "Friday",
     ["Monday", "Tuesday", "Wednesday"], "It says on Fridays."),
    ("c", "Read: On Wednesdays I have art. Which statement matches the passage?", "I have art on Wednesday.",
     ["I have music on Wednesday.", "I have art on Friday.", "I have art on Monday."], "Wednesdays means Wednesday, and art is art."),
])

V("vo_meal", "Meals", 5, "上", 3,
  "Recognize tea, sandwich, salad, and hamburger.",
  [("tea", "tea"), ("sandwich", "sandwich"), ("salad", "salad"), ("hamburger", "hamburger")])

F("fu_would2", "What would you like to eat", 5, "上", 3,
  "Use What would you like to eat? to order food.", "func_life", [
    ("c", "How would you ask someone what they want to eat?", "What would you like to eat?",
     ["What do you have on Mondays?", "Where is the kitchen?", "How much is the salad?"], "Ask What would you like to eat? when ordering food."),
    ("c", "What does \"I would like a sandwich and some tea\" mean?", "A sandwich and some tea",
     ["Salad and a hamburger", "Only a sandwich", "Only tea"], "It says a sandwich and some tea."),
    ("c", "If you want tea, how should you answer \"What would you like to drink?\"?", "I would like some tea.",
     ["I would like a hamburger.", "I would like a sandwich.", "I would like some salad."], "Tea is a drink."),
    ("c", "What would she like in \"She would like a salad\"?", "A salad",
     ["A hamburger", "A cup of tea", "A sandwich"], "It says a salad."),
])

R("rw_meal", "Understanding a Food Order", 5, "上", 3,
  "Read short food-ordering passages and identify what each person wants to eat.", "read_short", [
    ("c", "Read: Sarah would like a sandwich. Mike would like a hamburger. What would Sarah like?", "A sandwich",
     ["A hamburger", "Salad", "Tea"], "Sarah is matched with sandwich."),
    ("c", "Read: I would like some salad and some tea. Which statement matches the text?", "I would like some salad and some tea.",
     ["I would like a hamburger.", "I would like a sandwich.", "I would like only tea."], "The text mentions both salad and tea."),
    ("c", "Read: What would you like to eat? I would like a hamburger. What would the person like to eat?", "A hamburger",
     ["A sandwich", "Salad", "Tea"], "The answer is a hamburger."),
    ("c", "Read: My favourite food is salad. It is healthy. What is the person's favourite food?", "Salad",
     ["Tea", "A hamburger", "A sandwich"], "The text says the favourite food is salad."),
])

V("vo_can", "Ability Verbs", 5, "上", 4,
  "Recognize sing, dance, draw, and swim.",
  [("sing", "sing"), ("dance", "dance"), ("draw", "draw"), ("swim", "swim")])

G("gr_can", "Using Can to Talk about Ability", 5, "上", 4,
  "Use can followed by the base form of a verb to say that someone can do something.", "can_there", [
    ("c", "I ____ swim. Which word belongs in the blank?", "can",
     ["am", "is", "are"], "Use can to express ability."),
    ("c", "Which sentence means \"She can draw\"?", "She can draw.",
     ["She can draws.", "She cans draw.", "She is draw."], "Use the base form draw after can."),
    ("c", "What is the correct affirmative answer to \"Can you sing?\"?", "Yes, I can.",
     ["Yes, I do.", "Yes, I am.", "Yes, I sing."], "The affirmative answer to Can is Yes, I can."),
    ("c", "What does \"He cannot dance\" mean?", "He cannot dance",
     ["He can dance.", "He is dancing.", "He likes dancing."], "Cannot dance means not able to dance."),
])

F("fu_can", "Talking about What You Can Do", 5, "上", 4,
  "Use What can you do? to ask what someone is able to do.", "func_life", [
    ("c", "How would you ask someone what they can do?", "What can you do?",
     ["What do you look like?", "What would you like?", "What do you have?"], "Ask What can you do? about ability."),
    ("c", "What two things can the speaker do in \"I can sing and dance\"?", "Sing and dance",
     ["Draw and swim", "Only sing", "Only dance"], "It says sing and dance."),
    ("c", "If you cannot swim, how should you answer \"Can you swim?\"?", "No, I cannot.",
     ["No, I do not.", "Yes, I can.", "No, I am not."], "The negative answer to Can is No, I cannot."),
    ("c", "What can we do for the party in \"We can draw pictures for the party\"?", "Draw pictures",
     ["Swim", "Sing", "Cook"], "Draw pictures means to draw."),
])

R("rw_can", "Understanding a Passage about Abilities", 5, "上", 4,
  "Read a passage and identify who can do what.", "read_text", [
    ("c", "Read: John can swim. Amy can draw. Who can swim?", "John",
     ["Amy", "Sarah", "Mike"], "The passage says John can swim."),
    ("c", "Read: I can sing English songs. Which statement matches the passage?", "I can sing English songs.",
     ["I can dance.", "I cannot sing.", "I can draw."], "It says sing English songs."),
    ("c", "Read: What can you do? I can dance. What can this person do?", "Dance",
     ["Swim", "Draw", "Cook"], "The person says I can dance."),
    ("c", "Read: Zhang Peng cannot cook, but he can swim. What can Zhang Peng do?", "Swim",
     ["Cook", "Sing", "Draw"], "He cannot cook, but he can swim."),
])

V("vo_room5", "Things in a Room", 5, "上", 5,
  "Recognize bed, photo, plant, and clock.",
  [("bed", "bed"), ("photo", "photo"), ("plant", "plant"), ("clock", "clock")])

G("gr_there", "There Is and There Are", 5, "上", 5,
  "Use There is with a singular noun and There are with a plural noun to say what is in a place.", "can_there", [
    ("c", "Which sentence says there is one bed in the room?", "There is a bed.",
     ["There are a bed.", "There is beds.", "There be a bed."], "Bed is singular, so use There is."),
    ("c", "How many photos are there in \"There are two photos\"?", "2",
     ["1", "3", "12"], "Two means 2."),
    ("c", "Which sentence is correct?", "There are some plants.",
     ["There is some plants.", "There are a plant.", "There be plants."], "Plants is plural, so use There are."),
    ("c", "What does \"There is a clock\" mean?", "There is one clock",
     ["Where the clock is", "Whose clock it is", "How much the clock costs"], "There is means that something exists or is present."),
])

F("fu_there", "Describing Your Room", 5, "上", 5,
  "Use There is and There are to describe what is in a room.", "func_life", [
    ("c", "How would you say there is a big bed in the room?", "There is a big bed.",
     ["There are a big bed.", "There is big beds.", "There be a big bed."], "Use There is with one bed."),
    ("c", "What does \"There are so many pictures\" mean?", "There are many pictures",
     ["There is a bed.", "There is a clock.", "The room is dirty."], "So many pictures means many pictures."),
    ("c", "Where do the grandparents live in \"My grandparents live in a small house\"?", "In a small house",
     ["In a large school", "In a park", "In a shop"], "It says a small house."),
    ("c", "Where is the computer in \"The computer is on the desk\"?", "On the desk",
     ["On the bed", "In the photo", "Under the plant"], "It says on the desk."),
])

R("rw_room", "Understanding a Room Description", 5, "上", 5,
  "Read a passage about a room and identify what it contains.", "read_text", [
    ("c", "Read: There is a big bed and a clock. There are two plants. How many beds are there?", "1",
     ["2", "3", "There is no bed"], "There is a big bed means one bed."),
    ("n", "Read: There are three photos on the wall. How many photos are on the wall?", 3, "It says three photos."),
    ("c", "Read: There is a plant beside the clock. Where is the plant?", "Beside the clock",
     ["Under the bed", "Outside the door", "In the kitchen"], "Beside the clock means next to the clock."),
    ("c", "Read: There are some pictures. There is no computer. Which statement matches the passage?", "There are some pictures, but no computer.",
     ["There is a computer but no pictures.", "There is only one bed.", "There is nothing in the room."], "It says there are some pictures and no computer."),
])

V("vo_nature", "Nature Park", 5, "上", 6,
  "Recognize river, lake, mountain, and forest.",
  [("river", "river"), ("lake", "lake"), ("mountain", "mountain"), ("forest", "forest")])

G("gr_isthere", "Is There and Are There", 5, "上", 6,
  "Turn There is and There are into questions to ask whether something is present in a place.", "can_there", [
    ("c", "How would you ask, \"Are there any fish in the river?\"?", "Are there any fish in the river?",
     ["Is there any fish are?", "There are fish?", "Do there fish?"], "Fish is treated as plural here, so use Are there any."),
    ("c", "What is the correct affirmative answer to \"Is there a lake?\"?", "Yes, there is.",
     ["Yes, there are.", "Yes, it is.", "Yes, there be."], "The affirmative answer to Is there is Yes, there is."),
    ("c", "What is the correct negative answer to \"Are there any mountains?\"?", "No, there are not.",
     ["No, there is not.", "No, they are not.", "No, there not."], "The negative answer to Are there is No, there are not."),
    ("n", "There is one forest and there are two rivers. How many rivers are there?", 2, "There are two rivers."),
])

F("fu_park", "Talking about What's in a Park", 5, "上", 6,
  "Use Is there and Are there to talk about a nature park.", "func_life", [
    ("c", "How would you ask whether there is a lake in the park?", "Is there a lake in the park?",
     ["Are there a lake in the park?", "Is there any lakes?", "There is a lake?"], "Use Is there with one lake."),
    ("c", "What is in the park in \"There is a forest in the park\"?", "A forest",
     ["A river", "A mountain", "A lake"], "It says a forest."),
    ("c", "What does \"Are there any tall buildings?\" ask?", "Whether there are any tall buildings",
     ["Whether there is a river", "Whether there is a lake", "Whether there is a forest"], "Tall buildings means tall buildings."),
    ("c", "What is the nature park like in \"The nature park is quiet\"?", "It is quiet",
     ["It is noisy.", "It is small.", "It is expensive."], "Quiet means quiet."),
])

R("rw_park", "Understanding a Nature Park Description", 5, "上", 6,
  "Read a passage about a park and identify what it contains.", "read_text", [
    ("c", "Read: There is a lake in the park. There are some ducks on the lake. What is on the lake?", "Some ducks",
     ["Some mountains", "Some tall buildings", "A river"], "It says there are ducks on the lake."),
    ("c", "Read: Is there a forest? Yes, there is. Is there a forest?", "Yes",
     ["No", "There is only a river", "The passage does not answer"], "The answer is Yes, there is."),
    ("c", "Read: There are no tall buildings. There is a river. Which statement matches the passage?", "There are no tall buildings, and there is a river.",
     ["There are tall buildings but no river.", "There is a mountain.", "There is nothing there."], "It says no tall buildings and that there is a river."),
    ("n", "Read: There are two mountains behind the lake. How many mountains are behind the lake?", 2, "It says two mountains."),
])

# ---------- Grade 5, second semester ----------

V("vo_routine", "Daily Activities", 5, "下", 1,
  "Recognize the daily activities get up, go to school, eat dinner, and go to bed.",
  [("get up", "get up"), ("go to school", "go to school"), ("eat dinner", "eat dinner"), ("go to bed", "go to bed")])

G("gr_when", "Using When Do You to Ask about Time", 5, "下", 1,
  "Use When do you to ask when someone does an activity, and answer with a time such as at 6 o'clock.", "when_ord", [
    ("c", "How would you ask, \"When do you get up?\"?", "When do you get up?",
     ["When does you get up?", "When do you gets up?", "What do you get up?"], "Use When do you with you."),
    ("c", "I get up at 6 o'clock. What time do I get up?", "6 o'clock",
     ["5 o'clock", "7 o'clock", "8 o'clock"], "At 6 o'clock means 6 o'clock."),
    ("c", "I go to bed at 9 o'clock. What time do I go to bed?", "9 o'clock",
     ["6 o'clock", "7 o'clock", "8 o'clock"], "At 9 o'clock means 9 o'clock."),
    ("c", "What does \"When do you eat breakfast?\" ask?", "When you eat breakfast",
     ["Whether you like breakfast", "Where breakfast is", "How much breakfast costs"], "When asks about time."),
])

F("fu_day", "Talking about Daily Routines", 5, "下", 1,
  "Use I ... at ... to describe your daily routine.", "func_life", [
    ("c", "How would you say that you go to school at 7 o'clock?", "I go to school at 7 o'clock.",
     ["I get up at 7 o'clock.", "I eat dinner at 7 o'clock.", "I go to bed at 7 o'clock."], "Go to school means to attend school."),
    ("c", "If you eat dinner at 6 o'clock, how should you answer \"When do you eat dinner?\"?", "I eat dinner at 6 o'clock.",
     ["I eat dinner at 9 o'clock.", "I go to bed at 6 o'clock.", "I get up at 6 o'clock."], "The question asks when you eat dinner; the time is 6 o'clock."),
    ("c", "What do I often do on the weekend in \"I often clean my room on the weekend\"?", "Clean my room",
     ["Get up", "Go to school", "Eat dinner"], "It says clean my room."),
    ("c", "What does \"What do you do on the weekend?\" ask?", "What you do on the weekend",
     ["What time you get up", "What day you have English", "What your teacher is like"], "It asks about activities on the weekend."),
])

R("rw_day", "Understanding a Daily Routine", 5, "下", 1,
  "Read a daily-routine passage and identify when activities happen.", "read_text", [
    ("c", "Read: I get up at 6 o'clock. I go to school at 7 o'clock. What time do I go to school?", "7 o'clock",
     ["6 o'clock", "8 o'clock", "9 o'clock"], "It says go to school at 7."),
    ("n", "Read: I eat dinner at 6 o'clock and go to bed at 9 o'clock. What time do I go to bed?", 9, "It says go to bed at 9."),
    ("c", "Read: On the weekend I often wash my clothes. Which statement matches the passage?", "I often wash my clothes on the weekend.",
     ["I often go to school on the weekend.", "I wash my clothes at 6 o'clock.", "I never wash my clothes."], "It says often wash my clothes on the weekend."),
    ("c", "Read: Sarah says, \"I get up at 6:30.\" What time does Sarah get up?", "6:30",
     ["6:00", "7:00", "9:00"], "The quoted text says 6:30."),
])

V("vo_season", "Seasons", 5, "下", 2,
  "Recognize spring, summer, autumn, and winter. Use autumn for the fall season.",
  [("spring", "spring"), ("summer", "summer"), ("autumn", "autumn"), ("winter", "winter")])

F("fu_season", "Talking about Your Favorite Season", 5, "下", 2,
  "Use Which season do you like best? to talk about seasons.", "func_life", [
    ("c", "How would you ask which season someone likes best?", "Which season do you like best?",
     ["What time is it?", "What is the weather like?", "When do you get up?"], "Ask Which season do you like best? about someone's favorite season."),
    ("c", "I like summer best. I can swim. Which season do I like best?", "Summer",
     ["Spring", "Autumn", "Winter"], "It says summer."),
    ("c", "Which season is described in \"It is golden in autumn\"?", "Autumn",
     ["Spring", "Summer", "Winter"], "Autumn means autumn."),
    ("c", "What can you do in winter in \"Winter is white. I can make a snowman\"?", "Make a snowman",
     ["Swim", "Fly a kite", "Eat ice cream"], "It says make a snowman."),
])

R("rw_season", "Understanding a Passage about Seasons", 5, "下", 2,
  "Read a passage about seasons and identify a favorite season and the reason for it.", "read_text", [
    ("c", "Read: I like spring best. There are many flowers. Which season do I like best?", "Spring",
     ["Summer", "Autumn", "Winter"], "It says spring."),
    ("c", "Read: Summer is hot. I eat ice cream. What is summer like?", "It is hot",
     ["It is cold.", "There is snow.", "There are many flowers."], "It says hot."),
    ("c", "Read: My favourite season is autumn. The colours are beautiful. Which statement matches the passage?", "My favorite season is autumn.",
     ["My favorite season is winter.", "Autumn is cold.", "The passage does not mention colors."], "It says the favourite season is autumn."),
    ("c", "Read: In winter I can play in the snow. Where can I play in winter?", "In the snow",
     ["In the sea", "Among flowers", "In the classroom"], "It says in the snow."),
])

X("vo_month", "Months", "Vocabulary", 5, "下", 3, "conceptual",
  "Recognize March, May, October, and December, and know that there are 12 months in a year.", "vocab56", [
    ("c", "Which word means the third month of the year?", "March",
     ["May", "October", "December"], "The third month is March."),
    ("c", "Which month is May?", "May",
     ["March", "October", "December"], "May is the fifth month."),
    ("c", "Choose the word for the tenth month.", "October",
     ["March", "May", "December"], "The tenth month is October."),
    ("n", "How many months are there in a year?", 12, "There are 12 months in a year, from January to December."),
], conf="inferred")

G("gr_month", "Using In with Months", 5, "下", 3,
  "Use in March to refer to a month, not on March.", "when_ord", [
    ("c", "What does in March mean?", "During March",
     ["On March 1", "On Monday", "At three o'clock"], "Use in with a month to refer to the month as a whole."),
    ("c", "Which sentence says \"Children's Day is in June\"?", "Children's Day is in June.",
     ["Children's Day is on June.", "Children's Day is at June.", "Children's Day is June in."], "Use in before a month."),
    ("n", "How many months are there in a year?", 12, "There are 12 months in a year."),
    ("c", "Which month is May?", "The fifth month",
     ["The third month", "The fourth month", "The sixth month"], "May is the fifth month."),
])

F("fu_holiday", "Talking about the Month of a Holiday", 5, "下", 3,
  "Use is in to say which month a holiday falls in.", "func_life", [
    ("c", "How would you say that Teachers' Day is in September?", "Teachers' Day is in September.",
     ["Teachers' Day is in October.", "Teachers' Day is in June.", "Teachers' Day is in May."], "September is the ninth month."),
    ("c", "If Tree Planting Day is in March, how should you answer \"When is Tree Planting Day?\"?", "It is in March.",
     ["It is in May.", "It is in October.", "It is in December."], "March is the third month."),
    ("c", "We have a school trip in May. In which month is the school trip?", "May",
     ["March", "October", "December"], "It says in May."),
    ("c", "The party is in December. In which month is the party?", "December",
     ["March", "May", "October"], "December is the twelfth month."),
])

R("rw_cal", "Understanding a School Calendar", 5, "下", 3,
  "Read a school-calendar passage and identify the month of each event.", "read_text", [
    ("c", "Read: The school trip is in May. The party is in December. In which month is the trip?", "May",
     ["December", "March", "October"], "The trip is in May."),
    ("c", "Read: Tree Planting Day is in March. Which statement matches the passage?", "Tree Planting Day is in March.",
     ["Tree Planting Day is in May.", "The party is in March.", "The trip is in March."], "It says in March."),
    ("c", "Read: We have a sports meet in October. In which month is the sports meet?", "October",
     ["May", "March", "December"], "October is the tenth month."),
    ("n", "Read: There are twelve months in a year. How many months are there in a year?", 12, "It says twelve months."),
])

G("gr_ord", "Ordinal Numbers", 5, "下", 4,
  "Recognize ordinal numbers such as first, second, and third, and distinguish them from cardinal numbers.", "when_ord", [
    ("c", "How do you say 1st?", "first",
     ["one", "second", "third"], "1st is read as first."),
    ("c", "Which of these is an ordinal number?", "third",
     ["three", "thirteen", "thirty"], "Third is an ordinal number; three is a cardinal number."),
    ("n", "April is the fourth month. What number month is April?", 4, "Fourth means number 4."),
    ("c", "Which word is the English form of 2nd?", "second",
     ["two", "twelve", "twenty"], "2nd is second."),
])

F("fu_date", "Saying Dates", 5, "下", 4,
  "Say dates using expressions such as on April 1st.", "func_life", [
    ("c", "How would you say that the art show is on April 1st?", "The art show is on April 1st.",
     ["The art show is in April 1st.", "The art show is at April 1st.", "The art show is April on 1st."], "Use on with a specific date."),
    ("c", "What does \"When is the reading festival?\" ask?", "When the reading festival is",
     ["Where the reading festival is", "Whether you like reading", "How much the reading festival costs"], "When is asks about time."),
    ("c", "What date is \"It is on May 4th\"?", "May 4",
     ["April 5", "May 1", "April 4"], "May is the fifth month, and 4th means the fourth day."),
    ("c", "When is the birthday in \"My birthday is on March 21st\"?", "March 21",
     ["March 12", "May 21", "April 1"], "It says March 21st."),
])

R("rw_date", "Understanding a Date Announcement", 5, "下", 4,
  "Read an announcement and identify the date of each event.", "read_text", [
    ("c", "Read: The art show is on April 1st. What is the date of the art show?", "April 1",
     ["April 5", "May 1", "March 21"], "It says April 1st."),
    ("c", "Read: The reading festival is on May 5th. Which statement matches the announcement?", "The reading festival is on May 5.",
     ["The reading festival is on April 1.", "The art show is on May 5.", "The reading festival is in May."], "It says May 5th, and the event is the reading festival."),
    ("n", "Read: School starts on September 1st. On what day of the month does school start? Enter the day only.", 1, "The date is September 1st, so the day is 1."),
    ("c", "Read: The sports meet is on October 12th. In which month is the sports meet?", "October",
     ["April", "May", "September"], "October is the tenth month."),
])

G("gr_poss", "Possessive Pronouns", 5, "下", 5,
  "Use mine, yours, his, and hers to show ownership without repeating the noun.", "poss_pron", [
    ("c", "Which sentence says that this pen belongs to me?", "The pen is mine.",
     ["The pen is my.", "The pen is me.", "The pen is I."], "Use the possessive pronoun mine, not is my."),
    ("c", "Whose book is this? It is hers. Who owns the book?", "She does",
     ["He does", "I do", "You do"], "Hers means it belongs to her."),
    ("c", "The bag is yours. Who owns the bag?", "You do",
     ["I do", "He does", "They do"], "Yours means it belongs to you."),
    ("c", "Which sentence is correct?", "The dog is ours.",
     ["The dog is our.", "The dog is we.", "The dog is us."], "Use ours to mean it belongs to us."),
])

G("gr_ing", "Present Continuous", 5, "下", 5,
  "Use am, is, or are with a verb ending in -ing to describe an action in progress.", "continuous", [
    ("c", "He ____ reading. Which word belongs in the blank?", "is",
     ["am", "are", "be"], "Use is with he, followed by reading."),
    ("c", "Which sentence means \"They are eating dinner\"?", "They are eating dinner.",
     ["They are eat dinner.", "They eating dinner.", "They is eating dinner."], "Use are with they and the -ing form eating."),
    ("c", "What does \"I am singing\" mean?", "I am singing",
     ["I like singing.", "I can sing.", "I sang yesterday."], "Am singing describes an action in progress."),
    ("c", "What does \"What is she doing?\" ask?", "What she is doing now",
     ["Who she is", "What she can do", "What she likes doing"], "What is she doing asks about an action in progress."),
])

F("fu_whose", "Whose and Actions in Progress", 5, "下", 5,
  "Use Whose dog is it? and It is mine. to say who owns the object being discussed.", "func_life", [
    ("c", "How would you ask, \"Whose dog is this?\"?", "Whose dog is it?",
     ["Who dog is it?", "Where dog is it?", "What dog is it?"], "Use Whose to ask who owns something."),
    ("c", "If the book is mine, how should you answer \"Whose book is this?\"?", "It is mine.",
     ["It is my.", "It is me.", "It is I."], "Use mine to mean it belongs to me."),
    ("c", "The dog is his. Who owns the dog?", "He does",
     ["She does", "I do", "You do"], "His means it belongs to him."),
    ("c", "They are playing in the park. The picture is ours. Who owns the picture?", "We do",
     ["They do", "You do", "She does"], "Ours means it belongs to us."),
])

R("rw_doing", "Understanding Actions in Progress", 5, "下", 5,
  "Read a passage in the present continuous and identify who is doing what.", "read_text", [
    ("c", "Read: John is eating lunch. Amy is reading a book. What is John doing?", "Eating lunch",
     ["Reading a book", "Sleeping", "Drawing"], "It says John is eating lunch."),
    ("c", "Read: Look! The dog is sleeping. What is the dog doing?", "Sleeping",
     ["Eating", "Running", "Playing"], "It says is sleeping."),
    ("c", "Read: Whose picture is it? It is mine. I am drawing. Who is drawing?", "I am",
     ["John", "Amy", "The dog"], "I am drawing, and the picture is mine."),
    ("c", "Read: They are playing football. Which statement matches the passage?", "They are playing football.",
     ["They can play football.", "They played football yesterday.", "They do not like football."], "Are playing describes an action in progress."),
])

V("vo_rule", "Words for Rules", 5, "下", 6,
  "Recognize quietly, talk, keep, and desk.",
  [("quietly", "quietly"), ("talk", "talk"), ("keep", "keep"), ("desk", "desk")])

G("gr_imp", "Imperatives", 5, "下", 6,
  "Use an imperative beginning with a base-form verb to give an instruction, and use Do not to prohibit an action.", "modal_imp", [
    ("c", "Which sentence is an imperative?", "Talk quietly.",
     ["You talk quietly?", "She talks quietly.", "Talking quietly is."], "An imperative begins with a base-form verb."),
    ("c", "What does \"Keep to the right\" mean?", "Stay to the right",
     ["Stay to the left", "Be quiet", "Clean the desk"], "Keep to the right means stay on the right."),
    ("c", "What does \"Do not talk\" mean?", "Do not speak",
     ["Please speak", "You are speaking", "You like speaking"], "Do not talk tells someone not to speak."),
    ("c", "Which sentence means \"Please be quiet\"?", "Be quiet.",
     ["Is quiet.", "Are quiet.", "Quiet is be."], "Use the imperative Be quiet."),
])

F("fu_rule", "Stating Rules", 5, "下", 6,
  "Use imperatives to state rules for a library or classroom.", "func_life", [
    ("c", "What should you say to ask people to speak softly in a library?", "Talk quietly.",
     ["Talk loudly.", "Keep to the left.", "Do not read."], "Quietly means softly or in a quiet way."),
    ("c", "What does \"Keep your desk clean\" mean?", "Keep your desk clean",
     ["Stay to the right", "Do not speak", "You may run"], "It says to keep the desk clean."),
    ("c", "What is not allowed in the library in \"Do not eat in the library\"?", "Eating",
     ["Reading", "Speaking quietly", "Staying to the right"], "Do not eat prohibits eating."),
    ("c", "What does \"Work quietly\" ask someone to do?", "Work without making noise",
     ["Speak loudly", "Go outside to play", "Eat lunch"], "Quietly means in a quiet way."),
])

R("rw_rule", "Understanding Rules", 5, "下", 6,
  "Read a passage about rules and identify what is and is not allowed.", "read_text", [
    ("c", "Read: Talk quietly. Do not eat. Keep your desk clean. What is not allowed?", "Eating",
     ["Speaking quietly", "Keeping your desk clean", "Reading"], "It says Do not eat."),
    ("c", "Read: Keep to the right. Which statement matches the text?", "Please keep to the right.",
     ["Please keep to the left.", "Please eat something.", "Please speak loudly."], "It says Keep to the right."),
    ("c", "Read: We are reading in the library. Please work quietly. Where are the people?", "In the library",
     ["On the playground", "In the cafeteria", "In the park"], "It says in the library."),
    ("c", "Read: Do not run in the classroom. Walk quietly. How should you walk in the classroom?", "Walk quietly",
     ["Run", "Eat something", "Speak loudly"], "It says Walk quietly and Do not run."),
])
