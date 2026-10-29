# -*- coding: utf-8 -*-
"""Grade 7, first semester. Commonly used People’s Education Press Go for it! contents; unit titles and volume assignment are unverified."""
from en_tx import V, P, G, F, R

# "上" is the parser-required first-semester metadata value.


def q(prompt, answer, wrongs, expl):
    return ("c", prompt, answer, wrongs, expl)


P("ph_stress", "Word stress", 7, "上", 1,
  "Can identify which syllable of a common word is stressed.", "stress", [
    q("Which syllable is stressed in teacher?", "the first syllable",
      ["the second syllable", "both syllables are equally stressed", "there is no stress"], "The stress in tea-cher falls on tea."),
    q("Which syllable is stressed in about?", "the second syllable",
      ["the first syllable", "both syllables are equally stressed", "there is no stress"], "The stress in a-bout falls on bout."),
    q("Which word is stressed on the second syllable?", "begin",
      ["student", "China", "apple"], "The stress in be-gin falls on gin; the other three words are stressed on the first syllable."),
    q("Which syllable is stressed in computer?", "the second syllable",
      ["the first syllable", "the third syllable", "all three syllables are equally stressed"], "The stress in com-pu-ter falls on pu."),
])

P("ph_tone7", "Rising and falling intonation at sentence ends", 7, "上", 1,
  "Can distinguish falling intonation in statements and wh-questions from rising intonation in yes/no questions.", "tone", [
    q("What intonation is usually used at the end of the yes/no question Are you a student?", "rising intonation",
      ["falling intonation", "fall then rise", "stress on every word"], "Yes/no questions usually end with rising intonation."),
    q("What intonation is usually used at the end of the statement My name is Gina?", "falling intonation",
      ["rising intonation", "rise, then fall, then rise again", "no intonation"], "Statements usually end with falling intonation."),
    q("What intonation is usually used at the end of the wh-question Where is she?", "falling intonation",
      ["rising intonation", "the same rising intonation as yes/no questions", "rise only on where"], "Wh-questions usually end with falling intonation."),
    q("Which sentence usually ends with rising intonation?", "Is he your friend?",
      ["He is my friend.", "Where is your friend?", "She is Gina."],
      "Is he your friend is a yes/no question, so it ends with rising intonation."),
])

V("vo_name", "Names and forms of address", 7, "上", 1,
  "Recognize name, friend, girl, and boy.",
  [("name", "a person's name"), ("friend", "a companion"), ("girl", "a female child"), ("boy", "a male child")], "vocab7")

G("gr_be7", "The verb be: am, is, and are", 7, "上", 1,
  "Can choose am, is, or are to agree with the subject.", "be_have", [
    q("I ___ Gina. Which word completes the sentence?", "am",
      ["is", "are", "be"], "Use am after I."),
    q("She ___ my friend. Which word completes the sentence?", "is",
      ["am", "are", "be"], "Use is after she."),
    q("They ___ students. Which word completes the sentence?", "are",
      ["am", "is", "be"], "Use are after they."),
    q("Which sentence is correct?", "He is a boy.",
      ["He am a boy.", "He are a boy.", "He be a boy."], "Use is with he."),
])

F("fu_intro", "Greetings and self-introductions", 7, "上", 1,
  "Can greet someone and say your name.", "func_school", [
    q("You meet someone for the first time, and they say Nice to meet you. What should you reply?", "Nice to meet you, too.",
      ["Good night.", "See you yesterday.", "Nice to meeting you, too."], "Add too when replying to Nice to meet you."),
    q("Which sentence is suitable for saying that your name is Gina?", "My name is Gina.",
      ["Your name is Gina.", "She name is Gina.", "My name are Gina."], "Use My name is to give your name."),
    q("Which is a greeting to use when you meet someone in the morning?", "Good morning.",
      ["Good mornings.", "Good moning.", "Good monring."], "Use Good morning to greet someone in the morning."),
    q("Someone asks What's your name? Your name is Tom. What should you reply?", "My name is Tom.",
      ["His name is Tom.", "I name Tom.", "You are Tom?"], "Answer a question about your name with My name is."),
])

R("rw_intro", "Reading a self-introduction", 7, "上", 1,
  "Read a self-introduction and identify the person's name and role.", "read_detail", [
    q("Hello. My name is Gina. I am 12. I am a student. What is her name?", "Gina",
      ["Alice", "Tom", "Jack"], "The passage says My name is Gina."),
    q("Hello. My name is Gina. I am 12. I am a student. What does she do?", "a student",
      ["a teacher", "a doctor", "a driver"], "I am a student means that she is a student."),
    q("Hi. I am Jack. I am a boy. My friend is Gina. Who is Jack's friend?", "Gina",
      ["Tom", "Alice", "Mike"], "The passage says My friend is Gina."),
    q("Hi. I am Jack. I am a boy. My friend is Gina. Which statement matches the passage?", "Jack is a boy.",
      ["Jack is a girl.", "Gina is Jack.", "Jack is 12."], "The passage says Jack is a boy, but does not say he is 12."),
])

V("vo_family7", "Family members", 7, "上", 2,
  "Recognize family, parent, sister, and brother.",
  [("family", "a group of related people"), ("parent", "a mother or father"), ("sister", "a female sibling"), ("brother", "a male sibling")], "vocab7")

G("gr_this7", "This is and These are", 7, "上", 2,
  "Can use This is to introduce one person or thing and These are to introduce more than one.", "noun_pron", [
    q("You are introducing an older sister. Which sentence is correct?", "This is my sister.",
      ["These are my sister.", "This are my sister.", "These is my sister."], "Use This is for one person."),
    q("You are introducing two younger brothers. Which sentence is correct?", "These are my brothers.",
      ["This is my brothers.", "These is my brothers.", "This are my brothers."], "Use These are with a plural noun."),
    q("These are my parents. What does this sentence mean?", "These are my parents.",
      ["This is my sister.", "These are my books.", "This is my friend."], "Parents means a mother and father, and these are introduces more than one person or thing."),
    q("That is my brother. Which word refers to one person or thing at a distance?", "That",
      ["These", "Those", "Are"], "That refers to one farther away."),
])

G("gr_plural7", "Plural nouns", 7, "上", 2,
  "Can form plurals of common countable nouns.", "noun_pron", [
    q("What is the plural of book?", "books",
      ["bookes", "book", "bookies"], "Usually add s directly: books."),
    q("What is the plural of box?", "boxes",
      ["boxs", "boxies", "box"], "Add es to a word ending in x: boxes."),
    q("What is the plural of family?", "families",
      ["familys", "familyes", "familis"], "For a consonant followed by y, change y to i and add es."),
    q("Which sentence uses a plural noun correctly?", "I have two sisters.",
      ["I have two sister.", "I have two sisteres.", "I have two sisteries."], "Use the plural sisters after two."),
])

P("ph_s", "Pronunciation of final s", 7, "上", 2,
  "Can distinguish whether final -s or -es is pronounced /s/, /z/, or /ɪz/.", "esound", [
    q("Which word has the same final-s sound as books?", "maps",
      ["pens", "bags", "buses"], "The final s in books and maps is pronounced /s/."),
    q("Which word has the same final-s sound as bags?", "pens",
      ["books", "maps", "buses"], "The final s in bags and pens is pronounced /z/."),
    q("Which word ends with the /ɪz/ sound?", "buses",
      ["books", "bags", "maps"], "The -es in buses is pronounced /ɪz/."),
    q("Which word has the same final sound as boxes?", "watches",
      ["cats", "dogs", "birds"], "The endings of boxes and watches are both pronounced /ɪz/."),
])

F("fu_family7", "Introducing family members", 7, "上", 2,
  "Can introduce your family to someone else.", "func_school", [
    q("Which sentence can introduce your older sister to a classmate?", "This is my sister.",
      ["These are my sister.", "She is my parent?", "I am your sister."], "Use This is to introduce one person."),
    q("Someone asks Who is he? He is your younger brother. What should you reply?", "He is my brother.",
      ["She is my brother.", "He are my brother.", "This are my brother."], "Use he and is for a brother."),
    q("These are my parents. Whom is the speaker introducing?", "their parents",
      ["their classmates", "their teacher", "a friend's book"], "Parents means a mother and father."),
    q("Which sentence can introduce a family in a photo?", "This is my family.",
      ["This is my schoolbag.", "These are my pens.", "This are my family."],       "Family refers to the people in the speaker's family."),
])

R("rw_family7", "Reading a family introduction", 7, "上", 2,
  "Read a family introduction and identify the relationships between people.", "read_detail", [
    q("This is my family. These are my parents. This is my sister, Gina. Who is the speaker's sister?", "Gina",
      ["Tom", "Alice", "Jack"], "This is my sister, Gina tells us that Gina is the sister."),
    q("This is my family. These are my parents. This is my sister, Gina. Which statement matches the passage?", "Gina is the speaker's sister.",
      ["Gina is the speaker's brother.", "The speaker has no parents.", "Gina is a parent."],
      "The passage says This is my sister, Gina."),
    q("I have a brother. His name is Tom. I have no sister. Does the speaker have a sister?", "No",
      ["Yes, one", "Yes, two", "The passage does not say"], "I have no sister means the speaker has no sister."),
    q("I have a brother. His name is Tom. I have no sister. Who is Tom?", "the speaker's brother",
      ["the speaker's sister", "the speaker's parents", "the speaker's teacher"], "His name is Tom refers to the brother."),
])

V("vo_school7", "School supplies", 7, "上", 3,
  "Recognize pencil, eraser, dictionary, and ruler.",
  [("pencil", "writing instrument"), ("eraser", "rubber"), ("dictionary", "reference book"), ("ruler", "measuring tool")], "vocab7")

G("gr_poss7", "Possessive adjectives", 7, "上", 3,
  "Can use my, your, his, and her to modify nouns.", "noun_pron", [
    q("This is her eraser. Which sentence is correct?", "This is her eraser.",
      ["This is she eraser.", "This is hers eraser.", "This is her an eraser."], "Put the noun directly after her."),
    q("___ pencil is blue. The pencil belongs to Tom. Which word completes the sentence?", "His",
      ["He", "Him", "Her"], "Tom is male, so use the possessive adjective His."),
    q("What is the possessive adjective for I?", "my",
      ["me", "mine", "myself"], "I corresponds to my, not myself."),
    q("Which sentence is correct?", "Your dictionary is here.",
      ["You dictionary is here.", "Your is dictionary here.", "Yours dictionary is here."],
      "Your modifies dictionary; the possessive pronoun yours is not followed by a noun."),
])

G("gr_yesno", "Yes/no questions with be", 7, "上", 3,
  "Can turn sentences with be into yes/no questions and give short answers.", "be_have", [
    q("This is her pencil. Which sentence correctly changes it into a yes/no question?", "Is this her pencil?",
      ["Does this is her pencil?", "Is this her pencil.", "Are this her pencil?"],
      "Move be to the beginning; keep is with this."),
    q("Are you Gina? Which is the affirmative short answer?", "Yes, I am.",
      ["Yes, I are.", "Yes, I'm.", "Yes, I is."], "The short answer Yes, I am does not contract am."),
    q("Is he your brother? Which is the negative short answer?", "No, he isn't.",
      ["No, he aren't.", "No, he not.", "No, he doesn't."], "Use isn't with he."),
    q("Which sentence is a yes/no question?", "Are these your rulers?",
      ["These are your rulers.", "Your rulers are these.", "What these are?"],
      "The verb are moves to the beginning in Are these."),
])

F("fu_lost", "Claiming a lost item", 7, "上", 3,
  "Can ask who owns an item and answer yes or no.", "func_school", [
    q("You find a pencil and want to ask whether it belongs to someone. Which sentence is suitable?", "Is this your pencil?",
      ["This is your pencil.", "Are this your pencil?", "What your pencil?"], "Use Is this your pencil to ask."),
    q("Someone asks Is this your eraser? It is yours. What should you reply?", "Yes, it is.",
      ["Yes, it are.", "No, it is mine.", "Yes, I am."], "Use it for an item; answer Yes, it is."),
    q("What can a lost-and-found notice say to tell someone to ask the teacher for help?", "Ask the teacher for it.",
      ["I am the teacher.", "This are a teacher.", "Ask you teacher."], "Ask the teacher for it asks the teacher to help you get the item."),
    q("Which sentence says that this dictionary belongs to him?", "This is his dictionary.",
      ["This is he dictionary.", "This is him dictionary.", "This are his dictionary."], "His modifies dictionary."),
])

R("rw_notice", "Reading a lost-and-found notice", 7, "上", 3,
  "Read a lost-and-found notice and identify the item and contact person.", "read_detail", [
    q("Found: a blue pencil. Is this your pencil? Call Mary at 622-6033. What was found?", "a blue pencil",
      ["an eraser", "a dictionary", "a ruler"], "A blue pencil is the item that was found."),
    q("Found: a blue pencil. Is this your pencil? Call Mary at 622-6033. Who should you call?", "Mary",
      ["Gina", "Tom", "Jack"], "Call Mary means to phone Mary."),
    q("Lost: my dictionary. My name is Tom. Please call 139-0011. Who lost the dictionary?", "Tom",
      ["Mary", "Gina", "Alice"], "My name is Tom; the lost item is my dictionary."),
    q("Lost: my dictionary. My name is Tom. Please call 139-0011. Which statement matches the notice?", "Tom lost a dictionary.",
      ["Tom found a dictionary.", "Mary lost a pencil.", "The dictionary is blue."],
      "Lost: my dictionary means that the dictionary is missing."),
])

V("vo_room7", "Rooms and furniture", 7, "上", 4,
  "Recognize room, bed, table, and chair.",
  [("room", "indoor space"), ("bed", "furniture for sleeping"), ("table", "piece of furniture with a flat top"), ("chair", "seat for one person")], "vocab7")

G("gr_prep7", "Prepositions of place", 7, "上", 4,
  "Can use in, on, and under to describe where things are.", "there_prep", [
    q("The book is on the table. Which sentence is correct?", "The book is on the table.",
      ["The book is under the table.", "The book is in the table.", "The book are on the table."],
      "Use on for something on a surface."),
    q("The bag is under the bed. Which sentence is correct?", "The bag is under the bed.",
      ["The bag is on the bed.", "The bag is under the chair only.", "The bag are under the bed."],
      "Use under for something below another object."),
    q("Where is my schoolbag? What does this question ask?", "Where is my schoolbag?",
      ["What color is my schoolbag?", "Whose schoolbag is it?", "How much is the schoolbag?"], "Where asks about a place."),
    q("The keys are in the schoolbag. Which sentence is correct?", "The keys are in the schoolbag.",
      ["The keys is in the schoolbag.", "The keys are on the in.", "The key are in the schoolbag."],
      "Keys is plural, so use are; in means inside."),
])

F("fu_where7", "Asking where things are", 7, "上", 4,
  "Can ask where things are and describe their locations.", "func_life", [
    q("You cannot find your schoolbag. Which sentence can you use to ask where it is?", "Where is my schoolbag?",
      ["What is my schoolbag?", "Where are my schoolbag?", "Who is my schoolbag?"],
      "Use Where is for a singular item."),
    q("Someone asks where the schoolbag is. It is under the chair. What should you say?", "It is under the chair.",
      ["It are under the chair.", "It is the under chair.", "They is under the chair."],
      "Use It is under for a singular item."),
    q("Someone asks Where are my books? The books are on the table. What should you reply?", "They are on the table.",
      ["It is on the table.", "They is on the table.", "They are in the table."],
      "Use they are for books and on for a surface."),
    q("Which sentence asks someone to look under the bed?", "Look under the bed.",
      ["Look the bed under.", "Look on name.", "See you under."], "Look under the bed directs someone to look below the bed."),
])

R("rw_room7", "Reading a room description", 7, "上", 4,
  "Read a room description and identify where things are.", "read_detail", [
    q("This is my room. The book is on the table. The bag is under the chair. Where is the book?", "On the table",
      ["under the chair", "in the schoolbag", "on the bed"], "The book is on the table."),
    q("This is my room. The book is on the table. The bag is under the chair. Where is the bag?", "Under the chair",
      ["on the table", "on the bed", "in the book"], "The bag is under the chair."),
    q("The keys are in the schoolbag. The schoolbag is on the bed. Where are the keys?", "In the schoolbag",
      ["under the bed", "on the table", "on the chair"], "The keys are in the schoolbag."),
    q("The keys are in the schoolbag. The schoolbag is on the bed. Which statement matches the passage?", "The schoolbag is on the bed.",
      ["The keys are on the bed.", "The schoolbag is under the bed.", "The keys are under the chair."],
      "The schoolbag is on the bed, and the keys are inside it, not directly on the bed."),
])

V("vo_ball", "Ball sports", 7, "上", 5,
  "Recognize basketball, soccer, tennis, and volleyball.",
  [("basketball", "team sport played with a hoop"), ("soccer", "football"), ("tennis", "racket sport"), ("volleyball", "team sport played over a net")], "vocab7")

G("gr_have", "Have and has", 7, "上", 5,
  "Can choose have or has to agree with the subject.", "be_have", [
    q("I ___ a soccer ball. Which word completes the sentence?", "have",
      ["has", "am", "is"], "Use have after I."),
    q("She ___ a tennis ball. Which word completes the sentence?", "has",
      ["have", "are", "haves"], "Use has after she."),
    q("They ___ two basketballs. Which word completes the sentence?", "have",
      ["has", "haves", "is"], "Use have after they."),
    q("Which sentence is correct?", "He has a volleyball.",
      ["He have a volleyball.", "He haves a volleyball.", "He have volleyballs a."], "Use has with he."),
])

G("gr_do", "Do and does", 7, "上", 5,
  "Can use do or does to form simple-present questions and negative sentences.", "present", [
    q("___ you have a soccer ball? Which word completes the sentence?", "Do",
      ["Does", "Are", "Is"], "Use Do with you."),
    q("___ she have a tennis ball? Which word completes the sentence?", "Does",
      ["Do", "Is", "Has"], "Use Does with she; the following verb stays in the base form have."),
    q("He does not have a basketball. Which sentence is correct?", "He doesn't have a basketball.",
      ["He don't have a basketball.", "He doesn't has a basketball.", "He not have a basketball."],
      "Use the base form have after doesn't."),
    q("Do they have a volleyball? Which is the affirmative short answer?", "Yes, they do.",
      ["Yes, they have.", "Yes, they does.", "Yes, they are."], "Answer a question with Do using do."),
])

F("fu_ball", "Talking about sports", 7, "上", 5,
  "Can ask whether someone has a ball and talk about sports.", "func_school", [
    q("How can you ask someone whether they have a soccer ball?", "Do you have a soccer ball?",
      ["Are you have a soccer ball?", "Does you have a soccer ball?", "Do you has a soccer ball?"],
      "Use Do you have with you."),
    q("Someone asks Do you have a basketball? You do. What should you reply?", "Yes, I do.",
      ["Yes, I have.", "Yes, I does.", "Yes, I am."], "The affirmative short answer to Do you is Yes, I do."),
    q("Which sentence says that we play volleyball at school?", "We play volleyball at school.",
      ["We plays volleyball at school.", "We play the volleyballs at school always the.", "Us play volleyball."],
      "Use the base form play after we. Sports are usually used without the."),
    q("What is the speaker doing by saying Let's play soccer?", "suggesting that they play soccer",
      ["asking the price of a soccer ball", "saying they do not have a soccer ball", "introducing an older sister"], "Use Let's to make a suggestion."),
])

R("rw_ball", "Reading about sports", 7, "上", 5,
  "Read a short passage about sports and identify who has each ball.", "read_detail", [
    q("Tom has a basketball. He doesn't have a soccer ball. His sister has a tennis ball. Does Tom have a soccer ball?", "No",
      ["Yes", "Two", "The passage does not say"], "He doesn't have a soccer ball."),
    q("Tom has a basketball. He doesn't have a soccer ball. His sister has a tennis ball. Who has a tennis ball?", "Tom's sister",
      ["Tom", "Tom's father", "Tom's teacher"], "His sister has a tennis ball."),
    q("We have a volleyball. We play it after class. What do they have?", "a volleyball",
      ["a basketball", "a soccer ball", "a tennis ball"], "A volleyball is what they have."),
    q("We have a volleyball. We play it after class. When do they play?", "after class",
      ["before getting up in the morning", "while sleeping at home", "only on weekend nights"], "After class means when class has ended."),
])

V("vo_food7", "Food", 7, "上", 6,
  "Recognize banana, hamburger, salad, and ice-cream.",
  [("banana", "long curved fruit"), ("hamburger", "sandwich with a patty"), ("salad", "dish of mixed ingredients"), ("ice-cream", "frozen dessert")], "vocab7")

G("gr_count", "Countable and uncountable nouns", 7, "上", 6,
  "Can distinguish countable and uncountable nouns and choose a, an, or some.", "noun_pron", [
    q("Banana is countable. Which sentence is correct?", "I like bananas.",
      ["I like a bananaes.", "I like bananaes.", "I like an bananas."], "The plural of a countable noun is bananas."),
    q("Milk is uncountable. Which sentence is correct?", "I like milk.",
      ["I like a milk.", "I like milks.", "I like an milk."], "Uncountable nouns do not take a or an and are not made plural with s."),
    q("You want some salad. Which sentence is correct?", "I want some salad.",
      ["I want a salades.", "I want some salads the count.", "I want an salad."],
      "Salad is uncountable here, so use some salad."),
    q("Which word is uncountable?", "milk",
      ["banana", "hamburger", "apple"], "Milk is uncountable; bananas, hamburgers, and apples are countable."),
])

G("gr_like7", "Sentence patterns with like", 7, "上", 6,
  "Can use affirmative, negative, and question forms of like to talk about preferences.", "present", [
    q("She likes bananas. Which sentence is correct?", "She likes bananas.",
      ["She like bananas.", "She likes banana.", "She like a bananas."], "Add s to the verb after she, and use plural bananas."),
    q("I do not like hamburgers. Which sentence is correct?", "I don't like hamburgers.",
      ["I doesn't like hamburgers.", "I don't likes hamburgers.", "I not like hamburgers."],
      "Use don't for a negative with I, followed by the base form of the verb."),
    q("___ she like salad? Which word completes the question?", "Does",
      ["Do", "Is", "Are"], "Use Does with she and the base form like."),
    q("Do you like ice-cream? Which is the negative answer?", "No, I don't.",
      ["No, I doesn't.", "No, I'm not.", "No, I don't like."], "The negative short answer to Do you is No, I don't."),
])

F("fu_food7", "Talking about food", 7, "上", 6,
  "Can ask about and express preferences for food.", "func_life", [
    q("How can you ask whether someone likes salad?", "Do you like salad?",
      ["Are you like salad?", "Does you like salad?", "Do you likes salad?"], "Use Do you like with you."),
    q("You like bananas. What should you say?", "I like bananas.",
      ["I likes bananas.", "I like bananaes.", "I am like bananas."], "Use I like with the plural of a countable noun."),
    q("Someone says I don't like hamburgers. What does this mean?", "I don't like hamburgers.",
      ["I have hamburgers.", "I am eating hamburgers.", "The hamburgers are on the table."], "Don't like means not to like something."),
    q("How can you suggest having ice-cream together?", "Let's have some ice-cream.",
      ["Let's has some ice-cream.", "Let have an ice-cream the.", "Let's having ice-cream."],
      "Use the base form have after Let's."),
])

R("rw_food7", "Reading about food preferences", 7, "上", 6,
  "Read a short passage about food and identify people's preferences.", "read_detail", [
    q("Gina likes bananas and milk. She doesn't like hamburgers. Does Gina like hamburgers?", "No",
      ["Yes", "Only at school", "The passage does not say"], "She doesn't like hamburgers."),
    q("Gina likes bananas and milk. She doesn't like hamburgers. What does she like to drink?", "milk",
      ["salad", "hamburgers", "tea"], "Likes milk means that she likes milk."),
    q("Tom likes salad. He doesn't like ice-cream. His sister likes ice-cream. Who likes ice-cream?", "Tom's sister",
      ["Tom", "Gina", "Tom's father"], "His sister likes ice-cream."),
    q("Tom likes salad. He doesn't like ice-cream. Which statement matches the passage?", "Tom likes salad.",
      ["Tom likes ice-cream.", "Tom doesn't like salad.", "Tom has no sister in this text and he likes hamburgers."],
      "The first sentence is Tom likes salad. The second part of the distractor about hamburgers is not mentioned."),
])

V("vo_clothes7", "Clothes and colors", 7, "上", 7,
  "Recognize sock, shirt, skirt, and sweater.",
  [("sock", "short garment worn on the foot"), ("shirt", "upper-body garment"), ("skirt", "garment worn from the waist down"), ("sweater", "knitted warm top")], "vocab7")

G("gr_much", "Asking prices with How much", 7, "上", 7,
  "Can use How much to ask about prices and express prices in dollars.", "question", [
    q("How can you ask how much these socks cost?", "How much are these socks?",
      ["How much is these socks?", "How many are these socks?", "How much these socks are?"],
      "Socks is a plural noun, so use are; ask about price with How much."),
    q("The sweater costs 20 dollars. Which sentence is correct?", "The sweater is 20 dollars.",
      ["The sweater are 20 dollars.", "The sweater is 20 dollar.", "The sweater has 20 dollar."],
      "Use plural dollars for a price, and is with the singular sweater."),
    q("How much is this shirt? What does this question ask?", "How much does this shirt cost?",
      ["What color is the shirt?", "Where is the shirt?", "How many shirts do you have?"], "How much asks about a price."),
    q("The skirt costs 15 dollars. Which sentence is correct?", "The skirt is fifteen dollars.",
      ["The skirt are fifteen dollars.", "The skirt is fifteen dollar.", "The skirts is fifteen dollars."],
      "Use is for one skirt and the plural dollars."),
])

F("fu_shop7", "Shopping expressions", 7, "上", 7,
  "Can ask about prices and colors and decide whether to buy something.", "func_life", [
    q("How can you ask the price of a sweater in a shop?", "How much is the sweater?",
      ["How many is the sweater?", "What much is the sweater?", "How much the sweater is?"],
      "Use How much is with a singular item."),
    q("A clerk says It is 8 dollars. You decide to buy it. What should you say?", "I'll take it.",
      ["I take them are.", "I'll taking it.", "I am take it."], "I'll take it means you are buying it."),
    q("How can you ask for a red shirt?", "I want a red shirt.",
      ["I want a red shirts.", "I want red a shirt.", "I wants a red shirt."], "A red shirt means one shirt that is red."),
    q("A clerk says Can I help you? What are they doing?", "asking what help you need",
      ["asking your name", "saying the shirt is expensive", "introducing their family"], "Can I help you is a greeting used in a shop."),
])

R("rw_shop7", "Reading a shopping dialogue", 7, "上", 7,
  "Read a shopping dialogue and identify the price and decision.", "read_detail", [
    q("Woman: How much is this skirt? Clerk: It is 15 dollars. Woman: I'll take it. How much is the skirt?", "15 dollars",
      ["8 dollars", "20 dollars", "50 dollars"], "The clerk says it is 15 dollars."),
    q("Woman: How much is this skirt? Clerk: It is 15 dollars. Woman: I'll take it. Did she buy it?", "Yes, she bought it",
      ["No, she did not", "She only asked about the color", "The clerk would not sell it"], "I'll take it means she is buying it."),
    q("Boy: How much are the socks? Clerk: They are 5 dollars. Boy: They are too dear. I will not take them. Are the socks expensive, according to the boy?", "He thinks they are too expensive",
      ["He thinks they are very cheap", "He buys them right away", "The passage does not mention a price"], "Too dear means too expensive, and he does not buy them."),
    q("Complete the sentence: The sweater is 20 ___. I will take it. Which word completes it?", "dollars",
      ["dollar", "much", "color"], "Use plural dollars after 20."),
])

V("vo_date", "Months and ordinal numbers", 7, "上", 8,
  "Recognize January, February, March, and April.",
  [("January", "the first month of the year"), ("February", "the second month of the year"), ("March", "the third month of the year"), ("April", "the fourth month of the year")], "vocab7")

G("gr_when7", "Asking about dates with when", 7, "上", 8,
  "Can use when to ask about a date and answer with a month and ordinal number.", "question", [
    q("How can you ask what date someone's birthday is?", "When is your birthday?",
      ["When your birthday is?", "What is your birthday?", "When are your birthday?"],
      "When is your birthday asks for a date."),
    q("Your birthday is May 2. Which sentence is correct?", "My birthday is on May 2nd.",
      ["My birthday is on May two.", "My birthday is in May 2nd.", "My birthday are on May 2nd."],
      "Use on with a specific date and use the ordinal 2nd."),
    q("Which is the first month of the year?", "January",
      ["February", "March", "April"], "January is the first month of the year."),
    q("What is the cardinal number for third?", "three",
      ["thirdly", "thirty", "thirteen"], "Third is an ordinal number; its cardinal form is three."),
])

F("fu_bday7", "Talking about birthdays", 7, "上", 8,
  "Can ask and talk about birthdays and ages.", "func_school", [
    q("How can you ask someone when their birthday is?", "When is your birthday?",
      ["Where is your birthday?", "When are your birthday?", "How much is your birthday?"],
      "Use When is your birthday to ask for a date."),
    q("Your birthday is September 5. What should you say?", "It is on September 5th.",
      ["It is in September 5.", "It is on September five.", "It are on September 5th."],
      "Use on with a specific date and an ordinal number."),
    q("How old are you? What does this question ask?", "How old are you?",
      ["When is your birthday?", "What is your name?", "Where are you from?"], "How old asks about age."),
    q("How can you say that Alice is twelve years old?", "Alice is twelve.",
      ["Alice are twelve.", "Alice is twelfth.", "Alice has twelve."], "Use the cardinal number twelve for age, not the ordinal twelfth."),
])

R("rw_cal7", "Reading an event schedule", 7, "上", 8,
  "Read an event schedule and identify the dates and activities.", "read_detail", [
    q("School Day is on September 21st. The basketball game is on October 2nd. When is School Day?", "September 21",
      ["October 2", "September 2", "October 21"], "The passage says School Day is on September 21st."),
    q("School Day is on September 21st. The basketball game is on October 2nd. When is the basketball game?", "October 2",
      ["September 21", "October 21", "November 2"], "October 2nd is the date of the game."),
    q("Alice's birthday party is on May 5th. She is twelve. In which month is the party?", "May",
      ["April", "June", "March"], "May is the month of the party."),
    q("Alice's birthday party is on May 5th. She is twelve. Which statement matches the passage?", "Alice is twelve.",
      ["Alice is five.", "The party is in May 5th without on.", "Alice is twenty."],
      "She is twelve, not five or twenty."),
])

V("vo_subj", "School subjects", 7, "上", 9,
  "Recognize subject, science, history, and geography.",
  [("subject", "area of study"), ("science", "study of the natural world"), ("history", "study of the past"), ("geography", "study of places and the Earth")], "vocab7")

G("gr_because", "Using because to give reasons", 7, "上", 9,
  "Can use because to answer why and explain a reason.", "clause_adv", [
    q("Why do you like science? Which is a suitable answer?", "Because it is interesting.",
      ["Because it are interesting.", "So it is interesting.", "Why it is interesting."],
      "Answer why with because, and use is with it."),
    q("Which sentence is correct?", "I like history because it is fun.",
      ["I like history because it are fun.", "I like history so it is fun.", "Because I like history it is fun."],
      "Because connects a reason, as in it is fun."),
    q("What does the clause Because he likes P.E. do?", "Give a reason",
      ["Ask about a time", "Ask about a price", "Give a command"], "Because is used to give a reason."),
    q("She likes geography because it is useful. Which sentence is correct?", "She likes geography because it is useful.",
      ["She like geography because it is useful.", "She likes geography because it are useful.", "She likes geography so it is useful."],
      "Use likes with she and it is in the because-clause."),
])

F("fu_subj", "Talking about favorite subjects", 7, "上", 9,
  "Can name a favorite subject and explain why you like it.", "func_school", [
    q("How can you ask someone about their favorite subject?", "What's your favorite subject?",
      ["What's your favorite subjects?", "What your favorite subject is?", "How much is your favorite subject?"],
      "What's your favorite subject asks which subject someone likes best."),
    q("Your favorite subject is science. What should you say?", "My favorite subject is science.",
      ["My favorite subject are science.", "I favorite science.", "Science is my favorite subject are."],
      "Subject is singular, so use is."),
    q("How can you ask someone why they like history?", "Why do you like history?",
      ["Why does you like history?", "Why do you likes history?", "Because do you like history?"],
      "Use Why do you like with you."),
    q("You have geography on Friday afternoon. How can you tell a classmate?", "We have geography on Friday afternoon.",
      ["We has geography on Friday afternoon.", "We have geography in Friday afternoon.", "We have geography on Friday the afternoon is."],
      "Use on Friday afternoon for a weekday afternoon, and use have with we."),
])

R("rw_subj", "Reading a course description", 7, "上", 9,
  "Read a course description and identify the favorite subject and the reason.", "read_detail", [
    q("My favorite subject is science. I have it on Monday. I like it because it is interesting. What is the favorite subject?", "science",
      ["history", "geography", "P.E."], "The favorite subject is science."),
    q("My favorite subject is science. I have it on Monday. I like it because it is interesting. Why does the speaker like it?", "Because it is interesting",
      ["Because it is difficult", "Because it is Friday", "Because the teacher is strict; the passage gives no other reason"], "The passage says because it is interesting."),
    q("Jack's favorite subject is history. He thinks it is useful. He doesn't like geography. Does Jack like geography?", "No",
      ["Yes", "Only on Mondays", "The passage does not say"], "He doesn't like geography."),
    q("Jack's favorite subject is history. He thinks it is useful. Which statement matches the passage?", "Jack likes history.",
      ["Jack likes geography.", "Jack's favorite subject is science.", "History is not useful for Jack."],
      "His favorite subject is history, and he thinks it is useful."),
])
