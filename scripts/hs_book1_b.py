"""Continuation of required-course Book 1: the last two sections of Chapter 2, Chapters 3 and 4, and mathematical modeling. Imported by hs_book1.py."""
from hs_common import questions, topic

NA = "Number and Algebra"
IP = "Integrated Practice"
C2 = "Chapter 2: Quadratic Functions, Equations, and Inequalities"
C3 = "Chapter 3: Function Concepts and Properties"
C4 = "Chapter 4: Exponential and Logarithmic Functions"


def T(key, chapter, section, name, domain, typ, desc, crit, std, conf="exact", note=None):
    topic(key, 1, chapter, section, name, domain, typ, desc, crit, std, conf, note)


def Qs(key, items):
    questions(key, items)


def n(prompt, verify, expl):
    return ("n", prompt, verify, expl)


def c(prompt, ok, bad, expl):
    return ("c", prompt, ok, bad, expl)


T("ine.param", C2, "2.3", "Parameterized Quadratic Inequalities", NA, "reasoning",
  "Use the opening direction and graph of a quadratic function to discuss simple parameter conditions for an inequality to hold for all values or have a solution.",
  ["Can translate an always-true condition into a condition on an extremum", "Can write the required inequality for the parameter"],
  "PRE.09", "inferred", "Parameterized cases extend one-variable quadratic inequalities; the curriculum specifies only simple cases. Verification pending.")
Qs("ine.param", [
    n("For every real x, x²+1≥k. What is the greatest possible value of k?", "1",
      "The minimum of x²+1 is 1. k cannot exceed this minimum, so its greatest value is 1."),
    n("The inequality x²−2x+m>0 holds for every real x. Its discriminant must be less than 0. What is the discriminant when m=2?", "(-2)**2-4*1*2",
      "The discriminant is 4−8=−4, which is less than 0. The parabola opens upward, so the expression is indeed always positive."),
    n("The minimum of y=x²+2x+k is k−1. If the minimum is 3, what is k?", "3+1",
      "Completing the square gives (x+1)²+k−1. Thus k−1=3, so k=4."),
    c("For an upward-opening quadratic to lie entirely above the x-axis, its discriminant must be?", "less than 0",
      ["equal to 0", "greater than 0", "any real number"],
      "It must have no x-intercepts, so the discriminant is less than 0. If it equals 0, the graph touches the x-axis."),
])

T("ine.app", C2, "2.3", "Practical Applications of Inequalities", NA, "application",
  "Represent practical constraints such as profit or area with simple inequalities and find the number of positive-integer solutions.",
  ["Can write an inequality that matches the problem", "Can select integer solutions within the practical range"],
  "PRE.09", "inferred", "Practical problems are simple applications of inequalities. Verification pending.")
Qs("ine.app", [
    n("The profit is 3 yuan per item, and fixed costs have been recovered. If 3x>21 is required to earn more than 21 yuan, what is the smallest positive integer x?", "8",
      "3x>21, so x>7. The smallest positive integer is 8."),
    n("A rectangle's length is 2 more than its width x. Its area is less than 15, and x is a positive integer. What is the area when x=2?", "2*(2+2)",
      "The width is 2 and the length is 4, so the area is 8, which is less than 15. This question asks for the area at this specific value."),
    n("An item's price is at least 12 yuan and at most 20 yuan. How many integer prices are possible?", "20-12+1",
      "There are 9 integers from 12 to 20 inclusive."),
    c("When solving a practical problem with inequalities, what must also be done with the solutions?", "check that they make sense in context",
      ["always keep negative values", "keep only equation roots", "ignore the units"],
      "Lengths, item counts, and other quantities have practical constraints; discard solutions that do not make sense."),
])

T("fn.def", C3, "3.1", "Function Concepts", NA, "conceptual",
  "Understand a function as a mapping between sets: each x in the domain corresponds to exactly one y.",
  ["Can determine whether a mapping is a function", "Can identify its domain, correspondence, and range"],
  "FUN.01")
Qs("fn.def", [
    c("Which mapping from the real numbers to the real numbers is a function?", "each x maps to x+1",
      ["each positive number maps to its two square roots", "y²=x", "each x may map to any number greater than or equal to it"],
      "A function assigns exactly one y to each x. Two square roots, y²=x, and “any number” are not unique."),
    n("If f(x)=2x+1, find f(3).", "2*3+1",
      "Substitute x=3: 2×3+1=7."),
    n("If g(x)=x², find g(−2).", "(-2)**2",
      "Squaring gives 4, regardless of the sign of −2."),
    c("Do f(x)=x and g(t)=t represent the same function?", "yes, they have the same correspondence and both have the real numbers as their domain",
      ["no, the letters differ", "no, one is named f and the other g", "they are the same only if their ranges match"],
      "A function is determined by its domain and correspondence; the letter used for the input does not matter."),
])

T("fn.dom", C3, "3.1", "Function Domains", NA, "procedural",
  "Find the domains of simple functions involving fractions and even roots, and check integer inputs.",
  ["Can state the conditions that make an expression defined", "Can determine whether a given value is in the domain"],
  "FUN.02")
Qs("fn.dom", [
    n("For f(x)=1/(x−2), how many of 1, 2, and 3 are in the domain?", "len([1,3])",
      "The denominator cannot be 0, so x=2 is excluded. Both 1 and 3 are allowed, for a total of 2."),
    n("How many integers from 1 through 5 are in the domain of f(x)=√(x−1)?", "len([1,2,3,4,5])",
      "The radicand must be greater than or equal to 0, so x≥1. All 5 integers from 1 to 5 are allowed."),
    c("What is the domain of f(x)=1/x?", "all nonzero real numbers", ["all real numbers", "all positive numbers", "only 1"],
      "The denominator cannot be 0; all other real numbers are allowed."),
    n("For f(x)=√(4−x)+1/(x−1), is x=0 in the domain? Answer 1 if it is and 0 if it is not.", "1",
      "4−0≥0 and 0≠1, so both conditions are satisfied."),
])

T("fn.ran", C3, "3.1", "Function Ranges", NA, "procedural",
  "Find the range and extrema of simple functions from their formulas or finite domains.",
  ["Can calculate all function values on a finite domain", "Can state the extrema of a quadratic function on a specified interval"],
  "FUN.02", "inferred", "Range and domain are included in the same function-representation requirement. Verification pending.")
Qs("fn.ran", [
    n("For f(x)=x+1 with x∈{0,1,2}, what is the maximum function value?", "2+1",
      "The three values are 1, 2, and 3; the maximum is 3."),
    n("What is the maximum of f(x)=−x²?", "0",
      "The squared term is nonnegative, so its negative has a maximum of 0, attained at x=0."),
    n("For f(x)=x² with x∈{−1,2}, what is the sum of the two function values?", "(-1)**2+2**2",
      "1+4=5."),
    c("What is the range of y=2^x for real x?", "all positive real numbers",
      ["all real numbers", "all nonnegative real numbers", "all real numbers greater than or equal to 1"],
      "The exponential function is always positive. It can approach 0 without reaching it and can grow without bound."),
])

T("fn.rep", C3, "3.1", "Representations of Functions", NA, "conceptual",
  "Know that functions can be represented by formulas, graphs, or tables, and read values from tables and graphs.",
  ["Can name three ways to represent a function", "Can read a function value from a graph or table"],
  "FUN.02", "inferred", "The three representations are part of the function concept. Verification pending.")
Qs("fn.rep", [
    n("A table gives y=4 when x=1 and y=7 when x=2. What is the difference y(2)−y(1)?", "7-4",
      "Read the values directly from the table: 7−4=3."),
    n("A function is given by the table f(1)=2, f(2)=5, and f(4)=11. Find f(1)+f(4).", "2+11",
      "Read the values from the table: f(1)=2 and f(4)=11, for a sum of 13."),
    n("A graph passes through (2,5). What is the function value when x=2?", "5",
      "The point's y-coordinate is the corresponding function value."),
    c("Can a table of only four input-output pairs determine a unique function on all real numbers?", "no",
      ["yes, a written table is always unique", "yes, if the points lie on a line", "only a curve cannot be uniquely determined"],
      "The table gives only the listed pairs. Without specifying the domain and all correspondences, it cannot uniquely determine the entire function."),
])

T("fn.piece", C3, "3.1", "Piecewise Functions", NA, "procedural",
  "Evaluate a piecewise function using the formula for the interval containing the input, and solve simple piecewise pricing problems.",
  ["Can determine which interval contains the input", "Can evaluate the formula on each interval"],
  "FUN.02", "inferred", "A piecewise function is one specific form of function representation. Verification pending.")
Qs("fn.piece", [
    n("For x<0, f(x)=x+1; for x≥0, f(x)=2x. Find f(−2).", "-2+1",
      "Since −2<0, use the first formula: −2+1=−1."),
    n("For x<0, f(x)=x+1; for x≥0, f(x)=2x. Find f(3).", "2*3",
      "Since 3≥0, use the second formula, f(x)=2x: 2×3=6."),
    n("A taxi fare is 10 yuan for up to 3 km, plus 2 yuan per additional kilometer. What is the fare for 5 km?", "10+2*(5-3)",
      "The trip is 2 km over the limit: 10+4=14 yuan."),
    c("What should be checked at a boundary point of a piecewise function?", "which formula applies there and whether the function value is unique",
      ["the boundary point may have two values", "the boundary point must be undefined", "the two formulas must be identical"],
      "A boundary point must belong to one piece, and it must have exactly one function value."),
])

T("fn.mono", C3, "3.2", "Function Monotonicity", NA, "conceptual",
  "Use graphs and definitions to determine where linear and quadratic functions increase or decrease on specified intervals.",
  ["Can explain increasing and decreasing functions", "Can determine the monotonicity of y=kx+b"],
  "FUN.03")
Qs("fn.mono", [
    c("On the real numbers, f(x)=2x+1 is?", "increasing", ["decreasing", "increasing then decreasing", "not monotonic"],
      "Its slope is positive, so y increases as x increases."),
    c("On the real numbers, f(x)=−3x+1 is?", "decreasing", ["increasing", "decreasing then increasing", "constant"],
      "Its slope is negative, so y decreases as x increases."),
    n("For f(x)=2x+1, what is f(4)−f(1)?", "(2*4+1)-(2*1+1)",
      "9−3=6, a positive difference consistent with an increasing function."),
    c("On [0,+∞), y=x² is?", "increasing", ["decreasing", "increasing then decreasing", "not monotonic"],
      "The vertex is at the origin; to its right, the square increases as x increases."),
])

T("fn.monoproof", C3, "3.2", "Proving Monotonicity from the Definition", NA, "reasoning",
  "Choose arbitrary x1<x2 in an interval and compare f(x1) and f(x2) using their difference.",
  ["Can form and factor the difference correctly", "Can infer increasing or decreasing behavior from the sign of the difference"],
  "FUN.03", "inferred", "Proof from the definition is a fundamental method for establishing monotonicity. Verification pending.")
Qs("fn.monoproof", [
    n("For f(x)=3x−1, let x1=1 and x2=4. Find f(x2)−f(x1).", "(3*4-1)-(3*1-1)",
      "11−2=9, a positive difference; these points are consistent with an increasing function."),
    n("For f(x)=−x, if x2−x1=2, what is f(x2)−f(x1)?", "-2",
      "f(x2)−f(x1)=−(x2−x1)=−2. The difference is negative, indicating a decreasing function."),
    n("To prove f(x)=x+1 is increasing, use f(x2)−f(x1)=x2−x1. If x2−x1=5, what is the difference?", "5",
      "The difference is x2−x1, which is positive, so the function is increasing."),
    c("To show from the definition that f is increasing on an interval, what must be proved for x1<x2?", "f(x1)<f(x2)",
      ["f(x1)>f(x2)", "f(x1)=f(x2)", "it is enough to check integers"],
      "The inequality f(x1)<f(x2) must hold for every x1<x2 in the interval; checking only a few points is not enough."),
])

T("fn.max", C3, "3.2", "Maximum and Minimum Values", NA, "procedural",
  "Find the maximum and minimum of a quadratic function on a closed interval.",
  ["Can compare function values at endpoints and the vertex", "Can identify where an extremum is attained"],
  "FUN.03", "inferred", "Extrema and monotonicity are both basic properties of functions. Verification pending.")
Qs("fn.max", [
    n("For f(x)=x² on [−1,2], what is the maximum value?", "2**2",
      "The endpoint values at −1 and 2 are 1 and 4; the vertex value at 0 is 0. The maximum is 4."),
    n("For f(x)=x² on [−1,2], what is the minimum value?", "min([(-1)**2, 0**2, 2**2])",
      "The vertex x=0 lies in [−1,2], and f(0)=0. The endpoint values are 1 and 4, so the minimum is 0."),
    n("What is the maximum value of f(x)=−(x−1)²+5?", "5",
      "The squared term has a negative coefficient, so the maximum is 5, attained at x=1."),
    c("Where can a continuous function on a closed interval attain its extrema?", "at an endpoint or at a vertex or extremum inside the interval",
      ["only at endpoints", "only at the midpoint", "always outside the interval"],
      "For a quadratic, check whether its vertex lies in the interval and compare its value with the endpoint values."),
])

T("fn.parity", C3, "3.2", "Even and Odd Functions", NA, "conceptual",
  "Know that odd functions satisfy f(−x)=−f(x), even functions satisfy f(−x)=f(x), and the domain must be symmetric about the origin.",
  ["Can determine parity from the definition", "Know that a domain not symmetric about the origin rules out both evenness and oddness"],
  "FUN.04")
Qs("fn.parity", [
    c("What kind of function is f(x)=x²?", "even", ["odd", "both odd and even", "neither odd nor even"],
      "f(−x)=(−x)²=x²=f(x), and the domain is symmetric about the origin, so the function is even."),
    c("What kind of function is f(x)=x³?", "odd", ["even", "both odd and even", "neither odd nor even"],
      "f(−x)=−x³=−f(x), so the function is odd."),
    n("For f(x)=x², find f(2)+f(−2).", "2**2+(-2)**2",
      "An even function has equal values at opposite inputs: 4+4=8."),
    n("For f(x)=x³, find f(2)+f(−2).", "2**3+(-2)**3",
      "8+(−8)=0, a property of odd functions."),
])

T("fn.parityj", C3, "3.2", "Parity and Graph Symmetry", NA, "reasoning",
  "Know that even-function graphs are symmetric about the y-axis and odd-function graphs are symmetric about the origin, and use this to find values at symmetric points.",
  ["Can find a function value using symmetry", "Can identify a function that is both odd and even"],
  "FUN.04", "inferred", "Graph symmetry is the geometric meaning of parity. Verification pending.")
Qs("fn.parityj", [
    n("An even function has f(2)=7. What is f(−2)?", "7",
      "An even function is symmetric about the y-axis, so opposite inputs have equal values."),
    n("An odd function has f(2)=7. What is f(−2)?", "-7",
      "An odd function is symmetric about the origin, so f(−2)=−f(2)=−7."),
    n("A function is both odd and even, and f(3)=0. What must f(0) be?", "0",
      "If an odd function is defined at 0, f(0)=0. A function that is both odd and even must be identically 0."),
    c("What is the parity of f(x)=x²+x?", "neither odd nor even", ["odd", "even", "both odd and even"],
      "f(−x)=x²−x, which is neither f(x) nor −f(x)."),
])

T("fn.power", C3, "3.3", "Power Functions", NA, "conceptual",
  "Distinguish whether five basic power functions increase or decrease in the first quadrant and evaluate them at integer inputs.",
  ["Can identify which of y=x, y=x², y=x³, y=√x, and y=1/x are increasing", "Can evaluate these functions at positive integers"],
  "FUN.05")
Qs("fn.power", [
    n("For the power function y=x³, find the value when x=2.", "2**3",
      "The cube of 2 is 8."),
    n("For the power function y=1/x, find the value when x=4.", "Fraction(1,4)",
      "The reciprocal is 1/4."),
    c("Which power function is decreasing on (0,+∞)?", "y=1/x",
      ["y=x", "y=x²", "y=x³"],
      "On the positive real numbers, y=1/x decreases as x increases; the other three increase."),
    n("For y=√x, what is the value when x=9?", "isqrt(9)",
      "The principal square root of 9 is 3."),
])

T("fn.app1", C3, "3.3", "Describing Simple Relationships with Functions", NA, "application",
  "Represent simple relationships involving unit price or distance with functions and evaluate them.",
  ["Can identify the input variable and function value", "Can answer a specific question using a formula"],
  "FUN.11", "inferred", "This chapter first applies linear and quadratic relationships to simple cases; broader model selection is covered in function applications. Verification pending.")
Qs("fn.app1", [
    n("A notebook costs 4 yuan, so the cost of x notebooks is f(x)=4x. How much do 6 notebooks cost?", "4*6",
      "4×6=24 yuan."),
    n("A square has side length x and area s=x². What is its area when the side length is 5?", "5**2",
      "Area is the side length squared, so it is 25."),
    n("Distance is given by s=60t, where t is in hours. How many kilometers are traveled in 2 hours?", "60*2",
      "At 60 kilometers per hour, 2 hours covers 120 kilometers."),
    c("When representing a practical problem with a function, what should be identified first?", "the practical range of the input variable",
      ["use a letter and ignore its range", "allow a function value to correspond to any number of inputs", "the function must be quadratic"],
      "Counts, side lengths, and other real quantities cannot take arbitrary real values; the domain must fit the situation."),
])

T("exp.frac", C4, "4.1", "Rational Exponents", NA, "procedural",
  "Rewrite radicals as fractional powers and evaluate rational powers with exact results.",
  ["Can evaluate integer and simple fractional powers", "Can state that a negative exponent represents a reciprocal"],
  "FUN.06")
Qs("exp.frac", [
    n("Evaluate 2 to the power −3.", "Fraction(1, 2**3)",
      "A negative exponent represents a reciprocal: 2⁻³=1/8."),
    n("Evaluate 8^(2/3). The result is an integer.", "4",
      "8=2³, so (2³)^(2/3)=2²=4."),
    n("Evaluate 16^(1/2).", "isqrt(16)",
      "The principal square root of 16 is 4."),
    c("For a≥0, what is a^(1/2)?", "√a", ["a²", "1/a", "2a"],
      "The fractional exponent 1/2 represents the principal square root."),
])

T("exp.ops", C4, "4.1", "Exponent Rules", NA, "procedural",
  "Use product, quotient, and power-of-a-power rules to evaluate integer powers.",
  ["Can express a product of powers with the same base by adding exponents", "Can evaluate a power raised to a power"],
  "FUN.06", "inferred", "Exponent rules and the meaning of powers are combined in one curriculum clause. Verification pending.")
Qs("exp.ops", [
    n("Evaluate 2³×2⁴.", "2**3*2**4",
      "Add the exponents: 2⁷=128."),
    n("Evaluate 3⁵÷3².", "3**(5-2)",
      "Subtract the exponents: 3³=27."),
    n("Evaluate (2³)².", "(2**3)**2",
      "For a power raised to a power, multiply the exponents: 2⁶=64."),
    c("When multiplying powers with the same base, what should be done to the exponents?", "add them", ["multiply them", "subtract them and take the reciprocal", "leave them unchanged"],
      "a^m·a^n=a^(m+n). Multiplying exponents is the rule for a power raised to a power."),
])

T("exp.fn", C4, "4.2", "Exponential Function Concepts", NA, "conceptual",
  "Know that y=a^x, where a>0 and a≠1, is an exponential function, and evaluate it at specific inputs.",
  ["Can determine whether a formula is an exponential function", "Can evaluate an exponential function with a specific positive base"],
  "FUN.07")
Qs("exp.fn", [
    n("If f(x)=2^x, find f(5).", "2**5",
      "2⁵=32."),
    n("If f(x)=3^x, find f(0).", "3**0",
      "Any nonzero number raised to the power 0 is 1."),
    n("If f(x)=(1/2)^x, find f(3).", "Fraction(1,2)**3",
      "(1/2)³=1/8."),
    c("Which of the following is an exponential function?", "y=2^x", ["y=x²", "y=2·x", "y=2^x+1"],
      "An exponential function has a constant base, the variable as the exponent, and no additional coefficient or constant term. y=2^x+1 is a translation of an exponential function."),
])

T("exp.prop", C4, "4.2", "Properties of Exponential Functions", NA, "reasoning",
  "Determine monotonicity and compare values based on whether the base is greater than 1 or between 0 and 1.",
  ["Can determine how the base affects monotonicity", "Can compare two powers with the same base"],
  "FUN.07", "inferred", "Monotonicity and graph-based comparison are properties introduced after the exponential-function concept. Verification pending.")
Qs("exp.prop", [
    c("On the real numbers, y=2^x is?", "increasing", ["decreasing", "increasing then decreasing", "not monotonic"],
      "The base 2 is greater than 1, so the exponential function is increasing."),
    c("On the real numbers, y=(1/2)^x is?", "decreasing", ["increasing", "decreasing then increasing", "constant"],
      "The base is between 0 and 1, so the exponential function is decreasing."),
    n("Compare 2⁵ and 2³ by calculating 2⁵−2³.", "2**5-2**3",
      "32−8=24, a positive difference, so 2⁵ is greater, consistent with the increasing function."),
    n("If 2^x=8, what is x?", "3",
      "8=2³, so x=3."),
])

T("log.def", C4, "4.3", "Logarithm Concepts", NA, "procedural",
  "Understand that log_a N is the exponent to which a must be raised to obtain N, and evaluate simple logarithms.",
  ["Can rewrite a logarithmic expression in exponential form", "Can evaluate simple logarithms with base 2 or 10"],
  "FUN.08")
Qs("log.def", [
    n("Evaluate log₂32.", "log2(32)",
      "2⁵=32, so the logarithm is 5."),
    n("Evaluate lg1000, the common logarithm log₁₀1000.", "log10(1000)",
      "10³=1000, so the value is 3."),
    n("Evaluate log₂(1/8).", "log2(1/8)",
      "2⁻³=1/8, so the logarithm is −3."),
    c("What does log₂8=3 mean?", "2³=8", ["8³=2", "2×3=8", "3²=8"],
      "A logarithm gives the exponent: the base raised to that exponent equals the argument."),
])

T("log.ops", C4, "4.3", "Logarithm Rules", NA, "procedural",
  "Use the addition, subtraction, and scalar-multiplication rules for logarithms.",
  ["Can express the logarithm of a product as a sum of logarithms", "Can evaluate simple logarithmic expressions"],
  "FUN.08", "inferred", "Logarithm rules and the concept of logarithms are combined in one curriculum clause. Verification pending.")
Qs("log.ops", [
    n("Evaluate log₂8+log₂4.", "log2(8)+log2(4)",
      "3+2=5, which can also be written as log₂32."),
    n("Evaluate log₂16−log₂2.", "log2(16)-log2(2)",
      "4−1=3, or log₂8."),
    n("Evaluate 2·log₂8.", "2*log2(8)",
      "2×3=6, which equals log₂(8²)=log₂64."),
    c("What is log_a(MN)?", "log_a M + log_a N",
      ["log_a M · log_a N", "log_a M − log_a N", "log_a(M+N)"],
      "The logarithm of a product is the sum of the logarithms. The logarithm of a quotient is the one involving subtraction."),
])

T("log.change", C4, "4.3", "Change-of-Base Formula", NA, "procedural",
  "Use the change-of-base formula to rewrite a logarithm with base 2 or 10.",
  ["Can state the change-of-base formula", "Can evaluate logarithms by changing to base 2"],
  "FUN.08", "inferred", "The change-of-base formula is a tool for working with logarithms. Verification pending.")
Qs("log.change", [
    n("Evaluate log₄16.", "log2(16)/log2(4)",
      "16=4². By change of base, log₂16 / log₂4 = 4/2 = 2."),
    n("Evaluate log₈2.", "log2(2)/log2(8)",
      "log₂2=1 and log₂8=3, so the result is 1/3."),
    n("Evaluate log₄(1/16).", "log2(1/16)/log2(4)",
      "1/16=4⁻², so the result is −2."),
    c("What is the change-of-base formula for log_a b?", "log_c b / log_c a",
      ["log_c a / log_c b", "log_c a · log_c b", "log_c(a·b)"],
      "The numerator is the logarithm of the argument using the new base; the denominator is the logarithm of the original base."),
])

T("log.fn", C4, "4.4", "Logarithmic Functions", NA, "conceptual",
  "Know that y=log_a x, where a>0 and a≠1, has the positive real numbers as its domain, and evaluate specific values.",
  ["Can state the domain of a logarithmic function", "Can evaluate simple logarithms"],
  "FUN.09")
Qs("log.fn", [
    n("If f(x)=log₂x, find f(16).", "log2(16)",
      "2⁴=16, so the function value is 4."),
    c("What is the domain of y=log₂x?", "all positive real numbers", ["all real numbers", "all nonnegative real numbers", "all real numbers greater than or equal to 1"],
      "The argument must be greater than 0; the base is the constant 2."),
    n("If log₂x=5, what is x?", "2**5",
      "x=2⁵=32."),
    c("Which point lies on the graph of y=log₂x?", "(1,0)", ["(0,1)", "(0,0)", "(2,0)"],
      "For any valid base, the logarithm of 1 is 0, so the graph passes through (1,0)."),
])

T("log.prop", C4, "4.4", "Properties of Logarithmic Functions", NA, "reasoning",
  "Determine monotonicity from the base and compare the values of two logarithms.",
  ["Can determine whether a logarithmic function with base greater than 1 is increasing or decreasing", "Can compare logarithms with the same base"],
  "FUN.09", "inferred", "Monotonicity is a property introduced after the concept of logarithmic functions. Verification pending.")
Qs("log.prop", [
    c("On (0,+∞), y=log₂x is?", "increasing", ["decreasing", "increasing then decreasing", "not monotonic"],
      "The base 2 is greater than 1, so the logarithmic function is increasing."),
    c("On its domain, y=log_(1/2) x is?", "decreasing", ["increasing", "decreasing then increasing", "constant"],
      "The base is between 0 and 1, so the logarithmic function is decreasing."),
    n("Compare log₂16 and log₂4 by finding their difference.", "log2(16)-log2(4)",
      "4−2=2, a positive difference, so the first value is greater."),
    n("If log₂x>3, an integer lower bound for x is the integer after 2³. What is 2³?", "2**3",
      "Since the function is increasing, log₂x>3 means x>8. The value 8 itself does not satisfy the strict inequality."),
])

T("log.inv", C4, "4.4", "Exponential and Logarithmic Functions as Inverses", NA, "reasoning",
  "Know that y=a^x and y=log_a x are inverse functions, and use this relationship to evaluate expressions.",
  ["Can state the corresponding inverse-function relationships", "Can evaluate log_a(a^k) and a^(log_a k)"],
  "FUN.09", "inferred", "The inverse relationship is part of the connection between logarithmic and exponential functions. Verification pending.")
Qs("log.inv", [
    n("Evaluate log₂(2⁵).", "log2(2**5)",
      "Logarithms and exponentials are inverse operations, so the result is 5."),
    n("Evaluate 2^(log₂16).", "2**log2(16)",
      "Taking the logarithm and then exponentiating returns the argument, 16."),
    n("If f(x)=2^x, what is f⁻¹(8)?", "log2(8)",
      "The inverse is log₂x, and log₂8=3."),
    c("About which line are the graphs of y=2^x and y=log₂x symmetric?", "y=x",
      ["the y-axis", "the x-axis", "y=−x"],
      "Graphs of inverse functions are symmetric about the line y=x."),
])

T("fn.zero", C4, "4.5", "Function Zeros", NA, "procedural",
  "Know that a function zero is a real root of f(x)=0 and the x-coordinate where the graph crosses the x-axis.",
  ["Can find zeros of simple functions", "Can use a sign change in function values to locate an interval containing a zero"],
  "FUN.10")
Qs("fn.zero", [
    n("What is the positive zero of f(x)=x²−4?", "max(roots2(1,0,-4))",
      "x²=4, so the zeros are −2 and 2; the positive one is 2."),
    n("What is the zero of f(x)=x−5?", "5",
      "x−5=0, so the zero is 5."),
    n("What is the sum of the zeros of f(x)=x²−5x+6?", "2+3",
      "The zeros are 2 and 3, with sum 5."),
    c("If f(1)=−3, f(3)=5, and f is continuous, then?", "there is at least one zero in (1,3)",
      ["there is no zero", "the only zero is 1", "the zero must be 3"],
      "The function values at the endpoints have opposite signs, so the continuous graph crosses the x-axis at least once."),
])

T("fn.bisect", C4, "4.5", "Bisection Method", NA, "procedural",
  "Use bisection to halve an interval containing a root and evaluate the function at the midpoint.",
  ["Can find the midpoint of an interval", "Can choose the next interval from the sign of the midpoint function value"],
  "FUN.10", "inferred", "Bisection is a method for finding approximate solutions and is covered with the existence of function zeros. Verification pending.")
Qs("fn.bisect", [
    n("What is the midpoint of the interval (1,3)?", "(1+3)/2",
      "The midpoint is (1+3)/2=2."),
    n("For f(x)=x²−4, evaluate f(2).", "2**2-4",
      "4−4=0, so 2 is a zero and no further bisection is needed."),
    n("Bisect the interval (0,4) once. If the root is in the left half, what is the new right endpoint?", "(0+4)/2",
      "The midpoint is 2, so the left half is (0,2) and its right endpoint is 2."),
    c("What does bisection do to an interval containing a root at each step?", "split it at the midpoint and keep the half whose endpoint function values have opposite signs",
      ["keep only the longer half", "randomly discard one endpoint", "keep both halves"],
      "The zero lies in the half where the midpoint function value has the opposite sign from an endpoint."),
])

T("fn.model", C4, "4.5", "Choosing a Function Model", NA, "application",
  "Distinguish linear, quadratic, and exponential models based on the rate of change, and evaluate a chosen model.",
  ["Can identify a change that suits an exponential model", "Can evaluate a given model"],
  "FUN.11")
Qs("fn.model", [
    n("A bacteria population doubles every hour and starts at 100. How many bacteria are there after 3 hours?", "100*2**3",
      "The exponential model gives 100×2³=800."),
    n("An object travels at a constant speed according to s=40t. How far does it travel in 3 hours?", "40*3",
      "This is a linear model: 40×3=120."),
    n("A square's area is the square of its side length. What is its area when the side length increases from 0 to 6?", "6**2",
      "The area model is s=x²; at x=6, the area is 36."),
    c("If a quantity is multiplied by the same constant greater than 1 after each equal time interval, which model is more suitable?", "an exponential function",
      ["a linear function", "an inverse-proportion function", "a constant function"],
      "Repeated multiplication gives exponential growth, not a fixed increase each time."),
])

T("fn.modelapp", C4, "4.5", "Fitting and Predicting with Function Models", NA, "application",
  "Use a given function model to make a prediction and know that predictions must be checked against reality.",
  ["Can substitute known data into a model", "Can explain that a prediction is not an exact fact"],
  "FUN.11", "inferred", "Prediction is one step in applying functions and remains part of choosing and using a model. Verification pending.")
Qs("fn.modelapp", [
    n("Using P=20+3t, what is the value when t=10?", "20+3*10",
      "20+30=50."),
    n("Using N=5·2^t, what is the value when t=4?", "5*2**4",
      "5×16=80."),
    n("Using y=100−8t, what is the value when t=5?", "100-8*5",
      "100−40=60."),
    c("After making a prediction with a function model, what should be done?", "test the model against new real-world data",
      ["treat the calculated value as an absolute fact", "change every data point that does not fit", "stop collecting data"],
      "A model is an approximation. Test predictions and revise the model if it does not fit."),
])

T("mod.proc", "Mathematical Modeling", "Building a Function Model", "The Modeling Process", IP, "modeling",
  "Know that mathematical modeling involves posing a question, collecting data, building a model, solving, and validating.",
  ["Can list the main modeling steps in order", "Can identify validation as part of modeling"],
  "MI.01")
Qs("mod.proc", [
    c("What is a reasonable order for mathematical modeling?", "pose a question, collect data, build a model, solve, and validate",
      ["write the conclusion before finding a question", "collect data without building a model", "stop if validation fails; the model cannot be changed"],
      "Modeling is an iterative process; the model can be revised after validation."),
    n("A modeling group has recorded 4 sets of data. If validation has not been done, how many steps—posing the question, collecting data, modeling, and solving—have been completed?", "4",
      "The four listed steps are complete, but validation is not, so the process is not finished."),
    c("After building a function model, the calculated results differ greatly from measurements. What should be done?", "revisit the assumptions or model, revise it, and validate again",
      ["change the measured data to fit the model", "declare the problem unsolvable", "ignore the difference"],
      "A large discrepancy suggests the model or assumptions are unsuitable; revise them rather than changing the data."),
    c("What is the main result of a mathematical modeling activity?", "a validated model and its scope of applicability",
      ["an expression with no units", "a table without explanation", "a theorem that must be exactly true"],
      "A model addresses a practical question and should state its assumptions and limits."),
])

T("mod.fun", "Mathematical Modeling", "Building a Function Model", "Solving Practical Problems with Function Models", IP, "modeling",
  "Choose a linear or exponential function to describe simple data and calculate a prediction.",
  ["Can choose a model based on whether the change adds a fixed amount or multiplies by a fixed factor", "Can use a model to find a value at a specified time"],
  "MI.01", "inferred", "This point covers function models in the required-course modeling activity and shares a curriculum clause with the modeling process. Verification pending.")
Qs("mod.fun", [
    n("The water level rises 3 cm each hour and starts at 20 cm. According to a linear model, what is the level after 4 hours?", "20+3*4",
      "The level increases by the same amount each time: y=20+3t. At t=4, it is 32 cm."),
    n("An algae population doubles each day and starts at 6 units. According to an exponential model, what is it after 3 days?", "6*2**3",
      "It is multiplied by 2 each day: 6×2^t. At t=3, it is 48 units."),
    n("The model y=20+3t matches the measured value at t=2. What is their shared value?", "20+3*2",
      "20+6=26. Agreement at this point shows only a fit here, not that future predictions will always be accurate."),
    c("If data increase by about the same amount each time, which model should be tried first?", "a linear function",
      ["an exponential function", "a logarithmic function", "a constant function"],
      "A fixed increment is linear change. A fixed multiplier suggests an exponential model."),
])
