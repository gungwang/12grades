# Question bank guide (`data/questions.json`)

This small question bank for formal topics is used by the `diagnose/` tool, which asks at most two questions per topic. It currently has **828** topics (242 elementary + 315 middle-school + 143 high-school compulsory + 128 high-school selective-compulsory) and **3,459** questions. All school levels use the same question flow. **AI generated all questions and answers; teachers have not reviewed them.** Automated checks and independent review below help check correctness, but they do not make the answers authoritative. High-school questions have only been automatically verified; they have not been independently blind-solved.

Numbers labeled Round 5 in “Statistics” and “Verification methods” below refer only to the 1,407 middle-school questions at that time. See “Elementary questions (2026-10-19)” at the end for the elementary and current whole-bank totals.

## Format

`data/questions.json` is a JSON array with one object per question:

| Field | Required | Description |
|---|---|---|
| `id` | Yes | `<topicId>_q<N>`, for example `cnm_221_q2`. `_q1` is migrated from `diagnostic_question` in `topics.json`; the prompt begins with the original wording, with an answer-format note appended when needed. |
| `topicId` | Yes | Topic ID; it must refer to a formal topic. |
| `difficulty` | Yes | `basic` (direct use of a definition / one-step calculation), `standard` (textbook-example level, 2–3 steps), or `advanced` (integrated, multi-step, or error-prone content). |
| `type` | Yes | `numeric`, `choice`, `short`, or `self` (open-ended; requires self-assessment). |
| `prompt` | Yes | A self-contained question prompt, written in Chinese. State geometry conditions, lengths, angles, and coordinates in text so the question can be understood without a diagram. Include units in the prompt, not the answer. Use the optional `figure` field when a shape must be shown. |
| `answer` | Yes | String. For `numeric`, a number (integer / decimal / fraction `a/b` / negative number); separate multiple answers with the full-width comma `，`. For `choice`, the correct option letter; for `short`, the standard short answer; for `self`, the reference answer. |
| `choices` | Required for `choice` | `[{"key":"A","text":"…"}, …]`, with 3–4 options whose keys are A, B, C, and D in order and whose text is unique. An option can also have a `figure` (inline SVG). |
| `figure` | No | An inline SVG string for a diagram (uses only `viewBox` and `currentColor`; does not reference external resources). The diagnostic page and knowledge-graph sample-question panel render it below the prompt. |
| `hideChoiceText` | No | Set to `true` only for multiple-choice questions. When every option has a `figure`, the page shows the diagrams but hides the option labels (the labels remain in `text` for grading and reference-answer display). Use this for questions such as “Which of the following is a rectangular prism?” so the label does not reveal the answer. |
| `accept` | No | List of equivalent answers for `short` (also supported for `numeric`). |
| `explanation` | Yes | A 1–3 sentence explanation in Chinese, shown after the question is answered. |
| `verify` | No | A Python expression string used to verify `answer` automatically (see below). |
| `unordered` | No | Set to `true` for a `numeric` question with multiple answers when their order does not matter (for example, two roots of an equation). Multiple answers are compared in order when this field is absent. |
| `fixed_from_source` | No | Present only when a condition was added while migrating `diagnostic_question` because the original question was ambiguous; explains why. Currently used by three questions: `cnm_061_q1`, `cnm_070_q1`, and `cnm_253_q1`. |

The `diagnostic_question` field in `topics.json` is preserved unchanged for compatibility; the diagnostic tool falls back to it if the question bank is missing.

## Statistics (Round 5; middle-school questions only, 1,407 total)

- At that time, the bank contained **1,407** questions covering all 315 middle-school topics. Each topic had 4 questions (168 topics) or 5 questions (147 topics), with a minimum of 4, a maximum of 5, and an average of 4.47. These questions have not been rewritten since.
- By type: 903 `numeric`, 475 `choice`, 23 `short`, and 6 `self`; **`numeric` + `choice` account for 97.9%**.
- By difficulty: 591 `basic`, 537 `standard`, and 279 `advanced`. Every topic has both `basic` and `standard` questions and, in addition to q1, at least one more `basic` question (needed because the diagnostic prioritizes a `basic` question second).
- Correct-option distribution for `choice`: A 124, B 126, C 126, D 99. There are 101 questions with 3 options and 374 with 4 options.

## Verification methods

### 1. Automated verification: `python3 scripts/verify_questions.py`

`numeric` and `choice` questions can include a `verify` expression. The script evaluates it in a **restricted environment** (a Python `ast` allowlist: arithmetic, `**`, `//`, `%`, comparisons, lists / tuples / comprehensions, and indexing; calls are limited to `Fraction`, `sqrt`, `pi`, `sin`, `cos`, …, `comb`, `perm`, `gcd`, `lcm`, `sum`, `min`, `max`, `sorted`, `range`, `ceil`, `floor`, `mean`, `median`, `pvariance`, …, plus `solve2` (solve a pair of linear equations using exact fractions) and `roots2` (real roots of a quadratic equation); no imports, attribute access, or assignments; each evaluation times out after 2 seconds). The result is then compared with `answer`:

- `numeric`: Compare the result with each answer. Compare integers and fractions **exactly**, and floating-point values with a tolerance of 1e-9. Use `unordered` to determine whether multiple answers are order-independent.
- `choice`: Compare the result with the **content of the correct option** (compare numeric options by value; otherwise require an exact text match) and ensure no other option has the same value, to prevent multiple correct answers.

The script also checks formatting and reports `auto_verified` (has `verify` and passed), `mismatch`, and `unverifiable`; details are written to `data/verification_report.json`. Round 5 results at the time (middle-school questions only; see the end for current whole-bank totals):

| Metric | Count |
|---|---|
| `numeric` + `choice` questions | 1,378 |
| **`auto_verified`** (has `verify` and passed) | **875** (63.5% of `numeric` + `choice`) |
| **`mismatch`** | **0** |
| `unverifiable` (no `verify`) | 532: 464 `choice` (text or expressions that cannot be evaluated), 39 `numeric` (reasoning questions), 23 `short`, and 6 `self` |

Limitations of automated verification: question authors write `verify` expressions themselves, so the expression and answer may share the same source of error. Some expressions merely list constants (the authors noted `cnm_248_q4` and `cnm_093_q5`); independent second-pass review provides most of the assurance for those questions.

### 2. Independent second-pass review: `scripts/second_pass.py`

Independent solvers (**Claude subtasks**) who did **not see the answers** solved the questions again; their answers were then compared question by question with the bank:

 - Remove `answer`, `explanation`, `verify`, and `accept` from `numeric` / `choice` / `short` questions, leaving only prompts and options, then divide them into batches for the solvers (`second_pass.py prepare`). Each solver can read only their own batch. Tool-call logs were checked to confirm they did not read the question bank or other files.
- **Round A (full set):** 19 solvers answered 1,401 questions (903 `numeric`, 475 `choice`, and 23 `short`) in one pass.
- **Round B (higher-risk questions, more carefully):** 16 solvers answered 752 questions: every `numeric`, `choice`, and `short` question without `verify`, plus every `advanced` question. Solvers were instructed to reason in small batches, calculate nontrivial problems exactly with Python, and write a derivation for each question (`work_b_NN.json`).
- Original answers, derivations, and uncertainty notes are kept under `data/_second_pass/` (`ans_NN.json`, `ans_b_NN.json`, `work_b_NN.json`, `notes_NN.json`, and `mismatches*.json`). Recreate the question-batch files (`blind_*.json`) at any time with `second_pass.py prepare`.
- `second_pass.py compare` compares choice questions by option letter, numeric questions by value (in order or unordered), and normalized short answers against `answer` plus `accept`. Review each mismatch individually.

Results (see `second_pass` in `data/verification_report.json` and `data/second_pass_log.json`):

- Round A had 3 mismatches (`cnm_090_q3`, `cnm_213_q4`, and `cnm_311_q4`). Each was adjudicated using exact calculations; **all three were solver errors, and the bank answers were correct**. Round B had no mismatches.
- **Answer errors found and corrected: 0.** Five other issues were found and corrected: four ambiguous prompts (rewritten after solvers flagged them) and one incorrect explanation. Examples:
  - `cnm_133_q2`: “A point equidistant from the two endpoints of segment AB must lie on:” is true only in a plane → added “in the same plane.”
  - `cnm_053_q3`: the prompt referred to “the diagram…” but included no diagram → removed the reference.
  - `cnm_306_q2`: conventions differ on whether sample variance divides by `n` or `n−1` → specified “the mean of the squared differences between each value and the mean.”
  - `cnm_151_q3`: the explanation described option C as “not mentioned clearly” → a scan for “option letter conflicts with the answer in the explanation” found and corrected it.
- Solvers also flagged 16 questions as “uncertain.” Each was reviewed; except for the four prompt issues above, the prompt conditions uniquely determine the answer, so no change was made.
- The report shows `mismatch = 0` and `second_pass_mismatch = []`.
- During question authoring, each author ran `verify_questions.py --file` before submitting (requiring `mismatch = 0` and no format errors). Issues they corrected themselves at that stage were not recorded, so they are not included in the correction counts above.

### 3. Format validation: `python3 scripts/validate.py`

Question IDs are unique and match `topicId`; `topicId` exists and is not an external node; `difficulty` and `type` are valid; each `choice` question has 3–4 options with unique keys A–D in order, an `answer` that matches a key, and unique option text; `numeric` answers parse as numbers (including fractions, negative values, and multiple answers); required fields are non-empty; no unknown fields are present; every formal topic has at least 3 questions including `basic` and `standard`; q1 exists and its prompt starts with `diagnostic_question` (or has `fixed_from_source`); and `numeric` + `choice` make up at least 60% of the bank. The validator prints question-count statistics.

## Limitations

- **Teachers have not reviewed the questions.** Independent reviewers and authors came from the same model family; if they share a misconception about a topic, neither pass may reveal it. “Zero answer errors” means no disagreement was found, not that errors are impossible.
- About 36% of `numeric` and `choice` questions have no `verify`, mostly multiple-choice questions with text or expressions as options. These rely on independent review alone.
- Prompts are text-only; diagrams cannot be drawn. Geometry conditions are described in words. There are no diagram, construction, or proof questions (proof-reasoning questions use `choice` or `self`).
- **Multiple-choice distractors** reflect guesses about typical errors; they have not been calibrated against real student data. Difficulty labels (`basic` / `standard` / `advanced`) are the authors' subjective judgments, and no discrimination data is available within a difficulty level.
- Each topic has only 4–5 questions, which is not enough for a rigorous assessment. Questions may repeat after several retests; the diagnostic prioritizes unused questions and repeats them only after the unused ones are exhausted.
- `numeric` answers are limited to rational numbers (including decimals). Answers involving radicals or π can only be used in multiple-choice questions. The 23 `short` and 6 `self` questions rely on exact normalized matching or self-assessment, so equivalent wording may still be marked “requires self-assessment.”
- Middle-school batch files were deleted after merging. Elementary batches remain in `data/_qbatches/primary_g1.json` … `primary_g6.json`. Edit questions directly in `data/questions.json` (to rebuild elementary questions from batches, first restore the dependencies containing `cnm_ext_*` as described in `scripts/build_primary.py`), then run `verify_questions.py` and `validate.py`.

## Elementary questions (2026-10-19)

Each formal elementary topic has 4 questions, for **864** total; IDs look like `cnm_p001_q1`. Fields match those for middle-school questions. The q1 prompt is the topic's `diagnostic_question.question`; q1 and q2 are `basic`, and the other two are `standard`. There are no `short`, `self`, or `advanced` questions.

| Metric | Elementary (864 questions) | Whole bank (2,271 questions) |
|---|---|---|
| type | 644 `numeric`, 220 `choice` (100% total) | 1,547 `numeric`, 695 `choice`, 23 `short`, 6 `self` (`numeric` + `choice` account for 98.7%) |
| difficulty | 433 `basic`, 431 `standard` | 1,024 `basic`, 968 `standard`, 279 `advanced` |
| Questions per topic | Exactly 4; every topic has both `basic` and `standard` | Minimum 4, maximum 5, average 4.28 (384 topics with 4 questions, 147 with 5) |
| `auto_verified` | 864 (every `numeric` / `choice` question has a passing `verify`) | **1,739** |
| `mismatch` | 0 | **0** |
| `unverifiable` | 0 | 532 (464 `choice`, 39 `numeric`, 23 `short`, 6 `self`; all from the original middle-school set) |

Questions for younger students use age-appropriate language and avoid symbols they have not learned yet (for example, Grade 1 questions do not use equations with letters). `numeric` questions use the same restricted evaluation for `verify` as `scripts/verify_questions.py`.

Independent review is recorded as Round C in `data/second_pass_log.json`, titled “C: Independent review of elementary questions (`primary_recheck`; reads only prompts and options, not `answer` / `verify` / `explanation`).” `scripts/primary_recheck.py` recalculates answers using only prompts and options; there were **0** mismatches among 864 questions. This round did not use another person who was unfamiliar with the authoring scripts to solve every problem manually; instead, a separate program recalculated the answers without reading `answer`, `verify`, or `explanation`. This differs from the blind-solving method used in middle-school Rounds A and B. The A/B records were not changed. `second_pass_mismatch` remains an empty array.

Teachers have not reviewed the elementary questions either. If volume contents such as Grade 2, Volume 2, change later, the question scenarios may not need to change, but their chapter assignments must be checked against the textbook again.

## High-school compulsory questions (2026-10-20)

Each 2019 People's Education Press A-edition compulsory topic has 4 questions, for **572** total; IDs look like `cnm_h001_q1`. Fields match those for elementary and middle-school questions. The q1 prompt is the topic's `diagnostic_question.question`; q1 and q2 are `basic`, and the other two are `standard`. There are no `short`, `self`, or `advanced` questions. A diagnostic question's `answer` is a numeric value or the **text** of the correct option (not A/B/C/D; option letters rotate by topic index).

| Metric | High school (572 questions) | Whole bank (2,843 questions) |
|---|---|---|
| type | 362 `numeric`, 210 `choice` (100% total) | 1,909 `numeric`, 905 `choice`, 23 `short`, 6 `self` (`numeric` + `choice` account for 99.0%) |
| difficulty | 286 `basic`, 286 `standard` | 1,310 `basic`, 1,254 `standard`, 279 `advanced` |
| Questions per topic | Exactly 4; every topic has both `basic` and `standard` | Minimum 4, maximum 5, average 4.22 (527 topics with 4 questions, 147 with 5) |
| `auto_verified` | 572 | **2,311** |
| `mismatch` | 0 | **0** |
| `unverifiable` | 0 | 532 (the original middle-school questions without `verify`) |

Questions that can be calculated (arithmetic, simplification, evaluation, number of solutions, or endpoints) include `verify`. When an inequality's solution set is an interval, the question is converted to multiple choice or asks for the number of integer solutions or the smallest integer solution. Variance prompts specify division by `n` and use `pvariance`. Percentile questions state the position rule used by the PEP textbook (sort the data and locate `n × p%`; if the position is not an integer, use the next position; if it is an integer, average the two adjacent values) and are marked pending verification. Values such as √2 and √3/2 that cannot be written as simple fractions are tested in multiple-choice questions or replaced by their squared rational values.

Round D in `second_pass_log.json` states that `scripts/hs_build.py` calculates answers to high-school compulsory questions using the same `verify` expression, then writes those answers to the bank; `verify_questions.py` compares them once more. A zero mismatch means only that the format and expression agree; it is **not an independent solution pass**. These questions did not receive the blind-solving review used in middle-school Rounds A and B. For conceptual questions, the correct-option text matches the string returned by `verify`. The batch is in `data/_qbatches/high.json`.

Solid-geometry criteria and properties are tested with multiple-choice questions; students are not asked to write proofs. Teachers have not reviewed the high-school questions either.

## High-school selective-compulsory questions (2026-10-20)

Each 2019 People's Education Press A-edition selective-compulsory topic has 4 questions, for **512** total; IDs start with `cnm_h144_q1`. Fields match the compulsory questions. q1 and q2 are `basic`; q3 and q4 are `standard`. Each prompt is self-contained: it does not refer to another question with wording such as “the same,” “the previous question,” or “this function,” and does not ask whether “this topic” is required by the curriculum standard.

| Metric | Selective compulsory (512 questions) | Whole bank (3,355 questions) |
|---|---|---|
| type | 340 `numeric`, 172 `choice` | 2,251 `numeric`, 1,075 `choice`, 23 `short`, 6 `self` |
| difficulty | 256 `basic`, 256 `standard` | 1,566 `basic`, 1,510 `standard`, 279 `advanced` |
| Questions per topic | Exactly 4 | Minimum 4, maximum 5 |
| `auto_verified` | 512 | **2,823** |
| `mismatch` | 0 | **0** |
| `unverifiable` | 0 | 532 (the original middle-school questions without `verify`) |

Like Round D, Round E used `scripts/hs_sel_build.py` to generate answers with the same `verify` expression, then compared them with `verify_questions.py`; this was **not a blind-solving pass**. The batch is in `data/_qbatches/high_sel.json`.

## High-school English questions (2026-10-21)

Each 2019 People's Education Press high-school English topic has 4 questions, for **1,036** total; IDs start with `cne_h001_q1`. All are multiple-choice. The q1 prompt matches the topic's `diagnostic_question.question`, and its answer is the correct option's text (not A/B/C/D). q1 and q2 are `basic`; q3 and q4 are `standard`. Each prompt is self-contained: it does not begin with “the same,” “the previous question,” or similar references, and does not ask whether “this topic” is required by the curriculum standard. Reading passages are newly written and do not copy textbook text. There are no listening or speaking questions.

The 788 elementary and 980 middle-school English questions were already in the bank. The whole bank now has **6,159** questions (3,355 math + 2,804 English). `verify_questions.py` reports 5,627 `auto_verified`, 0 `mismatch`, and 532 `unverifiable` (the original middle-school math questions without `verify`). For high-school English, `verify` returns the correct-option text using the same logic used to author the question, so this is **not blind solving**. Generation scripts run from `scripts/enh_b1.py` through `enh_s4.py`; `scripts/enh_build.py` writes them to `questions.json`.

## New English textbooks (2026-10)

The new People's Education Press PEP and Go for it! textbooks added 23 topics (elementary `cne_p198`–`cne_p208`; middle school `cne_j246`–`cne_j257`), with 4 multiple-choice questions per topic, for 92 questions total. Distractors use common incorrect forms or similar-looking words. The whole bank now has **6,355** questions (3,459 math + 2,896 English). `verify_questions.py` reports 5,823 `auto_verified`, 0 `mismatch`, and 532 `unverifiable`; these counts are unchanged.
