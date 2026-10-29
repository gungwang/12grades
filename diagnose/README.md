# Math Topic Diagnostic Tool

A static, offline-capable web tool. A student or parent selects a target topic or chapter, and the tool adapts its questions to prerequisite relationships, identifies **root causes of weak areas**, recommends a **learning path ordered by prerequisites**, and lists related curriculum-standard entries. No build step, external CDN, or backend is required; progress stays in the browser's `localStorage`.

> The data (topics, prerequisite edges, and curriculum-standard mappings) is an AI-generated draft that has not been reviewed by teachers. Treat diagnostic results as guidance only.

## Run

From the project root (not from inside `diagnose/`):

```bash
python3 -m http.server 8000
# Open http://localhost:8000/diagnose/ in a browser.
```

The page reads data with `fetch('../data/*.json')`, including the `questions.json` question bank. If the question bank is missing, it falls back to each topic's `diagnostic_question` in `topics.json`. You cannot open the page directly with `file://`. The site-wide top navigation links here from the home page (`index.html` in the project root) and the knowledge graph (`../explore/`). The home page, graph, and diagnostic tool share `../assets/site.css`; `style.css` in this directory contains only the diagnostic page's layout.

### URL parameters (demos, screenshots, and shared links)

| Parameter | Meaning |
|---|---|
| `target=cnm_221` | Start a diagnostic for one topic (or multiple comma-separated IDs). Without `demo`, resume a saved session for the same target if one exists locally; otherwise start a new session. |
| `chapter=七上 Chapter 1` | Use an entire chapter as the target. Use the same “volume + chapter number” format as the list; URL-encode spaces. |
| `grade=七年级` | Run a grade-level screening diagnostic. Values range from Grade 1 through Grade 9; each grade includes both volumes. You can also use `七`. If `target` or `chapter` is also present, it takes precedence. |
| `volume=七上` | Diagnose one volume only (for example, `七上` or `八下`). Use it by itself or with `grade` (they must refer to the same grade, or the tool reports an error; `grade=七年级&volume=上` is also accepted). |
| `demo=1` | Simulate a student's answers and go directly to the results page. **The demo does not read or write saved sessions.** The target is answered incorrectly twice (weak); its first testable prerequisite is also answered incorrectly twice (weak root cause); the next-earlier topic (or the target's other prerequisite if there is no earlier topic) is answered incorrectly and then correctly (shaky); all other topics are answered correctly for the current `confirm` count (mastered). The results therefore show mastered, shaky, and weak topics together. For `grade` or `volume` screenings, the simulated student answers about one-sixth of topics incorrectly, one-sixth shakily (first answer wrong, second correct), and the rest correctly; the results include a chapter summary. |
| `step=2` | With `demo=1`, answer only the first two questions automatically, then stop on the question page for question 3. |
| `limit=16` | Maximum number of questions in this diagnostic (**counted by question**, not topic). If omitted, use the configured limit: 16 by default for one topic or a chapter (adjustable from 8 to 30), and 40 for an overall screening diagnostic (adjustable from 20 to 60). |
| `seed=abc` | Fix the random seed for question selection. The same target, seed, and answers produce the same questions (useful for testing and reproducing a session). If omitted, each session is random. The demo seed defaults to `demo`. |

Examples: `http://localhost:8000/diagnose/?target=cnm_221&demo=1`, `http://localhost:8000/diagnose/?grade=七年级&demo=1`, `?volume=七上&limit=50`, and `?chapter=七上%20Chapter%201&demo=1`.

## Workflow

1. **Start page:** Choose a school level (all / elementary / middle / high school), then search for a topic. Volume and chapter lists remain available but are collapsed by default; expand them as needed. Select “Set as target” or “Set entire chapter as target” beside a chapter heading. Set the question limit from 8 to 30; the setting is stored locally. On mobile, option buttons are at least 44 px tall.
   **Screening by grade:** Use the second card on the start page. Choose a grade from 1 through 9, or a high-school volume label (Grade 10, Grade 11, or Selective-Compulsory Volumes 1–3). Elementary and middle school users can then choose the whole grade, first volume, or second volume. High-school volumes are not split by semester: the scope button for either compulsory volume says “Entire compulsory volume,” and the button for a selective-compulsory volume says “Entire volume.” The card shows the number of topics in the scope. Set the question limit from 20 to 60 (40 by default); this setting is stored locally and is separate from the single-topic limit. This screening checks mastery of the selected grade's topics; it is not an advanced or contest test. Questions use basic, standard, and advanced levels: standard questions come before advanced confirmation questions, and a wrong answer is followed by a basic question. After you select “Start grade-level diagnostic,” the tool screens topics within the selected grade or volume. A correct answer also skips its prerequisites within the scope; a prerequisite is revisited within the scope only if the confirmation answer is still wrong. Prerequisites outside the scope are labeled “Prerequisite” and marked as unchecked. The saved session records the mode, so after a refresh, “Continue” resumes the grade-level diagnostic. Copy-paste URL values include `grade=高一`, `grade=高二`, and `grade=选必二`; aliases `高一必修` and `选择性必修第二册` are also accepted. English adds Compulsory Volumes 1–3 and Selective-Compulsory Volumes 1–4 to Grades 3–9; its URL must include `subject=english` (for example, `grade=选必一` or `grade=必修一`; the alias `选择性必修第一册` is also accepted). High-school English volumes are not split by semester: the scope button for a compulsory volume says “Entire compulsory volume,” and the selective-compulsory button says “Entire volume.” Without `subject`, these values do not select math.
2. **Question page:** Each question shows the topic, difficulty (basic / standard / advanced), type, its number for the topic, and “Why am I being asked this now?” (the target itself / a revisit because two questions for another topic were not passed / a retest after missing the first question). When the tool revisits a lower grade, it labels the topic “Prerequisite.”
   - Multiple choice: select an option, then choose “Submit answer.” Numeric and short-answer questions: enter an answer and choose “Submit answer” (or press Enter). Open-ended questions: enter your reasoning, then choose “Show reference answer and self-assess.”
   - After selecting “Show reference answer and self-assess,” choose Correct / Incorrect / I don't know.
   - “I don't know” displays the reference answer and explanation; choose “Next question” to record the answer as incorrect.
   **Every answer is followed by the reference answer and explanation**, including automatically graded answers. Then choose “Next question.” After automatic grading, you can select “Marked incorrectly…” to change the result manually. “Undo previous question” and “Restart” are also available.
3. **Results page:** Shows weak root causes, **shaky topics**, the recommended learning path (text list), a path graph, mastered and untested topics, related curriculum-standard entries, and the answer history (including each question, your answer, and the reference answer; you can correct individual answers, which recalculates the entire diagnostic). The graph uses Cytoscape + dagre and matches the knowledge graph: elementary, middle, and high school have different colors; hard prerequisites use solid lines and soft prerequisites use dashed lines; weak root causes are highlighted. Long names are shortened on the graph; hover or tap to see the full name. Grade-level results also include a **chapter summary** after the top-level statistics: each chapter's mastered / shaky / weak / untested counts (with a color bar) and the names of its weak and shaky topics, with weaker chapters first. If a weak topic has prerequisites outside the selected scope, a notice says that some prerequisites were not checked and can be diagnosed separately; the relevant root cause lists those prerequisites. Overall diagnostics do not label a “target,” and the curriculum-standard summary includes only topics on the learning path. You can “Export JSON” (including each question's ID, your answer, result, reference answer, and explanation) or “Print / Save as PDF” (the `@media print` stylesheet expands all collapsed sections when printing). You can also “Generate share image”: a 1080 × 1920 portrait image drawn on a canvas with the site name, subject and scope, mastered / shaky / weak / untested counts, the 2–3 weakest chapters or topics, 1–2 root causes, and the date. A QR code at the bottom points to `https://math.pansgo.com/?from=share`, beside the text “Scan to open this site.” The image includes no name and no payment information. Desktop users download it from a modal; on narrow screens, the image prompts users to press and hold to save it. The QR code is drawn locally by `assets/vendor/qrcode.js` (qrcode-generator 2.0.4, MIT).
4. Refreshing the page does not lose progress. The start page offers “Continue” or “Discard saved session.” IDs of questions already used are also stored in `localStorage` under `cnmDiagnose.seen.v1`; the next diagnostic prioritizes unused questions.

## Algorithm

All logic is in `engine.js` (UMD: use `window.DiagEngine` in a browser or `require` in Node; pure functions, no DOM, and session objects are JSON-serializable). The UI only calls the engine and renders its results.

**Graph and subgraph:** In `dependencies.json`, `prerequisiteId` is a prerequisite of `topicId`. The prerequisite subgraph for a target set contains the targets and all their ancestors (elementary and middle-school topics are in the same graph). It is stably topologically sorted, with prerequisites first and topics at the same level ordered as in `topics.json`, so results are reproducible. Each topic's prerequisites are sorted with **hard edges before soft edges**. The start page can filter by school level (all / elementary / middle / high school). Legacy IDs `cnm_ext_*` in a URL are expanded to the corresponding elementary topics using `data/id-aliases.json` before diagnosis (for example, `?target=cnm_ext_002`).

**Adaptive question selection** (`createSession` / `nextQuestion` / `nextItem` / `applyAnswer`) maintains a question stack. A topic is **mastered only after `confirm` consecutive correct answers** (3 by default; choose 2 / 3 / 5 on the start page, where the choice is stored locally; if the question bank has fewer questions, use the available number):

 - The initial stack orders targets by proximity to the target (later in topological order), so **the target itself is asked first**. For a chapter target, ask the last topic in the chapter first.
 - **Reaching the required number of consecutive correct answers** marks a topic **mastered** and all its ancestors (including elementary topics) as “mastered (inferred),” so they are not asked.
 - **An incorrect answer or “I don't know” before reaching the required count** leaves the result undecided and triggers another confirmation question for the same topic (same difficulty or easier; see “Question selection” below):
   - **If the confirmation answer is also incorrect or “I don't know,”** mark the topic **weak** and push its undecided direct prerequisites onto the top of the stack (hard first, then soft). Continue backward using **depth-first** traversal. **Only this case triggers prerequisite backtracking.**
   - **If the confirmation answer is correct,** mark the topic **shaky**, show it separately on the results page, and **include it in the learning path as a topic to review**. Do **not** backtrack to its prerequisites (the default behavior: one wrong answer followed by one correct answer is more likely to reflect carelessness or uncertainty than a prerequisite problem). Its prerequisites remain untested unless another backtrack or a later correct target answer determines their status.
- If a topic has too few questions in the bank (or no confirmation question remains), an incorrect answer marks it weak immediately. If the bank has fewer questions than `confirm`, answering all available questions correctly marks it mastered.
- Topics with a decided status (mastered / shaky / weak) are not asked again. A directly answered status is never overridden by an inferred mastery.
- Elementary topics use the same question flow as middle-school topics. The graph no longer contains `cnm_ext_*` nodes without questions.
- The question limit is **a count of questions**, not topics. It defaults to **16** and can be set from 8 to 30; the results page also offers “Answer 4 more questions.” At the limit, remaining topics are marked untested. If the limit is reached after a topic's first answer is incorrect and before its retest, mark the topic weak for now and note “Not retested” on the results page.

**Question selection** (`pickQuestion`) is a pure function determined by the session's `seed`:

 - Uses the `mulberry32` pseudorandom generator. Randomness depends only on `(seed, topic, question number)`, so **the same seed and answers produce the same questions**; `replay` also reproduces the same result after a refresh, undo, or correction. Set a seed with the `seed=` URL parameter. If omitted, a random seed is generated for each session and saved.
 - **First question:** Prefer **standard** difficulty; fall back to basic if there are no standard questions, and avoid advanced questions when possible. Prefer **unused** questions. IDs of previously used questions are stored in `localStorage` and passed to the engine as `avoid` when a session is created; a question may repeat if all questions have been used.
 - **After consecutive correct answers:** Prefer a **challenge** (advanced) question to confirm mastery, then standard, then basic.
 - **Confirmation after an incorrect answer:** Use the **same or an easier difficulty, preferably basic**; next try the first question's difficulty, then other easier questions, and only use a harder question if no other choice remains. Difficulty takes priority over whether a question is unused; within the same difficulty, prefer unused questions.
 - The same question is never asked twice in one session.

**Results** (`summarize`):

- **Root cause** = a weak topic whose direct prerequisites contain **no other weak topic** (a shaky prerequisite does not count as weak). If a prerequisite remains untested because the question limit was reached, note that the true root cause may be earlier. In hand-built graphs, prerequisites without diagnostic questions are listed separately; every elementary topic in the current data has a question.
- **Shaky** = a topic with an incorrect answer followed by a correct confirmation answer (`summary.shaky`).
- **Learning path** = topics in the prerequisite subgraph reachable from any root cause **or shaky topic** in the “depended on by” direction, excluding mastered topics and **ordered from lower to higher grade** (topological order is preserved within each grade, with prerequisites first). Weak and shaky topics are always included. Check untested topics on the path yourself. A wrong middle-school answer can lead to questions about elementary topics.
- **Path graph** (`layout` selects the nodes and edges; the page lays them out with Cytoscape + dagre): shows the union of the path, targets, root causes, and topics actually asked. Edges use the transitive reduction of reachability among the selected topics. Direct hard prerequisites use solid lines; soft prerequisites use dashed lines; omitted intermediate topics are shown with dotted lines. Prerequisites appear above targets. The text list still shows the complete learning order.

**Consistency:** `replay(graph, targets, answers)` reconstructs a session from its answer history. Refresh recovery, undo, and answer corrections all work by updating the history and replaying it, so session state cannot drift from the recorded answers.

## Grading rules

Grade by question type with `judgeQuestion(question, userText)`. Return correct or incorrect only when the result is **reliable**; otherwise, ask the user to compare the reference answer and self-assess (returns `correct`, `wrong`, or `manual`):

- **`choice`:** Compare option letters directly (`B`, `b`, `(B)`, and `B.` are accepted). Also accept option text when it matches after normalization. A different option is incorrect; an unrecognized answer requires self-assessment. In the interface, select an option to answer.
- **`numeric`:** Use the numeric rules below. If `answer` contains multiple values, order does not matter only when `unordered: true`; otherwise, compare values **in order**. Equivalent formats in `accept` are also correct.
- **`short`:** Mark correct only when the normalized answer exactly matches `answer` or `accept`. A mismatch is **not marked incorrect**; ask the user to self-assess because text and algebraic expressions have many equivalent forms.
- **`self`:** Always require self-assessment.
- In fallback mode (no question bank, so the question comes from `diagnostic_question`), use the general rules below.

The following general rules for numeric and text answers are implemented by `judgeAnswer`:

Normalize both answers: convert full-width characters to half-width with NFKC (for example, `１/２` → `1/2`); remove whitespace; normalize punctuation (including enumeration commas, full-width periods, multiplication and division signs); convert `²` to `^2`; normalize degree expressions such as “90 degrees,” “90°,” and “a 90° angle” to `90°`; convert `≦≧` to `≤≥`; remove a trailing full stop and a localized answer prefix; normalize thousands separators (`1,000` → `1000`); and normalize mixed numbers such as `1 1/2` and `1 and 1/2`.

Comparison rules:

1. If the normalized text is identical, mark it correct.
2. Split multiple answers on `,`, `;`, `、`, `，`, or the words “and,” “or,” and their equivalents. Do not split commas inside parentheses, so `(1,2)` is one answer. Compare multiple answers **without regard to order**: `-3 and -1/2` ≡ `-1/2，-3`.
3. When each answer can be safely parsed as a number, compare **exact rational values** (integers, decimals, fractions, percentages, mixed numbers, and signed or parenthesized values): `1/2` ≡ `0.5` ≡ `2/4` ≡ `50%`; `1/3` ≢ `0.333`. Compare coordinate pairs such as `(a,b)` component by component.
4. Variable names: for a single answer, `x=3` ≡ `3`. For multiple answers where the reference answer uses distinct variable names (such as `x=3，y=2`), compare variables when the answer includes them; if it omits them, compare values in the reference answer's order. Thus, `x=2，y=3` is incorrect.
5. Units: accept Chinese-language and symbolic aliases for meters (`m`), square meters (`m²`), degrees (`°`), and other supported units. Accept an answer if only one side includes a unit. Different known units are incorrect; an unknown unit requires self-assessment.
6. If both answers are numeric but not equivalent, mark the answer incorrect. For **algebraic expressions, text, and other forms**, mark an answer correct only if the normalized text is identical; otherwise, **do not decide**. Show the reference answer and ask the user to self-assess. For example, `y=3x+2` versus `y=2x+3` requires human judgment because equivalent forms such as `y=(x-2)²-1` and `y=x²-4x+3` cannot be reliably recognized.

The interface always notes that automatic grading is approximate, the reference answer takes precedence, and users can correct a result manually.

## Files

```
diagnose/index.html   Page shell (references ../assets/site.css, style.css, graph libraries, engine.js, and app.js)
diagnose/engine.js    Core algorithms and grading (pure functions, shared by browser and Node)
diagnose/app.js       UI: data loading, start / question / results pages, Cytoscape path graph, localStorage, export, and printing
diagnose/style.css    Diagnostic-page layout (including @media print); colors and navigation are in ../assets/site.css
tests/test_engine.js  Node tests (no dependencies): node tests/test_engine.js
scripts/screenshot.js Headless Chrome smoke test and screenshots: node scripts/screenshot.js
screenshots/          Diagnostic flow 01–05; home / graph / narrow screens 06–16; all ancestors and long names 17–20; high school 21–27; selective compulsory 28–31; elementary English 32–35; share images 38–40; middle-school English 43–46; high-school English 51–54
data/questions.json   Question bank (6,159 questions: 3,355 math + 2,804 English; see docs/questions.md)
```

### Tests

```bash
node tests/test_engine.js      # Hand-built graph + two-question grading + real data + elementary backtracking + legacy ID aliases + question bank; includes a randomized "consistent student" property test.
node scripts/screenshot.js     # Requires local Chrome/Chromium (set CHROME=… to specify a path); temporarily starts http.server (PORT, default 8765).
```

In the property test, a “consistent student” has a mastered set that is closed over ancestors. With no question limit, the diagnostic's weak set should exactly match the topics the student does not know, and root causes should exactly match topics the student does not know whose prerequisites they do know.

## Exported JSON structure

Fields include `version: 2`, `mode` (`target` or `screen`), `label`, `targets`, `limit`, `seed`, `asked`, `finished`, `limitReached`, `answers` (for each question: `order`, `topicId`, `questionId`, `difficulty`, `type`, `prompt`, `userAnswer`, `result`, `referenceAnswer`, and `explanation`), `weakRoots` (including mastery criteria, curriculum-standard IDs, untested prerequisites, and out-of-scope prerequisites in `outOfScopePrereqs`), `path` (with order and status), `weak`, `shaky`, `chapters` (overall diagnostics only: each chapter's `label`, status counts, and `weakTopics` / `shakyTopics` / `untestedTopics`), `mastered` (direct / inferred), `untested`, and `standards` (IDs and original text).

## Limitations

- **The confirmation count defaults to 3 per topic** (choose 2 / 3 / 5). The bank contains 4–5 questions per topic. Multiple-choice answers can be guessed, so “shaky” is a prompt to review, not a conclusion. Repeated diagnostics may reuse questions.
- **Shaky topics do not trigger backtracking** by design. If a student answers one question incorrectly but gets the confirmation question right, the tool does not continue checking prerequisites; a genuinely weak prerequisite may be missed. Shaky topics are shown on the path for the student to review.
- Correctly answering one topic causes all its ancestors to be inferred as mastered, which depends on the accuracy of the prerequisite graph. The prerequisite edges are an AI-generated draft that has not been reviewed by teachers.
- Elementary, middle-school, high-school compulsory, and selective-compulsory topics share one graph. The default question limit is 16, so a diagnostic may not reach the earliest topic in a long prerequisite chain. Increase the limit or run another diagnostic for untested topics in the results to reach Grade 1. Legacy links using `cnm_ext_*` redirect to representative topics in the alias file, not to every elementary topic in that subject. Selective-compulsory `grade` values 12–14 identify volumes, not school years. High-school English `grade` values 10–16 also identify volumes (three compulsory and four selective-compulsory volumes); the page does not label them as Grades 10–16.
- Grading supports only numeric answers, fractions, coordinates, multiple answers, and simple answers with units. Algebraic expressions, text answers, and proofs always require self-assessment. Equivalent fractions such as `2/4` are accepted because values are compared.
- A topic is marked weak only because the student answered incorrectly or selected “I don't know”; the tool does not distinguish conceptual errors from calculation mistakes.
- dagre lays out the path graph. Edges may pass close to other nodes when the path spans many levels; graph labels may be shortened, so use the text list for the complete order.
- Progress exists only in the current browser's `localStorage`; switching browsers or clearing data removes it. Private browsing may prevent saving.
- The page is usable on mobile: the start page emphasizes search, option and primary-action buttons are at least 44 px, and narrow screens do not overflow horizontally. Accessibility support (keyboard and screen readers) is limited to basic semantic labels.
