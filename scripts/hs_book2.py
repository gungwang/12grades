"""High school math, Book 2 (People's Education Press A, 2019): plane vectors, mathematical inquiry, and complex numbers.

The chapter list is compiled from third-party sources, not the publisher's official site. Page numbers have not been verified:
- Douban journal: https://www.douban.com/note/831269463/
- Textbook contents PDF compiled by Xu Qingpei: https://www.drhuang.com/chinese/science/mathematics/高中教科书数学目录.pdf

Chapter 6 through section 6.4 is included, with an inquiry activity that uses vectors to study triangles. Only sections 7.1 and 7.2 of Chapter 7 are included.
Section 7.3, the trigonometric form of complex numbers, is treated as optional and excluded. No finer section numbers are inferred.
"""
# The Chinese path in the cited PDF URL is part of the external resource URL and stays unchanged.
from hs_common import questions, topic

NA = "Numbers and Algebra"
GG = "Geometry"
IP = "Integrated Practice"
C6 = "Chapter 6: Plane Vectors and Their Applications"
C7 = "Chapter 7: Complex Numbers"


def T(key, chapter, section, name, domain, typ, desc, crit, std, conf="exact", note=None):
    topic(key, 2, chapter, section, name, domain, typ, desc, crit, std, conf, note)


def Qs(key, items):
    questions(key, items)


def n(prompt, verify, expl):
    return ("n", prompt, verify, expl)


def nu(prompt, verify, expl):
    return ("nu", prompt, verify, expl)


def c(prompt, ok, bad, expl):
    return ("c", prompt, ok, bad, expl)


T("vec.def", C6, "6.1", "Concept of plane vectors", GG, "conceptual",
  "Understand that a vector has both magnitude and direction, and that its length is called its magnitude.",
  ["Distinguish vectors from scalars", "State that the zero vector has magnitude 0"],
  "GA.01")
Qs("vec.def", [
    c("How does a vector differ from a scalar?", "A vector has direction; a scalar does not",
      ["A vector has no magnitude", "A scalar must have direction", "They are exactly the same"],
      "A vector is represented by a directed line segment. It has both magnitude and direction."),
    n("A vector has magnitude 5. What is its length?", "5",
      "A vector's magnitude is its length, so it is 5."),
    c("What is the magnitude of the zero vector?", "0", ["1", "Cannot be determined", "Equal to a unit vector"],
      "The zero vector has length 0. Its direction is undefined, so it is not compared by direction with other vectors."),
    c("When a vector is represented by a directed line segment, what must be specified?", "Its start point, endpoint, and direction",
      ["Only its length", "Only its start point", "Only the line it lies on"],
      "Without direction, only the length remains, so the vector is not uniquely determined."),
])

T("vec.eq", C6, "6.1", "Equal and collinear vectors", GG, "conceptual",
  "Understand that equal vectors have the same direction and magnitude, while collinear vectors point in the same or opposite directions.",
  ["Determine whether two vectors are equal", "Distinguish equality from collinearity"],
  "GA.01", "inferred", "Equality and collinearity are basic vector relationships. To be verified.")
Qs("vec.eq", [
    c("Two vectors are equal when they have?", "The same magnitude and direction",
      ["Only the same magnitude", "Only the same direction", "The same start point"],
      "Equality does not depend on the start point. Vectors can remain equal after being translated in parallel."),
    c("Two vectors with opposite directions and equal magnitudes are?", "Collinear but not equal",
      ["Equal", "Neither equal nor collinear", "Both must be zero vectors"],
      "Collinear vectors can point in the same or opposite directions. Opposite directions mean they are not equal."),
    n("Vector a has magnitude 4. What is the magnitude of any vector equal to a?", "4",
      "Equal vectors must have the same magnitude."),
    c("A unit vector is a vector with?", "Magnitude 1", ["Magnitude 0", "A direction parallel to an axis", "Any nonzero magnitude"],
      "A unit vector is restricted only to length 1; its direction can vary."),
])

T("vec.add", C6, "6.2", "Vector addition", GG, "procedural",
  "Use the triangle and parallelogram rules to add vectors, and add vectors by their coordinates.",
  ["Calculate the sum of two coordinate vectors", "State that vector addition is commutative"],
  "GA.02")
Qs("vec.add", [
    n("What is the x-coordinate of the sum of vectors (1, 2) and (3, 4)?", "1+3",
      "Add corresponding coordinates; the x-coordinate is 1+3=4."),
    n("What is the y-coordinate of the sum of vectors (1, 2) and (3, 4)?", "2+4",
      "Add corresponding coordinates; the y-coordinate is 2+4=6."),
    n("What is the x-coordinate of the sum of vectors (5, −1) and (−2, 1)?", "5+(-2)",
      "5−2=3."),
    c("Which methods can be used to add vectors?", "The triangle rule or the parallelogram rule",
      ["Add only their lengths and ignore direction", "Use coordinates only; do not draw a diagram", "Take the dot product first"],
      "Joining vectors head to tail is the triangle rule. They can also be drawn from a common start point as a parallelogram."),
])

T("vec.sub", C6, "6.2", "Vector subtraction", GG, "procedural",
  "Understand that a−b=a+(−b), and subtract vectors by their coordinates.",
  ["Calculate the difference of coordinate vectors", "State that subtracting a vector is adding its opposite"],
  "GA.02", "inferred", "Subtraction is the inverse operation of addition and is a linear operation. To be verified.")
Qs("vec.sub", [
    n("Subtract (2, 3) from vector (5, 1). What is the x-coordinate of the difference?", "5-2",
      "Subtract corresponding coordinates: 5−2=3."),
    n("What is the y-coordinate of the difference in the previous question?", "1-3",
      "1−3=−2."),
    n("If a=(4, 4), what is the magnitude of a−a?", "0",
      "Every vector minus itself is the zero vector, whose magnitude is 0."),
    c("What is a−b equal to?", "a plus the opposite of b",
      ["The magnitude of a minus the magnitude of b", "a with its direction reversed", "The dot product of a and b"],
      "Subtraction is defined as adding the opposite vector, not subtracting lengths directly."),
])

T("vec.mul", C6, "6.2", "Scalar multiplication of vectors", GG, "procedural",
  "Multiply a vector by a real number: a positive scalar keeps its direction, a negative scalar reverses it, and its magnitude is multiplied by the scalar's absolute value.",
  ["Calculate the coordinates after scalar multiplication", "State the magnitude after scalar multiplication"],
  "GA.02", "inferred", "Scalar multiplication, addition, and subtraction form the linear operations on vectors. To be verified.")
Qs("vec.mul", [
    n("What is the y-coordinate of 3 times vector (1, −2)?", "3*(-2)",
      "Multiply each coordinate by 3; the y-coordinate is −6."),
    n("Vector (3, 4) has magnitude 5. What is the magnitude of twice this vector?", "2*5",
      "Multiplication by a positive scalar multiplies the magnitude by that scalar: 2×5=10."),
    n("What is the x-coordinate of −1 times vector (2, −5)?", "-1*2",
      "The opposite vector has x-coordinate −2."),
    c("When k<0, what is the direction of k times a nonzero vector?", "Opposite to the original vector",
      ["The same as the original vector", "It becomes the zero vector", "Perpendicular to the original vector"],
      "A negative scalar reverses the direction and multiplies the magnitude by |k|."),
])

T("vec.col", C6, "6.2", "Vector collinearity theorem", GG, "reasoning",
  "Understand that a nonzero vector b is collinear with a if and only if there is a real number λ such that b=λa.",
  ["Determine whether one vector is a scalar multiple of another", "Find the scalar multiple"],
  "GA.02", "inferred", "The collinearity theorem uses scalar multiplication as a test. To be verified.")
Qs("vec.col", [
    n("What multiple of (1, 2) is vector (2, 4)?", "2",
      "2×(1, 2)=(2, 4), so the multiple is 2 and the vectors are collinear."),
    n("If (k, 6) is collinear with (2, 3), and the second coordinates give k/2=6/3, what is k?", "2*(6/3)",
      "Corresponding coordinates are proportional: k/2=2, so k=4."),
    c("Are (1, 0) and (0, 1) collinear?", "No", ["Yes", "Only if they have the same start point", "Yes, because their directions are opposite"],
      "There is no real number λ for which (0, 1)=λ(1, 0): the first coordinate would require λ=0, but the second coordinate is 1."),
    c("By the definition of collinearity, how is the zero vector related to any vector?", "The zero vector is collinear with any vector",
      ["It is collinear only with the zero vector", "It is perpendicular to every vector", "The relationship is undefined"],
      "Taking λ=0 gives 0=λa. The textbook treats the zero vector as collinear with every vector."),
])

T("vec.thm", C6, "6.3", "Fundamental theorem of plane vectors", GG, "conceptual",
  "Understand that two non-collinear vectors form a basis and every vector in the plane has a unique decomposition in that basis.",
  ["State that basis vectors must be non-collinear", "Express a vector as a linear combination of two non-collinear vectors"],
  "GA.03")
Qs("vec.thm", [
    c("For two vectors to form a basis for the plane, they must be?", "Non-collinear",
      ["Both have magnitude 1", "Perpendicular to each other", "Have different start points"],
      "Two collinear vectors cannot span the plane. They do not have to be perpendicular or unit vectors."),
    n("e1=(1, 0), e2=(0, 1), and (3, 5)=3 e1+5 e2. What is the coefficient of e1?", "3",
      "By the theorem, the coefficients are the coordinates in this basis: 3 and 5."),
    n("In the previous question, what is the coefficient of e2?", "5",
      "The y-coordinate 5 is the coefficient of e2."),
    c("In the basis e1=(1, 0), e2=(0, 1), what is true of the decomposition of (3, 5)?", "It is unique",
      ["There are infinitely many possible coefficients", "Uniqueness requires an orthogonal basis", "The coefficients must be positive"],
      "e1 and e2 are non-collinear and form a basis. The theorem guarantees that (3, 5)=3 e1+5 e2 exists and is unique."),
])

T("vec.coord", C6, "6.3", "Coordinate representation of a vector", GG, "procedural",
  "Represent a vector in the Cartesian plane using the coordinates of its start point and endpoint.",
  ["Find vector coordinates from its start point and endpoint", "State that vector coordinates equal endpoint coordinates minus start-point coordinates"],
  "GA.03", "inferred", "Coordinate representation is the fundamental theorem written in an orthogonal basis. To be verified.")
Qs("vec.coord", [
    n("The start point is (1, 2) and the endpoint is (4, 6). What is the vector's x-coordinate?", "4-1",
      "The x-coordinate is the endpoint's x-coordinate minus the start point's: 4−1=3."),
    n("What is the vector's y-coordinate in the previous question?", "6-2",
      "6−2=4."),
    n("If the start point and endpoint are both (2, −1), what is the vector's magnitude?", "0",
      "Its coordinates are (0, 0), so it is the zero vector."),
    c("Do a vector's coordinates depend on its start point?", "Yes; they equal the endpoint coordinates minus the start-point coordinates",
      ["No; they depend only on direction", "They depend only on length", "The start point must be the origin"],
      "Equal vectors have the same coordinates, but the coordinates of a directed segment are calculated from its own start point and endpoint."),
])

T("vec.coordop", C6, "6.3", "Coordinate operations", GG, "procedural",
  "Add, subtract, and scalar-multiply vectors using their coordinates.",
  ["Add or subtract corresponding coordinates", "Find the coordinates of a linear combination"],
  "GA.03", "inferred", "Coordinate operations are linear operations expressed in coordinates. To be verified.")
Qs("vec.coordop", [
    n("a=(2, −1), b=(1, 4). What is the x-coordinate of 2a+b?", "2*2+1",
      "2×2+1=5."),
    n("a=(2, −1), b=(1, 4). What is the y-coordinate of 2a+b?", "2*(-1)+4",
      "The y-coordinate is 2×(−1)+4=2."),
    n("a=(3, 1), b=(3, 1). What is the magnitude of a−b?", "0",
      "The difference is the zero vector."),
    nu("a=(1, 0), b=(0, 1). What are the two coordinates of a+b?", "(1,1)",
      "The sum is (1, 1). Write both coordinates; either order is acceptable."),
])

import hs_book2_b  # noqa: E402,F401
import hs_book2_c  # noqa: E402,F401
import hs_book2_edges  # noqa: E402,F401
