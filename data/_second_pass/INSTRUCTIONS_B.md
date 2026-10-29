# Blind-solving instructions (Round B, more carefully)

You are a middle-school math problem solver. Your task is to solve a batch of problems independently. **Do not know or look up the answer key.** Working directory: `/Users/a111/projects/12grades`. In the instructions below, `NN` is your two-digit batch number (for example, `03`).

Input: `data/_second_pass/blind_b_NN.json` (read it with Read; it is a JSON array, and each item has `id`, `type`, and `prompt`; multiple-choice items also have `choices`, and numeric items may have `note`).

Write two output files:
1. `data/_second_pass/ans_b_NN.json` — an object such as `{"question-id": "your answer"}`. Include every input problem, and make every value a string.
2. `data/_second_pass/work_b_NN.json` — an object such as `{"question-id": "one or two sentences with the derivation/checking points"}`. Include an entry for every problem (for example, key equations or intermediate results; for multiple-choice items, explain how you assessed each option).

Answer format:
- `type=numeric`: Write only the number (integer, decimal, fraction `a/b`, or negative number). Separate multiple answers with the full-width comma `，` in the order requested by the prompt; if the prompt does not specify an order, list them in ascending order. Do not include units, radicals, π, percent signs, or an `"x="` prefix. Follow any instructions in the prompt about decimal places or reducing fractions.
- `type=choice`: Write only the option letter, such as `"B"`. Check **every option** and answer only if exactly one option is correct.
- `type=short`: Write the shortest answer that suffices.

Strict rules (this is an independent review; compromising independence makes it meaningless):
1. **Read only** your `blind_b_NN.json` file and this instruction file. Do not read, search, or grep `data/questions.json`, `data/_qbatches/`, `data/verification_report.json`, `data/second_pass_log.json`, any other files under `data/_second_pass/`, `scripts/`, or `diagnostic_question` in `topics.json`.
2. **Do not answer the whole batch at once by intuition.** Split it into small batches (for example, 10 problems at a time) and reason through each problem. Use `python3` in Bash to calculate every nontrivial arithmetic problem, equation, geometry calculation, and probability count (`fractions.Fraction` for exact arithmetic, `math` for trigonometry and radicals, and `itertools` for counting permutations and combinations). Then write the answers. Append each batch's answers and derivations to the two files above; make sure both files are complete, valid JSON at the end.
3. For geometry problems, use only the conditions stated in the prompt; do not add your own. If a prompt is ambiguous, its conditions conflict, or a multiple-choice problem has no correct option or more than one correct option, still give the most reasonable answer you can. Begin that problem's derivation in `work` with the fixed tag `【存疑】`.
4. After writing the files, check that every `id` is covered and that both files are valid JSON (read them with `python3` and verify the item counts).

After you finish, reply with one sentence only: the number of problems and how many are marked `【存疑】`. Do not include the problems or answers.
