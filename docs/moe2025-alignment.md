# Alignment record for the 2025 routine revision (2026-10-21)

> In brief: the **elementary-school content requirements (Stages 1–3) were checked clause by clause** against the *Mathematics Curriculum Standards for Compulsory Education (2022 Edition, Revised in 2025)*:
> four clauses missing from the original dataset were added, one omitted final sentence was restored, and two IDs were renumbered to follow clause order.
> **The revised edition did not change modules, themes, or stage divisions.** This pass changed no topics, prerequisite edges, or questions.
> Stage 4 (Grades 7–9) and high school were **not** included in this check; see Section 7 for details.

## 1. Basis

| Item | Details |
|---|---|
| Current standard | The Ministry of Education's *Routine Revision of the Curriculum Plan and Curriculum Standards for Primary and Secondary Schools* (**Textbook [2025] No. 1**), including the *Mathematics Curriculum Standards for Compulsory Education (2022 Edition, Revised in 2025)* |
| Pre-revision baseline | *Mathematics Curriculum Standards for Compulsory Education (2022 Edition)* (Textbook [2022] No. 2); the repository's Stage 4 entries were transcribed from this edition's PDF |
| Full text used for this check | Locally saved `math-2025.txt` (306 KB public transcription, extracted character by character; Stage 4 completed on 2026-10-21). It is **not the Ministry of Education PDF** and has no page numbers. A scanned copy of the official PDF has been kept locally since 2026-10-21 for page-by-page comparison. |
| Review date | 2026-10-21 |
| Review scope | Stages 1–3 (Grades 1–6) × Number and Algebra / Geometry / Statistics and Probability |

For mathematics, the revised edition describes “17 detailed improvements” but does not change modules or themes. **These 17 changes are below the granularity represented in this dataset** (they affect wording, examples, academic-quality descriptions, and teaching guidance).
The purpose of this check was therefore not to replace every clause, but to **confirm whether elementary clauses were added or removed** and restore clauses missing from the original dataset.

## 2. Method (reproducible)

```bash
python3 scripts/moe2025_check.py --moe /path/to/math-2025.txt
```

1. Extract the **Content Requirements** block for each (domain, stage) from the revised text, then split it into clauses by subsection headings (such as `1. Number and Operations`) and clause numbers (such as `(1)`).
2. Pair the clauses with repository entries by (stage, domain, order), then calculate `difflib` similarity after removing “(Example N)” and retaining only letters and numbers.
3. **Treat similarity ≥ 0.995 as a match.** Manually review every clause below the threshold and classify it as one of:
   - **Transcription noise:** OCR dropped characters, footnotes were merged into the text, or symbols were lost → do not change the data (to avoid presenting noise as source text).
   - **Clause missing from the original data:** present in the revised edition but absent from the repository → add it.
   - **Genuine rewrite:** the standard actually changed the wording → revise the clause.

The script reports differences but does not write files; a person decides whether to make changes.

## 3. Clause-count comparison (Content Requirements)

| Stage | Domain | Repository before revision | Revised text | Result |
|---|---|---:|---:|---|
| First (Grades 1–2) | Number and Algebra | 8 | 8 | Match |
| Second (Grades 3–4) | Number and Algebra | 10 | 10 | Match (one clause completed; see §4) |
| Third (Grades 5–6) | Number and Algebra | 9 | 10 | **Add 1 clause** |
| First | Geometry | 3 | 3 | Match |
| Second | Geometry | 9 | 9 | Match |
| Third | Geometry | 12 | 12 | Match |
| First | Statistics and Probability | 1 | 1 | Match |
| Second | Statistics and Probability | 6 | 6 | Match (one clause completed; see §4) |
| Third | Statistics and Probability | 4 | 7 | **Add 3 clauses** |
| Total | | 62 | 66 | |

After the review, the script reported “Groups with clause-count mismatches: 0” and “Extra clauses: 0.”

## 4. Dataset changes (`data/cn-curriculum-standards.json`)

### 4.1 Add four clauses (already present in the 2022 edition, but missing from the original data)

| ID | Clause | Text |
|---|---|---|
| `cms-2022:3.NA.10` | Stage 3 · Quantitative Relationships (6) | Use common quantitative relationships to solve practical problems, reasonably explain what the results mean in context, gradually develop modeling awareness and geometric intuition, and improve problem-solving skills. |
| `cms-2022:3.SP.03` | Stage 3 · Collecting, Organizing, and Representing Data (3) | Obtain needed data from various media and understand simple statistical charts and tables. |
| `cms-2022:3.SP.04` | Same subsection (4) | Explore the meaning of percentages in a specific context, solve simple practical problems involving percentages, and understand their statistical meaning. |
| `cms-2022:3.SP.05` | Same subsection (5) | Apply charts, tables, or percentages in simple practical contexts to develop data awareness and an initial awareness of applications. |

⚠️ These four clauses are **not new requirements introduced in 2025**. They can be found verbatim by searching the public 2022-edition text (for example, Stage 3 statistics includes “obtain needed data from various media…,” as does item (6) under quantitative relationships).
They were omitted when the original data was split into numbered clauses during transcription. `text_status` records that they were missing from the original 2022-edition data.

### 4.2 Complete one clause

`cms-2022:2.SP.06`: the original text was “Reasonably apply charts, tables, and averages in simple practical contexts.” Restore the omitted final sentence: “Develop an initial awareness of data and its applications.” (The sentence appears in both the 2022 edition and the revised edition.)

### 4.3 Renumber IDs to match clause order

Original `3.SP.03` (likelihood of random events (1)) → `3.SP.06`; original `3.SP.04` (likelihood of random events (2)) → `3.SP.07`.
Without renumbering, newly added items (3), (4), and (5) would appear after the random-events items, disrupting clause order. This document's ID convention is **consecutive numbering by clause order within each domain**; the validator also checks continuity.

The two topics that reference these clauses were updated to use the new IDs: `cnm_p140` (references 03 and 04) and `cnm_p141` (references 04).
The old IDs are recorded in each entry's `note` for traceability.

### 4.4 `source` metadata

Added four fields: `revision`, `revision_status`, `revision_checked_at`, and `revision_scope`. Updated `title` to “(2022 edition, revised in 2025)” and appended the review method and remaining uncertainties to the end of `note`.

### 4.5 Page references: added for all 77 elementary entries (2026-10-21)

The official PDF is a **scan** (`义教-数学.pdf`, 186 pages, with zero text characters per page) and has no text layer. Page references were located by **rendering each PDF page as an image and inspecting it**, without relying on OCR. Conversion: **PDF page number = printed page number + 3** (for example, PDF page 4 = printed page 1, “I. Nature of the Curriculum”; PDF page 68 = printed page 65; PDF page 71 = printed page 68).

| Domain | Stage 1 | Stage 2 | Stage 3 |
|---|---|---|---|
| Number and Algebra | 18–19 | 20–21 | 23–24 |
| Geometry | 28 | 29–30 | 32–33 |
| Statistics and Probability | 37 | 38 | 39–40 |
| Integrated Practice | 42–43 | 46 | 49 |

Page references are stored in `page_or_ref` as `Printed curriculum-standard page N` and generated from the `PAGES` table in `scripts/primary_std.py`; rerunning `build_primary.py` still produces byte-identical output.
One rule remains unchanged: **the clause text is still a web transcription**, so `verbatim` remains `false`. Matching page references do not guarantee a verbatim transcription.

## 5. Transcription noise left unchanged

| Entry | Appearance in revised text | Handling |
|---|---|---|
| `3.NA.09` | “Understand proportional quantities (Example 20)” — the word “quantities” is missing | Keep the repository wording, “understand proportional quantities.” |
| `1.NA.02` | “Understand the meaning of the symbols \” — the inequality signs `<`, `=`, and `>` were lost during extraction | Keep the complete repository wording. |
| `3.SP.02` | A footnote was inserted into the middle of the text: “[1] mu is a traditional Chinese area unit; 1 mu ≈ 666.67 m².” | Remove the footnote and leave the clause unchanged (`moe2025_check.py` already skips footnote lines). |
| `4.GG.39` / `4.GG.75` | The transcription contains only “polygon 1]” and “property theorem 1:” — the footnote markers remain, but the footnote text is missing. | On 2026-10-21, page-by-page review of the official PDF confirmed that the footnote on printed page **65** says “Polygons in this standard refer to convex polygons,” and the footnote on printed page **68** says “Students are not required to prove these theorems.” The footnotes were restored in parentheses in the text. This indicates that the 2025 edition merely **moved the 2022 parenthetical notes to footnotes**; the requirements themselves did not change. |

## 6. Three common claims about the 2025 revision that do not match the text (for the main project)

These three claims are widely repeated in secondary commentary, but **the revised text does not support the claimed changes**:

1. **“Elementary students now learn simple equations in middle school.”** The elementary Content Requirements for all three stages have **never included a clause requiring students to solve equations**. Stage 3 quantitative relationships cover properties of equality, representing quantities with letters, ratios and proportions, and proportional quantities.
   “Simple equations” is a unit in the People's Education Press **textbook** for Grade 5, Volume 1, not a curriculum-standard requirement. This is a textbook-level issue, not a curriculum-standard revision; repository topics `cnm_p142`–`cnm_p146` for the Grade 5, Volume 1, “Simple Equations” unit are textbook topics and **were not changed**.
2. **“Elementary schools added ruler-and-compass constructions.”** The term “ruler and compass” appears only four times in the revised text: once in a footnote (line 311 of the completed `math-2025.txt`) and in **Examples 73 and 76** for Stage 4 (lines 3491 and 3539). **There is no ruler-and-compass construction clause in the elementary Content Requirements.** Topic `cnm_127` (basic ruler-and-compass constructions in Grade 8, Volume 1) remains correctly placed.
3. **“Middle schools added stratified sampling.”** The revised teaching guidance clearly states: “Teachers should understand stratified sampling, but **students need to learn only simple random sampling**” (line 2821). Stratified sampling is not a student content requirement, so **no topic was added**.

Quartiles and box plots appear in the revised edition (Example 86, starting at line 3001). Repository topics `cnm_216` and `cnm_305` already cover them, so no change was needed.

## 7. Not reviewed / pending verification

- **Stage 4 (157 clauses) was checked, but the data was not changed:** the first transcription used for Stage 4 was incomplete (the full Geometry and Statistics and Probability sections were missing, and Number and Algebra was mixed with appendix examples). The missing 884 lines were restored from the same source on 2026-10-21. After restoration, a clause-by-clause comparison showed that the 49 Number and Algebra, 92 Geometry, 13 Statistics and Probability, and 3 Integrated Practice clauses all match the repository's 157 clauses in **count, order, and content** (155 clauses had similarity ≥0.95; the other two had collapsed footnotes, whose text was confirmed against printed pages 65 and 68 of the official PDF and matches the 2022 parenthetical notes). Therefore, **the 2025 revision did not change Stage 4 Content Requirements, and no data change was needed**. The restoration and page-number conversion are recorded locally in `references/.moe-2025/README.md`.
- **High school (80 clauses) was not checked:** the text of the *General High School Mathematics Curriculum Standards (2017 Edition, Revised in 2025)* was not available; existing entries still reflect the 2017 edition revised in 2020.
- **Integrated Practice (IP) clauses were not aligned:** the 2022 edition has 6 / 4 / 1 “thematic activity” clauses; the revised edition uses narrative paragraphs that require manual splitting. This was not done in this pass (**page references were added**; see §4.5).
- **A full character-by-character comparison was not performed:** page review changed only three substantive differences (the symbols in `1.NA.02`, restoring “(such as y/x=5)” in `3.NA.09`, and the footnotes in `4.GG.39` / `4.GG.75`). The **wording** of the remaining 70-plus clauses was not compared character by character, so transcription noise may remain.
- **Examples in the revised edition's appendix increased from 63 to 94:** the repository does not cite example numbers (the conventional “(Example N)” markers were removed from clause text), so no migration was needed. Example numbers for newly added clauses were not recorded.
- **“Proportional quantities / directly proportional quantities” in `3.NA.09`:** the repository's `wording_note` already mentions this line-break discrepancy; it still needs to be checked against the PDF.
- **Topics, prerequisite edges, question bank, and pages were not changed.** Only three curriculum-standard references in `data/topics.json` were updated (see §4.3).

## 8. How to verify again

```bash
python3 scripts/validate.py                       # Check data consistency, including curriculum-standard ID continuity.
python3 scripts/build_primary.py                  # Rebuild data/ from scripts/primary_*.py (output should match repository files byte for byte).
python3 scripts/moe2025_check.py --moe <revision-text>  # Compare clause counts, differences, and omissions.
```

The generators for this pass were also updated: `scripts/primary_std.py` (adds four clauses, completes `2.SP.06`, and renumbers two IDs) and `scripts/primary_g46.py` (renumbers two curriculum-standard references).
**`python3 scripts/build_primary.py` was run in a temporary directory, and the SHA-256 hashes of the generated `topics.json`, `dependencies.json`, `questions.json`, `cn-curriculum-standards.json`, and `id-aliases.json` exactly match the repository files.** This confirms that the generator can reproduce these data files unchanged.

`moe2025_check.py` uses only the standard library. The default threshold is 0.995; use `--threshold` to lower it.
