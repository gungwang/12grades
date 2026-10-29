# -*- coding: utf-8 -*-
"""Topics from the second half of Grade 5 and Grade 6. Continues primary_g46.py."""
from primary_qgen import calc, story, ask, fact, choice_num

NA, GG, SP, IP = "Number and Algebra", "Geometry and Measurement", "Statistics and Probability", "Integrated Practice"
TOPICS = []


def U(grade, sem, n, uname, ip=False):
    def add(slug, name, dom, typ, desc, mc, std, pre, qs):
        built = []
        for q in qs:
            k = q[0]
            if k == "c":
                built.append(calc(q[1], q[2], q[3], q[4], q[5] if len(q) > 5 else False))
            elif k == "s":
                built.append(story(q[1], q[2], q[3], q[4], q[5], q[6] if len(q) > 6 else False))
            elif k == "a":
                built.append(ask(q[1], q[2], q[3], q[4]))
            elif k == "f":
                built.append(fact(q[1], list(q[2]), q[3], q[4], q[5] if len(q) > 5 else "basic"))
            elif k == "n":
                built.append(choice_num(q[1], q[2], list(q[3]), q[4], q[5]))
            else:
                raise ValueError(k)
        TOPICS.append({
            "slug": slug, "name": name, "domain": dom, "grade": grade, "semester": sem,
            "unit": n, "uname": uname, "ip": ip, "type": typ, "description": desc,
            "mastery_criteria": mc, "standards": std, "pre": pre, "qs": built,
            "root_reason": None,
        })
    return add


def S(*codes):
    return list(codes)


a = U(5, "Second semester", 4, "Meaning and Properties of Fractions")
a("frac_kind", "Proper, Improper, and Mixed Numbers", NA, "conceptual",
  "Distinguish proper and improper fractions and know that a fraction with a smaller numerator than denominator is less than 1.",
  ["Identify a fraction with a smaller numerator than denominator as proper", "Determine whether a fraction is improper"],
  S("3.NA.02"), ["frac_meaning"], [
    ("f", "What kind of fraction has a numerator smaller than its denominator?",
     ["Proper fraction", "Improper fraction", "Mixed number"],
     "Proper fraction", "A proper fraction is less than 1 because its numerator is smaller than its denominator.", "basic"),
    ("c", "7/4", "7÷4", "basic", "7÷4=7/4. The numerator is greater than the denominator, so it is an improper fraction."),
    ("a", "First write the quotient, then the remainder. Find both for 9÷4.", "(9//4, 9%4)", "standard", "9÷4=2 remainder 1, so 9/4=2 1/4."),
    ("c", "8/8", "8÷8", "standard", "8÷8=1; an improper fraction can equal 1."),
  ])

a("frac_basic", "Fundamental Property of Fractions", NA, "reasoning",
  "Multiplying or dividing both the numerator and denominator by the same nonzero number does not change a fraction's value.",
  ["Multiply a fraction's numerator and denominator by the same number", "Explain that this does not change the fraction's value"],
  S("3.NA.02"), ["frac_meaning", "div_stable"], [
    ("c", "1*3", "1×3", "basic", "Multiply both the numerator and denominator of 1/2 by 3. What is the new numerator?"),
    ("c", "2*3", "2×3", "basic", "Multiply the denominator 2 by 3 as well to get 6, so 1/2=3/6."),
    ("s", "Divide both the numerator and denominator of 4/8 by 4. What is the new numerator?", "4/4", "4÷4", "standard", "4÷4=1, so 4/8=1/2."),
    ("n", "6÷3", "6/3", ["1", "3", "4"], "standard", "Divide the numerator and denominator of 6/9 by 3; the new numerator is 2."),
  ])

a("frac_reduce", "Reducing Fractions", NA, "procedural",
  "Reduce a fraction to its simplest form, with relatively prime numerator and denominator.",
  ["Find a common factor of the numerator and denominator", "Reduce a fraction to simplest form"],
  S("3.NA.02"), ["frac_basic", "gcd"], [
    ("c", "6/8", "6÷8", "basic", "The greatest common divisor of 6 and 8 is 2, so 6/8=3/4."),
    ("c", "4/10", "4÷10", "basic", "4/10=2/5."),
    ("s", "Reduce 8/12. First find the greatest common divisor of 8 and 12. What is 12÷4?", "12/4", "12÷4", "standard", "The greatest common divisor is 4. Since 12÷4=3, 8/12=2/3."),
    ("n", "9÷3", "9/3", ["2", "6", "12"], "standard", "Divide the numerator and denominator of 9/15 by 3; the numerator becomes 3."),
  ])

a("frac_cmp", "Comparing Fractions", NA, "procedural",
  "Compare fractions with the same denominator or numerator. With different denominators, first rewrite them using a common denominator.",
  ["Compare fractions with a common denominator", "Compare fractions with a common numerator"],
  S("3.NA.02"), ["frac_reduce", "frac_basic"], [
    ("c", "3/5-1/5", "3/5－1/5", "basic", "The denominators are the same. 3/5 is greater than 1/5 by 2/5."),
    ("c", "1/2-1/3", "1/2－1/3", "basic", "With a common denominator, 3/6 is greater than 2/6 by 1/6."),
    ("s", "One piece of rope has 3/8 used and another has 5/8 used. Which has more used? First find the difference.", "5/8-3/8", "5/8－3/8", "standard", "5/8−3/8=2/8=1/4."),
    ("n", "4/7−2/7", "4/7-2/7", ["1/7", "3/7", "6/7"], "standard", "4/7−2/7=2/7."),
  ])

a("frac_to_dec", "Converting Between Fractions and Decimals", NA, "procedural",
  "Write fractions with denominators of 10 or 100 as decimals, and write terminating decimals as fractions.",
  ["Write tenths as one-place decimals", "Write one-place decimals as tenths"],
  S("3.NA.02"), ["frac_meaning", "dec_meaning"], [
    ("c", "3/10", "3÷10", "basic", "3/10=0.3.", True),
    ("c", "25/100", "25÷100", "basic", "25/100=0.25.", True),
    ("s", "How many 0.1s are in 0.7?", "0.7/0.1", "0.7÷0.1", "standard", "0.7=7/10.", True),
    ("c", "4/10", "4÷10", "standard", "4/10=0.4.", True),
  ])

a = U(5, "Second semester", 5, "Transformations of Figures (III)")
a("rotate", "Rotation", GG, "conceptual",
  "Understand rotation and know that a figure's size and shape do not change when it is rotated.",
  ["State that rotation preserves size and shape", "Describe a rotation as clockwise or counterclockwise"],
  S("3.GG.11", "2.GG.08"), ["translate", "reflect", "angle_measure"], [
    ("f", "What happens to a figure's size and shape after rotation?",
     ["Both its size and shape stay the same", "It always gets larger", "Its shape always changes"],
     "Both its size and shape stay the same", "Rotation changes only the figure's position and orientation.", "basic"),
    ("c", "90+90", "90＋90", "basic", "A 90-degree clockwise turn followed by another 90-degree turn is a total rotation of 180 degrees."),
    ("s", "The hour hand moves from 12 to 3, a 90-degree turn. How many more degrees does it turn to reach 6?", "90+0", "90＋0", "standard", "The move from 3 to 6 is another 90 degrees."),
    ("n", "360÷4", "360/4", ["60", "80", "120"], "standard", "One quarter of a full 360-degree turn is 90 degrees."),
  ])

a = U(5, "Second semester", 6, "Adding and Subtracting Fractions")
a("frac_lcd", "Finding a Common Denominator", NA, "procedural",
  "Rewrite fractions with different denominators using a common denominator, often the least common multiple of the denominators.",
  ["Find the least common multiple of two denominators", "Rewrite two fractions with the same denominator"],
  S("3.NA.04"), ["frac_basic", "lcm"], [
    ("c", "2*3", "2×3", "basic", "The least common multiple of 2 and 3 is 6, so use 6 as the common denominator."),
    ("c", "4*2", "4×2", "basic", "Multiply the numerator and denominator of 1/4 by 2 to get 2/8."),
    ("s", "To give 1/6 and 1/3 a common denominator, use 6. By what number must the denominator of 1/3 be multiplied?", "6/3", "6÷3", "standard", "6÷3=2, so 1/3=2/6."),
    ("n", "3×4", "3*4", ["7", "9", "16"], "standard", "The least common multiple of 3 and 4 is 12."),
  ])

a("frac_add", "Adding and Subtracting Unlike Fractions", NA, "procedural",
  "Add and subtract fractions with different denominators by first rewriting them with a common denominator.",
  ["Find a common denominator before adding", "Find a common denominator before subtracting"],
  S("3.NA.04"), ["frac_lcd", "frac_same_add"], [
    ("c", "1/2+1/4", "1/2＋1/4", "basic", "1/2=2/4, and 2/4+1/4=3/4."),
    ("c", "1/2-1/3", "1/2－1/3", "basic", "1/2=3/6 and 1/3=2/6, a difference of 1/6."),
    ("s", "Wheat covers 1/2 of a field and corn covers 1/3. What fraction of the field do they cover altogether?", "1/2+1/3", "1/2＋1/3", "standard", "1/2+1/3=3/6+2/6=5/6."),
    ("n", "3/4−1/2", "3/4-1/2", ["1/8", "1/2", "5/4"], "standard", "3/4−2/4=1/4."),
  ])

a("frac_mix", "Mixed Fraction Addition and Subtraction", NA, "procedural",
  "Calculate mixed addition and subtraction with fractions, evaluating parentheses first.",
  ["Calculate fraction addition and subtraction from left to right", "Evaluate fractions in parentheses first"],
  S("3.NA.04"), ["frac_add", "paren"], [
    ("c", "1/2+1/4-1/4", "1/2＋1/4－1/4", "basic", "Adding and then subtracting 1/4 leaves 1/2."),
    ("c", "3/4-1/4+1/2", "3/4－1/4＋1/2", "basic", "3/4−1/4=1/2, then adding 1/2 gives 1."),
    ("s", "A cup of water is partly drunk: 1/5 first, then another 2/5. What fraction has been drunk in total?", "1/5+2/5", "1/5＋2/5", "standard", "1/5+2/5=3/5."),
    ("n", "5/6−1/6−1/6", "5/6-1/6-1/6", ["1/6", "2/3", "5/6"], "standard", "5/6−1/6−1/6=3/6=1/2."),
  ])

a = U(5, "Second semester", 7, "Line Graphs")
a("line_chart", "Line Graphs", SP, "procedural",
  "Read line graphs and identify increases and decreases in quantities.",
  ["Read the quantity for a given day", "Describe whether a quantity is rising or falling"],
  S("3.SP.02"), ["bar", "mean"], [
    ("f", "What are line graphs useful for showing?",
     ["Changes in quantities", "How much each part contributes to a whole", "Only which value is largest"],
     "Changes in quantities", "An upward segment indicates an increase; a downward segment indicates a decrease.", "basic"),
    ("c", "18-12", "18－12", "basic", "The value rises from 12 on the previous day to 18 on the next day, an increase of 6."),
    ("s", "Twenty books were borrowed on Monday and 15 on Tuesday. How many fewer books were borrowed on Tuesday?", "20-15", "20－15", "standard", "20−15=5."),
    ("n", "8＋6＋4", "8+6+4", ["14", "16", "20"], "standard", "The quantities for three days are 8, 6, and 4, for a total of 18."),
  ])

a = U(5, "Second semester", 8, "Math Corner: Finding the Defective Item")
a("find_bad", "Finding the Defective Item", IP, "reasoning",
  "When using a balance to find a heavier or lighter defective item, divide the items into three groups for each weighing whenever possible.",
  ["Explain that items should be divided into three groups at each weighing", "Calculate the minimum number of weighings"],
  S(("3.NA.06", "Finding the Defective Item is a Math Corner topic in the current Grade 5 second-semester textbook; the content requirement has no matching title. To verify.")),
  ["mix_order", ("chance", "soft")], [
    ("f", "When looking for the defective item, what should you do at each step?",
     ["Divide the items into three groups to weigh", "Weigh only one item each time", "Weigh them all together once"],
     "Divide the items into three groups to weigh", "Place one group on each side of the balance and leave the third group off.", "basic"),
    ("c", "9/3", "9÷3", "basic", "Divide 9 parts into 3 groups, with 3 in each group."),
    ("s", "There are 81 parts, divided into 3 groups at each step. How many are in each group for the first weighing?", "81/3", "81÷3", "standard", "81÷3=27."),
    ("n", "27÷3", "27/3", ["6", "8", "12"], "standard", "27÷3=9."),
  ])

a = U(6, "First semester", 1, "Multiplication of Fractions")
a("frac_mul_int", "Multiplying a Fraction by an Integer", NA, "procedural",
  "Multiply the numerator by the integer to form the new numerator, keeping the denominator unchanged.",
  ["Multiply a fraction by an integer", "Reduce the result to simplest form"],
  S("3.NA.04"), ["frac_add", "frac_reduce"], [
    ("c", "2/7*3", "2/7×3", "basic", "2/7×3=6/7."),
    ("c", "3/4*2", "3/4×2", "basic", "3/4×2=6/4=3/2."),
    ("s", "Each bottle contains 3/5 liter of juice. How many liters are in 4 bottles?", "3/5*4", "3/5×4", "standard", "3/5×4=12/5."),
    ("n", "1/2×6", "1/2*6", ["2", "4", "6"], "standard", "1/2×6=3."),
  ])

a("frac_mul", "Multiplying Fractions", NA, "procedural",
  "Multiply fractions by multiplying the numerators and multiplying the denominators.",
  ["Multiply one fraction by another", "Reduce the result before writing the answer"],
  S("3.NA.04"), ["frac_mul_int", "dec_mul"], [
    ("c", "1/2*1/3", "1/2×1/3", "basic", "1/2×1/3=1/6."),
    ("c", "2/3*3/4", "2/3×3/4", "basic", "2/3×3/4=1/2."),
    ("s", "Half of a road has been paved, and 2/3 of that portion was paved in the morning. What fraction of the whole road was paved in the morning?", "1/2*2/3", "1/2×2/3", "standard", "1/2×2/3=1/3."),
    ("n", "3/5×5/6", "3/5*5/6", ["1/3", "2/3", "5/6"], "standard", "3/5×5/6=1/2."),
  ])

a("frac_mul_app", "Applications of Fraction Multiplication", NA, "application",
  "Use fraction multiplication to find a given fraction of a number.",
  ["Write 'a fraction of a number' as a multiplication expression", "Calculate and simplify the result"],
  S("3.NA.04", "3.NA.08"), ["frac_mul", "qty_rel"], [
    ("c", "20*1/4", "20×1/4", "basic", "1/4 of 20 is 5."),
    ("c", "18*2/3", "18×2/3", "basic", "2/3 of 18 is 12."),
    ("s", "A container holds 30 liters of oil, and 2/5 of it is used. How many liters are used?", "30*2/5", "30×2/5", "standard", "30×2/5=12."),
    ("n", "24×3/8", "24*3/8", ["6", "8", "12"], "standard", "24×3/8=9."),
  ])

a = U(6, "First semester", 2, "Position and Direction (II)")
a("dir_dist", "Locating a Place by Direction and Distance", GG, "application",
  "Locate an object using direction and distance, and describe a simple route.",
  ["Identify direction and distance as the two needed pieces of information", "Calculate a route length from directions and distances"],
  S("3.GG.08"), ["dir8", "coord_pair", "line_seg"], [
    ("c", "300+200", "300＋200", "basic", "Travel 300 meters east, then 200 meters north: the two segments total 500 meters."),
    ("c", "500-120", "500－120", "basic", "The planned route was 500 meters, but 120 meters were skipped, leaving 380 meters."),
    ("s", "A school is 800 meters northeast of a store, at 40° east of north. What is the distance only, in meters?", "800+0", "800＋0", "standard", "The distance is 800 meters."),
    ("n", "150＋250", "150+250", ["300", "350", "500"], "standard", "150＋250=400."),
  ])

a("route", "Describing a Simple Route", GG, "application",
  "Describe a route from one place to another using directions and distances, and calculate the total distance from a route map.",
  ["State the direction of each segment in order", "Add the lengths of all route segments"],
  S("3.GG.08"), ["dir_dist"], [
    ("c", "200+150+50", "200＋150＋50", "basic", "The three segments are 200, 150, and 50 meters, for a total of 400 meters."),
    ("c", "400-250", "400－250", "basic", "The route is 400 meters long. After walking 250 meters, 150 meters remain."),
    ("s", "Travel 120 meters east, then 80 meters south. What is the total distance?", "120+80", "120＋80", "standard", "120＋80=200."),
    ("n", "90＋60", "90+60", ["120", "140", "160"], "standard", "90＋60=150."),
  ])

a = U(6, "First semester", 3, "Dividing Fractions")
a("frac_div_int", "Dividing a Fraction by an Integer", NA, "procedural",
  "Divide a fraction by an integer by multiplying by the integer's reciprocal.",
  ["Explain that division by an integer equals multiplication by its reciprocal", "Divide a fraction by an integer"],
  S("3.NA.04", "3.NA.03"), ["frac_mul", "div_mean"], [
    ("c", "4/5/2", "4/5÷2", "basic", "4/5÷2=4/5×1/2=2/5."),
    ("c", "6/7/3", "6/7÷3", "basic", "6/7÷3=2/7."),
    ("s", "A 3/4-meter rope is cut equally into 3 pieces. How many meters long is each piece?", "(3/4)/3", "3/4÷3", "standard", "3/4÷3=1/4."),
    ("n", "8/9÷4", "8/9/4", ["1/9", "4/9", "8/9"], "standard", "8/9÷4=2/9."),
  ])

a("frac_div", "Dividing by a Fraction", NA, "procedural",
  "Divide by a fraction by multiplying by its reciprocal.",
  ["Explain that division by a fraction equals multiplication by its reciprocal", "Divide fractions and simplify the result"],
  S("3.NA.04"), ["frac_div_int", "frac_mul"], [
    ("c", "(3/4)/(1/2)", "(3/4)÷(1/2)", "basic", "3/4÷1/2=3/4×2/1=3/2."),
    ("c", "(2/3)/(4/5)", "(2/3)÷(4/5)", "basic", "2/3÷4/5=2/3×5/4=5/6."),
    ("s", "A sheet is 6/7 of a unit long. How many 2/7-unit pieces can it be divided into?", "(6/7)/(2/7)", "(6/7)÷(2/7)", "standard", "6/7÷2/7=3."),
    ("n", "(5/6)÷(5/12)", "(5/6)/(5/12)", ["1/2", "1", "5/2"], "standard", "5/6÷5/12=2."),
  ])

a("frac_div_app", "Applications of Fraction Division", NA, "application",
  "Use fraction division to find a unit quantity or determine how many fractional groups fit into a number.",
  ["Identify the amount corresponding to a fraction and find the whole", "Set up and calculate the expression"],
  S("3.NA.04", "3.NA.08"), ["frac_div", "frac_mul_app"], [
    ("c", "12/(3/4)", "12÷(3/4)", "basic", "If 3/4 of a number is 12, the number is 12÷3/4=16."),
    ("c", "6/(2/5)", "6÷(2/5)", "basic", "6÷2/5=15."),
    ("s", "A road is 2/5 complete, which is 8 kilometers. How long is the entire road?", "8/(2/5)", "8÷(2/5)", "standard", "8÷2/5=20."),
    ("n", "9÷(3/5)", "9/(3/5)", ["5", "12", "27"], "standard", "9÷3/5=15."),
  ])

a = U(6, "First semester", 4, "Ratio")
a("ratio", "Meaning of a Ratio", NA, "conceptual",
  "Understand that a ratio represents the division relationship between two numbers. The first term divided by the second is the ratio value.",
  ["Explain that the first term divided by the second gives the ratio value", "Find the value of a simple ratio"],
  S("3.NA.08"), ["frac_div", "div_2d"], [
    ("f", "What is the result of dividing the first term of a ratio by the second?",
     ["The ratio value", "The first term", "The second term"],
     "The ratio value", "First term ÷ second term = ratio value.", "basic"),
    ("a", "What is the value of the ratio 6:8?", "Fraction(6,8)", "basic", "6÷8=3/4."),
    ("a", "What is the value of the ratio 12:4?", "Fraction(12,4)", "standard", "12÷4=3."),
    ("n", "10÷2", "10/2", ["4", "8", "12"], "standard", "The value of the ratio 10:2 is 5."),
  ])

a("ratio_simple", "Simplifying Ratios", NA, "procedural",
  "Reduce a ratio to simplest whole-number terms by dividing both terms by their greatest common divisor.",
  ["Find the greatest common divisor of the two terms", "Write the first term of a ratio in simplest form"],
  S("3.NA.08"), ["ratio", "gcd"], [
    ("a", "After simplifying the ratio 12:8 to lowest whole-number terms, what is its first term?", "12//gcd(12,8)", "basic", "The greatest common divisor of 12 and 8 is 4, so the first term is 3."),
    ("a", "After simplifying the ratio 15:10 to lowest whole-number terms, what is its first term?", "15//gcd(15,10)", "basic", "The greatest common divisor is 5, so the first term is 3."),
    ("a", "After simplifying the ratio 18:12 to lowest whole-number terms, what is its first term?", "18//gcd(18,12)", "standard", "The greatest common divisor is 6, so the first term is 3."),
    ("n", "20÷4", "20/4", ["4", "6", "8"], "standard", "After reducing 20:4, the first term is 20÷4=5, giving the ratio 5:1."),
  ])

a("ratio_share", "Dividing a Quantity in a Given Ratio", NA, "application",
  "Divide a total quantity into parts according to a given ratio.",
  ["Find the value of one part", "Calculate each portion using the ratio"],
  S("3.NA.08"), ["ratio_simple", "frac_mul_app"], [
    ("c", "30/(2+3)*2", "30÷(2＋3)×2", "basic", "There are 5 parts in total, so each part is 6; the first 2 parts total 12."),
    ("c", "40/(1+3)", "40÷(1＋3)", "basic", "There are 4 parts in total, so each is 10."),
    ("s", "Divide 56 notebooks between two classes in the ratio 3:4. First find the number of notebooks per part.", "56/(3+4)", "56÷(3＋4)", "standard", "56÷7=8, so each part is 8 notebooks."),
    ("n", "90÷(2＋3)", "90/(2+3)", ["15", "20", "30"], "standard", "90÷5=18."),
  ])

a = U(6, "First semester", 5, "Circles")
a("circle", "Understanding Circles", GG, "conceptual",
  "Identify the center, radius, and diameter of a circle, draw circles with a compass, and know that all radii of the same circle are equal.",
  ["Explain that every point on a circle is one radius from the center", "Know that the diameter is twice the radius"],
  S("3.GG.02"), ["line_seg"], [
    ("f", "What is the distance from a point on a circle to its center?",
     ["It is always one radius", "It varies", "It is twice the diameter"],
     "It is always one radius", "All radii in a circle have the same length.", "basic"),
    ("c", "4*2", "4×2", "basic", "A circle with radius 4 centimeters has a diameter of 8 centimeters."),
    ("s", "A circle has a diameter of 10 centimeters. What is its radius in centimeters?", "10/2", "10÷2", "standard", "10÷2=5."),
    ("n", "6×2", "6*2", ["8", "10", "16"], "standard", "A circle with radius 6 centimeters has a diameter of 12 centimeters."),
  ])

a("pi", "Pi", NA, "conceptual",
  "Know that pi is the ratio of a circle's circumference to its diameter and can be approximated as 3.14 for calculations.",
  ["State that pi is approximately 3.14", "Estimate circumference by multiplying the diameter by 3.14"],
  S("3.GG.02"), ["circle", "dec_mul", "ratio"], [
    ("f", "What is the approximate value of pi?",
     ["3.14", "3.41", "31.4"],
     "3.14", "Circumference ÷ diameter ≈ 3.14. Use 314/100 for this calculation.", "basic"),
    ("c", "10*314/100", "10×314/100", "basic", "A circle with a 10-centimeter diameter has a circumference of about 31.4 centimeters.", True),
    ("s", "What is the approximate circumference of a circle with a 2-centimeter diameter? Use pi = 314/100.", "2*314/100", "2×314/100", "standard", "2×3.14=6.28.", True),
    ("c", "5*314/100", "5×314÷100", "standard", "A circle with a 5-centimeter diameter has a circumference of about 15.7 centimeters.", True),
  ])

a("circ", "Circumference of a Circle", GG, "procedural",
  "Find a circle's circumference by multiplying the diameter by pi or doubling the radius and multiplying by pi.",
  ["Find circumference from the radius", "Find circumference from the diameter"],
  S("3.GG.02"), ["pi"], [
    ("a", "What is the circumference of a circle with a radius of 2 centimeters? Use pi = 314/100.", "Fraction(2*314*2,100)", "basic", "2×3.14×2=12.56."),
    ("a", "What is the circumference of a circle with a radius of 5 centimeters? Use pi = 314/100.", "Fraction(2*314*5,100)", "basic", "2×3.14×5=31.4."),
    ("s", "A circle has a diameter of 4 centimeters. First find its radius. What is the radius in centimeters?", "4/2", "4÷2", "standard", "The radius is 2 centimeters; multiply 2×3.14 to find the circumference."),
    ("c", "2*314*1/100", "2×314×1÷100", "standard", "A circle with a 1-centimeter radius has a circumference of 6.28 centimeters.", True),
  ])

a("circ_app", "Applications of Circumference", GG, "application",
  "Use circumference to solve problems about a wheel rolling one turn or the distance around a circular garden.",
  ["Recognize when a problem asks for one circumference", "Substitute a radius or diameter to calculate"],
  S("3.GG.02"), ["circ", "qty_rel"], [
    ("a", "What is the circumference of a circle with a 1-centimeter radius? Use pi = 314/100.", "Fraction(2*314*1,100)", "basic", "A wheel with a 1-centimeter radius rolls about 6.28 centimeters in one turn."),
    ("c", "314/100*10", "314/100×10", "basic", "A circle with a 10-centimeter diameter has a circumference of about 31.4 centimeters.", True),
    ("s", "A circular garden has a diameter of 20 meters. About how many meters of fence are needed to go around it once? Use pi = 314/100.", "20*314/100", "20×314/100", "standard", "20×3.14=62.8.", True),
    ("c", "4*314/100", "4×314÷100", "standard", "A circle with a 4-centimeter diameter has a circumference of 12.56 centimeters.", True),
  ])

a("circ_area", "Area of a Circle", GG, "procedural",
  "Find the area of a circle by multiplying the radius by itself and then by pi.",
  ["State that a circle's area is calculated from its radius", "Calculate a simple circle area"],
  S("3.GG.02"), ["circ", "rect_area"], [
    ("a", "What is the area of a circle with a 2-centimeter radius, in square centimeters? Use pi = 314/100.", "Fraction(314*2*2,100)", "basic", "3.14×4=12.56."),
    ("a", "What is the area of a circle with a 10-centimeter radius, in square centimeters? Use pi = 314/100.", "Fraction(314*10*10,100)", "basic", "3.14×100=314."),
    ("s", "A circle has a radius of 5 centimeters. First multiply the radius by itself. What is 5×5?", "5*5", "5×5", "standard", "5×5=25; multiply by 3.14 to find the area."),
    ("c", "314*1*1/100", "314×1×1÷100", "standard", "A circle with a 1-centimeter radius has an area of 3.14 square centimeters.", True),
  ])

a("sector", "Understanding Sectors", GG, "conceptual",
  "A sector is bounded by two radii and the arc between them.",
  ["Identify the two radii of a sector", "Compare sectors and know that a larger central angle gives a larger sector"],
  S("3.GG.02"), ["circle", "angle_class"], [
    ("c", "2+1", "2＋1", "basic", "A sector has 2 radii and 1 arc, for a total of 3 boundary parts."),
    ("c", "90/360", "90÷360", "basic", "A 90-degree central angle is 1/4 of a full 360-degree circle.", True),
    ("s", "A central angle is 180 degrees. What fraction of a full circle is this? First calculate 180÷360.", "180/360", "180÷360", "standard", "180÷360=0.5, or half of the full circle.", True),
    ("n", "60÷30", "60/30", ["1", "3", "90"], "standard", "60 degrees is twice 30 degrees."),
  ])

a = U(6, "First semester", 6, "Percentages (I)")
a("pct_meaning", "Meaning of a Percentage", NA, "conceptual",
  "Understand that a percentage expresses how many hundredths one number is of another.",
  ["Explain that a percentage expresses the ratio between two numbers", "Read a percentage"],
  S(("3.NA.04", "Percentages appear in the third-stage objectives and teaching guidance, but not as a separate numbered content requirement in the material reviewed. To verify.")),
  ["frac_meaning", "dec_meaning", "ratio"], [
    ("f", "What does a percentage represent?",
     ["How many hundredths one number is of another", "An amount of money only", "An increase only"],
     "How many hundredths one number is of another", "50% means fifty per hundred.", "basic"),
    ("a", "What is 50% of 100?", "Fraction(100*50,100)", "basic", "Half of 100 is 50."),
    ("c", "25/100", "25÷100", "standard", "25%=25/100=0.25.", True),
    ("n", "1×100", "1*100", ["10", "50", "1000"], "standard", "100% of 1 is 100."),
  ])

a("pct_convert", "Converting Between Percentages, Fractions, and Decimals", NA, "procedural",
  "Convert percentages to fractions or decimals and decimals to percentages.",
  ["Convert a percentage to a decimal", "Convert a decimal to a percentage"],
  S(("3.NA.02", "The content requirement mentions conversions between decimals and fractions but does not explicitly name percentages. To verify.")),
  ["pct_meaning", "frac_to_dec"], [
    ("c", "25/100", "25÷100", "basic", "25%=0.25.", True),
    ("c", "0.4*100", "0.4×100", "basic", "0.4=40%. This calculation gives the number before the percent sign.", True),
    ("s", "Convert 3/4 to a percentage by first writing it as a decimal. What is 3÷4?", "3/4", "3÷4", "standard", "3÷4=0.75, which is 75%.", True),
    ("c", "8/100", "8÷100", "standard", "8%=0.08.", True),
  ])

a("pct_of", "Finding a Percentage of a Number", NA, "procedural",
  "Find a given percentage of a number.",
  ["Convert the percentage to a decimal or fraction and multiply", "Calculate the result"],
  S(("3.NA.04", "Finding a percentage of a number is a basic percentage calculation, but the content requirement does not explicitly name percentages. To verify.")),
  ["pct_convert", "frac_mul_app"], [
    ("a", "What is 25% of 80?", "Fraction(80*25,100)", "basic", "80×0.25=20."),
    ("a", "What is 10% of 200?", "Fraction(200*10,100)", "basic", "200×0.1=20."),
    ("a", "What is 50% of 60?", "Fraction(60*50,100)", "standard", "Half of 60 is 30."),
    ("n", "40×5/100", "40*5/100", ["1", "4", "20"], "standard", "5% of 40 is 2."),
  ])

a("pct_rate", "Finding a Percentage Rate", NA, "application",
  "Find what percentage one number is of another.",
  ["Divide the part by the whole", "Write the result as a percentage"],
  S(("3.NA.08", "Finding a percentage rate applies ratios and percentages, but the content requirement mentions ratios without explicitly naming percentages. To verify.")),
  ["pct_of", "ratio"], [
    ("c", "20/80*100", "20÷80×100", "basic", "20 is 25% of 80. The calculation gives 25."),
    ("c", "15/50*100", "15÷50×100", "basic", "15 is 30% of 50."),
    ("s", "Ten of 40 students met the target. What percentage met the target? First calculate 10÷40×100.", "10/40*100", "10÷40×100", "standard", "10÷40×100=25, or 25%."),
    ("n", "6÷20×100", "6/20*100", ["20", "26", "40"], "standard", "6 is 30% of 20."),
  ])

a("pct_find", "Finding the Whole from a Percentage", NA, "application",
  "Find the whole when a given percentage of it is known.",
  ["Recognize that division is used to find the whole", "Calculate the original number"],
  S(("3.NA.04", "Finding the original number from a percentage is an application not explicitly named in the content requirement. To verify.")),
  ["pct_of", "frac_div_app"], [
    ("c", "20/0.4", "20÷0.4", "basic", "If 40% of a number is 20, the number is 50.", True),
    ("c", "30/0.5", "30÷0.5", "basic", "If 50% of a number is 30, the number is 60.", True),
    ("s", "A student has read 25% of a book, or 40 pages. How many pages does the book contain?", "40/0.25", "40÷0.25", "standard", "40÷0.25=160.", True),
    ("n", "18÷0.2", "18/0.2", ["3.6", "36", "180"], "standard", "If 20% of a number is 18, the number is 90."),
  ])

a = U(6, "First semester", 7, "Pie Charts")
a("pie", "Pie Charts", SP, "procedural",
  "Read pie charts to determine how much each category contributes to a whole.",
  ["Explain that a pie chart shows each part as a share of the whole", "Use a percentage to calculate the quantity in a category"],
  S(("3.SP.02", "The transcription explicitly names bar and line graphs under 'use'; whether a separate clause includes pie charts remains to be verified.")),
  ["pct_meaning", "bar", "sector"], [
    ("f", "What are pie charts useful for showing?",
     ["How much each part contributes to the whole", "How a quantity changes over time", "Only which value is largest"],
     "How much each part contributes to the whole", "The size of each sector represents its percentage.", "basic"),
    ("a", "What is 25% of 40?", "Fraction(40*25,100)", "basic", "The whole is 40, and 25% of it is 10."),
    ("s", "A class has 50 students, and 40% like soccer. How many students like soccer?", "50*40/100", "50×40÷100", "standard", "50×40÷100=20."),
    ("n", "200×30/100", "200*30/100", ["30", "50", "80"], "standard", "30% of 200 is 60."),
  ])

a = U(6, "First semester", 8, "Math Corner: Numbers and Shapes")
a("num_shape", "Numbers and Shapes", IP, "reasoning",
  "Use figures to discover patterns in simple sequences and find the next number.",
  ["State how many dots or shapes are added at each step", "Find the next term according to the pattern"],
  S(("3.NA.07", "Numbers and Shapes is a Math Corner topic in the current Grade 6 first-semester textbook; the content requirement has no matching title and is tentatively linked to representing patterns with letters or symbols.")),
  ["pattern2", ("rect_area", "soft")], [
    ("c", "1+3", "1＋3", "basic", "The sequence 1, 4, 9 does not add the same number each time: 1+3=4, and the next step adds 5. First calculate 1+3."),
    ("c", "4+5", "4＋5", "basic", "In 1, 4, 9, the next value after 4 is 9; it is found by adding 5."),
    ("s", "A square dot pattern goes 1, 4, 9. The next value is 9+7. What is 9+7?", "9+7", "9＋7", "standard", "The next square number is 16."),
    ("n", "16＋9", "16+9", ["20", "24", "36"], "standard", "4×4=16; adding 9 gives 25, or 5×5."),
  ])

a = U(6, "Second semester", 1, "Negative Numbers")
a("neg_know", "Understanding Negative Numbers", NA, "conceptual",
  "Recognize negative numbers in contexts such as temperature, elevation, income, and expenses, and know that they represent quantities opposite in meaning to positive numbers.",
  ["Explain that negative numbers represent quantities opposite in meaning to positive numbers", "Use a negative number to represent a temperature below zero"],
  S("3.IP.01"), ["know_wan", "dec_cmp"], [
    ("f", "What do negative numbers represent?",
     ["A quantity opposite in meaning to a positive quantity", "A number greater than 100", "Temperature only, and nothing else"],
     "A quantity opposite in meaning to a positive quantity", "Income can be represented by a positive number and expenses by a negative number.", "basic"),
    ("f", "How is a temperature below zero represented?",
     ["With a negative number", "Only with 0", "With a number greater than 10"],
     "With a negative number", "A temperature 3 degrees below zero is written as −3.", "basic"),
    ("s", "The temperature drops from 3 degrees above zero to 2 degrees below zero. By how many degrees did it drop?", "3+2", "3＋2", "standard", "It drops 3 degrees from +3 to 0, then another 2 degrees, for a total of 5 degrees."),
    ("n", "18＋4", "18+4", ["14", "18", "24"], "standard", "The room is 18 degrees and a freezer is 4 degrees below zero, a difference of 22 degrees."),
  ])

a("neg_use", "Using Negative Numbers for Opposite Quantities", NA, "application",
  "Use positive and negative numbers for quantities with opposite meanings, such as income and expenses or rising and falling.",
  ["Choose a positive direction", "Calculate the combined result of increases and decreases"],
  S("3.IP.01"), ["neg_know"], [
    ("c", "8-5", "8－5", "basic", "An income of 8 yuan and an expense of 5 yuan leave 3 yuan."),
    ("c", "6+3", "6＋3", "basic", "A 6-meter descent followed by a 3-meter descent is a total descent of 9 meters."),
    ("s", "An elevator rises 12 floors and then descends 5 floors. How many floors above its starting point is it?", "12-5", "12－5", "standard", "12−5=7."),
    ("n", "20−7", "20-7", ["12", "14", "27"], "standard", "After depositing 20 yuan and withdrawing 7 yuan, 13 yuan remains."),
  ])

a = U(6, "Second semester", 2, "Percentages (II)")
a("pct_discount", "Discounts", NA, "application",
  "Understand discounts and calculate the price after a discount.",
  ["Explain that an 80% price is 80% of the original price", "Calculate a discounted price"],
  S(("3.NA.04", "Discounts are an application of percentages, but the content requirement does not explicitly name percentages. To verify.")),
  ["pct_of"], [
    ("f", "What does an 80% discount price mean?",
     ["80% of the original price", "The original price plus 80 yuan", "8% of the original price"],
     "80% of the original price", "An 80% price means the item is sold for 80% of its original price.", "basic"),
    ("a", "An item originally costs 50 yuan. What is its price after a 20% discount?", "Fraction(50*8,10)", "basic", "50×0.8=40."),
    ("a", "An item originally costs 80 yuan. What is its price after a 10% discount?", "Fraction(80*9,10)", "standard", "80×0.9=72."),
    ("n", "200×7/10", "200*7/10", ["14", "70", "180"], "standard", "A 70% price is 70% of the original, so 200×0.7=140."),
  ])

a("interest", "Interest Rate", NA, "application",
  "Calculate simple interest for one year from the principal and interest rate.",
  ["State that interest = principal × interest rate", "Calculate one year's interest"],
  S(("3.NA.04", "Interest rates are an application of percentages, but the content requirement does not explicitly name them. To verify.")),
  ["pct_discount", "pct_of"], [
    ("a", "What is 3% of 200?", "Fraction(200*3,100)", "basic", "With a principal of 200 yuan and a 3% annual rate, the interest is 6 yuan."),
    ("a", "What is 2% of 500?", "Fraction(500*2,100)", "basic", "500×2%=10."),
    ("s", "A deposit of 1000 yuan is held for one year at an annual interest rate of 4%. How much interest is earned?", "1000*4/100", "1000×4÷100", "standard", "1000×4%=40."),
    ("n", "800×5/100", "800*5/100", ["4", "20", "80"], "standard", "5% of 800 is 40."),
  ])

a("pct_app", "Percentage Applications", NA, "application",
  "Solve simple problems involving how much greater one number is than another as a percentage, including growth rates.",
  ["First find the amount of increase or decrease", "Divide the increase by the original amount and express it as a percentage"],
  S(("3.NA.08", "Growth rate is a percentage application not explicitly named in the content requirement. To verify.")),
  ["pct_rate", "pct_of", "interest"], [
    ("a", "What is 20% of 50?", "Fraction(50*20,100)", "basic", "A 20% increase on 50 is an increase of 10."),
    ("c", "80+16", "80＋16", "basic", "The original value was 80; after an increase of 16, it is 96."),
    ("s", "There were 40 people last year and 50 this year. How many more are there?", "50-40", "50－40", "standard", "50−40=10, and 10÷40=25%, so the increase is 25%."),
    ("n", "200×15/100", "200*15/100", ["15", "20", "40"], "standard", "15% of 200 is 30."),
  ])

a = U(6, "Second semester", 3, "Cylinders and Cones")
a("cyl_know", "Understanding Cylinders", GG, "conceptual",
  "Identify the two bases and curved side of a cylinder, and know that its bases are identical circles.",
  ["State that a cylinder's bases are identical circles", "Identify the height of a cylinder"],
  S("3.GG.05"), ["cuboid", "circle"], [
    ("f", "What shape are the two bases of a cylinder?",
     ["Identical circles", "Two triangles", "Two circles of different sizes"],
     "Identical circles", "The two bases have equal radii.", "basic"),
    ("c", "3*2", "3×2", "basic", "A cylinder with a base radius of 3 centimeters has a diameter of 6 centimeters."),
    ("s", "A cylinder is 10 centimeters tall and has a base radius of 2 centimeters. What is its height in centimeters?", "10+0", "10＋0", "standard", "Its height is 10 centimeters."),
    ("n", "5×2", "5*2", ["7", "8", "15"], "standard", "A circle with a radius of 5 centimeters has a diameter of 10 centimeters."),
  ])

a("cylinder", "Volume of a Cylinder", GG, "procedural",
  "Calculate the volume of a cylinder by multiplying the base area by the height.",
  ["Find the area of the circular base first", "Calculate volume as base area × height"],
  S("3.GG.05"), ["cyl_know", "circ_area", "cuboid_vol"], [
    ("a", "What is the volume, in cubic centimeters, of a cylinder with a base radius of 2 centimeters and height 5 centimeters? Use pi = 314/100.", "Fraction(314*2*2*5,100)", "basic", "3.14×4×5=62.8."),
    ("a", "What is the volume, in cubic centimeters, of a cylinder with a base radius of 1 centimeter and height 10 centimeters? Use pi = 314/100.", "Fraction(314*1*1*10,100)", "basic", "3.14×1×10=31.4."),
    ("s", "A cylinder has a base area of 12 square centimeters and a height of 4 centimeters. What is its volume in cubic centimeters?", "12*4", "12×4", "standard", "12×4=48."),
    ("c", "314*3*3*2/100", "314×3×3×2÷100", "standard", "A cylinder with radius 3 and height 2 has a volume of 56.52 cubic centimeters.", True),
  ])

a("cyl_surf", "Surface Area of a Cylinder", GG, "procedural",
  "Calculate a cylinder's surface area by adding the areas of its two bases and the rectangle formed by unfolding its curved side.",
  ["Calculate the total area of the two bases", "Add the lateral area to the base area"],
  S("3.GG.05"), ["cylinder", "circ"], [
    ("c", "12.56+12.56", "12.56＋12.56", "basic", "Each base has area 12.56, for a combined area of 25.12.", True),
    ("c", "25.12+31.4", "25.12＋31.4", "basic", "The bases total 25.12 and the lateral area is 31.4, so the surface area is 56.52.", True),
    ("s", "The unfolded curved side is a rectangle 6.28 centimeters long and 5 centimeters wide. What is its area in square centimeters?", "6.28*5", "6.28×5", "standard", "6.28×5=31.4.", True),
    ("n", "3.14×4", "3.14*4", ["6.28", "9.42", "15.7"], "standard", "A base with radius 2 has area 3.14×4=12.56."),
  ])

a("cone", "Volume of a Cone", GG, "procedural",
  "Know that a cone's volume is one third the volume of a cylinder with the same base and height.",
  ["State that a cone's volume is one third the volume of a matching cylinder", "Calculate a simple cone volume"],
  S("3.GG.05"), ["cylinder"], [
    ("f", "What shape is the base of a cone?",
     ["A circle", "A square", "Two circles"],
     "A circle", "A cone has one circular base and one vertex.", "basic"),
    ("c", "18.84/3", "18.84÷3", "basic", "A cylinder with the same base and height has volume 18.84; the cone is one third of that: 18.84÷3=6.28.", True),
    ("s", "A cylinder has a volume of 30 cubic centimeters. What is the volume of a cone with the same base and height?", "30/3", "30÷3", "standard", "30÷3=10."),
    ("c", "314*3*3*6/3/100", "314×3×3×6÷3÷100", "standard", "A cone with radius 3 and height 6 has a volume of 56.52.", True),
  ])

a = U(6, "Second semester", 4, "Proportion")
a("proportion", "Meaning and Fundamental Property of Proportions", NA, "conceptual",
  "An equation stating that two ratios are equal is a proportion. In a proportion, the product of the extremes equals the product of the means.",
  ["State that the product of the extremes equals the product of the means", "Determine whether two ratios form a proportion"],
  S("3.NA.08"), ["ratio"], [
    ("f", "How does the product of the extremes in a proportion compare with the product of the means?",
     ["They are equal", "It is always greater", "There is no fixed relationship"],
     "They are equal", "This is the fundamental property of proportions.", "basic"),
    ("c", "2*6", "2×6", "basic", "In 2:3=4:6, the product of the extremes is 2×6=12."),
    ("c", "3*4", "3×4", "basic", "The product of the means is 3×4=12, equal to the product of the extremes."),
    ("n", "5×8", "5*8", ["13", "30", "45"], "standard", "In 5:4=10:8, the product of the extremes is 40."),
  ])

a("solve_prop", "Solving Proportions", NA, "procedural",
  "Use the fundamental property of proportions to find an unknown term.",
  ["Write an equation stating that the products of the extremes and means are equal", "Find the unknown term"],
  S("3.NA.08", "3.NA.05"), ["proportion", "eq_solve"], [
    ("s", "2:3=8:x. What is x?", "8*3/2", "8×3÷2", "basic", "2x=24, so x=12."),
    ("s", "4:5=x:20. What is x?", "4*20/5", "4×20÷5", "basic", "5x=80, so x=16."),
    ("s", "6:x=2:5. First calculate 6×5÷2.", "6*5/2", "6×5÷2", "standard", "2x=30, so x=15."),
    ("n", "9×4÷3", "9*4/3", ["6", "10", "18"], "standard", "For 3:4=9:x, x=12."),
  ])

a("scale", "Scale", GG, "application",
  "Know that a scale is the ratio of distance on a map to actual distance, and make simple conversions.",
  ["Explain that scale is map distance divided by actual distance", "Find actual distance from map distance"],
  S("3.GG.10", "3.NA.08"), ["proportion", "dir_dist"], [
    ("f", "What is a map scale?",
     ["The ratio of map distance to actual distance", "Map distance plus actual distance", "A direction only"],
     "The ratio of map distance to actual distance", "Map distance : actual distance = scale.", "basic"),
    ("s", "On a map, 1 centimeter represents 100 actual centimeters. What actual distance does 4 centimeters represent?", "4*100", "4×100", "basic", "4×100=400."),
    ("s", "An actual distance of 800 centimeters is shown as 4 centimeters on a map. How many actual centimeters does 1 map centimeter represent?", "800/4", "800÷4", "standard", "800÷4=200."),
    ("n", "6×50", "6*50", ["56", "200", "560"], "standard", "A map distance of 6 centimeters at 50 actual centimeters per centimeter represents 300 actual centimeters."),
  ])

a("direct_prop", "Direct Proportion", NA, "conceptual",
  "Two quantities are directly proportional when they change by the same factor and their ratio remains constant.",
  ["State that directly proportional quantities have a constant ratio", "Use the ratio to find another quantity"],
  S(("3.NA.09", "The curriculum transcription says 'quantities in direct proportion'; whether the PDF says 'directly proportional quantities' has not yet been checked.")),
  ["proportion", "qty_rel"], [
    ("f", "What property do two directly proportional quantities have?",
     ["Their ratio is constant", "Their product is constant", "Their sum is constant"],
     "Their ratio is constant", "At a constant speed, distance and time are directly proportional.", "basic"),
    ("s", "At a constant speed, a traveler covers 180 kilometers in 3 hours. How far do they travel in 1 hour?", "180/3", "180÷3", "basic", "180÷3=60."),
    ("s", "Each notebook costs 4 yuan. How much do 7 notebooks cost?", "4*7", "4×7", "standard", "With a constant unit price, total cost is directly proportional to quantity: 4×7=28."),
    ("n", "12×5", "12*5", ["17", "50", "72"], "standard", "At 12 kilometers per hour, the distance in 5 hours is 60 kilometers."),
  ])

a("inverse_prop", "Inverse Proportion", NA, "conceptual",
  "Two quantities are inversely proportional when one increases by a factor and the other decreases by the reciprocal factor, keeping their product constant.",
  ["State that inversely proportional quantities have a constant product", "Use the product to find another quantity"],
  S(("3.NA.09", "Inverse proportion appears near direct proportion in the topic, but the transcription explicitly names only direct proportion. To verify.")),
  ["direct_prop", "div_mean"], [
    ("f", "What property do two inversely proportional quantities have?",
     ["Their product is constant", "Their ratio is constant", "Their difference is constant"],
     "Their product is constant", "With a fixed total cost, unit price and quantity are inversely proportional.", "basic"),
    ("s", "The total cost is fixed. At 4 yuan each, 6 items can be bought. How many can be bought at 3 yuan each?", "4*6/3", "4×6÷3", "basic", "4×6=24, and 24÷3=8."),
    ("s", "A road takes 6 days to repair at 8 meters per day. How many days will it take at 12 meters per day?", "8*6/12", "8×6÷12", "standard", "The total work is 48 meters; 48÷12=4 days."),
    ("n", "20×3÷5", "20*3/5", ["8", "10", "15"], "standard", "20×3=60, and 60÷5=12."),
  ])

a("prop_app", "Solving Practical Problems with Proportions", NA, "application",
  "Use direct or inverse proportion to set up a proportion and solve simple real-world problems.",
  ["Determine whether two quantities are directly or inversely proportional", "Set up a proportion and solve for the unknown"],
  S("3.NA.08"), ["direct_prop", ("inverse_prop", "soft"), "solve_prop"], [
    ("s", "Three notebooks cost 12 yuan. How much do 5 of the same notebooks cost?", "12/3*5", "12÷3×5", "basic", "Each costs 4 yuan, so 5 cost 20 yuan."),
    ("s", "A traveler covers 90 kilometers in 2 hours at a constant speed. How far do they travel in 4 hours?", "90/2*4", "90÷2×4", "basic", "The speed is 45 kilometers per hour, so 4 hours covers 180 kilometers."),
    ("s", "Six machines complete a job in 4 hours. How many hours would 8 identical machines need?", "6*4/8", "6×4÷8", "standard", "The work totals 24 machine-hours; 24÷8=3."),
    ("n", "15×2÷6", "15*2/6", ["3", "4", "7"], "standard", "15×2÷6=5."),
  ])

a = U(6, "Second semester", 5, "Math Corner: Pigeonhole Principle")
a("pigeon", "Pigeonhole Principle", IP, "reasoning",
  "If there are more objects than boxes, at least one box must contain two or more objects.",
  ["State the guaranteed minimum", "Compare the number of objects with the number of boxes"],
  S(("3.NA.06", "The Pigeonhole Principle is a Math Corner topic in the current Grade 6 second-semester textbook; the content requirement has no matching title. To verify.")),
  ["div_mean", ("rem_mean", "soft")], [
    ("f", "What does the pigeonhole principle state?",
     ["If there are more objects than boxes, at least one box contains two or more", "Each box can hold only one object", "The number of objects must equal the number of boxes"],
     "If there are more objects than boxes, at least one box contains two or more", "This is the simplest case of the pigeonhole principle.", "basic"),
    ("c", "5-3", "5－3", "basic", "Putting 5 pencils into 3 holders gives 2 more pencils than holders."),
    ("a", "First write the quotient, then the remainder. Find both for 7÷3.", "(7//3, 7%3)", "standard", "7÷3=2 remainder 1. Putting 7 books into 3 bags guarantees that at least one bag has 2 books."),
    ("c", "8-3", "8－3", "standard", "Putting 8 books into 3 bags gives more books than bags, so at least one bag must have 2 books."),
  ])
