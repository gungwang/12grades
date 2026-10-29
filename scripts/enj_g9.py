# -*- coding: utf-8 -*-
"""Full Grade 9 volume. Unit titles follow the common People's Education Press Go for it! outline; volume placement is pending verification."""
from en_tx import V, P, G, F, R

# "全" is the full-year semester token required by enj_build.py's Grade 9 validation and unit lookup.

def q(prompt, answer, wrongs, expl):
    return ("c", prompt, answer, wrongs, expl)


V("vo_learn", "Learning Strategies", 9, "全", 1,
  "Recognize pronunciation, expression, repeat, and patient.",
  [("pronunciation", "the way a word is spoken"), ("expression", "way of expressing an idea"), ("repeat", "say or do again"), ("patient", "able to wait calmly")], "vocab9")

G("gr_by", "Gerunds after by", 9, "全", 1,
  "Use by + a verb in the -ing form to explain how something is done.", "to_ing", [
    q("I learn English by reading the text. Which sentence is correct?", "I study English by reading the text.",
      ["I study English by read the text.", "I study English by to read the text.", "I study English with reading the text for by."],
      "Use reading after by."),
    q("She improves her pronunciation by listening to tapes. Which sentence is correct?", "She improves her pronunciation by listening to tapes.",
      ["She improves her pronunciation by listen to tapes.", "She improves her pronunciation by to listen to tapes.", "She improves her pronunciation by listened to tapes."],
      "Use by listening."),
    q("What does by doing express?", "A method",
      ["A past time", "An object of comparison", "A person who must perform a passive action"],
      "By + a gerund explains the method used."),
    q("You can practice by working in a group. Which sentence is correct?", "You can practice by working in a group.",
      ["You can practice by work in a group.", "You can practice by to work in a group.", "You can practice by worked in a group."],
      "Use by working."),
])

F("fu_learn", "Discussing Learning Strategies", 9, "全", 1,
  "Ask how someone studies and describe your own methods.", "func_school", [
    q("You want to ask how someone studies English. Which question is appropriate?", "How do you study English?",
      ["How do you studies English?", "How are you study English?", "How you study English?"],
      "Use How do you study?"),
    q("You learn by taking notes. How should you say this?", "I learn by taking notes.",
      ["I learn by take notes.", "I learn by to take notes.", "I learn with taking notes."],
      "Use by taking notes."),
    q("What is the speaker doing with “What about reading aloud?”", "Suggesting reading aloud",
      ["Asking how much a book costs", "Describing yesterday's test score", "Refusing to study"],
      "What about + a gerund introduces a suggestion."),
    q("You want to say that the teacher is patient. Which sentence is appropriate?", "The teacher is patient.",
      ["The teacher is patiently.", "The teacher are patient.", "The teacher is a patient to the book."],
      "Use is patient."),
])

R("rw_learn", "Reading about Study Strategies", 9, "全", 1,
  "Read study advice and identify the methods and results.", "read_detail", [
    q("Wei Fen studies English by reading aloud. She also learns new words by making word cards. How does she study English?", "By reading aloud",
      ["Only by watching TV", "She never reads", "Only by sleeping before a test"], "The passage says she reads aloud."),
    q("Wei Fen studies English by reading aloud. She also learns new words by making word cards. How does she learn new words?", "By making word cards",
      ["By throwing books away", "By asking only once", "By not reviewing"], "The passage says she makes word cards."),
    q("Paul was not patient before. Now he studies by listening to tapes every night. What does he do every night now?", "Listen to tapes",
      ["Write novels", "Go to a museum", "Avoid studying"], "The passage says he listens to tapes every night."),
    q("Paul was not patient before. Now he studies by listening to tapes. Which sentence agrees with the advice?", "Paul now learns by listening to tapes.",
      ["Paul still refuses to study.", "Wei Fen learns words only by sleeping.", "Paul has never listened to tapes."],
      "His current method is listening to tapes."),
])

V("vo_fest", "Festival Foods", 9, "全", 2,
  "Recognize mooncake, lantern, stranger, and relative.",
  [("mooncake", "traditional cake eaten at the Mid-Autumn Festival"), ("lantern", "portable light with a protective case"), ("stranger", "person one does not know"), ("relative", "member of one's family")], "vocab9")

G("gr_that", "Object Clauses with that", 9, "全", 2,
  "Use that to connect an opinion to a following statement; that may be omitted.", "clause_obj", [
    q("I think mooncakes are delicious. Which sentence is correct?", "I think that mooncakes are delicious.",
      ["I think that mooncakes is delicious.", "I think mooncakes are delicious that.", "I think that are mooncakes delicious."],
      "Use statement word order after that; mooncakes takes are."),
    q("She believes the story is true. Which sentence is correct?", "She believes that the story is true.",
      ["She believes that is the story true.", "She believes that the story true.", "She believes that the story are true."],
      "Use the statement clause the story is true."),
    q("What word order does an object clause introduced by that use?", "Statement word order",
      ["Question word order", "Imperative word order", "Inverted word order such as Are they"],
      "In the clause, the subject comes before the verb."),
    q("In which sentence can that be omitted without changing the meaning?", "I know that he likes lanterns.",
      ["I know that does he like lanterns.", "I know he likes lanterns that the end.", "That he likes lanterns I know are."],
      "That can be omitted from I know he likes lanterns."),
])

G("gr_ifwhether", "Object Clauses with if and whether", 9, "全", 2,
  "Use if or whether to introduce an object clause, with statement word order in the clause.", "clause_obj", [
    q("I don't know whether he will come. Which sentence is correct?", "I don't know if he will come.",
      ["I don't know if will he come.", "I don't know if he comes will.", "I don't know if does he come."],
      "In if he will come, the subject he comes before will."),
    q("She is asking whether to bring a lantern. Which sentence is correct?", "She asks whether she should bring a lantern.",
      ["She asks whether should she bring a lantern.", "She asks whether does she bring a lantern.", "She asks whether she should brings a lantern."],
      "Use whether she should bring."),
    q("What does if mean in an object clause?", "Whether",
      ["If, meaning “in the event that”", "Although", "So that"],
      "In an object clause, if means whether."),
    q("Which sentence has the correct word order?", "I wonder whether the story is true.",
      ["I wonder whether is the story true.", "I wonder whether does the story true.", "I wonder whether the story true is it."],
      "Use statement word order in whether the story is true."),
])

F("fu_fest", "Talking about Festivals", 9, "全", 2,
  "Talk about what people eat and do during festivals.", "func_life", [
    q("You want to say that people admire the moon during the Mid-Autumn Festival. Which sentence is suitable?", "People admire the moon on Mid-Autumn Festival.",
      ["People admires the moon on Mid-Autumn Festival.", "People admire the moon in Mid-Autumn Festival.", "People admire moon the on festival."],
      "Use on Mid-Autumn Festival and the base verb admire."),
    q("You want to ask whether someone likes mooncakes. Which question is suitable?", "Do you like mooncakes?",
      ["Do you like mooncake are?", "Are you like mooncakes?", "Do you likes mooncakes?"],
      "Use Do you like."),
    q("What does “I wonder if they will have a party” mean?", "I want to know whether they will have a party",
      ["I know they had a party yesterday", "If they have a party, it will certainly be canceled", "I do not care about the party"],
      "Wonder if means wanting to know whether something will happen."),
    q("You want to say that relatives gather together. Which sentence is suitable?", "The relatives get together.",
      ["The relatives gets together.", "The relative get together as a plural verb error.", "The relatives are get together."],
      "Use get with the plural subject relatives."),
])

R("rw_fest", "Reading about the Mid-Autumn Festival", 9, "全", 2,
  "Read a festival passage and identify its food and activities.", "read_detail", [
    q("Li Mei thinks that mooncakes are delicious. Her family admires the moon at night. What does she think of mooncakes?", "She thinks they are delicious",
      ["She thinks they taste bad", "She thinks they are too salty", "The passage does not say"], "The passage says the mooncakes are delicious."),
    q("Li Mei thinks that mooncakes are delicious. Her family admires the moon at night. What does her family do at night?", "Admire the moon",
      ["Race dragon boats", "Clean the house", "Go to a hospital"], "The passage says they admire the moon."),
    q("I don't know whether Tom will come. He is in another city. Is it certain that Tom will come?", "No, it is uncertain",
      ["Yes, he will definitely come", "He has already arrived", "The passage says he dislikes lanterns and will not come"],
      "The speaker says they do not know whether Tom will come."),
    q("Her family admires the moon at night. Which sentence agrees with the passage?", "The family watches the moon at night.",
      ["The family eats breakfast at night only.", "Tom has already arrived.", "Li Mei hates mooncakes."],
      "The passage says her family admires the moon at night."),
])

V("vo_polite", "Public Places", 9, "全", 3,
  "Recognize restroom, stamp, postcard, and politely.",
  [("restroom", "room with a toilet"), ("stamp", "small label used to mail a letter"), ("postcard", "card sent by mail without an envelope"), ("politely", "in a respectful manner")], "vocab9")

G("gr_whobj", "Object Clauses with Question Words", 9, "全", 3,
  "Change wh-questions to statement word order when using them in object clauses.", "clause_obj", [
    q("Could you tell me the location of the restroom? Which sentence is correct?", "Could you tell me where the restroom is?",
      ["Could you tell me where is the restroom?", "Could you tell me where the restroom is it?", "Could you tell me where does the restroom?"],
      "In where the restroom is, the verb comes after the subject."),
    q("I want to know the location of the bank. Which sentence is correct?", "I want to know where the bank is.",
      ["I want to know where is the bank.", "I want to know where the bank is there.", "I want to know the bank where is."],
      "Use the statement word order where the bank is."),
    q("She asks me when we are leaving. Which sentence is correct?", "She asks me when we leave.",
      ["She asks me when do we leave.", "She asks me when we do leave tomorrow the question order.", "She asks me when leave we."],
      "Use when we leave, not do we."),
    q("Why does an object clause not use question word order?", "It is part of a statement, not a direct question",
      ["Because where cannot be used", "Because the subject must be omitted", "Because only the past tense is allowed"],
      "After the clause is embedded, the subject still comes before the verb."),
])

F("fu_polite", "Asking for Directions Politely", 9, "全", 3,
  "Ask for directions politely and understand direct and indirect questions.", "func_view", [
    q("You want to ask politely where the post office is. Which sentence is suitable?", "Could you please tell me where the post office is?",
      ["Could you please tell me where is the post office?", "Tell me where is the post office now.", "Could you please tell me where the post office?"],
      "Use a polite request and statement word order in the embedded question."),
    q("Which direct question is correct?", "Where is the restroom?",
      ["Where the restroom is?", "Where is restroom the?", "Where the restroom is it?"],
      "In a direct question, is can come after where."),
    q("You need to buy one stamp. Which sentence is suitable?", "I need one stamp.",
      ["I need one stamps.", "I need a stamps.", "I need an stamp."],
      "Use the singular noun stamp after one."),
    q("What is the speaker's tone in “Excuse me, I wonder if you can help me”?", "Polite",
      ["An angry command", "The conversation has ended", "A description of a past mistake"],
      "Excuse me and wonder if are both polite, indirect expressions."),
])

R("rw_polite", "Reading a Directions Dialogue", 9, "全", 3,
  "Read a dialogue asking for directions and identify the locations.", "read_detail", [
    q("A: Could you tell me where the restroom is? B: Go along the hall and turn left. Where does the visitor want to go?", "The restroom",
      ["The post office", "The bank", "The museum"], "The embedded question asks where the restroom is."),
    q("A: Could you tell me where the restroom is? B: Go along the hall and turn left. How should the visitor get there?", "Walk along the hall, then turn left",
      ["Turn right and go upstairs", "Go back", "Take the elevator to the third floor"], "The directions are to go along the hall and turn left."),
    q("Mary asks where she can buy a stamp. The clerk says the shop is next to the library. Where can she buy a stamp?", "At the shop next to the library",
      ["In the restroom", "There is no shop upstairs at the post office", "At home"], "The shop is next to the library."),
    q("The clerk says the shop is next to the library. Which sentence agrees with the dialogue?", "The stamp shop is beside the library.",
      ["The restroom is next to the library in this second text.", "Mary already has a stamp.", "The clerk tells her to turn right for the restroom."],
      "The dialogue says that the shop is beside the library."),
])

V("vo_change9", "Changes over Time", 9, "全", 4,
  "Recognize humorous, silent, score, and background.",
  [("humorous", "funny or amusing"), ("silent", "not speaking or making a sound"), ("score", "number of points earned"), ("background", "a person's past or circumstances")], "vocab9")

G("gr_used", "used to for Past Habits", 9, "全", 4,
  "Use used to + a base verb for past habits or states that are no longer true.", "past", [
    q("I was afraid of the dark in the past. Which sentence is correct?", "I used to be afraid of the dark.",
      ["I used to was afraid of the dark.", "I use to be afraid of the dark.", "I used to being afraid of the dark."],
      "Use used to be."),
    q("She was silent in the past. Which sentence is correct?", "She used to be silent.",
      ["She used to silent.", "She used to is silent.", "She use to be silent."],
      "Use used to be silent."),
    q("What does used to express?", "A past habit or state that has usually changed",
      ["An action happening now", "Something certain to happen in the future", "Something that has never happened"],
      "Used to contrasts the past with the present."),
    q("Did you play the piano in the past? Which question is correct?", "Did you use to play the piano?",
      ["Did you used to play the piano?", "Did you use to played the piano?", "Use you to play the piano?"],
      "Use Did you use to in a question."),
])

F("fu_used", "Comparing the Past and Present", 9, "全", 4,
  "Describe what you or someone else was like in the past and what is different now.", "func_view", [
    q("You want to say that you were afraid of the dark but are not anymore. Which sentence is suitable?", "I used to be afraid of the dark, but I am not now.",
      ["I used to be afraid of the dark, but I am not now yesterday.", "I use to be afraid of the dark, but now I am not.", "I used to afraid of the dark, but I am not now."],
      "Use used to be to describe the past and but I am not now for the present."),
    q("He is more humorous now. Which sentence is suitable?", "He is more humorous than he used to be.",
      ["He is more humorous than he used to was.", "He is humorouser than he used to be.", "He is more humorouser than he use to be."],
      "Use than he used to be."),
    q("What does “What did you use to do after school?” ask?", "What you often did after school in the past",
      ["What you are doing now", "What you will do after school tomorrow", "What your score is"],
      "Did you use to do asks about a past habit."),
    q("You want to say that your score is higher than before. Which sentence is suitable?", "My score is higher than it used to be.",
      ["My score is higher than it used to was.", "My score is more high than it used to be.", "My score is highest than it used to be."],
      "Use higher than it used to be."),
])

R("rw_used", "Reading about Changes", 9, "全", 4,
  "Read about changes and compare the past with the present.", "read_detail", [
    q("Andy used to be silent. Now he is humorous and talks a lot. What was he like before?", "Very quiet",
      ["Very funny", "Very noisy", "He had a high score"], "He used to be silent."),
    q("Andy used to be silent. Now he is humorous and talks a lot. What is he like now?", "Funny and talkative",
      ["Still completely silent", "Afraid to speak", "The passage does not say"], "The passage says he is humorous now."),
    q("Tina used to hate tests. Her score is higher now. How has her score changed?", "It is higher than before",
      ["It is lower than before", "It has not changed", "The passage does not mention her score"], "Her score is higher now."),
    q("Tina used to hate tests. Which sentence agrees with the passage?", "Tina did not like tests before.",
      ["Tina still hates talking and is silent.", "Andy used to be humorous.", "Tina's score is lower now."],
      "The passage says Tina used to hate tests."),
])

V("vo_material", "Materials", 9, "全", 5,
  "Recognize cotton, steel, produce, and widely.",
  [("cotton", "soft fiber from a plant"), ("steel", "strong metal made mostly of iron"), ("produce", "make or manufacture"), ("widely", "by many people or in many places")], "vocab9")

G("gr_pass", "Simple Present Passive", 9, "全", 5,
  "Use am, is, or are + past participle to describe a present passive action or state.", "passive", [
    q("This shirt is made of cotton. Which sentence is correct?", "This shirt is made of cotton.",
      ["This shirt is made from cotton as a visible cloth error.", "This shirt is make of cotton.", "This shirt made of cotton."],
      "Use is made of cotton. Use of when the material remains recognizable."),
    q("Tea is grown in many places in China. Which sentence is correct?", "Tea is grown in many places in China.",
      ["Tea is grow in many places in China.", "Tea grows by people in many places as a passive form.", "Tea is grown by in China."],
      "Use is grown in the present passive."),
    q("Which form is used for the simple present passive?", "am, is, or are + past participle",
      ["do + base verb", "have + verb-ing", "will + past tense"],
      "Use the present form of be + a past participle."),
    q("Are these bags made of steel? Which question is correct?", "Are these bags made of steel?",
      ["Do these bags made of steel?", "Are these bags make of steel?", "Are these bags made from steel if the steel is still clearly steel?"],
      "Use Are ... made of?"),
])

F("fu_made", "Asking What Something Is Made Of", 9, "全", 5,
  "Ask about an object's material and where it is produced.", "func_life", [
    q("You want to ask what a shirt is made of. Which question is suitable?", "What is the shirt made of?",
      ["What is the shirt made from of?", "What does the shirt made of?", "What is the shirt make of?"],
      "Use What is ... made of?"),
    q("It is produced in China. How should you say this?", "It is produced in China.",
      ["It is produce in China.", "It produced in China.", "It is produced by China people the word order."],
      "Use is produced in China."),
    q("What does “Where is tea grown?” ask?", "Where tea is grown",
      ["Who likes drinking tea", "How much tea costs", "What color tea is"],
      "Where is ... grown asks about a place of production."),
    q("You want to say that this material is widely used. Which sentence is suitable?", "This material is widely used.",
      ["This material is widely use.", "This material widely is used.", "This material is wide used."],
      "Use is widely used."),
])

R("rw_made", "Reading a Product Description", 9, "全", 5,
  "Read a product description and identify its materials and place of production.", "read_detail", [
    q("The shirt is made of cotton. It is produced in China. What is the shirt made of?", "Cotton",
      ["Steel", "Glass", "Paper"], "The passage says it is made of cotton."),
    q("The shirt is made of cotton. It is produced in China. Where is it produced?", "China",
      ["France", "Japan", "The passage does not say"], "The passage says it is produced in China."),
    q("These forks are made of steel. They are used widely in restaurants. What are the forks made of?", "Steel",
      ["Cotton", "Wood", "Gold other than silver"], "The passage says they are made of steel."),
    q("These forks are made of steel. Which sentence agrees with the description?", "The forks are steel products.",
      ["The forks are made of cotton.", "The shirt is made of steel.", "Tea is grown in the shirt factory."],
      "The passage says the forks are made of steel."),
])

V("vo_invent", "Inventions", 9, "全", 6,
  "Recognize inventor, mention, website, and daily.",
  [("inventor", "person who creates something new"), ("mention", "refer to briefly"), ("website", "set of pages on the internet"), ("daily", "happening or used every day")], "vocab9")

G("gr_passpast", "Simple Past Passive", 9, "全", 6,
  "Use was or were + past participle to describe a past passive action.", "passive", [
    q("The telephone was invented by Bell. Which sentence is correct?", "The telephone was invented by Bell.",
      ["The telephone was invent by Bell.", "The telephone is invented by Bell in the past sentence.", "The telephone invented by Bell."],
      "Use was invented by."),
    q("When were these inventions mentioned? Which question is correct?", "When were the inventions mentioned?",
      ["When did the inventions mentioned?", "When were the inventions mention?", "When was the inventions mentioned?"],
      "Use were mentioned with the plural subject inventions."),
    q("Which form is used for the simple past passive?", "was or were + past participle",
      ["is + verb-ing", "have + past participle", "did + past participle"],
      "Use the past form of be + a past participle."),
    q("The website was created last year. Which sentence is correct?", "The website was set up last year.",
      ["The website was set up next year.", "The website set up last year by nobody the active error.", "The website was set up last year by it."],
      "Use was set up last year."),
])

F("fu_invent", "Asking about Inventions", 9, "全", 6,
  "Ask when or by whom something was invented.", "func_view", [
    q("You want to ask when the zipper was invented. Which question is suitable?", "When was the zipper invented?",
      ["When was the zipper invent?", "When did the zipper invented?", "When was the zipper invented by time?"],
      "Use When was ... invented?"),
    q("It was invented by chance. How should you say this?", "It was invented by accident.",
      ["It was invented by an accident person only.", "It invented by accident.", "It was invent by accident."],
      "Use was invented by accident."),
    q("What does “Who was it invented by?” ask?", "Who invented it",
      ["How much it costs now", "What color it is", "Whether it will break tomorrow"],
      "Who ... by asks about the inventor."),
    q("You want to say that people use it every day. Which sentence is suitable?", "People use it in daily life.",
      ["People uses it in daily life.", "People use it in daily life yesterday the tense.", "People are use it in daily life."],
      "Use use it in daily life."),
])

R("rw_invent", "Reading about Inventions", 9, "全", 6,
  "Read about inventions and identify the inventors and uses.", "read_detail", [
    q("The telephone was invented by Bell. It is used for talking to people far away. Who invented the telephone?", "Bell",
      ["Edison", "A student", "The passage does not say"], "The passage says it was invented by Bell."),
    q("The telephone was invented by Bell. It is used for talking to people far away. What is the telephone used for?", "Talking to people far away",
      ["Boiling tea", "Printing books", "Moving mountains"], "The passage says it is used for talking to people far away."),
    q("Potato chips were invented by accident. A cook made them in a restaurant. How were they invented?", "By accident",
      ["After ten years of planned research", "By voting on a website", "The passage does not say"], "The passage says they were invented by accident."),
    q("Potato chips were invented by accident. Which sentence agrees with the description?", "Potato chips were an accidental invention.",
      ["Bell invented potato chips.", "The telephone was invented by a cook.", "Potato chips were invented on purpose in this text."],
      "By accident means that the invention was unplanned."),
])

V("vo_teen", "Rules for Teenagers", 9, "全", 7,
  "Recognize license, safety, society, and choice.",
  [("license", "official permission to do something"), ("safety", "freedom from danger"), ("society", "people living together in a community"), ("choice", "act of choosing")], "vocab9")

G("gr_allow", "be allowed to", 9, "全", 7,
  "Use be allowed to to say that someone has permission to do something.", "passive", [
    q("Teenagers should have permission to choose their own clothes. Which sentence is correct?", "Teenagers should be allowed to choose their own clothes.",
      ["Teenagers should be allowed choose their own clothes.", "Teenagers should be allowed to choosing their own clothes.", "Teenagers should allowed to choose their own clothes."],
      "Use be allowed to choose."),
    q("I do not have permission to stay up late. Which sentence is correct?", "I am not allowed to stay up late.",
      ["I am not allowed stay up late.", "I am not allowed to staying up late.", "I not allowed to stay up late."],
      "Use am not allowed to stay."),
    q("What does be allowed to mean?", "To have permission",
      ["To have to refuse", "A past habit", "To be giving someone permission now"],
      "Allowed is passive; to is followed by an action."),
    q("Are sixteen-year-old students allowed to drive? Which question is correct?", "Are sixteen-year-olds allowed to drive?",
      ["Do sixteen-year-olds allowed to drive?", "Are sixteen-year-olds allowed drive?", "Are sixteen-year-olds allow to drive?"],
      "Use Are ... allowed to drive?"),
])

F("fu_allow", "Discussing Permissions", 9, "全", 7,
  "Express agreement or disagreement with school rules and other permissions.", "func_view", [
    q("You disagree with sixteen-year-olds driving. Which sentence is suitable?", "I don't think sixteen-year-olds should be allowed to drive.",
      ["I don't think sixteen-year-olds should be allowed drive.", "I am not think they should be allowed to drive.", "I don't think they should allowed to drive."],
      "Use don't think ... should be allowed to drive."),
    q("You want to say that safety matters. Which sentence is suitable?", "Safety is important.",
      ["Safety are important.", "Safety is importance.", "The safety is important than."],
      "Use Safety is important."),
    q("You want to say that this is their own choice. Which sentence is suitable?", "It is their own choice.",
      ["It is their own choices one.", "It are their own choice.", "It is they own choice."],
      "Use their own choice."),
    q("What does “I agree with the rule” mean?", "I support the rule",
      ["The rule does not exist", "I have not read the rule yet", "I want to cancel every rule"],
      "Agree with means to support or accept something."),
])

R("rw_allow", "Reading about Rules and Permissions", 9, "全", 7,
  "Read a discussion and identify who is allowed to do what.", "read_detail", [
    q("Students are not allowed to use phones in class. They are allowed to use them after school. May students use phones in class?", "No",
      ["Yes", "Only to listen to music", "The passage does not say"], "The passage says phones are not allowed in class."),
    q("Students are not allowed to use phones in class. They are allowed to use them after school. What about after school?", "Yes, they may use them",
      ["No", "They may look but not touch", "They must hand them in"], "The passage says they are allowed to use them after school."),
    q("Anna thinks sixteen-year-olds should be allowed to choose their clothes. Her father disagrees. Who disagrees?", "Her father",
      ["Anna", "The teacher, who has agreed that they can drive", "Both of them agree"], "The passage says her father disagrees."),
    q("Her father disagrees. Which sentence agrees with the passage?", "Anna and her father do not have the same opinion.",
      ["Both of them disagree with choice.", "Students may use phones in class.", "Anna's father agrees with her."],
      "Her father disagrees with Anna."),
])

V("vo_owner", "Ownership", 9, "全", 8,
  "Recognize whose, attend, valuable, and picnic.",
  [("whose", "belonging to which person"), ("attend", "be present at"), ("valuable", "worth a lot of money or importance"), ("picnic", "meal eaten outdoors")], "vocab9")

G("gr_mustbe", "must for Deduction", 9, "全", 8,
  "Use must for a strong positive deduction and can't for a strong negative deduction.", "modal", [
    q("The guitar has Carla's name on it, so it must be hers. Which sentence is correct?", "The guitar must be Carla's.",
      ["The guitar must is Carla's.", "The guitar must be Carla.", "The guitar can be Carla's as a weak guess in this sure case."],
      "Use must be when the evidence supports a strong deduction."),
    q("He cannot be at the picnic; I saw him at the library. Which sentence is correct?", "He can't be at the picnic.",
      ["He must be at the picnic although I see him in the library.", "He can't is at the picnic.", "He must not to be at the picnic."],
      "Use can't be when there is evidence against the claim."),
    q("What does must express here?", "A strong deduction",
      ["A completed past obligation", "A polite request", "An ongoing passive action"],
      "Must be expresses a strong belief that something is true."),
    q("This valuable book has Tom's name on it. Who does it belong to?", "It must belong to Tom.",
      ["It must belongs to Tom.", "It must belong Tom.", "It can't belong to Tom because the name is Tom."],
      "Use must belong to."),
])

F("fu_guess", "Guessing Who Owns Something", 9, "全", 8,
  "Use clues to infer who owns an object.", "func_view", [
    q("You want to ask who owns this backpack. Which question is suitable?", "Whose backpack is this?",
      ["Who's backpack is this owner?", "Whose backpack this is?", "Who backpack is this?"],
      "Use Whose backpack is this?"),
    q("You are certain it belongs to Mary. What should you say?", "It must be Mary's.",
      ["It must Mary's.", "It can be Mary's if we are completely sure.", "It must is Mary's."],
      "Use must be Mary's."),
    q("The CD has pop music on it, and Mary likes pop music. Which sentence is suitable?", "It must belong to Mary.",
      ["It must belong Mary.", "It must belongs to Mary.", "It can't belong to Mary because she likes pop."],
      "Use must belong to Mary."),
    q("You want to say that he is at a picnic and therefore is not here. Which sentence is suitable?", "He must be attending the picnic.",
      ["He must attending the picnic.", "He must be attend the picnic.", "He can be attending the picnic as a certain fact."],
      "Use must be attending."),
])

R("rw_guess", "Reading about Deductions", 9, "全", 8,
  "Read a short passage and infer who owns each object.", "read_detail", [
    q("The notebook has Anna's name on it. It must be hers. Who owns the notebook?", "Anna",
      ["Tom", "The teacher", "No one; it is unclaimed"], "It has Anna's name on it, so it must be hers."),
    q("The toy truck can't be Mary's. She does not like trucks. Does Mary own the toy truck?", "No",
      ["Definitely", "Possibly, because she likes it", "The passage does not say"], "The passage says it can't be Mary's."),
    q("Somebody is attending a picnic. The volleyball must belong to that person. Who is the volleyball associated with?", "The person attending the picnic",
      ["Anna, who owns the notebook", "Mary, who owns the truck", "The library"], "The volleyball must belong to the person attending the picnic."),
    q("The notebook has Anna's name on it. Which sentence agrees with the passage?", "Anna owns the notebook.",
      ["Mary owns the toy truck.", "The volleyball is Anna's notebook.", "The notebook has no name."],
      "Anna's name is on the notebook."),
])

V("vo_music", "Music Genres", 9, "全", 9,
  "Recognize prefer, lyrics, Australian, and electronic.",
  [("prefer", "like one thing more than another"), ("lyrics", "words of a song"), ("Australian", "relating to Australia"), ("electronic", "using electronic instruments or technology")], "vocab9")

G("gr_attr", "Relative Clauses", 9, "全", 9,
  "Use that, who, or which to modify a person or thing mentioned earlier.", "clause_attr", [
    q("I like music that I can dance to. Which sentence is correct?", "I like music that I can dance to.",
      ["I like music who I can dance to.", "I like music that I can dance to it.", "I like music which I can dance."],
      "Music is a thing, so use that; keep to in dance to."),
    q("The person speaking now is my teacher. Which sentence is correct?", "The man who is talking is my teacher.",
      ["The man which is talking is my teacher.", "The man who talking is my teacher.", "The man who is talking he is my teacher."],
      "Use who for a person and do not repeat he in the relative clause."),
    q("This is the book I bought yesterday. Which sentence is correct?", "This is the book which I bought yesterday.",
      ["This is the book who I bought yesterday.", "This is the book which I bought it yesterday.", "This is the book which I buy yesterday."],
      "Use which for a thing, use the past tense bought, and do not repeat it."),
    q("Which relative pronoun is most suitable for a person?", "who",
      ["what", "how", "whosever"],
      "Who refers to a person."),
])

F("fu_music", "Talking about Music Preferences", 9, "全", 9,
  "Say what music you like and explain why.", "func_life", [
    q("You want to say that you prefer songs with clear lyrics. Which sentence is suitable?", "I prefer songs that have clear lyrics.",
      ["I prefer songs who have clear lyrics.", "I prefer songs that they have clear lyrics.", "I prefer songs which has clear lyrics."],
      "Use songs that have."),
    q("You want to ask what kind of music someone likes. Which question is suitable?", "What kind of music do you like?",
      ["What kind of music do you like it?", "What kind of music you like?", "What kind of music are you like?"],
      "Use What kind of music do you like?"),
    q("You like music that you can sing along with. Which sentence is suitable?", "I like music that I can sing along with.",
      ["I like music that I can sing along.", "I like music who I can sing along with.", "I like music that can I sing along with."],
      "Use sing along with."),
    q("What does “He likes Australian singers” mean?", "He likes singers from Australia",
      ["He is Australian, so he does not sing", "He does not like singers", "He likes only electronic products"],
      "Australian singers are singers from Australia."),
])

R("rw_music", "Reading about Music Preferences", 9, "全", 9,
  "Read about music preferences and identify who likes which kind of music.", "read_detail", [
    q("Cindy likes music that she can dance to. She prefers songs with clear lyrics. What kind of music does she like?", "Music she can dance to with clear lyrics",
      ["Music with no lyrics", "Classical music that can only be heard quietly, not danced to", "The passage does not say"], "The passage mentions music she can dance to and songs with clear lyrics."),
    q("Tony likes singers who write their own songs. He does not like electronic music. What kind of singers does he like?", "Singers who write their own songs",
      ["People who only play electronic music", "People who do not write songs", "The passage does not say"], "The passage says he likes singers who write their own songs."),
    q("Tony does not like electronic music. Does he like electronic music?", "No",
      ["Yes", "Only at parties", "He likes it more than Cindy does"], "The passage says he does not like it."),
    q("Cindy likes music that she can dance to. Which sentence agrees with the passage?", "Cindy likes dance music.",
      ["Tony likes electronic music.", "Cindy hates clear lyrics.", "Tony likes singers who never write songs."],
      "The passage says Cindy likes music she can dance to."),
])

V("vo_custom", "Social Customs", 9, "全", 10,
  "Recognize bow, kiss, greet, and manner.",
  [("bow", "bend forward as a greeting"), ("kiss", "touch with the lips as a greeting"), ("greet", "say hello to someone"), ("manner", "way of behaving")], "vocab9")

G("gr_supposed", "be supposed to", 9, "全", 10,
  "Use be supposed to for actions expected by a custom or rule.", "modal", [
    q("You should shake hands. Which sentence is correct?", "You are supposed to shake hands.",
      ["You are supposed shake hands.", "You are supposed to shaking hands.", "You supposed to shake hands."],
      "Use are supposed to shake."),
    q("You should not speak loudly there. Which sentence is correct?", "You are not supposed to talk loudly there.",
      ["You are not supposed talk loudly there.", "You are not supposed to talking loudly there.", "You not supposed to talk loudly there."],
      "Use are not supposed to talk."),
    q("What does be supposed to mean?", "Should or be expected to",
      ["Used to", "Already allowed to leave", "Bowing right now"],
      "It describes what is expected by a rule or custom."),
    q("Are they expected to bow when they meet for the first time? Which question is correct?", "Are they supposed to bow when they meet for the first time?",
      ["Do they supposed to bow when they meet for the first time?", "Are they supposed bow when they meet?", "Are they suppose to bow when they meet?"],
      "Use Are they supposed to bow?"),
])

F("fu_custom", "Explaining What People Should Do", 9, "全", 10,
  "Explain how people are expected to greet each other in a place.", "func_view", [
    q("Friends often shake hands when they meet in China. Which sentence is suitable?", "In China, people are supposed to shake hands.",
      ["In China, people are supposed shake hands.", "In China, people supposed to shake hands.", "In China, people are supposed to shaking hands."],
      "Use are supposed to shake hands."),
    q("You want to ask how people are expected to greet each other in Japan. Which question is suitable?", "How are people supposed to greet in Japan?",
      ["How do people supposed to greet in Japan?", "How are people supposed greet in Japan?", "How people are supposed to greet in Japan?"],
      "Use How are people supposed to greet...?"),
    q("You want to say that being late is impolite. Which sentence is suitable?", "It is impolite to be late.",
      ["It is impolite be late.", "It is impolite to being late.", "It is impolite to late."],
      "Use impolite to be late."),
    q("What does “We kissed when we met” mean?", "We kissed when we met",
      ["We refused to greet each other", "We are learning the word for bowing", "We did not meet"],
      "The sentence says that they kissed when they met."),
])

R("rw_custom", "Reading about Customs", 9, "全", 10,
  "Read a customs notice and identify what people should and should not do.", "read_detail", [
    q("In this country, you are supposed to bow when you meet someone. You are not supposed to kiss. What should you do when you meet someone?", "Bow",
      ["Kiss", "The passage says nothing about bowing or handshakes", "Do nothing"], "The passage says people are supposed to bow."),
    q("In this country, you are supposed to bow when you meet someone. You are not supposed to kiss. Should you kiss?", "No",
      ["Yes", "Only kiss strangers", "The passage does not say"], "The passage says people are not supposed to kiss."),
    q("Being on time is important. It is impolite to be late for a meeting. What is it like to be late for a meeting?", "Impolite",
      ["Encouraged", "It does not matter", "A kind of greeting"], "The passage says it is impolite to be late."),
    q("You are supposed to bow. Which sentence agrees with the notice?", "Bowing is the expected greeting.",
      ["Kissing is required.", "Being late is polite.", "People should not bow."],
      "The notice says people are expected to bow."),
])

V("vo_emotion", "Emotional Responses", 9, "全", 11,
  "Recognize friendship, king, pale, and queen.",
  [("friendship", "relationship between friends"), ("king", "male ruler of a country"), ("pale", "having a light or unhealthy-looking color"), ("queen", "female ruler or wife of a king")], "vocab9")

G("gr_make", "make + Object + Base Verb or Adjective", 9, "全", 11,
  "Use make + somebody + base verb or make + somebody + adjective.", "to_ing", [
    q("Sad movies make me cry. Which sentence is correct?", "Sad movies make me cry.",
      ["Sad movies make me to cry.", "Sad movies make me crying.", "Sad movies make me cried."],
      "Use the base form cry after make me."),
    q("The news made him happy. Which sentence is correct?", "The news made him happy.",
      ["The news made him happily.", "The news made him to happy.", "The news made he happy."],
      "Use the adjective happy after made him."),
    q("Which form of do follows make somebody do?", "The base form of the verb",
      ["to + verb", "verb-ing", "Past tense"],
      "The verb after make does not take to."),
    q("The king's decision made the queen look pale. Which sentence is correct?", "The king's decision made the queen pale.",
      ["The king's decision made the queen to pale.", "The king's decision made the queen palely.", "The king's decision made the queen pales."],
      "Use made the queen pale."),
])

F("fu_feel9", "Expressing Reactions to Movies", 9, "全", 11,
  "Describe how a movie makes you feel.", "func_view", [
    q("You want to say that this movie makes you want to cry. Which sentence is suitable?", "The movie makes me want to cry.",
      ["The movie makes me to want to cry.", "The movie makes me wanting to cry.", "The movie makes me want cry."],
      "Use makes me want to cry."),
    q("You want to ask someone's opinion of the movie. Which question is suitable?", "What do you think of the movie?",
      ["What do you think the movie of?", "How do you think of the movie is?", "What are you think of the movie?"],
      "Use What do you think of...?"),
    q("You want to say that friendship makes her happy. Which sentence is suitable?", "Friendship makes her happy.",
      ["Friendship makes her happily.", "Friendship make her happy.", "Friendship makes she happy."],
      "Use makes her happy."),
    q("What does “The king looks pale” mean?", "The king looks pale",
      ["The king is very happy", "The queen is laughing", "The movie has not started"],
      "Looks pale describes the king's appearance."),
])

R("rw_movie", "Reading a Movie Review", 9, "全", 11,
  "Read a review and identify the feelings the movie caused.", "read_detail", [
    q("The sad movie made Amy cry. It also made her think about friendship. What did the movie make Amy do?", "Cry and think about friendship",
      ["Fall asleep", "Leave the theater without crying", "Start laughing nonstop"], "The passage says it made Amy cry and think about friendship."),
    q("The sad movie made Amy cry. Why did she cry?", "Because the movie was sad",
      ["Because of a joke", "Because the king invited her to dinner", "The passage does not give a reason"], "The passage says the sad movie made Amy cry."),
    q("The story of the king and the queen made Ben sleepy. He did not cry. Did Ben cry?", "No",
      ["Yes", "He cried with Amy", "The passage does not say"], "The passage says he did not cry."),
    q("The story made Ben sleepy. Which sentence agrees with the review?", "Ben felt sleepy because of the story.",
      ["Ben cried a lot.", "Amy did not think about friendship.", "The queen made Amy sleepy in the first text."],
      "The passage says the story made Ben sleepy."),
])

V("vo_unexp", "Unexpected Events", 9, "全", 12,
  "Recognize unexpected, backpack, block, and burn.",
  [("unexpected", "not expected"), ("backpack", "bag carried on one's back"), ("block", "part of a city between streets"), ("burn", "be damaged by fire")], "vocab9")

G("gr_ppast", "Past Perfect", 9, "全", 12,
  "Use had + past participle for an event completed before another past event.", "pastperf", [
    q("The train left before I arrived. Which sentence is correct?", "The train had left when I arrived.",
      ["The train has left when I arrived.", "The train had left when I arrive.", "The train left when I had arrived as the earlier event."],
      "Use had left for the earlier event and arrived for the later one."),
    q("My brother left before I got up. Which sentence is correct?", "By the time I got up, my brother had left.",
      ["By the time I got up, my brother has left.", "By the time I got up, my brother had leave.", "By the time I get up, my brother had left."],
      "Had left describes an event before got up."),
    q("What is the form of the past perfect?", "had + past participle",
      ["have + verb-ing", "was + verb-ing", "would + base verb"],
      "The form is had done."),
    q("She found that her backpack had burned before she returned. Which sentence is correct?", "She found that her backpack had burned.",
      ["She found that her backpack has burned.", "She found that her backpack had burn.", "She had found that her backpack burned first after she found it."],
      "Burned happened before found, so use had burned."),
])

F("fu_unexp", "Describing an Unexpected Event", 9, "全", 12,
  "Describe an unexpected event in chronological order.", "func_view", [
    q("You want to explain that you were late because your alarm did not ring. Which sentence is suitable?", "I was late because my alarm had not gone off.",
      ["I was late because my alarm has not gone off.", "I was late because my alarm had not went off.", "I was late because my alarm did not had gone off."],
      "Had not gone off happened before being late."),
    q("You want to say that it was completely unexpected. Which sentence is suitable?", "It was totally unexpected.",
      ["It was totally unexpectedness.", "It were totally unexpected.", "It was total unexpected."],
      "Use was totally unexpected."),
    q("By the time I reached the airport, the plane had taken off. When did the plane take off?", "Before I reached the airport",
      ["After I arrived", "At the same time", "The next day"],
      "Had taken off happened before reached."),
    q("You want to say that you had left your backpack at home. Which sentence is suitable?", "I had left my backpack at home.",
      ["I have left my backpack at home before I noticed yesterday.", "I had leave my backpack at home.", "I left my backpack at home after I found it missing first."],
      "Had left means it happened before you noticed the backpack was missing."),
])

R("rw_unexp", "Reading about Unexpected Events", 9, "全", 12,
  "Read about unexpected events and identify which happened first.", "read_detail", [
    q("By the time Carl woke up, the bus had already left. He had forgotten to set the alarm. Which events happened earlier?", "He forgot to set the alarm, and the bus had already left",
      ["He woke up first, and then the bus left", "The bus was still waiting for him", "The alarm rang first"], "He had forgotten and the bus had already left before he woke up."),
    q("By the time Carl woke up, the bus had already left. Was the bus still there when he woke up?", "No, it had already left",
      ["It was still outside", "It had not arrived yet", "The passage does not say"], "The passage says the bus had already left."),
    q("When Nina got home, she found the kitchen had burned. The fire was unexpected. What did she discover when she got home?", "The kitchen had already burned",
      ["The kitchen was being built", "The fire had not started", "The backpack was burning, but the kitchen was fine"], "The passage says the kitchen had burned."),
    q("The fire was unexpected. Which sentence agrees with the story?", "Nina did not expect the fire.",
      ["Carl caught the bus.", "The kitchen burned after Nina arrived.", "Carl had set the alarm."],
      "Unexpected means Nina did not expect it."),
])

V("vo_earth", "Environmental Protection", 9, "全", 13,
  "Recognize litter, bottom, coal, and plastic.",
  [("litter", "trash left in a public place"), ("bottom", "lowest part"), ("coal", "black fossil fuel burned for energy"), ("plastic", "lightweight material made from polymers")], "vocab9")

G("gr_review", "Choosing the Correct Tense", 9, "全", 13,
  "Choose among the present, past, future, continuous, and perfect tenses based on time expressions.", "tense", [
    q("I usually walk to school. Which sentence is correct?", "I usually walk to school.",
      ["I usually walked to school every present day.", "I am usually walk to school.", "I have walk to school every day."],
      "Usually describes a habit, so use the simple present walk."),
    q("I walked to school yesterday. Which sentence is correct?", "I walked to school yesterday.",
      ["I walk to school yesterday.", "I have walked to school yesterday.", "I was walk to school yesterday."],
      "Use walked with yesterday."),
    q("I am walking to school now. Which sentence is correct?", "I am walking to school now.",
      ["I walk to school now as a finished past action.", "I have walked to school now in this ongoing sentence.", "I am walk to school now."],
      "The action is happening now, so use am walking."),
    q("They had planted one thousand trees by the end of last month. Which sentence is correct?", "They had planted one thousand trees by the end of last month.",
      ["They have planted one thousand trees by the end of last month.", "They planted one thousand trees by the end of next month.", "They had plant one thousand trees by the end of last month."],
      "By the end of last month is a past deadline, so use had planted."),
])

F("fu_earth", "Talking about Environmental Actions", 9, "全", 13,
  "Describe actions people can take to protect the environment.", "func_view", [
    q("You want to say that people should not litter. Which sentence is suitable?", "We should not throw litter on the ground.",
      ["We should not to throw litter on the ground.", "We should not throwing litter on the ground.", "We not should throw litter on the ground."],
      "Use should not throw."),
    q("You want to say that plastic harms the ocean. Which sentence is suitable?", "Plastic is bad for the ocean.",
      ["Plastic are bad for the ocean.", "Plastic is badly for the ocean.", "Plastic is bad to the ocean bottom word."],
      "Use is bad for."),
    q("You want to say that people can use less coal. Which sentence is suitable?", "We can use less coal.",
      ["We can use less coals as a countable pile.", "We can to use less coal.", "We can using less coal."],
      "Use can use less coal."),
    q("The river was clean before. Now there is litter at the bottom. What is being contrasted?", "It was clean before, but now there is litter at the bottom",
      ["The river has always been clean", "All the litter has been removed", "Coal has turned into plastic"],
      "The contrast is between was clean and now there is litter."),
])

R("rw_earth", "Reading an Environmental Appeal", 9, "全", 13,
  "Read an appeal and identify the problem and suggested actions.", "read_detail", [
    q("Last year the river was clean. Now people throw plastic into it. What do people throw into the river now?", "Plastic",
      ["A boat made of coal", "Trees", "The passage does not say"], "The passage says people throw plastic into the river."),
    q("Last year the river was clean. Now people throw plastic into it. What was the river like last year?", "Clean",
      ["Full of litter", "Dry", "The passage does not say"], "The passage says it was clean."),
    q("We should pick up litter and use less plastic. What does the appeal ask people to do?", "Pick up litter and use less plastic",
      ["Burn more coal", "Leave litter at the bottom", "Close all rivers"], "The appeal asks people to pick up litter and use less plastic."),
    q("We should pick up litter. Which sentence agrees with the appeal?", "People are asked to collect litter.",
      ["People should throw more plastic.", "The river was dirty last year.", "Coal is the only topic."],
      "The appeal asks people to pick up litter."),
])

R("rw_cloze9", "Cloze Exercise", 9, "全", 13,
  "Complete a passage with words that fit the context.", "read_cloze", [
    q("The city ___ dirty ten years ago. People have planted trees since then. Which word completes the sentence?", "was",
      ["is", "were", "has"], "Use was with ten years ago; city is singular."),
    q("We ___ not supposed to throw plastic into the river. Which word completes the sentence?", "are",
      ["is", "be", "were yesterday now"], "Use are supposed with we."),
    q("By the time the students arrived, the volunteers ___ already cleaned the park. Which word completes the sentence?", "had",
      ["have", "has", "did"], "The cleaning happened before the students arrived, so use had cleaned."),
    q("Music that we can dance ___ makes the trip fun. Which word completes the sentence?", "to",
      ["who", "for to", "which it"], "The phrase is dance to music; keep to after the relative clause."),
])

V("vo_memory", "Graduation Memories", 9, "全", 14,
  "Recognize survey, standard, graduate, and ceremony.",
  [("survey", "set of questions used to collect information"), ("standard", "level of quality or achievement"), ("graduate", "complete a course of study"), ("ceremony", "formal event held for a special occasion")], "vocab9")

G("gr_ger", "Gerunds and Infinitives", 9, "全", 14,
  "Distinguish verbs followed by to + a base verb from those followed by an -ing form.", "to_ing", [
    q("I remember seeing all of you. Which sentence is correct?", "I remember meeting all of you.",
      ["I remember to meeting all of you.", "I remember meet all of you.", "I remember meeting to all of you."],
      "Remember meeting means to recall something that already happened."),
    q("Remember to lock the door. This is an action that has not happened yet. Which sentence is correct?", "Remember to lock the door.",
      ["Remember locking the door for a future action.", "Remember to locking the door.", "Remember lock the door."],
      "Remember to lock means to remember that you need to do it."),
    q("She enjoys singing. Which sentence is correct?", "She enjoys singing.",
      ["She enjoys to sing.", "She enjoys sing.", "She enjoys to singing."],
      "Use an -ing form after enjoy."),
    q("He decided to leave. Which sentence is correct?", "He decided to leave.",
      ["He decided leaving.", "He decided leave.", "He decided to leaving."],
      "Use an infinitive after decide."),
])

G("gr_tag", "Tag Questions", 9, "全", 14,
  "Add a short question with the opposite polarity after a statement.", "sentence", [
    q("She is a student, isn't she? Which sentence is correct?", "She is a student, isn't she?",
      ["She is a student, isn't he?", "She is a student, is she?", "She is a student, doesn't she?"],
      "The statement has affirmative is, so the tag is negative: isn't she."),
    q("You like apples, don't you? Which sentence is correct?", "You like apples, don't you?",
      ["You like apples, aren't you?", "You like apples, do you?", "You like apples, doesn't you?"],
      "Like is a main verb, so use don't you."),
    q("He didn't come yesterday, did he? Which sentence is correct?", "He didn't come yesterday, did he?",
      ["He didn't come yesterday, didn't he?", "He didn't come yesterday, was he?", "He didn't come yesterday, does he?"],
      "The statement is negative, so the tag is affirmative: did he."),
    q("What is the usual polarity of the tag question?", "Opposite to the statement",
      ["It must repeat the whole sentence", "It can use only a noun as the subject", "It cannot use be"],
      "A positive statement usually takes a negative tag, and a negative statement takes a positive tag."),
])

F("fu_memory", "Remembering School Life", 9, "全", 14,
  "Reflect on school life at graduation.", "func_school", [
    q("You want to say that you remember meeting someone for the first time. Which sentence is suitable?", "I remember meeting you on the first day.",
      ["I remember to meet you on the first day already done.", "I remember meet you on the first day.", "I remember meeting you tomorrow."],
      "Use remember meeting for something that already happened."),
    q("The ceremony is on Friday. You want to confirm the date with a classmate. Which sentence is suitable?", "The ceremony is on Friday, isn't it?",
      ["The ceremony is on Friday, isn't he?", "The ceremony is on Friday, is it?", "The ceremony is on Friday, doesn't it?"],
      "Use isn't it as the tag."),
    q("You want to say that you will graduate next year. Which sentence is suitable?", "We will graduate next year.",
      ["We will graduate last year.", "We graduated next year.", "We are graduate next year."],
      "Use will graduate with next year."),
    q("You want to say that the survey has already been completed. Which sentence is suitable?", "We have already done the survey.",
      ["We have yet done the survey.", "We did already the survey tomorrow.", "We have already do the survey."],
      "Use have already done."),
])

R("rw_write", "Writing Key Points", 9, "全", 14,
  "Choose a sentence that covers all key points and uses consistent pronouns and tense.", "write_point", [
    q("Key points: you went to the park last weekend, flew a kite with classmates, and the weather was sunny. Which sentence covers all the points?",
      "Last weekend I went to the park with my classmates and flew a kite. It was sunny.",
      ["Next weekend I will go to the park alone.",
       "Last weekend I went to the park. It was rainy, and I did not fly a kite.",
       "I go to the park every weekend and fly a kite."],
      "Include the past time, classmates, kite flying, and sunny weather."),
    q("Key points: use the present perfect to say you have studied at this school for three years and still like English. Which sentence fits?",
      "I have studied at this school for three years, and I still like English.",
      ["I studied at this school for three years, but I have left it.",
       "I have studied at this school since three years, and I liked English only before.",
       "I study at this school tomorrow for three years."],
      "Use have studied for three years and still like."),
    q("Key points: advise a friend to throw away less plastic and mention that there is already litter at the bottom of the river. Which sentence fits?",
      "You should throw less plastic because there is already litter at the bottom of the river.",
      ["You should throw more plastic into the river.",
       "There was no litter, so do nothing.",
       "I threw plastic yesterday and I will not give advice."],
      "Include the advice to use less plastic and the litter already at the bottom of the river."),
    q("Key points: the graduation ceremony is on Friday, and you remember first meeting the teacher. Confirm the date with a correct tag question. Which sentence fits?",
      "I remember meeting the teacher, and the ceremony is on Friday, isn't it?",
      ["I remember to meet the teacher next Friday, is it?",
       "The ceremony was on Friday, wasn't he?",
       "I remember meeting the teacher, but I do not know any date."],
      "Use meeting for something remembered from the past and isn't it to confirm the Friday date."),
])
