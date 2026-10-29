# Review of English distractors and curriculum standards

Only the text of incorrect answer choices was changed. Correct answers, option letters, question IDs, prompts, explanations, and `verify` were not changed. Nothing was pushed or deployed.

## Scope of changes

There are 2,779 English multiple-choice questions in total (`cne_p` / `cne_j` / `cne_h`). This pass changed only distractors that were obviously nonsensical and easy to eliminate; options that already resembled plausible learner errors were left unchanged.

| School level | Questions changed | Options changed |
|---|---:|---:|
| Elementary `cne_p` | 0 | 0 |
| Middle school `cne_j` | 3 | 5 |
| High school `cne_h` | 120 | 323 |
| Total | 123 | 328 |

The elementary-school distractors were already plausible errors involving numbers, colors, family terms, or subject–verb agreement, so none were changed. In middle-school questions, only nonsensical options in three questions were changed (`cne_j005_q1`, `cne_j005_q3`, and `cne_j011_q4`). Most changes were in high-school functional expressions and writing prompts, where options such as “The stadium ran me” had accumulated.

The same replacements were made in `data/questions.json` and in the scripts that generate these questions: `scripts/enj_g7a.py` and `scripts/enh_b1.py` through `scripts/enh_s4.py`. This prevents a future rebuild from restoring the old options.

## Editing approach

Distractors use the same sentence structure as the correct answer and contain one typical error: subject–verb agreement, verb form, article use, preposition choice, an extra `to`, an extra `-s` after an infinitive, a near-miss spelling (adjacent letters swapped or one letter missing), or the order of adjacent words. For questions that require specific content points, a grammar-only change might leave all three required points intact and still make the option correct, so one required content word was changed instead. Reading-comprehension options that were grammatical but contradicted the passage were not rewritten into other statements that might also be correct.

No new distractors were created by adding words such as `earthquake`, `ate`, or a noun after `Please`. Collective nouns such as `band` were not changed from `is` to `are` or vice versa, because both forms are accepted.

### Examples

Greetings and responses (middle school and high-school basics):

- `cne_j005_q1`: `I am a book.` → `Nice to meeting you, too.` (incorrect `-ing` after `to`). The existing `Good night.` and `See you yesterday.` were already wrong as a greeting and in tense, so they were left alone.
- `cne_j005_q3`: `Good evening is a book.` / `What is your pen?` / `Sit on the name.` → `Good mornings.` / `Good moning.` / `Good monring.` (pluralization, a missing letter, and two adjacent letters swapped).
- `cne_h005_q1`: `I ate the classroom` → `Hi, my name Lin is`; `Please earthquake the book` → `Hi, my name are Lin`.

Agreement, articles, and prepositions (high school):

- `cne_h005_q3`: `I am in a flood` → `I am at Class 3`; `Class 3 is eating` → `I is in Class 3`.
- `cne_h007_q2`: `You are a new earthquake` → `I is a new student at this school`; another option is `I am an new student at this school`.
- `cne_h015_q3`: `I would liked to join the debate club`, `I would like to joining the debate club`, and `I would to like to join the debate club` (verb form after a modal, `to` + `-ing`, and an extra `to`).

For questions with required content points, changing only the grammar is not enough:

- `cne_h007_q1` requires the name Lin Xiao, Class 3, and a like of music. `Class 3 likes Monday` was changed to `I am Lin Xiao in Class 3, and I like football`. The name and class remain, but music is replaced by football, so one of the three required points is missing. The two existing options that omit required information (`I am Lin Xiao in Class 3` and `I like music and football`) were left unchanged.

Near-miss spelling, used when the sentence has no better grammatical cue:

- `cne_h007_q4`: the three incorrect options for `Hello, let me introduce myself` were changed to `itnroduce`, `introdcue`, and `inroduce`. They remain misspellings of the same word, so the sentence is no longer correct.

Grammatical reading-comprehension statements that simply contradicted the passage were not changed. For example, `The earthquake hit on Monday` in `cne_h035_q4` contradicts a passage that says Friday. The tag question `He is a coach, doesn't he?` is also grammatical rather than nonsensical, so it was left unchanged.

## Spot-checks of standards and volumes

The spot-check covered only entries or volumes marked “pending verification.” The Ministry of Education PDFs were not checked page by page against the original text, so **nothing was changed and no “pending verification” label was removed**.

The following items were checked and match the current mappings:

- People's Education Press (PEP, 2019), Compulsory Volume 1 unit titles. The lesson list on Baidu Baike's “High School English Compulsory Volume 1” page and a 2019 companion workbook's table of contents (`ynmdfz.net`: Welcome Unit, Teenage Life, Travelling Around, Sports and Fitness, Natural Disasters, and Languages Around the World) match the grade 10 `TITLES` in `scripts/enh_build.py`.
- People's Education Press (PEP, 2019), Selective Compulsory Volume 1. The table of contents republished by Linfen Entrance Examination Network on 2022-11-23 lists Unit 1 People of Achievement, Unit 2 Looking into the Future, Unit 3 Fascinating Parks, Unit 4 Body Language, and Unit 5 Working the Land. These match grade 13 in `TITLES`. Courseware titles on 21st Century Education Network use the same unit names.
- People's Education Press New Target (Go for it), Grade 7, Volume 1. Jiaxiwang lists Unit 2 as “This is my sister” and Unit 3 as “Is this your pencil”; Gaili English's Grade 7, Volume 1 lesson page also lists Unit 2 as “This is my sister.” These match `UNITS` in `scripts/enj_build.py`. Some online blogs reverse these two units, but because they conflict with both sources, they were not considered sufficient evidence to change the volume mapping.

The following curriculum-standard entries were reviewed, but this was not sufficient to change their wording or remove the “pending verification” label:

- `ces-2022:1.PH.01` through `1.PH.03`: uppercase and lowercase letters, vowel letters, and closed syllables. They read like public paraphrases, so `verbatim` remains `false`.
- `ces-2017:H.B.GR.01` through `03`: sentence elements, phrases, and tense. These are also paraphrases, not original curriculum-standard text.
- One vocabulary entry for selective-compulsory high school English in `ces-2017` includes science fiction, landmarks, ocean exploration, public service, and career planning in its “standard” wording; the text itself says it is a paraphrase. It looks more like a set of textbook unit themes than a verified curriculum-standard passage. Without the PDF, it cannot be rewritten and presented as the original wording.

Sections 11 and 12 of `docs/standards-mapping.md` already state that these English curriculum standards were not checked page by page. The notes in `enh_build.py` and `enj_build.py` also say the volume mappings are pending verification. These notes were left unchanged.

## Remaining uncertainties

- None of the curriculum-standard sentences above were checked page by page against the Ministry of Education PDFs; `page_or_ref` remains “pending verification.”
- Of the seven high-school volumes, only the unit titles for Compulsory Volume 1 and Selective Compulsory Volume 1 were checked. Grammar-point placement was not checked page by page. The tag-question topic is assigned to Unit 3 of Compulsory Volume 1, but this was not verified against textbook page numbers.
- The unit names for elementary PEP English (starting in Grade 3) appear to follow the common 2012 sequence (Grade 3, Volume 1, from “Hello” to “Happy birthday”). The textbook contents pages were not opened during this pass, so elementary volumes remain pending verification.
- The other middle-school volumes, High School Compulsory Volumes 2 and 3, and Selective Compulsory Volumes 2 through 4 use the same known unit lists; the textbooks were not opened volume by volume.
- Among the 2,779 multiple-choice questions, unchanged distractors only appeared to resemble plausible learner errors during spot-checks. They were not rewritten manually one by one.
- Some high-school distractors use transposed letters (such as `itnroduce`) or swap the last two words. These are not ideal and are more noticeable than genuine collocation errors, but they no longer form another correct sentence.
- A person-agreement error such as `He is in Class 3` is grammatical, but it does not fulfill a prompt asking the student to introduce themselves, so it is not a second correct answer.
