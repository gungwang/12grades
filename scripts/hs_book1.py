"""PEP A Edition (2019), Compulsory Volume 1.

The chapter outline combines the following third-party sources; none is the official PEP website. Page numbers were not verified and are marked as needing verification:
- Teacher's Home, https://www.renjiaoshe.com/jiaocai/2069.html (sections 1.1–5.7 and mathematical modeling were visible when checked)
- Douban journal, https://www.douban.com/note/831269463/
- PDF of the textbook contents compiled by Xu Qingpei, https://www.drhuang.com/chinese/science/mathematics/高中教科书数学目录.pdf

Only sections corroborated by all of these sources are included; no finer subsection numbers or page numbers are invented.
Mathematical modeling is placed after Chapter 4; the activity is titled "Build a Function Model."
"""
# The Han characters in the third-party PDF URL are part of the source URL and must remain unchanged.
from hs_common import edge, questions, topic

NA = "Numbers and Algebra"
IP = "Integrated Practice"

C1 = "Chapter 1: Sets and Common Logical Notation"
C2 = "Chapter 2: Quadratic Functions, Equations, and Inequalities"
C3 = "Chapter 3: Concepts and Properties of Functions"
C4 = "Chapter 4: Exponential and Logarithmic Functions"
C5 = "Chapter 5: Trigonometric Functions"


def T(key, chapter, section, name, domain, typ, desc, crit, std, conf="exact", note=None):
    topic(key, 1, chapter, section, name, domain, typ, desc, crit, std, conf, note)


def Qs(key, items):
    questions(key, items)


def n(prompt, verify, expl):
    return ("n", prompt, verify, expl)


def nu(prompt, verify, expl):
    return ("nu", prompt, verify, expl)


def c(prompt, ok, bad, expl):
    return ("c", prompt, ok, bad, expl)


# ---------------------------------------------------------------- Chapter 1

T("set.mean", C1, "1.1", "Meaning of a Set", NA, "conceptual",
  "Know that a set consists of well-defined objects called elements.",
  ["Decide whether a group of objects can form a set", "Distinguish an element from a set"],
  "PRE.01")
Qs("set.mean", [
    c("Which group of objects can form a set?", "All positive integers", ["Relatively tall students", "Beautiful flowers", "Very large numbers"],
      "The objects in a set must be well-defined. Positive integers have a clear criterion; the other three groups do not."),
    n("Write 1, 2, 2, 3 as a set. How many distinct elements are there?", "len([1,2,3])",
      "Elements in a set are distinct. The repeated 2 is counted once, leaving 1, 2, and 3: 3 elements."),
    c("What is the empty set?", "A set containing no elements", ["A set containing only 0", "A set containing one element", "A set whose elements are all equal"],
      "The empty set has no elements. A set containing 0 has one element and is not empty."),
    c("Can the phrase \"very small positive numbers\" define a set?", "No, because \"very small\" has no precise criterion", ["Yes, because positive numbers are well-defined", "Yes, but only a finite set", "No, because there are infinitely many positive numbers"],
      "A set requires a well-defined criterion. An infinite collection such as all positive integers can be a set, but \"very small\" is not precise."),
])

T("set.in", C1, "1.1", "Element-Set Membership", NA, "conceptual",
  "Use belongs to and does not belong to for the relationship between an element and a set, and know that a set does not repeat elements.",
  ["Determine whether an object belongs to a given set", "Use the membership symbols correctly"],
  "PRE.01", "inferred", "The curriculum standard includes element-set membership under the meaning of a set; this topic focuses only on membership. Source wording needs verification.")
Qs("set.in", [
    n("How many even numbers are in the set {0, 2, 4, 6}?", "len([0,2,4,6])",
      "0, 2, 4, and 6 are all even, so all 4 elements count."),
    c("What is the relationship between 2 and the set {1, 2, 3}?", "2 belongs to the set", ["2 does not belong to the set", "{2} belongs to the set", "2 is a subset of the set"],
      "2 is an element of the set, so it belongs to the set. Membership and subset relationships are different."),
    n("How many elements greater than 6 are in the set {1, 3, 5, 7, 9}?", "len([7,9])",
      "The elements greater than 6 are 7 and 9, so there are 2."),
    c("In the set {1, 2, 2}, the element 2 is written twice. Can it count as two distinct elements?", "No; elements in a set are distinct", ["Yes, if both are written", "Yes, but parentheses are needed", "Only infinite sets cannot have duplicates"],
      "Elements in a set are distinct. {1, 2, 2} is the same set as {1, 2}; the repeated 2 counts only once."),
])

T("set.list", C1, "1.1", "Roster Method", NA, "procedural",
  "Represent a finite set by listing its elements and count how many elements it has.",
  ["List all elements in a finite set that meet a condition", "Know that order and repetition do not matter when listing a set"],
  "PRE.01", "inferred", "The roster method is one way to represent a set; the curriculum standard does not separate representation methods into individual clauses. Source wording needs verification.")
Qs("set.list", [
    n("List the positive integers less than 6. How many elements are there?", "len([1,2,3,4,5])",
      "The positive integers less than 6 are 1, 2, 3, 4, and 5, for a total of 5."),
    n("How many elements are in the set {1, 2, 3}?", "len([1,2,3])",
      "The three listed numbers are distinct, so the set has 3 elements."),
    n("How many positive even numbers are less than or equal to 10?", "len([2,4,6,8,10])",
      "The positive even numbers not greater than 10 are 2, 4, 6, 8, and 10: 5 numbers."),
    c("Which statement about representing a set by listing its elements is correct?", "The order of the elements can change without changing the set",
      ["The elements must be listed from least to greatest", "Each element must be written at least twice", "It can represent only infinite sets"],
      "The order does not matter when listing a set. {1, 2} and {2, 1} are the same set."),
])

T("set.desc", C1, "1.1", "Set-Builder Notation", NA, "conceptual",
  "Represent sets using set-builder notation and choose between set-builder and roster notation.",
  ["Interpret {x | condition}", "Rewrite simple set-builder notation using roster notation"],
  "PRE.01", "inferred", "Set-builder notation is one way to represent a set and is grouped with roster notation under the meaning of a set. Source wording needs verification.")
Qs("set.desc", [
    n("How many elements are in the set {x | x is a positive integer less than 4}?", "len([1,2,3])",
      "The positive integers less than 4 are 1, 2, and 3, for a total of 3."),
    n("How many elements are in the set {x | x is a positive divisor of 12}?", "len([1,2,3,4,6,12])",
      "The positive divisors of 12 are 1, 2, 3, 4, 6, and 12, for a total of 6."),
    c("Which method is more suitable for representing all integers?", "Set-builder notation", ["Roster notation", "Only a diagram", "Only the empty set"],
      "There are infinitely many integers, so they cannot all be listed one by one; set-builder notation is suitable."),
    c("What does x represent in {x | x>0}?", "Numbers that satisfy x>0", ["Only the number 1", "The number of elements greater than 0", "The number of solutions to an equation"],
      "In set-builder notation, the condition appears after the vertical bar; x represents all elements that satisfy it."),
])

T("set.nums", C1, "1.2", "Common Number Sets", NA, "conceptual",
  "Recognize the natural-number, integer, rational-number, and real-number sets and their inclusion relationships. This graph follows the PEP A Edition convention that 0 is a natural number.",
  ["Determine which common number set contains a given number", "State the inclusion relationships among N, Z, Q, and R"],
  "PRE.01", "inferred", "Common number sets apply set notation to the classification of real numbers. Source wording needs verification.")
Qs("set.nums", [
    n("Under this graph's convention, 0 is a natural number. How many natural numbers are in the set {−1, 0, 1, 2}?", "len([0,1,2])",
      "The natural numbers include 0 and the positive integers. −1 is not natural; the other 3 numbers are."),
    n("How many positive integers are in the set {−2, −1, 0, 1}?", "len([1])",
      "The positive integers start at 1. Zero and negative numbers are not positive, so only 1 qualifies."),
    c("How are the rational-number set and real-number set related?", "The rational numbers are a proper subset of the real numbers",
      ["The real numbers are a subset of the rational numbers", "The sets are equal", "The sets have no elements in common"],
      "All rational numbers are real, but the real numbers also include irrationals, so the rational numbers are a proper subset."),
    c("Which set contains √2?", "The real numbers, but not the rational numbers",
      ["The natural numbers", "The integers", "The rational numbers"],
      "√2 is irrational and real, but it is not rational, an integer, or a natural number."),
])

T("set.sub", C1, "1.2", "Subsets and Set Equality", NA, "conceptual",
  "Determine whether one set is a subset of another or whether two sets are equal; know that the empty set is a subset of every set.",
  ["Use the definition to decide whether A is a subset of B", "Know that A=B means each set is a subset of the other"],
  "PRE.02")
Qs("set.sub", [
    n("How many subsets does the set {1, 2} have?", "2**2",
      "An n-element set has 2 to the power of n subsets. A 2-element set has 4 subsets, including the empty set and the set itself."),
    c("How are {1, 2} and {2, 1} related?", "The two sets are equal",
      ["The first is a proper subset of the second", "Neither contains the other", "Only the second is a subset of the first"],
      "The sets contain exactly the same elements; only the order differs, so they are equal."),
    n("How many subsets does the empty set have?", "2**0",
      "The empty set has one subset: itself."),
    c("If A is a subset of B, which statement must be true?", "Every element of A is in B",
      ["Every element of B is in A", "A has fewer elements than B", "A cannot equal B"],
      "By definition, every element of A is also an element of B. A may equal B, so it need not have fewer elements."),
])

T("set.proper", C1, "1.2", "Proper Subsets", NA, "procedural",
  "Know that a proper subset is a subset that is not equal to the original set, and calculate the number of proper subsets of a finite set.",
  ["Distinguish a subset from a proper subset", "Calculate the number of proper subsets of an n-element set"],
  "PRE.02", "inferred", "A proper subset is a type of subset relationship and is not a separate curriculum-standard clause. Source wording needs verification.")
Qs("set.proper", [
    n("How many proper subsets does a set with 3 elements have?", "2**3-1",
      "There are 8 subsets; remove the set itself to get 7 proper subsets."),
    n("How many proper subsets does {1} have?", "2**1-1",
      "Its subsets are the empty set and itself. Removing itself leaves just the empty set: 1 proper subset."),
    c("Is a set included among its own proper subsets?", "No", ["Yes", "Only the empty set is", "Only infinite sets are not"],
      "A proper subset must be a subset and must not equal the original set, so a set is not a proper subset of itself."),
    n("How many proper subsets does a 4-element set have?", "2**4-1",
      "There are 16 subsets; remove the set itself to get 15 proper subsets."),
])

T("set.inter", C1, "1.3", "Intersection", NA, "procedural",
  "Find the intersection of two sets and know that each element in the intersection belongs to both sets.",
  ["List the common elements of two finite sets", "State the subset relationships among A∩B, A, and B"],
  "PRE.03")
Qs("set.inter", [
    n("A={1, 2, 3, 4}, B={3, 4, 5}. How many elements are in A∩B?", "len([3,4])",
      "The elements that belong to both A and B are 3 and 4, so there are 2."),
    n("A={1, 2}, B={3, 4}. How many elements are in their intersection?", "0",
      "There are no common elements, so the intersection is empty and has 0 elements."),
    n("A={1, 2, 3}. How many elements are in A∩A?", "len([1,2,3])",
      "The elements A shares with itself are all of its elements, so there are 3."),
    c("If A is a subset of B, what is A∩B?", "A", ["B", "The empty set", "The union of A and B"],
      "Every element of A is in B, so the common part is A."),
])

T("set.union", C1, "1.3", "Union", NA, "procedural",
  "Find the union of two sets and use |A|+|B|−|A∩B| to count the elements in a finite union.",
  ["List the union of two finite sets", "Use inclusion-exclusion to count the elements in a union"],
  "PRE.03", "inferred", "Union and intersection are both basic set operations. Source wording needs verification.")
Qs("set.union", [
    n("A has 3 elements, B has 3 elements, and their intersection has 2 elements. How many elements are in the union?", "3+3-2",
      "The size of the union is the sum of the set sizes minus the shared elements counted twice: 3+3−2=4."),
    n("A={1, 2}, B={2, 3, 4}. How many elements are in A∪B?", "len([1,2,3,4])",
      "The union is 1, 2, 3, and 4. Count 2 only once, for a total of 4."),
    n("A has 5 elements. B is a subset of A with 2 elements. How many elements are in A∪B?", "5",
      "All elements of B are already in A, so the union is A and still has 5 elements."),
    c("What must be true about A∪B and A?", "A is a subset of A∪B", ["A∪B is a subset of A", "They are equal", "Their intersection is empty"],
      "The union contains all elements of A and B, so A is a subset of the union."),
])

T("set.comp", C1, "1.3", "Complement", NA, "procedural",
  "Find the complement of a set within a given universal set; know that the complement and the original set have no elements in common and together form the universal set.",
  ["List the complement within a finite universal set", "Find the number of elements in a complement by subtracting the set size from the universal-set size"],
  "PRE.03", "inferred", "Complement, intersection, and union are basic set operations. Source wording needs verification.")
Qs("set.comp", [
    n("A universal set has 5 elements, and A has 2. How many elements are in the complement of A?", "5-2",
      "The complement contains the elements in the universal set that are not in A: 5−2=3."),
    n("The universal set is U={1, 2, 3, 4}, and A={1, 4}. How many elements are in the complement of A?", "len([2,3])",
      "The elements not in A are 2 and 3, so there are 2."),
    n("Taking the complement of A's complement gives a set with the same number of elements as A. If A has 6 elements, how many elements does the result have?", "6",
      "The complement of the complement is A itself, so it still has 6 elements."),
    c("What is the intersection of A and its complement in the universal set?", "The empty set", ["The universal set", "A itself", "The complement itself"],
      "No element of the complement belongs to A, so they have no elements in common."),
])

T("set.mix", C1, "1.3", "Mixed Operations on Sets", NA, "procedural",
  "Perform mixed intersection, union, and complement operations within a specific finite universal set.",
  ["Evaluate mixed operations in the order indicated by parentheses", "Check results using element counts"],
  "PRE.03", "inferred", "Mixed operations combine intersection, union, and complement; they do not have a separate curriculum-standard clause. Source wording needs verification.")
Qs("set.mix", [
    n("A universal set has 8 elements, A has 5, B has 4, and A∩B has 2. How many elements are in A∪B?", "5+4-2",
      "First find the union: 5+4−2=7."),
    n("A universal set has 8 elements, A has 5, B has 4, and A∩B has 2. How many elements are in the complement of A∪B?", "8-(5+4-2)",
      "The union has 5+4−2=7 elements. Its complement contains the remaining 8−7=1 element."),
    n("A has 6 elements and A∩B has 2. How many elements belong to A but not to B?", "6-2",
      "Remove the 2 shared elements from A, leaving 4 elements that belong only to A."),
    c("Do taking a complement and then an intersection always give the same result as doing them in the reverse order?", "Not necessarily",
      ["Always", "They differ only for the empty set", "They differ only for infinite sets"],
      "Changing the order of operations generally changes the result. Pay attention to parentheses and the universal set."),
])

T("logic.suff", C1, "1.4", "Sufficient and Necessary Conditions", NA, "reasoning",
  "Determine whether p is a sufficient condition for q, a necessary condition, or neither.",
  ["Interpret \"if p then q\" as p being a sufficient condition for q", "Give examples of conditions that are only sufficient or only necessary"],
  "PRE.04")
Qs("logic.suff", [
    c("For real x, what kind of condition is \"x>2\" for \"x>0\"?", "Sufficient but not necessary",
      ["Necessary but not sufficient", "Necessary and sufficient", "Neither necessary nor sufficient"],
      "x>2 implies x>0, so it is sufficient. But x>0 does not imply x>2, so it is not necessary."),
    c("For real x, what kind of condition is \"x>0\" for \"x>2\"?", "Necessary but not sufficient",
      ["Sufficient but not necessary", "Necessary and sufficient", "Neither necessary nor sufficient"],
      "x>2 requires x>0, so it is necessary. But x>0 alone does not imply x>2, so it is not sufficient."),
    n("Let A={1, 2} and B={1, 2, 3}. Record 1 if \"x∈A\" implies \"x∈B\" and 0 if it does not. What should be recorded?", "1",
      "A is a subset of B, so x∈A always implies x∈B. Record 1."),
    c("What kind of condition is \"x=1\" for \"x²=1\"?", "Sufficient but not necessary",
      ["Necessary but not sufficient", "Necessary and sufficient", "Neither necessary nor sufficient"],
      "x=1 implies x²=1, but x²=1 also allows x=−1, so x=1 is not necessary."),
])

T("logic.iff", C1, "1.4", "Necessary and Sufficient Conditions", NA, "reasoning",
  "Know that a necessary and sufficient condition implies the other condition in both directions, and determine whether simple statements are equivalent.",
  ["Explain that necessary and sufficient means each condition implies the other", "Determine whether two simple conditions are equivalent"],
  "PRE.04", "inferred", "A necessary and sufficient condition is both sufficient and necessary. Source wording needs verification.")
Qs("logic.iff", [
    c("For real x, what kind of condition is \"x²=4\" for \"x=2 or x=−2\"?", "Necessary and sufficient",
      ["Sufficient but not necessary", "Necessary but not sufficient", "Neither necessary nor sufficient"],
      "Each statement implies the other: the real solutions of x²=4 are exactly 2 and −2."),
    c("Is \"two sides of a triangle are equal\" a necessary and sufficient condition for \"two angles of the triangle are equal\"?",
      "Necessary and sufficient", ["Sufficient but not necessary", "Necessary but not sufficient", "Neither necessary nor sufficient"],
      "Equal sides imply equal opposite angles, and equal angles imply equal opposite sides, so each condition implies the other."),
    n("If p is a necessary and sufficient condition for q, record 1 for \"p implies q\" and 1 for \"q implies p.\" What is the sum of the two values?", "1+1",
      "Necessary and sufficient means both implications hold, so 1+1=2."),
    c("What kind of condition is \"x>1\" for \"x≥1\"?", "Sufficient but not necessary",
      ["Necessary and sufficient", "Necessary but not sufficient", "Neither necessary nor sufficient"],
      "x>1 implies x≥1, but x≥1 also allows x=1, which does not imply x>1."),
])

T("logic.quant", C1, "1.5", "Universal and Existential Quantifiers", NA, "conceptual",
  "Distinguish \"for all\" from \"there exists\" and determine whether simple statements with one quantifier are true.",
  ["Identify whether a statement uses a universal or existential quantifier", "Determine whether a statement is true over a given domain"],
  "PRE.05")
Qs("logic.quant", [
    c("Which quantifier appears in the statement \"The square of every real number is greater than or equal to 0\"?", "A universal quantifier",
      ["An existential quantifier", "No quantifier", "Both universal and existential quantifiers"],
      "\"Every\" is a universal quantifier. The statement is true."),
    c("Is the statement \"There is a real number whose square is −1\" true or false?", "False",
      ["True", "True and universal", "Cannot be determined"],
      "The square of a real number cannot be negative, so no such real number exists; the statement is false."),
    n("How many elements in {1, 2, 3} satisfy x>2? Use this to decide whether there exists an x>2.", "len([3])",
      "Only 3 is greater than 2, so there is 1 such element and the existential statement is true."),
    c("Which quantifier appears in the statement \"Some right triangles are isosceles\"?", "An existential quantifier",
      ["A universal quantifier", "A negation quantifier", "No quantifier"],
      "\"Some\" means that at least one exists, so it is an existential quantifier. An isosceles right triangle does exist."),
])

T("logic.neg", C1, "1.5", "Negating Statements with One Quantifier", NA, "reasoning",
  "Negate statements with one quantifier: the negation of a universal statement is existential, and the negation of an existential statement is universal.",
  ["Write the negation of a universal statement", "Write the negation of an existential statement"],
  "PRE.05", "inferred", "Negating statements is included with the curriculum-standard requirement on universal and existential quantifiers. Source wording needs verification.")
Qs("logic.neg", [
    c("What is the negation of \"Every real number is greater than 0\"?", "There is a real number that is not greater than 0",
      ["Every real number is not greater than 0", "There is a real number greater than 0", "Every real number is less than 0"],
      "The negation of a universal statement is existential, and the predicate is negated. Do not simply change \"every\" to \"every ... not.\""),
    c("What is the negation of \"There is an even integer\"?", "Every integer is not even",
      ["There is an integer that is not even", "Every integer is even", "There are no odd integers"],
      "The negation of an existential statement is universal, with the predicate negated to \"not even.\""),
    n("The statement \"1>0\" is true and is assigned truth value 1. What truth value should its negation have?", "0",
      "The negation of a true statement is false, so its truth value is 0."),
    c("When negating \"There exists x∈R such that x²<0,\" which quantifier should be used?", "A universal quantifier",
      ["An existential quantifier again", "No quantifier", "Two existential quantifiers"],
      "The negation of an existential statement is universal. The original statement is false, so its negation, \"the square of every real number is greater than or equal to 0,\" is true."),
])

# ---------------------------------------------------------------- Chapter 2

T("ine.eq", C2, "2.1", "Properties of Equations and the Meaning of Inequalities", NA, "conceptual",
  "Distinguish equations from inequalities and know that an inequality expresses an order relationship between two real numbers.",
  ["Determine whether an expression is an equation or an inequality", "Know that both sides of an inequality are real numbers"],
  "PRE.06")
Qs("ine.eq", [
    c("What relationship is expressed by 3<5?", "An inequality relationship", ["An equality relationship", "Set membership", "A function mapping"],
      "The less-than symbol states that the numbers are unequal and ordered, so it expresses an inequality."),
    n("What is the solution to 2x=6?", "6/2",
      "Divide both sides by 2 to get x=3. The properties of equality give the unique solution."),
    n("If a=b, what is the difference between a+3 and b+3?", "0",
      "Adding the same number to both sides preserves equality, so the difference is 0."),
    c("Which expression is an inequality?", "x+1>0", ["x+1=0", "x+1", "{x | x>0}"],
      "An inequality uses a symbol such as greater than or less than to express an ordering relationship."),
])

T("ine.def", C2, "2.1", "Solution Sets of Inequalities", NA, "procedural",
  "Solve simple linear inequalities in one variable and identify the integers in their solution sets.",
  ["Write the solutions of an inequality as a range", "Find the integers in a solution set"],
  "PRE.06", "inferred", "A solution set is a direct application of inequality properties and uses the solution-set language introduced in junior high. Source wording needs verification.")
Qs("ine.def", [
    n("What is the smallest positive integer solution of x+3>5?", "3",
      "x>2. The smallest positive integer greater than 2 is 3."),
    n("What is the greatest integer solution of 2x−1<5?", "2",
      "2x<6, so x<3. The greatest integer less than 3 is 2."),
    n("How many integer solutions of x≥4 are less than or equal to 7?", "len([4,5,6,7])",
      "The solutions are 4, 5, 6, and 7: 4 integers."),
    c("What is the solution set of x>1?", "All real numbers greater than 1",
      ["Only 2", "All real numbers greater than or equal to 1", "All positive integers"],
      "Since the domain is not restricted to integers, the solution set consists of real numbers, and it excludes 1."),
])

T("ine.prop", C2, "2.1", "Properties of Inequalities", NA, "reasoning",
  "Apply the basic properties of inequalities: adding the same number to both sides or multiplying by a positive number preserves the direction; multiplying by a negative number reverses it.",
  ["Determine whether an inequality sign must reverse after a transformation", "Use the properties to compare two numbers"],
  "PRE.06", "inferred", "Proofs of the properties are grouped with the curriculum-standard clause on equation and inequality properties. Source wording needs verification.")
Qs("ine.prop", [
    n("Given a>b, compare a+4 with b+4. Answer 1 if a+4 is greater, −1 if it is smaller, and 0 if they are equal.", "1",
      "Adding the same number to both sides preserves the inequality direction, so a+4 is still greater."),
    n("Given a>b, compare −2a with −2b. Answer 1 if −2a is greater and −1 if it is smaller.", "-1",
      "Multiplication by a negative number reverses the inequality, so −2a < −2b and −2a is smaller."),
    c("When both sides are multiplied by −3, what should happen to the inequality sign?", "Reverse direction", ["Keep its direction", "Change it to an equals sign", "Remove the sign"],
      "Multiplication or division by a negative number reverses the inequality sign."),
    n("If a−b=5, and a>b is recorded as 1, what should be recorded?", "1",
      "The difference is positive, so a is greater than b."),
])

T("ine.diff", C2, "2.1", "Comparing Values by Subtraction", NA, "procedural",
  "Subtract two expressions and use the sign of the difference to determine their order.",
  ["Correctly calculate the difference between two expressions", "Use the sign of the difference to determine which is greater"],
  "PRE.06", "inferred", "Subtraction is one method of comparison; the curriculum standard requires comparing values. Source wording needs verification.")
Qs("ine.diff", [
    n("Compare 2³ and 3² by calculating 2³−3².", "2**3-3**2",
      "8−9=−1. The difference is negative, so 2³ is smaller."),
    n("To compare (a+1)² with a²+1, first calculate the nonconstant part of their difference. The difference is 2a. What is it when a=3?", "2*3",
      "(a+1)²−(a²+1)=2a. When a=3, the difference is 6, so the first expression is greater."),
    n("What is the difference between 7² and 50?", "7**2-50",
      "49−50=−1, so 7² is less than 50."),
    c("What does a difference of 0 between two expressions show?", "The expressions are equal", ["The first is greater", "The second is greater", "They cannot be compared"],
      "A difference of 0 means equality; a positive difference means the first is greater, and a negative difference means it is smaller."),
])

T("ine.int", C2, "2.1", "Integer Solutions of Inequalities", NA, "procedural",
  "List and count the integer solutions of an inequality within a specified range.",
  ["List all integers in the solution set", "Find the number or sum of those integers"],
  "PRE.06", "inferred", "Integer solutions restrict an inequality's solution set to integers and remain part of inequality solving. Source wording needs verification.")
Qs("ine.int", [
    n("How many integer solutions does 1<x<5 have?", "len([2,3,4])",
      "The endpoints are excluded; the integer solutions are 2, 3, and 4, for a total of 3."),
    n("What is the sum of the integer solutions of 0≤x≤3?", "0+1+2+3",
      "The integer solutions are 0, 1, 2, and 3, which sum to 6."),
    n("How many integer solutions does −2≤x<2 have?", "len([-2,-1,0,1])",
      "−2 is included and 2 is excluded, giving 4 integer solutions."),
    c("What is the smallest integer solution of x>3?", "4", ["3", "5", "There is none"],
      "The integers greater than 3 start at 4. The number 3 itself does not satisfy the strict inequality."),
])

T("ine.amgm", C2, "2.2", "The Arithmetic Mean-Geometric Mean Inequality", NA, "procedural",
  "Know that the arithmetic mean of two positive numbers is at least their geometric mean, with equality if and only if the numbers are equal.",
  ["Calculate the arithmetic and geometric means of two positive numbers", "State the condition for equality"],
  "PRE.07")
Qs("ine.amgm", [
    n("What is the arithmetic mean of 4 and 9?", "(4+9)/2",
      "The arithmetic mean is (4+9)/2=13/2."),
    n("What is the geometric mean of 4 and 9?", "isqrt(4*9)",
      "The geometric mean is √(4×9)=√36=6."),
    c("When does equality hold in the arithmetic mean-geometric mean inequality (a+b)/2 ≥ √(ab)?", "a=b and both are positive",
      ["a and b only need to be positive", "a+b=1", "ab=1"],
      "The arithmetic mean and geometric mean are equal when the two positive numbers are equal."),
    n("What is the arithmetic mean of 1 and 1 minus their geometric mean?", "(1+1)/2-isqrt(1*1)",
      "Both means are 1, so their difference is 0 and equality holds."),
])

T("ine.amgmapp", C2, "2.2", "Finding Extrema with the AM-GM Inequality", NA, "application",
  "Use the arithmetic mean-geometric mean inequality to find extrema of positive numbers when their sum or product is fixed, and check whether equality is attainable.",
  ["Determine when the AM-GM inequality applies", "State the extremum and the values at which it is attained"],
  "PRE.07", "inferred", "Finding extrema is a straightforward application of the AM-GM inequality. Source wording needs verification.")
Qs("ine.amgmapp", [
    n("Positive numbers x and y satisfy x+y=10. What is the greatest possible value of xy?", "(10/2)**2",
      "The product is greatest when x=y=5; its maximum is 5×5=25."),
    n("Positive numbers x and y satisfy xy=16. What is the smallest possible value of x+y?", "2*isqrt(16)",
      "x+y ≥ 2√(xy)=8, with equality when x=y=4."),
    n("For positive x, what is the minimum value of x+4/x?", "2*isqrt(4)",
      "The product of x and 4/x is 4, so their sum is at least 2√4=4, attained when x=2."),
    c("When using the AM-GM inequality to find an extremum, what should you do if its equality condition cannot be met?", "Do not treat the bound as the extremum",
      ["Still call it the extremum", "Change the inequality sign to equality", "Use negative numbers instead"],
      "If equality cannot be attained, the bound is not the minimum or maximum."),
])

T("ine.three", C2, "2.3", "Quadratic Functions and Equations", NA, "reasoning",
  "Interpret the roots of a quadratic equation as the intersections of the graph of its quadratic function with the x-axis.",
  ["Use the discriminant to determine the number of intersections", "Find the real roots of an equation"],
  "PRE.08")
Qs("ine.three", [
    n("What is the smaller real root of x²−5x+6=0?", "min(roots2(1,-5,6))",
      "Factor to get (x−2)(x−3)=0; the smaller root is 2."),
    n("What is the larger real root of x²−5x+6=0?", "max(roots2(1,-5,6))",
      "The roots are 2 and 3, so the larger one is 3."),
    n("What is the positive root of x²−4=0?", "max(roots2(1,0,-4))",
      "x²=4, so the real roots are −2 and 2; the positive root is 2."),
    c("How many times does the graph of y=x²+1 intersect the x-axis?", "0", ["1", "2", "Infinitely many"],
      "x²+1=0 has no real roots, so the graph lies entirely above the x-axis."),
])

T("ine.quad", C2, "2.3", "Quadratic Inequalities in One Variable", NA, "procedural",
  "Solve quadratic inequalities in one variable using factorization or function graphs, and count their integer solutions.",
  ["Determine the form of a quadratic inequality's solution set", "Count the integers in the solution set"],
  "PRE.09")
Qs("ine.quad", [
    n("How many integer solutions does x²−5x+6<0 have?", "0",
      "(x−2)(x−3)<0, so 2<x<3; there are no integers between 2 and 3."),
    n("What is the sum of the integer solutions of x²−5x+6≤0?", "2+3",
      "The solution set is 2≤x≤3, with integer solutions 2 and 3; their sum is 5."),
    n("How many integer solutions satisfy x²−4>0 and |x|<4?", "len([-3,3])",
      "x²>4 gives x<−2 or x>2. With −4<x<4, the only integer solutions are −3 and 3, so there are 2."),
    n("What is the sum of the integer solutions of (x−1)(x−4)<0?", "2+3",
      "The solution set is 1<x<4, with integer solutions 2 and 3; their sum is 5."),
])

import hs_book1_b  # noqa: E402,F401
import hs_book1_c  # noqa: E402,F401
import hs_book1_edges  # noqa: E402,F401
