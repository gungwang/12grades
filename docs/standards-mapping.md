# Curriculum-standard alignment: topics ↔ *Mathematics Curriculum Standards for Compulsory Education (2022 Edition; the 2025 routine revision is current)*

> **Status: AI generated the mappings; teachers and curriculum experts have not reviewed them.** This applies to elementary, middle-school, high-school compulsory, and selective-compulsory topics. `exact` and `inferred` are this project's judgment labels, not terms from the curriculum standards. The 48 high-school compulsory and 32 selective-compulsory entries are public paraphrases, not text verified page by page.
>
> **2026-10-19:** The file now includes Stages 1–3. The text of the 157 Stage 4 entries has not changed. Stages 1–3 **were not** checked page by page against the Ministry of Education PDF; see Section 1. The “315 / 157 / 15 unmapped” counts in Sections 3–5 below are from Round 3, which covered only Stage 4. Current whole-dataset counts are in Section 8.
>
> **2026-10-21 (2025 revision):** Stages 1–3 were checked against the *Mathematics Curriculum Standards for Compulsory Education (2022 Edition, Revised in 2025)*. Four clauses missing from the original dataset were added, one omitted final sentence was restored, and two IDs were renumbered to follow clause order. No changes to modules or themes were found. See [moe2025-alignment.md](moe2025-alignment.md) for the method and remaining uncertainties.

## 1. Curriculum-standard sources

| Item | Details |
|---|---|
| Document | *Mathematics Curriculum Standards for Compulsory Education (2022 Edition)*, issued by the Ministry of Education of the People's Republic of China |
| Publication page | <http://www.moe.gov.cn/srcsite/A26/s8001/202204/t20220420_619921.html> (Ministry of Education notice issuing the 2022 compulsory-education curriculum plan and standards, Textbook [2022] No. 2) |
| PDF used | <http://www.moe.gov.cn/srcsite/A26/s8001/202204/W020220510531636118932.pdf> (the mathematics curriculum-standard document marked “Use this version” on the publication page, dated 2022-05-09) |
| Scope | Content Requirements for Stages 1–4. Stage 4 (Grades 7–9) was entered on 2026-10-17; Stages 1 (Grades 1–2), 2 (Grades 3–4), and 3 (Grades 5–6) were added on 2026-10-19. |
| Retrieval dates | 2026-10-17 (Stage 4); 2026-10-19 (Stages 1–3) |

Acquisition method and text quality: this PDF is a scan with no text layer. A web-crawling service recognized the PDF text, which was then organized into entries. Two pages (printed pages 63 and 65) were spot-checked against the original PDF images, and the recognized text matched character by character; **the remaining pages were not compared character by character**. Use the Ministry of Education PDF as the source of record when citing the standard.

The Stage 4 entries remain the following **157** clauses (the text has not changed):

| Domain | Count | Corresponding curriculum-standard themes (subthemes) |
|---|---|---|
| Number and Algebra (NA) | 49 | Numbers and Expressions (rational numbers, real numbers, algebraic expressions); Equations and Inequalities (equations and systems of equations, inequalities and systems of inequalities); Functions (function concepts, linear functions, quadratic functions, inverse proportion functions) |
| Geometry (GG) | 92 | Properties of Figures (points, lines, planes, and angles; intersecting and parallel lines; triangles; quadrilaterals; circles; definitions, propositions, and theorems); Transformations of Figures (reflection, rotation, translation, similarity, projection); Figures and Coordinates (position and coordinates; motion and coordinates) |
| Statistics and Probability (SP) | 13 | Sampling and Data Analysis (11 clauses); Probability of Random Events (2 clauses) |
| Integrated Practice (IP) | 3 | Project-Based Learning (3 clauses) |

Entry granularity: each natural clause under a curriculum-standard “Content Requirement” is one entry (Number and Algebra and Geometry use circled numerals ①②③…; Statistics and Probability and Integrated Practice use numbered clauses such as (1), (2), …). **Clauses are not split further.** IDs use `cms-2022:4.<NA|GG|SP|IP>.<NN>` and are numbered consecutively within each domain in the order used by the standard. Each entry also has `theme`, `section`, `clause` (the original clause number), and `page_or_ref` (printed page; PDF page = printed page + 7). Set `"elective": true` for a clause designated as optional (marked `*` in the standard and not required for exams): `NA.26` (systems of three linear equations in three variables), `GG.51` (construct a tangent to a circle from a point outside it), and `GG.52` (tangent-segment theorem). Preserve the standard's `*` marker on optional subclauses embedded within an entry.

All entries contain the original standard text; `verbatim` defaults to `true`. Formatting changes are limited to removing circled numerals, converting LaTeX formulas to plain text, incorporating footnotes into parenthetical text, and joining clauses split across pages.

### Stages 1–3 (added 2026-10-19)

Elementary domains use the same names as Stage 4: Number and Algebra, Geometry, Statistics and Probability, and Integrated Practice. Their codes remain NA / GG / SP / IP. IDs look like `cms-2022:1.NA.01`, `cms-2022:2.GG.03`, and `cms-2022:3.SP.02`; numbering starts at 01 and is consecutive within each stage and domain.

| Stage | Number and Algebra | Geometry | Statistics and Probability | Integrated Practice | Total |
|---|---:|---:|---:|---:|---:|
| 1 (Grades 1–2) | 8 | 3 | 1 | 6 | 18 |
| 2 (Grades 3–4) | 10 | 9 | 6 | 4 | 29 |
| 3 (Grades 5–6) | 10 | 12 | 7 | 1 | 30 |
| 4 (Grades 7–9) | 49 | 92 | 13 | 3 | 157 |
| Total | 77 | 116 | 27 | 14 | **234** |

Sources and text status (recorded in `source.note` and each elementary entry):

- Public transcription: 21st Century Education Network preview, <http://zy.21cnjy.com/20610065> (retrieved 2026-10-19). This is not a Ministry of Education page.
- The reference PDF remains <http://www.moe.gov.cn/srcsite/A26/s8001/202204/W020220510531636118932.pdf> (a scan; printed page = PDF page − 7). **Stages 1–3 were not checked page by page**, so `page_or_ref` is “pending verification,” `verbatim` is `false`, and `text_status` says “Public transcription; not checked page by page against the Ministry of Education PDF.”
- No clauses that could not be read in the transcription were invented, and no example numbers were assigned.
- **Percentages** appear in Stage 3 objectives and teaching guidance. None of the numbered Content Requirements read so far explicitly names percentages, so **no new percentage curriculum-standard clause was created**. Percentage topics were mapped to existing clauses with `confidence: inferred`; the `note` records that verification is pending.
- **Stage 3 Integrated Practice:** this transcription confirms only Thematic Activity 1 (using negative numbers to express opposite quantities, `cms-2022:3.IP.01`). Other theme names were not confirmed in the body text and are not listed separately.

The original 18 `cnm_ext_*` nodes were deleted (approach B); an empty `standards` array is no longer used to represent elementary topics. Every formal elementary topic has 1–2 mappings.

## 2. Mapping rules

Every topic in `topics.json` has a `standards` array (with the same fields for elementary and middle-school topics). Each element has this shape:

```json
{"id": "cms-2022:4.NA.17", "confidence": "exact", "note": "optional"}
```

- **`exact`:** The clause explicitly names the topic's core concept, skill, or theorem. Compare the topic name or mastery criteria with the clause and find matching wording. Example: `cnm_221 Completing the square` → `NA.27` (“solve … quadratic equations using completing the square, the quadratic formula, and factorization”).
- **`inferred`:** The clause does not name the topic, but the topic is a prerequisite concept, special case, extension, typical application, or textbook-level refinement. The standard may mention it only in its Academic Requirements, Teaching Guidance, or examples. **Every `inferred` mapping must include a `note`** explaining the connection. Example: `cnm_016 Reciprocals` → `NA.04`, note: “A reciprocal is a concept associated with division; it is not listed separately in the standard.”
- Map each topic to 1–3 clauses, preferring `exact`. Current distribution: 245 topics have 1 mapping, 66 have 2, 2 have 3, and 2 have none.
- A curriculum-standard clause may be cited by several topics. Clauses are often broad (for example, `GG.33` covers properties and criteria for isosceles triangles and properties and criteria for equilateral triangles), so it is normal for several topics to share an `exact` mapping. **`Exact` does not mean the topic and clause have the same granularity.**
- If the standard marks a clause as optional (`*`), map topics according to content; do not downgrade the mapping solely because it is optional.
- The standard distinguishes levels such as know, understand, master, explore, and prove. **The mappings do not record these levels.**

See Section 6 for the checks performed by `scripts/validate.py`.

## 3. Coverage

| Metric | Value |
|---|---|
| Total formal topics | 315 |
| Formal topics with non-empty `standards` | **313 (99.4%)** |
| Formal topics with empty `standards` | 2 |
| Topics with at least one `exact` mapping | 262 (83.2%) |
| Topics with only `inferred` mappings | 51 (16.2%) |
| Mapping count | 286 `exact`, 97 `inferred` (383 total) |

By domain (formal topics with non-empty mappings / total): Number and Algebra 142/142, Geometry 115/117, Statistics and Probability 43/43, Integrated Practice 13/13.

**Reverse coverage:** Of 157 curriculum-standard clauses, 142 are referenced by at least one topic and **15 have no corresponding topic** (see Section 5). Nine more clauses have only `inferred` mappings: `NA.08` (opposites and absolute values of real numbers), `NA.22` (algebraic reasoning), `NA.30` (checking whether an equation's solutions are reasonable), `GG.37` (centroid of a triangle), `GG.58` (counterexamples), `GG.88` (bearing and distance), `GG.92` (coordinates and similarity transformations), `IP.02`, and `IP.03`.

Integrated Practice: the standard has only three general clauses for this domain and does not divide them by specific content. All 13 Integrated Practice topics map to these three clauses. Topics whose mathematical content fits the contexts listed in `IP.01` (equations and inequalities, functions, transformations of figures, figures and coordinates, sampling and data analysis) are marked `exact`; `IP.02` and `IP.03` describe only the learning process, so their mappings are all `inferred`.

## 4. Unmapped topics (formal topics with empty `standards`)

| ID | Topic | Reason |
|---|---|---|
| `cnm_130` | Common auxiliary lines and models for congruent triangles | Doubling a median, extending a segment, and similar methods are problem-solving techniques; the standard has no corresponding Content Requirement. Mapping them strongly to every congruent-triangle clause would overstate the connection. |
| `cnm_192` | Folding and moving-point problems in quadrilaterals | This is an integrated problem-solving type that combines folding (reflection), moving points, the Pythagorean theorem, and equations. The standard has no corresponding clause, and there is no single primary clause to choose. |

## 5. Curriculum-standard clauses without corresponding topics (possible gaps in the topic system)

No topic references these clauses. Most concern constructions, appreciation, or extensions for which the graph has no corresponding topic:

| Curriculum-standard clause | Content |
|---|---|
| `NA.05` | Use rational-number operations to solve simple problems. |
| `GG.05` | Understand the meaning of the distance between two points; measure and express that distance. |
| `GG.20` | Use a set square and ruler to draw a line parallel to a given line through a point outside that line. |
| `GG.21` | Use ruler-and-compass construction to draw a line parallel to a given line through a point outside that line. |
| `GG.38` | Construct triangles with a ruler and compass (given three sides, two sides and their included angle, or two angles and their included side; construct an isosceles triangle given its base and altitude; construct a right triangle given one leg and the hypotenuse). |
| `GG.42` | Understand the distance between two parallel lines and measure that distance. |
| `GG.51` | *Optional:* construct a tangent to a circle from a point outside the circle. |
| `GG.59` | Understand proof by contradiction through examples. |
| `GG.63` | Recognize and appreciate reflection-symmetric figures in nature and everyday life. |
| `GG.66` | Explore the central-symmetry properties of segments, parallelograms, regular polygons, and circles. |
| `GG.67` | Recognize and appreciate centrally symmetric figures in nature and everyday life. |
| `GG.69` | Recognize and appreciate applications of translation in nature and everyday life. |
| `GG.70` | Design patterns using reflection, rotation, and translation of figures. |
| `GG.84` | Understand real-life applications of views and nets through examples. |
| `SP.06` | Participate in data-classification activities and learn to classify data using the principle of minimizing the sum of squared deviations within groups (Example 85). |

No topics were added in this pass, as requested. Keep this list for a future decision about whether to add topics.

## 6. Validation

In addition to its existing checks, `python3 scripts/validate.py` does the following:

- If `data/cn-curriculum-standards.json` exists, check its required `source` fields, entry-ID format and consecutive numbering within each domain, consistency between `domain` and the domain code in each ID, and that `text` is in Chinese.
- Each `standards[].id` must appear in `items[].id` in that file. `confidence` must be `exact` or `inferred`; a topic cannot cite the same entry more than once or cite more than three entries. A topic that references `standards` when the standards file is missing is also an error.
- Print curriculum-standard entry counts by domain; counts and percentages of formal topics with non-empty or empty `standards`; counts of `exact` and `inferred` mappings; and the number of clauses with no corresponding topic.
- If a formal topic has an empty `standards` array, print it in a WARNING list (up to 30 topics); **this does not affect the exit code**. Set `STRICT_STANDARDS=1` to treat this as an error and return exit code 1.

## 7. Known limitations

- **Curriculum clauses and textbook topics have different granularity:** clauses are broad, while textbook and graph topics are more specific. One-to-many and many-to-one relationships are common. `exact` means only that a clause mentions the topic; it does not mean their scopes are identical. Mapping counts alone cannot show whether the clauses are fully covered.
- **Requirement levels are not recorded:** the standard distinguishes knowing, understanding, mastering, exploring, and proving, each at a different depth. Mappings do not reflect these levels, and topic `mastery_criteria` have not been calibrated to them.
- **Textbook content beyond or more specific than the standard:** examples include properties of right triangles with a 30° angle (`cnm_140`), solving by taking square roots (`cnm_220`), reciprocals, linear pairs, and applications of rotation and geometric proof. The standard does not list these separately, so they can only be mapped as `inferred`. Conversely, see Section 5 for clauses that lack corresponding topics.
- **Optional content and “not required for exams” are not propagated to topics:** topics have no optional flag. When needed, consult the `elective` clause (`cnm_093` systems of three linear equations in three variables; `cnm_263` tangent-segment theorem).
- **Topics grouped by problem type:** the standard has no corresponding clauses for topics such as application-problem types, “integrated applications,” or “common auxiliary lines,” so their mappings are subjective.
- **Integrated Practice has only three general clauses:** mappings for the 13 Integrated Practice topics are not very discriminating. They show only that a topic belongs to this domain, not how a specific activity aligns with the standard.
- **Textbook edition:** topic order follows the 2024 PEP edition, while the curriculum standard is the 2022 edition. Their chapters, examples, and optional-content scopes differ. The Grade 9, Volume 2 contents are themselves from a third-party source (see the README), so some mappings may not match the standard because of textbook coverage.
- **Curriculum-standard text came from recognition:** see Section 1; only two pages were spot-checked.
- **Stages 1–3 have not been checked page by page against the Ministry of Education PDF.** Page references and some wording (for example, whether the transcription's “proportional” should read “directly proportional”) remain pending verification.
- **No human review:** AI made all `confidence` and `note` judgments.

## 8. Current whole dataset (2026-10-19, including elementary topics)

| Metric | Value |
|---|---|
| Curriculum-standard clauses | 234 (77 in Stages 1–3 + 157 in Stage 4) |
| Formal topics | 531 (216 elementary, 315 middle school) |
| Non-empty `standards` | **529 / 531** |
| Still empty | `cnm_130`, `cnm_192` (unchanged from Round 3; no mappings were added) |
| Mapping count | 512 `exact`, 128 `inferred` (640 total) |
| Topics with at least one `exact` mapping | 448 |
| Referenced curriculum-standard clauses | 202 / 234 |
| Clauses with no corresponding topic | **32** |

Of the 28 clauses, the 15 Stage 4 clauses remain those listed in Section 5. Another 17 clauses from Stages 1–3 are not referenced by any topic (most are broad statements about developing spatial awareness / sense of quantity or process requirements that were not split into separate topics):

| Curriculum-standard clause | Content (transcription; pending verification) |
|---|---|
| `1.NA.06` | Experience the meaning of numbers and operations while solving problems in everyday contexts. |
| `1.GG.03` | Develop an initial sense of space and quantity through recognizing and measuring figures. |
| `1.IP.06` | Use mathematics learned to record personal experiences or tell a short story involving mathematics. |
| `2.NA.07` | Use a calculator to calculate, solve simple problems, and explore simple patterns. |
| `2.NA.09` | Understand in a specific context that quantities equal to the same quantity are equal. |
| `2.GG.07` | Strengthen spatial awareness and sense of quantity through recognizing and measuring figures. |
| `2.GG.09` | Develop spatial awareness while experiencing the positions and movements of figures. |
| `2.SP.04` | Read simple statistical charts and tables in the media. |
| `2.SP.06` | Reasonably use charts, tables, and averages in simple contexts. |
| `2.IP.04` | Know that the Qin dynasty unified systems of weights and measures (a research-type theme). |
| `3.GG.07` | Further develop a sense of quantity, spatial awareness, and geometric intuition through recognizing and measuring figures. |
| `3.GG.12` | Appreciate patterns formed by translation, rotation, and reflection, and design simple patterns on grid paper. |
| `3.SP.01` | Collect, organize, and analyze data, and describe conclusions. |

Elementary topics: all 216 have mappings; 175 have one mapping and 41 have two. Middle-school mapping counts remain at Round 3 levels: 286 `exact` + 97 `inferred`. New elementary mappings are 226 `exact` + 31 `inferred`.

## 9. High-school compulsory (2026-10-20)

Based on the five themes in the compulsory course of the *General High School Mathematics Curriculum Standards (2017 Edition, Revised in 2025)*. The issuance notice is at <http://www.moe.gov.cn/srcsite/A26/s8001/202006/t20200603_462199.html>. The PDF at <https://www.pep.com.cn/xw/zt/rjwy/gzkb2020/202205/P020220517519489596282.pdf> was consulted, but **not checked page by page**. All 48 entries have `verbatim: false`, `page_or_ref` set to “pending verification,” and `text_status` identifying them as public paraphrases.

IDs in the form `cms-2017:H.<module>.NN` are organized by theme for this graph; they are not the Ministry of Education's original IDs. Modules do not map one-to-one to domains:

| Module | Count | Themes |
|---|---:|---|
| PRE | 9 | Preparatory topics (sets, common logical language, equality and inequality relationships, and viewing quadratic equations and inequalities through functions) |
| FUN | 17 | Functions (concepts and properties, power / exponential / logarithmic functions, trigonometric functions, and applications of functions) |
| GA | 12 | Geometry and Algebra (plane vectors and applications, complex numbers, and introductory solid geometry). Complex numbers are assigned to Number and Algebra; vectors and solid geometry are assigned to Geometry. |
| PS | 8 | Probability and Statistics |
| MI | 2 | Mathematical modeling activities and mathematical inquiry activities |

Each high-school compulsory topic maps to one clause: 48 `exact` and 95 `inferred` mappings (`inferred` entries all have a `note` and are marked pending verification). No clause was created for 7.3, the trigonometric form of complex numbers. The 28 compulsory-education clauses that previously had no corresponding topic were not cited by this later expansion.

## 10. High-school selective compulsory (2026-10-20)

Based on the selective-compulsory course in the same standard; it was still **not checked page by page**. Added 32 entries, numbered after the compulsory entries. All have `verbatim: false` and `page_or_ref` set to “pending verification.”

| Module | Added | IDs |
|---|---:|---|
| FUN | 8 | `FUN.18`–`FUN.25` (sequences and derivatives) |
| GA | 11 | `GA.13`–`GA.23` (spatial vectors, lines and circles, and conic sections) |
| PS | 11 | `PS.09`–`PS.19` (counting principles, probability, and statistics) |
| MI | 2 | `MI.03`–`MI.04` (statistical modeling and Pascal's triangle inquiry) |

Each of the 128 selective-compulsory topics maps to one clause. New mappings: 60 `exact` and 68 `inferred`.

| Metric | Value |
|---|---|
| Curriculum-standard clauses | 314 (234 compulsory education + 48 high-school compulsory + 32 selective-compulsory) |
| Formal topics | 802 (216 elementary, 315 middle school, 143 high-school compulsory, 128 selective-compulsory) |
| Non-empty `standards` | **800 / 802** |
| Still empty | `cnm_130`, `cnm_192` |
| Mapping count | 620 `exact`, 291 `inferred` |
| Topics with at least one `exact` mapping | 556 |
| Referenced curriculum-standard clauses | 282 / 314 |
| Clauses with no corresponding topic | 28 (the original compulsory-education math clauses) |

## 11. Elementary English (2026-10-20)

Based on public paraphrases of Levels 1 and 2 in the *English Curriculum Standards for Compulsory Education (2022 Edition)*; they were **not checked page by page**. Added 35 entries, all with `verbatim: false` and `page_or_ref` set to “pending verification.” IDs in the form `ces-2022:<level>.<domain>.NN` were created for this graph and are not the Ministry of Education's original IDs. The math-standard `source` was not changed; English sources are recorded in the same file's `english` object.

| Level | Code | Count | Domain |
|---|---|---:|---|
| 1 (Grades 3–4) | PH | 5 | Phonology |
| 2 (Grades 5–6) | PH | 2 | Phonology |
| 1 | VO | 1 | Vocabulary |
| 2 | VO | 2 | Vocabulary |
| 1 | GR | 7 | Grammar |
| 2 | GR | 9 | Grammar |
| 1 | FU | 3 | Functional language |
| 2 | FU | 2 | Functional language |
| 1 | RW | 2 | Reading and writing |
| 2 | RW | 2 | Reading and writing |

Each of the 208 elementary English topics maps to one clause. The vocabulary list was not copied word for word from the appendix. All 35 clauses are currently referenced. The 28 compulsory-education math clauses that previously had no corresponding topic were not cited by these additions.

The 37 Level 3 middle-school English clauses (`ces-2022:3.*`, added 2026-10-21) are also public paraphrases, all pending verification, and are recorded in the same file's `english` object; they are not detailed here.

## 12. High-school English (2026-10-21)

Based on public paraphrases of the compulsory and selective-compulsory courses in the *General High School English Curriculum Standards (2017 Edition, Revised in 2020)*; they were **not checked page by page**. This is not a separate high-school English standard issued in 2022. Added 44 clauses, all with `verbatim: false`, `page_or_ref` set to “pending verification,” and `text_status` stating that they were not checked page by page against the standard. IDs in the form `ces-2017:H.<B|S>.<PH|VO|GR|FU|RW>.NN` were created for this graph: `B` means compulsory and `S` means selective compulsory; these are not the Ministry of Education's original IDs. The math-standard `source` was not changed. `english.title` remains the *English Curriculum Standards for Compulsory Education (2022 Edition)* (`year: 2022`). High-school sources are in `english.senior` (as of 2026-10-22, citing the *General High School English Curriculum Standards (2017 Edition, Revised in 2025)*, `year: 2025`; the clauses were not rechecked against the 2025 revision; issuance notice: <http://www.moe.gov.cn/srcsite/A26/s8001/202006/t20200603_462199.html>).

| Course | Code | Count | Domain |
|---|---|---:|---|
| Compulsory | PH | 3 | Phonology |
| Selective compulsory | PH | 2 | Phonology |
| Compulsory | VO | 4 | Vocabulary |
| Selective compulsory | VO | 4 | Vocabulary |
| Compulsory | GR | 11 | Grammar |
| Selective compulsory | GR | 8 | Grammar |
| Compulsory | FU | 3 | Functional language |
| Selective compulsory | FU | 3 | Functional language |
| Compulsory | RW | 3 | Reading and writing |
| Selective compulsory | RW | 3 | Reading and writing |

Each of the 259 high-school English topics maps to one clause. Compulsory topics map only to `H.B`; selective-compulsory topics map only to `H.S`. Uses not explicitly named in the standard (for example, absolute constructions, mixed-time conditionals, and “but for”) are marked `inferred`. All 44 clauses are currently referenced. The 28 compulsory-education math clauses that previously had no corresponding topic were not cited. Neither the vocabulary list nor unit contents were checked page by page.

## 13. Middle-school physics (2026-10-22)

Based on the Content Requirements in the “Curriculum Content” section of the *Physics Curriculum Standards for Compulsory Education (2022 Edition, Revised in 2025)* (the 2025 routine revision, Textbook [2025] No. 1). The curriculum-standard PDF is a scan. OCR text was manually checked against page images (correcting similar-looking characters such as those meaning “routine,” “self,” and “related to”), but **was not checked character by character against a printed copy**. All entries have `verbatim: false`; `page_or_ref` contains PDF page numbers. Added 89 entries using IDs in the form `cps-2022:<primary-theme>.<secondary-theme>.<number>`, matching the original three-level clause numbering: Matter 12, Motion and Interaction 24, Energy 23, Experimental Inquiry 21, and Interdisciplinary Practice 9. Sources are recorded in the same file's `physics` object; the math `source` was not changed.

Each of the 92 physics topics maps to 1–3 clauses, for 162 mappings total (128 `exact`, 34 `inferred`). Sections with student-required experiments (measuring length, speed, or density; using a spring scale; investigating friction; liquid pressure; buoyancy; levers; reflection; plane-mirror imaging; convex-lens imaging; ammeters; voltmeters; the voltmeter-ammeter method; current and voltage in series and parallel circuits; relationships among current, voltage, and resistance; energized solenoids; and electromagnetic induction) also map to the experiment clauses under 4.1 / 4.2. “Interdisciplinary Practice” sections map to 5.x clauses.

Three clauses currently have no corresponding topic: `cps-2022:1.3.3` (understand the broad history of human exploration of the solar system and the universe, …), `cps-2022:2.1.3` (give examples of the many forms of motion in nature, …), and `cps-2022:3.2.4` (name some machines used by humans; understand machines' …). The PEP edition does not give these topics separate sections; related content is distributed across other sections.
