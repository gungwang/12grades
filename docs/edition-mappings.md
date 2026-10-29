# Contributing textbook-edition mappings

For Issue #11 (Shanghai Edition and other textbook editions).

## Approach

Do not create a separate topic database for the Shanghai Edition. Topics in `data/topics.json` remain organized according to the People's Education Press (PEP) edition: `grade`, `semester`, and `chapter` refer to its volumes and chapters, and PEP is the default. Mappings for other editions answer just one question: **which volume and unit cover the same topic in that edition?**

All editions share the same topics, prerequisite edges, question bank, and curriculum-standard mappings. Editions differ in which topics they include and how finely they divide them, so these mappings show only an approximate location and do not guarantee one-to-one correspondence.

## Data format

### 1. Optional `mappings` field on a topic

```json
{
  "id": "cnm_p158",
  "name": "Greatest common divisor",
  "grade": 5,
  "semester": "下",
  "chapter": "Grade 5, Volume 2, Unit 2: Factors and Multiples",
  "mappings": {
    "hujiao_math": {"grade": 5, "term": "上", "unit": "Unit name", "chapter": "Chapter name"}
  }
}
```

The values above illustrate the structure; they are not a real mapping.

- `mappings` is an object whose keys are **edition IDs**: lowercase letters, digits, and underscores, in the form `<edition pinyin>_<subject>`. For example, `hujiao_math` is the Shanghai Edition, `sujiao_math` is the Jiangsu Education Edition, and `beishida_math` is the Beijing Normal University Press Edition. Use the same format for Jiangsu Education, Beijing Normal University Press, and other editions.
- **Do not** include the PEP edition in `mappings` (`renjiao_math` and `pep_math` will fail validation). The topic's own `grade`, `semester`, and `chapter` fields already describe the PEP edition.
- Each value is a mapping entry:

| Field | Required | Description |
|---|---|---|
| `grade` | Yes | Grade in this edition, as an integer (1–9; use this repository's 10–14 numbering for high school) |
| `term` | Yes | `上` / `下` / `全` (the Shanghai Edition calls these the first and second semesters; use `上` and `下`, respectively) |
| `unit` | No | Unit or chapter name; a non-empty string |
| `chapter` | No | Section or lesson name; a non-empty string |
| `note` | No | Explain differences in topic coverage, combined or split topics, and other relevant details |

- **Do not** add a `mappings` field to a topic with no mapping (an empty object will fail validation). Omitting the field does not cause a validation error.
- No topic in `topics.json` currently has a `mappings` field.

### 2. Contribution file: `data/mappings/<edition-id>.json`

Editing `topics.json` directly is difficult to review because it is a large file. Submit mappings in a separate, smaller file; after review, a maintainer will merge them into the relevant topics' `mappings` fields.

```json
{
  "edition": "hujiao_math",
  "label": "Shanghai Edition mathematics (Shanghai Education Press)",
  "status": "draft",
  "source": "Mapping sources: textbook title, edition, table of contents or URL, and date checked",
  "entries": [
    {"topicId": "cnm_p158", "grade": 5, "term": "上", "unit": "…", "chapter": "…"}
  ]
}
```

- `status`: `example` (format demonstration only), `draft` (has sources but needs verification), or `reviewed` (another person checked it against the textbook). `draft` and `reviewed` entries must include `source`.
- The filename must start with the `edition` value. Example files use `<edition>.example.json`, must have `status: "example"`, and may contain at most 10 entries.
- Each `entries[].topicId` must refer to an existing formal math topic, and IDs must not repeat within a file. The rules for `grade`, `term`, `unit`, `chapter`, and `note` are the same as above.

The repository's `data/mappings/hujiao_math.example.json` contains only six **placeholder** entries. They have not been checked against the Shanghai Edition textbook and must not be used as its table of contents.

## How to submit a PR

1. Make sure you have verifiable sources: a textbook table of contents, a teacher's-edition table of contents, or a public table of contents from an education authority or publisher. Record the edition and the date you checked it. **Do not fill in mappings from memory** or copy an entire page from another website.
2. Copy the example file to `data/mappings/<edition-id>.json`, change `status` to `draft`, and fill in `label` and `source`.
3. Find the corresponding topics by grade in `data/topics.json`. Add `topicId`, `grade`, and `term` for each one; add `unit` when the table of contents provides a unit name. **Submit one grade or volume at a time** to make review easier.
4. If editions differ in coverage (a topic is absent or several topics are combined), omit absent topics and explain combined topics in `note`.
5. Run `python3 scripts/validate.py` locally. It should print `VALIDATION PASSED` and show your entry count on the `Textbook edition mappings` line.
6. Submit a PR. State your sources and coverage in its description (for example, “Shanghai Edition, Grade 1, first and second semesters; X topics mapped”). Do not claim that an entire volume is aligned.

## Current status and limitations

- The frontend does **not** read mapping data yet. The graph and diagnostic tool still display grades and volumes according to the PEP edition. In a child's profile, “textbook edition” is only a note (see `docs/pwa.md`).
- Future frontend behavior: if a user selects a non-PEP edition and a topic has no corresponding `mappings` entry, continue to display its PEP grade and show “Mappings for this edition are incomplete.” Do not hide a topic because its mapping is missing.
- Incomplete mapping coverage is normal. Do not add placeholder values just to fill gaps.
