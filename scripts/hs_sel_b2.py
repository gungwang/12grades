"""People's Education Press A edition (2019), Selective Compulsory Book 2.

The chapter outline is based on the following third-party sources, neither of which is an official People's Education Press website. Page numbers have not been verified:
- Teacher's Home https://www.renjiaoshe.com/jiaocai/2073.html (4.1–4.4, 5.1–5.3)
- 21st Century Education Network textbook overview http://zy.21cnjy.com/20824168 (lists sequences and derivatives, and mentions mathematical induction)

Section 4.4 is listed as “Mathematical Induction*” in the Teacher's Home outline. An asterisk usually marks optional material, but the curriculum standard includes this requirement, so whether it is compulsory is unverified.
Only sections that could be matched are included; no page numbers are invented. More detailed headings such as 5.1.1 come from a study-guide outline and are not included in section.
"""
from hs_sel_common import questions, topic

NA = "Numbers and Algebra"

# The Chinese chapter-number markers are required by hs_build.py's ch_num parser.
C4 = "第四章 Sequences"
C5 = "第五章 Derivatives and Their Applications for One-Variable Functions"


def T(key, chapter, section, name, typ, desc, crit, std, conf="exact", note=None):
    topic(key, 2, chapter, section, name, NA, typ, desc, crit, std, conf, note)


def Qs(key, items):
    questions(key, items)


def n(prompt, verify, expl):
    return ("n", prompt, verify, expl)


def c(prompt, ok, bad, expl):
    return ("c", prompt, ok, bad, expl)


NOTE = "The textbook practices this requirement in separate sections. Pending verification."

# ---------------------------------------------------------------- Chapter 4

T("seq.def", C4, "4.1", "Concept of a Sequence", "conceptual",
  "A sequence is an ordered list of numbers, and each term has a definite index.",
  ["Recognize that order matters in a sequence", "Identify a term by its index"],
  "FUN.18")
Qs("seq.def", [
    c("Which statement best distinguishes a sequence from a set?", "Order matters in a sequence, but not in a set",
      ["A sequence cannot contain repeated numbers", "A sequence must have infinitely many terms", "Every term in a sequence must be positive"],
      "A sequence is ordered. Rearranging the same numbers usually gives a different sequence."),
    n("What is the third term of the sequence 3, 5, 7, 9?", "7",
      "Counting from the first term, the third term is 7."),
    n("How many terms are in the sequence 2, 4, 6, 8, 10?", "5",
      "Count all five listed terms."),
    c("Is 1, 1, 1, 1 a sequence?", "Yes; all the terms may be equal",
      ["No, because terms repeat", "No, because it is not increasing", "No, because it has no general term"],
      "A constant sequence is still a sequence; every term is 1."),
])

T("seq.rep", C4, "4.1", "Representing Sequences", "conceptual",
  "A sequence can be represented by listing its terms, using a general-term formula, or drawing a graph. Its graph consists of isolated points.",
  ["Read a specified term from a list", "Recognize that a sequence graph is not a continuous curve"],
  "FUN.18", "inferred", NOTE)
Qs("seq.rep", [
    n("The general term is a_n=2n+1. What is the fourth term?", "2*4+1",
      "Substitute n=4 to get 8+1=9."),
    c("What does the graph of a sequence usually look like?", "A set of isolated points",
      ["A continuous straight line", "An entire parabola", "A circle"],
      "The indices are positive integers, so the graph has points only at positive integer values; it is not a continuous curve."),
    n("The first four terms are 1, 3, 5, 7. What is the sum of the first and fourth terms?", "1+7",
      "1+7=8."),
    c("When a sequence is written using a general-term formula, what values does n usually take?", "Positive integers",
      ["Any real number", "Any negative number", "Only 0"],
      "Term indices start at 1 and are positive integers."),
])

T("seq.term", C4, "4.1", "General-Term Formula", "procedural",
  "A general-term formula expresses the nth term in terms of its index n. Once the formula is known, any specified term can be found.",
  ["Substitute an index into a general-term formula", "Find a simple general term from the first few terms"],
  "FUN.18", "inferred", NOTE)
Qs("seq.term", [
    n("a_n=3n−1. What is a_4?", "3*4-1",
      "3×4−1=11."),
    n("a_n=n². What is a_5?", "5*5",
      "5 squared is 25."),
    n("a_n=10−n. What is a_3?", "10-3",
      "10−3=7."),
    c("What are the first three terms of a_n=2n?", "2, 4, 6",
      ["1, 2, 3", "2, 3, 4", "1, 3, 5"],
      "Substituting n=1, 2, and 3 gives 2, 4, and 6."),
])

T("seq.rec", C4, "4.1", "Simple Recurrence Relations", "procedural",
  "A recurrence expresses later terms using earlier terms. Given the first term and the recurrence, the sequence can be calculated term by term.",
  ["Find the next term from the first term and a recurrence", "Distinguish a general-term formula from a recurrence"],
  "FUN.18", "inferred", NOTE)
Qs("seq.rec", [
    n("a_1=3, a_{n+1}=a_n+4. What is a_2?", "3+4",
      "Each term is 4 greater than the previous one, so a_2=7."),
    n("a_1=2, a_{n+1}=3a_n. What is a_3?", "2*3*3",
      "a_2=6 and a_3=18."),
    n("a_1=5, a_{n+1}=a_n−1. What is a_4?", "5-3",
      "There are three steps from the first to the fourth term, so a_4=2."),
    c("What does a_{n+1}=a_n+2 describe?", "A recurrence relation",
      ["A general term that gives any term directly without the first term", "The sum of the sequence", "The derivative of a function"],
      "It expresses each term using the previous term; the first term is also needed to determine the sequence."),
])

T("ap.def", C4, "4.2", "Definition of an Arithmetic Sequence", "conceptual",
  "A sequence is arithmetic if, from the second term onward, the difference between each term and the previous term is the same constant. This constant is the common difference.",
  ["Determine whether a sequence is arithmetic", "Find the common difference"],
  "FUN.19")
Qs("ap.def", [
    n("What is the common difference of 3, 7, 11, 15?", "7-3",
      "Subtract consecutive terms: 7−3=4."),
    c("Is 2, 5, 8, 11 an arithmetic sequence?", "Yes, with common difference 3",
      ["No, because all terms are positive", "No, because it has finitely many terms", "Yes, with common difference 2"],
      "Every pair of consecutive terms differs by 3, so this is an arithmetic sequence with common difference 3."),
    n("An arithmetic sequence has first term 6 and common difference −2. What is the second term?", "6+(-2)",
      "6−2=4."),
    c("Is the constant sequence 5, 5, 5, 5 arithmetic?", "Yes, with common difference 0",
      ["No, the common difference must be positive", "No, because the difference is 0", "Yes, with common difference 5"],
      "Every consecutive difference is 0, so it is still an arithmetic sequence, with common difference 0."),
])

T("ap.term", C4, "4.2", "General Term of an Arithmetic Sequence", "procedural",
  "For an arithmetic sequence with first term a1 and common difference d, the general term is a_n=a1+(n−1)d.",
  ["Find a specified term from the first term and common difference", "Find the common difference from two terms"],
  "FUN.19")
Qs("ap.term", [
    n("An arithmetic sequence has a_1=3 and d=4. What is a_6?", "3+5*4",
      "a_6=3+(6−1)×4=23."),
    n("An arithmetic sequence has a_1=10 and d=−3. What is a_4?", "10+3*(-3)",
      "10+(4−1)×(−3)=1."),
    n("An arithmetic sequence has a_3=8 and a_7=20. What is the common difference?", "Fraction(20-8, 7-3)",
      "There are four common differences between the terms: (20−8)/4=3."),
    c("The general term of an arithmetic sequence is linear. What happens to a term when n increases by 1?", "It increases by one common difference",
      ["It doubles", "It always stays the same", "It is squared"],
      "Consecutive terms differ by d, so increasing the index by 1 adds one common difference."),
])

T("ap.mid", C4, "4.2", "Arithmetic Mean", "procedural",
  "If a, b, c form an arithmetic sequence, then 2b=a+c, and b is the arithmetic mean of a and c.",
  ["Find the arithmetic mean from the two endpoints", "Determine whether three numbers form an arithmetic sequence"],
  "FUN.19", "inferred", NOTE)
Qs("ap.mid", [
    n("What is the arithmetic mean of 5 and 11?", "Fraction(5+11, 2)",
      "(5+11)/2=8."),
    n("The arithmetic mean is 6 and the first number is 2. What is the last number?", "2*6-2",
      "2×6=2+the last number, so the last number is 10."),
    n("The numbers 4, k, 10 form an arithmetic sequence. What is k?", "Fraction(4+10, 2)",
      "2k=14, k=7."),
    c("If a, b, c form an arithmetic sequence, which equation is equivalent?", "2b=a+c",
      ["2b=ac", "b=a+c", "b²=ac"],
      "Twice the middle term equals the sum of the endpoints. b²=ac is the relation for a geometric mean."),
])

T("ap.sum", C4, "4.2", "Sum of the First n Terms of an Arithmetic Sequence", "procedural",
  "The sum of the first n terms is S_n=n(a1+a_n)/2, or equivalently S_n=na1+n(n−1)d/2.",
  ["Find the sum of the first n terms from the first and last terms", "Find the sum of the first n terms from the first term and common difference"],
  "FUN.19")
Qs("ap.sum", [
    n("An arithmetic sequence has a_1=3 and a_6=23. What is the sum of the first 6 terms?", "6*(3+23)//2",
      "S_6=6×(3+23)/2=78."),
    n("An arithmetic sequence has a_1=2 and d=3. What is the sum of the first 5 terms?", "5*2+5*4*3//2",
      "S_5=5×2+5×4×3/2=10+30=40."),
    n("The sum of the first 10 terms is 100 and the sum of the first 9 is 81. What is the 10th term?", "100-81",
      "The 10th term is S_10−S_9=19."),
    c("To find the sum of the first n terms of an arithmetic sequence, what do you do after adding the first and last terms and multiplying by n?", "Divide by 2",
      ["Multiply by 2", "Square the result", "Do nothing else"],
      "The formula is n times the sum of the first and last terms, divided by 2."),
])

T("ap.fn", C4, "4.2", "Arithmetic Sequences and Linear Functions", "reasoning",
  "The general term a_n=dn+(a1−d) of an arithmetic sequence is a linear function of n, and the common difference is the coefficient of n.",
  ["Write a general term as a linear function", "Read the common difference from the coefficient of n"],
  "FUN.19", "inferred", NOTE)
Qs("ap.fn", [
    n("The general term is a_n=4n−1. What is the common difference?", "4",
      "The coefficient of n, 4, is the common difference."),
    n("The general term is a_n=4n−1. What is the first term?", "4*1-1",
      "Substituting n=1 gives 3."),
    c("Which type of function graph contains the points of an arithmetic sequence?", "The graph of a linear function",
      ["The graph of an exponential function", "The graph of an inverse-proportion function", "A circle"],
      "The general term is linear in n, so these points lie on a straight line."),
    n("An arithmetic sequence has common difference −2 and first term 9. What is the coefficient of n in a_n?", "-2",
      "a_n=−2n+constant, so the coefficient of n is the common difference, −2."),
])

T("ap.app", C4, "4.2", "Applications of Arithmetic Sequences", "application",
  "Savings that increase by a fixed amount each period and the number of seats in successive rows can often be modeled by arithmetic sequences.",
  ["Recognize a fixed increase per period as the common difference", "Find a specified term or the sum of the first several terms"],
  "FUN.19", "inferred", NOTE)
Qs("ap.app", [
    n("A theater has 20 seats in the first row, with 2 more seats in each following row. How many seats are in the sixth row?", "20+5*2",
      "This is an arithmetic sequence with a_1=20 and d=2, so a_6=30."),
    n("A theater has 20 seats in the first row, with 2 more seats in each following row. How many seats are there in the first six rows?", "6*(20+30)//2",
      "The last row has 30 seats, so S_6=6×50/2=150."),
    n("Each month, a person saves 10 yuan more than the previous month. If the first month's deposit is 100 yuan, how much is deposited in the fourth month?", "100+3*10",
      "a_4=100+3×10=130 yuan."),
    c("If someone walks a fixed number of steps more each day than the day before, which sum model fits the total number of steps?", "The sum of the first n terms of an arithmetic sequence",
      ["The sum of the first n terms of a geometric sequence", "The first day's steps multiplied by the number of days", "The average value of a derivative"],
      "The daily increase is fixed, so the terms form an arithmetic sequence."),
])

T("gp.def", C4, "4.3", "Definition of a Geometric Sequence", "conceptual",
  "A sequence is geometric if, from the second term onward, the ratio of each term to the previous term is the same nonzero constant. This constant is the common ratio.",
  ["Determine whether a sequence is geometric", "Find the common ratio"],
  "FUN.20")
Qs("gp.def", [
    n("What is the common ratio of 2, 6, 18, 54?", "6//2",
      "Divide a term by the previous term: 6/2=3."),
    c("Is 5, 5, 5, 5 a geometric sequence?", "Yes, with common ratio 1",
      ["No, the common ratio cannot be 1", "No, because the difference is 0", "Yes, with common ratio 5"],
      "Every consecutive ratio is 1, so it is both an arithmetic and a geometric sequence."),
    n("A geometric sequence has first term 3 and common ratio −2. What is the second term?", "3*(-2)",
      "3×(−2)=−6."),
    c("Can a geometric sequence contain a zero term?", "No; the ratio of the next term to that term would be undefined or would not remain a fixed common ratio",
      ["Yes, with common ratio 0", "Yes, as long as it has finitely many terms", "Every term must be 0"],
      "If a term is 0, the ratio of the next term to it cannot be a fixed nonzero constant. The textbook requires both the common ratio and the terms to be nonzero."),
])

T("gp.term", C4, "4.3", "General Term of a Geometric Sequence", "procedural",
  "For a geometric sequence with first term a1 and common ratio q, the general term is a_n=a1·q^(n−1).",
  ["Find a specified term from the first term and common ratio", "Find the common ratio from two terms"],
  "FUN.20")
Qs("gp.term", [
    n("A geometric sequence has a_1=2 and q=3. What is a_4?", "2*3**3",
      "a_4=2×3³=54."),
    n("A geometric sequence has a_1=5 and q=2. What is a_3?", "5*2**2",
      "5×4=20."),
    n("A geometric sequence has a_2=6 and a_5=48, with a positive common ratio. What is the common ratio?", "2",
      "a_5=a_2·q³, 48=6q³, q³=8, q=2."),
    c("In a geometric sequence with common ratio −1, how are consecutive terms related?", "They are opposites",
      ["They are always equal", "Every term is 0", "The common difference is −1"],
      "Multiplication by −1 changes the sign, so consecutive terms are opposites."),
])

T("gp.mid", C4, "4.3", "Geometric Mean", "procedural",
  "If a, G, b form a geometric sequence and have the same sign, then G²=ab. G is the geometric mean of a and b.",
  ["Find the geometric mean of two positive numbers", "Distinguish a geometric mean from an arithmetic mean"],
  "FUN.20", "inferred", NOTE)
Qs("gp.mid", [
    n("What is the positive geometric mean of 2 and 8?", "isqrt(2*8)",
      "G²=16, so the positive value is G=4."),
    n("What is the geometric mean of the positive numbers 3 and 12?", "isqrt(3*12)",
      "G²=36, G=6."),
    c("What relation does the geometric mean of two positive numbers satisfy?", "Its square equals the product of the two numbers",
      ["Twice it equals the sum of the two numbers", "It equals the difference of the two numbers", "It equals the sum of the two numbers"],
      "G²=ab. Twice the middle term equaling the sum of the endpoints describes an arithmetic mean."),
    n("The positive numbers 4, k, 16 form a geometric sequence. What is k?", "isqrt(4*16)",
      "k²=64, k=8."),
])

T("gp.sum", C4, "4.3", "Sum of the First n Terms of a Geometric Sequence", "procedural",
  "When q≠1, S_n=a1(q^n−1)/(q−1). When q=1, S_n=na1.",
  ["Use the sum formula when the common ratio is not 1", "Recognize that the case q=1 must be handled separately"],
  "FUN.20")
Qs("gp.sum", [
    n("A geometric sequence has a_1=2 and q=3. What is the sum of the first 4 terms?", "2*(3**4-1)//(3-1)",
      "S_4=2×(81−1)/2=80."),
    n("A geometric sequence has a_1=5 and q=1. What is the sum of the first 4 terms?", "4*5",
      "When the common ratio is 1, every term is 5, so the sum is 20."),
    n("A geometric sequence has a_1=1 and q=2. What is the sum of the first 5 terms?", "(2**5-1)//(2-1)",
      "S_5=1×(32−1)/1=31."),
    c("Why can't S_n=a1(q^n−1)/(q−1) be used directly when q=1?", "The denominator is 0",
      ["A sequence with common ratio 1 does not exist", "The first term must be 0", "The sequence must have infinitely many terms"],
      "q−1=0, so the denominator is undefined; use S_n=na1 instead."),
])

T("gp.fn", C4, "4.3", "Geometric Sequences and Exponential Functions", "reasoning",
  "The general term a_n=a1·q^(n−1) of a geometric sequence is exponential in form, with the common ratio as its base.",
  ["Identify the common ratio as the exponential base", "Compare the domains of a geometric sequence and an exponential function"],
  "FUN.20", "inferred", NOTE)
Qs("gp.fn", [
    n("The general term is a_n=3×2^(n−1). What is the common ratio?", "2",
      "Each term is multiplied by 2 to get the next term, so the common ratio is 2."),
    n("The general term is a_n=3×2^(n−1). What is a_1?", "3*2**0",
      "2^0=1, so the first term is 3."),
    c("What is the main difference between a geometric sequence and the exponential function y=a1·q^(x−1)?", "The sequence's input takes only positive integer values",
      ["The sequence's base must be negative", "An exponential function cannot have positive values", "They are completely unrelated"],
      "The general-term formula has the same form, but n takes only positive integer values, so the graph consists of isolated points."),
    n("A geometric sequence has common ratio 4 and first term 1. What is a_3?", "1*4**2",
      "a_3=4²=16."),
])

T("gp.app", C4, "4.3", "Applications of Geometric Sequences", "application",
  "Quantities that grow or shrink by the same ratio can be modeled by geometric sequences.",
  ["Recognize a fixed growth rate as a common ratio", "Find a quantity after several periods"],
  "FUN.20", "inferred", NOTE)
Qs("gp.app", [
    n("A bacteria population doubles each hour. If it starts at 3, how many bacteria are there after 3 hours?", "3*2**3",
      "After tripling by a factor of 2 three times, 3×2³=24. If the starting amount is counted as the first term, the amount after 3 hours is the fourth term."),
    n("A savings balance doubles each year. If it is 100 yuan at the end of year 1, how much is it at the end of year 3?", "100*2**2",
      "The balance doubles twice from the end of year 1 to the end of year 3, giving 400 yuan."),
    n("Each time a sheet of paper is folded, the number of layers doubles. One fold makes 2 layers. How many layers are there after 4 folds?", "2**4",
      "Four folds make 16 layers."),
    c("Which model fits a quantity multiplied by the same growth factor every year?", "A geometric sequence",
      ["An arithmetic sequence with a nonzero common difference", "The mean alone", "The slope of a linear function"],
      "The ratio of consecutive terms is fixed, so the sequence is geometric."),
])

T("ind.idea", C4, "4.4", "Principle of Mathematical Induction", "conceptual",
  "Mathematical induction first verifies the base case, then proves that if the statement holds for n=k, it also holds for n=k+1. This establishes it for all positive integers.",
  ["State the two steps of induction", "Recognize that checking only a few specific values is not a proof"],
  "FUN.21", "inferred", "The Teacher's Home outline marks Section 4.4, Mathematical Induction, with an asterisk, which usually indicates optional material. The curriculum standard requires familiarity with the principle; whether it is compulsory is unverified.")
Qs("ind.idea", [
    c("What is usually the first step of mathematical induction?", "Verify the base case",
      ["Assume the statement holds for every positive integer", "Find the derivative first", "Draw a graph without checking the claim"],
      "First verify the starting value, for example, that the statement holds for n=1."),
    c("What must be proved in the second step?", "If the statement holds for n=k, then it also holds for n=k+1",
      ["If it holds for n=k, then it holds for n=1", "Check only n=2 and n=3", "Prove that the common difference is 0"],
      "This step shows that any valid case k implies the next case."),
    n("The sum of the first n positive odd numbers is n². What is the sum when n=1?", "1",
      "The first positive odd number is 1, and 1²=1, so the base case holds."),
    c("Can checking that a statement holds for n=1, 2, 3, and 4 replace mathematical induction?", "No; finitely many examples do not constitute a proof",
      ["Yes, four examples are enough", "Yes, as long as all values are positive", "No, because induction does not allow checking the base case"],
      "Induction uses the recurrence step to cover every positive integer after the base case; checking only a few values is not enough."),
])

T("ind.use", C4, "4.4", "Proving Simple Statements by Induction", "reasoning",
  "To prove an identity involving positive integers, state the base case and show the steps from k to k+1.",
  ["Verify the base case", "Use the induction hypothesis in the inductive step"],
  "FUN.21")
Qs("ind.use", [
    n("The sum of the first n positive integers is n(n+1)/2. What is the sum when n=5?", "5*6//2",
      "The formula gives 15. Adding 1+2+3+4+5 directly also gives 15."),
    n("Consider the statement “n²+n is even.” What is n²+n when n=4?", "4*4+4",
      "16+4=20, which is even. A proof by induction must also show the step from k to k+1."),
    c("In an inductive step, which statement may be assumed?", "The statement holds for n=k",
      ["The statement already holds for n=k+1", "It holds for every real number", "The common difference is 1"],
      "This is the induction hypothesis. The goal is to prove the case n=k+1."),
    n("The sum of the first n positive odd numbers is n². What is the sum when n=6?", "6*6",
      "6²=36."),
])

# ---------------------------------------------------------------- Chapter 5

T("der.avg", C5, "5.1", "Average Rate of Change", "procedural",
  "The average rate of change of a function over an interval is the change in its function values divided by the change in its input values.",
  ["Calculate the average rate of change on a given interval", "Identify the average rate of change as the slope of a secant line"],
  "FUN.22")
Qs("der.avg", [
    n("For f(x)=x², what is the average rate of change from x=1 to x=3?", "Fraction(3*3-1*1, 3-1)",
      "(9−1)/(3−1)=4."),
    n("For f(x)=2x+1, what is the average rate of change from x=0 to x=4?", "Fraction((2*4+1)-(2*0+1), 4-0)",
      "The average rate of change of a linear function is its slope, 2."),
    n("A distance changes from 0 meters at t=0 to 20 meters at t=5. What is the average speed?", "Fraction(20-0, 5-0)",
      "20/5=4 meters per second."),
    c("Which line's slope on the graph of a function represents its average rate of change?", "The secant line through the two endpoints",
      ["The tangent at one endpoint", "A line perpendicular to the x-axis", "An asymptote"],
      "The secant connects the graph points at the interval's endpoints, and its slope is the average rate of change."),
])

T("der.inst", C5, "5.1", "Instantaneous Rate of Change and the Limit Idea", "conceptual",
  "As the change in the input approaches 0, the limit of the average rate of change is the instantaneous rate of change. Specific rational values are used here to illustrate the process.",
  ["Recognize the instantaneous rate of change as the limit of average rates of change", "Use smaller input changes to observe the average rate of change"],
  "FUN.22", "inferred", "The limit idea appears in the development of the derivative concept; limit calculations are not treated separately. Pending verification.")
Qs("der.inst", [
    n("For f(x)=x², what is the average rate of change from x=2 to x=2.5?", "Fraction(Fraction(5,2)**2-4, Fraction(1,2))",
      "f(2.5)=6.25 and f(2)=4. The change is 2.25; dividing by 0.5 gives 4.5."),
    n("For f(x)=x², the instantaneous rate of change at x=2 is the limit as the input change approaches 0. What is the value of 2x at x=2?", "2*2",
      "The derivative of x² is 2x, which equals 4 at x=2. The average rate of change approaches 4 as the interval shrinks."),
    c("How is the instantaneous rate of change obtained?", "As the limit of the average rate of change as the input change approaches 0",
      ["As any average rate of change", "As the function value itself", "As the length of the domain"],
      "First calculate an average rate of change, then let the interval length approach 0. This is the limit idea behind the derivative."),
    n("For f(x)=x² near x=1, what is the average rate of change when h=1?", "Fraction((1+1)**2-1, 1)",
      "(4−1)/1=3. As h gets smaller, the result approaches the derivative value 2."),
])

T("der.def", C5, "5.1", "Definition of a Derivative", "conceptual",
  "The derivative of a function at a point is its instantaneous rate of change there. The derivative is itself a function of the input, denoted f'(x).",
  ["Recognize the derivative as the instantaneous rate of change", "Calculate the derivative value of a basic power function at a point"],
  "FUN.22")
Qs("der.def", [
    n("For f(x)=x², f'(x)=2x. What is f'(3)?", "2*3",
      "Substitute x=3 into the derivative to get 6."),
    n("For f(x)=x³, f'(x)=3x². What is f'(2)?", "3*2*2",
      "3×4=12."),
    c("What is the derivative f'(x)?", "A function of the input variable",
      ["A fixed line segment unrelated to x", "The domain of the function", "The graph of the function itself"],
      "There may be a derivative value at every point; these values form the derivative function."),
    n("The derivative of the constant function f(x)=5 is 0. What is f'(4)?", "0",
      "A constant function does not change, so its derivative is 0 at every point."),
])

T("der.fun", C5, "5.1", "Derivative Function", "conceptual",
  "Collecting the derivative values at all points gives the derivative function. The original function and its derivative may have different domains.",
  ["Find a derivative at a point from the derivative function", "Distinguish f(x) from f'(x)"],
  "FUN.22", "inferred", NOTE)
Qs("der.fun", [
    n("f'(x)=3x²−3. What is f'(2)?", "3*2*2-3",
      "3×4−3=9."),
    n("f'(x)=4x. What is f'(0)?", "0",
      "4×0=0."),
    c("What is the relationship between f(x)=x² and f'(x)=2x?", "2x is the derivative of x²",
      ["They are the same function", "2x is the domain of x²", "2x is the graph of x²"],
      "The derivative is obtained from the original function and is generally a different function."),
    n("f'(x)=−2x+4. What is f'(1)?", "-2*1+4",
      "−2+4=2."),
])

T("der.geo", C5, "5.1", "Geometric Meaning of the Derivative", "conceptual",
  "The derivative of a function at a point is the slope of the tangent to the curve there.",
  ["Interpret a derivative value as a tangent slope", "Recognize that a positive derivative gives an upward-sloping tangent"],
  "FUN.22", "inferred", NOTE)
Qs("der.geo", [
    n("The derivative of y=x² at x=1 is 2. What is the tangent slope?", "2",
      "The derivative is the tangent slope, so the slope is 2."),
    c("When f'(x0)>0, how does the tangent at the corresponding point behave?", "It rises from left to right",
      ["It falls from left to right", "It is perpendicular to the x-axis", "It does not intersect the curve"],
      "A positive slope means the tangent rises."),
    n("f'(x)=2x. What is the tangent slope at x=−1?", "2*(-1)",
      "The slope is −2, so the tangent falls."),
    c("If a derivative does not exist, what might be true of the tangent?", "It is vertical, so its slope is undefined",
      ["Its slope must be 0", "The curve must be undefined", "It must pass through the origin"],
      "A cusp or vertical tangent, for example, has no finite slope, so the derivative cannot be written as a real number."),
])

T("der.tan", C5, "5.1", "Tangent-Line Equation", "procedural",
  "The tangent to a curve at (x0, y0) has slope f'(x0); write its equation in point-slope form.",
  ["Find the slope at a point of tangency", "Write the tangent equation in point-slope form and find its intercept"],
  "FUN.22", "inferred", NOTE)
Qs("der.tan", [
    n("The tangent to y=x² at (1, 1) has slope 2. What is its y-intercept?", "1+2*(0-1)",
      "y−1=2(x−1). When x=0, y=−1."),
    n("What is the tangent slope to y=x² at x=0?", "0",
      "The derivative 2x is 0 at x=0, so the tangent is the horizontal line y=0."),
    n("For f(x)=x³ and f'(x)=3x², what is the tangent slope at x=1?", "3*1*1",
      "3×1=3."),
    c("When writing a tangent equation in point-slope form, which point must be used?", "The point of tangency",
      ["The origin, regardless of where the tangent point is", "Any point unrelated to the curve", "The focus"],
      "The tangent passes through the point of tangency, and its slope is the derivative there."),
])

T("der.basic", C5, "5.2", "Derivatives of Basic Elementary Functions", "procedural",
  "The derivative of a constant function is 0, and (x^n)'=nx^(n−1). Use this rule to differentiate positive integer powers directly.",
  ["Differentiate power functions", "Recognize that the derivative of a constant function is 0"],
  "FUN.23")
Qs("der.basic", [
    n("For f(x)=x³, what is the derivative function's value at x=2?", "3*2**2",
      "(x³)'=3x², which equals 12 at x=2."),
    n("f(x)=x^4. What is f'(1)?", "4*1**3",
      "4x³ equals 4 at x=1."),
    n("f(x)=7. What is f'(5)?", "0",
      "The derivative of a constant is 0."),
    c("What is (x²)'?", "2x",
      ["x²", "2", "x"],
      "Bring the exponent to the front and reduce the exponent by 1: 2x."),
])

T("der.lin", C5, "5.2", "Derivative Rules for Sums, Differences, and Constant Multiples", "procedural",
  "The derivative of a sum or difference is the sum or difference of the derivatives. A constant factor can be taken outside the derivative.",
  ["Differentiate a polynomial term by term", "Differentiate a constant multiple of a function"],
  "FUN.23", "inferred", NOTE)
Qs("der.lin", [
    n("f(x)=x²+3x. What is f'(1)?", "2*1+3",
      "f'(x)=2x+3, which equals 5 at x=1."),
    n("f(x)=4x³−x. What is f'(1)?", "12*1**2-1",
      "f'(x)=12x²−1, which equals 11 at x=1."),
    n("f(x)=5x². What is f'(2)?", "10*2",
      "(5x²)'=10x, which equals 20 at x=2."),
    c("What is the derivative of a sum?", "The sum of the derivatives",
      ["The product of the derivatives", "The quotient of the derivatives", "The product of the original functions"],
      "(u+v)'=u'+v'."),
])

T("der.comp", C5, "5.2", "Derivatives of Simple Composite Functions", "procedural",
  "For a function of the form f(ax+b), the derivative is the outer derivative multiplied by the inner coefficient a.",
  ["Differentiate f(ax+b)", "Multiply the outer derivative by the coefficient a"],
  "FUN.23", "inferred", "The curriculum standard requires only composites of the form f(ax+b). Pending verification.")
Qs("der.comp", [
    n("y=(2x+1)². What is the derivative at x=1?", "2*(2*1+1)*2",
      "The outer derivative is 2(2x+1); multiply by the inner derivative 2. At x=1, this is 2×3×2=12."),
    n("y=(3x−1)². What is the derivative at x=1?", "2*(3*1-1)*3",
      "2×2×3=12."),
    n("f(x)=x² and y=f(2x). What is the derivative of y at x=1?", "2*(2*1)*2",
      "The derivative of x² at 2x is 2×(2x), then multiply by 2. At x=1, the result is 8."),
    c("When differentiating (ax+b)², what must be multiplied at the end?", "The inner coefficient a",
      ["Always multiply by 0", "Always divide by a", "Do not multiply by anything else"],
      "The chain rule requires multiplying by the inner derivative, which is a here."),
])

T("der.mono", C5, "5.3", "Derivatives and Monotonicity", "reasoning",
  "A function is increasing on an interval where f'(x)>0 and decreasing where f'(x)<0.",
  ["Determine whether a function increases or decreases from the sign of its derivative", "Recognize that isolated points where the derivative is 0 do not change monotonicity on the whole interval"],
  "FUN.24")
Qs("der.mono", [
    n("f(x)=x² and f'(x)=2x. What is f'(−1)?", "2*(-1)",
      "−2<0, so x² decreases near x=−1."),
    c("If f'(x)>0 throughout an open interval, how does the function behave on that interval?", "It is increasing",
      ["It is decreasing", "It is constant", "It is not monotonic"],
      "A positive derivative means the function value increases as the input increases."),
    n("f'(x)=−2x. What is f'(3)?", "-2*3",
      "−6<0, so the function decreases near x=3."),
    c("If f'(x) is negative on an interval, how does the graph move from left to right?", "Downward",
      ["Upward", "Stay horizontal", "Become a circle"],
      "A negative derivative means the function is decreasing, so the graph slopes downward."),
])

T("der.inc", C5, "5.3", "Finding Intervals of Monotonicity with Derivatives", "procedural",
  "Differentiate first, then solve f'(x)>0 and f'(x)<0 to find the intervals of monotonicity for polynomial functions of degree at most 3.",
  ["Find the derivative of a polynomial", "Write the solution set of f'(x)>0 as an interval of increase"],
  "FUN.24", "inferred", NOTE)
Qs("der.inc", [
    n("f(x)=x²−4x. What is x when f'(x)=0?", "2",
      "f'(x)=2x−4=0 gives x=2. The function decreases to the left and increases to the right."),
    n("f(x)=x³−3x. What is f'(1)?", "3*1*1-3",
      "f'(x)=3x²−3=3(x²−1), which is 0 at x=1."),
    n("f(x)=x³−3x. What is f'(2)?", "3*4-3",
      "3×4−3=9>0, so the function increases near x=2."),
    c("For f'(x)=2x−4, what is the solution to f'(x)>0?", "x>2",
      ["x<2", "x=2", "Any real number"],
      "Solving 2x−4>0 gives x>2, the interval where the function is increasing."),
])

T("der.ext", C5, "5.3", "Conditions for Local Extrema", "reasoning",
  "A zero derivative is a necessary condition for a differentiable function to have an extremum. A change in the derivative's sign across the point is sufficient.",
  ["Find points where the derivative is 0", "Distinguish local maxima from local minima using the signs on either side"],
  "FUN.24", "inferred", NOTE)
Qs("der.ext", [
    n("For f(x)=x²−4x+1, what is the x-coordinate of a possible extremum?", "2",
      "f'(x)=2x−4=0 gives x=2. The derivative changes from negative to positive, so this is a local minimum."),
    n("What is the value of f(x)=x²−4x+1 at x=2?", "2*2-4*2+1",
      "4−8+1=−3."),
    c("What is the derivative of a differentiable function usually at an extremum?", "It is 0",
      ["It is always positive", "It is always negative", "It never exists"],
      "A zero derivative is necessary for an extremum. However, a zero derivative alone does not guarantee one; check for a sign change on either side."),
    c("What kind of point has a positive derivative to the left and a negative derivative to the right?", "A local maximum",
      ["A local minimum", "Definitely not an extremum", "A discontinuity"],
      "The function first increases and then decreases, so the point is a local maximum."),
])

T("der.max", C5, "5.3", "Absolute Extrema on a Closed Interval", "procedural",
  "A continuous function on a closed interval attains its maximum and minimum at a local extremum or an endpoint. Compare the function values at these points.",
  ["List the local extrema and endpoints", "Compare function values to find the maximum or minimum"],
  "FUN.24", "inferred", NOTE)
Qs("der.max", [
    n("What is the maximum of f(x)=x²−2x on [0, 3]?", "max(0*0-2*0, 1*1-2*1, 3*3-2*3)",
      "f'(x)=2x−2, with a critical point at x=1. f(0)=0, f(1)=−1, and f(3)=3, so the maximum is 3."),
    n("What is the minimum of f(x)=x²−2x on [0, 3]?", "min(0, 1-2, 9-6)",
      "The candidate values are 0, −1, and 3, so the minimum is −1."),
    n("For f(x)=−x²+4 on [−1, 1], what is the function value at the endpoint x=1?", "-(1*1)+4",
      "−1+4=3. The vertex at x=0 has the larger value 4."),
    c("When finding extrema on a closed interval, what must be checked in addition to points where the derivative is 0?", "The two endpoints of the interval",
      ["Only the origin", "Only points where the derivative is 1", "Nothing else"],
      "An extremum may occur at an endpoint, so do not check only critical points."),
])

T("der.opt", C5, "5.3", "Optimization with Derivatives", "application",
  "Express area, profit, or another quantity as a function, then use derivatives to find its maximum or minimum on the domain.",
  ["Express practical constraints as a function and its domain", "Use derivatives to find an optimal value"],
  "FUN.25")
Qs("der.opt", [
    n("A rectangle has perimeter 20. Its area is greatest when its sides are equal. What is the maximum area?", "(20//4)**2",
      "The square has side length 5 and area 25."),
    n("A rectangle has perimeter 20, with sides x and 10−x. Its area is S=x(10−x). What is x when S'(x)=0?", "5",
      "S=10x−x², so S'=10−2x=0 and x=5."),
    n("A rectangle is built against a wall using 24 meters of fencing for its other three sides. The sides perpendicular to the wall have length x, and the side parallel to it has length 24−2x. What is x when the area is greatest?", "6",
      "S=x(24−2x)=24x−2x², so S'=24−4x=0 and x=6."),
    c("What is the final step when using derivatives for optimization?", "Compare function values at critical points and domain endpoints",
      ["Set the derivative equal to 1 only", "Check only the length of the domain", "Replace the function with its derivative and stop"],
      "The optimum must be within the allowed range, and a critical point must be checked to determine whether it is a maximum or minimum."),
])

T("der.poly", C5, "5.3", "Polynomial Functions of Degree at Most 3", "procedural",
  "The curriculum standard requires using derivatives to study polynomials of degree at most 3. The derivative of a cubic polynomial is quadratic.",
  ["Differentiate a cubic polynomial", "Find points where the derivative is 0"],
  "FUN.24", "inferred", "The curriculum standard limits the study of monotonicity and extrema to polynomials of degree at most 3. Pending verification.")
Qs("der.poly", [
    n("f(x)=x³−3x+1. What is f'(0)?", "0-3",
      "f'(x)=3x²−3, which equals −3 at x=0."),
    n("For f(x)=x³−3x, what is the positive value of x when f'(x)=0?", "1",
      "3x²−3=0 gives x²=1, so the positive root is 1."),
    n("f(x)=2x³. What is f'(1)?", "6*1*1",
      "(2x³)'=6x², which equals 6 at x=1."),
    c("What is the degree of the derivative of a cubic polynomial?", "Quadratic",
      ["Cubic", "Linear", "Constant"],
      "Differentiation reduces the degree by 1, so a cubic becomes a quadratic."),
])
