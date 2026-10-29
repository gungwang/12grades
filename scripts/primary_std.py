# -*- coding: utf-8 -*-
"""Content-requirement entries for Stages 1–3.

The clauses are from a public-preview transcription of the Compulsory Education Mathematics Curriculum Standards (2022 edition) published by 21st Century Education Network
(http://zy.21cnjy.com/20610065, retrieved 2026-10-19); they have not been checked page by page against the Ministry of Education PDF.
Line breaks have been restored. Possible issues at joins, superscripts, and phrases such as "directly proportional" are marked "needs verification" in each item's note or text_status.
verbatim is always false. Only content requirements are included; academic requirements and teaching suggestions are excluded.
"""

def _it(stage, code, n, domain, section, clause, text, note=None, text_status=None):
    sid = "cms-2022:%s.%s.%02d" % (stage, code, n)
    item = {
        "id": sid,
        "domain": domain,
        "section": section,
        "clause": clause,
        "text": text,
        "page_or_ref": ("Printed curriculum page %d" % PAGES[sid]) if sid in PAGES else "Needs verification",
        "verbatim": False,
        "text_status": text_status or "Public-preview transcription; not checked page by page against the Ministry of Education PDF",
    }
    if note:
        item["wording_note"] = note
    return item


NA, GG, SP, IP = "Number and Algebra", "Geometry and Measurement", "Statistics and Probability", "Integrated Practice"

# 2026-10-21: Printed curriculum page numbers for 77 primary-school clauses, checked against each page of the official PDF (PDF page = printed page + 3).
# Each range is (domain, start, end, printed page); entries are assigned pages automatically by ID.
PAGES = {}
for _k, _a, _b, _p in [
    ("1.NA", 1, 6, 18), ("1.NA", 7, 8, 19),
    ("2.NA", 1, 1, 20), ("2.NA", 2, 10, 21),
    ("3.NA", 1, 2, 23), ("3.NA", 3, 10, 24),
    ("1.GG", 1, 3, 28),
    ("2.GG", 1, 5, 29), ("2.GG", 6, 9, 30),
    ("3.GG", 1, 5, 32), ("3.GG", 6, 12, 33),
    ("1.SP", 1, 1, 37),
    ("2.SP", 1, 6, 38),
    ("3.SP", 1, 2, 39), ("3.SP", 3, 7, 40),
    ("1.IP", 1, 1, 42), ("1.IP", 2, 6, 43),
    ("2.IP", 1, 4, 46),
    ("3.IP", 1, 1, 49),
]:
    for _n in range(_a, _b + 1):
        PAGES["cms-2022:%s.%02d" % (_k, _n)] = _p

ITEMS = [
    # ---------- Stage 1: Number and Algebra ----------
    _it(1, "NA", 1, NA, "Number and Operations", "(1)",
        "In real-world contexts, develop an intuitive understanding of numbers up to 10,000 and their place values; know that an abacus can represent multi-digit numbers."),
    _it(1, "NA", 2, NA, "Number and Operations", "(2)",
        "Understand what <, =, and > mean and compare numbers up to 10,000; through comparing numbers, develop an intuitive understanding of equality and inequality.",
        "2026-10-21: Corrected the symbols to match printed page 18 of the official PDF (originally <, =, >); removed the Example 2 quotation from the body per convention."),
    _it(1, "NA", 3, NA, "Number and Operations", "(3)",
        "In concrete contexts, understand the meaning of the four arithmetic operations and the relationships among them."),
    _it(1, "NA", 4, NA, "Number and Operations", "(4)",
        "Explore the reasoning and methods behind addition and subtraction; perform addition and subtraction with whole numbers."),
    _it(1, "NA", 5, NA, "Number and Operations", "(5)",
        "Explore the reasoning and methods behind multiplication and division; perform simple whole-number multiplication and division."),
    _it(1, "NA", 6, NA, "Number and Operations", "(6)",
        "Through solving problems in everyday contexts, understand the meaning of numbers and operations, and begin to develop symbol awareness, number sense, computational fluency, and reasoning awareness."),
    _it(1, "NA", 7, NA, "Quantitative Relationships", "(1)",
        "Use numbers and operations to solve problems in simple everyday contexts; explain the real-world meaning of the results and begin to develop awareness of how mathematics is applied."),
    _it(1, "NA", 8, NA, "Quantitative Relationships", "(2)",
        "Explore ways to express simple patterns of change in a context using numbers or symbols."),
    # ---------- Stage 1: Geometry and Measurement ----------
    _it(1, "GG", 1, GG, "Shape Recognition and Measurement", "(1)",
        "Identify simple solid and plane figures using physical objects and models, classify shapes, and make pictures from simple shapes."),
    _it(1, "GG", 2, GG, "Shape Recognition and Measurement", "(2)",
        "Recognize the importance of a common unit of measurement in everyday life; learn the meter and centimeter as units of length. Estimate and measure the lengths of some objects."),
    _it(1, "GG", 3, GG, "Shape Recognition and Measurement", "(3)",
        "Develop an initial sense of space and measurement through learning about shapes and measuring them."),
    # ---------- Stage 1: Statistics and Probability ----------
    _it(1, "SP", 1, SP, "Data Classification", "1",
        "Classify objects, shapes, or data; begin to understand the relationship between classification and its criteria, and develop an initial awareness of data."),
    # ---------- Stage 1: Integrated Practice ----------
    _it(1, "IP", 1, IP, "Sharing Math Games", "Theme activity 1",
        "In concrete contexts, look back on activities related to learning mathematics during preschool, rekindle intuitive understanding and prior learning experiences, spark further interest in mathematics, try using relevant mathematical vocabulary, and gradually develop good study habits."),
    _it(1, "IP", 2, IP, "Happy Shopping Street", "Theme activity 2",
        "Recognize RMB in real-world contexts, perform simple unit conversions, understand the role of money, develop an awareness of thrift, and begin to build financial literacy."),
    _it(1, "IP", 3, IP, "Where Is Time?", "Theme activity 3",
        "Learn hours, minutes, and seconds in everyday contexts; use life experience to understand and describe durations, understand the meaning of time, and learn to be punctual."),
    _it(1, "IP", 4, IP, "My Classroom", "Theme activity 4",
        "Use above, below, left, right, in front, and behind to describe relative positions in everyday contexts; learn the four cardinal directions—east, south, west, and north. Develop an initial sense of space."),
    _it(1, "IP", 5, IP, "The Ruler on Your Body", "Theme activity 5",
        "Apply what you have learned about measuring length to identify some body-based 'lengths'; use these lengths as units to measure spaces or other objects, gain measurement experience, and develop a sense of measurement."),
    _it(1, "IP", 6, IP, "Math Comic Strip", "Theme activity 6",
        "Use mathematics learned so far to record personal experiences or tell a short story involving mathematics; express an understanding of quantitative relationships and see how mathematics connects to everyday life.",
        "The transcription splits the body of Theme activity 6 across lines; the fragments were joined at 'or tell' and 'a short story involving mathematics'. Needs verification."),
    # ---------- Stage 2: Number and Algebra ----------
    _it(2, "NA", 1, NA, "Number and Operations", "(1)",
        "In concrete contexts, learn numbers greater than 10,000 and understand the base-ten system; explore and master multiplication and division with multi-digit numbers, and understand the transition from the unknown to the known."),
    _it(2, "NA", 2, NA, "Number and Operations", "(2)",
        "In concrete contexts, begin to understand decimals, fractions, and fraction units; add and subtract fractions with the same denominator and decimals with one decimal place."),
    _it(2, "NA", 3, NA, "Number and Operations", "(3)",
        "Understand the four arithmetic operations while solving simple real-world problems; perform mixed operations with whole numbers."),
    _it(2, "NA", 4, NA, "Number and Operations", "(4)",
        "Explore and understand the properties of operations (the commutative and associative properties of addition and multiplication, and the distributive property of multiplication over addition); use letters to represent these properties."),
    _it(2, "NA", 5, NA, "Number and Operations", "(5)",
        "Use numbers to describe features of things in everyday contexts, gradually developing number sense, computational fluency, and an initial awareness of reasoning."),
    _it(2, "NA", 6, NA, "Quantitative Relationships", "(1)",
        "Use numbers and operations to solve problems in real-world contexts; when solving practical problems, choose appropriate units for simple estimates and understand the role estimation plays in everyday life."),
    _it(2, "NA", 7, NA, "Quantitative Relationships", "(2)",
        "Use a calculator to solve simple real-world problems and explore simple patterns."),
    _it(2, "NA", 8, NA, "Quantitative Relationships", "(3)",
        "In concrete contexts, recognize common quantitative relationships: total = part + part, total cost = unit price × quantity, and distance = speed × time; use these relationships to solve simple real-world problems."),
    _it(2, "NA", 9, NA, "Quantitative Relationships", "(4)",
        "In concrete contexts, understand that quantities equal to the same quantity are equal."),
    _it(2, "NA", 10, NA, "Quantitative Relationships", "(5)",
        "Solve simple everyday problems and explain the real-world meaning of the results; explore simple patterns and begin to develop modeling and application awareness."),
    # ---------- Stage 2: Geometry and Measurement ----------
    _it(2, "GG", 1, GG, "Shape Recognition and Measurement", "(1)",
        "Use examples to learn segments, rays, and lines; understand that a segment is the shortest path between two points and that the distance between two points is the length of that segment; use a ruler and compass to construct a segment equal to a given segment; understand the positions of two lines in the same plane."),
    _it(2, "GG", 2, GG, "Shape Recognition and Measurement", "(2)",
        "Learn about angles in everyday contexts and compare their sizes; measure angles with a protractor and draw angles with a protractor or set square."),
    _it(2, "GG", 3, GG, "Shape Recognition and Measurement", "(3)",
        "Learn the kilometer as a unit of length and learn the decimeter and millimeter; learn the centimeter, decimeter, and meter as area units; convert simple units; choose appropriate units to estimate lengths and areas of objects and measure them.",
        "The transcription lists centimeter, decimeter, and meter as area units; the square-unit superscripts may have been lost. Needs verification."),
    _it(2, "GG", 4, GG, "Shape Recognition and Measurement", "(4)",
        "Learn triangles and quadrilaterals, and classify them by their properties."),
    _it(2, "GG", 5, GG, "Shape Recognition and Measurement", "(5)",
        "Learn about perimeter and area through examples; explore and master the formulas for the perimeter and area of rectangles and squares."),
    _it(2, "GG", 6, GG, "Shape Recognition and Measurement", "(6)",
        "Identify a simple object as seen from different angles based on the object itself, a photograph, or a visual representation."),
    _it(2, "GG", 7, GG, "Shape Recognition and Measurement", "(7)",
        "Strengthen spatial reasoning and a sense of measurement through learning about shapes and measuring them."),
    _it(2, "GG", 8, GG, "Position and Movement of Shapes", "(1)",
        "Recognize translation, rotation, and reflection (axial symmetry) in examples."),
    _it(2, "GG", 9, GG, "Position and Movement of Shapes", "(2)",
        "Develop spatial reasoning and initial geometric intuition while exploring the position and movement of shapes."),
    # ---------- Stage 2: Statistics and Probability ----------
    _it(2, "SP", 1, SP, "Data Collection, Organization, and Representation", "(1)",
        "Go through the process of collecting, organizing, describing, and analyzing simple data; learn simple ways to collect data and present the organized results."),
    _it(2, "SP", 2, SP, "Data Collection, Organization, and Representation", "(2)",
        "Through simple data analysis, recognize the information contained in data and the role of using data to communicate."),
    _it(2, "SP", 3, SP, "Data Collection, Organization, and Representation", "(3)",
        "Learn bar charts and use them appropriately to represent and analyze data."),
    _it(2, "SP", 4, SP, "Data Collection, Organization, and Representation", "(4)",
        "Interpret simple statistical charts and tables in newspapers, on television, online, and in other media."),
    _it(2, "SP", 5, SP, "Data Collection, Organization, and Representation", "(5)",
        "Explore the meaning of the mean and solve simple related real-world problems."),
    _it(2, "SP", 6, SP, "Data Collection, Organization, and Representation", "(6)",
        "Apply statistical charts and the mean appropriately in simple real-world contexts, developing an initial awareness of data and its application.",
        "2026-10-21: Restored the ending, 'developing an initial awareness of data and its application,' based on the 2025 revision (the phrase was already in the 2022 edition but was cut off at a line break in the transcription); removed the Example 41 quotation from the body per convention."),
    # ---------- Stage 2: Integrated Practice ----------
    _it(2, "IP", 1, IP, "The Secrets of Years, Months, and Days", "Theme activity 1",
        "Learn the 24-hour clock; learn about years, months, and days and how they relate; use this knowledge to explain everyday problems and begin to apply it. Learn how people in ancient China understood the four seasons and explore China's outstanding traditional culture."),
    _it(2, "IP", 2, IP, "The Story of Cao Chong Weighing an Elephant", "Theme activity 2",
        "Using the story of Cao Chong weighing an elephant as a starting point and real-world materials, explore grams, kilograms, and metric tons and how they relate; understand that quantities equal to the same quantity are equal, develop a sense of measurement and reasoning, and gain experience with mathematical activities."),
    _it(2, "IP", 3, IP, "Finding the Treasure", "Theme activity 3",
        "In everyday contexts, learn northeast, northwest, southeast, and southwest; understand directions described by clock positions, describe the direction of an object, and develop spatial reasoning."),
    _it(2, "IP", 4, IP, "The Story of Weights and Measures", "Theme activity 4",
        "Learn that China unified weights and measures during the Qin dynasty; consult sources to understand the significance of metrology, learn that early measurement methods used everyday objects, and deepen understanding of quantities and units while developing a richer sense of measurement."),
    # ---------- Stage 3: Number and Algebra ----------
    _it(3, "NA", 1, NA, "Number and Operations", "(1)",
        "Learn the divisibility criteria for 2, 3, and 5; learn common multiples and least common multiples, common factors and greatest common factors, and odd, even, prime, and composite numbers."),
    _it(3, "NA", 2, NA, "Number and Operations", "(2)",
        "Explore and understand the meanings of decimals and fractions in concrete contexts and learn about units of counting; convert between decimals and fractions, further developing number sense and symbol awareness."),
    _it(3, "NA", 3, NA, "Number and Operations", "(3)",
        "Understand the relationship between integer division and fractions in concrete contexts."),
    _it(3, "NA", 4, NA, "Number and Operations", "(4)",
        "Perform simple arithmetic and mixed operations with decimals and fractions; recognize the consistency of operations and develop computational fluency and reasoning awareness."),
    _it(3, "NA", 5, NA, "Quantitative Relationships", "(1)",
        "Understand the basic properties of equality in concrete contexts."),
    _it(3, "NA", 6, NA, "Quantitative Relationships", "(2)",
        "Choose an appropriate method of estimation when solving real-world problems."),
    _it(3, "NA", 7, NA, "Quantitative Relationships", "(3)",
        "Explore ways to use letters to represent relationships, properties, and patterns in concrete contexts; understand how letters express generality."),
    _it(3, "NA", 8, NA, "Quantitative Relationships", "(4)",
        "Understand ratios, proportions, and proportional allocation in real-world contexts, and solve simple related problems."),
    _it(3, "NA", 9, NA, "Quantitative Relationships", "(5)",
        "Use concrete contexts to recognize directly proportional quantities (e.g., y/x = 5); explore patterns or trends (e.g., y = 5x).",
        "2026-10-21: Restored (e.g., y/x = 5) based on printed page 24 of the official PDF (omitted from the original transcription); the formula is written as y/x = 5 per project convention, and Examples 20 and 21 were removed from the body."),
    _it(3, "NA", 10, NA, "Quantitative Relationships", "(6)",
        "Use common quantitative relationships to solve real-world problems, explain the real-world meaning of the results, gradually develop modeling awareness and geometric intuition, and improve problem-solving ability.",
        "2026-10-21: Restored this clause, which was present in the 2022 edition but omitted when the original preview transcription was cut off after (5).",
        "Transcribed from the 2025 routine revision; restored on 2026-10-21 because this clause was missing from the original 2022-edition data."),
    # ---------- Stage 3: Geometry and Measurement ----------
    _it(3, "GG", 1, GG, "Shape Recognition and Measurement", "(1)",
        "Know that the sum of any two sides of a triangle is greater than the third side; know that the interior angles of a triangle sum to 180°."),
    _it(3, "GG", 2, GG, "Shape Recognition and Measurement", "(2)",
        "Learn circles and sectors, draw circles with a compass, learn about pi, and explore formulas for circumference and area; solve simple real-world problems."),
    _it(3, "GG", 3, GG, "Shape Recognition and Measurement", "(3)",
        "Learn the kilometer and hectare as area units; explore and master formulas for the areas of parallelograms, triangles, and trapezoids; estimate the areas of irregular shapes.",
        "The transcription lists kilometer and hectare as area units; square-unit superscripts may have been lost. Needs verification."),
    _it(3, "GG", 4, GG, "Shape Recognition and Measurement", "(4)",
        "Understand the meaning of volume (or capacity) through examples, learn its units and convert between them, and experience methods for measuring the volume of irregular objects."),
    _it(3, "GG", 5, GG, "Shape Recognition and Measurement", "(5)",
        "Learn cuboids, cubes, and cylinders and their nets; explore and master formulas for their volume and surface area; learn cones and explore their volume formula; use these formulas to solve simple real-world problems."),
    _it(3, "GG", 6, GG, "Shape Recognition and Measurement", "(6)",
        "For simple objects, identify the shapes seen from different directions (front, side, and top)."),
    _it(3, "GG", 7, GG, "Shape Recognition and Measurement", "(7)",
        "Further develop a sense of measurement, spatial reasoning, and geometric intuition through learning about shapes and measurement."),
    _it(3, "GG", 8, GG, "Position and Movement of Shapes", "(1)",
        "Determine an object's position based on a reference point, direction, and distance; describe simple routes in real-world contexts."),
    _it(3, "GG", 9, GG, "Position and Movement of Shapes", "(2)",
        "Use ordered pairs (natural numbers only) to represent point positions; understand the correspondence between ordered pairs and points on grid paper."),
    _it(3, "GG", 10, GG, "Position and Movement of Shapes", "(3)",
        "Understand scale and use grid paper to enlarge or reduce simple shapes proportionally."),
    _it(3, "GG", 11, GG, "Position and Movement of Shapes", "(4)",
        "Translate or rotate simple shapes on grid paper; learn about symmetric shapes and axes of symmetry, and complete simple symmetric shapes on grid paper."),
    _it(3, "GG", 12, GG, "Position and Movement of Shapes", "(5)",
        "Appreciate everyday patterns through translation, rotation, and symmetry; design simple patterns on grid paper, appreciate mathematical beauty, and develop spatial reasoning."),
    # ---------- Stage 3: Statistics and Probability ----------
    _it(3, "SP", 1, SP, "Data Collection, Organization, and Representation", "(1)",
        "For a real-world problem, go through the process of collecting, organizing, and analyzing data, and give a reasonable account of the conclusions."),
    _it(3, "SP", 2, SP, "Data Collection, Organization, and Representation", "(2)",
        "Learn line graphs and pie charts; use bar graphs and line graphs to display relevant data and explain what they show.",
        "The phrase 'use' mentions only bar graphs and line graphs; the transcription may have been cut at a line break before a separate clause about pie charts. Needs verification."),
    _it(3, "SP", 3, SP, "Data Collection, Organization, and Representation", "(3)",
        "Obtain needed data from various media and interpret simple statistical charts and tables.",
        "2026-10-21: Restored this clause, which was present in the 2022 edition but omitted when the original preview transcription was cut off after (2).",
        "Transcribed from the 2025 routine revision; restored on 2026-10-21 because this clause was missing from the original 2022-edition data."),
    _it(3, "SP", 4, SP, "Data Collection, Organization, and Representation", "(4)",
        "Explore the meaning of percentages in concrete contexts, solve simple related real-world problems, and understand their statistical significance.",
        "2026-10-21: Restored this clause, which was present in the 2022 edition but omitted from the original transcription; percentages are an independent clause in this stage's content requirements.",
        "Transcribed from the 2025 routine revision; restored on 2026-10-21 because this clause was missing from the original 2022-edition data."),
    _it(3, "SP", 5, SP, "Data Collection, Organization, and Representation", "(5)",
        "Apply statistical charts or percentages in simple real-world contexts, developing data awareness and an initial awareness of how data can be applied.",
        "2026-10-21: Restored this clause, which was present in the 2022 edition but omitted from the original transcription.",
        "Transcribed from the 2025 routine revision; restored on 2026-10-21 because this clause was missing from the original 2022-edition data."),
    _it(3, "SP", 6, SP, "Likelihood of Random Events", "(1)",
        "Use examples to experience simple random phenomena and the possibilities of their outcomes.",
        "Original ID cms-2022:3.SP.03; renumbered to 06 on 2026-10-21 to follow clause order (after adding clauses (3), (4), and (5) under Data Collection, Organization, and Representation)."),
    _it(3, "SP", 7, SP, "Likelihood of Random Events", "(2)",
        "In real-world contexts, describe qualitatively how likely some simple random events are.",
        "Original ID cms-2022:3.SP.04; renumbered to 07 on 2026-10-21 to follow clause order."),
    # ---------- Stage 3: Integrated Practice ----------
    _it(3, "IP", 1, IP, "Expressing Quantities with Opposite Meanings", "Theme activity 1",
        "In familiar contexts, learn about quantities with opposite meanings; understand what negative numbers represent in context; recognize that negative numbers can represent quantities opposite to positive ones, further developing number sense."),
]

# The available transcription confirms only Theme activity 1 under Stage 3 Integrated Practice. Other theme titles have not been verified in the body and are not listed separately.
# 2026-10-21: A review of the full Compulsory Education Mathematics Curriculum Standards (2022 edition, revised in 2025) confirmed four additional Stage 3 content clauses:
# Quantitative Relationships (6) and Data Collection, Organization, and Representation (3), (4), and (5). These were present in the 2022 edition but omitted because the preview transcription ended after (5)/(2);
# they have now been added. Percentages are indeed a separate clause. Remaining items to verify are listed in docs/moe2025-alignment.md.
