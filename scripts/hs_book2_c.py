"""Continuation of required-course Book 2: introduction to solid geometry, statistics, and probability. Imported by hs_book2.py."""
from hs_common import questions, topic

NA = "Number and Algebra"
GG = "Geometry and Measurement"
SP = "Statistics and Probability"
C8 = "Chapter 8: Introduction to Solid Geometry"
C9 = "Chapter 9: Statistics"
C10 = "Chapter 10: Probability"


def T(key, chapter, section, name, domain, typ, desc, crit, std, conf="exact", note=None):
    topic(key, 2, chapter, section, name, domain, typ, desc, crit, std, conf, note)


def Qs(key, items):
    questions(key, items)


def n(prompt, verify, expl):
    return ("n", prompt, verify, expl)


def c(prompt, ok, bad, expl):
    return ("c", prompt, ok, bad, expl)


T("sol.prism", C8, "8.1", "Structure of Prisms", GG, "conceptual",
  "Identify the bases, lateral faces, lateral edges, and vertices of a prism, and count the vertices, edges, and faces of simple prisms.",
  ["Can name the parts of a prism", "Can count the vertices, edges, and faces of a right prism"],
  "GA.08")
Qs("sol.prism", [
    n("How many vertices does a cuboid have?", "8",
      "Each base has 4 vertices, for a total of 8."),
    n("How many edges does a cuboid have?", "12",
      "Each base has 4 edges, plus 4 lateral edges, for a total of 12."),
    n("How many faces does a triangular prism have?", "5",
      "It has 2 bases and 3 lateral faces, for a total of 5."),
    c("The two bases of a prism are?", "parallel and congruent",
      ["always perpendicular", "always rectangles", "not necessarily parallel"],
      "The lateral edges connect the two congruent bases in parallel planes. In a right prism, the lateral edges are also perpendicular to the bases."),
])

T("sol.round", C8, "8.1", "Cylinders, Cones, and Spheres", GG, "conceptual",
  "Name the key elements of cylinders, cones, and spheres, and distinguish them from prisms.",
  ["Can identify a cylinder's generatrix and height", "Can name a sphere's radius"],
  "GA.08", "inferred", "Solids of revolution and prisms are both basic solid figures. Verification pending.")
Qs("sol.round", [
    c("A cylinder can be formed by?", "rotating a rectangle once around one of its sides",
      ["rotating a right triangle once around one leg", "rotating a semicircle once around its diameter", "translating a parallelogram"],
      "Rotating a rectangle around one side forms a cylinder. Rotating a right triangle forms a cone, and rotating a semicircle forms a sphere."),
    n("A cylinder has 2 bases. Counting its lateral surface as one more, what is the value of “number of bases + 1”?", "2+1",
      "There are 2 bases and one curved lateral surface, so 2+1=3."),
    c("The distance from any point on a sphere to its center?", "is equal to the radius",
      ["is sometimes the diameter", "can be any positive number", "is the circumference"],
      "A sphere is the set of points at a fixed distance—the radius—from its center."),
    c("A cone's generatrix is?", "the segment from the vertex to a point on the base circumference",
      ["the diameter of the base", "the altitude, which must equal the radius", "the width of the unfolded lateral surface"],
      "The generatrix lies on the lateral surface; its length is generally not the same as the height."),
])

T("sol.comb", C8, "8.1", "Simple Composite Solids", GG, "procedural",
  "Decompose simple composite solids into prisms, cones, and spheres, and count the visible components.",
  ["Can identify the basic solids in a composite figure", "Can use the quantity of each component separately"],
  "GA.08", "inferred", "Composite solids combine basic solid figures. Verification pending.")
Qs("sol.comb", [
    n("A solid is made by joining 1 cylinder and 1 cone. How many basic solids are there?", "1+1",
      "It separates into two basic solids."),
    n("If a cylinder and a cone both have a base radius of 3, what is their common radius?", "3",
      "The problem gives the common radius as 3."),
    c("To find the volume of a composite solid, usually?", "split it into basic solids and add or subtract their volumes",
      ["use one formula for the whole solid", "count only the largest part", "ignore any concave parts"],
      "There is no single new formula for a composite solid; calculate its components."),
    c("If a small sphere is removed from a large sphere, the remaining volume is?", "the large sphere's volume minus the small sphere's volume",
      ["the sum of the two volumes", "the small sphere's volume only", "the difference of their surface areas"],
      "Removing a part means subtracting its volume, not adding it."),
])

T("sol.oblique", C8, "8.2", "Oblique Projection", GG, "procedural",
  "Know that in an oblique view of a horizontal figure, segments parallel to the horizontal axis keep their length, while segments parallel to the vertical axis are drawn at half length.",
  ["Can identify the direction whose lengths remain unchanged", "Can halve the length of a segment parallel to the vertical axis"],
  "GA.08", "inferred", "Oblique projection is a prescribed method for drawing perspective views. Verification pending.")
Qs("sol.oblique", [
    n("A segment in a horizontal figure is 6 units long and parallel to the horizontal axis. How long is it in the perspective view?", "6",
      "The length of a segment parallel to the horizontal axis is unchanged."),
    n("A segment parallel to the vertical axis is 8 units long. How long is it drawn in an oblique view?", "8/2",
      "A segment parallel to the vertical axis is drawn at half its original length, so it is 4."),
    n("A segment parallel to the vertical axis appears 3 units long in the perspective view. What was its original length?", "3*2",
      "The drawing shows half the original length, so the original length was 6."),
    c("In oblique projection, what is the usual angle between the horizontal and vertical axes?", "45° or 135°",
      ["must be 90°", "must be 30°", "can be 0°"],
      "The axes, originally perpendicular, are not drawn at a right angle in the perspective view; 45° is commonly used."),
])

T("sol.draw", C8, "8.2", "Perspective Views of Horizontal Plane Figures", GG, "procedural",
  "Use oblique-projection rules to find the corresponding length of a segment in a perspective view.",
  ["Can handle horizontal and vertical directions separately", "Can recognize that parallel segments remain parallel in the perspective view"],
  "GA.08", "inferred", "Perspective views are a direct application of oblique projection. Verification pending.")
Qs("sol.draw", [
    n("A square with side length 4 lies in a horizontal plane, with one side parallel to the horizontal axis. What is that side's length in the perspective view?", "4",
      "It is parallel to the horizontal axis, so its length remains 4."),
    n("What is the perspective-view length of the square's perpendicular side?", "4/2",
      "The side parallel to the vertical axis is drawn at half length, so it is 2."),
    c("Segments that are parallel in the original figure are, in an oblique view?", "still parallel",
      ["perpendicular", "always equal in length", "not drawable"],
      "Oblique projection preserves parallelism, but halves lengths in the vertical direction."),
    n("Two segments parallel to the horizontal axis in a perspective view were originally 5 units each. What is the sum of their lengths in the view?", "5+5",
      "Neither length changes, so their sum is 10."),
])

T("sol.area", C8, "8.3", "Surface Areas of Simple Solids", GG, "procedural",
  "Calculate the surface areas of prisms and cubes, and substitute given base areas or unfolded lateral-surface measurements for cylinders and cones.",
  ["Can calculate the surface areas of cubes and cuboids", "Can substitute measurements from an unfolded curved surface into a formula"],
  "GA.09")
Qs("sol.area", [
    n("What is the surface area of a cube with edge length 3?", "6*3**2",
      "It has 6 faces, each with area 9, so the surface area is 54."),
    n("What is the surface area of a cuboid with length 2, width 3, and height 4?", "2*(2*3+3*4+4*2)",
      "2×(6+12+8)=52."),
    n("The lateral surface of a cylinder unfolds into a rectangle. If the base circumference is 10 and the height is 4, what is the lateral surface area?", "10*4",
      "Lateral surface area equals base circumference times height. The circumference is given, so there is no need to calculate π."),
    c("When unfolded, the lateral surface of a cone is a?", "sector", ["rectangle", "two circles", "triangle"],
      "Cut along a generatrix to unfold the lateral surface into a sector. The base is a separate circle."),
])

T("sol.vol", C8, "8.3", "Volumes of Simple Solids", GG, "procedural",
  "Find the volume of a prism by multiplying its base area by its height, and find the volume of a cone using one third of that product.",
  ["Can calculate the volume of a prism or a cylinder with a known base area", "Can calculate the volume of a cone with a known base area and height"],
  "GA.09", "inferred", "Volume and surface area are both measurements of simple solids. Verification pending.")
Qs("sol.vol", [
    n("What is the volume of a prism with base area 20 and height 4?", "20*4",
      "A prism's volume is its base area times its height, or 80."),
    n("What is the volume of a cylinder with base area 10 and height 6?", "10*6",
      "A cylinder is also a prism, so its volume is base area times height. The base area is given."),
    n("What is the volume of a cone with base area 9 and height 3?", "Fraction(1,3)*9*3",
      "A cone's volume is one third the volume of a prism with the same base and height: 9×3/3=9."),
    c("What is the ratio of the volumes of a cone and a cylinder with the same base and height?", "1:3", ["1:2", "1:1", "2:3"],
      "The cone's volume formula includes 1/3; the cylinder's does not."),
])

T("sol.ball", C8, "8.3", "Sphere Volume and Surface Area", GG, "reasoning",
  "Know that a sphere's volume is proportional to the cube of its radius and its surface area to the square of its radius, and compare scale factors for different radii.",
  ["Can find a volume ratio from a radius ratio", "Can find a surface-area ratio from a radius ratio"],
  "GA.09", "inferred", "Sphere measurements are covered with the volume and surface area of simple solids. Numerical questions do not expand formulas involving π. Verification pending.")
Qs("sol.ball", [
    n("If a sphere's radius doubles, by what factor does its volume change?", "2**3",
      "Volume is proportional to the cube of the radius, so 2³=8."),
    n("If a sphere's radius triples, by what factor does its surface area change?", "3**2",
      "Surface area is proportional to the square of the radius, so 3²=9."),
    n("What is the ratio of the volumes of spheres with radii 1 and 2? Divide the larger volume by the smaller one.", "2**3/1**3",
      "8/1=8."),
    c("In the formula for a sphere's volume, the radius is raised to the?", "third power", ["second power", "first power", "radius does not appear"],
      "V=4/3 π r³. This question tests only the exponent, not the decimal value involving π."),
])

T("sol.axiom", C8, "8.4", "Basic Facts About Planes", GG, "conceptual",
  "Understand the basic facts for determining a plane and for the intersection of two planes.",
  ["Can state that three noncollinear points determine a plane", "Can state that two intersecting planes meet in a line"],
  "GA.10")
Qs("sol.axiom", [
    c("How many planes are determined by three points that are not on the same line?", "exactly one",
      ["none", "exactly two", "infinitely many"],
      "Three noncollinear points determine exactly one plane. Three collinear points do not determine a unique plane."),
    c("If two distinct planes have a common point, then?", "they share exactly one line through that point",
      ["that is their only common point", "they must coincide", "they share no line"],
      "Two intersecting planes meet along a line."),
    n("A cuboid has 8 vertices. Choose the 2 endpoints of one edge. Are those two points and the edge's midpoint collinear? Answer 1 if they are, 0 otherwise.", "1",
      "The endpoints and midpoint lie on the same edge, so the three points are collinear."),
    c("A line and a point not on the line determine?", "a unique plane",
      ["a unique line", "two planes", "no plane"],
      "The point and any two points on the line form three noncollinear points, which determine a plane."),
])

T("sol.line", C8, "8.4", "Relative Positions of Lines in Space", GG, "conceptual",
  "Distinguish intersecting, parallel, and skew lines; know that skew lines are neither parallel nor intersecting.",
  ["Can determine whether two lines are coplanar", "Can explain what skew lines are"],
  "GA.10", "inferred", "The relative positions of lines in space are classified after the basic facts. Verification pending.")
Qs("sol.line", [
    c("Skew lines are?", "two lines that do not lie in any one plane",
      ["intersecting lines that are not perpendicular", "parallel lines", "nonintersecting lines in one plane"],
      "Parallel lines are coplanar. Skew lines neither intersect nor run parallel."),
    c("In a cuboid, an edge on the top base and an edge on the bottom base that is not parallel to it and is not on the same lateral face?", "may be skew",
      ["must intersect", "must be parallel", "must coincide"],
      "Edges that are not coplanar and are not parallel are skew lines."),
    n("How many intersection points do two intersecting lines in space have?", "1",
      "Intersecting lines have exactly one common point."),
    c("In space, parallel lines are?", "coplanar and have no common points",
      ["always skew", "always perpendicular", "always intersecting"],
      "By definition, parallel lines lie in one plane and have no common points."),
])

T("sol.pos", C8, "8.4", "Relative Positions of Lines and Planes", GG, "conceptual",
  "Distinguish a line intersecting a plane, parallel to a plane, or lying in it, as well as parallel and intersecting planes.",
  ["Can name the three possible positions of a line and a plane", "Can state that two planes are either parallel or intersecting"],
  "GA.10", "inferred", "The relative positions of lines and planes are covered with those of lines in space. Verification pending.")
Qs("sol.pos", [
    c("How many possible relative positions are there for a line and a plane?", "three: the line lies in the plane, is parallel to it, or intersects it",
      ["only parallel or perpendicular", "only intersecting", "four, including skew"],
      "A line either lies in a plane, is parallel to it, or intersects it. Skewness describes two lines."),
    c("Two distinct planes are?", "parallel or intersecting",
      ["possibly skew", "always perpendicular", "always coincident"],
      "If two distinct planes do not intersect, they are parallel."),
    n("How many common points do a line and a plane have when they intersect?", "1",
      "They intersect at one point. If they shared two points, the line would lie in the plane."),
    c("If two points on a line lie in a plane, then?", "the entire line lies in that plane",
      ["the line is parallel to the plane", "the line has only one intersection with the plane", "the line is perpendicular to the plane"],
      "This follows directly from the basic facts about planes."),
])

T("sol.lpj", C8, "8.5", "Criterion for a Line Parallel to a Plane", GG, "reasoning",
  "Use the criterion that a line outside a plane is parallel to a line in that plane to establish that the line is parallel to the plane.",
  ["Can state the conditions of the criterion", "Can identify a missing condition that makes it inapplicable"],
  "GA.11")
Qs("sol.lpj", [
    c("Line a lies outside a plane and is parallel to line b in the plane. Then?", "a is parallel to the plane",
      ["a intersects the plane", "a also lies in the plane", "a is perpendicular to the plane"],
      "This is the criterion for a line to be parallel to a plane. Line a must lie outside the plane."),
    c("If a is parallel to line b in a plane, but a also lies in that plane, what can be concluded?", "a cannot be said to be parallel to the plane",
      ["it is still parallel to the plane", "it must be perpendicular", "a is skew"],
      "A line in a plane is not parallel to the plane; parallel lines or planes must have no common points."),
    n("How many lines in the plane are needed as a reference for this criterion?", "1",
      "It is enough to have one line in the plane parallel to the given line."),
    c("When a line is parallel to a plane, how many common points do they have?", "0", ["1", "infinitely many", "2"],
      "Parallel means there are no common points."),
])

T("sol.lpp", C8, "8.5", "Property of a Line Parallel to a Plane", GG, "reasoning",
  "Know that if a plane through a given line intersects the known plane, their intersection line is parallel to the given line.",
  ["Can state that the intersection line is parallel to the given line", "Can distinguish a criterion from a property"],
  "GA.11", "inferred", "The property theorem is paired with the criterion theorem. Verification pending.")
Qs("sol.lpp", [
    c("Line a is parallel to plane α. A plane through a intersects α along b. Then?", "a is parallel to b",
      ["a is perpendicular to b", "a intersects b", "a and b are skew"],
      "This is the property of a line parallel to a plane: the intersection line is parallel to the original line."),
    c("What is the difference between a criterion theorem and a property theorem?", "a criterion uses conditions to establish parallelism; a property uses existing parallelism to derive another parallel relationship",
      ["they are exactly the same", "a property is used to draw perspective views", "a criterion applies only to perpendicularity"],
      "Using an established parallel relationship to derive another is a property; using another parallel relationship to establish line-plane parallelism is a criterion."),
    n("How many intersection lines appear in the property theorem?", "1",
      "Two intersecting planes meet along one line."),
    c("If a line is parallel to a plane, its direction is?", "the same as the direction of a parallel line in the plane",
      ["always perpendicular to the plane", "always passes through the plane", "not parallel to any line in the plane"],
      "The property theorem identifies a line in the plane parallel to the given line."),
])

T("sol.ppj", C8, "8.5", "Criterion for Parallel Planes", GG, "reasoning",
  "Use the criterion that two intersecting lines in one plane are both parallel to another plane to establish that the planes are parallel.",
  ["Can state that two intersecting lines are required", "Can explain why one line is not enough"],
  "GA.11", "inferred", "The criterion for parallel planes follows the criterion for a line parallel to a plane. Verification pending.")
Qs("sol.ppj", [
    c("Two intersecting lines in plane α are both parallel to plane β. Then?", "α is parallel to β",
      ["α intersects β", "α is perpendicular to β", "only line-plane parallelism follows"],
      "Both intersecting lines must be parallel to the other plane to guarantee that the planes are parallel."),
    c("Can one line in a plane, parallel to another plane, establish that the planes are parallel?", "no",
      ["yes", "only if the line is a lateral edge", "only in a cuboid"],
      "One line can establish line-plane parallelism. The plane could still tilt around that line."),
    n("How many intersecting lines in the plane does the criterion require as references?", "2",
      "It requires two lines, and they must intersect."),
    c("If the two lines are parallel rather than intersecting, then?", "the criterion cannot be applied directly",
      ["the planes are still parallel", "the planes must be perpendicular", "the lines are skew"],
      "Two parallel lines do not provide enough directions; the theorem requires intersecting lines."),
])

T("sol.ppp", C8, "8.5", "Property of Parallel Planes", GG, "reasoning",
  "Know that when a third plane cuts two parallel planes, the two intersection lines are parallel.",
  ["Can state that the two intersection lines are parallel", "Can identify such intersection lines in a cuboid"],
  "GA.11", "inferred", "The property of parallel planes is paired with its criterion. Verification pending.")
Qs("sol.ppp", [
    c("When a third plane cuts two parallel planes, the two intersection lines are?", "parallel",
      ["perpendicular", "always intersecting", "always skew"],
      "This is the property theorem for parallel planes."),
    n("The top and bottom bases of a cuboid are parallel. A lateral face intersects each base in a line. Are these two intersection lines parallel? Answer 1 if they are, 0 otherwise.", "1",
      "The lateral face cuts a pair of parallel planes. The intersection lines are corresponding edges of the bases, so they are parallel."),
    c("If two planes are parallel, a line in one plane is what relative to the other plane?", "parallel",
      ["intersecting", "contained in the other plane", "perpendicular"],
      "Otherwise the line would connect the planes at a common point, and the planes would intersect."),
    c("How many common points do two parallel planes have?", "0", ["1", "infinitely many along a line", "all points"],
      "Parallel planes have no common points."),
])

T("sol.lvj", C8, "8.6", "Criterion for a Line Perpendicular to a Plane", GG, "reasoning",
  "Use the criterion that a line perpendicular to two intersecting lines in a plane is perpendicular to the plane.",
  ["Can state that the line must be perpendicular to two intersecting lines", "Can explain why one line is not enough"],
  "GA.12")
Qs("sol.lvj", [
    c("Line l is perpendicular to two intersecting lines in a plane. Then?", "l is perpendicular to the plane",
      ["l is only parallel to the plane", "l lies in the plane", "there is not enough information"],
      "This is the criterion for a line to be perpendicular to a plane. The two lines must intersect."),
    c("Can a line be shown perpendicular to a plane if it is perpendicular to only one line in the plane?", "no",
      ["yes", "yes, if that line passes through the center of a circle", "yes, in a perspective view"],
      "One line is not enough; the given line may be perpendicular to only one direction."),
    n("How many intersecting lines in the plane are required by the criterion?", "2",
      "Two intersecting lines are required."),
    c("A cuboid's lateral edges are what relative to its base?", "perpendicular", ["parallel", "skew", "in the base"],
      "The lateral edges are perpendicular to two intersecting edges of the base, so they are perpendicular to the base."),
])

T("sol.lvp", C8, "8.6", "Property of a Line Perpendicular to a Plane", GG, "reasoning",
  "Know that two lines perpendicular to the same plane are parallel.",
  ["Can infer that two lines are parallel from their perpendicularity to a plane", "Can give an example in a cuboid"],
  "GA.12", "inferred", "The property theorem is paired with the criterion theorem. Verification pending.")
Qs("sol.lvp", [
    c("Two lines perpendicular to the same plane are?", "parallel",
      ["always intersecting", "always skew", "always perpendicular"],
      "This is the property of a line perpendicular to a plane."),
    n("A cuboid has 4 lateral edges, all perpendicular to the base. Are two adjacent lateral edges parallel? Answer 1 if they are, 0 otherwise.", "1",
      "All are perpendicular to the base, so the lateral edges are parallel to one another."),
    c("If a line is perpendicular to a plane, it is perpendicular to?", "every line in the plane",
      ["only two lines", "every line outside the plane", "only the lateral edges"],
      "By definition, a line perpendicular to a plane is perpendicular to every line in the plane."),
    c("What relationship between two lines is the conclusion of the property theorem?", "parallel", ["perpendicular", "intersecting", "skew"],
      "Because both lines are perpendicular to the same plane, they are parallel."),
])

T("sol.perp", C8, "8.6", "Perpendicular Planes", GG, "reasoning",
  "Know that if one plane contains a line perpendicular to another plane, the two planes are perpendicular. Dihedral-angle measures are not calculated.",
  ["Can use a perpendicular line to establish that two planes are perpendicular", "Know that this graph does not require calculating dihedral angles"],
  "GA.12", "inferred", "Perpendicular planes are established using line-plane perpendicularity. Measuring dihedral angles is part of an elective required course and is not covered here. Verification pending.")
Qs("sol.perp", [
    c("If one plane contains a line perpendicular to another plane, the two planes are?", "perpendicular",
      ["parallel", "necessarily coincident", "impossible to determine"],
      "This is the criterion for perpendicular planes. The perpendicular line lies in one of the planes."),
    n("In a cube, after choosing one face as the base, how many faces are perpendicular to it?", "4",
      "Each of the four side faces contains a perpendicular to the base (a lateral edge). By the criterion, each is perpendicular to the base; the opposite face is parallel to it."),
    n("Two adjacent lateral faces of a cuboid are both perpendicular to the base. How many lateral edges in one of these faces are perpendicular to the base? Count only that face's own lateral edges.", "2",
      "The face is a rectangle, and both of its lateral edges are perpendicular to the base."),
    c("A wall and a floor are usually modeled as?", "two perpendicular planes",
      ["two parallel planes", "two skew lines", "a sphere"],
      "The wall-floor intersection is the baseboard line, and the wall contains a line perpendicular to the floor."),
])

T("sta.src", C9, "9.1", "Ways to Obtain Data", SP, "conceptual",
  "Know that data can be obtained through surveys, experiments, observations, and references, and choose a method appropriate to the question.",
  ["Can name common data sources", "Can decide whether a question calls for a census or a sample"],
  "PS.01")
Qs("sta.src", [
    c("You want to know the lifetime of a batch of light bulbs, but testing destroys them. What is more appropriate?", "a sample test",
      ["test every bulb in a census", "ask only one person for an opinion", "collect no data"],
      "Lifetime testing is destructive, so sample the products rather than testing them all."),
    c("Looking up population data already published by the statistics bureau is?", "consulting existing data",
      ["a random experiment", "an in-person questionnaire", "designing a new experiment"],
      "The data already exist, so they can simply be consulted."),
    n("A class has 40 students. How many students' data must be collected for a census?", "40",
      "A census collects data from everyone; here, that is 40 students."),
    c("What should be clarified first when collecting data?", "the question to be studied",
      ["draw a histogram first", "calculate the variance first", "write the conclusion first"],
      "The question determines what data to collect and from whom."),
])

T("sta.srs", C9, "9.1", "Simple Random Sampling", SP, "procedural",
  "Use a draw or random numbers for simple random sampling, and know that each individual has an equal chance of selection.",
  ["Can calculate each person's probability of being selected", "Can state the defining feature of simple random sampling"],
  "PS.02")
Qs("sta.srs", [
    n("A population has 20 people. One person is selected by simple random sampling. What is the probability of selecting any particular person?",
      "Fraction(1,20)",
      "Each person has the same chance, so the probability is 1/20."),
    n("There are 10 items in a population. How many different ways are there to select 2 by simple random sampling?", "comb(10,2)",
      "The number of combinations is C(10,2)=45."),
    c("Simple random sampling requires?", "each individual to have the same chance of being selected",
      ["select only people with high scores", "sample in proportion to class size", "the sample must equal the population"],
      "Equal chances are essential to simple random sampling. Sampling in proportion to group size is stratified sampling."),
    c("For a lottery draw, the numbers should be?", "thoroughly mixed before drawing",
      ["drawn from the smallest upward", "only even numbers drawn", "the same person drawn repeatedly until satisfied"],
      "Without mixing, later numbers would have almost no chance of being drawn."),
])

T("sta.strat", C9, "9.1", "Stratified Random Sampling", SP, "procedural",
  "Allocate the sample across strata in proportion to the number of individuals in each stratum.",
  ["Can calculate how many people to sample from each stratum", "Can add the stratum counts to check the sample size"],
  "PS.02", "inferred", "Stratified sampling and simple random sampling are both random-sampling methods. Verification pending.")
Qs("sta.strat", [
    n("Stratum A has 40 people and stratum B has 60. If 1/10 is sampled from each, how many people should be sampled from A?", "40/10",
      "40×1/10=4."),
    n("Stratum A has 40 people and stratum B has 60. If 1/10 is sampled from each, how many people should be sampled from B?", "60/10",
      "Sample 1/10 from each stratum: 60×1/10=6 from B."),
    n("What is the combined sample size for both strata?", "40/10+60/10",
      "4+6=10, which is also 1/10 of the total population of 100."),
    c("Stratified sampling is appropriate when?", "the population consists of several distinctly different strata",
      ["the population has only 2 individuals", "all individuals are exactly alike", "continuous production cannot be grouped"],
      "When each stratum is relatively uniform but strata differ, proportional sampling better represents the population."),
])

T("sta.choose", C9, "9.1", "Choosing a Sampling Method", SP, "reasoning",
  "Choose simple random sampling or stratified sampling based on whether the population has distinct strata.",
  ["Can identify proportional sampling as stratified sampling", "Can explain that a sample is not the population itself"],
  "PS.02", "inferred", "Choosing a method builds on knowing both sampling methods. Verification pending.")
Qs("sta.choose", [
    c("A school has very different enrollment in its three grades. To estimate daily homework time for the whole school, which method is more suitable?", "stratified random sampling",
      ["sample only one grade", "combine the grades without accounting for enrollment", "survey only teachers"],
      "The grades may differ, so use strata in proportion to enrollment."),
    c("Twenty pens are in one box, with no meaningful strata beyond their appearance. Which method should be used to inspect 4 pens?", "simple random sampling",
      ["stratified sampling is required", "a census", "select only the first pen"],
      "There are no distinct strata, so simple random sampling is sufficient."),
    n("A sample size of 8 does not mean the population has only 8 people. If the population is 80, what fraction of it is the sample?", "Fraction(8,80)",
      "8/80=1/10."),
    c("What does a conclusion from sampling represent?", "an estimate that may not equal the exact population value",
      ["it must equal the population parameter", "it cannot be used to make any judgment", "it applies only to the sampled people and not the population"],
      "A sample provides an estimate and includes random error."),
])

T("sta.hist", C9, "9.2", "Frequency Histograms", SP, "procedural",
  "Know that each rectangle's area represents frequency, its height is frequency divided by class width, and all areas sum to 1.",
  ["Can find a frequency from relative frequency, class width, and sample size", "Can check that the relative frequencies sum to 1"],
  "PS.03")
Qs("sta.hist", [
    n("The class width is 5, and relative frequency divided by class width is 0.04. The sample size is 50. What is the frequency for this class?", "Fraction(4,100)*5*50",
      "Relative frequency=0.04×5=0.2, so frequency=0.2×50=10."),
    n("Two classes have relative frequencies 0.3 and 0.7. What is their sum?", "Fraction(3,10)+Fraction(7,10)",
      "The areas of all rectangles sum to 1."),
    n("The class width is 10, a class has frequency 20, and the sample size is 100. Express this class's relative frequency divided by its class width as a fraction.",
      "Fraction(20,100)/10",
      "Relative frequency=20/100=1/5; dividing by class width 10 gives 1/50."),
    c("In a histogram, what does the height of a rectangle represent?", "relative frequency divided by class width",
      ["the frequency itself", "the sample size", "the class width"],
      "Frequency is represented by area, so height must be relative frequency/class width. If class widths differ, heights alone cannot be compared as frequencies."),
])

T("sta.read", C9, "9.2", "Reading a Histogram", SP, "procedural",
  "Recover frequencies from relative frequencies and class widths, and compare the sizes of groups.",
  ["Can calculate a specified class frequency", "Can compare two relative frequencies"],
  "PS.03", "inferred", "Reading a graph is an application of frequency histograms. Verification pending.")
Qs("sta.read", [
    n("The sample size is 40, and a class has relative frequency 0.25. What is its frequency?", "Fraction(1,4)*40",
      "0.25×40=10."),
    n("Class A has relative frequency 0.2 and class B has 0.35. How much greater is B's relative frequency?", "Fraction(35,100)-Fraction(20,100)",
      "0.35−0.20=0.15."),
    n("A class has relative frequency 1/5 in a sample of 80. How many data points are in that class?", "Fraction(1,5)*80",
      "80/5=16."),
    c("In a histogram with equal class widths, a taller rectangle means?", "the class has a greater relative frequency",
      ["the data in the class are smaller", "the sample size is larger", "the mean is larger"],
      "When class widths are equal, height is proportional to relative frequency."),
])

T("sta.pct", C9, "9.2", "Percentiles", SP, "procedural",
  "Find a percentile using the convention common in PEP textbook exercises: sort the data in ascending order and set i=n×p%. If i is not an integer, take the ceil(i)-th value; if i is an integer, average the i-th and (i+1)-th values.",
  ["Can determine whether i is an integer", "Can select the corresponding value according to the rule"],
  "PS.04", "inferred", "Percentiles are a numerical characteristic used to estimate a population from a sample. The algorithm follows a common textbook description and has not been checked page by page against a print edition. Verification pending.")
Qs("sta.pct", [
    n("The data 1, 2, 3, 4 are sorted in ascending order, with n=4. Find the 50th percentile. Rule: i=n×50%; when i is an integer, average the i-th and (i+1)-th values.",
      "(sorted([1,2,3,4])[1]+sorted([1,2,3,4])[2])/2",
      "i=2, so average the 2nd and 3rd values, 2 and 3; their mean is 5/2."),
    n("The data 2, 4, 6, 8, 10 are sorted, with n=5. Find the 20th percentile. If i=n×20% is an integer, average the i-th and (i+1)-th values.",
      "(sorted([2,4,6,8,10])[0]+sorted([2,4,6,8,10])[1])/2",
      "i=1, so average the 1st and 2nd values, 2 and 4; their mean is 3."),
    n("The data 1, 3, 5, 7, 9 are sorted, with n=5. Find the 50th percentile. Since i=2.5 is not an integer, take the first integer position after it, the 3rd value.",
      "sorted([1,3,5,7,9])[2]",
      "The 3rd value is 5."),
    c("What does a percentile describe?", "the value at a particular percentage position in a sample",
      ["always the mean", "always the mode", "the sample size"],
      "It describes a position in the sorted data, not the average of all values."),
])

T("sta.center", C9, "9.2", "Estimating a Population Center from a Sample", SP, "procedural",
  "Calculate a sample mean and median and use them to estimate the center of a population.",
  ["Can find the mean of a data set", "Can find the median"],
  "PS.04")
Qs("sta.center", [
    n("What is the mean of the sample 2, 4, 6, 8?", "mean([2,4,6,8])",
      "(2+4+6+8)/4=5."),
    n("What is the median of the sample 1, 3, 3, 7?", "median([1,3,3,7])",
      "The two middle values after sorting are both 3, so the median is 3."),
    n("What is the mean of the sample 1, 2, 9?", "mean([1,2,9])",
      "(1+2+9)/3=4."),
    c("When a data set has an unusually large value, which is often a more robust estimate of its center?", "the median",
      ["always switch to the range", "look only at the maximum", "the sample size"],
      "The median is not pulled by extreme values at either end, while the mean can be."),
])

T("sta.spread", C9, "9.2", "Estimating Population Variability from a Sample", SP, "procedural",
  "Use the range and population variance (divide by n) to compare data variability. Whenever a question says variance, it means division by n.",
  ["Can calculate the range", "Can calculate variance using division by n"],
  "PS.04", "inferred", "Variability and center are both used to estimate a population. The variance convention matches the middle-school sample-variance question: divide by n. Verification pending.")
Qs("sta.spread", [
    n("What is the range of the data 2, 4, 4, 6?", "6-2",
      "Maximum minus minimum: 6−2=4."),
    n("What is the variance of the data 2, 4, 4, 6? Divide by n.", "pvariance([2,4,4,6])",
      "The mean is 4, the sum of squared deviations is 8, and dividing by 4 gives 2."),
    n("What is the variance of the data 5, 5, 5? Divide by n.", "pvariance([5,5,5])",
      "Every value equals the mean, so the variance is 0."),
    c("A larger variance means?", "greater variability in the data",
      ["a larger mean", "more data points", "a larger median"],
      "Variance measures deviation from the mean; it is not the mean itself."),
])

T("sta.chart", C9, "9.2", "Choosing a Statistical Chart", SP, "reasoning",
  "Choose a bar chart, line chart, pie chart, or histogram to suit a question.",
  ["Can explain that pie charts show proportions", "Can explain that line charts show changes"],
  "PS.04", "inferred", "Charts are a way to present estimates of a population from a sample. Verification pending.")
Qs("sta.chart", [
    c("To see what percentage of the whole each part represents, which chart is more suitable?", "a pie chart",
      ["a line chart", "a stem-and-leaf plot is unnecessary here; use a pie chart", "write only the variance"],
      "A pie chart represents proportions by the sizes of its sectors."),
    c("To see how daily temperatures change over a month, which chart is more suitable?", "a line chart",
      ["a pie chart", "a bar chart showing only the total", "write only the mode"],
      "A line chart shows rises and falls over time."),
    n("A pie chart has three categories with percentages 20, 30, and 50. What is their sum?", "20+30+50",
      "All categories together should account for 100%."),
    c("Which chart is used to compare distributions over several continuous intervals?", "a frequency histogram",
      ["draw only one pie sector", "calculate only one mean", "do not group the data"],
      "A histogram is designed to show the frequency distribution of grouped data."),
])

T("sta.case", C9, "9.3", "Statistical Case Study", SP, "application",
  "Compare the means of two samples in a simple case study and explain that the conclusion is an estimate.",
  ["Can calculate and compare two sample means", "Can state that a sample-based conclusion is not an absolute fact"],
  "PS.04", "inferred", "A statistical case study combines methods for estimating a population from a sample. The PEP example “Obesity Among Company Employees” is pending verification; this uses only a structurally similar small example.")
Qs("sta.case", [
    n("Group A has 4 people with weights 60, 62, 64, and 66. What is the mean?", "mean([60,62,64,66])",
      "(60+62+64+66)/4=63."),
    n("What is the mean of group B's values 70, 70, 70?", "mean([70,70,70])",
      "All three values are 70."),
    n("What is group B's mean minus group A's mean?", "70-63",
      "70−63=7. This shows only the difference between these samples; the sampling method must also be considered."),
    c("How should a case-study conclusion from a sample be used?", "as an estimate, with an explanation of how the sample was selected",
      ["as the exact value for the whole population", "without reporting the sample size", "change the data to make the conclusion look better"],
      "A statistical case study should report both the data source and the limits of its conclusion."),
])

T("prb.space", C10, "10.1", "Sample Points and Sample Spaces", SP, "conceptual",
  "Know that each possible outcome of an experiment is a sample point and that the set of all sample points is the sample space.",
  ["Can list all sample points for a finite experiment", "Can state that a sample space is represented as a set"],
  "PS.05")
Qs("prb.space", [
    n("A fair coin is tossed 2 times. How many sample points are there?", "2**2",
      "Each toss has two outcomes, so there are 4 outcomes in total: HH, HT, TH, and TT."),
    n("A bag contains 3 distinct balls. One is drawn. How many sample points are there?", "3",
      "Each ball is one sample point."),
    c("A sample space is?", "the set of all sample points",
      ["only the most likely outcome", "an event with probability 1", "the outcome that has already occurred"],
      "The sample space is listed before an experiment and includes every possible outcome."),
    c("Representing a sample space as a set means?", "treating outcomes as elements",
      ["treating probabilities as elements", "using roster notation only, never set-builder notation", "excluding the empty set"],
      "In high-school probability, set language is used and outcomes are elements."),
])

T("prb.event", C10, "10.1", "Random Events", SP, "conceptual",
  "Know that an event is a subset of the sample space, the certain event is the sample space itself, and the impossible event is the empty set.",
  ["Can decide whether an event is certain or impossible", "Can state that an event's probability is between 0 and 1"],
  "PS.05", "inferred", "An event is a subset of the sample space. Verification pending.")
Qs("prb.event", [
    c("What is the probability of a certain event?", "1", ["0", "1/2", "it can exceed 1"],
      "It occurs every time, so its probability is 1."),
    c("Which set represents an impossible event?", "the empty set", ["the sample space", "a set containing one sample point", "all real numbers"],
      "No sample point can make it occur."),
    n("A sample space has 5 sample points, and an event contains all 5. What is its probability under the classical model?", "Fraction(5,5)",
      "The event contains every sample point, so its probability is 1; it is a certain event."),
    c("A random event is?", "an event that may or may not occur",
      ["an event that must occur", "an event that cannot occur", "an object outside the sample space"],
      "A random event has probability strictly between 0 and 1. Certain and impossible events are the two extremes."),
])

T("prb.ops", C10, "10.1", "Event Relationships and Operations", SP, "procedural",
  "Use intersection, union, and complement to represent events occurring together, at least one occurring, and complementary events.",
  ["Can explain the meaning of a union and an intersection", "Can count the sample points in a complementary event in a finite sample space"],
  "PS.05", "inferred", "Event operations are set operations. Verification pending.")
Qs("prb.ops", [
    n("The sample space has 8 points and event A has 3. How many sample points are in the complement of A?", "8-3",
      "The complement has 8−3=5 points."),
    n("A has 4 sample points, B has 5, and A∩B has 2. How many sample points are in A∪B?", "4+5-2",
      "The union has 4+5−2=7 points."),
    c("What does A∩B represent?", "A and B both occur",
      ["at least one of A or B occurs", "A does not occur", "the sample space"],
      "An intersection is the shared part; both events occur."),
    c("Besides being mutually exclusive, complementary events must?", "together make up the entire sample space",
      ["have a nonempty intersection", "both have probability 1/2", "each contain exactly one sample point"],
      "Mutually exclusive events cannot occur together. Complementary events must also cover all outcomes."),
])

T("prb.class", C10, "10.1", "Classical Probability", SP, "procedural",
  "In a finite sample space with equally likely outcomes, find an event's probability by dividing its number of sample points by the total.",
  ["Can determine whether outcomes are equally likely", "Can use combinations to calculate sampling probabilities"],
  "PS.06")
Qs("prb.class", [
    n("A bag contains 5 red and 3 blue balls, 8 in total. Two are drawn at random. What is the probability of drawing 2 red balls?",
      "Fraction(comb(5,2),comb(8,2))",
      "C(5,2)/C(8,2)=10/28=5/14."),
    n("What is the probability of rolling a number greater than 4 on a fair die?", "Fraction(2,6)",
      "There are 6 equally likely outcomes, and 5 and 6 are favorable, so the probability is 1/3."),
    n("A number is chosen with equal probability from 1, 2, 3, 4. What is the probability of choosing an even number?", "Fraction(2,4)",
      "The even numbers are 2 and 4, so the probability is 1/2."),
    c("A classical probability model requires sample points to be?", "finite in number and equally likely",
      ["possibly infinite", "allowed to have unequal probabilities", "a continuous interval"],
      "When outcomes are not equally likely, probability cannot be found by dividing one count by another."),
])

T("prb.add", C10, "10.1", "Addition Rule for Probability", SP, "procedural",
  "Use the addition rule for mutually exclusive events, P(A∪B)=P(A)+P(B), and inclusion-exclusion when events are not mutually exclusive.",
  ["Can determine whether two events are mutually exclusive", "Can calculate the probability of the union of mutually exclusive events"],
  "PS.06", "inferred", "The addition rule is a calculation based on classical probability and probability properties. Verification pending.")
Qs("prb.add", [
    n("A and B are mutually exclusive, with P(A)=1/4 and P(B)=1/5. What is P(A∪B)?", "Fraction(1,4)+Fraction(1,5)",
      "For mutually exclusive events, add the probabilities: 1/4+1/5=9/20."),
    n("P(A)=1/2, P(B)=1/3, and P(A∩B)=1/6. What is P(A∪B)?", "Fraction(1,2)+Fraction(1,3)-Fraction(1,6)",
      "For events that are not mutually exclusive, subtract the overlap: 1/2+1/3−1/6=2/3."),
    n("The probability of an event's complement is 1/5. What is the probability of the original event?", "1-Fraction(1,5)",
      "Complementary event probabilities sum to 1, so the original event has probability 4/5."),
    c("Why can probabilities of mutually exclusive events be added directly?", "they cannot occur together, so their intersection is empty",
      ["they are independent", "their probabilities are both 1", "there are infinitely many sample points"],
      "Mutual exclusivity is not the same as independence. Here, the intersection is empty."),
])

T("prb.excl", C10, "10.1", "Mutually Exclusive and Complementary Events", SP, "reasoning",
  "Distinguish mutually exclusive and complementary events: complementary events are always mutually exclusive, but mutually exclusive events are not always complementary.",
  ["Can determine whether a pair of events is mutually exclusive or complementary", "Can calculate the probability of a complementary event"],
  "PS.06", "inferred", "The distinction between mutual exclusivity and complementation is important when using the probability addition rule. Verification pending.")
Qs("prb.excl", [
    c("Are complementary events always mutually exclusive?", "yes", ["never", "only when their probabilities are 1/2", "cannot be determined"],
      "Complementary events cannot occur together, so they are mutually exclusive; they also cover the entire sample space."),
    c("Are mutually exclusive events always complementary?", "not necessarily", ["always", "always in a classical model", "only when there are two sample points"],
      "Two events may both fail to occur. For example, rolling a 1 and rolling a 2 are mutually exclusive but not complementary."),
    n("P(A)=0.3. If B is the complement of A, express P(B) as a fraction. 0.3=3/10.", "1-Fraction(3,10)",
      "1−3/10=7/10."),
    n("A sample space has 6 equally likely outcomes. How many outcomes are in the union of “roll a 1” and “roll a 2”?", "2",
      "The counts of mutually exclusive events add: 1+1=2. Their union is not a certain event."),
])

T("prb.ind", C10, "10.2", "Independence of Events", SP, "conceptual",
  "Know that A and B are independent if P(A∩B)=P(A)P(B). Independence is not mutual exclusivity.",
  ["Can use multiplication to find the probability of two independent events occurring together", "Can explain the difference between independence and mutual exclusivity"],
  "PS.07")
Qs("prb.ind", [
    n("A and B are independent, with P(A)=1/2 and P(B)=1/3. What is P(A∩B)?", "Fraction(1,2)*Fraction(1,3)",
      "For independent events, multiply their probabilities to find the probability that both occur: 1/6."),
    n("A coin is tossed twice independently. The probability of heads on each toss is 1/2. What is the probability of heads on both tosses?",
      "Fraction(1,2)*Fraction(1,2)",
      "1/4."),
    c("If neither A nor B is impossible and they are mutually exclusive, then they are?", "not independent",
      ["always independent", "both have probability 0", "impossible to intersect"],
      "For mutually exclusive events, P(A∩B)=0, while P(A)P(B)>0; the two are not equal."),
    c("What does independence mean?", "whether one event occurs does not change the probability of the other",
      ["the two events cannot occur together", "the two events must occur together", "their probabilities sum to 1"],
      "Independence concerns the product of probabilities, not an empty intersection."),
])

T("prb.indp", C10, "10.2", "Calculating Probabilities for Independent Events", SP, "procedural",
  "Calculate the probability that an event occurs every time or at least once in repeated independent trials. Conditional probability is outside the required-course scope.",
  ["Can calculate the probability of an event occurring in all n independent trials", "Can use the complementary event to calculate the probability of at least one occurrence"],
  "PS.07", "inferred", "These calculations apply the definition of independence. Conditional probability is not introduced. Verification pending.")
Qs("prb.indp", [
    n("The probability of a hit on each shot is 1/2. What is the probability of hitting on all three independent shots?", "Fraction(1,2)**3",
      "(1/2)³=1/8."),
    n("The probability of a miss on each shot is 1/2. What is the probability of missing all three times?", "Fraction(1,2)**3",
      "It is also 1/8."),
    n("The probability of a hit on one shot is 1/2. The complement of at least one hit is missing all three shots. What is the probability of at least one hit in three independent shots?",
      "1-Fraction(1,2)**3",
      "1−1/8=7/8."),
    c("Does calculating “at least once” using its complement require conditional probability?", "no",
      ["yes", "the first shot must already be a hit", "only in a classical model"],
      "Complementary events and independence are sufficient. Conditional probability is elective required-course content."),
])

T("prb.freq", C10, "10.3", "Frequency and Probability", SP, "conceptual",
  "Know that as the number of trials increases, frequency tends to stabilize near probability, but frequency itself is not probability.",
  ["Can calculate the frequency in a set of trials", "Can explain the difference between frequency and probability"],
  "PS.08")
Qs("prb.freq", [
    n("An experiment is performed 200 times and an event occurs 40 times. What is its frequency?", "Fraction(40,200)",
      "40/200=1/5."),
    n("The experiment is performed 100 more times, and the event occurs 20 times. What is the frequency in this batch?", "Fraction(20,100)",
      "20/100=1/5."),
    c("A frequency stabilizes near 1/5. What does this suggest?", "the probability can be estimated as 1/5",
      ["the probability has become the next frequency value", "the event must occur next time", "the experiment can stop and its result will no longer change"],
      "Frequency provides an estimate; the next outcome is still random."),
    c("What is the difference between frequency and probability?", "frequency comes from trials already performed, while probability describes the event's underlying behavior",
      ["they are always equal", "frequency can exceed 1", "probability changes with the number of trials"],
      "Probability is a fixed model value; frequency fluctuates and gradually stabilizes."),
])

T("prb.fest", C10, "10.3", "Estimating Probability from Frequency", SP, "application",
  "Estimate probability from the frequency in many repeated trials and compare estimates based on different numbers of trials.",
  ["Can choose the estimate based on more trials", "Can calculate frequency as an estimate"],
  "PS.08", "inferred", "Estimating probability from frequency is an application of frequency stability. Verification pending.")
Qs("prb.fest", [
    n("An event occurs 320 times in 1000 trials. What probability does its frequency estimate?", "Fraction(320,1000)",
      "320/1000=8/25."),
    n("In another experiment, the event occurs 8 times in 10 trials. What is the frequency in those 10 trials?", "Fraction(8,10)",
      "8/10=4/5. With fewer trials, fluctuations tend to be larger."),
    c("For the same experiment, which estimate is usually more reliable?", "the estimate based on more trials",
      ["the one with the higher frequency", "the one based on fewer trials", "the first one performed"],
      "Frequency is more stable with more trials."),
    n("If the estimated probability is 1/4, about how many occurrences are expected in 40 trials?", "40*Fraction(1,4)",
      "The expected count is 40×1/4=10. The actual count may still fluctuate."),
])
