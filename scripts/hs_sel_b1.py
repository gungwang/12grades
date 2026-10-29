"""People's Education Press A (2019), Selective Compulsory, Book 1.

The chapter outline is compiled from the following third-party sources. None is the People's Education Press official website; page numbers have not been verified:
- Teachers' Home https://www.renjiaoshe.com/jiaocai/2072.html (1.1–1.4, 2.1–2.5, 3.1–3.3)
- E-Book Textbook Network https://www.dzskb.com/rjabgzsxxzxbx1.html
- Learning Power reposted table of contents http://www.xuexili.com/keben/70150.html

Only sections confirmed by these sources are included; finer subsection numbers and page numbers are not invented.
Subdivisions such as 1.1.1 come from lesson-video titles and are not treated as original textbook subsection numbers.
"""
from hs_sel_common import questions, topic

GG = "Geometry and Measurement"

C1 = "Chapter 1: Spatial Vectors and Solid Geometry"
C2 = "Chapter 2: Equations of Lines and Circles"
C3 = "Chapter 3: Equations of Conic Sections"


def T(key, chapter, section, name, typ, desc, crit, std, conf="exact", note=None):
    topic(key, 1, chapter, section, name, GG, typ, desc, crit, std, conf, note)


def Qs(key, items):
    questions(key, items)


def n(prompt, verify, expl):
    return ("n", prompt, verify, expl)


def c(prompt, ok, bad, expl):
    return ("c", prompt, ok, bad, expl)


NOTE = "The textbook separates this requirement into practice items. Needs verification."

# ---------------------------------------------------------------- Chapter 1

T("sv.def", C1, "1.1", "Concept of a Spatial Vector", "conceptual",
  "A spatial vector is a quantity in space with both magnitude and direction, extending the idea of a plane vector.",
  ["Explain the relationship between a spatial vector and a directed segment", "Know that vectors with the same direction but different magnitudes are not equal"],
  "GA.13", "inferred", "The concept appears at the start of the spatial-vector operations requirement. Needs verification.")
Qs("sv.def", [
    c("Which option describes a spatial vector?", "a quantity with both magnitude and direction",
      ["a quantity with length but no direction", "a point with a position but no magnitude", "a segment with no indicated direction"],
      "A vector has both magnitude and direction. A segment with no indicated direction is not a vector."),
    n("a=(1，0，0), b=(2，0，0). The vectors have the same direction. How many times larger is |b| than |a|?", "2",
      "Their magnitudes are 1 and 2, so |b| is twice |a|. Vectors with the same direction but different magnitudes are not equal."),
    c("What is the magnitude of the zero vector?", "0",
      ["1", "the magnitude of any nonzero vector", "undefined"],
      "The zero vector has length 0. Its direction is undefined, but its magnitude is 0."),
    n("A(0，0，0), B(0，3，0). What is the y-coordinate of the vector represented by directed segment AB?", "3",
      "Subtract the starting point's y-coordinate from the endpoint's: 3−0=3."),
])

T("sv.lin", C1, "1.1", "Linear Operations on Spatial Vectors", "procedural",
  "Perform addition, subtraction, and scalar multiplication of spatial vectors using the same rules as for plane vectors.",
  ["Calculate the sum and difference of two spatial vectors", "Multiply a spatial vector by a scalar"],
  "GA.13")
Qs("sv.lin", [
    n("a=(1，0，2), b=(3，4，−1). What is the x-coordinate of a+b?", "1+3",
      "Add corresponding coordinates; the x-coordinate is 1+3=4."),
    n("a=(2，−1，4), b=(2，3，1). What is the z-coordinate of a−b?", "4-1",
      "Subtract the z-coordinates: 4−1=3."),
    n("a=(1，−2，3). What is the y-coordinate of 3a?", "3*(-2)",
      "Multiply each coordinate by 3; the y-coordinate is 3×(−2)=−6."),
    c("Which rule can be used to add spatial vectors?", "the triangle rule or the parallelogram rule",
      ["multiply all the coordinates", "only the zero vector in a common plane", "the sum of two vectors is always the zero vector"],
      "Spatial-vector addition uses the triangle rule or parallelogram rule, just like plane-vector addition."),
])

T("sv.dot", C1, "1.1", "Dot Product of Spatial Vectors", "procedural",
  "The dot product of spatial vectors is the sum of the products of corresponding coordinates, and also the product of their magnitudes and the cosine of their angle.",
  ["Calculate a dot product from coordinates", "Know that two nonzero vectors are perpendicular when their dot product is 0"],
  "GA.13")
Qs("sv.dot", [
    n("a=(1，2，2), b=(2，0，1). What is a·b?", "1*2+2*0+2*1",
      "Multiply corresponding coordinates and add: 2+0+2=4."),
    n("a=(1，0，−1), b=(2，5，2). What is a·b?", "1*2+0*5+(-1)*2",
      "2+0−2=0, so the vectors are perpendicular."),
    c("What does a dot product of 0 tell you about two nonzero spatial vectors?", "the vectors are perpendicular",
      ["the vectors are parallel", "the vectors have equal magnitudes", "the vectors must both be zero vectors"],
      "If two nonzero vectors have a dot product of 0, the cosine of their angle is 0, so the angle is a right angle."),
    n("a=(3，1，0), b=(1，1，4). What is a·b?", "3*1+1*1+0*4",
      "Multiply corresponding coordinates and add: 3+1+0=4."),
])

T("sv.mod", C1, "1.1", "Magnitude and Angle of Spatial Vectors", "procedural",
  "Find a spatial vector's magnitude by taking the square root of the sum of its squared coordinates; use the dot product and both magnitudes to determine the angle.",
  ["Find a vector's magnitude from its coordinates", "Use the dot product to identify an acute, right, or obtuse angle"],
  "GA.13", "inferred", NOTE)
Qs("sv.mod", [
    n("a=(2，3，6). What is |a|?", "isqrt(2*2+3*3+6*6)",
      "The magnitude is the square root of the sum of the squared coordinates: √(4+9+36)=√49=7."),
    n("a=(1，2，2), b=(2，1，−2). What is a·b?", "1*2+2*1+2*(-2)",
      "The dot product is 2+2−4=0, so the angle is a right angle."),
    c("If a·b>0 and neither a nor b is the zero vector, what is the angle between them?", "acute",
      ["right", "obtuse", "always 0 degrees"],
      "The dot product is |a||b|cosθ. Since the magnitudes are positive and the dot product is positive, cosθ>0 and the angle is acute."),
    n("a=(0，3，4). What is |a|?", "isqrt(0+9+16)",
      "√(9+16)=√25=5."),
])

T("sv.col", C1, "1.1", "Collinear Spatial Vectors", "reasoning",
  "Vectors a and b are collinear if a real number λ exists such that b=λa; proportional coordinates can also be used to check collinearity.",
  ["Determine whether two spatial vectors are collinear", "Find an unknown parameter from a collinearity condition"],
  "GA.13", "inferred", NOTE)
Qs("sv.col", [
    n("b=(2，4，−6), a=(1，2，−3). If b=λa, what is λ?", "2",
      "Each coordinate of b is twice the corresponding coordinate of a, so λ=2 and the vectors are collinear."),
    c("a=(1，0，2), b=(2，0，4). What is the relationship between these vectors?", "they are collinear",
      ["perpendicular but not collinear", "neither collinear nor perpendicular", "they must be perpendicular"],
      "b=2a, so the vectors are collinear. Their dot product is 2+0+8≠0, so they are not perpendicular."),
    n("a=(1，2，k) and b=(2，4，6) are collinear. What is k?", "3",
      "The coordinates are proportional: 1/2=2/4=k/6, so k=3."),
    c("Is the zero vector collinear with any spatial vector?", "yes, because 0=0·a",
      ["only with a unit vector", "never", "only when it lies on a coordinate axis"],
      "The zero vector equals any vector multiplied by 0, so it is collinear with every vector."),
])

T("sv.basis", C1, "1.2", "Fundamental Theorem of Spatial Vectors", "conceptual",
  "Any spatial vector can be represented uniquely as a linear combination of three noncoplanar vectors.",
  ["State that a basis requires three noncoplanar vectors", "Determine whether a set of vectors can form a basis"],
  "GA.14")
Qs("sv.basis", [
    c("In the fundamental theorem of spatial vectors, how many noncoplanar vectors are usually needed in a basis?", "3",
      ["2", "4", "1"],
      "A plane basis uses 2 noncollinear vectors; a spatial basis uses 3 noncoplanar vectors."),
    c("Can three vectors in the same plane form a spatial basis?", "no, because they are coplanar",
      ["yes, as long as none is the zero vector", "yes, as long as they are pairwise perpendicular", "no, because spatial vectors cannot be added"],
      "Three coplanar vectors cannot uniquely represent every spatial vector."),
    n("e1, e2, e3 form a basis, and a=2e1−e2+3e3. What is the coefficient of e3?", "3",
      "The linear representation is a=2e1+(−1)e2+3e3, so the coefficient of e3 is 3."),
    c("Is the linear representation of each spatial vector unique for a given basis?", "yes, it is unique",
      ["there are at least two representations", "only unit vectors have unique representations", "the coefficients can be changed arbitrarily"],
      "The theorem states that the coefficients are unique for a fixed basis."),
])

T("sv.orth", C1, "1.2", "Orthogonal Decomposition of Spatial Vectors", "reasoning",
  "If the three basis vectors are pairwise perpendicular, a vector can be decomposed along these three directions.",
  ["State that orthogonal decomposition requires pairwise perpendicular basis vectors", "Read the components along three pairwise perpendicular directions"],
  "GA.14", "inferred", NOTE)
Qs("sv.orth", [
    c("What condition must the three directions satisfy for an orthogonal decomposition?", "they must be pairwise perpendicular",
      ["they must be pairwise parallel", "each must have length 2", "they must be coplanar"],
      "Orthogonal means perpendicular. The three directions must be pairwise perpendicular for decomposition along orthogonal directions."),
    n("i, j, and k are pairwise perpendicular unit vectors. In a=3i−2j+k, what is the coefficient in the k direction?", "1",
      "a is already written as an orthogonal decomposition, and the coefficient of k is 1."),
    n("a=4i+j−2k, where i, j, and k are pairwise perpendicular unit vectors. What is a·i?", "4",
      "In an orthonormal basis, a·i is the coefficient in the i direction, 4."),
    c("What is it called when a vector is decomposed along three pairwise perpendicular directions?", "orthogonal decomposition",
      ["collinear decomposition", "dot product only", "random decomposition"],
      "Decomposition along mutually perpendicular directions is called orthogonal decomposition."),
])

T("sv.frame", C1, "1.3", "Three-Dimensional Cartesian Coordinate System", "conceptual",
  "A three-dimensional Cartesian coordinate system has three number lines originating at the origin and perpendicular to one another; a point is represented by an ordered triple (x，y，z).",
  ["State that the three coordinate axes are pairwise perpendicular", "Read a point's three coordinates"],
  "GA.14")
Qs("sv.frame", [
    n("What is the z-coordinate of P(3，−1，5)?", "5",
      "The third component of an ordered triple is the z-coordinate, which is 5."),
    c("Which coordinate axis contains the point (0，0，4)?", "the z-axis",
      ["the x-axis", "the y-axis", "none of the coordinate axes"],
      "Since x=0 and y=0, the point lies on the z-axis, with z-coordinate 4."),
    c("How are the three axes of a three-dimensional Cartesian coordinate system positioned relative to one another?", "they are pairwise perpendicular",
      ["they are pairwise parallel", "they must be coplanar and overlap", "they intersect but are not perpendicular"],
      "In a right-handed coordinate system, the x-, y-, and z-axes meet at the origin and are pairwise perpendicular."),
    n("What is the distance from A(2，0，0) to the origin?", "2",
      "The point is on the x-axis, so its distance from the origin is the absolute value of its x-coordinate, 2."),
])

T("sv.coord", C1, "1.3", "Coordinates of a Spatial Vector", "procedural",
  "The coordinates of a vector from point A to point B equal the coordinates of B minus those of A.",
  ["Write a vector's coordinates from two points", "Express a vector in component form"],
  "GA.14", "inferred", NOTE)
Qs("sv.coord", [
    n("A(1，2，0), B(4，2，5). What is the x-coordinate of vector AB?", "4-1",
      "Subtract the starting point's x-coordinate from the endpoint's: 4−1=3."),
    n("A(0，1，2), B(0，1，6). What is the z-coordinate of vector AB?", "6-2",
      "The difference in z-coordinates is 6−2=4; the other two components are 0."),
    n("What is the y-coordinate of vector a=(3，−2，1)?", "-2",
      "The second component is the y-coordinate, −2."),
    c("What must be true of the coordinates of equal spatial vectors?", "their corresponding components must be equal",
      ["only their magnitudes need to be equal", "only their x-coordinates need to be equal", "their coordinates may differ by a constant"],
      "Vectors are equal if and only if their corresponding components are equal."),
])

T("sv.cop", C1, "1.3", "Vector Operations in Coordinates", "procedural",
  "In coordinates, linear operations are performed componentwise, and the dot product is the sum of products of corresponding components.",
  ["Add vectors and multiply them by scalars in coordinates", "Calculate a dot product from coordinates"],
  "GA.14", "inferred", NOTE)
Qs("sv.cop", [
    n("a=(1，0，2), b=(3，4，−1). What is the x-coordinate of 2a+b?", "2*1+3",
      "2a=(2，0，4); after adding b, the x-coordinate is 2+3=5."),
    n("a=(1，2，2), b=(2，−1，3). What is a·b?", "1*2+2*(-1)+2*3",
      "2−2+6=6."),
    n("a=(2，−1，2). What is |a|²?", "2*2+(-1)*(-1)+2*2",
      "The square of the magnitude is the sum of the squared coordinates: 4+1+4=9."),
    c("How do you add two vectors in coordinates?", "add corresponding components",
      ["multiply all the components", "add only the magnitudes", "add all three components to the first component"],
      "Addition, subtraction, and scalar multiplication are all performed componentwise."),
])

T("sv.dist", C1, "1.3", "Distance Between Two Points in Space", "procedural",
  "The distance between two spatial points is the magnitude of the vector joining them, found by taking the square root of the sum of the squared coordinate differences.",
  ["Calculate the distance between two points from coordinate differences", "Know that the distance formula follows from the Pythagorean theorem"],
  "GA.14", "inferred", "Distance is a direct application of coordinate operations. Needs verification.")
Qs("sv.dist", [
    n("A(0，0，0), B(2，3，6). What is the length of AB?", "isqrt(4+9+36)",
      "√(4+9+36)=√49=7."),
    n("A(1，2，2), B(1，6，2). What is the length of AB?", "isqrt(0+16+0)",
      "Only the y-coordinates differ, by 4, so the distance is 4."),
    n("A(1，1，1), B(2，2，2). What is the square of the length of AB?", "1+1+1",
      "All three coordinate differences are 1, so the squared distance is 3."),
    c("Which theorem underlies the distance formula for two points in space?", "the Pythagorean theorem",
      ["the angle sum of a triangle", "the intercept theorem for parallel lines", "the inscribed-angle theorem"],
      "The three mutually perpendicular coordinate differences form a right-angle relationship, so the distance follows from the Pythagorean theorem."),
])

T("sv.dir", C1, "1.4", "Direction Vector of a Line", "conceptual",
  "Any nonzero vector parallel to a line is a direction vector for that line; a line has more than one direction vector.",
  ["Find a direction vector from two points on a line", "Know that multiplying a direction vector by a nonzero real number gives another direction vector"],
  "GA.15")
Qs("sv.dir", [
    n("A line passes through A(1，2，3) and B(4，6，3). What is the x-coordinate of a direction vector?", "4-1",
      "AB=(3，4，0), so its x-coordinate is 3."),
    c("d is a direction vector of line l. Which of the following must also be a direction vector of l?", "3d",
      ["the zero vector", "a nonzero vector perpendicular to d", "a vector with magnitude 0"],
      "Multiplying a direction vector by a nonzero real number preserves its parallel direction. The zero vector cannot be a direction vector."),
    n("Direction vector d=(2，−2，4). For the collinear vector (1，−1，k), what is k?", "2",
      "(2，−2，4)=2(1，−1，2), so k=2."),
    c("Does a line have only one direction vector?", "no; any nonzero multiple works",
      ["yes, it has only one", "yes, it must be a unit vector", "no, but they must be perpendicular"],
      "A line's direction vector is not unique; any nonzero multiple represents the same direction."),
])

T("sv.normal", C1, "1.4", "Normal Vector of a Plane", "conceptual",
  "A nonzero vector perpendicular to a plane is called a normal vector to the plane.",
  ["Explain that a normal vector is perpendicular to two intersecting lines in the plane", "Know that a nonzero multiple of a normal vector is also a normal vector"],
  "GA.15")
Qs("sv.normal", [
    c("What is the relationship between a plane and its normal vector?", "perpendicular",
      ["parallel", "the vector must lie in the plane", "they form a 45-degree angle"],
      "A normal vector is perpendicular to the plane and therefore to every line in the plane."),
    n("n=(1，2，2) is a normal vector to a plane. The in-plane vector a=(2，0，k) is perpendicular to n. What is k?", "-1",
      "The dot product is 1×2+2×0+2k=0, so 2+2k=0 and k=−1."),
    n("n=(0，0，3). As a normal vector, what is its dot product with the in-plane vector (1，2，0)?", "0",
      "0×1+0×2+3×0=0, so the vector is indeed perpendicular to the normal."),
    c("n is a normal vector to a plane. Which of the following is also a normal vector to that plane?", "−2n",
      ["the zero vector", "a nonzero direction vector of a line in the plane", "a nonzero vector perpendicular to n"],
      "Any nonzero multiple of a normal vector is still perpendicular to the plane. A direction vector within the plane is parallel to the plane, not a normal."),
])

T("sv.lpar", C1, "1.4", "Using Vectors to Test Line-Plane Parallelism", "reasoning",
  "If a line's direction vector is perpendicular to a plane's normal vector and the line is not in the plane, the line is parallel to the plane.",
  ["Use the dot product of a direction vector and a normal vector to test line-plane parallelism", "Distinguish a parallel line from a line contained in the plane"],
  "GA.15", "inferred", NOTE)
Qs("sv.lpar", [
    n("Direction vector d=(1，−1，0), normal vector n=(1，1，1). What is d·n?", "1*1+(-1)*1+0*1",
      "1−1+0=0, so the direction vector is perpendicular to the normal vector."),
    c("A line is not in a plane, and the dot product of its direction vector and the plane's normal vector is 0. What is their relationship?", "the line is parallel to the plane",
      ["they intersect", "the line must lie in the plane", "the line is perpendicular to the plane"],
      "The direction vector is perpendicular to the normal, and the line is not in the plane, so it is parallel to the plane."),
    n("d=(2，1，k), n=(1，−2，2), and d·n=0. What is k?", "0",
      "2×1+1×(−2)+2k=0, so 2−2+2k=0 and k=0."),
    c("What happens when the dot product of a line's direction vector and a plane's normal vector is not 0?", "the line intersects the plane",
      ["the line must be parallel to the plane", "the line must coincide with the plane", "the line cannot have any point in common with the plane"],
      "The line's direction is not perpendicular to the normal, so the line passes through the plane and intersects it."),
])

T("sv.ppar", C1, "1.4", "Using Vectors to Test Plane-Plane Parallelism", "reasoning",
  "If two planes' normal vectors are collinear, the planes are parallel or coincident.",
  ["Use whether normal vectors are collinear to test plane-plane parallelism", "Know that collinear normals still require checking whether the planes coincide"],
  "GA.15", "inferred", NOTE)
Qs("sv.ppar", [
    n("n1=(1，−2，2), n2=(2，−4，4). What multiple of n1 is n2?", "2",
      "Each component is twice as large, so the normal vectors are collinear."),
    c("Two distinct planes have collinear normal vectors. What is their relationship?", "they are parallel",
      ["they are perpendicular", "they intersect at 60 degrees", "they must coincide"],
      "Collinear normals mean the planes have the same orientation. Since they are distinct, they are parallel."),
    n("n1=(1，0，−1), n2=(k，0，−3) are collinear, and k>0. What is k?", "3",
      "From the third component, n2=3n1, so k=3."),
    c("What happens if two planes' normal vectors are not collinear?", "the planes intersect",
      ["they must be parallel", "they must coincide", "they must be perpendicular"],
      "Noncollinear normal vectors mean the planes have different orientations, so they intersect. To determine whether they are perpendicular, also check whether the dot product is 0."),
])

T("sv.lperp", C1, "1.4", "Using Vectors to Test Line-Plane Perpendicularity", "reasoning",
  "A line is perpendicular to a plane when its direction vector is collinear with the plane's normal vector.",
  ["Determine whether a direction vector and a normal vector are collinear", "Express the proportional relationship between a line's direction vector and a plane's normal when they are perpendicular"],
  "GA.15", "inferred", NOTE)
Qs("sv.lperp", [
    n("A line has direction vector d=(2，−2，4), and a plane has normal vector n=(1，−1，2). What multiple of n is d?", "2",
      "d=2n, so the vectors are collinear and the line is perpendicular to the plane."),
    c("A line's direction vector is collinear with a plane's normal vector. What is their relationship?", "the line is perpendicular to the plane",
      ["the line is parallel to the plane", "the line lies in the plane", "the line is neither perpendicular nor intersecting"],
      "If the line's direction is the same as or opposite to the normal, the line is perpendicular to the plane."),
    n("d=(1，k，2) and n=(2，4，4) are collinear. What is k?", "2",
      "d=(1/2)n, so k=4×(1/2)=2."),
    c("When a line is perpendicular to a plane, must its direction vector be a unit vector?", "no",
      ["yes", "yes, it must have magnitude 2", "yes, it must be the zero vector"],
      "Collinearity is sufficient; the direction vector does not need to have magnitude 1."),
])

T("sv.pperp", C1, "1.4", "Using Vectors to Test Plane-Plane Perpendicularity", "reasoning",
  "Two planes are perpendicular when their normal vectors are perpendicular.",
  ["Use the dot product of normal vectors to test plane-plane perpendicularity", "Convert plane-plane perpendicularity into perpendicularity of the normal vectors"],
  "GA.15", "inferred", NOTE)
Qs("sv.pperp", [
    n("n1=(1，0，1), n2=(1，2，−1). What is n1·n2?", "1*1+0*2+1*(-1)",
      "1+0−1=0, so the normal vectors and the planes are perpendicular."),
    c("Two planes have normal vectors with a dot product of 0. What is the relationship between the planes?", "they are perpendicular",
      ["they are parallel", "they coincide", "it cannot be determined"],
      "Perpendicular normal vectors correspond to perpendicular planes."),
    n("n1=(2，1，0), n2=(1，k，3), and n1·n2=0. What is k?", "-2",
      "2×1+1×k+0×3=0, so k=−2."),
    c("To test whether two planes are perpendicular, which vectors do you check?", "the two planes' normal vectors",
      ["one direction vector from each plane, which must be parallel", "any vectors in the two planes", "vectors from the origin to the planes"],
      "Use the normal vectors: if they are perpendicular, the planes are perpendicular."),
])

T("sv.ang", C1, "1.4", "Angles in Space", "procedural",
  "Angles between skew or intersecting lines, and the angle between a line and a plane, can be determined using direction vectors and normal vectors.",
  ["Use the dot product of direction vectors to analyze the angle between lines", "Know that the sine of the angle between a line and a plane depends on its direction vector and the plane's normal vector"],
  "GA.15", "inferred", NOTE)
Qs("sv.ang", [
    n("Two lines have direction vectors d1=(1，0，0) and d2=(0，1，0). What is d1·d2?", "0",
      "The dot product is 0, so the line directions are perpendicular and the angle is 90 degrees."),
    c("If the dot product of two line direction vectors is positive, what is the acute angle between the lines?", "acute",
      ["right", "obtuse", "0 degrees"],
      "The angle between lines is usually taken to be no greater than 90 degrees. A positive dot product means this angle is acute."),
    n("d=(0，3，4), n=(0，0，1). What is d·n?", "4",
      "0×0+3×0+4×1=4. For the line-plane angle, divide by both magnitudes as well; this question asks only for the dot product."),
    c("To find the angle between two skew lines, what should you identify first?", "a direction vector for each line",
      ["any two plane normals, ignoring their directions", "the midpoints of the two lines", "a zero vector perpendicular to both lines"],
      "Direction vectors determine the directions of the lines, and the angle is determined by these vectors."),
])

T("sv.dih", C1, "1.4", "Dihedral Angles", "procedural",
  "A dihedral angle can be measured using the angle between normal vectors; take care to identify which sides of the planes form the interior of the dihedral angle.",
  ["Write normal vectors for the two half-planes", "Know that the plane angle of a dihedral angle equals or supplements the angle between the normal vectors"],
  "GA.15", "inferred", "The compulsory course does not require dihedral-angle calculations; the selective-compulsory course measures them with vectors. Needs verification.")
Qs("sv.dih", [
    n("Two half-planes have normal vectors n1=(1，0，0) and n2=(0，1，0). What is n1·n2?", "0",
      "The dot product is 0, so the normal vectors are perpendicular."),
    c("When using normal vectors to find a dihedral angle, how might the angle between the normals relate to the plane angle of the dihedral angle?", "they may be equal or supplementary",
      ["they always differ by 45 degrees", "they are always unrelated", "they are always both 0 degrees"],
      "Depending on which side each normal points toward, the angle between the normals may equal the dihedral angle or be its supplement."),
    n("n1=(0，0，1), n2=(0，0，5). What is n1·n2?", "5",
      "0+0+1×5=5. Both normal vectors point along the z-axis in the same direction."),
    c("What kind of angle is a dihedral angle?", "the angle between two half-planes",
      ["the distance between two skew lines", "the distance from a point to a plane", "a central angle of a circle"],
      "A dihedral angle is formed by an edge and two half-planes that meet along the edge."),
])

T("sv.pdist", C1, "1.4", "Distance from a Point to a Plane", "procedural",
  "The distance from a point to the plane ax+by+cz+d=0 is the absolute value obtained by substituting the point, divided by the magnitude of the normal vector.",
  ["Use the point-to-plane distance formula", "Know that the numerator is an absolute value and the denominator is the normal vector's magnitude"],
  "GA.15", "inferred", NOTE)
Qs("sv.pdist", [
    n("What is the distance from point (1，1，1) to the plane x+2y+2z−6=0?",
      "Fraction(abs(1+2*1+2*1-6), isqrt(1+4+4))",
      "The numerator is |1+2+2−6|=1, and the denominator is √(1+4+4)=3, so the distance is 1/3."),
    n("What is the distance from the origin to the plane x+2y+2z−6=0?",
      "Fraction(abs(0+0+0-6), isqrt(1+4+4))",
      "The numerator is 6 and the denominator is 3, so the distance is 2."),
    n("What is the magnitude of the normal vector (2，−1，2) to the plane 2x−y+2z+3=0?", "isqrt(4+1+4)",
      "√(4+1+4)=√9=3, which is the denominator of the distance formula."),
    c("What is the distance from a point on a plane to the plane?", "0",
      ["the magnitude of the normal vector", "1", "it cannot be calculated"],
      "A point on the plane satisfies its equation, so the numerator and distance are 0."),
])

T("sv.use", C1, "1.4", "Using Vectors to Solve Simple Solid-Geometry Problems", "application",
  "Express parallelism, perpendicularity, and distance as vector conditions, then use coordinate calculations in place of some geometric proofs.",
  ["Express a solid-geometry condition as a vector equation", "Use coordinate results to show parallelism or perpendicularity"],
  "GA.15", "inferred", NOTE)
Qs("sv.use", [
    n("In a cuboid, one edge has direction vector (4，0，0) and another has direction vector (0，3，0). What is their dot product?", "0",
      "4×0+0×3+0×0=0, so the edges are perpendicular."),
    n("What is the distance from point (0，0，2) to the plane z=0?", "2",
      "The plane z=0 is the xy-plane, so the point's height gives the distance, 2."),
    c("To prove that a line is parallel to a plane using vectors, what should you show about the direction vector and normal vector?", "their dot product is 0",
      ["their dot product is 1", "their magnitudes are equal", "all their coordinates are equal"],
      "A dot product of 0 shows that the direction vector is perpendicular to the normal. Then show that the line is not in the plane to conclude that they are parallel."),
    n("Direction vector d=(1，1，1), normal vector n=(1，−1，0). What is d·n?", "1*1+1*(-1)+1*0",
      "1−1+0=0, so the line is either parallel to the plane or contained in it."),
])

# ---------------------------------------------------------------- Chapter 2

T("ln.ang", C2, "2.1", "Angle of Inclination of a Line", "conceptual",
  "The angle of inclination is the smallest nonnegative angle from the positive x-axis to the upward direction of a line; it ranges from 0 degrees up to, but not including, 180 degrees.",
  ["State the range of an angle of inclination", "Distinguish the angle of inclination from the other angle a line makes with the x-axis"],
  "GA.16")
Qs("ln.ang", [
    c("What is the range of an angle of inclination?", "at least 0 degrees and less than 180 degrees",
      ["at least 0 and at most 90 degrees", "greater than 0 and less than 360 degrees", "any real number"],
      "The angle of inclination is the smallest nonnegative angle from the positive x-axis to the upward direction of a line, so its range is [0，180) degrees."),
    c("What is the angle of inclination of a line parallel to the x-axis and pointing right?", "0 degrees",
      ["90 degrees", "180 degrees", "45 degrees"],
      "The line points in the same direction as the positive x-axis, so its angle of inclination is 0 degrees."),
    n("A line has an angle of inclination of 90 degrees. What angle does it make with the y-axis?", "0",
      "A line with a 90-degree angle of inclination is perpendicular to the x-axis and points in the y-axis direction, so the angle is 0 degrees."),
    c("A line has an angle of inclination of 120 degrees. How does it look from left to right?", "it slopes downward",
      ["it slopes upward", "it is parallel to the x-axis", "it is parallel to the y-axis"],
      "When the angle of inclination is greater than 90 and less than 180 degrees, the line slopes downward from left to right."),
])

T("ln.slope", C2, "2.1", "Slope of a Line", "conceptual",
  "The slope is the tangent of the angle of inclination. When the angle is 90 degrees, the line is perpendicular to the x-axis and its slope is undefined.",
  ["State that slope is the tangent of the angle of inclination", "Know that a line perpendicular to the x-axis has an undefined slope"],
  "GA.16")
Qs("ln.slope", [
    c("When a line has a defined slope, what is it equal to?", "the tangent of its angle of inclination",
      ["the sine of its angle of inclination", "its angle of inclination itself", "the cosine of its angle of inclination"],
      "The slope is k=tanα, where α is the angle of inclination."),
    c("What is the slope of a line perpendicular to the x-axis?", "undefined",
      ["0", "1", "−1"],
      "The angle of inclination is 90 degrees, and its tangent is undefined, so the slope is undefined."),
    n("A line slopes upward from left to right and passes through two points where x increases by 2 and y increases by 2. What is its slope?", "Fraction(2,2)",
      "Slope equals the change in y divided by the change in x: 2/2=1."),
    c("How is a line with slope 0 positioned relative to the x-axis?", "parallel to or coincident with it",
      ["perpendicular", "at a 45-degree angle", "its slope is undefined"],
      "A slope of 0 means the angle of inclination is 0 degrees, so the line is parallel to the x-axis."),
])

T("ln.two", C2, "2.1", "Slope Formula Through Two Points", "procedural",
  "For a line through distinct points (x1，y1) and (x2，y2), if x1≠x2 its slope is (y2−y1)/(x2−x1).",
  ["Find a line's slope from two points", "Know that the line through two points with the same x-coordinate has undefined slope"],
  "GA.16", "inferred", NOTE)
Qs("ln.two", [
    n("What is the slope of the line through (1，1) and (4，7)?", "Fraction(7-1, 4-1)",
      "(7−1)/(4−1)=6/3=2."),
    n("What is the slope of the line through (0，2) and (3，−4)?", "Fraction(-4-2, 3-0)",
      "(−4−2)/(3−0)=−6/3=−2."),
    c("What is the slope of the line through (2，1) and (2，5)?", "undefined",
      ["0", "2", "4"],
      "The points have the same x-coordinate, so the line is perpendicular to the x-axis and its slope is undefined."),
    n("What is the slope of the line through (−1，3) and (3，3)?", "Fraction(3-3, 3-(-1))",
      "The y-coordinate does not change, so the slope is 0."),
])

T("ln.par", C2, "2.1", "Using Slope to Test Parallelism and Perpendicularity", "reasoning",
  "For two lines with defined slopes, equal slopes imply parallel lines, and a product of slopes equal to −1 implies perpendicular lines.",
  ["Use slope to determine whether lines are parallel", "Use the product of slopes to determine whether lines are perpendicular"],
  "GA.16", "inferred", NOTE)
Qs("ln.par", [
    c("Two distinct lines both have slope 3. What is their relationship?", "parallel",
      ["perpendicular", "they must coincide", "they intersect at 60 degrees"],
      "Both slopes are defined and equal, so the lines are parallel. The problem states that they are distinct."),
    n("One line has slope 2. A perpendicular line has a defined slope. What is its slope?", "Fraction(-1,2)",
      "The product of perpendicular lines' slopes is −1, so the other slope is −1/2."),
    c("One line has undefined slope and another has slope 0. What is their relationship?", "perpendicular",
      ["parallel", "coincident", "cannot be determined"],
      "The line with undefined slope is perpendicular to the x-axis, while the line with slope 0 is parallel to it, so they are perpendicular."),
    n("Line l1 has slope −3, and l2 is parallel to l1. What is the slope of l2?", "-3",
      "Parallel lines with defined slopes have equal slopes, so the slope remains −3."),
])

T("ln.ps", C2, "2.2", "Point-Slope Form of a Line", "procedural",
  "A line through (x0，y0) with slope k can be written as y−y0=k(x−x0).",
  ["Write the point-slope form from a point and slope", "Read a line's slope and a point on it from point-slope form"],
  "GA.17")
Qs("ln.ps", [
    n("A line passes through (1，2) and has slope 3. What is its y-intercept?", "2+3*(0-1)",
      "y−2=3(x−1). When x=0, y=2−3=−1."),
    n("What is the slope of the line y−4=2(x−1)?", "2",
      "In point-slope form, the coefficient of (x−1) is the slope, 2."),
    n("A line passes through (0，−1) and has slope −2. What is y when x=3?", "-1+(-2)*(3-0)",
      "y+1=−2(x−0); when x=3, y=−1−6=−7."),
    c("Which line cannot be represented directly in point-slope form?", "a line perpendicular to the x-axis, with undefined slope",
      ["a line with slope 0", "a line through the origin with slope 1", "a line with slope −1"],
      "Point-slope form requires a defined slope. A line perpendicular to the x-axis has undefined slope and should be written as x=x0."),
])

T("ln.intc", C2, "2.2", "Intercept Form of a Line", "procedural",
  "A line with nonzero intercepts a and b on the coordinate axes, at (a，0) and (0，b), can be written as x/a+y/b=1.",
  ["Read the x- and y-intercepts from intercept form", "Know that a line through the origin cannot be written in intercept form"],
  "GA.17", "inferred", "Intercept form is one way of writing the two-point form. Needs verification.")
Qs("ln.intc", [
    n("What is the y-intercept of the line x/2+y/3=1?", "3",
      "The denominator under y is the y-intercept, 3."),
    n("What is the x-intercept of the line x/4+y/5=1?", "4",
      "The denominator under x is the x-intercept, 4."),
    c("Can a line through the origin be written in intercept form x/a+y/b=1?", "no, at least one of the intercepts is 0",
      ["yes, as long as its slope is 1", "yes, set both a and b to 0", "no, because the origin has no coordinates"],
      "Intercept form requires both intercepts to be nonzero. A line through the origin has at least one intercept equal to 0."),
    n("A line has an x-intercept of 6 and a y-intercept of 2. What is the sum of the intercepts?", "6+2",
      "Its intercept form is x/6+y/2=1, and the sum of the intercepts is 8."),
])

T("ln.gen", C2, "2.2", "General Form of a Line", "procedural",
  "Every line in the plane can be written as Ax+By+C=0, where A and B are not both 0. If B≠0, its slope is −A/B.",
  ["Convert point-slope form to general form", "Find the slope from general form"],
  "GA.17", "inferred", NOTE)
Qs("ln.gen", [
    n("What is the slope of the line 2x−y+4=0?", "2",
      "Rewrite it as y=2x+4; the slope is 2. Alternatively, −A/B=−2/(−1)=2."),
    n("What is the slope of the line x+2y−6=0?", "Fraction(-1,2)",
      "Rewrite it as y=−x/2+3; the slope is −1/2."),
    n("What is the y-coordinate of the intersection of 3x+4y−12=0 with the y-axis?", "3",
      "When x=0, 4y=12, so y=3."),
    c("For Ax+By+C=0 to represent a line, what must be true of A and B?", "they cannot both be 0",
      ["they must both equal 1", "A must equal B", "C must equal 0"],
      "If A and B are both 0, the equation is no longer a first-degree equation in x and y and cannot represent a line."),
])

T("ln.ix", C2, "2.3", "Intersection of Two Lines", "procedural",
  "The coordinates of the intersection of two lines are the common solution to their equations.",
  ["Solve two linear equations simultaneously to find an intersection", "Know that equal slopes do not give a unique intersection"],
  "GA.18")
Qs("ln.ix", [
    n("What is the x-coordinate of the intersection of x+y=5 and x−y=1?", "solve2(1,1,5,1,-1,1)[0]",
      "Adding the equations gives 2x=6, so x=3. The y-coordinate is 2."),
    n("What is the y-coordinate of the intersection of x+y=5 and x−y=1?", "solve2(1,1,5,1,-1,1)[1]",
      "Subtracting the equations gives 2y=4, so y=2."),
    n("What is the x-coordinate of the intersection of y=2x and y=x+3?", "3",
      "2x=x+3, so x=3 and y=6."),
    c("How many intersection points do two distinct lines with the same defined slope have?", "0",
      ["exactly 1", "exactly 2", "infinitely many"],
      "Distinct lines with equal slopes are parallel and have no intersection."),
])

T("ln.d2", C2, "2.3", "Distance Between Two Points", "procedural",
  "The distance between two points in the plane is the square root of the sum of the squared differences in their x- and y-coordinates.",
  ["Calculate distance using the two-point distance formula", "Know that the formula follows from the Pythagorean theorem"],
  "GA.18")
Qs("ln.d2", [
    n("What is the distance between (1，2) and (4，6)?", "isqrt((4-1)**2+(6-2)**2)",
      "The x-difference is 3 and the y-difference is 4, so the distance is √(9+16)=5."),
    n("What is the distance between (0，0) and (5，12)?", "isqrt(25+144)",
      "√(25+144)=√169=13."),
    n("What is the distance between (−1，2) and (2，2)?", "isqrt((2-(-1))**2+(2-2)**2)",
      "The y-coordinates are equal, so the distance is the absolute x-coordinate difference, 3."),
    c("Which theorem directly underlies the distance formula between two points?", "the Pythagorean theorem",
      ["the law of sines", "the secant-secant theorem", "the midsegment theorem"],
      "The x- and y-coordinate differences are the legs of a right triangle, and the distance is its hypotenuse."),
])

T("ln.dpl", C2, "2.3", "Distance from a Point to a Line", "procedural",
  "The distance from point (x0，y0) to line Ax+By+C=0 is |Ax0+By0+C| divided by √(A²+B²).",
  ["Apply the point-to-line distance formula", "Know that the distance is 0 when the point lies on the line"],
  "GA.18")
Qs("ln.dpl", [
    n("What is the distance from the origin to the line 3x+4y−10=0?",
      "Fraction(abs(3*0+4*0-10), isqrt(9+16))",
      "The numerator is 10 and the denominator is 5, so the distance is 2."),
    n("What is the distance from point (1，1) to the line x+y−2=0?",
      "Fraction(abs(1+1-2), isqrt(1+1))",
      "The numerator is 0 because the point lies on the line, so the distance is 0."),
    n("What is the absolute value of the numerator in the distance from (1，2) to x−y+1=0?", "abs(1-2+1)",
      "Substitution gives |1−2+1|=0. The denominator is √2, so the distance is 0."),
    c("What is the distance from a point on a line to the line?", "0",
      ["1", "the slope of the line", "the formula cannot be used"],
      "The point satisfies the line equation, so the numerator and distance are 0."),
])

T("ln.dpp", C2, "2.3", "Distance Between Parallel Lines", "procedural",
  "The distance between parallel lines Ax+By+C1=0 and Ax+By+C2=0 is |C1−C2| divided by √(A²+B²).",
  ["Write parallel lines in general form with the same A and B", "Calculate the distance between parallel lines"],
  "GA.18", "inferred", NOTE)
Qs("ln.dpp", [
    n("What is the distance between the parallel lines 3x+4y−1=0 and 3x+4y−11=0?",
      "Fraction(abs(-1-(-11)), isqrt(9+16))",
      "The numerator is |−1+11|=10 and the denominator is 5, so the distance is 2."),
    n("For the parallel lines x−y+1=0 and x−y−3=0, what is the numerator |C1−C2|?", "abs(1-(-3))",
      "The constant terms are 1 and −3, so their absolute difference is 4."),
    c("Can the distance between two nonparallel lines be discussed?", "no; intersecting lines do not have a constant distance",
      ["yes; use the parallel-line formula", "yes; the distance is always 0", "yes; the distance is always 1"],
      "Only the distance from points on one parallel line to the other line is constant."),
    n("What is the distance between the parallel lines 5x+12y+1=0 and 5x+12y−25=0?",
      "Fraction(abs(1-(-25)), isqrt(25+144))",
      "The numerator is 26 and the denominator is 13, so the distance is 2."),
])

# ---------------------------------------------------------------- Circles

T("cir.std", C2, "2.4", "Standard Equation of a Circle", "procedural",
  "A circle with center (a，b) and radius r has equation (x−a)²+(y−b)²=r².",
  ["Write the standard equation from the center and radius", "Read the center and radius from the standard equation"],
  "GA.19")
Qs("cir.std", [
    n("What is the radius of the circle (x−2)²+(y+1)²=25?", "isqrt(25)",
      "The right side is the square of the radius, 25, so the radius is 5."),
    n("What is the x-coordinate of the center of the circle (x−2)²+(y+1)²=25?", "2",
      "In the standard form (x−a)², a is the x-coordinate of the center; here it is 2."),
    n("A circle has center (0，0) and radius 6. What number appears on the right side of its equation?", "6*6",
      "Its equation is x²+y²=36, where the right side 36 is the square of the radius."),
    c("Does the point (5，0) lie on the circle x²+y²=25?", "it lies on the circle",
      ["it lies inside the circle", "it lies outside the circle", "it is the center"],
      "5²+0²=25, so the point satisfies the equation and lies on the circle."),
])

T("cir.gen", C2, "2.4", "General Equation of a Circle", "procedural",
  "The equation x²+y²+Dx+Ey+F=0 represents a circle when D²+E²−4F>0; its center is (−D/2，−E/2).",
  ["Complete the square to find the center and radius", "Determine whether a general equation represents a circle"],
  "GA.19", "inferred", NOTE)
Qs("cir.gen", [
    n("What is the radius of the circle x²+y²−4x+2y−4=0?", "isqrt((4//2)**2+(2//2)**2-(-4))",
      "Completing the square gives (x−2)²+(y+1)²=9, so the radius is 3."),
    n("What is the x-coordinate of the center of the circle x²+y²−4x+2y−4=0?", "4//2",
      "D=−4, so the x-coordinate of the center is −D/2=2."),
    n("For x²+y²+2x+2y+2=0, what is D²+E²−4F?", "4+4-4*2",
      "D=2, E=2, F=2, so 4+4−8=0. The equation represents a single point, not an ordinary circle."),
    c("What condition is needed for x²+y²+Dx+Ey+F=0 to represent a circle with positive radius?", "D²+E²−4F>0",
      ["D²+E²−4F<0", "F must equal 0", "D and E must equal 0"],
      "After completing the square, the right side must be positive for the radius to be positive. If it is 0, the equation represents a point; if negative, it has no real locus."),
])

T("cir.find", C2, "2.4", "Finding a Circle's Equation from Conditions", "reasoning",
  "The center, radius, or points on a circle can determine its equation; undetermined coefficients are often used.",
  ["Write an equation from the center and radius", "Find undetermined coefficients using a point on the circle"],
  "GA.19", "inferred", NOTE)
Qs("cir.find", [
    n("A circle is centered at the origin and passes through (3，4). What is its radius?", "isqrt(9+16)",
      "The distance from the origin to (3，4) is 5, so the radius is 5."),
    n("The circle (x−1)²+(y−2)²=r² passes through (1，5). What is r²?", "(1-1)**2+(5-2)**2",
      "Substituting the point gives r²=0+9=9."),
    n("A circle has center (2，0) and radius 5. What is the x-coordinate of its intersection with the positive x-axis?", "2+5",
      "The center is on the x-axis, so the right-hand intersection has x-coordinate 2+5=7."),
    c("Which set of information is sufficient to determine a circle?", "its center and radius",
      ["only its center", "only its radius", "only one point on the circle"],
      "The center determines the position and the radius determines the size; both are needed to determine the circle."),
])

T("lc.pos", C2, "2.5", "Relative Positions of a Line and a Circle", "reasoning",
  "Compare the distance d from the center to the line with the radius r: if d<r they intersect, if d=r they are tangent, and if d>r they are disjoint.",
  ["Calculate the distance from the center to a line", "Determine the relative position by comparing d and r"],
  "GA.20")
Qs("lc.pos", [
    n("For the circle x²+y²=25 and the line x=3, what is the distance from the center to the line?", "3",
      "The center is the origin, which is 3 units from x=3."),
    c("For the circle x²+y²=25 and the line x=3, what is their relative position?", "they intersect",
      ["they are tangent", "they are disjoint", "the line passes through the center"],
      "d=3 and r=5, so d<r and the line intersects the circle at two points."),
    n("For the circle x²+y²=25 and the line x=5, what is the distance from the center to the line?", "5",
      "The distance equals the radius 5, so the line is tangent to the circle."),
    c("What is the relationship between a circle and a line when the distance from the center to the line is greater than the radius?", "they are disjoint",
      ["they intersect at two points", "they are tangent", "the line passes through the center"],
      "When d>r, there are no common points, so they are disjoint."),
])

T("lc.chord", C2, "2.5", "Chord Cut by a Line", "procedural",
  "For a radius r and perpendicular distance d from the center to a chord, the half-chord length is √(r²−d²), and the full chord is twice that.",
  ["Find a chord length from the radius and center-to-chord distance", "Know that the chord length is 0 when a line is tangent"],
  "GA.20", "inferred", NOTE)
Qs("lc.chord", [
    n("For the circle x²+y²=25 and the line x=3, what is the chord length?", "2*isqrt(25-9)",
      "The center-to-chord distance is 3, so the half-chord length is √(25−9)=4 and the full chord is 8."),
    n("The radius is 5 and the center-to-chord distance is 4. What is the half-chord length?", "isqrt(25-16)",
      "√(25−16)=3."),
    n("The radius is 13 and the center-to-chord distance is 5. What is the chord length?", "2*isqrt(169-25)",
      "The half-chord length is √(169−25)=√144=12, so the chord length is 24."),
    c("What is the chord length when a line is tangent to a circle?", "0",
      ["the radius", "the diameter", "the center-to-chord distance"],
      "A tangent has only one common point with the circle, so the chord length is 0."),
])

T("cc.pos", C2, "2.5", "Relative Positions of Two Circles", "reasoning",
  "Let the radii be r1 and r2, and the distance between centers be d. If d=r1+r2 the circles are externally tangent; if d=|r1−r2| they are internally tangent; if d lies between these values they intersect.",
  ["Calculate the distance between centers", "Determine the relative position from the center distance and radii"],
  "GA.20", "inferred", NOTE)
Qs("cc.pos", [
    n("Two circles have center distance 5 and radii 3 and 4. How many common points do they have?",
      "2 if abs(3-4)<5<3+4 else (1 if 5==abs(3-4) or 5==3+4 else 0)",
      "|3−4|<5<3+4, so the circles intersect at 2 points."),
    n("Two circles both have radius 3 and their centers are 6 units apart. How many common points do they have?",
      "2 if abs(3-3)<6<3+3 else (1 if 6==abs(3-3) or 6==3+3 else 0)",
      "The center distance equals the sum of the radii, so the circles are externally tangent and have 1 common point."),
    c("What is the relationship between two circles when their centers are farther apart than the sum of their radii?", "they are externally disjoint",
      ["they are externally tangent", "they intersect", "one is inside the other"],
      "The centers are farther apart than the sum of the radii, so the circles have no common points and lie outside one another."),
    n("Two circles have radii 5 and 3 and center distance 2. What is |r1−r2|?", "abs(5-3)",
      "The absolute difference of the radii is 2, equal to the center distance, so the circles are internally tangent."),
])

T("lc.app", C2, "2.5", "Simple Applications of Lines and Circles", "application",
  "Whether a route or pipe intersects a circular region can be modeled as the relative position of a line and a circle.",
  ["Represent a circular region with a circle equation", "Draw a conclusion by comparing the distance and radius"],
  "GA.20", "inferred", NOTE)
Qs("lc.app", [
    n("A circular irrigation area is centered at the origin and has radius 10. A straight pipe follows x=6. What is the distance from the center to the pipe?", "6",
      "The pipe is the line x=6, which is 6 units from the origin. This is less than the radius, so the pipe crosses the irrigation area."),
    n("A circle has radius 10 and a center-to-chord distance of 6. What is the length of the pipe segment inside the circle?", "2*isqrt(100-36)",
      "The half-chord length is √(100−36)=8, so the full chord is 16."),
    c("A circular restricted area has radius 5. A straight road is 5 units from its center. How does the road meet the boundary?", "it is tangent",
      ["it passes through the restricted area", "it is disjoint from the area", "it passes through the center"],
      "The distance equals the radius, so the road is tangent to the circle and has one common point."),
    n("A circle has radius 5 and a chord with center-to-chord distance 3. How much shorter is the chord than the diameter?", "10-2*isqrt(25-9)",
      "The diameter is 10 and the chord is 8, so the difference is 2."),
])

# ---------------------------------------------------------------- Chapter 3

T("el.def", C3, "3.1", "Definition of an Ellipse", "conceptual",
  "An ellipse is the locus of points in a plane for which the sum of the distances to two fixed points is constant and greater than the distance between those points.",
  ["State the sum-of-distances condition in the definition of an ellipse", "Know that the constant must exceed the distance between the foci"],
  "GA.21")
Qs("el.def", [
    c("In the definition of an ellipse, how are a point's distances to the two foci related?", "their sum is a constant greater than the distance between the foci",
      ["their difference is constant", "their product is constant", "their sum equals the distance between the foci"],
      "The sum is constant and must exceed the distance between the foci for the locus to be an ellipse."),
    n("The sum of the distances from any point on an ellipse to its two foci is 10. If this sum is 2a, what is a?", "5",
      "2a=10, so a=5."),
    c("If the sum of the distances equals the distance between the foci, what is the locus?", "the line segment between the foci",
      ["an ellipse", "a hyperbola", "the entire plane"],
      "When the sum equals the focal distance, the point can only lie on the segment between the foci; it does not form an ellipse."),
    n("An ellipse has foci on the x-axis and a=5. What is the sum of the distances from a point on the ellipse to the foci?", "2*5",
      "By definition, the sum is 2a=10."),
])

T("el.eq", C3, "3.1", "Standard Equation of an Ellipse", "procedural",
  "When the foci lie on the x-axis, the standard equation of an ellipse is x²/a²+y²/b²=1, where a>b>0.",
  ["Write the standard equation for an ellipse with foci on the x-axis", "Read a and b from the standard equation"],
  "GA.21")
Qs("el.eq", [
    n("For the ellipse x²/25+y²/16=1, what is a?", "isqrt(25)",
      "The denominator under x² is a²=25, so a=5."),
    n("For the ellipse x²/25+y²/16=1, what is b?", "isqrt(16)",
      "The denominator under y² is b²=16, so b=4."),
    n("If a=3, b=2, and the foci lie on the x-axis, what is a² in the standard equation?", "3*3",
      "The equation is x²/9+y²/4=1, so a²=9."),
    c("Which curve is represented by x²/9+y²/4=1?", "an ellipse with foci on the x-axis",
      ["an ellipse with foci on the y-axis", "a hyperbola", "a parabola"],
      "Both terms are positive and sum to 1. The denominator under x² is larger, so the foci lie on the x-axis."),
])

T("el.abc", C3, "3.1", "Relationship Among a, b, and c for an Ellipse", "reasoning",
  "For an ellipse, c²=a²−b², the focal distance is 2c, and the eccentricity is c/a.",
  ["Find c from a and b", "Calculate eccentricity"],
  "GA.21", "inferred", NOTE)
Qs("el.abc", [
    n("For an ellipse with a=5 and b=4, what is c?", "isqrt(25-16)",
      "c²=a²−b²=25−16=9, so c=3."),
    n("For an ellipse with a=5 and c=3, what is its eccentricity?", "Fraction(3,5)",
      "The eccentricity is e=c/a=3/5."),
    n("For an ellipse with a=13 and b=5, what is the focal distance 2c?", "2*isqrt(169-25)",
      "c²=169−25=144, so c=12 and the focal distance is 24."),
    c("What is the range of an ellipse's eccentricity?", "greater than 0 and less than 1",
      ["greater than 1", "equal to 1", "less than 0"],
      "0<c<a, so 0<e<1. The closer e is to 1, the flatter the ellipse."),
])

T("el.prop", C3, "3.1", "Basic Geometric Properties of an Ellipse", "conceptual",
  "For an ellipse with foci on the x-axis, the major-axis length is 2a, the minor-axis length is 2b, and its bounds are −a≤x≤a and −b≤y≤b.",
  ["State the lengths of the major and minor axes", "Write the bounds of an ellipse"],
  "GA.21", "inferred", NOTE)
Qs("el.prop", [
    n("What is the major-axis length of the ellipse x²/25+y²/9=1?", "2*5",
      "a=5, so the major-axis length is 2a=10."),
    n("What is the minor-axis length of the ellipse x²/25+y²/9=1?", "2*3",
      "b=3, so the minor-axis length is 2b=6."),
    n("What is the greatest x-coordinate of a point on the ellipse x²/25+y²/9=1?", "5",
      "The range of x is −5 to 5, so the greatest x-coordinate is 5."),
    c("For an ellipse with foci on the x-axis, where is the major axis?", "on the x-axis",
      ["on the y-axis", "on the line y=x", "on any line"],
      "The major axis lies along the axis containing the foci; here it is the x-axis."),
])

T("el.app", C3, "3.1", "Simple Applications of Ellipses", "application",
  "Planetary orbits and elliptical fields can be described using the semimajor axis, semiminor axis, and sum of distances.",
  ["Interpret the sum of distances as 2a", "Find the distance from the center to a focus using a and b"],
  "GA.21", "inferred", NOTE)
Qs("el.app", [
    n("An elliptical track has semimajor axis 5 and semiminor axis 4. What is the sum of the distances from a point on the track to the two foci?", "2*5",
      "By definition, the sum of the distances is 2a=10."),
    n("An ellipse has semimajor axis 5 and semiminor axis 4. What is the distance from its center to a focus?", "isqrt(25-16)",
      "c=√(25−16)=3."),
    n("An elliptical lens has a=10 and b=8. What is c, the numerator of its eccentricity?", "isqrt(100-64)",
      "c=√(100−64)=√36=6."),
    c("When an ellipse is used to model a planetary orbit, where is the Sun usually located?", "at one focus",
      ["at an endpoint of the major axis", "at an endpoint of the minor axis", "outside the ellipse"],
      "This is a common application of the ellipse definition: the sum of distances to the two foci is constant, and the Sun lies at one focus."),
])

T("hy.def", C3, "3.2", "Definition of a Hyperbola", "conceptual",
  "A hyperbola is the locus of points in a plane for which the absolute difference of the distances to two fixed points is constant and less than the distance between those points.",
  ["State that a hyperbola is defined using a difference of distances", "Know that the constant must be less than the focal distance"],
  "GA.22")
Qs("hy.def", [
    c("In the definition of a hyperbola, what is compared for a point's distances to the two foci?", "their absolute difference",
      ["their sum", "their product", "their quotient"],
      "A hyperbola has a constant absolute difference of distances; an ellipse has a constant sum."),
    n("For a point on a hyperbola, the absolute difference of its distances to the foci is 6. If 2a=6, what is a?", "3",
      "The constant is 2a, so a=3."),
    c("If the absolute difference of the distances equals the distance between the foci, what is the locus?", "two rays",
      ["a hyperbola", "an ellipse", "a circle"],
      "When the absolute difference equals the focal distance, the points lie on the extensions of the line segment between the foci, forming two rays."),
    n("A hyperbola has a=4. What is the constant in its definition?", "2*4",
      "The constant is 2a=8."),
])

T("hy.eq", C3, "3.2", "Standard Equation of a Hyperbola", "procedural",
  "When the foci lie on the x-axis, the standard equation of a hyperbola is x²/a²−y²/b²=1.",
  ["Write the standard equation for a hyperbola with foci on the x-axis", "Distinguish an ellipse from a hyperbola by its equation"],
  "GA.22", "inferred", NOTE)
Qs("hy.eq", [
    n("For the hyperbola x²/9−y²/16=1, what is a?", "isqrt(9)",
      "The denominator under x² is a²=9, so a=3."),
    n("For the hyperbola x²/9−y²/16=1, what is b²?", "16",
      "The denominator of the y² term is b²=16."),
    c("Which curve is represented by x²/4−y²/9=1?", "a hyperbola with foci on the x-axis",
      ["an ellipse", "a hyperbola with foci on the y-axis", "a parabola"],
      "The terms are subtracted and the equation equals 1. The x² term comes first, so the foci lie on the x-axis."),
    n("If a=5 and b=12, what is a² in the standard equation?", "25",
      "The equation is x²/25−y²/144=1."),
])

T("hy.prop", C3, "3.2", "Basic Geometric Properties of a Hyperbola", "conceptual",
  "When the foci lie on the x-axis, the transverse-axis length is 2a, the conjugate-axis length is 2b, and c²=a²+b².",
  ["Find c from a and b", "State the lengths of the transverse and conjugate axes"],
  "GA.22", "inferred", NOTE)
Qs("hy.prop", [
    n("For a hyperbola with a=3 and b=4, what is c?", "isqrt(9+16)",
      "For a hyperbola, c²=a²+b²=9+16=25, so c=5."),
    n("For a hyperbola with a=3 and b=4, what is the transverse-axis length?", "2*3",
      "The transverse-axis length is 2a=6."),
    n("For a hyperbola with a=5 and c=13, what is b²?", "13*13-5*5",
      "b²=c²−a²=169−25=144."),
    c("How does the eccentricity c/a of a hyperbola compare with 1?", "greater than 1",
      ["greater than 0 and less than 1", "equal to 1", "less than 0"],
      "c²=a²+b²>a², so c>a and the eccentricity is greater than 1."),
])

T("hy.asym", C3, "3.2", "Asymptotes of a Hyperbola", "conceptual",
  "The asymptotes of x²/a²−y²/b²=1 are y=(b/a)x and y=−(b/a)x.",
  ["Write the equations of the asymptotes", "Find the asymptote slopes from a and b"],
  "GA.22", "inferred", NOTE)
Qs("hy.asym", [
    n("What is the absolute slope of an asymptote of x²/9−y²/16=1?", "Fraction(4,3)",
      "b=4 and a=3, so the absolute slope is b/a=4/3."),
    n("For a hyperbola with a=5 and b=5, what is the absolute slope of its asymptotes?", "Fraction(5,5)",
      "b/a=1, so the asymptotes are y=x and y=−x."),
    c("How many asymptotes does x²/a²−y²/b²=1 have?", "2",
      ["1", "4", "none"],
      "The asymptotes are the two lines y=±(b/a)x."),
    n("A hyperbola has asymptotes y=±2x and a=3. What is b?", "6",
      "b/a=2, so b=6."),
])

T("pa.def", C3, "3.3", "Definition of a Parabola", "conceptual",
  "A parabola is the locus of points in a plane that are equally distant from a fixed point and a fixed line. The point is the focus, and the line is the directrix.",
  ["State the equal-distance condition in the definition of a parabola", "Distinguish the focus from the directrix"],
  "GA.23")
Qs("pa.def", [
    c("Which two distances are compared in the definition of a parabola?", "the distance to the focus and the distance to the directrix",
      ["the sum of the distances to two foci", "the difference of the distances to two foci", "the distance to the center"],
      "A parabola does not have two foci. It is the locus of points equidistant from the focus and the directrix."),
    n("A point on a parabola is 6 units from the focus. How far is it from the directrix?", "6",
      "The definition requires these distances to be equal, so it is also 6 units."),
    c("What kind of figure is the directrix of a parabola?", "a line",
      ["a point", "a circle", "another parabola"],
      "The directrix is a fixed line, and the focus is a fixed point."),
    n("A point is 4 units from the focus and 4 units from the directrix. What is the difference between the distances?", "0",
      "The distances are equal, so their difference is 0; the point can lie on the parabola."),
])

T("pa.eq", C3, "3.3", "Standard Equation of a Parabola", "procedural",
  "A parabola with vertex at the origin and focus on the positive x-axis has equation y²=2px (p>0) and focus (p/2，0).",
  ["Find the focus coordinates from 2p", "Determine the direction in which a parabola opens"],
  "GA.23", "inferred", NOTE)
Qs("pa.eq", [
    n("For the parabola y²=8x, what is the x-coordinate of its focus?", "8//4",
      "2p=8, so p=4 and the focus is (p/2，0)=(2，0)."),
    n("For the parabola y²=4x, what is 2p in its equation?", "4",
      "Comparing with y²=2px gives 2p=4."),
    c("In which direction does y²=4x open?", "to the right",
      ["to the left", "upward", "downward"],
      "y² equals a positive multiple of x, so the focus is on the positive x-axis and the parabola opens to the right."),
    n("A parabola has focus (3，0), vertex at the origin, and opens to the right. What is 2p?", "12",
      "The focus's x-coordinate is p/2=3, so p=6 and 2p=12; the equation is y²=12x."),
])

T("pa.prop", C3, "3.3", "Basic Geometric Properties of a Parabola", "conceptual",
  "For y²=2px (p>0), the range is x≥0, the axis of symmetry is the x-axis, and the directrix is x=−p/2.",
  ["Write the directrix equation", "State the axis of symmetry and range"],
  "GA.23", "inferred", NOTE)
Qs("pa.prop", [
    n("For the parabola y²=8x, what is x in the directrix equation?", "-2",
      "p/2=2, so the directrix is x=−p/2, or x=−2."),
    n("What is the minimum value of x on the parabola y²=4x?", "0",
      "It opens to the right and has vertex at the origin, so x≥0 and its minimum is 0."),
    c("What is the axis of symmetry of y²=2px (p>0)?", "the x-axis",
      ["the y-axis", "the line y=x", "the directrix"],
      "The equation contains y², so it is symmetric about the x-axis."),
    n("What is the distance from the focus to the directrix of y²=12x?", "6",
      "p/2=3, so the focus-to-directrix distance is p=6."),
])

T("pa.app", C3, "3.3", "Simple Applications of Parabolas", "application",
  "Parabolas are often used for the cross-sections of searchlights and satellite dishes; rays parallel to the axis converge at the focus.",
  ["Find the focus from a cross-section equation", "Use the definition to compare distances to the focus and directrix"],
  "GA.23", "inferred", NOTE)
Qs("pa.app", [
    n("A satellite-dish cross-section is y²=16x, with units in meters. What is the distance from the focus to the vertex?", "16//4",
      "2p=16, so p=8 and the focus-to-vertex distance is p/2=4 meters."),
    n("A point on the cross-section y²=16x is 9 meters from the focus. How far is it from the directrix?", "9",
      "The parabola definition guarantees these distances are equal."),
    n("A right-opening parabola has focus (2，0). What is 2p?", "8",
      "p/2=2, so p=4 and 2p=8."),
    c("Where do rays parallel to a parabola's axis of symmetry converge after reflection?", "at the focus",
      ["at the vertex", "at any point on the directrix", "at the center"],
      "This optical property of parabolas is used in simple models of searchlights and satellite dishes."),
])

T("co.sec", C3, "3.3", "Number of Intersections of a Line and an Ellipse", "reasoning",
  "Substitute the line into the ellipse equation. The number of real roots of the resulting quadratic equals the number of intersections of the line and ellipse.",
  ["Substitute a line into an ellipse equation", "Determine the number of intersections from the number of real roots"],
  "GA.21", "inferred", "The curriculum requires studying ellipses with equations and solving simple applications. Counting intersections of a line and ellipse is a basic form of this requirement; harder chord-length problems are not listed separately. Needs verification.")
Qs("co.sec", [
    n("How many intersections are there between the ellipse x²/4+y²/3=1 and the line y=x?", "len(roots2(Fraction(7,12), 0, -1))",
      "Substitution gives (1/4+1/3)x²=1, or 7x²/12=1. There are two real roots, so there are 2 intersections."),
    n("How many intersections are there between the ellipse x²/4+y²/1=1 and the line y=2?", "0",
      "On the ellipse, |y|≤1, so the line y=2 lies above it and has no intersections."),
    n("How many intersections are there between the ellipse x²/4+y²/1=1 and the line y=1?", "1",
      "When y=1, x=0, so there is only one intersection, (0，1); the line is tangent to the ellipse."),
    c("After substituting a line into an ellipse equation, the resulting quadratic has two distinct real roots. What does this mean?", "there are two intersections",
      ["there are no intersections", "there is one intersection", "the line passes through both foci"],
      "Each real root gives the x-coordinate of an intersection. Two distinct real roots mean two intersections."),
])
