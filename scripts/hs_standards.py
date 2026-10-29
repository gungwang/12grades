"""High-school required-course curriculum standards (public paraphrases, not checked page by page against the source).

Source: General High School Mathematics Curriculum Standards (2017 Edition, 2025 Revision), five required-course themes.
Issuance notice: http://www.moe.gov.cn/srcsite/A26/s8001/202006/t20200603_462199.html
Reference PDF (not checked page by page): https://www.pep.com.cn/xw/zt/rjwy/gzkb2020/202205/P020220517519489596282.pdf

IDs cms-2017:H.<module>.NN are organized by topic in this graph; they are not original Ministry of Education IDs.
Conditional probability, the trigonometric form of complex numbers, vectors in space, lines and circles,
conic sections, sequences, derivatives, counting principles, random variables, and measuring dihedral
angles are part of elective required courses or textbook enrichment and are not listed separately.
"""
from hs_common import standard

NA = "Number and Algebra"
GG = "Geometry and Measurement"
SP = "Statistics and Probability"
IP = "Integrated Practice"

PRE = "Prerequisite Knowledge"
FUN = "Functions"
GA = "Geometry and Algebra"
PS = "Probability and Statistics"
MI = "Mathematical Modeling and Inquiry Activities"

# Every text is paraphrased; the compiler sets verbatim=false and page_or_ref to "pending verification".
standard("PRE.01", NA, PRE, "Sets", "Paraphrase",
         "Understand what a set is; use notation to express element-set membership; choose roster or set-builder notation in context; and recognize common number sets and their notation. (Public paraphrase; verification pending.)")
standard("PRE.02", NA, PRE, "Sets", "Paraphrase",
         "Understand subsets, proper subsets, and set equality, and determine whether one set contains another. (Public paraphrase; verification pending.)")
standard("PRE.03", NA, PRE, "Sets", "Paraphrase",
         "Understand intersections, unions, and complements; find them for sets; and use them in specific problems. (Public paraphrase; verification pending.)")
standard("PRE.04", NA, PRE, "Common Logical Notation", "Paraphrase",
         "Understand sufficient, necessary, and necessary-and-sufficient conditions, and determine the implication relationship between two propositions. (Public paraphrase; verification pending.)")
standard("PRE.05", NA, PRE, "Common Logical Notation", "Paraphrase",
         "Understand universal and existential quantifiers, and write the negation of a proposition containing one quantifier. (Public paraphrase; verification pending.)")
standard("PRE.06", NA, PRE, "Equality and Inequality", "Paraphrase",
         "Review the properties of equations; understand the concept and properties of inequalities; know how to prove inequality properties; compare values with inequalities; and solve simple one-variable linear inequalities. (Public paraphrase; verification pending.)")
standard("PRE.07", NA, PRE, "Equality and Inequality", "Paraphrase",
         "Know the basic inequality, use it to solve simple optimization problems, and identify when equality holds. (Public paraphrase; verification pending.)")
standard("PRE.08", NA, PRE, "Quadratic Equations and Inequalities from a Function Perspective", "Paraphrase",
         "Relate the roots of a quadratic equation to the solution set of a quadratic inequality using the graph of a quadratic function. (Public paraphrase; verification pending.)")
standard("PRE.09", NA, PRE, "Quadratic Equations and Inequalities from a Function Perspective", "Paraphrase",
         "Solve quadratic inequalities with the help of quadratic functions, and handle simple parameterized inequalities and practical problems. (Public paraphrase; verification pending.)")

standard("FUN.01", NA, FUN, "Function Concepts and Properties", "Paraphrase",
         "Understand functions using set language and mappings, and determine whether two functions are the same. (Public paraphrase; verification pending.)")
standard("FUN.02", NA, FUN, "Function Concepts and Properties", "Paraphrase",
         "Find the domains and ranges of simple functions, understand the three ways to represent a function, and work with simple piecewise functions. (Public paraphrase; verification pending.)")
standard("FUN.03", NA, FUN, "Function Concepts and Properties", "Paraphrase",
         "Understand monotonicity and maximum or minimum values, and use the definition to determine or prove monotonicity for simple functions. (Public paraphrase; verification pending.)")
standard("FUN.04", NA, FUN, "Function Concepts and Properties", "Paraphrase",
         "Understand even and odd functions, identify these properties in simple functions, and know how parity affects the graph. (Public paraphrase; verification pending.)")
standard("FUN.05", NA, FUN, "Function Concepts and Properties", "Paraphrase",
         "Understand power functions and use their graphs to explore the behavior of y=x, y=x², y=x³, y=x^(1/2), and y=x^(-1). (Public paraphrase; verification pending.)")
standard("FUN.06", NA, FUN, "Exponential and Logarithmic Functions", "Paraphrase",
         "Understand rational exponents and the rules for operations with powers. (Public paraphrase; verification pending.)")
standard("FUN.07", NA, FUN, "Exponential and Logarithmic Functions", "Paraphrase",
         "Understand exponential functions, know their monotonicity, and compare values using their graphs. (Public paraphrase; verification pending.)")
standard("FUN.08", NA, FUN, "Exponential and Logarithmic Functions", "Paraphrase",
         "Understand logarithms and their operation rules, and use the change-of-base formula to rewrite a logarithm with a familiar base. (Public paraphrase; verification pending.)")
standard("FUN.09", NA, FUN, "Exponential and Logarithmic Functions", "Paraphrase",
         "Understand logarithmic functions and their monotonicity; know that exponential and logarithmic functions are inverses; and compare logarithmic values. (Public paraphrase; verification pending.)")
standard("FUN.10", NA, FUN, "Function Concepts and Properties", "Paraphrase",
         "Use graphs to understand the relationship between function zeros and equation roots, and use bisection to find approximate solutions. (Public paraphrase; verification pending.)")
standard("FUN.11", NA, FUN, "Function Applications", "Paraphrase",
         "Choose a linear, quadratic, exponential, logarithmic, or other function model to fit a problem and solve simple practical problems. (Public paraphrase; verification pending.)")
standard("FUN.12", NA, FUN, "Trigonometric Functions", "Paraphrase",
         "Understand arbitrary angles and radian measure, convert between degrees and radians, and calculate arc lengths in radians. (Public paraphrase; verification pending.)")
standard("FUN.13", NA, FUN, "Trigonometric Functions", "Paraphrase",
         "Use the unit circle to understand trigonometric functions, determine their signs in each quadrant, and know the fundamental identities for the same angle. (Public paraphrase; verification pending.)")
standard("FUN.14", NA, FUN, "Trigonometric Functions", "Paraphrase",
         "Know the reduction formulas and use them to evaluate trigonometric functions of arbitrary angles in terms of acute angles. (Public paraphrase; verification pending.)")
standard("FUN.15", NA, FUN, "Trigonometric Functions", "Paraphrase",
         "Use graphs to understand the properties of sine, cosine, and tangent, including their domains, ranges, periods, monotonicity, and extrema. (Public paraphrase; verification pending.)")
standard("FUN.16", NA, FUN, "Trigonometric Functions", "Paraphrase",
         "Know the sum-and-difference formulas for sine, cosine, and tangent, as well as the double-angle formulas, and perform simple identities. (Public paraphrase; verification pending.)")
standard("FUN.17", NA, FUN, "Trigonometric Functions", "Paraphrase",
         "Use y=Asin(ωx+φ) to describe periodic phenomena, determine its parameters from given conditions, and solve simple application problems. (Public paraphrase; verification pending.)")

standard("GA.01", GG, GA, "Planar Vectors and Applications", "Paraphrase",
         "Understand planar vectors, equal vectors, and collinear vectors, and represent vectors with directed line segments. (Public paraphrase; verification pending.)")
standard("GA.02", GG, GA, "Planar Vectors and Applications", "Paraphrase",
         "Know vector addition, subtraction, and scalar multiplication and their geometric meanings, and understand when vectors are collinear. (Public paraphrase; verification pending.)")
standard("GA.03", GG, GA, "Planar Vectors and Applications", "Paraphrase",
         "Understand the fundamental theorem of planar vectors, represent vectors using a basis and coordinates, and perform linear operations in coordinates. (Public paraphrase; verification pending.)")
standard("GA.04", GG, GA, "Planar Vectors and Applications", "Paraphrase",
         "Understand the dot product and its coordinate form, and use it to find magnitudes, angles, and perpendicular relationships. (Public paraphrase; verification pending.)")
standard("GA.05", GG, GA, "Planar Vectors and Applications", "Paraphrase",
         "Use the sine and cosine rules to solve triangles and simple geometry and measurement problems. (Public paraphrase; verification pending.)")
standard("GA.06", NA, GA, "Complex Numbers", "Paraphrase",
         "Understand complex numbers, know their algebraic and geometric forms, and determine whether two complex numbers are equal. (Public paraphrase; verification pending.)")
standard("GA.07", NA, GA, "Complex Numbers", "Paraphrase",
         "Know addition, subtraction, multiplication, and division of complex numbers, and understand the geometric meaning of addition and subtraction. Trigonometric form is not required in the compulsory course. (Public paraphrase; verification pending.)")
standard("GA.08", GG, GA, "Introduction to Solid Geometry", "Paraphrase",
         "Recognize prisms, pyramids, frustums, spheres, and simple composite solids, and draw perspective views of horizontally placed plane figures using oblique projection. (Public paraphrase; verification pending.)")
standard("GA.09", GG, GA, "Introduction to Solid Geometry", "Paraphrase",
         "Calculate the surface areas and volumes of simple solids such as prisms, pyramids, cylinders, cones, and spheres. (Public paraphrase; verification pending.)")
standard("GA.10", GG, GA, "Introduction to Solid Geometry", "Paraphrase",
         "Use models such as cuboids to understand the relative positions of points, lines, and planes in space, and learn the basic axioms. (Public paraphrase; verification pending.)")
standard("GA.11", GG, GA, "Introduction to Solid Geometry", "Paraphrase",
         "Understand criteria and properties for parallel lines and planes in space, and identify simple parallel relationships. Calculating dihedral angles is not required. (Public paraphrase; verification pending.)")
standard("GA.12", GG, GA, "Introduction to Solid Geometry", "Paraphrase",
         "Understand criteria and properties for perpendicular lines and planes in space, and identify simple perpendicular relationships. (Public paraphrase; verification pending.)")

standard("PS.01", SP, PS, "Statistics", "Paraphrase",
         "Know the main ways to obtain data and choose an appropriate collection method for a given problem. (Public paraphrase; verification pending.)")
standard("PS.02", SP, PS, "Statistics", "Paraphrase",
         "Understand simple random sampling and stratified random sampling, and select and carry out a method based on the population. (Public paraphrase; verification pending.)")
standard("PS.03", SP, PS, "Statistics", "Paraphrase",
         "Create frequency tables and histograms, read frequencies from a histogram, and estimate percentile positions. (Public paraphrase; verification pending.)")
standard("PS.04", SP, PS, "Statistics", "Paraphrase",
         "Use sample statistics and charts to estimate population characteristics, appreciate the uncertainty of statistical inference, and complete simple statistical case studies. (Public paraphrase; verification pending.)")
standard("PS.05", SP, PS, "Probability", "Paraphrase",
         "Understand sample points and sample spaces, and use set notation to represent random events and event operations. (Public paraphrase; verification pending.)")
standard("PS.06", SP, PS, "Probability", "Paraphrase",
         "Understand classical probability, know its basic properties, and use the addition rule for mutually exclusive events. (Public paraphrase; verification pending.)")
standard("PS.07", SP, PS, "Probability", "Paraphrase",
         "Understand independence of events and use it to calculate the probability that two events occur together. Conditional probability is not required in the compulsory course. (Public paraphrase; verification pending.)")
standard("PS.08", SP, PS, "Probability", "Paraphrase",
         "Understand the stability of relative frequency, use it to estimate probability, and distinguish frequency from probability. (Public paraphrase; verification pending.)")

standard("MI.01", IP, MI, "Mathematical Modeling Activity", "Paraphrase",
         "Work through the full mathematical modeling process: pose a question, collect data, build a function model, solve and validate it, and complete a function-modeling activity. (Public paraphrase; verification pending.)")
standard("MI.02", IP, MI, "Mathematical Inquiry Activity", "Paraphrase",
         "Carry out a mathematical inquiry, use vectors to study the relationships between a triangle's sides and angles, and report the findings. (Public paraphrase; verification pending.)")
