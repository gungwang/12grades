# -*- coding: utf-8 -*-
"""People's Education Press (2019), Selective Compulsory, Book 4. Unit titles follow the commonly used table of contents; the volume assignment needs verification."""
from enh_tx import V, P, G, F, R, q


def load():
    V("vo_fiction", "Science Fiction", 16, 1,
      "Recognize fiction, android, clone, and alien.",
      [("fiction", "a work of fiction"), ("android", "humanoid robot"), ("clone", "clone"), ("alien", "extraterrestrial")], "vo_work")

    V("vo_android", "Future Technology", 16, 1,
      "Recognize spacecraft, gravity, dimension, and experiment.",
      [("spacecraft", "spacecraft"), ("gravity", "gravity"), ("dimension", "dimension"), ("experiment", "experiment")], "vo_work")

    G("gr_nonfinmix", "Choosing Non-finite Forms", 16, 1,
      "Choose to do, doing, or done in context.", "nonfin", [
        q("The android needs ___ before the next flight. It needs someone to check it; which form completes the blank?", "to be checked",
          "to checking", "check", "checked it",
          "Use to be checked after needs to show that the android needs to be checked."),
        q("In which sentence is written used as a modifier?", "The fiction written last year is still popular",
          "The fiction writing last year is still popular", "Written the fiction last year is popular",
          "The fiction to writing last year is popular",
          "Written last year modifies fiction, meaning the story was written last year."),
        q("She remembers ___ the spacecraft door. Which form means she remembers having already closed it?", "closing",
          "to close", "closed it yesterday as a finite verb", "to closing",
          "Remember doing means you recall doing something; remember to do means you remember that you need to do it."),
        q("Which sentence correctly means 'I'm glad to be invited aboard'?", "I am glad to be invited aboard",
          "I am glad to inviting aboard", "I am glad inviting aboard as the whole predicate",
          "I am glad be invited aboard",
          "Use to be invited after glad; it is the passive infinitive."),
      ])

    G("gr_donevs", "Perfect and Passive Non-finite Forms", 16, 1,
      "Distinguish having done, having been done, and being done.", "nonfin", [
        q("___ the experiment, the crew left the lab. The experiment was already complete; which phrase fits the blank?", "Having finished",
          "Having been finished", "Being finished", "Finished by them now",
          "The crew performed the experiment, so use Having finished."),
        q("The clone, ___ in secret for years, was finally found. It had been hidden for years; which phrase completes the sentence?",
          "having been hidden", "having hidden", "hiding the lab", "to hide",
          "The clone was hidden, and this happened before it was found, so use having been hidden."),
        q("Which sentence means that the door is currently being repaired?", "The door being repaired cannot be used",
          "The door having repaired cannot be used", "The door to repairing cannot be used",
          "Repairing the door cannot be used as if the door repairs itself",
          "Being repaired means that the repair is in progress."),
        q("What is the difference between Having been tested twice and being tested?", "The first means it has already been tested; the second means it is being tested.",
          "Both mean a future active action.", "The first is a question, and the second is a subjunctive form.", "Both can only be used as predicates.",
          "Having been tested is perfect passive; being tested is progressive passive."),
      ], "inferred")

    F("fu_scifi", "Discussing a Science-Fiction Plot", 16, 1,
      "Use one or two sentences to say who did what in a science-fiction story and what has been completed.", "fu_argue", [
        q("To say that the android needs to be checked first, which sentence is appropriate?", "The android needs to be checked first",
          "The android needs to checking first", "Checked needs the android", "The android checking needs",
          "Needs to be checked means that the android needs to be checked."),
        q("To say that the crew left after finishing the experiment, which sentence is appropriate?", "Having finished the experiment, the crew left",
          "Having been finished the experiment, the crew left", "The experiment having the crew left",
          "Finished the crew the experiment",
          "The crew performed the action, so use Having finished."),
        q("To say that the story written last year is still popular, which sentence is appropriate?", "The fiction written last year is still popular",
          "The fiction writing last year is still popular", "Written is the fiction popular last",
          "The fiction to writing is popular",
          "Written last year is used as a modifier."),
        q("To remind someone to close the spacecraft door, which has not been done yet, which sentence is appropriate?", "Please remember to close the spacecraft door",
          "Please remember closing the spacecraft door yesterday", "Remember closed the door",
          "To closing remember the door",
          "Use remember to close for something that has not been done yet; use remember closing for something already done."),
      ])

    _sf = "The fiction written in 2019 follows an android. Having finished a gravity experiment, the crew found the clone hidden in the lab. The spacecraft door being repaired cannot open yet."
    R("rw_scifi", "Reading a Science-Fiction Passage", 16, 1,
      "Distinguish who performed the experiment, what has been hidden, and what is being repaired.", "rw_infer", [
        q(_sf + " In what year was the story written?", "2019", "It is being written this year.", "The year the crew left is not given.", "The passage does not give a year.",
          "Written in 2019 shows that it was written in 2019."),
        q(_sf + " What did the crew do before finding the clone?", "They finished a gravity experiment.", "They were repairing the spacecraft door.", "They hid the android.", "They opened the repaired door.",
          "Having finished a gravity experiment happened before they found the clone."),
        q(_sf + " What was the clone's condition at the time?", "It was hidden in the lab.", "It was conducting an experiment.", "It was repairing the door.", "It had left the spacecraft.",
          "The passage says the clone was hidden in the lab."),
        q(_sf + " Why can the spacecraft door not open yet?", "It is being repaired.", "It has already been repaired.", "The crew forgot to do the experiment.", "The story has not been finished.",
          "Being repaired means that the repair is in progress."),
      ])

    R("wr_scifi", "Writing a Science-Fiction Summary", 16, 1,
      "Choose a summary sentence that includes the required points.", "rw_write_s", [
        q("Key points: a story written in 2019, the crew having finished a gravity experiment, and the door being repaired. Which sentence includes all three?",
          "The fiction written in 2019 shows a crew having finished a gravity experiment, while the door is being repaired",
          "The fiction is new", "The crew left", "The door is a door",
          "All three key points must be included."),
        q("Which sentence in the summary says that the clone had been hidden for years?", "The clone, having been hidden for years, was found",
          "The clone, having hidden for years, was found as if it hid itself",
          "The clone being hide was found", "Hidden having the clone was",
          "The clone was hidden, so use having been hidden."),
        q("Which sentence is suitable as the first sentence of the summary?", "This science fiction follows an android on a spacecraft",
          "This science fiction follow an android on a spacecraft", "This science fiction follows an android on an spacecraft", "This science fiction follows an android on a sapcecraft",
          "A summary can begin by introducing the characters and setting."),
        q("Which sentence means that she remembers having already closed the door?", "She remembers closing the door",
          "She remembers to close the door yesterday as a finished act", "She remembers closed the door",
          "Closing remembers she the door",
          "Remembers closing means she remembers doing it."),
      ])

    V("vo_landmark", "Landmarks", 16, 2,
      "Recognize landmark, statue, temple, and tower.",
      [("landmark", "landmark"), ("statue", "statue"), ("temple", "temple"), ("tower", "tower")], "vo_work")

    V("vo_sight", "Places of Interest", 16, 2,
      "Recognize attraction, scenery, guide, and queue.",
      [("attraction", "tourist attraction"), ("scenery", "scenery"), ("guide", "tour guide"), ("queue", "line")], "vo_work")

    G("gr_nomatter", "No Matter and -ever Clauses", 16, 2,
      "Use no matter who or whoever to introduce concessive clauses.", "advcls", [
        q("No matter who the guide is, we leave at nine. Which sentence is correct?", "No matter who the guide is, we leave at nine",
          "No matter who is the guide, we leave at nine", "Whoever the guide is the queue",
          "No matter whom the guide is he, we leave",
          "Who is a subject complement in the clause, so use statement order, the guide is, not question order."),
        q("___ you visit, take a photo of the statue. Which word means 'no matter where you visit'?", "Wherever",
          "Wherever place", "No matter wherever", "Where",
          "Wherever means no matter where. Where alone names a place and does not mean 'no matter where.'"),
        q("Which sentence means the same as No matter what the scenery is?", "Whatever the scenery is, we will stop",
          "What the scenery is, we will stop", "No matter whatever the scenery is",
          "Whatever is the scenery we stop as a question",
          "Whatever can replace no matter what."),
        q("In a concessive clause, what does whoever mean?", "no matter who", "only the person who", "the place where", "because",
          "In concessive clauses, whoever means no matter who."),
      ], "inferred")

    G("gr_wherecls", "Adverbial Clauses with Where", 16, 2,
      "Tell whether where introduces a place adverbial clause or a relative clause modifying a preceding noun.", "advcls", [
        q("In which sentence does where introduce a place adverbial clause?", "Where there is a tower, there is a queue",
          "The tower where we waited is old", "This is the temple where we prayed",
          "The place where we met is quiet",
          "The opening clause Where there is a tower has no antecedent, so it is a place adverbial clause. In the other sentences, where follows a noun."),
        q("Put the statue ___ it can be seen. Which word completes the sentence?", "where",
          "which", "what", "wherever place",
          "Where introduces a place adverbial clause that says to put it somewhere it can be seen."),
        q("In The landmark where we took photos, which word does where modify?", "landmark",
          "the whole sentence; there is no antecedent", "photos", "took",
          "Where immediately follows landmark in a relative clause, not an adverbial clause."),
        q("Where there is a temple, there are visitors. Which sentence is correct?", "Where there is a temple, there are visitors",
          "The temple where there are visitors is where", "Where a temple there is visitors",
          "There is a temple where there, visitors",
          "Where there is a temple is a place adverbial clause."),
      ], "inferred")

    F("fu_sight", "Introducing Places of Interest", 16, 2,
      "Introduce a landmark and explain who may come and where to put things.", "fu_desc", [
        q("To say that the group meets at nine, no matter who the guide is, which sentence is appropriate?", "Whoever the guide is, we meet at nine",
          "Whoever is the guide, we meet at nine as a question order", "No matter whoever the guide",
          "Who the guide is we meet",
          "Whoever the guide is is a concessive clause and uses statement word order."),
        q("To tell visitors to leave their bags where they can see the statue, which sentence is appropriate?", "Leave your bag where you can see the statue",
          "Leave your bag which you can see the statue", "Leave your bag what you can see",
          "Where leave your bag the statue",
          "Where you can see the statue is a place adverbial clause."),
        q("To introduce the tower as a city landmark, which sentence is appropriate?", "The tower is a landmark of the city",
          "The tower are a landmark of the city", "The tower is an landmark of the city", "The tower is a lnadmark of the city",
          "Use is a landmark to introduce the landmark."),
        q("To say that the group will stop whatever the scenery is like, which sentence is appropriate?", "Whatever the scenery is, we will stop",
          "What the scenery is we stop", "No matter whatever we stop", "Scenery is whatever stop",
          "Whatever the scenery is means no matter what the scenery is like."),
      ])

    _sg = "Where there is a tower, visitors queue for photos. Whoever the guide is, the group meets at the statue. The temple where they prayed is older than the tower."
    R("rw_sight", "Reading About Places of Interest", 16, 2,
      "Distinguish place adverbial clauses from relative clauses that modify nouns.", "rw_infer", [
        q(_sg + " Where do visitors queue to take photos?", "Where there is a tower", "Only inside the temple", "At the guide's home", "The passage does not say where they queue.",
          "The passage says, Where there is a tower, visitors queue."),
        q(_sg + " Where does the group meet?", "At the statue", "At the top of the tower", "At any temple", "They do not meet.",
          "The group meets at the statue."),
        q(_sg + " In the phrase the temple where they prayed, what does where modify?", "temple", "the whole sentence as a place adverbial", "tower", "visitors",
          "Where follows temple, so it introduces a relative clause."),
        q(_sg + " If the guide changes, does the meeting time change?", "No. The group meets at the statue no matter who the guide is.", "Yes, they meet at the tower.", "The passage says the meeting is canceled.", "Only the original guide can meet the group.",
          "Whoever the guide is means no matter who the guide is."),
      ])

    R("wr_sight", "Writing a Visitor Guide", 16, 2,
      "Choose a visitor-guide sentence that includes the required points.", "rw_write_s", [
        q("Key points: people queue when there is a tower; the group meets at the statue no matter who the guide is; the temple where they prayed is older. Which sentence includes all three?",
          "Where there is a tower people queue, whoever the guide is the group meets at the statue, and the temple where they prayed is older",
          "The tower is tall", "People like photos", "The temple is old",
          "All three key points must be included."),
        q("Which sentence tells visitors to keep their ticket somewhere they can see it?", "Keep the ticket where you can see it",
          "Keep the ticket which you can see it", "Keep the ticket what you can see",
          "Where keep the ticket you",
          "Where you can see it is a place adverbial clause."),
        q("Which sentence is suitable as the first sentence of the visitor guide?", "This walk starts at the city landmark",
          "This walk start at the city landmark", "This walk starts at the city lnadmark", "This walk starts at the city landmrak",
          "A guide can begin by stating the starting point."),
        q("Which sentence means 'take a photo whatever the scenery is like'?", "Whatever the scenery is, take a photo",
          "What the scenery is, take a photo", "No matter whatever take a photo", "Scenery whatever is take",
          "Whatever the scenery is means no matter what the scenery is like."),
      ])

    V("vo_ocean", "The Ocean", 16, 3,
      "Recognize ocean, voyage, harbour, and tide.",
      [("ocean", "ocean"), ("voyage", "voyage"), ("harbour", "harbor"), ("tide", "tide")], "vo_work")

    V("vo_voyage", "Voyaging", 16, 3,
      "Recognize sailor, compass, storm, and anchor.",
      [("sailor", "sailor"), ("compass", "compass"), ("storm", "storm"), ("anchor", "anchor")], "vo_work")

    G("gr_advconc", "Concession and Contrast with Although and While", 16, 3,
      "Use although or while to express concession and contrast.", "advcls", [
        q("Although there was a storm, the sailors still set out. Which sentence is correct?", "Although there was a storm, the sailors set out",
          "Although there was a storm, but the sailors set out", "Although a storm, the sailors set out",
          "Despite although the storm, sailors set",
          "Do not use but with although."),
        q("While the tide was high, ___ . Which phrase means that the ship stayed in the harbor despite the high tide?",
          "the ship stayed in the harbour", "but the ship stayed in the harbour", "so the ship stayed and although",
          "stayed the ship although",
          "Here while expresses concession, so the main clause is the ship stayed, without but."),
        q("Which sentence uses while to express contrast?", "The compass worked, while the radio failed",
          "While the compass worked, but the radio failed", "The compass worked while but the radio",
          "While compass, radio failed but",
          "While connects contrasting ideas."),
        q("How should although and but be used together?", "Do not add but when you use although.", "They must always appear together.", "Put but before although.",
          "Although can modify only a noun.",
          "Although already expresses contrast, so do not add but."),
      ])

    G("gr_advso", "So That and In Case", 16, 3,
      "Use so that to express purpose and in case to mean 'as a precaution.'", "advcls", [
        q("They left early so they could catch the tide. Which sentence is correct?", "They left early so that they could catch the tide",
          "They left early so that they can caught the tide", "They left early in case they could catch the tide as their purpose only",
          "So that they left early catch the tide",
          "So that they could catch expresses purpose."),
        q("Take a compass ___ you get lost. Which phrase means 'as a precaution in case you get lost'?", "in case",
          "so that", "although", "while",
          "In case means 'as a precaution'; so that expresses a purpose."),
        q("Which sentence expresses a purpose rather than a precaution?", "She checked the anchor so that the ship would not drift",
          "She checked the anchor in case the ship drifted", "Although she checked the anchor, it held",
          "While she checked the anchor, he watched",
          "So that the ship would not drift states a purpose. In case prepares for the ship actually drifting."),
        q("What does a clause introduced by in case mainly express?", "a precaution against something that may happen", "a reason that has already occurred", "concession, like although", "a relative clause",
          "In case means 'as a precaution.'"),
      ])

    F("fu_sea", "Explaining a Voyage Plan", 16, 3,
      "Explain that a voyage will go ahead despite bad weather, its purpose, and what precautions are being taken.", "fu_desc", [
        q("To say that the group will set out despite a storm, which sentence is appropriate?", "Although there is a storm, we will set out",
          "Although there is a storm, but we will set out", "Despite although the storm we set",
          "Although storm we but set",
          "Do not use but with although."),
        q("To say that the group leaves early in order to catch the tide, which sentence is appropriate?", "We leave early so that we can catch the tide",
          "We leave early in case we can catch the tide", "So that we leave early catch",
          "We leave early although we can catch the tide",
          "So that expresses purpose."),
        q("To remind someone to take a compass in case they get lost, which sentence is appropriate?", "Take a compass in case you get lost",
          "Take a compass so that you get lost", "Take a compass although you get lost",
          "In case take a compass you lost",
          "In case you get lost expresses a precaution against getting lost."),
        q("To contrast the working compass with the failed radio, which sentence is appropriate?", "The compass works, while the radio has failed",
          "The compass works, while but the radio has failed", "While the compass works but the radio",
          "The compass works although but the radio failed",
          "While can express contrast; do not add but."),
      ])

    _sea = "Although the storm was close, the sailors left harbour early so that they could catch the tide. They took a compass in case the radio failed. The anchor held, while the small boat did not."
    R("rw_sea", "Reading About a Voyage", 16, 3,
      "Identify the concession, purpose, and precaution in the passage.", "rw_infer", [
        q(_sea + " What did the sailors do as the storm approached?", "They left the harbor early anyway.", "They stayed in the harbor.", "They threw away the compass.", "Only the small boat set out.",
          "Although the storm was close, the sailors left."),
        q(_sea + " Why did they leave early?", "To catch the tide.", "In case the radio failed.", "Because the anchor broke.", "To contrast the small boat.",
          "So that they could catch the tide states the purpose."),
        q(_sea + " Why did they take a compass?", "As a precaution in case the radio failed.", "To catch the tide.", "To make the small boat fail.", "Because the storm had ended.",
          "They took a compass in case the radio failed."),
        q(_sea + " Which two things are contrasted by while?", "The anchor held, but the small boat did not.", "The storm and the tide.", "The compass and the harbor.", "The sailors and the radio's purpose.",
          "The passage says, The anchor held, while the small boat did not."),
      ])

    R("wr_sea", "Writing a Voyage Memo", 16, 3,
      "Choose a memo sentence that includes the required points.", "rw_write_s", [
        q("Key points: leave the harbor despite the storm, leave early to catch the tide, and take a compass in case the radio fails. Which sentence includes all three?",
          "Although a storm was close they left so that they could catch the tide, and they took a compass in case the radio failed",
          "They left the harbour", "The tide was high", "They had a compass",
          "All three key points must be included."),
        q("Which sentence in the memo says that the anchor held but the small boat did not?", "The anchor held, while the small boat did not",
          "The anchor held, while but the small boat did not", "Although the anchor held, but the boat did not",
          "While the anchor held but the boat",
          "While expresses contrast; do not add but."),
        q("Which sentence is suitable as the first sentence of the memo?", "Check the tide before the voyage",
          "Check the tide before the vyoage", "Check the tide before the voygae", "Check the tide before the voage",
          "A memo can begin with something that needs to be checked."),
        q("Which sentence means 'start early so that you can see the route'?", "Start early so that you can see the route",
          "Start early in case you can see the route as your only purpose", "Start early although you can see the route",
          "So that start early you see",
          "So that you can see expresses purpose."),
      ])

    V("vo_donate", "Community Giving", 16, 4,
      "Recognize donate, volunteer, charity, and share.",
      [("donate", "donate"), ("volunteer", "volunteer"), ("charity", "charity"), ("share", "share")], "vo_work")

    V("vo_community", "Community Service", 16, 4,
      "Recognize community, shelter, fundraising, and neighbour.",
      [("community", "community"), ("shelter", "shelter"), ("fundraising", "fundraising"), ("neighbour", "neighbor")], "vo_work")

    G("gr_mixcls", "Appositive and Relative Clauses", 16, 4,
      "Distinguish appositive clauses from relative clauses introduced by that.", "nouncls", [
        q("In which sentence does that introduce an appositive clause?", "The news that the shelter will open spread quickly",
          "The shelter that opened last year is small", "The volunteer that we met is kind",
          "The charity that raised money is local",
          "The that-clause after news explains the content of the news; that has no grammatical role in the clause. In the other sentences, that is the subject or object of a relative clause modifying a noun."),
        q("The fact ___ more neighbours donated money surprised us. Which word completes the sentence?", "that",
          "which", "what", "whose",
          "Use that after fact to introduce an appositive clause explaining the fact."),
        q("In The book that you donated, what is the grammatical role of that?", "object", "it only links an appositive clause and has no role", "subject", "adverbial",
          "Donated needs an object, and that refers to book, so this is a relative clause."),
        q("Which nouns are more commonly followed by appositive clauses?", "content nouns such as news, fact, and idea", "only who modifying a person", "where as a place adverbial",
          "than in a comparative",
          "An appositive clause explains the specific content of news, fact, or idea."),
      ])

    G("gr_whatnom", "Noun Clauses with What", 16, 4,
      "Use what to introduce subject or object clauses, with what serving a grammatical role inside the clause.", "nouncls", [
        q("___ the volunteers need is more blankets. Which word completes the sentence?", "What",
          "That", "Which", "Whatever the thing",
          "The clause is missing an object, so use What. A subject clause introduced by That is not missing a grammatical element."),
        q("She asked ___ we could share. Which word means 'the thing that we could share'?", "what",
          "that", "which the blankets", "what that",
          "The object clause after asked is missing the object of share, so use what."),
        q("In which sentence does what act as the subject of its clause?", "What surprised the neighbours was the fundraising",
          "That surprised the neighbours was the fundraising", "What the neighbours surprised was",
          "The news what surprised them was true",
          "In What surprised the neighbours, what is the subject of the clause. What cannot introduce an appositive clause after news."),
        q("What is the main difference between what and that when they introduce noun clauses?", "what has a grammatical role in the clause, while that does not",
          "what can never be the subject", "that must be the object", "both can introduce only relative clauses",
          "What has meaning and a grammatical role; that only connects the clauses."),
      ])

    F("fu_share", "Planning a Community Event", 16, 4,
      "Explain the content of a news item and say what volunteers need.", "fu_plan_s", [
        q("To report the news that the shelter will open, which sentence is appropriate?", "The news that the shelter will open is true",
          "The news which the shelter will open is true", "The news what the shelter will open is true",
          "That the news the shelter will open",
          "Use a that-clause after news, not what or which."),
        q("To say that blankets are what the volunteers need, which sentence is appropriate?", "What the volunteers need is blankets",
          "That the volunteers need is blankets", "What need the volunteers is blankets",
          "The fact what they need is blankets",
          "What the volunteers need is a subject clause, with what as the object of need."),
        q("To ask a neighbour to help on Saturday, which sentence is appropriate?", "Could you volunteer on Saturday",
          "Could you volunteer in Saturday", "Could you vlounteer on Saturday", "Could you vounteer on Saturday",
          "Could you volunteer is a polite way to make a request."),
        q("To say that the rapid growth of the fundraiser surprised people, which sentence is appropriate?", "The fact that the fundraising grew so fast surprised us",
          "The fact which the fundraising grew so fast surprised us", "The fact what grew surprised",
          "Fact that the surprised fundraising",
          "Use a that-clause after fact to explain what happened."),
      ])

    _sh = "The news that the shelter will open on Saturday surprised the neighbours. What the volunteers need is blankets. The charity that organised the fundraising thanked every donor."
    R("rw_share", "Reading About Community Giving", 16, 4,
      "Distinguish clauses that explain news content from clauses that modify nouns.", "rw_infer", [
        q(_sh + " What news surprised the neighbours?", "The shelter will open on Saturday.", "The volunteers do not need blankets.", "The charity did not fundraise.", "The passage contains no news.",
          "The news is that the shelter will open."),
        q(_sh + " What do the volunteers need?", "Blankets", "A new tower", "A compass", "More news clauses",
          "What the volunteers need is blankets."),
        q(_sh + " In The charity that organised the fundraising, what kind of clause is that?", "a relative clause", "an appositive clause", "a subject clause", "a place adverbial clause",
          "That refers to charity and acts as the subject of organised, so it introduces a relative clause."),
        q(_sh + " What does the that-clause after news do?", "It explains the content of the news.", "It modifies the word Saturday.", "It replaces blankets.", "It expresses concession.",
          "That the shelter will open is an appositive to news."),
      ])

    R("wr_share", "Writing a Volunteer Notice", 16, 4,
      "Choose a notice sentence that includes the required points.", "rw_write_s", [
        q("Key points: the shelter opens Saturday, volunteers need blankets, and the charity that organized the fundraiser gives thanks. Which sentence includes all three?",
          "The news is that the shelter opens on Saturday, what the volunteers need is blankets, and the charity that organised the fundraising says thank you",
          "The shelter opens", "Blankets are useful", "The charity is kind",
          "All three key points must be included."),
        q("Which sentence in the notice correctly states the content of a fact?", "The fact that we still need coats should be shared",
          "The fact which we still need coats should be shared", "The fact what we need coats should",
          "Fact that should coats",
          "Use a that-clause after fact as an appositive."),
        q("Which sentence is suitable as the first sentence of the notice?", "We need volunteers for the community shelter",
          "We needs volunteers for the community shelter", "We need vlounteers for the community shelter", "We need volunteres for the community shelter",
          "A notice can begin by stating who is needed."),
        q("Which sentence means 'what they shared helped the shelter'?", "What they shared helped the shelter",
          "That they shared helped the shelter", "What helped they shared the shelter",
          "The news what they shared helped",
          "What they shared is the subject, and what is the object of shared."),
      ])

    V("vo_career", "Career Planning", 16, 5,
      "Recognize career, applicant, interview, and qualification.",
      [("career", "career"), ("applicant", "applicant"), ("interview", "interview"), ("qualification", "qualification")], "vo_work")

    V("vo_resume", "Application Materials", 16, 5,
      "Recognize résumé, reference, deadline, and employ.",
      [("résumé", "résumé"), ("reference", "letter of reference"), ("deadline", "deadline"), ("employ", "employ")], "vo_work")

    G("gr_tensemix", "Choosing Tenses in Context", 16, 5,
      "Choose between the simple past, present perfect, and simple future in a narrative.", "mix", [
        q("She ___ three interviews since Monday, and the next one is on Friday. Which form completes the sentence?", "has had",
          "had", "will have", "is having had",
          "Since Monday refers to a period continuing to the present, use the present perfect has had."),
        q("By the time the deadline arrived, she ___ the résumé. It had already been sent before the deadline; which form completes the sentence?",
          "had sent", "has sent", "sends", "will send",
          "Arrived is in the past, and the sending happened earlier, so use had sent."),
        q("Which sentence uses a tense that matches its time expression?", "I have worked here since June",
          "I have worked here in June 2019", "I work here since June", "I had worked here since June now",
          "Since June continues to the present, use the present perfect. In June 2019 refers to a completed point in the past, so do not use have worked."),
        q("The interview is next Friday. Which sentence is correct?", "The interview will take place next Friday",
          "The interview took place next Friday", "The interview has taken place next Friday",
          "The interview takes place next Friday as a finished past event",
          "Next Friday is in the future, so use will take place."),
      ])

    G("gr_provided", "Conditions with Provided That", 16, 5,
      "Use provided that to mean 'as long as a condition is met.'", "advcls", [
        q("They will review your résumé as long as you submit it before the deadline. Which sentence is correct?",
          "They will read it provided that you send it before the deadline",
          "They will read it provided that you sent it before the deadline next week",
          "Provided that you will send it, they read it yesterday",
          "They read it provided what you send",
          "Provided that introduces a condition. With a future main clause, use the present-tense send in the condition clause."),
        q("You can get the job ___ you pass the interview. Which phrase means 'as long as you pass'?", "provided that",
          "so that", "although", "in case",
          "Provided that means 'as long as'; so that expresses purpose, although expresses concession, and in case expresses precaution."),
        q("Which sentence makes having two references a condition?", "We will employ her provided that she has two references",
          "We employed her provided that she has two references next year",
          "Provided that she had two references, we employ her yesterday",
          "We employ her so that she has two references",
          "Provided that she has two references states the condition for employing her."),
        q("Which phrase is closest in meaning to provided that?", "as long as", "although", "so that", "in case",
          "Provided that means 'as long as.'"),
      ], "inferred")

    P("ph_weak", "Weak Forms of Function Words", 16, 5,
      "Recognize that articles, prepositions, and conjunctions are often unstressed in sentences.", "weak", [
        q("In bread and butter, how is and usually pronounced in connected speech?", "unstressed, with a reduced vowel", "strongly stressed and lengthened", "with a rising question intonation", "unconnected to the words around it",
          "And is a function word and is often unstressed in a sentence."),
        q("Which type of words is more often unstressed?", "articles, prepositions, conjunctions, and auxiliary verbs", "all content nouns in a sentence", "people's names", "lexical verbs at the end of a sentence",
          "Function words are often unstressed, while content words usually retain stress."),
        q("In I want to apply, how is to usually pronounced when unstressed?", "as the reduced form /tə/", "with the long vowel in two", "with strong stress, like toe", "omitted and replaced by rising intonation",
          "When unstressed, the vowel in to is often reduced to /ə/."),
        q("To emphasize that this is the application in question, which word can be stressed?", "this, rather than stressing of", "only of", "only a", "and the most",
          "The emphasis falls on the content word this; the function words of and a can remain unstressed."),
      ])

    F("fu_job", "Discussing a Job Application", 16, 5,
      "Describe application steps already completed, what comes next, and conditions set by the employer.", "fu_plan_s", [
        q("To say that you have had three interviews since Monday, which sentence is appropriate?", "I have had three interviews since Monday",
          "I had three interviews since Monday", "I have three interviews since Monday as a past point",
          "I will have three interviews since Monday",
          "Since Monday continues to the present, so use have had."),
        q("To say that the résumé will be reviewed as long as it is submitted before the deadline, which sentence is appropriate?",
          "They will read it provided that you send it before the deadline",
          "They read it yesterday provided that you will send it", "Provided that send you, they will read",
          "They will read it although you send it before the deadline",
          "Provided that you send it means 'as long as you send it.'"),
        q("To politely ask whether you can have an interview before Friday, which sentence is appropriate?", "Could I come for an interview before Friday",
          "Could I come for an itnerview before Friday", "Could I come for an interveiw before Friday", "Could I come for an inerview before Friday",
          "Could I come is a polite way to ask about arrangements."),
        q("To say that the résumé had been sent before the deadline arrived, which sentence is appropriate?", "I had sent the résumé before the deadline arrived",
          "I have sent the résumé before the deadline arrived", "I send the résumé before the deadline arrived",
          "I will send the résumé before the deadline arrived",
          "The résumé was sent before arrived, so use had sent."),
      ])

    _job = "Lin has had two interviews since Monday. She had sent her résumé before the deadline arrived. The company will employ her provided that the references arrive this week. The next interview will take place on Friday."
    R("rw_job", "Reading About a Job Posting", 16, 5,
      "Identify which application steps are complete and which still depend on a condition.", "rw_argue", [
        q(_job + " How many interviews has Lin had since Monday?", "Two", "Three, and they are all in the future.", "None", "The passage does not say how many.",
          "She has had two interviews since Monday."),
        q(_job + " What was the status of the résumé when the deadline arrived?", "It had already been sent.", "It had not been written yet.", "It would be sent on Friday.", "The company refused to accept it.",
          "She had sent her résumé before the deadline arrived."),
        q(_job + " What condition must be met for the company to employ her?", "The references must arrive this week.", "She must write another résumé.", "The interview must be moved to Monday.", "There is no condition.",
          "The condition is that the references arrive this week."),
        q(_job + " When will the next interview take place?", "On Friday", "Before Monday", "It already ended on the deadline.", "The passage does not give a time.",
          "The next interview will take place on Friday."),
      ])

    R("wr_job", "Writing a Job Application Email", 16, 5,
      "Choose an email sentence that includes the required points.", "rw_write_s", [
        q("Key points: two interviews since Monday, the résumé sent before the deadline, and employment provided that the references arrive this week. Which sentence includes all three?",
          "She has had two interviews since Monday, she had sent the résumé before the deadline, and they will employ her provided that the references arrive this week",
          "She had an interview", "The résumé was sent", "References matter",
          "All three key points must be included."),
        q("Which sentence in the email says that the next interview is on Friday?", "The next interview will take place on Friday",
          "The next interview took place on Friday", "The next interview has taken place on Friday",
          "The next interview takes place on Friday last year",
          "Friday is in the future, so use will take place."),
        q("Which sentence is suitable as the first sentence of the email?", "I am writing to apply for the post",
          "I am write to apply for the post", "I am writing to applying for the post", "I am writing to applys for the post",
          "An application email can begin by stating its purpose."),
        q("Which sentence means 'you can start as long as you pass the interview'?", "You can start provided that you pass the interview",
          "You can start so that you pass the interview", "You started yesterday provided that you pass",
          "Provided that you passed, you can start next week as a past failure",
          "Provided that you pass states the condition for starting work."),
      ])
