# -*- coding: utf-8 -*-
"""People's Education Press (2019), Compulsory Book 1. Unit names follow the commonly used contents; volume assignment is unverified."""
from enh_tx import V, P, G, F, R, q


def load():
    G("gr_sentmem", "Sentence elements", 10, 0,
      "Can identify the subject, predicate, and object of a simple sentence.", "sent", [
        q("The boy likes music. Which word is the subject?", "The boy", "likes", "music", "the full stop",
          "The boy performs the action, so it is the subject."),
        q("The boy likes music. Which word is the predicate?", "likes", "The boy", "music", "a comma",
          "Likes expresses the action, so it is the predicate."),
        q("She reads English every day. Which word is the object?", "English", "She", "reads", "every day",
          "Reads is a transitive verb, and English is its object. Every day is an adverbial."),
        q("In which sentence is music the object?", "We love music", "Music sounds good", "The music is loud", "They are students",
          "In We love music, music is the object. The other three use a subject-linking verb-complement pattern."),
      ])

    G("gr_svo", "Five basic sentence patterns", 10, 0,
      "Can distinguish subject-verb, subject-verb-object, subject-linking verb-complement, double-object, and object-complement patterns.", "sent", [
        q("Birds fly. Which basic sentence pattern is this?", "Subject-verb", "Subject-verb-object", "Subject-linking verb-complement", "Double object",
          "Fly is an intransitive verb, so it has no object."),
        q("She gave me a book. Which basic sentence pattern is this?", "Double object", "Subject-verb", "Subject-linking verb-complement", "Single object",
          "Gave is followed by two objects: me and a book."),
        q("The soup tastes good. Which basic sentence pattern is this?", "Subject-linking verb-complement", "Subject-verb-object", "Double object", "Object complement",
          "Tastes is a linking verb, and good is the subject complement."),
        q("Which sentence follows the subject-verb-object pattern?", "They play basketball", "The baby cried", "He is a doctor", "She looks happy",
          "Play is a transitive verb, and basketball is its object."),
      ])

    G("gr_svoc", "Object complements", 10, 0,
      "Can identify object complements and distinguish them from double objects.", "sent", [
        q("In We call him Tom, what function does Tom serve?", "Object complement", "Subject", "Modifier", "Adverbial",
          "Tom identifies the object him, so it is an object complement."),
        q("In I found the film interesting, what function does interesting serve?", "Object complement", "Subject", "Predicate", "Indirect object",
          "Interesting describes the object the film."),
        q("Which sentence contains an object complement?", "The news made her happy", "She gave me a pen", "They are friends", "Birds can fly",
          "Happy describes the object her. Gave me a pen has two objects."),
        q("Please keep the room clean. What does clean describe?", "the room", "Please", "keep", "the full stop",
          "Clean is an object complement describing the state of the room."),
      ])

    V("vo_campus", "Campus facilities", 10, 0,
      "Recognize campus, lecture, locker, and freshman.",
      [("campus", "school grounds"), ("lecture", "talk"), ("locker", "storage locker"), ("freshman", "first-year student")], "vo_school")

    F("fu_greet", "Greeting and introducing yourself", 10, 0,
      "Can greet a new classmate and say which class you are in.", "fu_daily", [
        q("On the first day of school, which sentence is appropriate for greeting someone and giving your name?", "Hi, my name is Lin",
          "Hi, my name are Lin", "Hi, your name is Lin", "Hi, my name Lin is",
          "Use Hi, my name is to greet someone and give your name."),
        q("Someone says Nice to meet you. What should you reply?", "Nice to meet you too",
          "See you yesterday", "Nice to meeting you too", "Nice to meets you too",
          "Add too when replying to Nice to meet you."),
        q("Which sentence tells a classmate that you are in Class 3?", "I am in Class 3",
          "I am at Class 3", "I is in Class 3", "He is in Class 3",
          "Use I am in Class 3 to say which class you are in."),
        q("Which greeting can you use when you meet a teacher in the school building in the morning?", "Good morning",
          "Good mornings", "Good moning", "Good monring",
          "Use Good morning to greet someone in the morning."),
      ])

    _w = "Lin is a new student. She is in Class 3. Her first lecture is on Monday."
    R("rw_welcome", "Reading a new student's profile", 10, 0,
      "Read a brief profile of a new student and identify her class and the day of her first lecture.", "rw_detail", [
        q(_w + " What is Lin?", "a new student", "a teacher", "a doctor", "a driver", "The passage says she is a new student."),
        q(_w + " Which class is she in?", "Class 3", "Class 1", "Class 5", "Class 9", "The passage says she is in Class 3."),
        q(_w + " On what day is her first lecture?", "Monday", "Tuesday", "Friday", "Sunday", "The passage says it is on Monday."),
        q(_w + " Which statement matches the passage?", "Lin has a lecture on Monday",
          "Lin is a teacher", "Lin is in Class 9", "The lecture is on Friday",
          "The passage says only that she is a new student and has a lecture on Monday."),
      ])

    R("wr_welcome", "Writing a self-introduction", 10, 0,
      "Can choose sentences for a self-introduction based on required points.", "rw_write", [
        q("Key points: name Lin Xiao, Class 3, and a love of music. Which sentence includes all three?",
          "I am Lin Xiao in Class 3, and I like music",
          "I am Lin Xiao in Class 3", "I like music and football", "I am Lin Xiao in Class 3, and I like football",
          "The name, class, and music preference all need to be included."),
        q("Which sentence is suitable for introducing yourself as a new student to a pen pal by email?",
          "I am a new student at this school",
          "I is a new student at this school", "I am an new student at this school", "I not am a new student at this school",
          "Use I am a new student to introduce yourself."),
        q("Which sentence mentions a hobby in a self-introduction?", "I enjoy playing basketball",
          "The campus is large", "Monday is a day", "Class 3 is a room",
          "Enjoy playing basketball describes a hobby."),
        q("Which sentence is suitable as the opening of a self-introduction?", "Hello, let me introduce myself",
          "Hello, let me itnroduce myself", "Hello, let me introdcue myself", "Hello, let me inroduce myself",
          "A self-introduction can begin with Hello, let me introduce myself."),
      ])

    P("ph_toneb", "Rising and falling intonation at sentence ends", 10, 0,
      "Can distinguish the falling intonation of statements and wh-questions from the rising intonation of yes/no questions.", "tone_b", [
        q("What intonation is usually used at the end of the yes/no question Are you in Class 3?", "rising intonation",
          "falling intonation", "stress on every word", "no intonation", "Yes/no questions usually end with rising intonation."),
        q("What intonation is usually used at the end of the statement I am a new student?", "falling intonation",
          "rising intonation", "rise, then fall, then rise again", "keep rising only on student", "Statements usually end with falling intonation."),
        q("What intonation is usually used at the end of the wh-question Where is the lecture?", "falling intonation",
          "rising intonation", "the same rising intonation as yes/no questions", "rise only on where", "Wh-questions usually end with falling intonation."),
        q("Which sentence usually ends with rising intonation?", "Is the locker yours",
          "The locker is mine", "Where is the locker", "She is a freshman",
          "Is the locker yours is a yes/no question, so it ends with rising intonation."),
      ])

    V("vo_course", "Courses and homework", 10, 1,
      "Recognize course, homework, quiz, and grade.",
      [("course", "class"), ("homework", "school assignments"), ("quiz", "short test"), ("grade", "score")], "vo_school")

    V("vo_challenge", "Challenges and clubs", 10, 1,
      "Recognize challenge, debate, volunteer, and confident.",
      [("challenge", "difficult task"), ("debate", "formal discussion"), ("volunteer", "person who offers help"), ("confident", "self-assured")], "vo_school")

    G("gr_np", "Noun phrases", 10, 1,
      "Can identify noun phrases and determine their function in a sentence.", "phrase", [
        q("The tall boy in blue. What kind of phrase is this?", "Noun phrase", "Verb phrase", "A standalone preposition", "Adverb phrase",
          "Boy is the head noun, preceded by a determiner and an adjective."),
        q("What function can My new schoolbag serve in a sentence?", "Subject or object", "Predicate", "Linking verb", "Auxiliary verb",
          "A noun phrase can serve as a subject or object, but not as a predicate by itself."),
        q("Which is a noun phrase?", "a difficult maths course", "runs quickly", "very carefully", "looks happy",
          "Course is the head noun, preceded by an article and an adjective."),
        q("She joined the school debate team. Which is the object?", "the school debate team",
          "She", "joined", "the word school by itself", "The school debate team is a noun phrase and the object of joined."),
      ])

    G("gr_adjp", "Adjective and adverb phrases", 10, 1,
      "Can identify adjective and adverb phrases and determine whether they function as subject complements or adverbials.", "phrase", [
        q("The question is very difficult. What is very difficult?", "An adjective phrase used as a subject complement",
          "A noun phrase used as a subject", "A verb phrase used as a predicate", "A prepositional phrase used as an object",
          "Difficult is an adjective modified by very; the phrase follows a linking verb as a subject complement."),
        q("He spoke quite clearly. What is quite clearly?", "An adverb phrase used as an adverbial",
          "A noun phrase used as an object", "An adjective phrase used as a subject complement", "A double object",
          "Clearly is an adverb modifying spoke, so it functions as an adverbial."),
        q("Which is an adjective phrase?", "good at maths", "the maths course", "speak English", "in the morning",
          "Good is an adjective, and at maths completes its meaning."),
        q("She is afraid of the quiz. What does afraid of the quiz describe?", "She",
          "is", "the word the", "the full stop", "The subject complement describes the state of the subject She."),
      ])

    F("fu_club", "Talking about courses and clubs", 10, 1,
      "Can name a favorite course and respond to a suggestion to join a club.", "fu_daily", [
        q("Which sentence is suitable for saying that English is your favorite course?", "My favourite course is English",
          "Your favourite course is English", "My fvaourite course is English", "My favourtie course is English",
          "Use My favourite course is to name your favorite course."),
        q("A classmate suggests joining the debate club, and you agree. What should you reply?", "That sounds good. I will join",
          "That sounds good. I will joined", "That sounds good. I will to join", "That suonds good. I will join",
          "You can accept the suggestion by saying That sounds good."),
        q("How can you ask whether someone has joined a club?", "Have you joined a club",
          "Have you joined an club", "Have you jioned a club", "Have you joiend a club",
          "Use Have you joined a club to ask someone."),
        q("Which sentence says that volunteering makes you more confident?",
          "Volunteering makes me more confident",
          "Volunteering make me more confident", "Vlounteering makes me more confident", "Volunteernig makes me more confident",
          "Makes me more confident describes the change brought about by the activity."),
      ])

    _t = "Chen likes his English course, but the maths quiz is a challenge. He also joins the debate club."
    R("rw_teen", "Reading about school life", 10, 1,
      "Read a short passage about school life and identify the course and club.", "rw_detail", [
        q(_t + " Which course does Chen like?", "English", "maths", "history", "music", "The passage says he likes his English course."),
        q(_t + " What is a challenge for him?", "the maths quiz", "his English course", "the debate club", "the campus", "The passage says the maths quiz is a challenge."),
        q(_t + " Which club has he joined?", "the debate club", "the music club", "the basketball team", "the science club", "The passage says he joined the debate club."),
        q(_t + " Which statement matches the passage?", "Chen joins the debate club",
          "Chen hates English", "The English quiz is a challenge", "Chen joins the music club",
          "The maths quiz, not his English course, is a challenge."),
      ])

    R("wr_teen", "Writing a club application", 10, 1,
      "Can choose a sentence for a club application based on required points.", "rw_write", [
        q("Key points: join the debate club, enjoy discussion, and be free every Friday. Which sentence includes all three?",
          "I want to join the debate club because I like discussion and I am free on Friday",
          "I want to join the debate club", "I am free on Friday", "I like music on Monday",
          "All three points need to be included."),
        q("Which application sentence gives a reason?", "I want to join because I like debate",
          "The club is a room", "Friday is a day", "Please open the door",
          "The clause after because gives the reason for joining."),
        q("Which sentence is a suitable opening for the application?", "I would like to join the debate club",
          "I would liked to join the debate club", "I would like to joining the debate club", "I would like to joins the debate club",
          "An application can begin with I would like to join."),
        q("The teacher asks you to describe your free time in the present tense. Which sentence fits?", "I am free on Friday afternoon",
          "I was free in 1990 only", "I will was free", "I am free in Friday afternoon",
          "Use I am free to describe current availability."),
      ])

    V("vo_travel", "Travel plans", 10, 2,
      "Recognize destination, brochure, accommodation, and itinerary.",
      [("destination", "place you are going"), ("brochure", "informational booklet"), ("accommodation", "lodging"), ("itinerary", "travel plan")],
      "vo_world")

    V("vo_place", "Places to visit", 10, 2,
      "Recognize castle, waterfall, temple, and scenery.",
      [("castle", "fortified building"), ("waterfall", "water falling over a steep drop"), ("temple", "place of worship"), ("scenery", "landscape")], "vo_world")

    G("gr_futcont", "Present continuous for future plans", 10, 2,
      "Can use the present continuous to talk about future arrangements.", "tense", [
        q("I ___ Tom at the station tomorrow. Which form completes the blank to show an arranged meeting?", "am meeting",
          "meet", "was meeting", "met", "Use the present continuous am meeting for an arranged future event."),
        q("Which sentence describes an arranged future event?", "We are flying to Xi'an next Friday",
          "We fly every Friday", "We flew last Friday", "Birds are animals",
          "The present continuous with next Friday describes an arranged trip."),
        q("What does She is leaving for Beijing tonight mainly mean?", "She has arranged to leave tonight",
          "She is sleeping tonight", "She left last night", "She dislikes Beijing", "Is leaving with a future time expression indicates an arrangement."),
        q("You plan to visit the castle tomorrow. Which sentence is suitable?", "We are visiting the castle tomorrow",
          "We visit the castle yesterday", "We visited the castle tomorrow", "We are visit tomorrow",
          "Visited is past and cannot be used with tomorrow; use are visiting for an arrangement."),
      ])

    G("gr_themoment", "Present tense in time and conditional clauses", 10, 2,
      "Can use the simple present for future meaning in time and conditional clauses.", "tense", [
        q("I will call you when I ___ there. Which form completes the blank?", "arrive",
          "will arrive", "arrived", "am arrived", "Use the simple present in the when-clause to refer to the future."),
        q("If it ___ tomorrow, we will stay in. Which form completes the blank?", "rains",
          "will rain", "rained", "is rain", "Do not use will in the if-clause; use rains."),
        q("Which sentence is correct?", "I will tell her as soon as she comes",
          "I will tell her as soon as she will come", "I tell her as soon as she will come",
          "I told her as soon as she will come tomorrow",
          "Use the present tense in the as soon as-clause and will in the main clause."),
        q("We will start after the guide ___. Which form completes the blank?", "arrives",
          "will arrive", "arrive", "is arrive", "Use arrives in the time clause introduced by after."),
      ])

    F("fu_plantrip", "Talking about travel plans", 10, 2,
      "Can describe an arranged trip and respond to an invitation.", "fu_plan", [
        q("Which sentence tells a classmate that you have arranged to fly to Xi'an on Friday?", "We are flying to Xi'an on Friday",
          "We flew to Xi'an tomorrow", "We is flying to Xi'an on Friday", "We are fly to Xi'an on Friday",
          "Use the present continuous for an arranged trip."),
        q("A friend invites you to visit a waterfall, and you would like to go. What should you reply?", "Yes, I would love to",
          "Yes, I would loved to", "Yes, I would to love to", "Yes, I wuold love to",
          "You can accept an invitation by saying Yes, I would love to."),
        q("How can you ask where the other person is staying?", "Where is your accommodation",
          "Where is your accommodatoin", "Where is your acommodation", "Where is accommodation your",
          "Use Where is your accommodation to ask about lodging."),
        q("Which sentence suggests checking the itinerary before leaving?", "Let's check the itinerary before we leave",
          "Let's to check the itinerary before we leave", "Let's check the iitnerary before we leave", "We left tomorrow",
          "Use Let's check the itinerary to make a suggestion."),
      ])

    _p = "Anna is travelling to Xi'an next Friday. She is staying in a small hotel. Her itinerary includes a temple and a museum."
    R("rw_itin", "Reading an itinerary", 10, 2,
      "Read an itinerary, identify the timing, lodging, and sights, and determine whether the writer only lists plans.", "rw_main", [
        q(_p + " When is Anna going to Xi'an?", "next Friday", "last Friday", "next year", "yesterday", "The passage says next Friday."),
        q(_p + " Where is she staying?", "a small hotel", "in a castle", "a school dormitory", "beside a waterfall", "The passage says she is staying in a small hotel."),
        q(_p + " What does her itinerary include?", "a temple and a museum", "a beach and a glacier", "a farm and a factory", "a station and an airport",
          "The passage says her itinerary includes a temple and a museum."),
        q(_p + " Which best describes the author's attitude?", "She is simply describing an arranged plan",
          "She strongly opposes the trip", "She is criticizing the hotel", "She is asking for help",
          "The passage only lists the timing and plans; it does not express opposition."),
      ])

    R("wr_itin", "Writing an itinerary email", 10, 2,
      "Can choose sentences for an itinerary email based on required points.", "rw_write", [
        q("Key points: leave on Friday, stay in a small hotel, and visit the Terracotta Army. Which sentence includes all three?",
          "We are leaving on Friday, staying in a small hotel and visiting the Terracotta Army",
          "We are leaving on Friday", "The hotel is small", "I like museums",
          "Mention the departure, lodging, and sight."),
        q("Which sentence says that the train ticket has already been booked?", "I have already booked the train ticket",
          "I have already book the train ticket", "I not have already booked the train ticket", "I have arleady booked the train ticket",
          "Use have booked to say that the ticket is already booked."),
        q("Which sentence is suitable as the opening of an itinerary email?", "I am writing to tell you about my trip",
          "I am write to tell you about my trip", "I am writing to telling you about my trip", "I am writing to tells you about my trip",
          "Use I am writing to tell you to explain the purpose of the email."),
        q("Which sentence says that you will go to the museum instead if it rains?", "If it rains, we will go to the museum",
          "If it will rain, we go to the museum", "If it rains, we went tomorrow", "If rains it, we will go",
          "Use rains in the if-clause and will go in the main clause."),
      ])

    V("vo_sport", "Sports", 10, 3,
      "Recognize marathon, stadium, coach, and medal.",
      [("marathon", "long-distance race"), ("stadium", "sports arena"), ("coach", "trainer"), ("medal", "award")], "vo_world")

    V("vo_health", "Fitness and health", 10, 3,
      "Recognize fitness, muscle, diet, and injury.",
      [("fitness", "physical condition"), ("muscle", "body tissue"), ("diet", "everyday food"), ("injury", "physical harm")], "vo_world")

    G("gr_taghs", "Tag questions", 10, 3,
      "Can match a tag question's subject, auxiliary, and positive or negative polarity to its statement.", "tag", [
        q("She can swim, ___? Which tag completes the sentence?", "can't she", "can she", "can't he", "doesn't she",
          "The statement is affirmative with can, so use the negative tag can't she."),
        q("They didn't win, ___? Which tag completes the sentence?", "did they", "didn't they", "do they", "won they",
          "The statement is negative with didn't, so use the affirmative tag did they."),
        q("Which sentence has a correct tag question?", "He is a coach, isn't he",
          "He is a coach, is he", "He is a coach, isn't she", "He is a coach, doesn't he",
          "The negative tag for is is isn't he."),
        q("You have finished the race, ___? Which tag completes the sentence?", "haven't you",
          "have you", "didn't you", "don't you", "Have is the auxiliary, so an affirmative statement takes the negative tag haven't you."),
      ])

    G("gr_advp", "Adverb phrases as adverbials", 10, 3,
      "Can identify adverb phrases and determine which verb they modify.", "phrase", [
        q("She runs very quickly. Which word does very quickly modify?", "runs", "She", "very by itself", "the period",
          "The adverb phrase modifies the verb runs."),
        q("Which is an adverb phrase?", "much more carefully", "a careful coach", "the big stadium", "looks strong",
          "Carefully is an adverb, modified by much more."),
        q("He trains quite hard before the marathon. What function does quite hard serve?", "Adverbial",
          "Subject", "Object", "Modifier", "Quite hard modifies trains, so it functions as an adverbial."),
        q("Which sentence contains a phrase used as an adverbial?", "They played fairly well", "They are fairly good players",
          "A fairly good player arrived", "The fairly big stadium is new",
          "Well modifies played. In the other sentences, fairly modifies an adjective."),
      ])

    F("fu_sport", "Giving exercise advice", 10, 3,
      "Can give advice about exercise and health and respond to someone else's advice.", "fu_plan", [
        q("Your friend rarely exercises. Which sentence suggests walking every day?", "You could walk for thirty minutes a day",
          "You could walked for thirty minutes a day", "You could walk for thirty minutes an day", "You could to walk for thirty minutes a day",
          "Use You could to make a suggestion."),
        q("A coach says, Don't train when you are injured. You understand. What should you reply?", "All right, I will rest",
          "I will train harder tonight", "The muscle is a coach", "Yesterday rest tomorrow",
          "If you are injured, follow the advice and rest."),
        q("Which sentence invites a classmate to run at the stadium with you on Saturday?", "Shall we run at the stadium on Saturday",
          "Shall we run at the stadium in Saturday", "Shall we run at the stadium on Staurday", "We ran tomorrow",
          "Use Shall we to make an invitation."),
        q("Which sentence says that a balanced diet helps your fitness?", "A balanced diet helps your fitness",
          "A balanced diet help your fitness", "A blaanced diet helps your fitness", "A balanecd diet helps your fitness",
          "Helps your fitness describes the effect of diet."),
      ])

    _m = "Li ran a marathon last Sunday and won a medal. His coach says he should rest because of a small injury."
    R("rw_match", "Reading a race report", 10, 3,
      "Read a short race report and identify the result and the coach's advice.", "rw_detail", [
        q(_m + " What event did Li take part in?", "a marathon", "swimming", "a debate", "a lecture", "The passage says he ran a marathon."),
        q(_m + " What did he receive?", "a medal", "a castle", "a brochure", "a locker", "The passage says he won a medal."),
        q(_m + " Why does his coach advise him to rest?", "Because he has a minor injury", "Because he lost", "Because he has class next week", "Because he has no coach",
          "The passage says he has a small injury."),
        q(_m + " Which statement matches the passage?", "Li won a medal", "Li lost the marathon",
          "The coach wants him to train all night", "Li has no injury",
          "He won a medal but sustained a minor injury."),
      ])

    R("wr_match", "Writing a sports brief", 10, 3,
      "Can choose a sentence for a short sports report based on required points.", "rw_write", [
        q("Key points: a marathon last Sunday, a medal, and the coach's advice to rest. Which sentence includes all three?",
          "Li ran a marathon last Sunday, won a medal, and his coach told him to rest",
          "Li ran a marathon", "He won a medal", "The coach likes music",
          "Include the time, result, and advice."),
        q("Which sentence uses the past tense for a completed game?", "Our team won the game yesterday",
          "Our team wins the game yesterday", "Our team will won yesterday", "Won our team yesterday the game",
          "Use the past-tense won with yesterday."),
        q("Which sentence reminds readers to watch for injuries?", "Stop training if you feel an injury",
          "Stop tarining if you feel an injury", "Stop trainnig if you feel an injury", "Stop trining if you feel an injury",
          "If you feel an injury gives a warning."),
        q("Which tag question checks whether the reader has seen the notice?", "You have read the notice, haven't you",
          "You have read the notice, have you", "You have read the notice, didn't he",
          "You read the notice, aren't you",
          "The negative tag for have is haven't you."),
      ])

    V("vo_disaster", "Natural disasters", 10, 4,
      "Recognize earthquake, flood, hurricane, and drought.",
      [("earthquake", "shaking of the ground"), ("flood", "overflow of water"), ("hurricane", "powerful tropical storm"), ("drought", "long period without rain")], "vo_soc")

    V("vo_rescue", "Rescue and safety", 10, 4,
      "Recognize rescue, shelter, survivor, and warning.",
      [("rescue", "saving someone from danger"), ("shelter", "safe place to stay"), ("survivor", "person who remains alive"), ("warning", "notice of possible danger")], "vo_soc")

    G("gr_relpro", "Relative clauses with relative pronouns", 10, 4,
      "Can use who, which, and that to introduce restrictive relative clauses.", "rel", [
        q("The girl ___ is singing is my classmate. Which pronoun completes the sentence?", "who",
          "which", "where", "whom",           "The antecedent is a person serving as the clause's subject, so use who."),
        q("The book ___ I bought is about disasters. Which pronoun completes the sentence?", "that",
          "who", "where", "whom",           "The antecedent is a thing serving as the object, so that is suitable."),
        q("Which sentence is correct?", "I know the doctor who saved the child",
          "I know the doctor which saved the child", "I know the doctor where saved the child",
          "I know the doctor he saved the child",
          "Doctor refers to a person; use who as the subject, not which."),
        q("This is the warning ___ saved many lives. Which pronoun completes the sentence?", "which",
          "who", "whom", "where", "Warning refers to a thing and is the subject, so use which."),
      ])

    G("gr_relwhose", "Whose and whom", 10, 4,
      "Can use whose to show possession and whom as the object of a preposition or verb.", "rel", [
        q("The student ___ mother is a doctor sits here. Which pronoun completes the sentence?", "whose",
          "who", "which", "whom", "The mother belongs to the student, so use whose."),
        q("The man ___ we met is a survivor. The blank is the object of met, and the antecedent is a person. Which pronoun fits?", "whom",
          "whose", "which", "where",           "The antecedent is a person serving as the object in the relative clause, so use whom."),
        q("Which sentence uses whose correctly?", "I helped a boy whose house was flooded",
          "I helped a boy who house was flooded", "I helped a boy which house was flooded",
          "I helped a boy whom house was flooded",
          "The house belongs to the boy, so use whose house."),
        q("The woman to ___ I spoke is a volunteer. Which pronoun completes the sentence?", "whom",
          "whose", "which", "where", "Use whom for a person after the preposition to."),
      ])

    F("fu_rescue", "Describing a disaster and asking for help", 10, 4,
      "Can describe a disaster, express concern, and ask for help.", "fu_view", [
        q("Which sentence tells a classmate that the flood is severe and many people need help?", "The flood is serious and many people need help",
          "The flood are serious and many people need help", "The flood is serious and many peoples need help", "The flood is sreious and many people need help",
          "You can describe the disaster by saying The flood is serious."),
        q("Which sentence politely asks someone to donate blankets?", "Could you please donate some blankets",
          "Could you please donate some balnkets", "Could you please donate some blanktes", "Could you please donate some blnkets",
          "Use Could you please to make a polite request."),
        q("Which sentence expresses concern for the survivors?", "I am worried about the survivors",
          "I is worried about the survivors", "He is worried about the survivors", "I am worried about the sruvivors",
          "Use I am worried about to express concern."),
        q("A classmate says the rescue team has left, and you are relieved. What should you reply?", "I am glad the rescue team has left",
          "I am glad the team never left", "I is glad the rescue team has left", "He is glad the rescue team has left",
          "Use I am glad to express relief."),
      ])

    _n = "A strong earthquake hit the town on Friday. Rescue teams found twenty survivors. The warning had been sent ten minutes earlier."
    R("rw_news", "Reading a disaster report", 10, 4,
      "Read a report about a disaster that has occurred and identify when it happened, the number of people, and the warning.", "rw_detail", [
        q(_n + " On what day did the earthquake happen?", "Friday", "Monday", "Sunday", "No date is given", "The passage says it happened on Friday."),
        q(_n + " How many survivors did the rescue teams find?", "twenty people", "ten people", "two people", "one hundred people", "The passage says they found twenty survivors."),
        q(_n + " When was the warning sent?", "ten minutes before the earthquake", "one day after the earthquake", "It was not sent", "one hour before the earthquake",
          "The passage says the warning had been sent ten minutes earlier."),
        q(_n + " Which statement matches the passage?", "Rescue teams found twenty survivors",
          "The earthquake hit on Monday", "No warning was sent", "The town had no earthquake",
          "Both the number of survivors and the timing must match the passage."),
      ])

    R("wr_news", "Writing a disaster report", 10, 4,
      "Can choose a sentence for a report based on required points and use past tenses appropriately.", "rw_write", [
        q("Key points: an earthquake on Friday, twenty survivors found, and a warning sent ten minutes earlier. Which sentence includes all three?",
          "An earthquake hit on Friday, rescue teams found twenty survivors, and the warning had been sent ten minutes earlier",
          "An earthquake hit on Friday", "Twenty people arrived", "The warning was loud",
          "Include all three points in the same sentence."),
        q("Which sentence uses the right tense to report a completed rescue?", "The team rescued five people yesterday",
          "The team rescues five people yesterday", "The team will rescued yesterday", "Rescued the team yesterday five",
          "Use the past-tense rescued with yesterday."),
        q("Which sentence reminds readers to go to a shelter?", "Please go to the nearest shelter",
          "Please go to the naerest shelter", "Please go to the nearset shelter", "Please go to the nerest shelter",
          "This imperative sentence reminds readers to go to the nearest shelter."),
        q("Which sentence correctly uses a relative clause to describe the station that sent the warning?", "The station that sent the warning is local",
          "The sattion that sent the warning is local", "The station where sent the warning",
          "The station he sent the warning is local",
          "Station is a thing, so use that without repeating the subject in the clause."),
      ])

    V("vo_lang", "Language and writing", 10, 5,
      "Recognize dialect, character, accent, and vocabulary.",
      [("dialect", "regional variety of a language"), ("character", "written symbol"), ("accent", "way of pronouncing a language"), ("vocabulary", "set of words")], "vo_world")

    V("vo_affix", "Prefixes and suffixes", 10, 5,
      "Can use common prefixes and suffixes to infer the meanings of derived words.",
      [("unhappy", "not happy"), ("careful", "cautious"), ("writer", "author"), ("rewrite", "write again")], "vo_form")

    G("gr_reladv", "Relative adverbs in relative clauses", 10, 5,
      "Can use when, where, and why to introduce restrictive relative clauses.", "rel", [
        q("I remember the day ___ we met. Which word completes the sentence?", "when",
          "which", "who", "whose",           "The day refers to a time, so use when."),
        q("The village ___ I grew up is quiet. Which word completes the sentence?", "where",
          "when", "who", "whose",           "The village refers to a place, so use where."),
        q("I know the reason ___ she left. Which word completes the sentence?", "why",
          "where", "who", "whom",           "The reason gives a cause, so use why."),
        q("Which sentence is correct?", "This is the museum where we learned about characters",
          "This is the museum when we learned about characters",
          "This is the museum who we learned about characters",
          "This is the museum why we learned about characters",
          "A museum is a place, so use where."),
      ])

    G("gr_relprep", "Prepositions before relative pronouns", 10, 5,
      "Can place a preposition before a relative pronoun and choose whom or which.", "rel", [
        q("This is the man to ___ I spoke. Which pronoun completes the sentence?", "whom",
          "who", "whose", "where",           "When the preposition to comes first, use whom for a person."),
        q("The article in ___ I found the word is short. Which pronoun completes the sentence?", "which",
          "whom", "who", "where", "Use which for a thing after the preposition in."),
        q("Which sentence is correct?", "The student with whom I practised is kind",
          "The student with who I practised is kind", "The student with whose I practised is kind",
          "The student with where I practised is kind",
          "With comes first, and whom refers to a person."),
        q("The topic about ___ we argued is dialects. Which pronoun completes the sentence?", "which",
          "whom", "who", "when",           "Topic is a subject, so use which after about."),
      ], "inferred")

    F("fu_lang", "Talking about languages", 10, 5,
      "Can share opinions about languages, dialects, and Chinese characters and give reasons.", "fu_view", [
        q("How can you say that Chinese characters are interesting but hard to write?", "Chinese characters are interesting but hard to write",
          "Chinese characters are interest but hard to write", "Chinese characters are interesting but hard to writing", "Chinese characters are interesting but hard to writes",
          "Interesting but hard expresses an opinion and gives a reason."),
        q("How can you ask whether someone can speak their local dialect?", "Can you speak your local dialect",
          "Can you speak your local dailect", "Can you speak your local dialcet", "Can you speak your local dilect",
          "Use Can you speak to ask about someone's ability."),
        q("Someone has a strong accent, and you did not hear them clearly. What is a polite response?", "Could you say that again more slowly",
          "Your accent is terrible, stop", "Could you say that again more solwly", "Could you say that again more slolwy",
          "Use Could you say that again to politely ask someone to repeat something."),
        q("Which sentence says that reading helps expand your vocabulary?", "Reading helps you build your vocabulary",
          "Reading help you build your vocabulary", "Reading helps you build your vcoabulary", "Reading helps you build your vocabulray",
          "Helps you build your vocabulary describes the benefit of reading."),
      ])

    _l = "Mei is learning Chinese characters. She thinks the writing is difficult, but she likes reading short stories. Her vocabulary grows every week."
    R("rw_lang", "Reading about language learning", 10, 5,
      "Read a short passage about language learning and summarize her difficulty and attitude.", "rw_main", [
        q(_l + " What is Mei learning?", "Chinese characters", "French grammar", "a marathon", "rescue", "The passage says she is learning Chinese characters."),
        q(_l + " What does she find difficult?", "writing", "the language lab", "running", "lodging", "The passage says the writing is difficult."),
        q(_l + " How is her vocabulary changing?", "It grows every week", "It has stopped growing", "She has no vocabulary", "It grows only on Fridays",
          "The passage says her vocabulary grows every week."),
        q(_l + " How does she feel about reading?", "She enjoys short stories", "She dislikes all reading", "She is only worried about floods", "She has no opinion",
          "The passage says she likes reading short stories."),
      ])

    P("ph_stresshs", "Stress in multisyllabic words", 10, 5,
      "Can identify which syllable is stressed in a multisyllabic word.", "stress", [
        q("Which syllable is stressed in vocabulary?", "the second syllable", "the first syllable", "the fourth syllable", "all four syllables equally",
          "The stress in vo-CAB-u-la-ry falls on cab."),
        q("Which syllable is stressed in character?", "the first syllable", "the second syllable", "the third syllable", "there is no stress",
          "The stress in CHAR-ac-ter falls on the first syllable."),
        q("Which word is stressed on the second syllable?", "disaster", "dialect", "character", "shelter",
          "The stress in dis-AS-ter falls on the second syllable. Dialect, character, and shelter are stressed on the first syllable."),
        q("Which syllable is stressed in accommodation?", "the third syllable", "the first syllable", "the second syllable", "the fifth syllable",
          "The stress in a-ccom-mo-DA-tion falls on da, the third syllable."),
      ])

    R("wr_lang", "Writing a language-learning plan", 10, 5,
      "Can choose a sentence for a learning plan based on required points.", "rw_write", [
        q("Key points: learn ten Chinese characters a day, read short texts, and review vocabulary on weekends. Which sentence includes all three?",
          "I will learn ten characters a day, read a short text and review vocabulary at the weekend",
          "I will learn ten characters", "I like stories", "The weekend is long",
          "Include all three points."),
        q("Which sentence uses a time clause to say that you will read after finishing your homework?", "I will read after I finish my homework",
          "I will read after I will finish my homework", "I read after I will finish tomorrow",
          "After I will finish, I read yesterday",
          "Use finish in the after-clause and will read in the main clause."),
        q("Which sentence is suitable as the first sentence of a plan?", "My plan for learning Chinese is simple",
          "My plan for learning Chinese are simple", "My plan for laerning Chinese is simple", "My plan for learnnig Chinese is simple",
          "A plan can begin with the summary My plan is simple."),
        q("Which sentence correctly uses a relative clause to introduce a teacher who helps you?", "I thank the teacher who helps me every week",
          "I thank the teacher which helps me every week", "I thank the teacher where helps me",
          "I thank the teacher he helps me every week",
          "Teacher refers to a person, so use who."),
      ])
