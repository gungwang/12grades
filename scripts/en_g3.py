# -*- coding: utf-8 -*-
"""Grade 3, first and second semesters. Common unit order for the PEP English series starting in Grade 3; volume assignments need verification."""
from en_tx import V, S, P, G, F, R

# The semester values are schema tokens for the first and second semesters; keep them unchanged.
# ---------- Grade 3, first semester ----------

P("ph_alpha", "English Alphabet", 3, "上", 1,
  "Recognize and read the 26 letters of the English alphabet in order.", "letters", [
    ("n", "How many letters are in the English alphabet?", 26, "The English alphabet runs from A to Z and has 26 letters."),
    ("c", "Which letter comes immediately after D in the alphabet?", "the letter E",
     ["the letter C", "the letter F", "the letter B"], "The letter after D is E."),
    ("c", "Which sequence is in alphabetical order?", "A, B, C, D",
     ["A, C, B, D", "B, A, D, C", "D, C, B, A"], "The alphabet begins A, B, C, D."),
    ("c", "Which is the last letter of the alphabet?", "the letter Z",
     ["the letter Y", "the letter X", "the letter A"], "The last letter of the alphabet is Z."),
])

P("ph_case", "Uppercase and Lowercase Letters", 3, "上", 1,
  "Match the uppercase and lowercase forms of the same letter.", "letters", [
    ("c", "Which pair shows the uppercase and lowercase forms of the same letter?", "Gg",
     ["Dp", "Bt", "Qm"], "The uppercase form is G and the lowercase form is g, so the pair is Gg."),
    ("c", "Which is a lowercase letter?", "the lowercase letter h",
     ["the capital letter H", "the capital letter B", "the capital letter M"],
     "h is lowercase; H, B, and M are uppercase."),
    ("n", "How many uppercase letters are in the English alphabet?", 26, "The uppercase letters run from A to Z and total 26."),
    ("c", "Which form of the letter begins the word bag?", "the lowercase letter b",
     ["the capital letter B", "the lowercase letter d", "the capital letter D"],
     "bag begins with a lowercase b."),
])

P("ph_vowel", "Vowel Letters", 3, "上", 1,
  "Identify the vowel letters a, e, i, o, and u.", "vowel_letter", [
    ("c", "Which is a vowel letter?", "the letter A",
     ["the letter B", "the letter C", "the letter D"], "A is a vowel; B, C, and D are not."),
    ("n", "How many vowel letters are there in English?", 5, "The vowel letters are a, e, i, o, and u: 5 in total."),
    ("c", "Which is not a vowel letter?", "the letter T",
     ["the letter A", "the letter E", "the letter U"], "T is a consonant."),
    ("c", "Which group contains only vowel letters?", "A, E, I, O, U",
     ["A, E, I, O, B", "B, C, D, F, G", "A, B, C, D, E"], "The five vowel letters are A, E, I, O, and U."),
])

S("ph_cons", "Initial Sound of Consonant b", 3, "上", 1,
  "Match consonant b with the beginning sound in words such as bag, bed, bus, and box.",
  "Initial sound of the letter b", ["bag", "bed", "bus", "box"], ["cat", "dog", "pen", "sun"],
  "consonant", mode="start")

V("vo_greet", "Greetings", 3, "上", 1,
  "Recognize hello, hi, goodbye, and thanks.",
  [("hello", "hello (a greeting)"), ("hi", "hi (a greeting)"), ("goodbye", "goodbye (a farewell)"), ("thanks", "thanks (an expression of gratitude)")])

G("gr_am", "The Verb am", 3, "上", 1,
  "Use am with I to introduce your name or age.", "be", [
    ("c", "I ____ ten. Which word belongs in the blank?", "am",
     ["is", "are", "be"], "I takes am, so the sentence is I am ten."),
    ("c", "You ____ a student. Which word belongs in the blank?", "are",
     ["am", "is", "be"], "You takes are."),
    ("c", "Which sentence is correct?", "I am Amy.",
     ["I are Amy.", "I be Amy.", "Am I Amy name."], "Introduce yourself by saying I am Amy."),
    ("c", "My name ____ Chen Jie. Which word belongs in the blank?", "is",
     ["am", "are", "be"], "Name takes is."),
])

F("fu_greet", "Greetings, Farewells, and Thanks", 3, "上", 1,
  "Use Hello, Goodbye, and Thank you to greet, say farewell, and express thanks.", "func_greet", [
    ("c", "What should you say when you meet your teacher?", "Hello!",
     ["Goodbye!", "Thank you!", "I am ten."], "Say Hello when you meet someone."),
    ("c", "What should you say when you are leaving?", "Goodbye!",
     ["Hello!", "Thank you!", "I am Amy."], "Say Goodbye when leaving."),
    ("c", "What should you say when someone helps you?", "Thank you!",
     ["Hello!", "Goodbye!", "I am five."], "Say Thank you to express gratitude."),
    ("c", "What should you say to tell someone your name?", "I am Mike.",
     ["Goodbye, Mike.", "Thank you, Mike.", "Hello is Mike."], "Introduce your name by saying I am Mike."),
])

R("rw_hello", "Understanding Introductions", 3, "上", 1,
  "Read a self-introduction and identify the person's name.", "read_short", [
    ("c", "Read: Hello! I am Sarah. What is the person's name?", "Sarah",
     ["Mike", "Amy", "John"], "The sentence says I am Sarah."),
    ("c", "Read: Hi! I am John. Which sentence has the same meaning?", "His name is John.",
     ["His name is Sarah.", "He is saying goodbye.", "He is saying thanks."], "The passage says I am John."),
    ("c", "Read: Goodbye, Amy! What is Amy doing?", "Saying goodbye",
     ["Greeting someone", "Saying thanks", "Introducing her age"], "Goodbye is a farewell."),
    ("c", "Read: I am Chen Jie. Thank you! Which sentence appears in the passage?", "I am Chen Jie.",
     ["I am Sarah.", "I am Mike.", "I am John."], "The name in the passage is Chen Jie."),
])

V("vo_colour", "Colors", 3, "上", 2,
  "Recognize red, yellow, green, and blue.",
  [("red", "the color red"), ("yellow", "the color yellow"), ("green", "the color green"), ("blue", "the color blue")])

G("gr_itis", "Using It Is to Describe Color", 3, "上", 2,
  "Use It is with a color word to describe an object's color.", "be", [
    ("c", "It ____ red. Which word belongs in the blank?", "is",
     ["am", "are", "be"], "It takes is."),
    ("c", "Which sentence is correct?", "It is blue.",
     ["It are blue.", "It am blue.", "It be blue."], "Use It is blue to describe the color."),
    ("c", "The apple ____ green. Which word belongs in the blank?", "is",
     ["am", "are", "be"], "Apple is singular, so it takes is."),
    ("c", "Which sentence says that an object is yellow?", "It is yellow.",
     ["I yellow.", "Yellow it.", "It yellow is."], "The complete sentence is It is yellow."),
])

F("fu_colour", "Asking About Color", 3, "上", 2,
  "Ask What colour is it? to find out an object's color, and answer with It is.", "func_daily", [
    ("c", "How do you ask \"What color is it?\"?", "What colour is it?",
     ["What is your name?", "How are you?", "Goodbye!"], "Ask about color with What colour is it?"),
    ("c", "What colour is it? If it is red, how should you answer?", "It is red.",
     ["It is blue.", "I am red.", "It are red."], "Red is the color word; the sentence is It is red."),
    ("c", "What does Show me green mean?", "Show me something green",
     ["Show me something red", "Show me something yellow", "Show me something blue"], "Green is the color green."),
    ("c", "It is blue and yellow. How many colors are named?", "Blue and yellow",
     ["Red and green", "Blue only", "Yellow only"], "The sentence names blue and yellow."),
])

R("rw_colour", "Reading About Colors", 3, "上", 2,
  "Choose the statement that matches the written color description. Use the text as the source of truth about the picture.", "read_pic", [
    ("c", "Text: Look at the apple. It is blue. What color is the apple?", "Blue",
     ["Red", "Green", "Yellow"], "The text says blue, so the apple is blue."),
    ("c", "Text: The bag is yellow. Which sentence matches the text?", "The bag is yellow.",
     ["The bag is green.", "The bag is red.", "The bag is blue."], "Yellow is the color word in the text."),
    ("c", "Text: I see a red bird. What color is the bird?", "Red",
     ["Yellow", "Green", "Blue"], "The text says red."),
    ("c", "Text: The pen is green. Which statement is correct?", "It is green.",
     ["It is red.", "It is blue.", "It is yellow."], "The text says the pen is green."),
])

V("vo_body", "Parts of the Face", 3, "上", 3,
  "Recognize face, eye, nose, and mouth.",
  [("face", "the face"), ("eye", "the eye"), ("nose", "the nose"), ("mouth", "the mouth")])

G("gr_this", "This Is and That Is", 3, "上", 3,
  "Use This is for something nearby and That is for something farther away.", "pointer", [
    ("c", "Pointing to a nearby pen, which sentence is correct?", "This is a pen.",
     ["These is a pen.", "This are a pen.", "This be a pen."], "Use This is for one object nearby."),
    ("c", "Pointing to a ruler farther away, which sentence is correct?", "That is a ruler.",
     ["This are a ruler.", "That am a ruler.", "That be a ruler."], "Use That is for one object farther away."),
    ("c", "In This is my nose, what does This refer to?", "This one nearby",
     ["That one farther away", "Several objects", "An object in the past"], "This refers to something nearby."),
    ("c", "In That is a cat, what does That refer to?", "That one farther away",
     ["This one nearby", "Several objects", "Your own name"], "That refers to something farther away."),
])

F("fu_body", "Introducing Parts of the Face", 3, "上", 3,
  "Use This is my to introduce parts of your face.", "func_daily", [
    ("c", "Pointing to your eye, what should you say?", "This is my eye.",
     ["This is my nose.", "This is my mouth.", "This is my face."], "Eye is the word for the organ of sight."),
    ("c", "What does This is my mouth introduce?", "The mouth",
     ["The eye", "The nose", "The face"], "Mouth is the opening used for eating and speaking."),
    ("c", "In Look at me. This is my face., what are you showing?", "Your face",
     ["A book", "An apple", "A schoolbag"], "Face means the front part of the head."),
    ("c", "How do you ask someone to look at your nose?", "Look at my nose.",
     ["Look at my ear.", "Look at my hand.", "Look at my foot."], "The nose is the facial feature used for smelling."),
])

R("rw_body", "Understanding Descriptions of the Face", 3, "上", 3,
  "Read sentences describing facial features and identify the part mentioned.", "read_pic", [
    ("c", "Text: This is my face. It is red. What color is the face?", "Red",
     ["Yellow", "Green", "Blue"], "The text says It is red."),
    ("c", "Text: This is my nose. Which sentence matches the text?", "This is my nose.",
     ["This is my mouth.", "This is my eye.", "This is my ear."], "Nose is the facial feature used for smelling."),
    ("c", "Text: Look at my eye. It is blue. What is blue?", "The eye",
     ["The nose", "The mouth", "The face"], "Eye is the part, and blue is its color."),
    ("c", "Text: This is my mouth. Which sentence appears in the text?", "This is my mouth.",
     ["This is my nose.", "This is my eye.", "This is my face."], "The text says mouth."),
])

V("vo_animal", "Animals", 3, "上", 4,
  "Recognize cat, dog, bird, and duck.",
  [("cat", "a cat"), ("dog", "a dog"), ("bird", "a bird"), ("duck", "a duck")])

F("fu_thisanimal", "Introducing Animals with This Is a", 3, "上", 4,
  "Use This is a followed by an animal noun to introduce an animal.", "func_daily", [
    ("c", "How do you introduce a cat?", "This is a cat.",
     ["This is a dog.", "This is a bird.", "This is a duck."], "A cat is a small domesticated feline."),
    ("c", "In This is a duck, which animal is it?", "A duck",
     ["A cat", "A dog", "A bird"], "A duck is a waterbird."),
    ("c", "What is this? If the answer is a dog, which sentence should you say?", "It is a dog.",
     ["It is a cat.", "It is a bird.", "It is a duck."], "A dog is a domesticated canine."),
    ("c", "Look! That is a bird. What is farther away?", "A bird",
     ["A cat", "A dog", "A duck"], "A bird is an animal with feathers and wings."),
])

R("rw_animal", "Understanding Sentences About Animals", 3, "上", 4,
  "Read sentences about animals and identify the animal and its color.", "read_short", [
    ("c", "Read: This is a cat. It is black. What is it?", "A cat",
     ["A dog", "A bird", "A duck"], "A cat is a small domesticated feline."),
    ("c", "Read: That is a duck. It is yellow. What color is the duck?", "Yellow",
     ["Black", "Blue", "Green"], "The text says It is yellow."),
    ("c", "Read: I see a dog. Which sentence matches the text?", "I see a dog.",
     ["I see a cat.", "I see a bird.", "I see a duck."], "Dog names a domesticated canine."),
    ("c", "Read: This is a bird. It is blue. Which sentence is correct?", "The bird is blue.",
     ["The bird is red.", "The cat is blue.", "The duck is blue."], "The text says bird and gives its color as blue."),
])

V("vo_food", "Food", 3, "上", 5,
  "Recognize bread, egg, rice, and milk.",
  [("bread", "bread"), ("egg", "an egg"), ("rice", "cooked rice"), ("milk", "milk")])

G("gr_like", "Expressing Likes with I Like", 3, "上", 5,
  "Use I like and I do not like to express preferences.", "present_basic", [
    ("c", "Which sentence means \"I like bread\"?", "I like bread.",
     ["I likes bread.", "Like I bread.", "I like am bread."], "Say I like bread to express that you like something."),
    ("c", "What does I like milk mean?", "I like milk",
     ["I do not like milk", "I have milk", "Milk likes me"], "Here, like means to enjoy or prefer something."),
    ("c", "Which sentence is correct?", "I like apples.",
     ["I likes apples.", "I like am apples.", "Like I apples."], "Use like, without -s, after I."),
    ("c", "What does I do not like rice mean?", "I do not like rice",
     ["I like rice", "I do not have rice", "Rice does not like me"], "Do not like expresses a negative preference."),
])

F("fu_food", "Talking About Food Preferences", 3, "上", 5,
  "Use I like and Have some to talk about food.", "func_daily", [
    ("c", "How do you say that you like eggs?", "I like eggs.",
     ["I like milk.", "I like rice.", "I like bread."], "The plural of egg is eggs."),
    ("c", "What does Have some bread mean?", "Please have some bread",
     ["Please have some rice", "Please have some milk", "Please have some eggs"], "Bread is a baked food."),
    ("c", "What does Can I have some milk? ask?", "May I have some milk?",
     ["May I have some bread?", "Where is the milk?", "Do you like milk?"], "Have some milk means to ask for or offer some milk."),
    ("c", "Which sentence means \"I like rice\"?", "I like rice.",
     ["I like bread.", "I like eggs.", "I like milk."], "Rice is the word for the cooked grain."),
])

R("rw_food", "Understanding Statements About Food Preferences", 3, "上", 5,
  "Read what a person says about food preferences and identify the food they like.", "read_short", [
    ("c", "Read: Sarah says, \"I like bananas.\" What does Sarah like?", "Bananas",
     ["Apples", "Bread", "Rice"], "The quoted sentence says bananas."),
    ("c", "Read: Mike says, \"I like milk.\" Which sentence matches the passage?", "Mike likes milk.",
     ["Mike likes rice.", "Mike does not like milk.", "Sarah likes milk."], "Mike is speaking, and he likes milk."),
    ("c", "Read: I like bread. I do not like eggs. What does this person dislike?", "Eggs",
     ["Bread", "Milk", "Rice"], "Do not like eggs means the person dislikes eggs."),
    ("c", "Read: Chen Jie says, \"I like rice.\" Which sentence gives the same meaning?", "Chen Jie likes rice.",
     ["Chen Jie likes bread.", "Chen Jie likes milk.", "Chen Jie does not like rice."], "The quoted sentence says I like rice."),
])

V("vo_num", "Numbers 1 to 10", 3, "上", 6,
  "Recognize one, two, three, and ten.",
  [("one", "the number 1"), ("two", "the number 2"), ("three", "the number 3"), ("ten", "the number 10")])

V("vo_toy", "Toys and Gifts", 3, "上", 6,
  "Recognize ball, doll, kite, and boat.",
  [("ball", "a ball"), ("doll", "a toy doll"), ("kite", "a kite"), ("boat", "a small boat")])

G("gr_howmany", "Asking How Many", 3, "上", 6,
  "Use numbers from 1 to 10 and How many to ask about quantity.", "number_q", [
    ("c", "How do you ask \"How many balloons do you have?\"?", "How many balloons?",
     ["How old balloons?", "What many balloons?", "How many balloon is?"], "Use How many to ask about quantity."),
    ("n", "In the sequence one, two, three, what number comes next?", 4, "The number after three is four, or 4."),
    ("c", "What does How many cakes? ask?", "It asks how many cakes there are",
     ["What color the cakes are", "Where the cakes are", "Who wants cake"], "How many asks about quantity."),
    ("c", "I have five books. How many books are there?", "5",
     ["4", "6", "10"], "Five is 5."),
])

F("fu_bday", "Asking About Age", 3, "上", 6,
  "Ask How old are you? to find out someone's age, and answer with I am.", "func_greet", [
    ("c", "How do you ask someone how old they are?", "How old are you?",
     ["How are you?", "How many are you?", "What is your name?"], "Ask How old are you? to find out someone's age."),
    ("c", "How old are you? If the person is 9, how should they answer?", "I am nine.",
     ["I am ten.", "I am five.", "I am six."], "Nine is the word for 9."),
    ("c", "When do you say Happy birthday!?", "On someone's birthday",
     ["When saying goodbye", "When asking for directions", "When shopping"], "Happy birthday is a birthday greeting."),
    ("c", "What does This is a gift for you mean?", "This is a present for you",
     ["This is my balloon", "How old are you?", "Goodbye"], "Gift means a present."),
])

R("rw_num", "Understanding Quantity", 3, "上", 6,
  "Read a sentence to find the number of objects.", "read_short", [
    ("c", "Read: I have three balls. How many balls are there?", "3",
     ["2", "4", "10"], "Three is 3."),
    ("c", "Read: I see ten kites. Which sentence matches the text?", "I see 10 kites.",
     ["I see 5 kites.", "I see 10 balls.", "I see 1 kite."], "Ten kites means 10 kites."),
    ("n", "Read: This is a boat. I have one boat. How many boats are there?", 1, "One is 1."),
    ("c", "Read: I am six. I have two dolls. How many dolls are there?", "2",
     ["6", "1", "3"], "Two dolls means 2 dolls; six is the person's age."),
])

# ---------- Grade 3, second semester ----------

S("ph_a", "Short Vowel a", 3, "下", 1,
  "Recognize short vowel a in stressed closed syllables, as in cat, bag, map, and hat.",
  "Short vowel a", ["cat", "bag", "map", "hat"], ["he", "kite", "nose", "me"], "short_vowel")

V("vo_country", "Countries and Origins", 3, "下", 1,
  "Recognize China, Canada, the UK, and the USA.",
  [("China", "China"), ("Canada", "Canada"), ("UK", "the United Kingdom"), ("USA", "the United States")])

G("gr_from", "Using I Am From to Say Where Someone Is From", 3, "下", 1,
  "Use am or is with from to say where you or someone else is from.", "be", [
    ("c", "I ____ from China. Which word belongs in the blank?", "am",
     ["is", "are", "be"], "I takes am."),
    ("c", "Which sentence means \"I am from Canada\"?", "I am from Canada.",
     ["I are from Canada.", "I from Canada am.", "Am from I Canada."], "The correct sentence is I am from Canada."),
    ("c", "What does Where are you from? ask?", "Where you are from",
     ["How old you are", "What your name is", "What you like"], "Where are you from asks about someone's origin."),
    ("c", "She ____ from the UK. Which word belongs in the blank?", "is",
     ["am", "are", "be"], "She takes is."),
])

F("fu_from", "Asking Where Someone Is From", 3, "下", 1,
  "Ask Where are you from? and answer with I am from.", "func_greet", [
    ("c", "How do you ask someone where they are from?", "Where are you from?",
     ["What is your name?", "How old are you?", "How are you?"], "Ask Where are you from? to find out someone's origin."),
    ("c", "Where are you from? If you are from China, how should you answer?", "I am from China.",
     ["I am from Canada.", "I am from the UK.", "I am from the USA."], "China is the English name of the country."),
    ("c", "He is from the USA. Where is he from?", "The United States",
     ["China", "Canada", "The United Kingdom"], "The USA means the United States."),
    ("c", "When are you most likely to hear Welcome back to school!?", "When returning to school",
     ["When leaving school", "At dinner", "While shopping"], "Welcome back to school greets someone returning to school."),
])

R("rw_from", "Understanding Where Someone Is From", 3, "下", 1,
  "Read a self-introduction and identify the person's country of origin.", "read_short", [
    ("c", "Read: Hello! I am Amy. I am from the UK. Where is Amy from?", "The United Kingdom",
     ["China", "Canada", "The United States"], "The UK means the United Kingdom."),
    ("c", "Read: I am Zhang Peng. I am from China. Which sentence matches the passage?", "Zhang Peng is from China.",
     ["Zhang Peng is from Canada.", "Amy is from China.", "Zhang Peng is from the United States."], "The name is Zhang Peng, and the country is China."),
    ("c", "Read: She is from Canada. Where is she from?", "Canada",
     ["The United Kingdom", "China", "The United States"], "Canada is the country named in the sentence."),
    ("c", "Read: Mike says, \"I am from the USA.\" Where is Mike from?", "The United States",
     ["The United Kingdom", "China", "Canada"], "The quoted text says the USA."),
])

S("ph_e", "Short Vowel e", 3, "下", 2,
  "Recognize short vowel e, as in ten, pen, red, and leg.",
  "Short vowel e", ["ten", "pen", "red", "leg"], ["cat", "cake", "kite", "nose"], "short_vowel")

V("vo_family", "Family Members", 3, "下", 2,
  "Recognize father, mother, brother, and sister.",
  [("father", "a male parent"), ("mother", "a female parent"), ("brother", "a male sibling"), ("sister", "a female sibling")])

G("gr_who", "Asking Who Someone Is with Who Is", 3, "下", 2,
  "Ask Who is he? or Who is she? and introduce family members with He is or She is.", "pronoun", [
    ("c", "How do you ask \"Who is he?\"?", "Who is he?",
     ["Who are he?", "Who he is name?", "What is he who?"], "Ask Who is he? to find out who a male person is."),
    ("c", "What does Who is she? ask?", "Who she is",
     ["Where she is", "How old she is", "What she likes"], "Who is she? asks about a female person's identity."),
    ("c", "He ____ my father. Which word belongs in the blank?", "is",
     ["am", "are", "be"], "He takes is."),
    ("c", "Which sentence is correct?", "She is my mother.",
     ["She are my mother.", "She am my mother.", "She be my mother."], "Use is after She."),
])

F("fu_family", "Introducing Family Members", 3, "下", 2,
  "Use This is my to introduce family members.", "func_daily", [
    ("c", "How do you introduce your father?", "This is my father.",
     ["This is my mother.", "This is my sister.", "This is my brother."], "Father means a male parent."),
    ("c", "Who is This is my sister referring to?", "A sister",
     ["A father", "A mother", "A brother"], "Sister means a female sibling."),
    ("c", "Who is he? If he is your brother, how should you answer?", "He is my brother.",
     ["She is my sister.", "She is my mother.", "He is my father."], "Say He is my brother to introduce a brother."),
    ("c", "What does This is my family mean?", "This is my family",
     ["This is my friend", "This is my school", "This is my book"], "Family means the people in your family."),
])

R("rw_family", "Understanding Family Introductions", 3, "下", 2,
  "Read sentences introducing family members and identify who is being described.", "read_short", [
    ("c", "Read: This is my father. He is from China. Who is this?", "A father",
     ["A mother", "A sister", "A friend"], "Father means a male parent."),
    ("c", "Read: She is my mother. Which sentence matches the text?", "She is my mother.",
     ["He is my father.", "She is my sister.", "He is my brother."], "The sentence says She is my mother."),
    ("c", "Read: This is my brother. He is ten. How old is the brother?", "10 years old",
     ["6 years old", "9 years old", "8 years old"], "He is ten means he is 10 years old."),
    ("c", "Read: Sarah says, \"This is my sister.\" Which sentence is correct?", "Sarah is introducing her sister.",
     ["Sarah is introducing her father.", "Sarah is introducing her mother.", "Sarah is introducing her teacher."], "Sister means a female sibling."),
])

S("ph_i", "Short Vowel i", 3, "下", 3,
  "Recognize short vowel i, as in big, pig, sit, and fish.",
  "Short vowel i", ["big", "pig", "sit", "fish"], ["cake", "he", "nose", "cat"], "short_vowel")

V("vo_size", "Size and Height", 3, "下", 3,
  "Recognize big, small, tall, and short. Here, short means not tall.",
  [("big", "large in size"), ("small", "little in size"), ("tall", "of great height"), ("short", "not tall")])

G("gr_size", "Using Adjectives for Size and Height", 3, "下", 3,
  "Use It is with big, small, tall, or short to describe an animal.", "be", [
    ("c", "Which sentence means \"It is small\"?", "It is small.",
     ["It is tall.", "It is big.", "It is long."], "Small means little in size."),
    ("c", "Look at the elephant. It is big. What is the elephant like?", "It is large",
     ["It is small", "It is short", "It is short in length"], "Big means large in size."),
    ("c", "The giraffe is tall. What is the giraffe like?", "It is tall",
     ["It is short", "It is small", "It is short in length"], "Tall means of great height."),
    ("c", "What does It is short mean?", "It is not tall",
     ["It is tall", "It is big", "It is long"], "In this lesson, short describes height."),
])

R("rw_zoo", "Understanding Zoo Descriptions", 3, "下", 3,
  "Read sentences describing animals and answer based on the text.", "read_pic", [
    ("c", "Text: Look at the bear. It is big. What is the bear like?", "It is big",
     ["It is small", "It is short", "It is thin"], "The text says It is big."),
    ("c", "Text: The monkey is small. Which sentence matches the text?", "The monkey is small.",
     ["The monkey is big.", "The monkey is tall.", "The bear is small."], "Monkey names the animal, and small describes its size."),
    ("c", "Text: The giraffe is tall. The cat is short. Which animal is tall?", "The giraffe",
     ["The cat", "The bear", "The monkey"], "The text says the giraffe is tall."),
    ("c", "Text: It is a pig. It is big. Which animal is big?", "The pig",
     ["The cat", "The bird", "The duck"], "Pig names the animal."),
])

S("ph_o", "Short Vowel o", 3, "下", 4,
  "Recognize short vowel o, as in dog, box, hot, and not.",
  "Short vowel o", ["dog", "box", "hot", "not"], ["note", "nose", "cake", "he"], "short_vowel")

V("vo_roomobj", "Things in a Room", 3, "下", 4,
  "Recognize desk, chair, bag, and book.",
  [("desk", "a desk"), ("chair", "a chair"), ("bag", "a schoolbag"), ("book", "a book")])

G("gr_prep", "In, On, and Under", 3, "下", 4,
  "Use in, on, and under to describe whether an object is inside, on top of, or below something.", "pointer", [
    ("c", "The book is inside the desk. Which sentence should you choose?", "The book is in the desk.",
     ["The book is on the desk.", "The book is under the desk.", "The book is desk."], "Use in to mean inside."),
    ("c", "The ball is under the chair. Where is the ball?", "Under the chair",
     ["On the chair", "Inside the chair", "Beside the chair"], "Under means below."),
    ("c", "The cat is on the box. Where is the cat?", "On the box",
     ["Inside the box", "Under the box", "Behind the box"], "On means on top of."),
    ("c", "What does Where is my car? ask?", "Where my car is",
     ["Whose car it is", "What color the car is", "Whether you like cars"], "Where is asks about location."),
])

F("fu_where", "Asking About Location", 3, "下", 4,
  "Use Where is to ask where an object is.", "func_daily", [
    ("c", "How do you ask where a schoolbag is?", "Where is my bag?",
     ["What is my bag?", "Who is my bag?", "How is my bag?"], "Use Where is to ask about location."),
    ("c", "Where is the book? If the book is on the chair, how should you answer?", "It is on the chair.",
     ["It is in the chair.", "It is under the chair.", "It is the chair."], "Use on for something on top of a surface."),
    ("c", "In It is in the desk, where is the object?", "Inside the desk",
     ["On the desk", "Under the desk", "Beside the chair"], "In the desk means inside the desk."),
    ("c", "Which sentence has the same meaning as The ball is under the chair?", "The ball is below the chair.",
     ["The ball is on the chair.", "The book is under the chair.", "The ball is in the desk."], "Ball means a ball, and under the chair means below the chair."),
])

R("rw_where", "Understanding Locations", 3, "下", 4,
  "Read sentences about location and identify where an object is.", "read_pic", [
    ("c", "Text: The book is on the desk. Where is the book?", "On the desk",
     ["Inside the desk", "Under the desk", "On the chair"], "On the desk means on top of the desk."),
    ("c", "Text: My bag is under the chair. Which sentence matches the text?", "The bag is under the chair.",
     ["The bag is on the chair.", "The book is under the chair.", "The bag is in the desk."], "Bag means a schoolbag, and under the chair gives its location."),
    ("c", "Text: The pen is in the bag. Where is the pen?", "Inside the bag",
     ["On the bag", "Under the bag", "On the desk"], "In the bag means inside the bag."),
    ("c", "Text: Where is the car? It is under the desk. Where is the car?", "Under the desk",
     ["On the desk", "On the chair", "In the schoolbag"], "The answer says under the desk."),
])

S("ph_u", "Short Vowel u", 3, "下", 5,
  "Recognize short vowel u, as in fun, run, cup, and sun.",
  "Short vowel u", ["fun", "run", "cup", "sun"], ["use", "cute", "cake", "he"], "short_vowel")

P("ph_shortrev", "Review: The Five Short Vowels", 3, "下", 5,
  "Distinguish short vowels, as in cat, from long vowels, as in cake.", "short_vowel", [
    ("c", "Which word has the same a sound as cat?", "bag",
     ["cake", "name", "face"], "Bag and cat both have short a."),
    ("c", "Which word has a different vowel sound from cake?", "cat",
     ["name", "face", "make"], "Cat has a short vowel; name, face, and make have the a-e pattern."),
    ("c", "Which word has a different vowel sound from big?", "bike",
     ["pig", "sit", "fish"], "Bike has the i-e pattern; big, pig, sit, and fish have short i."),
    ("c", "Which word has the same vowel sound as sun?", "cup",
     ["use", "cute", "tube"], "Sun and cup both have short u."),
])

V("vo_fruit", "Fruit", 3, "下", 5,
  "Recognize pear, apple, banana, and orange. Here, orange means the fruit.",
  [("pear", "a pear"), ("apple", "an apple"), ("banana", "a banana"), ("orange", "the fruit orange")])

G("gr_doyou", "Yes/No Questions with Do You Like", 3, "下", 5,
  "Ask about preferences with Do you like and answer Yes, I do or No, I do not.", "present_basic", [
    ("c", "How do you ask whether someone likes pears?", "Do you like pears?",
     ["Does you like pears?", "Do you likes pears?", "Are you like pears?"], "Use Do before you."),
    ("c", "Do you like apples? Which is an affirmative answer?", "Yes, I do.",
     ["Yes, I does.", "Yes, I am.", "Yes, I like do."], "The affirmative answer to a Do question is Yes, I do."),
    ("c", "Do you like bananas? Which is a negative answer?", "No, I do not.",
     ["No, I does not.", "No, I am not.", "No, I not like."], "The negative answer to a Do question is No, I do not."),
    ("c", "What does Do you like oranges? ask?", "Whether you like oranges",
     ["Where the oranges are", "What color the oranges are", "How many oranges you have"], "Do you like asks about preference."),
])

G("gr_plural", "Plural Count Nouns", 3, "下", 5,
  "Form common plurals of nouns such as cat and box.", "plural", [
    ("c", "What is the plural of cat?", "cats",
     ["cates", "caties", "cat"], "Usually, add s: cats."),
    ("c", "What is the plural of box?", "boxes",
     ["boxs", "boxies", "box"], "Add es to a word ending in x: boxes."),
    ("n", "How many dogs are there in two dogs?", 2, "Two means 2."),
    ("c", "Which sentence uses a plural noun?", "I see three birds.",
     ["I see one bird.", "I see a bird.", "I see the bird."], "Three birds is plural."),
])

R("rw_fruit", "Understanding Fruit Preferences", 3, "下", 5,
  "Read short conversations using Do you like and identify the preferred fruit.", "read_short", [
    ("c", "Read: Do you like pears? Yes, I do. Does the person like pears?", "Yes",
     ["No", "It is not stated", "The person only likes apples"], "The answer is Yes, I do."),
    ("c", "Read: Do you like apples? No, I do not. Which sentence matches the conversation?", "The person does not like apples.",
     ["The person likes apples.", "The person likes pears.", "The person has three apples."], "No, I do not expresses a negative preference."),
    ("c", "Read: I like bananas. I see four bananas. How many bananas are there?", "4",
     ["3", "5", "2"], "Four is 4."),
    ("c", "Read: I have an orange. What does orange mean here?", "The fruit",
     ["The color", "An apple", "A pear"], "In this fruit lesson, an orange means the fruit."),
])

V("vo_num20", "Numbers 11 to 20", 3, "下", 6,
  "Recognize eleven, twelve, thirteen, and twenty.",
  [("eleven", "the number 11"), ("twelve", "the number 12"), ("thirteen", "the number 13"), ("twenty", "the number 20")])

G("gr_howmany2", "How Many with Numbers 11 to 20", 3, "下", 6,
  "Use How many and number words from 11 to 20 to state a quantity.", "number_q", [
    ("c", "What does How many apples do you see? ask?", "It asks how many apples you see",
     ["Whether you like apples", "What color the apples are", "Where the apples are"], "How many asks about quantity."),
    ("n", "What number is eleven?", 11, "Eleven is 11."),
    ("c", "I see fifteen kites. How many kites are there?", "15",
     ["14", "16", "50"], "Fifteen is 15."),
    ("c", "Which number comes after twelve?", "thirteen",
     ["eleven", "twenty", "fourteen"], "Thirteen comes after twelve."),
])

R("rw_count", "Understanding Quantities from 11 to 20", 3, "下", 6,
  "Read sentences and identify quantities from 11 to 20.", "read_short", [
    ("c", "Read: I see eleven birds. How many birds are there?", "11",
     ["10", "12", "20"], "Eleven is 11."),
    ("n", "Read: How many cars do you see? I see twenty. How many cars are there?", 20, "Twenty is 20."),
    ("c", "Read: I have twelve crayons. Which sentence matches the text?", "I have 12 crayons.",
     ["I have 11 crayons.", "I have 13 crayons.", "I have 20 crayons."], "Twelve is 12."),
    ("c", "Read: I see thirteen kites and eleven birds. How many kites are there?", "13",
     ["11", "12", "20"], "The number of kites is thirteen."),
])
