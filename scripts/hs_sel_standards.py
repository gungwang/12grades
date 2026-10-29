"""Senior high school selective compulsory curriculum standards (public paraphrases, not checked page by page).

Source: Selective Compulsory Courses in the Senior High School Mathematics Curriculum Standards (2017 Edition, Revised 2025).
Issuance notice: http://www.moe.gov.cn/srcsite/A26/s8001/202006/t20200603_462199.html
Reference PDF (not checked page by page): https://www.pep.com.cn/xw/zt/rjwy/gzkb2020/202205/P020220517519489596282.pdf

Numbering continues as cms-2017:H.<module>.NN after the compulsory-course entries; these are not the Ministry of Education's original numbers.
Functions continue from FUN.18, Geometry and Algebra from GA.13, Probability and Statistics from PS.09, and Modeling and Inquiry from MI.03.
Definite integrals are not listed among the optional compulsory content requirements and are not given a separate entry.
"""
from hs_sel_common import standard

NA = "Number and Algebra"
GG = "Shapes and Geometry"
SP = "Statistics and Probability"
IP = "Integrated Practice"

FUN = "Functions"
GA = "Geometry and Algebra"
PS = "Probability and Statistics"
MI = "Mathematical Modeling and Inquiry Activities"

standard("FUN.18", NA, FUN, "Sequences", "Paraphrase",
         "Understand the concept and representations of sequences, including that a sequence is a function defined on the positive integers. (Public paraphrase; verification pending.)")
standard("FUN.19", NA, FUN, "Sequences", "Paraphrase",
         "Understand arithmetic sequences; know their nth-term and first-n-terms sum formulas; understand their relationship to linear functions; and solve simple problems. (Public paraphrase; verification pending.)")
standard("FUN.20", NA, FUN, "Sequences", "Paraphrase",
         "Understand geometric sequences; know their nth-term and first-n-terms sum formulas; understand their relationship to exponential functions; and solve simple problems. (Public paraphrase; verification pending.)")
standard("FUN.21", NA, FUN, "Sequences", "Paraphrase",
         "Understand the principle of mathematical induction and use it to prove simple statements. This section is marked with an asterisk in the textbook contents; whether it is optional remains to be verified. (Public paraphrase; verification pending.)")
standard("FUN.22", NA, FUN, "Derivatives of Functions of One Variable and Their Applications", "Paraphrase",
         "Move from average rate of change to instantaneous rate of change; understand the concept of a derivative and the idea of limits; recognize that the derivative is a function of the independent variable; and understand its geometric meaning. (Public paraphrase; verification pending.)")
standard("FUN.23", NA, FUN, "Derivatives of Functions of One Variable and Their Applications", "Paraphrase",
         "Use the definition to find derivatives of basic functions such as constant and power functions; use basic derivative rules and the four arithmetic operations to differentiate simple functions; and differentiate simple composite functions of the form f(ax+b). (Public paraphrase; verification pending.)")
standard("FUN.24", NA, FUN, "Derivatives of Functions of One Variable and Their Applications", "Paraphrase",
         "Understand the relationship between derivatives and monotonicity, and find monotonic intervals for polynomials of degree at most three. Understand the necessary and sufficient conditions for extrema, and find extrema and absolute extrema on closed intervals for polynomials of degree at most three. (Public paraphrase; verification pending.)")
standard("FUN.25", NA, FUN, "Derivatives of Functions of One Variable and Their Applications", "Paraphrase",
         "Use derivatives to solve simple real-world optimization problems, such as maximizing profit or minimizing material use. (Public paraphrase; verification pending.)")

standard("GA.13", GG, GA, "Spatial Vectors and Solid Geometry", "Paraphrase",
         "Understand spatial vectors and know their linear operations, dot products, and coordinate representations. (Public paraphrase; verification pending.)")
standard("GA.14", GG, GA, "Spatial Vectors and Solid Geometry", "Paraphrase",
         "Understand the fundamental theorem of spatial vectors; know the spatial Cartesian coordinate system and the orthogonal decomposition and coordinate representation of spatial vectors; and use coordinates to find the distance between two points in space. (Public paraphrase; verification pending.)")
standard("GA.15", GG, GA, "Spatial Vectors and Solid Geometry", "Paraphrase",
         "Describe lines and planes using direction and normal vectors; use vectors to determine parallelism and perpendicularity; and solve simple measurement problems involving spatial angles and the distance from a point to a plane. (Public paraphrase; verification pending.)")
standard("GA.16", GG, GA, "Coordinate Geometry in the Plane", "Paraphrase",
         "Understand the angle of inclination and slope of a line, know the two-point slope formula, and use slopes to determine whether two lines are parallel or perpendicular. (Public paraphrase; verification pending.)")
standard("GA.17", GG, GA, "Coordinate Geometry in the Plane", "Paraphrase",
         "Know the point-slope, two-point, and general forms of a line equation. (Public paraphrase; verification pending.)")
standard("GA.18", GG, GA, "Coordinate Geometry in the Plane", "Paraphrase",
         "Find the intersection of two lines by solving a system of equations; know the distance between two points and the distance from a point to a line; and find the distance between two parallel lines. (Public paraphrase; verification pending.)")
standard("GA.19", GG, GA, "Coordinate Geometry in the Plane", "Paraphrase",
         "Know the standard and general equations of a circle, and determine a circle's equation from geometric conditions. (Public paraphrase; verification pending.)")
standard("GA.20", GG, GA, "Coordinate Geometry in the Plane", "Paraphrase",
         "Use the equations of lines and circles to determine the relative positions of a line and a circle or two circles, and solve simple problems. (Public paraphrase; verification pending.)")
standard("GA.21", GG, GA, "Coordinate Geometry in the Plane", "Paraphrase",
         "Know the definition, standard equation, and basic geometric properties of an ellipse, and understand simple applications of ellipses. (Public paraphrase; verification pending.)")
standard("GA.22", GG, GA, "Coordinate Geometry in the Plane", "Paraphrase",
         "Understand the definition, standard equation, asymptotes, and basic geometric properties of a hyperbola. (Public paraphrase; verification pending.)")
standard("GA.23", GG, GA, "Coordinate Geometry in the Plane", "Paraphrase",
         "Understand the definition, standard equation, and basic geometric properties of a parabola, and understand simple applications of parabolas. (Public paraphrase; verification pending.)")

standard("PS.09", SP, PS, "Counting Principles", "Paraphrase",
         "Use examples to understand the addition principle for counting by cases and the multiplication principle for counting in stages, and use them to solve simple counting problems. (Public paraphrase; verification pending.)")
standard("PS.10", SP, PS, "Counting Principles", "Paraphrase",
         "Understand permutations and combinations; derive the formulas for the numbers of permutations and combinations using counting principles; and solve simple problems. (Public paraphrase; verification pending.)")
standard("PS.11", SP, PS, "Counting Principles", "Paraphrase",
         "Explain the binomial theorem using counting principles, and use it to solve simple problems involving binomial expansions. (Public paraphrase; verification pending.)")
standard("PS.12", SP, PS, "Probability", "Paraphrase",
         "Use classical probability to understand conditional probability; use the multiplication rule and law of total probability; understand Bayes' theorem; and understand the relationship between conditional probability and independence. (Public paraphrase; verification pending.)")
standard("PS.13", SP, PS, "Probability", "Paraphrase",
         "Understand discrete random variables, their probability distributions, and the properties of those distributions. (Public paraphrase; verification pending.)")
standard("PS.14", SP, PS, "Probability", "Paraphrase",
         "Understand the expected value and variance of a discrete random variable, and calculate these statistics for simple probability distributions. (Public paraphrase; verification pending.)")
standard("PS.15", SP, PS, "Probability", "Paraphrase",
         "Understand Bernoulli trials; know the binomial distribution and its numerical characteristics; understand the hypergeometric distribution and its mean; and solve simple real-world problems. (Public paraphrase; verification pending.)")
standard("PS.16", SP, PS, "Probability", "Paraphrase",
         "Use frequency histograms to understand the characteristics of the normal distribution, including the meaning of its mean and variance. (Public paraphrase; verification pending.)")
standard("PS.17", SP, PS, "Statistics", "Paraphrase",
         "Use examples to understand the statistical meaning of the sample correlation coefficient, and compare the strengths of correlation in several pairs of data sets. (Public paraphrase; verification pending.)")
standard("PS.18", SP, PS, "Statistics", "Paraphrase",
         "Understand the simple linear regression model and the principle of least squares; calculate least-squares parameter estimates; and use a regression line to make simple predictions. (Public paraphrase; verification pending.)")
standard("PS.19", SP, PS, "Statistics", "Paraphrase",
         "Understand 2×2 contingency tables and the idea of tests for independence, and carry out simple tests for independence. (Public paraphrase; verification pending.)")

standard("MI.03", IP, MI, "Mathematical Modeling Activities", "Paraphrase",
         "Experience the process of making predictions with a statistical model: pose a question, organize paired data, build a regression model, and evaluate its predictions. (Public paraphrase; verification pending.)")
standard("MI.04", IP, MI, "Mathematical Inquiry Activities", "Paraphrase",
         "Experience mathematical inquiry by using binomial coefficients to investigate simple properties of Pascal's triangle and state conclusions. (Public paraphrase; verification pending.)")
