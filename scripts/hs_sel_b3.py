"""People's Education Press A Edition (2019), Selective Required Volume III.

The chapter structure is compiled from the following third-party sources; none is the publisher's official website. Page numbers are omitted and details remain to be verified:
- Teacher's Home https://www.renjiaoshe.com/jiaocai/2074.html
  (6.1–6.3, 7.1–7.5, 8.1 Correlation Between Paired Data, 8.2, and 8.3 Categorical Variables and Contingency Tables;
   the table of contents does not list mathematical inquiry or mathematical modeling separately)
- Haoduo E-Textbooks https://www.haoduoyun.cc/book/rjb/shuxue/bwx3.shtml
  (6.1–6.3, mathematical inquiry: "Properties and Applications of Pascal's Triangle", 7.1–7.5,
   8.1 Statistical Correlation of Paired Data, 8.2 Simple Linear Regression Models and Their Applications,
   8.3 Contingency Tables and Tests of Independence, and "Mathematical Model: Building Statistical Models for Prediction")
- Xuexili http://www.xuexili.com/keben/70201.html
  (6.1–6.3, 7.1–7.5, 8.1 Correlation, and 8.3 Contingency Tables and Tests of Independence)
- Linfen Education Advancement Exam Network https://www.linfenk12.com/7302.html
  (8.1 Correlation and 8.3 Contingency Tables and Tests of Independence)

The section names for 8.1 and 8.3 differ by source. Topic names follow Haoduo E-Textbooks, with alternatives noted in the notes.
Only the two mathematical inquiry/modeling activities explicitly named by a source are included. Haoduo E-Textbooks calls the modeling activity "Mathematical Model"; this plan labels it "Mathematical Modeling" pending verification.
Page numbers are not included.
"""
from hs_sel_common import questions, topic

SP = "Statistics and Probability"
IP = "Integrated Practice"

C6 = "Chapter 6: Counting Principles"
C7 = "Chapter 7: Random Variables and Their Distributions"
C8 = "Chapter 8: Statistical Analysis of Paired Data"


def T(key, chapter, section, name, domain, typ, desc, crit, std, conf="exact", note=None):
    topic(key, 3, chapter, section, name, domain, typ, desc, crit, std, conf, note)


def Qs(key, items):
    questions(key, items)


def n(prompt, verify, expl):
    return ("n", prompt, verify, expl)


def c(prompt, ok, bad, expl):
    return ("c", prompt, ok, bad, expl)


NOTE = "The textbook practices this requirement in separate parts. To verify."
NOTE81 = "The 8.1 section name follows Haoduo E-Textbooks: 'Statistical Correlation of Paired Data.' Teacher's Home and Xuexili use 'Correlation Between Paired Data.' To verify."
NOTE83 = "The 8.3 section name follows Haoduo E-Textbooks and the Linfen table of contents: 'Contingency Tables and Tests of Independence.' Teacher's Home uses 'Categorical Variables and Contingency Tables.' To verify."

# ---------------------------------------------------------------- Chapter 6

T("cnt.add", C6, "6.1", "Addition Principle for Counting", SP, "conceptual",
  "If an activity can be completed using one of several mutually exclusive categories of methods, the total number of methods is the sum of the counts in each category.",
  ["Determine when to count by mutually exclusive cases and add", "Count the total number of methods across mutually exclusive categories"],
  "PS.09")
Qs("cnt.add", [
    n("There are 3 bus services and 2 train services from Town A to Town B. A traveler can use only one mode. How many ways are there to travel?", "3+2",
      "The categories are mutually exclusive, so add: 3+2=5."),
    n("A shelf has 4 math books and 5 language-arts books. If you choose 1 book, how many choices are there?", "4+5",
      "Choose either a math book or a language-arts book, so add the counts: 4+5=9."),
    c("When does the addition principle for counting apply?", "The categories of methods are mutually exclusive, and choosing one category is enough to complete the activity",
      ["Every category must be completed once", "Each step must be followed by another step", "Methods may belong to both categories and still be added"],
      "The categories must not overlap; completing any one of them finishes the activity. Overlapping categories cannot be added directly."),
    n("Six people signed up for singing and four for dancing. No one signed up for both. How many people signed up in total?", "6+4",
      "The groups do not overlap, so 6+4=10."),
])

T("cnt.mul", C6, "6.1", "Multiplication Principle for Counting", SP, "conceptual",
  "If an activity requires several successive steps, multiply the number of choices at each step to get the total number of methods.",
  ["Determine when to count by successive steps and multiply", "Calculate the product of the number of choices at each step"],
  "PS.09")
Qs("cnt.mul", [
    n("There are 3 shirts and 4 pairs of pants. Choosing one of each gives how many outfits?", "3*4",
      "Choose a shirt and then pants: 3×4=12."),
    n("There are 2 routes from A to B and 3 from B to C. How many routes go from A through B to C?", "2*3",
      "There are two successive choices: 2×3=6."),
    c("When does the multiplication principle for counting apply?", "Every step must be completed in sequence for the activity to be complete",
      ["Completing any one step is enough", "The number of choices at each step should be added", "The steps can be rearranged into mutually exclusive categories"],
      "In a sequence of steps, every step must be completed. Multiply the number of choices at each step."),
    n("A three-digit code uses digits 0 through 9, with repetition allowed. How many codes are possible?", "10*10*10",
      "Each of the three positions has 10 choices, so 10×10×10=1000."),
])

T("cnt.mix", C6, "6.1", "Combined Case and Step Counting", SP, "procedural",
  "When a problem involves both cases and successive steps, identify which counts should be added and which should be multiplied, then combine them.",
  ["Use both addition and multiplication in one counting problem", "Write a counting expression step by step"],
  "PS.09", "inferred", NOTE)
Qs("cnt.mix", [
    n("Choose 1 representative from 3 boys and 2 girls, then give that person 1 of 4 notebooks. How many ways can this be done?", "(3+2)*4",
      "Choosing a person is a case count, so add to get 5. Choosing a notebook is the next step: 5×4=20."),
    n("You can travel to Beijing by 2 flights or 3 high-speed trains. After arriving, choose 1 of 4 hotels. How many itineraries are possible?", "(2+3)*4",
      "Add the mutually exclusive travel choices to get 5, then multiply by the 4 hotel choices: 20."),
    c("Choose a mode of transport first, then a hotel. Transport options are flights and high-speed trains. How should the count be calculated?", "Add the transport choices, then multiply by the number of hotels",
      ["Add all transport and hotel choices", "Count only the hotels", "Multiply the flight and train counts, then add the hotels"],
      "Transport modes are mutually exclusive, so add them. Choosing a hotel is a further step, so multiply."),
    n("There are 2 breakfast options and 3 lunch options. Choosing one of each gives how many combinations?", "2*3",
      "Both steps are required, so 2×3=6."),
])

T("arr.def", C6, "6.2", "Concept of a Permutation", SP, "conceptual",
  "A permutation is an ordered arrangement of k elements selected from n distinct elements. Different orders count as different permutations.",
  ["Explain that permutations depend on order", "Calculate small permutation counts"],
  "PS.10")
Qs("arr.def", [
    c("Which situation is a permutation?", "Choose 2 of 4 students and arrange them in order",
      ["Choose 2 of 4 students to form a group, ignoring order", "Put 4 books in a pile without distinguishing left from right", "Care only about which people were selected"],
      "A permutation arranges items in order. A selection without order is a combination."),
    n("How many ways can 2 of 4 distinct elements be arranged in a row?", "perm(4,2)",
      "There are 4 choices for the first position and 3 for the second: 4×3=12."),
    n("How many ways can the distinct letters A, B, and C be arranged in a row?", "perm(3,3)",
      "There are 3×2×1=6 arrangements."),
    c("When are two permutations considered the same?", "They contain the same selected elements in the same order",
      ["Whenever they contain the same selected elements", "Whenever they contain the same number of elements", "Whenever their first positions match"],
      "A permutation depends both on which elements are chosen and on their positions."),
])

T("arr.num", C6, "6.2", "Permutation Formula", SP, "procedural",
  "The number of permutations is A(n,k)=n!/(n−k)!, the product of k consecutive decreasing integers starting at n.",
  ["Calculate permutation counts", "Explain the permutation formula"],
  "PS.10")
Qs("arr.num", [
    n("What is A(6,2)?", "perm(6,2)",
      "6×5=30."),
    n("What is A(5,1)?", "perm(5,1)",
      "Selecting one element gives 5 arrangements."),
    n("What is A(4,4)?", "factorial(4)",
      "The 4 elements can be arranged in 4×3×2×1=24 ways."),
    c("How can A(n,k) be written?", "n factorial divided by (n−k) factorial",
      ["n factorial multiplied by k factorial", "k factorial divided by n factorial", "n plus k"],
      "A(n,k)=n!/(n−k)!, where k cannot exceed n."),
])

T("arr.app", C6, "6.2", "Simple Applications of Permutations", SP, "application",
  "Count queues, assignments to distinct roles, and numbers with no repeated digits as ordered selections.",
  ["Determine whether a practical problem involves permutations", "Use a permutation count to express the result"],
  "PS.10", "inferred", NOTE)
Qs("arr.app", [
    n("Five students line up for a photo, and everyone must stand in line. How many lineups are possible?", "factorial(5)",
      "Arrange all 5 students: 5×4×3×2×1=120."),
    n("How many ways can 7 different books be distributed to Alice, Ben, and Chris, one book each?", "perm(7,3)",
      "The recipients are distinct, so assignments are ordered: A(7,3)=7×6×5=210."),
    n("How many three-digit numbers can be made from 1, 2, 3, and 4 if each digit is used at most once?", "perm(4,3)",
      "The hundreds, tens, and units places form an ordered selection: A(4,3)=24."),
    c("Three different books are distributed to three different people, one book each. What counting method applies?", "A permutation of 3 elements",
      ["A combination selecting 1 of the 3 books", "Adding the number of books", "A count that ignores who receives each book"],
      "The recipients are distinct, so who gets each book matters. Count all permutations."),
])

T("com.def", C6, "6.2", "Concept of a Combination", SP, "conceptual",
  "A combination is a selection of k elements from n distinct elements where only the selected elements matter, not their order.",
  ["Distinguish combinations from permutations", "Calculate small combination counts"],
  "PS.10")
Qs("com.def", [
    c("Which situation is a combination?", "Choose 2 of 4 students to attend a meeting, without assigning an order",
      ["Choose 2 of 4 students and arrange them in a line", "Make a three-digit number from 3 distinct digits", "Arrange 5 people in different positions in a line"],
      "A combination depends only on which people are selected, not their order."),
    n("How many ways can 2 of 4 distinct elements be selected when order does not matter?", "comb(4,2)",
      "There are 12 ordered arrangements. Each combination corresponds to 2 permutations, so 12/2=6."),
    n("How many ways can 2 of 5 students be selected for classroom duty when order does not matter?", "comb(5,2)",
      "C(5,2)=10."),
    c("If a group of selected elements is merely reordered, how should it be counted as a combination?", "As the same combination",
      ["As a different combination", "As the factorial of the permutation count", "It can no longer be called a combination"],
      "Combinations ignore order, so reordering does not create a new combination."),
])

T("com.num", C6, "6.2", "Combination Formula", SP, "procedural",
  "The number of combinations is C(n,k)=n!/(k!(n−k)!), or the permutation count divided by k factorial.",
  ["Calculate combination counts", "Know that C(n,0)=1"],
  "PS.10")
Qs("com.num", [
    n("What is C(6,2)?", "comb(6,2)",
      "6×5/2=15."),
    n("What is C(5,0)?", "comb(5,0)",
      "Selecting no elements gives one empty selection."),
    n("What is C(10,3)?", "comb(10,3)",
      "10×9×8/(3×2×1)=120."),
    c("What is the relationship between C(n,k) and A(n,k)?", "The combination count equals the permutation count divided by k factorial",
      ["The combination count equals the permutation count multiplied by k", "The combination count equals n factorial", "They are always equal"],
      "Each combination has k! internal orderings, so C(n,k)=A(n,k)/k!."),
])

T("com.prop", C6, "6.2", "Properties of Combination Numbers", SP, "reasoning",
  "Combination numbers satisfy C(n,k)=C(n,n−k) and the adjacent-term identity C(n,k)+C(n,k−1)=C(n+1,k).",
  ["Use symmetry to calculate combination numbers", "Check combination numbers using the addition identity"],
  "PS.10", "inferred", NOTE)
Qs("com.prop", [
    n("Given C(8,3)=C(8,5), what is C(8,5)?", "comb(8,5)",
      "C(8,5)=C(8,3)=56."),
    n("What is C(6,2)+C(6,3)?", "comb(6,2)+comb(6,3)",
      "15+20=35, which also equals C(7,3)."),
    c("Which expression equals C(n,k)?", "C(n,n−k)",
      ["C(k,n)", "C(n,k)+n", "A(n,n−k)"],
      "Selecting k elements and leaving n−k are two views of the same selection, so C(n,k)=C(n,n−k)."),
    n("What is C(5,1)+C(5,2)?", "comb(5,1)+comb(5,2)",
      "5+10=15."),
])

T("com.app", C6, "6.2", "Simple Applications of Combinations", SP, "application",
  "Use combinations when selecting people or objects without regard to order. If selections are made separately by category, multiply the combination counts.",
  ["Determine when a practical problem calls for combinations rather than permutations", "Calculate combination counts for selections by category"],
  "PS.10", "inferred", NOTE)
Qs("com.app", [
    n("How many ways can 3 of 6 students be selected for an activity when order does not matter?", "comb(6,3)",
      "C(6,3)=20."),
    n("From 5 boys and 4 girls, how many ways can 2 boys and 1 girl be selected?", "comb(5,2)*comb(4,1)",
      "Choose the boys in C(5,2)=10 ways and the girl in C(4,1)=4 ways. Multiply to get 40."),
    n("A batch of 10 products has 2 defective items. How many ways are there to select 3 products with exactly 1 defective item?", "comb(2,1)*comb(8,2)",
      "Choose 1 of the 2 defective items and 2 of the 8 good items: 2×28=56."),
    c("How should 3 people be selected from a group of 8 to form a team with no assigned roles?", "Use the combination count C(8,3)",
      ["Use the permutation count A(8,3)", "8+3", "8 factorial"],
      "Order does not matter within the team, and there are no distinct roles, so use a combination."),
])

T("bin.thm", C6, "6.3", "Binomial Theorem", SP, "conceptual",
  "The expansion of (a+b)^n is the sum of terms C(n,k) a^(n−k) b^k, with k ranging from 0 to n.",
  ["State the number of terms in an expansion", "Find the binomial coefficient of a specified term"],
  "PS.11")
Qs("bin.thm", [
    n("What is the coefficient of x² in the expansion of (1+x)^3?", "comb(3,2)",
      "The term has k=2, so its binomial coefficient is C(3,2)=3."),
    n("How many terms are in the expansion of (a+b)^4?", "4+1",
      "k ranges from 0 to 4, giving 5 terms."),
    c("What is the general term in the binomial expansion of (a+b)^n?", "C(n,k) multiplied by a to the power n−k and b to the power k",
      ["a to the power n plus b to the power n", "n times a times b", "Only the terms a to the power n and b to the power n"],
      "Each term has a combination coefficient, and the exponents of a and b add to n."),
    n("What is the coefficient of ab in the expansion of (a+b)^2?", "comb(2,1)",
      "(a+b)^2=a²+2ab+b², so the coefficient of ab is 2."),
])

T("bin.term", C6, "6.3", "Specified Terms in a Binomial Expansion", SP, "procedural",
  "When terms are arranged in descending powers of a, term k+1 is C(n,k) a^(n−k) b^k. The exponents can be used to find k.",
  ["Find k from an exponent", "Calculate the coefficient of a specified term, including its factor"],
  "PS.11")
Qs("bin.term", [
    n("In (a+b)^5 arranged in descending powers of a, what is the binomial coefficient of the third term?", "comb(5,2)",
      "The third term corresponds to k=2, so C(5,2)=10."),
    n("What is the coefficient of x² in the expansion of (2x+1)^4?", "comb(4,2)*2**2",
      "For x², the exponent of 2x is 2, so k=2. C(4,2)×2²=6×4=24."),
    n("What is the constant term in the expansion of (x+1)^6?", "comb(6,6)",
      "The constant term has x exponent 0, so its coefficient is C(6,6)=1."),
    c("In the general term T_(k+1), how are the exponents of a and b related?", "Their exponents add to n",
      ["Both exponents equal k", "Their exponents multiply to n", "Their exponents add to k"],
      "The exponent of a is n−k and the exponent of b is k, so their sum is n."),
])

T("bin.coef", C6, "6.3", "Sum of Binomial Coefficients", SP, "reasoning",
  "Setting a=b=1 shows that the sum of the binomial coefficients is 2^n.",
  ["Calculate the sum of a row of binomial coefficients", "Explain why the sum is 2 to the power n"],
  "PS.11", "inferred", NOTE)
Qs("bin.coef", [
    n("What is the sum of all the binomial coefficients in (a+b)^4?", "2**4",
      "Set a=b=1; the left side becomes 2^4=16."),
    n("What is the sum of all the binomial coefficients in (a+b)^6?", "2**6",
      "2^6=64."),
    c("When (1+1)^n is expanded, what does the left side equal?", "2 to the power n",
      ["n factorial", "n", "0"],
      "(1+1)^n=2^n, which is exactly the sum of all the binomial coefficients."),
    n("What is C(4,0)+C(4,1)+C(4,2)+C(4,3)+C(4,4)?", "sum(comb(4,k) for k in range(5))",
      "This is the coefficient sum for (a+b)^4, which equals 16."),
])

T("inq.yh", "Mathematical Inquiry", "Properties and Applications of Pascal's Triangle", "Properties of Pascal's Triangle", IP, "modeling",
  "Row n of Pascal's triangle, counting from row 0, contains the binomial coefficients of (a+b)^n. The row is symmetric, and the sum of adjacent entries gives an entry in the next row.",
  ["Read an entry of Pascal's triangle using the stated indexing", "Explain the sum of adjacent entries using combination numbers"],
  "MI.04")
Qs("inq.yh", [
    n("Arrange the binomial coefficients of (a+b)^n in a row, with n starting at 0. What is the third entry from the left in row n=5 (corresponding to k=2)?", "comb(5,2)",
      "This entry is C(5,2)=10."),
    n("What is the sum of all entries in row n=4?", "2**4",
      "The sum of the binomial coefficients is 2^4=16."),
    n("In Pascal's triangle, C(5,1)+C(5,2) equals which combination number in the next row? First find the sum.", "comb(5,1)+comb(5,2)",
      "C(6,2)=C(5,1)+C(5,2)=5+10=15."),
    c("How is Pascal's triangle related to the binomial theorem?", "Each row gives the coefficients in a binomial expansion",
      ["Each row lists the natural numbers 1, 2, 3 in order", "It is used only to calculate sums of arithmetic sequences", "It has no connection to combination numbers"],
      "Row n, counting from row 0, contains the binomial coefficients of (a+b)^n."),
])

# ---------------------------------------------------------------- Chapter 7

T("pr.cond", C7, "7.1", "Conditional Probability", SP, "conceptual",
  "The probability of event A given that event B has occurred is P(A|B)=P(A∩B)/P(B).",
  ["Calculate conditional probability in a restricted sample space", "State the definition of conditional probability"],
  "PS.12")
Qs("pr.cond", [
    n("A bag contains 5 red and 3 blue balls. One red ball has been drawn without replacement. What is the probability that the next ball is red?", "Fraction(4,8)",
      "There are 4 red and 3 blue balls left, 8 in total. The probability of red is 4/8=1/2."),
    n("A fair die is rolled, and the result is known to be even. Given this condition, what is the probability that the result is greater than 3?", "Fraction(2,3)",
      "The even outcomes are 2, 4, and 6. Two of them exceed 3, so the probability is 2/3."),
    c("What is the definition of P(A|B)?", "P(A and B both occur) divided by P(B)",
      ["P(A) divided by P(B)", "P(A) plus P(B)", "P(A) multiplied by P(B), then plus 1"],
      "Conditional probability restricts the sample space to the outcomes where B has occurred."),
    n("An experiment has 8 equally likely outcomes. Event B contains 4 outcomes, and 1 outcome belongs to both A and B. What is P(A|B)?", "Fraction(1,4)",
      "Among the 4 outcomes in B, 1 also belongs to A, so the probability is 1/4."),
])

T("pr.mul", C7, "7.1", "Multiplication Rule for Probability", SP, "procedural",
  "P(A∩B)=P(A)P(B|A). Probabilities can be multiplied in the order that events occur.",
  ["Use the multiplication rule to calculate the probability of two events occurring together", "Write conditional probabilities in event order"],
  "PS.12")
Qs("pr.mul", [
    n("P(A)=1/2 and P(B|A)=1/3. What is the probability that both A and B occur?", "Fraction(1,2)*Fraction(1,3)",
      "By the multiplication rule, 1/2×1/3=1/6."),
    n("A bag contains 5 red and 5 blue balls. Two are drawn in order without replacement. What is the probability of red first, then blue?", "Fraction(5,10)*Fraction(5,9)",
      "The probability of red first is 5/10; then the probability of blue is 5/9. Multiply to get 5/18."),
    c("In P(A∩B)=P(A)P(B|A), what does the second factor represent?", "The probability of B given that A has occurred",
      ["The probability of the complement of B", "The sum of A and B", "The number of sample points"],
      "First A occurs; then consider B under that condition."),
    n("Each trial has a success probability of 1/2, and two trials are independent. What is the probability that both succeed?", "Fraction(1,2)*Fraction(1,2)",
      "The probability of success on the second trial remains 1/2 given success on the first, so multiply to get 1/4."),
])

T("pr.tot", C7, "7.1", "Law of Total Probability", SP, "procedural",
  "If several mutually exclusive causes cover all possibilities, an event's probability is the sum of each cause's probability multiplied by the corresponding conditional probability.",
  ["Partition a sample space into mutually exclusive cases", "Calculate total probability"],
  "PS.12")
Qs("pr.tot", [
    n("Box A contains 2 red and 1 white ball; Box B contains 1 red and 2 white balls. A box is chosen at random, then one ball is drawn. What is the probability of drawing a red ball?",
      "Fraction(1,2)*Fraction(2,3)+Fraction(1,2)*Fraction(1,3)",
      "Choosing A and drawing red has probability 1/3; choosing B and drawing red has probability 1/6. Add them to get 1/2."),
    n("Machine A makes 3/5 of all products and has a defect rate of 1/10. Machine B makes 2/5 and has a defect rate of 1/5. What is the probability that a randomly selected product is defective?",
      "Fraction(3,5)*Fraction(1,10)+Fraction(2,5)*Fraction(1,5)",
      "3/50+4/50=7/50."),
    c("What conditions must the causes satisfy when using the law of total probability?", "They must be mutually exclusive and together cover all possibilities",
      ["They may overlap", "Every cause must have the same probability", "There can only be one cause"],
      "First divide the possibilities into cases with no overlap or omissions, then add their weighted probabilities."),
    n("Three routes are chosen with probabilities 1/2, 1/3, and 1/6. Their respective pass rates are 1, 1/2, and 0. What is the overall probability of passing?",
      "Fraction(1,2)*1+Fraction(1,3)*Fraction(1,2)+Fraction(1,6)*0",
      "1/2+1/6+0=2/3."),
])

T("pr.bayes", C7, "7.1", "Bayes' Theorem", SP, "procedural",
  "Given that an outcome has occurred, use its total probability as the denominator to find the probability that it came from a particular cause.",
  ["Calculate the probability of a cause given an observed outcome", "Identify the denominator as the total probability of that outcome"],
  "PS.12")
Qs("pr.bayes", [
    n("Machine A makes 3/5 of all products and has a defect rate of 1/10; machine B makes 2/5 and has a defect rate of 1/5. Given that a selected item is defective, what is the probability it came from A?",
      "Fraction(Fraction(3,5)*Fraction(1,10), Fraction(3,5)*Fraction(1,10)+Fraction(2,5)*Fraction(1,5))",
      "The numerator is 3/50 and the denominator is 7/50, giving 3/7."),
    n("Box A has a red-ball probability of 2/3; Box B has a red-ball probability of 1/3. The boxes are equally likely to be chosen. Given that a red ball was drawn, what is the probability it came from A?",
      "Fraction(Fraction(1,2)*Fraction(2,3), Fraction(1,2)*Fraction(2,3)+Fraction(1,2)*Fraction(1,3))",
      "The numerator is 1/3 and the denominator is 1/2, giving 2/3."),
    c("What is Bayes' theorem mainly used for?", "Finding the probability of a cause after observing an outcome",
      ["Finding only the probability of a cause before it occurs", "Making all probabilities add to more than 1", "Replacing the permutation formula"],
      "It reverses the direction of conditional probability: infer the cause from the outcome."),
    n("P(D)=1/5, P(positive|D)=4/5, P(positive|not D)=1/5, and P(not D)=4/5. Given a positive result, what is the probability that D is present?",
      "Fraction(Fraction(1,5)*Fraction(4,5), Fraction(1,5)*Fraction(4,5)+Fraction(4,5)*Fraction(1,5))",
      "The numerator and the other term in the denominator are both 4/25, so the conditional probability is 1/2."),
])

T("pr.cind", C7, "7.1", "Conditional Probability and Independence", SP, "reasoning",
  "If P(B|A)=P(B), then A does not change the probability of B, and A and B are independent. Independence is not the same as mutual exclusivity.",
  ["Use conditional probability to test independence", "Distinguish independence from mutual exclusivity"],
  "PS.12", "inferred", NOTE)
Qs("pr.cind", [
    n("Events A and B are independent, and P(B)=1/3. What is P(B|A)?", "Fraction(1,3)",
      "For independent events, the conditional probability equals the event's probability, so it remains 1/3."),
    n("Events A and B are independent, with P(A)=1/2 and P(B)=1/4. What is the probability that both occur?", "Fraction(1,2)*Fraction(1,4)",
      "For independent events, multiply: 1/8."),
    c("What property do conditional probabilities have for independent events?", "P(B|A) equals P(B)",
      ["P(B|A) must equal 0", "P(B|A) must equal 1", "P(A and B both occurring) must equal 0"],
      "The occurrence of A does not change the probability of B. A probability of zero for joint occurrence describes mutual exclusivity, not independence."),
    c("Are mutually exclusive events and independent events the same?", "No. Mutually exclusive events cannot occur together; independent events do not affect each other's probability",
      ["Yes, the terms are synonyms", "Yes, mutually exclusive events are always independent", "No, independent events have equal probabilities"],
      "If both events have positive probability, they cannot be independent and mutually exclusive: once one occurs, the conditional probability of the other is zero."),
])

T("rv.def", C7, "7.2", "Discrete Random Variables", SP, "conceptual",
  "A random variable assigns a real number to each outcome of an experiment. It is discrete if it takes a finite or countable set of values.",
  ["Identify the possible values of a random variable in an experiment", "Explain that discreteness depends on the set of possible values"],
  "PS.13")
Qs("rv.def", [
    n("A fair die is rolled, and X is the number shown. How many distinct values can X take?", "6",
      "The result can be any integer from 1 to 6, giving 6 values."),
    c("What are the possible values of a discrete random variable like?", "A finite or countable set of values",
      ["Every real number in an interval", "Values that cannot be represented numerically", "Negative values only"],
      "Die rolls and defect counts are discrete. All real numbers in an interval are not."),
    n("A fair coin is tossed twice, and X is the number of heads. How many distinct values can X take?", "3",
      "X can be 0, 1, or 2."),
    n("A bag contains balls labeled 1, 2, and 3. One ball is drawn, and X is its label. How many labels correspond to X=2?", "1",
      "Only one ball has label 2, so that value corresponds to one outcome."),
])

T("rv.law", C7, "7.2", "Probability Distribution", SP, "procedural",
  "A probability distribution lists each value of a random variable and its corresponding probability. Probabilities are nonnegative and sum to 1.",
  ["Find a missing probability using the fact that probabilities sum to 1", "Check whether a probability distribution is valid"],
  "PS.13")
Qs("rv.law", [
    n("X takes values 1, 2, and 3. P(X=1)=1/2 and P(X=2)=1/3. What is P(X=3)?", "1-Fraction(1,2)-Fraction(1,3)",
      "The three probabilities sum to 1, so the third is 1/6."),
    n("X takes only 0 and 1, with P(X=0)=1/4. What is P(X=1)?", "1-Fraction(1,4)",
      "1−1/4=3/4."),
    c("What conditions must a probability distribution satisfy?", "Every probability is nonnegative, and all probabilities sum to 1",
      ["Every probability is greater than 1", "The probabilities sum to the number of values", "Probabilities may be negative as long as they sum to 1"],
      "Probabilities cannot be negative, and the probabilities of all possible values must account for exactly 1."),
    n("P(X=0)=1/5 and P(X=1)=4/5. What is the sum of these probabilities?", "Fraction(1,5)+Fraction(4,5)",
      "1/5+4/5=1, so they can form a complete distribution."),
])

T("rv.two", C7, "7.2", "Two-Point Distribution", SP, "conceptual",
  "A random variable taking only 0 and 1 has P(X=1)=p and P(X=0)=1−p. It describes success or failure in one trial.",
  ["Find the failure probability from the success probability", "State that the mean of a two-point distribution is p"],
  "PS.13", "inferred", "A two-point distribution is one example of a probability distribution. To verify.")
Qs("rv.two", [
    n("X has a two-point distribution with P(X=1)=1/4. What is P(X=0)?", "1-Fraction(1,4)",
      "The failure probability is 1−p=3/4."),
    n("In a two-point distribution, P(X=1)=1/4. What is the mean of X?", "Fraction(1,4)",
      "0×(1−p)+1×p=p, so the mean is 1/4."),
    c("What does a two-point distribution describe?", "A single trial with only two outcomes: success and failure",
      ["A trial with infinitely many outcomes", "A process that must be repeated n times", "A random variable that can take any integer"],
      "Record success as 1 and failure as 0, giving just two possible values."),
    n("For a fair coin, let X=1 for heads and X=0 for tails. What is P(X=1)?", "Fraction(1,2)",
      "The probability of heads is 1/2."),
])

T("rv.mean", C7, "7.3", "Mean of a Discrete Random Variable", SP, "procedural",
  "The mean, or expected value, is the sum of each value multiplied by its probability. It is a probability-weighted average.",
  ["Calculate a mean from a probability distribution", "Explain that the mean is a weighted average"],
  "PS.14")
Qs("rv.mean", [
    n("X takes values 1, 2, and 3 with probabilities 1/2, 1/3, and 1/6, respectively. What is the mean of X?",
      "1*Fraction(1,2)+2*Fraction(1,3)+3*Fraction(1,6)",
      "1/2+2/3+1/2=5/3."),
    n("X takes values 0 and 1 with probabilities 3/4 and 1/4, respectively. What is its mean?", "0*Fraction(3,4)+1*Fraction(1,4)",
      "The mean is 1/4."),
    c("How is the mean of a discrete random variable calculated?", "Weight each value by its probability and add the results",
      ["Add all values directly", "Use only the value with the greatest probability", "Divide the maximum value by the number of values"],
      "Values with higher probabilities have greater influence on the mean."),
    n("X takes values 2 and 4, each with probability 1/2. What is its mean?", "2*Fraction(1,2)+4*Fraction(1,2)",
      "1+2=3."),
])

T("rv.var", C7, "7.3", "Variance of a Discrete Random Variable", SP, "procedural",
  "Variance is the probability-weighted sum of squared deviations from the mean. The standard deviation is the square root of the variance.",
  ["Calculate the variance of a simple distribution", "Know that a constant random variable has variance 0"],
  "PS.14")
Qs("rv.var", [
    n("X takes values 0 and 1, each with probability 1/2. What is its variance?",
      "(0-Fraction(1,2))**2*Fraction(1,2)+(1-Fraction(1,2))**2*Fraction(1,2)",
      "The mean is 1/2. Both squared deviations are 1/4; weighting each by 1/2 gives a variance of 1/4."),
    n("X takes values 1 and 3, each with probability 1/2. What is its variance?",
      "(1-2)**2*Fraction(1,2)+(3-2)**2*Fraction(1,2)",
      "The mean is 2. Both squared deviations are 1, so the weighted variance is 1."),
    c("What does variance describe?", "How spread out the values are around the mean",
      ["The number of possible values", "The maximum value", "The sum of the probabilities"],
      "Variance is larger when values are farther from the mean and those deviations are more likely."),
    n("X always equals 5, so P(X=5)=1. What is its variance?", "(5-5)**2*1",
      "The value never deviates from its mean, so the variance is 0."),
])

T("rv.bern", C7, "7.4", "Bernoulli Trials", SP, "conceptual",
  "Each trial has two possible outcomes, the probability of success remains p, and trials are independent. Repeating the trial n times gives n Bernoulli trials.",
  ["Determine whether a set of trials is Bernoulli", "Identify the number of trials and the success probability"],
  "PS.15")
Qs("rv.bern", [
    n("Each independent trial has a success probability of 1/5. What is the probability of failure?", "1-Fraction(1,5)",
      "The failure probability is 1−p=4/5."),
    c("What conditions must Bernoulli trials satisfy?", "Each trial has two outcomes, the success probability is constant, and the trials are independent",
      ["Each trial may have many outcomes", "The success probability increases from trial to trial", "The outcomes must be combined into one mutually exclusive result"],
      "All three conditions are required: two outcomes, constant probability, and independence."),
    n("The same trial is repeated independently 4 times. What is the number of trials n?", "4",
      "There are 4 repetitions, so n=4."),
    n("There are n=3 trials, each with success probability p=1/2. What is the probability of failure on one trial?", "1-Fraction(1,2)",
      "1−1/2=1/2."),
])

T("rv.bin", C7, "7.4", "Binomial Distribution", SP, "procedural",
  "In n Bernoulli trials, the number of successes X follows a binomial distribution: P(X=k)=C(n,k) p^k (1−p)^(n−k).",
  ["Calculate a probability for a binomial distribution", "Explain that X is the number of successes"],
  "PS.15")
Qs("rv.bin", [
    n("X follows B(4,1/2). What is P(X=2)?", "comb(4,2)*Fraction(1,2)**4",
      "C(4,2)×(1/2)^4=6/16=3/8."),
    n("X follows B(3,1/3). What is P(X=0)?", "Fraction(2,3)**3",
      "All three trials fail: (2/3)^3=8/27."),
    n("X follows B(2,1/2). What is P(X=1)?", "comb(2,1)*Fraction(1,2)**2",
      "C(2,1)×1/4=1/2."),
    c("What does X represent in a binomial distribution B(n,p)?", "The number of successes in n independent repeated trials",
      ["The success probability on each trial", "The number of possible values when a trial fails", "The total number of sample-space outcomes"],
      "X can take values 0, 1, …, n and records the number of successes."),
])

T("rv.bstat", C7, "7.4", "Mean and Variance of a Binomial Distribution", SP, "procedural",
  "If X follows B(n,p), its mean is np and its variance is np(1−p).",
  ["Calculate the mean of a binomial distribution", "Calculate the variance of a binomial distribution"],
  "PS.15")
Qs("rv.bstat", [
    n("X follows B(10,1/5). What is its mean?", "10*Fraction(1,5)",
      "np=10×1/5=2."),
    n("X follows B(10,1/5). What is its variance?", "10*Fraction(1,5)*Fraction(4,5)",
      "np(1−p)=2×4/5=8/5."),
    n("X follows B(4,1/2). What is its mean?", "4*Fraction(1,2)",
      "4×1/2=2."),
    c("Which is the variance formula for a binomial distribution?", "np(1−p)",
      ["np", "n+p", "p divided by n"],
      "The mean is np. Multiply it by the failure probability 1−p to get the variance."),
])

T("rv.hyp", C7, "7.4", "Hypergeometric Distribution", SP, "procedural",
  "A population of N items contains K defective items. If n items are drawn without replacement, the number of defectives drawn follows a hypergeometric distribution.",
  ["Calculate a probability for sampling without replacement", "Distinguish a hypergeometric distribution from a binomial distribution with replacement"],
  "PS.15")
Qs("rv.hyp", [
    n("A batch of 10 products contains 4 defective items. Three are drawn without replacement. What is the probability of drawing exactly 1 defective item?",
      "Fraction(comb(4,1)*comb(6,2), comb(10,3))",
      "C(4,1)×C(6,2)/C(10,3)=4×15/120=1/2."),
    n("A batch of 10 products contains 4 defective items. Three are drawn without replacement. What is the probability that all 3 are defective?",
      "Fraction(comb(4,3)*comb(6,0), comb(10,3))",
      "C(4,3)×C(6,0)/120=4/120=1/30."),
    n("A batch of 10 products contains 4 defective items. Three are drawn without replacement. What is the probability that none are defective?",
      "Fraction(comb(4,0)*comb(6,3), comb(10,3))",
      "C(6,3)/120=20/120=1/6."),
    c("How does the sampling method differ between a hypergeometric and a binomial distribution?", "A hypergeometric distribution uses sampling without replacement",
      ["A hypergeometric distribution replaces each item after sampling", "Both require an infinite population", "A hypergeometric distribution cannot use combinations"],
      "Without replacement, the number of defectives remaining changes, so use combinations rather than a fixed probability p."),
])

T("rv.hmean", C7, "7.4", "Mean of a Hypergeometric Distribution", SP, "procedural",
  "When n items are drawn without replacement, the mean number from a specified category is nK/N.",
  ["Calculate the mean of a hypergeometric distribution", "Explain the meanings of N, K, and n in the formula"],
  "PS.15", "inferred", NOTE)
Qs("rv.hmean", [
    n("A population has 10 items, 4 in a specified category. If 3 are sampled without replacement, what is the mean number from that category?", "Fraction(3*4,10)",
      "nK/N=12/10=6/5."),
    n("A population has 8 items, 2 in a specified category. If 4 are sampled without replacement, what is the mean count from that category?", "Fraction(4*2,8)",
      "8/8=1."),
    c("In the hypergeometric mean nK/N, what does K represent?", "The number of items in the specified category in the population",
      ["The number of items sampled", "The population size", "The number of items left after sampling"],
      "N is the population size, n is the sample size, and K is the population count in the specified category."),
    n("A population has 6 items, 3 in a specified category. If 2 are sampled without replacement, what is the mean count from that category?", "Fraction(2*3,6)",
      "6/6=1."),
])

T("rv.norm", C7, "7.5", "Properties of the Normal Distribution", SP, "conceptual",
  "A normal curve is a single-peaked bell curve symmetric about its mean. The mean sets its axis of symmetry, and the variance determines its spread.",
  ["State that a normal curve is symmetric about its mean", "Explain that a larger variance makes the curve flatter"],
  "PS.16")
Qs("rv.norm", [
    n("A normal distribution has mean 5. What is the x-coordinate of the normal curve's axis of symmetry?", "5",
      "The axis of symmetry is x equal to the mean, so it is 5."),
    c("What shape does a normal curve have?", "A single peak and symmetry about the mean",
      ["Two peaks and a left skew", "A straight line", "Values only on the negative side"],
      "It is high in the middle, low on both ends, and symmetric."),
    c("How does a normal curve change when its variance increases?", "It becomes flatter and spreads farther to both sides",
      ["It becomes narrower and taller", "Its axis of symmetry moves to 0", "It becomes a piecewise line"],
      "A larger variance means more spread-out data, so the curve becomes flatter."),
    n("What is the mean of the standard normal distribution?", "0",
      "The standard normal distribution has mean 0 and variance 1."),
])

T("rv.nrule", C7, "7.5", "Empirical Rule for the Normal Curve", SP, "conceptual",
  "A common textbook approximation is that about 68% of values lie within 1 standard deviation of the mean and about 95% lie within 2 standard deviations.",
  ["Identify the interval within 1 standard deviation of the mean", "Know that these percentages are approximate empirical rules"],
  "PS.16", "inferred", "The 68% and 95% figures are common textbook approximations, not exact calculations. To verify.")
Qs("rv.nrule", [
    n("A normal distribution has mean 10 and standard deviation 2. How many standard deviations is the half-width of the interval within 1 standard deviation of the mean?", "1",
      "The interval is one standard deviation from the mean."),
    c("According to the common empirical rule, where do about 95% of values lie?", "Within 2 standard deviations of the mean",
      ["Within 1 standard deviation of the mean", "Only at the mean", "More than 10 standard deviations from the mean"],
      "About 68% lie within 1 standard deviation and about 95% within 2. These figures are approximate."),
    n("The standard normal distribution has standard deviation 1. What is the positive endpoint 3 standard deviations from the mean?", "3",
      "The mean is 0, so 0+3×1=3."),
    c("How should the 68% and 95% figures in the empirical rule be understood?", "As approximations, not exact percentages calculated from the data in this problem",
      ["They must equal the exact sample percentages", "They apply only to a uniform distribution", "They mean the variance is 68"],
      "These are common approximations for areas under the normal curve; exact areas require integration."),
])

# ---------------------------------------------------------------- Chapter 8

T("cor.scatter", C8, "8.1", "Statistical Correlation of Paired Data", SP, "conceptual",
  "Plot paired data as a scatterplot. Points trending upward along a line indicate positive correlation; points trending downward indicate negative correlation.",
  ["Determine positive or negative correlation from the scatterplot trend", "Know that correlation is not an exact functional relationship"],
  "PS.17", "inferred", NOTE81)
Qs("cor.scatter", [
    c("What does a scatterplot trending roughly from the lower left to the upper right indicate?", "Positive correlation",
      ["Negative correlation", "It must be the function y=x", "No correlation"],
      "As x increases, y tends to increase, which is positive correlation. The points do not lie on one line, so this is not a deterministic function."),
    c("What does a scatterplot trending roughly from the upper left to the lower right indicate?", "Negative correlation",
      ["Positive correlation", "Zero variance", "A sample size of zero"],
      "As x increases, y tends to decrease, which is negative correlation."),
    n("Three paired observations are (1, 2), (2, 3), and (3, 5). In how many pairs is the second value greater than the first?", "3",
      "2>1, 3>2, and 5>3, so all three have a greater second value."),
    c("What is the difference between statistical correlation and a functional relationship?", "Correlation allows points to vary around a line, while a function assigns a definite y to each x",
      ["They are exactly the same", "Correlation requires all points to overlap", "A function cannot be plotted on a coordinate plane"],
      "Paired data usually show variation, so we describe their correlation rather than claiming every point satisfies one exact equation."),
])

T("cor.r", C8, "8.1", "Sample Correlation Coefficient", SP, "procedural",
  "The sample correlation coefficient r uses products of deviations to measure the direction and strength of linear correlation. Its value lies between −1 and 1.",
  ["Calculate the sum of products of deviations for a small data set", "Know that linear correlation is strong when r is near 1 or −1"],
  "PS.17")
Qs("cor.r", [
    n("For the data (1, 2), (2, 4), and (3, 6), the means of x and y are 2 and 4. What is the sum of the products of deviations?",
      "(-1)*(-2)+0*0+1*2",
      "The deviations are (−1,−2), (0,0), and (1,2), so the products sum to 2+0+2=4."),
    n("For the data (1, 1), (2, 2), and (3, 3), the means of x and y are both 2. What is the sum of the products of deviations?",
      "(-1)*(-1)+0*0+1*1",
      "The products are 1, 0, and 1, summing to 2. This data set has correlation coefficient 1."),
    c("What is the range of the sample correlation coefficient r?", "From −1 to 1",
      ["From 0 to 100", "Any positive integer", "Only 0 or 1"],
      "r=1 indicates perfect positive correlation, r=−1 perfect negative correlation, and r=0 no linear correlation."),
    c("What does r=0 indicate?", "The data have no linear correlation",
      ["Perfect positive correlation", "A sample size of zero", "Every y equals x squared"],
      "r=0 rules out a linear relationship, but does not show that no other relationship exists."),
])

T("cor.cmp", C8, "8.1", "Comparing Correlation Strength", SP, "reasoning",
  "Compare the strength of linear correlation using |r|. A larger absolute value indicates stronger linear correlation; the sign indicates only its direction.",
  ["Compare two correlation coefficients using absolute value", "Distinguish correlation direction from strength"],
  "PS.17")
Qs("cor.cmp", [
    n("Two sample correlation coefficients are −3/5 and 1/5. What is the absolute value of the one indicating stronger linear correlation?",
      "max(abs(Fraction(-3,5)), abs(Fraction(1,5)))",
      "|−3/5|=3/5, which is larger than 1/5. The negative sign indicates the opposite direction only."),
    c("Which indicates stronger linear correlation, |r|=0.9 or |r|=0.2?", "|r|=0.9 is stronger",
      ["|r|=0.2 is stronger", "They are equally strong", "Absolute values cannot be compared"],
      "The closer the absolute value is to 1, the stronger the linear correlation."),
    c("Are r=0.8 and r=−0.8 equally strong in linear correlation?", "Yes, because their absolute values are equal",
      ["No, a positive value is always stronger", "No, a negative value means no correlation", "Yes, because the two numbers sum to 0"],
      "The sign indicates positive or negative correlation; the absolute value indicates strength."),
    n("What is |−4/5|?", "abs(Fraction(-4,5))",
      "The absolute value is 4/5."),
])

T("reg.model", C8, "8.2", "Simple Linear Regression Model", SP, "conceptual",
  "Simple linear regression expresses a response variable as a linear function of an explanatory variable plus random error.",
  ["Identify the explanatory and response variables in a model", "Find the value on the line when the error is zero"],
  "PS.18")
Qs("reg.model", [
    c("What is the basic form of a simple linear regression model?", "The response variable equals a linear function plus random error",
      ["The response variable equals the square of the explanatory variable", "The two variables must be equal", "The model cannot include error"],
      "Observed points vary around the line, and that variation is represented by random error."),
    n("The linear part is y=2x+1, and take the error as 0. What is the value of this part when x=3?", "2*3+1",
      "2×3+1=7. An actual observation may also include error."),
    c("In a regression model, which variable is typically used to estimate the other?", "Use the explanatory variable to estimate the response variable",
      ["Use sample size to estimate variance", "Replace all data with the correlation coefficient", "Use only rankings and no data"],
      "The explanatory variable is the input, and the response variable is the quantity to predict."),
    n("What is the value of the line y=−1+2x when x=0?", "-1+2*0",
      "Substituting x=0 gives −1, the intercept of the line."),
])

T("reg.ls", C8, "8.2", "Least-Squares Principle", SP, "conceptual",
  "The least-squares method selects the line that minimizes the sum of squared residuals. A residual is the observed value minus the predicted value.",
  ["Calculate a residual", "State that least squares minimizes the sum of squared residuals"],
  "PS.18")
Qs("reg.ls", [
    n("A point has observed value 5 and predicted value 3. What is its residual?", "5-3",
      "Residual = observed − predicted = 2."),
    n("The points (0, 0) and (2, 2) lie on the line y=x. What is the sum of their squared residuals?", "(0-0)**2+(2-2)**2",
      "Both residuals are 0, so the sum of squares is 0."),
    c("What criterion does the least-squares method use to select a line?", "Minimize the sum of squared residuals",
      ["Minimize the number of residuals", "Require the slope to be 1", "Require the intercept to be 0"],
      "Square each residual before adding them so positive and negative values do not cancel. The regression line minimizes this sum."),
    n("The observed value is 4 and the predicted value is 4. What is the squared residual?", "(4-4)**2",
      "The residual is 0, so its square is also 0."),
])

T("reg.est", C8, "8.2", "Least-Squares Estimates of Regression Coefficients", SP, "procedural",
  "For points (x_i,y_i), the slope is b=(n∑xy−∑x∑y)/(n∑x²−(∑x)²), and the intercept is a=ȳ−b x̄.",
  ["Calculate a slope from a small data set", "Then calculate the intercept"],
  "PS.18")
Qs("reg.est", [
    n("For the points (1, 1), (2, 3), and (3, 5), what is the least-squares slope b?",
      "Fraction(3*(1+6+15)-6*9, 3*(1+4+9)-6*6)",
      "The numerator is 3×22−54=12, and the denominator is 42−36=6, so the slope is 2."),
    n("For the points (1, 1), (2, 3), and (3, 5), the regression slope is 2, the mean of y is 3, and the mean of x is 2. What is the intercept a?",
      "3-2*2",
      "a=ȳ−b x̄=3−4=−1."),
    n("What is the slope of the line through (0, 1) and (1, 3), calculated as (3−1)/(1−0)?", "Fraction(3-1,1-0)",
      "The slope through these two points is 2."),
    c("After finding the slope b, how is the intercept a commonly calculated?", "Subtract b times the mean of x from the mean of y",
      ["Divide the mean of x by the mean of y", "Add all x values", "Take the reciprocal of the slope"],
      "The regression line passes through the sample center (x̄, ȳ), so a=ȳ−b x̄."),
])

T("reg.pred", C8, "8.2", "Prediction with a Regression Line", SP, "application",
  "Substitute a new x into the regression line to obtain a predicted y value. A prediction is an estimate, not a certain observation.",
  ["Substitute x into a line to find a predicted value", "Know that predictions and observations may differ"],
  "PS.18")
Qs("reg.pred", [
    n("A regression line is y=2x−1. What is the predicted y value when x=4?", "2*4-1",
      "8−1=7."),
    n("A regression line is y=−2+3x. What is the predicted value when x=2?", "-2+3*2",
      "−2+6=4."),
    c("What should a value obtained from a regression line be called?", "A predicted value; the actual observation may differ",
      ["It must equal the next observed value", "The sample size", "The correlation coefficient itself"],
      "The line provides an estimate. Random error can make an observation differ."),
    n("A regression line is y=5−x. What is the predicted value when x=0?", "5-0",
      "At x=0, the prediction is the intercept, 5."),
])

T("ct.tab", C8, "8.3", "2×2 Contingency Table", SP, "procedural",
  "When each of two categorical variables has two categories, arrange the counts in a 2×2 contingency table and calculate row totals, column totals, and the grand total.",
  ["Calculate the total in a contingency table", "Calculate a row total"],
  "PS.19", "inferred", NOTE83)
Qs("ct.tab", [
    n("A contingency table has cell counts 10, 6, 4, and 10. What is the total number of observations?", "10+6+4+10",
      "Add the four cells: 10+6+4+10=30."),
    n("The first row of a contingency table contains 10 and 6. What is the row total?", "10+6",
      "10+6=16."),
    c("What does a 2×2 contingency table organize?", "Two categorical variables, each with two categories",
      ["The mean of a set of continuous measurements", "The slope of a regression line", "A permutation count A(n,k)"],
      "Each observation falls into one category for each variable, so it fits into one of four cells."),
    n("A four-cell table has counts 3, 5, 2, and 6. What is the total count?", "3+5+2+6",
      "3+5+2+6=16."),
])

T("ct.idea", C8, "8.3", "Idea Behind the Test of Independence", SP, "conceptual",
  "A test of independence begins by assuming that two categorical variables are independent, then checks whether the observed contingency table deviates too far from that assumption.",
  ["Explain that independence is assumed first and deviation is then assessed", "Know that ad−bc=0 indicates balance among the four cells"],
  "PS.19")
Qs("ct.idea", [
    c("What assumption is made at the start of a test of independence?", "The two categorical variables are assumed to be independent",
      ["The variables are assumed to have a causal relationship", "The sample size is assumed to be 0", "The regression slope is assumed to be 1"],
      "Start by assuming independence. If the data deviate too far, question that assumption."),
    n("A contingency table has a=2, b=3, c=4, and d=6. What is ad−bc?", "2*6-3*4",
      "12−12=0. Equal cross-products give a contrast of zero."),
    c("If the observed contingency table deviates substantially from the independence assumption, what can be concluded?", "There is substantial evidence that the variables are associated",
      ["It has been proved that the variables are unrelated", "The probabilities must be changed to values greater than 1", "The sample is the entire population"],
      "A test provides statistical evidence, not absolute logical proof."),
    c("What type of variables are considered in a test of independence?", "Categorical variables",
      ["Only continuous regression residuals", "Only permutation counts", "Only standard deviations of normal distributions"],
      "A contingency table records category frequencies, so the variables are categorical."),
])

T("ct.chi", C8, "8.3", "Test-of-Independence Statistic", SP, "procedural",
  "For a 2×2 table, use χ²=n(ad−bc)²/((a+b)(c+d)(a+c)(b+d)). A larger value provides more evidence of an association.",
  ["Substitute the four cell counts into the formula", "Know that a statistic of 0 means the cross-products balance"],
  "PS.19", "inferred", "This is a common statistic for testing independence in a 2×2 table. Critical-value tables have not been checked against each edition. To verify.")
Qs("ct.chi", [
    n("A contingency table has a=20, b=5, c=5, and d=20. Using χ²=n(ad−bc)²/((a+b)(c+d)(a+c)(b+d)), what is the statistic?",
      "Fraction(50*(20*20-5*5)**2, 25*25*25*25)",
      "n=50, ad−bc=375, and the denominator is 25 to the fourth power. The result is 18."),
    n("A contingency table has a=4, b=1, c=1, and d=4. Using the same χ² formula, what is the statistic?",
      "Fraction(10*(4*4-1*1)**2, 5*5*5*5)",
      "n=10 and ad−bc=15. Then 10×225/625=18/5."),
    c("What does a large value of this statistic suggest?", "The categorical variables are more likely to be associated rather than independent",
      ["The frequencies of both variables must be 0", "The independence assumption must be accepted", "The sample correlation coefficient must be 1"],
      "The larger the departure from independence, the larger the statistic. Whether to reject the assumption also depends on the critical value."),
    n("A contingency table has 1 in each of its four cells. Using the same χ² formula, what is the statistic?",
      "Fraction(4*(1*1-1*1)**2, 2*2*2*2)",
      "ad−bc=0, so the statistic is 0."),
])

T("mod.stat", "Mathematical Modeling", "Building Statistical Models for Prediction", "Building Statistical Models for Prediction", IP, "modeling",
  "Build a regression model from paired data: pose a question, organize the data, estimate a line, then check predictions using residuals or new data.",
  ["Make a prediction using a given line", "Compare the residual sums of squares of two models"],
  "MI.03", "inferred", "Haoduo E-Textbooks labels this 'Mathematical Model: Building Statistical Models for Prediction'; the Teacher's Home contents do not list it separately. The activity is classified as mathematical modeling. To verify.")
Qs("mod.stat", [
    n("The fitted line is y=3x+2. What is the predicted value when x=5?", "3*5+2",
      "15+2=17."),
    c("What is the most complete sequence for making predictions with a statistical model?", "Pose a question, organize paired data, build a model, then evaluate its predictions",
      ["Write a conclusion first, then decide whether to collect data", "Calculate only a permutation count", "Use the rank from one test in place of all data"],
      "A model must be checked against data and prediction performance; do not write down the answer first."),
    n("A predicted value is 10 and the subsequent observation is 8. What is the absolute error?", "abs(10-8)",
      "|10−8|=2. A large error calls for checking the model."),
    n("Model A has a residual sum of squares of 4; Model B has 9. If the smaller sum is preferred, what is the selected sum?", "min(4,9)",
      "4 is less than 9, so choose Model A and its sum of 4."),
])
