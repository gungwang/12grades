"""Continuation of Compulsory Course 2: dot products, solving triangles, exploration, and complex numbers. Imported by hs_book2.py."""
from hs_common import questions, topic

NA = "Numbers and Algebra"
GG = "Geometry"
IP = "Comprehensive Practice"
C6 = "Chapter 6: Plane Vectors and Their Applications"
C7 = "Chapter 7: Complex Numbers"


def T(key, chapter, section, name, domain, typ, desc, crit, std, conf="exact", note=None):
    topic(key, 2, chapter, section, name, domain, typ, desc, crit, std, conf, note)


def Qs(key, items):
    questions(key, items)


def n(prompt, verify, expl):
    return ("n", prompt, verify, expl)


def c(prompt, ok, bad, expl):
    return ("c", prompt, ok, bad, expl)


T("vec.dot", C6, "6.4", "Vector Dot Product", GG, "procedural",
  "Know a·b=|a||b|cosθ and calculate the dot product from coordinates using x1x2+y1y2.",
  ["Calculate a dot product from coordinates", "Know that a dot product is a scalar"],
  "GA.04")
Qs("vec.dot", [
    n("Find (1, 2)·(3, 4).", "1*3+2*4",
      "1×3+2×4=11."),
    n("Find (1, 0)·(0, 1).", "1*0+0*1",
      "The coordinate basis vectors are perpendicular, so their dot product is 0."),
    n("a=(2, −1). Find a·a.", "2*2+(-1)*(-1)",
      "4+1=5, which is the square of the magnitude."),
    c("What is the result of a dot product?", "A real number", ["A vector", "A line", "A point"],
      "A dot product, also called a scalar product, is a number rather than a vector."),
])

T("vec.dotop", C6, "6.4", "Properties of the Dot Product", GG, "procedural",
  "Use the distributive property to expand dot products and know that a·a equals the square of the magnitude.",
  ["Calculate a·a", "Use the distributive property to find (a+b)·c"],
  "GA.04", "inferred", "The properties are computational rules that follow the definition of the dot product. Needs verification.")
Qs("vec.dotop", [
    n("a=(3, 4). Since |a|²=a·a, what is |a|?", "isqrt(3*3+4*4)",
      "3²+4²=25, so the magnitude is 5."),
    n("a=(1, 2), b=(3, 0), c=(1, 1). Find a·c and b·c, then add them. What is the result?", "(1*1+2*1)+(3*1+0*1)",
      "(a+b)·c=a·c+b·c, so 1+2+3=6."),
    n("If a·b=4, what is (2a)·b?", "2*4",
      "A scalar factor can be taken outside the dot product, so 2×4=8."),
    c("In general, is a·b equal to b·a?", "Yes", ["No", "Only when they are perpendicular", "Only when they are parallel"],
      "The dot product is commutative; changing the order of the coordinate products does not change their sum."),
])

T("vec.angle", C6, "6.4", "Vector Magnitude and Angle", GG, "procedural",
  "Find a vector's magnitude from its coordinates and determine whether two vectors are perpendicular.",
  ["Find a magnitude using the Pythagorean theorem", "Know that a zero dot product indicates perpendicular vectors"],
  "GA.04", "inferred", "Magnitude and angle are geometric interpretations of the dot product. Needs verification.")
Qs("vec.angle", [
    n("Find the magnitude of the vector (3, 4).", "isqrt(3**2+4**2)",
      "√(9+16)=√25=5."),
    n("Find the magnitude of the vector (5, 12).", "isqrt(5**2+12**2)",
      "√(25+144)=√169=13."),
    n("a=(1, 2), b=(2, −1). What is a·b, and are the vectors perpendicular?", "1*2+2*(-1)",
      "2−2=0. The dot product is 0, so the vectors are perpendicular."),
    c("What is the necessary and sufficient condition for two nonzero vectors to be perpendicular?", "Their dot product is 0",
      ["Their magnitudes are equal", "Their sum is the zero vector", "Their coordinates are equal"],
      "a·b=|a||b|cosθ=0. Since neither magnitude is 0, cosθ=0."),
])

T("vec.cos", C6, "6.4", "Law of Cosines", GG, "procedural",
  "Use the law of cosines to find the square of the third side when two sides and the cosine of their included angle are known.",
  ["State the law of cosines", "Find the square of the third side when cos is 0, 1, or 1/2"],
  "GA.05")
Qs("vec.cos", [
    n("Two sides are 2 and 3, and the cosine of their included angle is 1/2. What is the square of the third side?", "2**2+3**2-2*2*3*Fraction(1,2)",
      "c²=a²+b²−2ab cosC=4+9−6=7."),
    n("Two sides are 3 and 4, and their included angle is 90°, so its cosine is 0. What is the square of the third side?", "3**2+4**2-0",
      "For a right angle, the cosine term is 0, so 3²+4²=25."),
    n("What is the length of the third side in the previous question?", "isqrt(25)",
      "√25=5, which is the Pythagorean theorem."),
    c("When the included angle is acute, the term −2ab cosC in the law of cosines is?", "Negative; the square of the third side is less than the sum of the squares of the other two sides",
      ["Always positive", "Always 0", "Independent of the angle"],
      "The cosine of an acute angle is positive, so a positive value is subtracted from the sum of the squares."),
])

T("vec.sin", C6, "6.4", "Law of Sines", GG, "procedural",
  "Use a/sinA=2R to find a side or the diameter for special angles.",
  ["Use the law of sines when sin is 1 or 1/2", "State the relation between the law of sines and the circumcircle's diameter"],
  "GA.05", "inferred", "The law of sines and law of cosines are both used to solve triangles. Needs verification.")
Qs("vec.sin", [
    n("a=2, A=30°, sin30°=1/2. What is a/sinA?", "2/sin(radians(30))",
      "2÷(1/2)=4. This equals the circumcircle's diameter, 2R."),
    n("In a right triangle, the hypotenuse is opposite 90° and sin90°=1. If the hypotenuse c=6, what is c/sinC?", "6/sin(radians(90))",
      "6/1=6, which is the hypotenuse itself because the hypotenuse is the circumcircle's diameter."),
    n("A=90°, a=10. The circumradius R satisfies 2R=a/sinA. What is R?", "10/2",
      "sin90°=1, so 2R=10 and R=5."),
    c("When is the law of sines useful?", "When two angles and one side are known, or when two sides and the opposite angle of one are known",
      ["Only to find a vector's magnitude", "As a replacement for every use of the law of cosines", "Only for equilateral triangles"],
      "The law of sines relates each side to the sine of its opposite angle."),
])

T("vec.solve", C6, "6.4", "Solving Triangles", GG, "application",
  "Choose the law of sines or cosines to find unknown side or angle values in a triangle.",
  ["Choose whether to use the law of sines or cosines", "Find the third side of a right triangle"],
  "GA.05", "inferred", "Solving triangles combines the laws of sines and cosines. Needs verification.")
Qs("vec.solve", [
    n("Two sides of a triangle are 6 and 8, and their included angle is 90°. What is the third side?", "isqrt(6**2+8**2)",
      "The triangle is right-angled, so the third side is √(36+64)=10."),
    n("An equilateral triangle has side length 2. What is the measure of each interior angle?", "60",
      "All three sides and angles are equal, so each angle is 60°."),
    n("What is the sum of the interior angles of a triangle, in degrees?", "180",
      "When solving a triangle, the angle sum gives the third angle if the other two are known."),
    c("Which law should you use first to find an angle when all three sides are known?", "The law of cosines",
      ["The law of sines", "Measure only once with a protractor", "Vector addition"],
      "When all three sides are known, the law of cosines directly gives the cosine of an angle."),
])

T("vec.sapply", C6, "6.4", "Practical Applications of Triangle Solving", GG, "application",
  "Translate simple measurement problems into finding a side or angle of a triangle.",
  ["Identify the known sides and angles in a measurement problem", "Find a distance in a right-angle setting"],
  "GA.05", "inferred", "Measurement is a typical application of solving triangles. Needs verification.")
Qs("vec.sapply", [
    n("A boat travels 12 km straight out from the shore, then another 5 km at a right angle. How far is it from the starting point in a straight line?", "isqrt(12**2+5**2)",
      "The two legs are perpendicular, so the distance is √(144+25)=13 km."),
    n("A ramp has a vertical rise of 3 m and a horizontal run of 4 m. How long is the sloping surface?", "isqrt(3**2+4**2)",
      "The hypotenuse of the right triangle is 5 m."),
    n("A right triangle has hypotenuse 2 and an acute angle of 30°. What is the length of the side opposite this angle?",
      "2*sin(radians(30))",
      "The opposite side equals the hypotenuse times the sine, so 2×1/2=1."),
    c("When turning a real measurement problem into a triangle-solving problem, what should you do first?", "Draw a diagram and label the known sides and angles",
      ["Apply the law of sines without identifying the sides", "Measure a length only once", "Ignore the right angle"],
      "First identify which known elements are sides and which are angles, then choose a theorem."),
])

T("vec.geom", C6, "6.4", "Using Vectors to Study Geometry", GG, "reasoning",
  "Use vector magnitudes and dot products to show simple geometric facts about perpendicularity and length.",
  ["Use the dot product to determine perpendicularity", "Compare lengths using magnitudes"],
  "GA.05", "inferred", "Using vectors to study geometry is an application beyond the laws of sines and cosines. Needs verification.")
Qs("vec.geom", [
    n("Adjacent side vectors of a parallelogram are (2, 1) and (1, −2). What is their dot product?", "2*1+1*(-2)",
      "2−2=0, so the adjacent sides are perpendicular."),
    n("What is the magnitude of the vector (6, 8)?", "isqrt(6**2+8**2)",
      "√(36+64)=10."),
    n("A(0, 0), B(3, 4). What is the length of line segment AB?", "isqrt(3**2+4**2)",
      "The vector AB=(3, 4) has magnitude 5."),
    c("To prove that two lines are perpendicular using vectors, what should you show about their direction vectors?", "Their dot product is 0",
      ["Their magnitudes are equal", "Their sum is the zero vector", "All their coordinates are positive"],
      "Two nonzero vectors are perpendicular when their dot product is 0."),
])

T("mod.vec", "Mathematical Exploration", "Using Vectors to Study Triangles", "Using Vectors to Study Triangles", IP, "modeling",
  "Use vectors to restate relationships between the sides and angles of a triangle, following the steps of an exploration and calculating a specific example.",
  ["State that an exploration includes a conjecture, derivation, and verification", "Calculate a triangle side length using vector coordinates"],
  "MI.02")
Qs("mod.vec", [
    n("A triangle has vertices A(0, 0), B(4, 0), and C(0, 3). What is the length of side BC?", "isqrt((4-0)**2+(0-3)**2)",
      "Vector BC=(4, −3), so its magnitude is √(16+9)=5."),
    n("A triangle has vertices A(0, 0), B(4, 0), and C(0, 3). What is the length of side AB?", "isqrt((4-0)**2+(0-0)**2)",
      "Vector AB=(4, 0), so its magnitude is √(16+0)=4."),
    n("A triangle has vertices A(0, 0), B(4, 0), and C(0, 3). What is the length of side AC?", "isqrt((0-0)**2+(3-0)**2)",
      "Vector AC=(0, 3), so its magnitude is √(0+9)=3."),
    c("What is the main point of this exploration?", "Vectors can turn relationships between a triangle's sides and angles into coordinate calculations",
      ["Vectors cannot be used with triangles", "Triangles can only be studied with a protractor", "An exploration does not need a specific example"],
      "This right triangle shows AB²+AC²=BC², consistent with the law of cosines."),
])

T("cpx.def", C7, "7.1", "Definition of a Complex Number", NA, "conceptual",
  "Know that a complex number is z=a+bi, where a and b are real numbers and i²=−1; a is the real part and b is the imaginary part.",
  ["Identify the real and imaginary parts", "Know that a real number is a complex number with imaginary part 0"],
  "GA.06")
Qs("cpx.def", [
    n("What is the real part of the complex number 3−2i?", "3",
      "The real part is the term without i, which is 3 here."),
    n("What is the imaginary part of the complex number 3−2i?", "-2",
      "The imaginary part is the real coefficient of i, which is −2, not −2i."),
    n("What is i²?", "-1",
      "The square of the imaginary unit is defined as −1."),
    c("When the real number 5 is written as a complex number, what is its imaginary part?", "0", ["5", "1", "i"],
      "5=5+0i, so its imaginary part is 0."),
])

T("cpx.geo", C7, "7.1", "Geometric Representation of Complex Numbers", NA, "conceptual",
  "Know that a complex number a+bi corresponds to the point (a, b) on the complex plane and that its modulus is the distance from that point to the origin.",
  ["Write the point corresponding to a complex number", "Calculate a modulus when the square root is exact"],
  "GA.06", "inferred", "The geometric representation and the definition of complex numbers are covered in the same item. Needs verification.")
Qs("cpx.geo", [
    n("What is the modulus of the complex number 3+4i?", "isqrt(3**2+4**2)",
      "It corresponds to the point (3, 4), which is 5 units from the origin."),
    n("What is the modulus of the complex number −6?", "6",
      "It corresponds to the point (−6, 0), which is 6 units from the origin."),
    c("Which point on the complex plane corresponds to a+bi?", "(a, b)", ["(b, a)", "(a, bi)", "(i, a)"],
      "The real part is the horizontal coordinate, and the imaginary part is the vertical coordinate."),
    c("Where is the point corresponding to the pure imaginary number 2i?", "On the imaginary axis", ["On the real axis", "At the origin", "On the line y=x"],
      "Its real part is 0, so its point is (0, 2), on the imaginary axis."),
])

T("cpx.eq", C7, "7.1", "Equality of Complex Numbers", NA, "procedural",
  "Know that a+bi=c+di if and only if a=c and b=d.",
  ["Compare the real and imaginary parts separately", "Use the equality to find an unknown real number"],
  "GA.06", "inferred", "The equality condition is a basic property of the algebraic form. Needs verification.")
Qs("cpx.eq", [
    n("If x+2i=3+yi, where x and y are real numbers, what is x?", "3",
      "The real parts are equal, so x=3."),
    n("What is y in the previous question?", "2",
      "The imaginary parts are equal, so y=2."),
    n("If (m+1)+(n−1)i=0, what is m?", "-1",
      "0=0+0i, so the real parts give m+1=0 and m=−1."),
    c("For two complex numbers to be equal, what must be true?", "Their real parts and their imaginary parts are equal",
      ["Only their moduli are equal", "Only their real parts are equal", "Only the absolute values of their imaginary parts are equal"],
      "The real and imaginary parts in the algebraic form are unique, so both must match."),
])

T("cpx.add", C7, "7.2", "Addition and Subtraction of Complex Numbers", NA, "procedural",
  "Add or subtract the real parts together and the imaginary parts together.",
  ["Calculate the sum of two complex numbers", "Calculate the difference of two complex numbers"],
  "GA.07")
Qs("cpx.add", [
    n("What is the real part of (1+2i)+(3+4i)?", "1+3",
      "The real part is 1+3=4."),
    n("What is the imaginary part of (1+2i)+(3+4i)?", "2+4",
      "Add the imaginary parts: 2+4=6."),
    n("What is the real part of (5+i)−(2+3i)?", "5-2",
      "The real part is 5−2=3."),
    n("What is the imaginary part of (5+i)−(2+3i)?", "1-3",
      "The imaginary part is 1−3=−2."),
])

T("cpx.addg", C7, "7.2", "Geometric Meaning of Complex Addition and Subtraction", NA, "reasoning",
  "Know that adding and subtracting complex numbers corresponds to adding and subtracting vectors, and that the modulus of a sum does not exceed the sum of the moduli.",
  ["Add and subtract complex numbers by treating them as vectors", "Compare the modulus of a sum with the sum of the moduli"],
  "GA.07", "inferred", "The geometric meaning interprets addition and subtraction in terms of vectors. Needs verification.")
Qs("cpx.addg", [
    n("The moduli of 3 and 4i are 3 and 4, respectively. What is the modulus of their sum, 3+4i?", "isqrt(3**2+4**2)",
      "The two vectors are perpendicular, so the modulus of their sum is 5."),
    n("What is the sum of the two moduli in the previous question?", "3+4",
      "3+4=7, which is greater than the modulus of the sum, 5."),
    n("The complex numbers 2 and 5 both lie on the real axis. What is the modulus of their sum?", "2+5",
      "When they point in the same direction, their moduli add directly, giving 7."),
    c("What is the relationship between |z1+z2| and |z1|+|z2|?", "|z1+z2| is less than or equal to |z1|+|z2|",
      ["Always strictly greater", "Always equal", "There is no definite relationship"],
      "This is the triangle inequality. Equality holds when the directions are the same."),
])

T("cpx.mul", C7, "7.2", "Multiplication of Complex Numbers", NA, "procedural",
  "Multiply complex numbers using the distributive property and replace i² with −1.",
  ["Find the real part of the product of two complex numbers", "Evaluate positive integer powers of i that simplify to ±1"],
  "GA.07", "inferred", "Multiplication, addition, and subtraction are all basic arithmetic operations. Needs verification.")
Qs("cpx.mul", [
    n("Evaluate (1+i)(1−i).", "1*1-1*(-1)",
      "(1+i)(1−i)=1−(i)²=1−(−1)=2. The imaginary part is 0."),
    n("Evaluate i².", "-1",
      "By definition, i²=−1."),
    n("Evaluate i⁴.", "1",
      "i⁴=(i²)²=(−1)²=1."),
    n("What is the real part of (2+i)(1+0i)?", "2",
      "Multiplication by 1 leaves the complex number unchanged, so the real part remains 2."),
])

T("cpx.div", C7, "7.2", "Division of Complex Numbers", NA, "procedural",
  "Use the conjugate of the denominator to turn division into multiplication, then find the real or imaginary part of the result.",
  ["Identify a complex conjugate", "Calculate quotients with a real denominator or an integer result"],
  "GA.07", "inferred", "Division is the final basic arithmetic operation. Needs verification.")
Qs("cpx.div", [
    n("What is the real part of (4+6i)/2?", "4/2",
      "Divide the real and imaginary parts by 2; the real part is 2."),
    n("What is the imaginary part of (4+6i)/2?", "6/2",
      "The imaginary part is 6/2=3."),
    n("The conjugate of 1+i is 1−i. What is their product?", "1*1-1*(-1)",
      "A complex number multiplied by its conjugate equals the square of its modulus, which is 2 here."),
    n("What is (1+i)/(1+i)?", "1",
      "A nonzero complex number divided by itself equals 1."),
])

T("cpx.pow", C7, "7.2", "Powers of Complex Numbers", NA, "procedural",
  "Evaluate integer powers of i and simple powers with real coefficients that simplify to integers.",
  ["Simplify powers of i to 1, −1, i, or −i, including the real-valued cases", "Calculate (a+bi)(a−bi)"],
  "GA.07", "inferred", "Powers are repeated multiplication; this item does not cover trigonometric form. Needs verification.")
Qs("cpx.pow", [
    n("i³=−i. What is its imaginary part?", "-1",
      "i³=i²·i=−i, so the imaginary part is −1 and the real part is 0."),
    n("Evaluate (1+2i)(1−2i).", "1*1-2*(-2)",
      "1−(2i)²=1−4i²=1+4=5."),
    n("Evaluate (3+i)(3−i).", "3*3-1*(-1)",
      "The square of the modulus is 9+1=10."),
    c("Starting with i¹, which cycle describes the positive integer powers of i?", "i, −1, −i, 1",
      ["Only 1 and −1", "Only i", "1, i, and −1"],
      "The powers repeat every 4 steps: i, −1, −i, 1."),
])
