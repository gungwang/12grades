# -*- coding: utf-8 -*-
"""People's Education Press (2019), Compulsory Book 2. Unit titles follow the common outline; volume placement is pending verification."""
from enh_tx import V, P, G, F, R, q


def load():
    V("vo_heritage", "Cultural Heritage", 11, 1,
      "Recognize heritage, temple, preserve, and relic.",
      [("heritage", "cultural legacy"), ("preserve", "protect and maintain"), ("relic", "historic object"), ("dynasty", "ruling period")], "vo_soc")

    V("vo_protect", "Protecting Cultural Relics", 11, 1,
      "Recognize restore, damage, ancient, and site.",
      [("restore", "repair to its original condition"), ("damage", "harm"), ("ancient", "very old"), ("site", "location")], "vo_soc")

    G("gr_nonrest", "Nonrestrictive Relative Clauses", 11, 1,
      "Use a comma and who or which to add information, rather than that.", "rel", [
        q("My brother, ___ lives in Luoyang, is a guide. Which word completes the sentence?", "who",
          "that", "which", "whom", "In a nonrestrictive relative clause, use who as the subject for a person, not that."),
        q("The temple, ___ was built in the Tang Dynasty, is famous. Which word completes the sentence?", "which",
          "that", "who", "where", "Use which for a thing in a nonrestrictive relative clause, not that."),
        q("Which sentence is correct?", "The site, which we visited, is ancient",
          "The site, that we visited, is ancient", "The site which, we visited is ancient",
          "The site, who we visited, is ancient",
          "Use which in a nonrestrictive clause after a comma."),
        q("Does the main clause still make sense if a nonrestrictive relative clause is removed?", "Yes; the clause adds extra information",
          "No; the main clause no longer makes sense", "The relative clause becomes the subject", "The comma must be removed",
          "A nonrestrictive clause adds extra information; the main clause remains complete without it."),
      ])

    G("gr_whichsent", "Which Referring to a Whole Clause", 11, 1,
      "Use which to refer to the entire preceding clause and distinguish this use from restrictive relative clauses.", "rel", [
        q("He missed the train, ___ made him late. Which word completes the sentence?", "which",
          "that", "who", "what", "Here, which refers to the whole event of missing the train."),
        q("In which sentence does which refer to the whole preceding clause?", "She forgot the ticket, which was a pity",
          "The ticket which she forgot was blue", "The boy who forgot it is Tom",
          "This is the train which was late",
          "The which clause after the comma refers to the event of forgetting the ticket."),
        q("They restored the site, ___ took three years. Which word completes the sentence?", "which",
          "who", "that", "where", "Here, which refers to the whole process of restoring the site."),
        q("In which sentence can that not be replaced by which referring to the whole clause?", "The relic that we saw is small",
          "Rain came, which stopped the work", "He was late, which annoyed the guide",
          "The bridge fell, which shocked everyone",
          "In “The relic that we saw,” that refers to relic, not to the whole clause."),
      ], "inferred")

    F("fu_heritage", "Discussing Heritage Protection", 11, 1,
      "Exchange views on protecting cultural heritage and explain your reasons.", "fu_view", [
        q("You want to say that an ancient temple should be protected. Which sentence is suitable?", "I think the ancient temple should be preserved",
          "I thinks the ancient temple should be preserved", "I not think the ancient temple should be preserved", "I think the ancient temple should be perserved",
          "Use should be preserved to say that something ought to be protected."),
        q("You want to explain that the damage was caused by visitors carving the walls. Which sentence is suitable?", "The damage comes from visitors cutting the walls",
          "Damage is a coach", "The damage come from visitors cutting the walls", "The damage comes from vsiitors cutting the walls",
          "Use comes from to explain a cause."),
        q("Someone says restoration is too expensive. You partly agree; how should you respond?", "I see your point, but the site is worth it",
          "I see your piont, but the site is worth it", "I see your poit, but the site is worth it", "I see your point, but the site is worh it",
          "I see your point, but... is a way to partly agree."),
        q("You want to suggest setting visitor rules. Which sentence is suitable?", "We could make rules for visitors",
          "We could maked rules for visitors", "We could to make rules for visitors", "We could make rules for vsiitors",
          "Use We could make rules to make a suggestion."),
      ])

    _h = "The old city wall is part of the local heritage. Workers are restoring a gate that was damaged by rain. Visitors may take photos but must not touch the relics."
    R("rw_heritage", "Reading a Heritage Notice", 11, 1,
      "Read a heritage notice and summarize whether it describes visitor rules or argues against protection.", "rw_main", [
        q(_h + " What is the city wall part of?", "Local heritage", "A sports stadium", "An email", "A marathon", "The passage calls it local heritage."),
        q(_h + " Why is the gate being restored?", "It was damaged by rain", "Visitors bought it", "It was newly built", "There is no gate",
          "The passage says it was damaged by rain."),
        q(_h + " What must visitors not do?", "Touch the relics", "Take photos", "Read the notice", "Stand outside",
          "The passage says visitors must not touch the relics."),
        q(_h + " What is the passage mainly doing?", "Describing the heritage site and visitor rules", "Arguing against protecting the wall", "Hiring a coach", "Reporting a flood",
          "The passage describes restoration and rules; it does not argue against protection."),
      ])

    R("wr_heritage", "Writing a Heritage Recommendation", 11, 1,
      "Select a sentence for a short recommendation based on its key points.", "rw_write", [
        q("Key points: the wall is heritage, rain caused damage, and visitors must not touch it. Which sentence includes all three?",
          "The wall is heritage, rain damaged it, and visitors must not touch the relics",
          "The wall is heritage", "Rain is wet", "Visitors like photos",
          "All three key points must be included."),
        q("You want to add the wall's age with a nonrestrictive relative clause. Which sentence is correct?",
          "The wall, which dates from the Ming Dynasty, needs care",
          "The wall, that dates from the Ming Dynasty, needs care",
          "The wall which, dates from the Ming Dynasty needs care",
          "The wall, who dates from the Ming Dynasty, needs care",
          "Use which, not that, in a nonrestrictive clause."),
        q("Which sentence is suitable as the opening of a recommendation?", "I suggest we protect the old city wall",
          "I sgugest we protect the old city wall", "I suggset we protect the old city wall", "I sugest we protect the old city wall",
          "I suggest is a suitable way to begin a recommendation."),
        q("Which sentence correctly uses which to refer to the whole clause?", "Some people carve names, which damages the stone",
          "The stone which people carve is soft", "People who carve names are few",
          "This is the wall which is old",
          "The which clause after the comma refers to the act of carving names."),
      ])

    V("vo_wild", "Wildlife", 11, 2,
      "Recognize wildlife, species, habitat, and extinct.",
      [("wildlife", "wild animals"), ("species", "kind of organism"), ("habitat", "natural home"), ("extinct", "no longer existing")], "vo_soc")

    V("vo_habitat", "Protecting Habitats", 11, 2,
      "Recognize reserve, hunter, endangered, and plain.",
      [("reserve", "protected area"), ("hunter", "person who hunts"), ("endangered", "at risk of extinction"), ("plain", "large flat area")], "vo_soc")

    G("gr_passcont", "Present Continuous Passive", 11, 2,
      "Form the present continuous passive with am, is, or are + being + past participle.", "passive", [
        q("The reserve ___ now. It is being cleaned. Which form completes the sentence?", "is being cleaned",
          "is cleaning", "is cleaned", "was being cleaned", "The present continuous passive uses is being + past participle."),
        q("Which sentence uses the present continuous passive?", "The antelopes are being protected",
          "The antelopes are protecting", "The antelopes were protected", "The antelopes have protected",
          "Are being protected describes an action that is currently being done to them."),
        q("A new plain ___ for the birds this week. Which form completes the sentence?", "is being prepared",
          "is preparing", "prepares", "is been prepared", "The subject is receiving the action, so use is being prepared."),
        q("Which sentence uses the voice incorrectly?", "The habitat is being destroy",
          "The habitat is being destroyed", "Workers are destroying the old fence", "The fence is being repaired",
          "Use the past participle destroyed after being, not the base form destroy."),
      ])

    G("gr_ppvsing", "Past Participles and -ing Forms", 11, 2,
      "Choose an -ing form or a past participle based on whether the subject does or receives the action.", "pp", [
        q("The story is ___ (interest). The story is exciting. Which form completes the sentence?", "interesting",
          "interested", "interest", "interests", "Use interesting to describe the quality of a thing."),
        q("The children are ___ in whales. Which form completes the sentence?", "interested",
          "interesting", "interest", "interests", "Use interested to describe how a person feels."),
        q("Which sentence is correct?", "We are worried about the endangered species",
          "We are worrying species about the endangered", "The species is worried to us",
          "The news is worried",
          "Use worried for how a person feels; use worrying for something that causes concern."),
        q("A ___ species describes a species that causes concern. Which form completes the phrase?", "worrying",
          "worried", "worry", "worries", "Use worrying to describe a species that makes people concerned."),
      ], "inferred")

    F("fu_protect", "Discussing Wildlife Protection", 11, 2,
      "Explain reasons for protecting wildlife and respond to differing views.", "fu_view", [
        q("You want to say that the Tibetan antelopes are being protected. Which sentence is suitable?", "The antelopes are being protected in the reserve",
          "The antelopes are protecting the reserve", "The atnelopes are being protected in the reserve", "The anteloeps are being protected in the reserve",
          "Use are being protected for an action being done to the antelopes now."),
        q("You want to explain that hunters are the main source of danger. Which sentence is suitable?", "Hunters are the main danger to this species",
          "Hunters is the main danger to this species", "Hnuters are the main danger to this species", "Huntres are the main danger to this species",
          "Use are the main danger to explain the cause."),
        q("Someone says the reserve is useless. You disagree; how should you respond?", "I don't agree, because the numbers are rising",
          "I don't agree, because the numbers are rise", "I don't agree, because the nmubers are rising", "I don't agree, because the numbres are rising",
          "Add a reason with because when you disagree."),
        q("You want to advise people not to buy products made from wild animals. Which sentence is suitable?", "Please do not buy products made from wild animals",
          "Please do not buy porducts made from wild animals", "Please do not buy produtcs made from wild animals", "Please do not buy prducts made from wild animals",
          "Use the imperative Please do not buy to make a suggestion."),
      ])

    _a = "The Tibetan antelope was once endangered. Now the animals are being protected on the plain. Visitors are interested in the reserve but must not feed the wildlife."
    R("rw_wild", "Reading about Wildlife Protection", 11, 2,
      "Read about wildlife protection and identify the past situation and current measures.", "rw_detail", [
        q(_a + " What was the Tibetan antelope's status in the past?", "Endangered", "Already extinct", "Overpopulated", "Living in a city",
          "The passage says it was once endangered."),
        q(_a + " What is happening to them now?", "They are being protected on the plain", "They are being hunted", "They have left the reserve", "They are being fed by visitors",
          "The passage says they are being protected on the plain."),
        q(_a + " What must visitors not do?", "Feed the wildlife", "Show interest in the reserve", "Read the notice", "Stand outside",
          "The passage says visitors must not feed the wildlife."),
        q(_a + " Which sentence agrees with the passage?", "Visitors must not feed the wildlife",
          "The antelope is extinct", "The animals are protecting the visitors", "The plain has no reserve",
          "The passage says that visitors must not feed the wildlife."),
      ])

    R("wr_wild", "Writing a Wildlife Protection Poster", 11, 2,
      "Choose a sentence for a wildlife-protection poster based on its key points.", "rw_write", [
        q("Key points: the species was endangered, it is now being protected, and visitors must not feed it. Which sentence includes all three?",
          "This species was endangered, it is being protected now, and please do not feed it",
          "This species was endangered", "Please do not feed it", "The plain is wide",
          "All three key points must be included."),
        q("A poster needs the present continuous passive to describe current work. Which sentence fits?", "A new fence is being built",
          "A new fence is building", "A new fence built being", "A new fence is been built",
          "Only is being built is in the present continuous passive."),
        q("Which sentence is suitable as the poster title?", "Protect the endangered antelope",
          "Protect the ednangered antelope", "Protect the endangeerd antelope", "Protect the enangered antelope",
          "A title can use the imperative Protect."),
        q("Which sentence correctly distinguishes interested from interesting?", "Children are interested in the interesting film",
          "Children are interesting in the interested film", "The film is interested in children",
          "Children are interest in the film",
          "Use interested for people and interesting for the film."),
      ])

    V("vo_net", "The Internet", 11, 3,
      "Recognize Internet, blog, comment, and identity.",
      [("Internet", "global computer network"), ("blog", "online journal"), ("comment", "remark or response"), ("identity", "who a person is")], "vo_world")

    V("vo_online", "Online Behavior", 11, 3,
      "Recognize online, privacy, password, and post.",
      [("online", "connected to the internet"), ("privacy", "the right to keep personal information private"), ("password", "secret access code"), ("post", "publish online")], "vo_world")

    G("gr_passperf", "Present Perfect Passive", 11, 3,
      "Form the present perfect passive with have or has + been + past participle.", "passive", [
        q("The password ___ . It has already been changed. Which form completes the sentence?", "has been changed",
          "has changed", "has being changed", "was being changed", "The present perfect passive uses has been + past participle."),
        q("Which sentence uses the present perfect passive?", "Two comments have been deleted",
          "Two comments have deleted", "Two comments are deleting", "Two comments deleted been",
          "Have been deleted means the comments have already been removed."),
        q("My blog ___ by many students since Monday. Which form completes the sentence?", "has been read",
          "has read", "is being read", "have been read", "Blog is singular, so use has been read in the present perfect passive."),
        q("Which sentence is correct?", "The post has been shared online",
          "The post has been share online", "The post has being shared online", "The post have been shared online",
          "Use the past participle shared after been; use has with a singular subject."),
      ])

    G("gr_since", "Since with the Present Perfect", 11, 3,
      "Use the present perfect with a time introduced by since.", "tense", [
        q("I ___ this blog since 2020. Which form completes the sentence?", "have kept",
          "kept", "keep", "am keeping", "Use have kept with since 2020."),
        q("Which sentence is correct?", "She has used the same password since May",
          "She used the same password since May", "She uses the same password since May",
          "She has used the same password since three days",
          "Use the present perfect with a point in time after since. “Since three days” is not a correct time expression; use “for three days” or “since three days ago.”"),
        q("The app ___ many times since it was posted. Which form completes the sentence?", "has been updated",
          "was updated", "is updated", "updated", "The since clause gives the starting point, so use the present perfect passive in the main clause."),
        q("Which tense is most often used with since Monday?", "The present perfect", "The simple past by itself", "The present continuous for a future arrangement", "The simple present for a habit",
          "Since describes a period continuing from the past to the present, so use the present perfect."),
      ], "inferred")

    F("fu_net", "Discussing Online Safety", 11, 3,
      "Make suggestions about online habits and explain why privacy matters.", "fu_plan", [
        q("You want to remind a classmate not to share a password publicly. Which sentence is suitable?", "Never post your password online",
          "Post your password to everyone", "Never post your psasword online", "Never post your passwrod online",
          "Use Never post your password to give a warning."),
        q("You want to say that a rude comment has been removed. Which sentence is suitable?", "The rude comment has been deleted",
          "The rude comment has deleted the blog", "The rude cmoment has been deleted", "The rude commnet has been deleted",
          "Use has been deleted to say that something has already been removed."),
        q("Someone asks why you use a nickname. Which sentence gives a reason?", "I use a nickname to protect my privacy",
          "I use a nickname to protecting my privacy", "I use a nickname to protects my privacy", "I use an nickname to protect my privacy",
          "To protect my privacy explains the purpose."),
        q("You want to suggest checking someone's identity before adding them as a friend. Which sentence is suitable?", "Check the person's identity before you add them",
          "Check the person's iedntity before you add them", "Check the person's identtiy before you add them", "Check the person's idntity before you add them",
          "Use the imperative Check to make a suggestion."),
      ])

    _i = "Since March, Lin's class blog has been read by students in three schools. One unkind comment has been deleted. Lin never posts his real name or password."
    R("rw_net", "Reading about Online Safety", 11, 3,
      "Read about online behavior and decide whether the writer is stating facts or praising a rude comment.", "rw_main", [
        q(_i + " Since when has the blog been read?", "Since March", "Yesterday", "One day three years ago", "No time is given",
          "The passage says since March."),
        q(_i + " What happened to the unkind comment?", "It has been deleted", "It was pinned", "It is increasing", "It became a password",
          "The passage says it has been deleted."),
        q(_i + " What does Lin not post?", "His real name or password", "The class blog", "The school name", "Any pictures",
          "The passage says he never posts his real name or password."),
        q(_i + " How does the writer respond to the unkind comment?", "They delete it rather than approve of it",
          "They keep it because it is funny", "They do not mention it", "They encourage more comments like it",
          "The comment was deleted, showing the writer does not approve of it."),
      ])

    R("wr_net", "Writing an Online Safety Reminder", 11, 3,
      "Choose a sentence for an online safety reminder based on its key points.", "rw_write", [
        q("Key points: do not post passwords, protect privacy, and the rude comment has been deleted. Which sentence includes all three?",
          "Do not post your password, protect your privacy, and the rude comment has been deleted",
          "Do not post your password", "Privacy matters", "The blog is new",
          "All three key points must be included."),
        q("A reminder describes a rule that has applied from March until now. Which tense is appropriate?", "The rule has been used since March",
          "The rule was used since March", "The rule is used since March", "The rule has used since March",
          "Use the present perfect with since March; because the rule receives the action, use has been used."),
        q("Which sentence is suitable as the reminder's title?", "Keep your identity safe online",
          "Keep your iedntity safe online", "Keep your identtiy safe online", "Keep your idntity safe online",
          "Keep your identity safe online works as a title."),
        q("Which sentence correctly uses the present perfect passive?", "The photo has been removed",
          "The photo has been remove", "The photo has being removed", "The photo have been removed",
          "Use has been + the past participle removed."),
      ])

    V("vo_hist", "History and Traditions", 11, 4,
      "Recognize tradition, castle, battle, and kingdom.",
      [("tradition", "long-established practice"), ("battle", "fight between armies"), ("kingdom", "country ruled by a king or queen"), ("custom", "traditional practice")], "vo_soc")

    V("vo_trad", "Festival Customs", 11, 4,
      "Recognize ancestor, honour, gathering, and poem.",
      [("ancestor", "person from whom someone is descended"), ("honour", "show respect for or remember"), ("gathering", "meeting of people"), ("poem", "piece of writing in verse")], "vo_soc")

    G("gr_ppattr", "Past Participles as Modifiers and Complements", 11, 4,
      "Use past participles as modifiers or subject complements to express a passive meaning or a completed action.", "pp", [
        q("A ___ castle means a castle that has been destroyed. Which form completes the phrase?", "ruined",
          "ruining", "ruin", "ruins", "Use the past participle ruined as a modifier for a castle that has been destroyed."),
        q("The gate is ___. It is closed. Which form completes the sentence?", "closed",
          "closing", "close", "closes", "Use the past participle closed as a subject complement to describe a state."),
        q("Which sentence is correct?", "The poem written by Li Bai is famous",
          "The poem writing by Li Bai is famous", "The poem wrote by Li Bai is famous",
          "The poem write by Li Bai is famous",
          "Written by Li Bai modifies poem."),
        q("The visitors were ___ by the old custom. Which form completes the sentence?", "surprised",
          "surprising", "surprise", "surprises", "Use surprised as a subject complement for how people feel."),
      ])

    G("gr_ppcomp", "Past Participles as Object Complements", 11, 4,
      "Use a past participle as an object complement to describe what was done to the object.", "pp", [
        q("I heard my name ___. My name was called. Which form completes the sentence?", "called",
          "calling", "call", "to calling", "The name receives the action, so use called as the object complement."),
        q("She found the window ___. The window had been broken. Which form completes the sentence?", "broken",
          "breaking", "broke", "break", "The window receives the action, so use broken."),
        q("Which sentence is correct?", "We saw the hall decorated with poems",
          "We saw the hall decorating with poems", "We saw the hall decorate with poems",
          "We saw the hall to decorated with poems",
          "The hall receives the action, so use decorated as the object complement."),
        q("They kept the tradition ___. The tradition was preserved. Which form completes the sentence?", "preserved",
          "preserving", "preserve", "to preserving", "The tradition receives the action, so use preserved."),
      ])

    F("fu_hist", "Discussing Traditions", 11, 4,
      "Describe a tradition and say whether you support keeping it.", "fu_view", [
        q("You want to describe the Qingming custom of remembering ancestors. Which sentence is suitable?", "On Qingming people honour their ancestors",
          "On Qingming people honour their acnestors", "On Qingming people honour their ancestros", "On Qingming people honour their anestors",
          "Honour their ancestors describes the custom."),
        q("You want to say that this poem was written by Li Bai. Which sentence is suitable?", "This is a poem written by Li Bai",
          "This is a poem writing by Li Bai", "This is a poem wrote by Li Bai", "Poem is written Li Bai by",
          "Use written by as a modifier."),
        q("You want to say that you support keeping this gathering. Which sentence is suitable?", "I support keeping this gathering",
          "I support eating the tradition", "I support keeping this gtahering", "I support keeping this gathernig",
          "Use I support keeping to state your view."),
        q("Someone asks whether you saw the decorated hall. Which answer is correct?", "Yes, I saw the hall decorated with flowers",
          "Yes, I saw the hall decorating with flowers", "Yes, I saw the hall decorate flowers",
          "Yes, decorated saw I the hall",
          "Use decorated as an object complement to show that the hall received the decoration."),
      ])

    _d = "During the festival, families hold a gathering to honour their ancestors. A poem written by a local teacher is read aloud. Last year the old hall was decorated with paper flowers."
    R("rw_hist", "Reading about Traditions", 11, 4,
      "Read about a tradition and identify the purpose of the gathering and how the hall was decorated.", "rw_detail", [
        q(_d + " What is the gathering for?", "To honour ancestors", "To celebrate a competition", "To restore the city wall", "To publish a blog", "The passage says the gathering is to honour their ancestors."),
        q(_d + " Who wrote the poem?", "A local teacher", "Li Bai", "A visitor", "No author is given", "The passage says it was written by a local teacher."),
        q(_d + " What happened to the hall last year?", "It was decorated with paper flowers", "It was destroyed by rain", "It was turned into a stadium", "There was no hall",
          "The passage says it was decorated with paper flowers."),
        q(_d + " Which sentence agrees with the passage?", "Families honour their ancestors",
          "The poem was written by Li Bai", "The hall is a new stadium", "There is no gathering",
          "The passage says that families honour their ancestors."),
      ])

    R("wr_hist", "Writing about a Tradition", 11, 4,
      "Choose a sentence introducing a tradition based on its key points.", "rw_write", [
        q("Key points: the gathering honours ancestors, a poem by a local teacher is read aloud, and the hall is decorated with paper flowers. Which sentence includes all three?",
          "Families gather to honour ancestors, read a poem written by a local teacher, and the hall is decorated with paper flowers",
          "Families gather", "The poem is short", "Paper flowers are red",
          "All three key points must be included."),
        q("You want to use a past participle as a modifier. Which sentence is correct?", "The custom kept by the village is old",
          "The custom keeping by the village is old", "The custom keep by the village is old",
          "The custom to kept by the village is old",
          "Kept by the village modifies custom."),
        q("Which sentence is suitable as the opening of an introduction?", "Let me tell you about a local tradition",
          "Let me tell you about an local tradition", "Let me tell you about a local tardition", "Let me tell you about a local traditoin",
          "Let me tell you about is a suitable opening."),
        q("Which sentence uses an object complement correctly?", "We found the door closed",
          "We found the door closing by nobody", "We found the door close", "We found closed the door was",
          "The door receives the action, so use closed as the object complement."),
      ])

    V("vo_musicb", "Music", 11, 5,
      "Recognize classical, band, perform, and audience.",
      [("classical", "relating to a traditional style of music"), ("band", "group of musicians"), ("perform", "play music or act before an audience"), ("audience", "people watching or listening")], "vo_world")

    V("vo_band", "Performing Music", 11, 5,
      "Recognize instrument, stage, rhythm, and composer.",
      [("instrument", "object used to make music"), ("stage", "raised area where performers appear"), ("rhythm", "pattern of beats in music"), ("composer", "person who writes music")], "vo_world")

    G("gr_ingattr", "-ing Forms as Modifiers and Subject Complements", 11, 5,
      "Use an -ing form as a modifier or subject complement to show an active meaning or a quality of a thing.", "ing", [
        q("A ___ band means a band that is performing now. Which form completes the phrase?", "performing",
          "performed", "perform", "to performing", "Use performing as a modifier for a band that is performing now."),
        q("The news is ___. The news makes people excited. Which form completes the sentence?", "exciting",
          "excited", "excite", "excites", "Use exciting as a subject complement to describe the quality of the news."),
        q("Which sentence is correct?", "The smiling audience loved the song",
          "The smiled audience loved the song", "The smile audience loved the song",
          "The audience smiling loved are the song",
          "Smiling modifies audience and describes people with smiles on their faces."),
        q("Her job is ___ the stage. Her job is to arrange the stage. Which form completes the sentence?", "designing",
          "designed", "design", "to designed", "Use designing after is to describe what the job involves."),
      ])

    G("gr_ingadv", "-ing Forms as Adverbials and Object Complements", 11, 5,
      "Use an -ing form as an adverbial or object complement to express an active meaning.", "ing", [
        q("___ the violin, she walked onto the stage. Which form completes the sentence?", "Playing",
          "Played", "Play", "To played", "She plays the violin, so use Playing in the adverbial phrase."),
        q("I heard someone ___ in the hall. I heard someone singing. Which form completes the sentence?", "singing",
          "sung", "sang", "to singing", "Someone is doing the singing, so use singing as the object complement."),
        q("Which sentence is correct?", "He sat in the audience, listening carefully",
          "He sat in the audience, listened carefully", "He sat in the audience, listen carefully",
          "Listening carefully, the song was beautiful",
          "He is the one listening; the song cannot be the subject of listening."),
        q("We watched the band ___. We watched the band performing. Which form completes the sentence?", "performing",
          "performed", "perform", "to performed", "The band performs the action, so use performing as the object complement."),
      ])

    P("ph_linkhs", "Linking within Sense Groups", 11, 5,
      "Recognize linking between a word ending in a consonant and one beginning with a vowel.", "link", [
        q("In “an old instrument,” which two words are most likely to link?", "an and old",
          "The final sounds of old and instrument", "Two consonants within instrument", "No words",
          "An ends in a consonant and old begins with a vowel, so the words can link."),
        q("In “look at it,” where does a consonant link to a vowel?", "The /k/ at the end of look links to at",
          "You must pause after the /t/ in at because no vowel follows", "It begins with a consonant, so linking is impossible", "Stress and separate all three words",
          "The final consonant in look can link to the vowel at the start of at."),
        q("Which phrase is best for practicing linking?", "stand up", "big drums", "classical music", "six bands",
          "Stand ends in a consonant and up begins with a vowel. The other adjacent sounds are mostly consonant-to-consonant."),
        q("Where does linking mainly occur?", "Between a final consonant in one word and an initial vowel in the next",
          "Above every vowel letter", "After a period", "Between commas, where a pause is required",
          "Linking connects the final consonant of one word to the initial vowel of the next."),
      ])

    P("ph_ploshs", "Incomplete Release of Stop Consonants", 11, 5,
      "Recognize incomplete release when the first of two adjacent stop consonants is formed but not fully released.", "link", [
        q("In “a big band,” which sound is often not fully released?", "The /g/ at the end of big",
          "A vowel in band", "The vowel in a", "No sound",
          "The /g/ in big and /b/ in band are both stop consonants; the first is often not fully released."),
        q("Which pair contains adjacent stop consonants?", "good time", "my audience", "high note", "old stage",
          "The /d/ in good and /t/ in time are adjacent stop consonants."),
        q("What usually happens to the first stop consonant during incomplete release?", "The mouth forms it, but the airflow is not fully released",
          "It must be pronounced for extra time", "It changes into a vowel", "The whole word is deleted",
          "The first stop is often formed by blocking the airflow but is not fully released."),
        q("In “sit down,” which sound is most likely to be incompletely released?", "The /t/ at the end of sit",
          "A vowel in down", "The vowel in sit", "The /n/ at the end of down",
          "The /t/ is followed immediately by /d/ in down and is often not fully released."),
      ])

    F("fu_music", "Talking about a Performance", 11, 5,
      "Describe a performance and suggest going to hear it together.", "fu_plan", [
        q("You want to say that the band is performing on stage now. Which sentence is suitable?", "The band is performing on the stage",
          "The band is performed on the stage", "The band is perform on the stage", "The band is performnig on the stage",
          "The band performs the action, so use is performing."),
        q("You want to invite a classmate to a classical concert. Which sentence is suitable?", "Shall we go to the classical concert",
          "Shall we go to the calssical concert", "Shall we go to the classiacl concert", "We went tomorrow",
          "Use Shall we go to invite someone."),
        q("You want to describe the audience smiling as they listen. Which sentence is suitable?", "The audience sat there, smiling",
          "The audience sat there, smiled", "The aduience sat there, smiling", "The audiecne sat there, smiling",
          "Smiling is an adverbial whose logical subject is the audience."),
        q("You want to say that the rhythm makes the show exciting. Which sentence is suitable?", "The rhythm made the show exciting",
          "The rhythm made the show excited", "Exciting made the rhythm a person", "Show is exciting made",
          "Use exciting for the quality of the show, not excited for a person's feeling."),
      ])

    _u = "A student band is performing on the stage. The audience is listening, clapping at the end of each song. The composer of the last piece is a teacher at the school."
    R("rw_music", "Reading about a Performance", 11, 5,
      "Read about a performance and summarize what the audience is doing and whether the writer is simply describing it.", "rw_main", [
        q(_u + " Who is performing on stage?", "A student band", "The composer alone", "The audience", "The teacher's choir",
          "The passage says a student band is performing."),
        q(_u + " What does the audience do at the end of each song?", "Clap", "Leave", "Write poems", "Repair instruments",
          "The passage says they clap."),
        q(_u + " Who composed the last piece?", "A teacher at the school", "A student", "No composer is mentioned", "A visitor in the audience",
          "The passage says the composer is a teacher at the school."),
        q(_u + " What is the passage mainly doing?", "Describing the performance as it happens", "Criticizing the band", "Hiring hunters", "Arguing against classical music",
          "The passage simply describes the performance and the audience."),
      ])

    R("wr_music", "Writing a Performance Notice", 11, 5,
      "Choose a sentence for a performance notice based on its key points.", "rw_write", [
        q("Key points: a student band, a Friday performance on stage, and an on-time arrival for the audience. Which sentence includes all three?",
          "The student band is performing on the stage on Friday, and the audience should arrive on time",
          "The student band is performing", "Friday is busy", "Please be quiet",
          "All three key points must be included."),
        q("Which sentence correctly uses an -ing adverbial to describe entering the hall?", "Entering the hall, please keep quiet",
          "Entered the hall, please keep quiet", "The hall entering, please keep quiet",
          "Keep quiet, the door entering",
          "The understood subject of Entering should be the person being addressed."),
        q("Which sentence is suitable as the notice title?", "Student band on stage this Friday",
          "Sutdent band on stage this Friday", "Studnet band on stage this Friday", "Stdent band on stage this Friday",
          "Student band on stage this Friday works as a title."),
        q("Which sentence uses an -ing form as a modifier?", "The performing band needs two more players",
          "The performed band needs two more players", "The band performing needs are players two",
          "Needs the band performing players",
          "Performing modifies band and means the band is performing."),
      ])
