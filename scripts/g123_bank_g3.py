# -*- coding: utf-8 -*-
"""Grade 3 question bank. Each topic has 2 basic, 1 standard, and 1 challenge question."""

BANK = {}

# ---------- Grade 3, first semester ----------
BANK["cnm_p221"] = [
    ("c", "basic", "Arrange 4 identical unit cubes in a row from left to right. What does the row look like from the front?",
     ["A circle", "A triangle", "4 squares in a row"], "C",
     "From the front, a row of unit cubes appears as the same number of squares in a row."),
    ("n", "basic", "Unit cubes are arranged in a row from left to right. From the front, you see 5 squares. How many unit cubes are in the row?", "5",
     "When cubes are arranged in a single layer and row, the number of squares seen from the front is the number of cubes.", "5"),
    ("n", "standard", "Place 3 unit cubes on the bottom, then place 1 on top of one of them. How many cubes are there in all?", "4",
     "There are 3 cubes on the bottom and 1 more on top, for a total of 4.", "3+1"),
    ("n", "challenge", "From the front, the left column is 2 cubes high and the right column is 1 cube high. The columns are side by side. What is the minimum number of unit cubes used?", "3",
     "The left column needs at least 2 cubes and the right at least 1, for a minimum of 3.", "2+1"),
]

BANK["cnm_p222"] = [
    ("n", "basic", "Cut a rectangular prism along its edges and unfold it. How many faces are in the net?", "6",
     "A rectangular prism has 6 faces, so its net also has 6 faces.", "6"),
    ("c", "basic", "What shape is each face of an unfolded cube?", ["A triangle", "A square", "A circle"], "B",
     "Every face of a cube is a square."),
    ("n", "standard", "Opposite faces of a rectangular prism are identical. How many pairs of opposite faces are there among its 6 faces?", "3",
     "There is one top-bottom pair, one front-back pair, and one left-right pair: 3 pairs in all.", "6//2"),
    ("n", "challenge", "The top of a rectangular-prism box is a rectangle 5 centimeters long and 3 centimeters wide. How long is the opposite bottom face?", "5",
     "Opposite faces are identical, so the bottom is also 5 centimeters long.", "5"),
]

BANK["cnm_p223"] = [
    ("n", "basic", "Evaluate 36−8+12 from left to right, since it uses only addition and subtraction. What is the result?", "40",
     "36−8=28, and 28+12=40.", "36-8+12"),
    ("n", "basic", "Evaluate 48÷6×3 from left to right, since it uses only multiplication and division. What is the result?", "24",
     "48÷6=8, and 8×3=24.", "48//6*3"),
    ("n", "standard", "In 25+5×4, multiply first. What is the result?", "45",
     "First, 5×4=20; then 25+20=45.", "25+5*4"),
    ("n", "challenge", "Evaluate 60−36÷4. If you mistakenly subtract first, you get 6. What is the result when you use the correct order?", "51",
     "First, 36÷4=9; then 60−9=51.", "60-36//4"),
]

BANK["cnm_p058"] = [
    ("c", "basic", "What should you do with parentheses?",
     ["Evaluate the expression inside first", "Evaluate the parentheses last", "You can skip the parentheses"], "A", "Evaluate the expression inside parentheses first."),
    ("n", "basic", "Evaluate the parentheses first: what is (8−3)×2?", "10", "First, 8−3=5; then 5×2=10.", "(8-3)*2"),
    ("n", "standard", "Evaluate the parentheses first: what is (2+5)×4?", "28", "First, 2+5=7; then 7×4=28.", "(2+5)*4"),
    ("n", "challenge", "Eight students are divided equally into 2 groups, then 3 more students join each group. How many students are in each group now?", "7",
     "First divide: 8÷2=4 students per group. Then add 3: 4+3=7.", "8//2+3"),
]

BANK["cnm_p059"] = [
    ("n", "basic", "A bookstore received 25 books, then 17 more, and sold 13. How many books are left?", "29",
     "Add, then subtract: 25+17=42, and 42−13=29.", "25+17-13"),
    ("n", "basic", "A shelf has 40 books. Twelve are borrowed in the morning and 10 more in the afternoon. How many books are left?", "18",
     "40−12=28, and 28−10=18.", "40-12-10"),
    ("n", "standard", "A shelf has 40 books. Twelve are borrowed in the morning, then 8 are returned in the afternoon. How many books are on the shelf now?", "36",
     "40−12=28, and 28+8=36.", "40-12+8"),
    ("n", "challenge", "A shelf has 40 books. Twelve are borrowed in the morning, 8 are returned in the afternoon, and 6 more are borrowed in the evening. How many books are on the shelf now?", "30",
     "40−12=28, 28+8=36, and 36−6=30.", "40-12+8-6"),
]

BANK["cnm_p067"] = [
    ("n", "basic", "How many millimeters are in 3 centimeters?", "30", "1 centimeter=10 millimeters, so 3 centimeters=30 millimeters.", "3*10"),
    ("n", "basic", "How many millimeters are in 8 centimeters?", "80", "8×10=80 millimeters.", "8*10"),
    ("n", "standard", "One nail is 2 centimeters long and another is 15 millimeters long. How many millimeters longer is the 2-centimeter nail?", "5",
     "2 centimeters=20 millimeters, and 20−15=5 millimeters.", "2*10-15"),
    ("n", "challenge", "One stick is 25 millimeters long and another is 3 centimeters long. How many millimeters longer is the longer stick?", "5",
     "3 centimeters=30 millimeters, which is 30−25=5 millimeters longer than 25 millimeters.", "3*10-25"),
]

BANK["cnm_p068"] = [
    ("n", "basic", "How many centimeters are in 5 decimeters?", "50", "1 decimeter=10 centimeters, so 5 decimeters=50 centimeters.", "5*10"),
    ("n", "basic", "How many centimeters are in 12 decimeters?", "120", "12×10=120 centimeters.", "12*10"),
    ("n", "standard", "A desk is about 7 decimeters tall. How many centimeters is that?", "70", "7×10=70 centimeters.", "7*10"),
    ("n", "challenge", "A rope is 2 decimeters long. If 5 centimeters are cut off, how many centimeters remain?", "15",
     "2 decimeters=20 centimeters, and 20−5=15 centimeters.", "2*10-5"),
]

BANK["cnm_p069"] = [
    ("c", "basic", "How many meters are in 1 kilometer?", ["1000 meters", "100 meters", "10 meters"], "A", "1 kilometer=1000 meters."),
    ("n", "basic", "How many meters are in 3 kilometers?", "3000", "3×1000=3000 meters.", "3*1000"),
    ("n", "standard", "How many meters are in 6 kilometers?", "6000", "6×1000=6000 meters.", "6*1000"),
    ("n", "challenge", "The school is 2 kilometers from the park, and the library is another 500 meters away. How many meters is the school from the library?", "2500",
     "2 kilometers=2000 meters; adding 500 meters gives 2500 meters.", "2*1000+500"),
]

BANK["cnm_p056"] = [
    ("c", "basic", "How many grams are in 1 kilogram?", ["1000 grams", "100 grams", "10 grams"], "A", "1 kilogram=1000 grams."),
    ("n", "basic", "How many grams are in 2 kilograms?", "2000", "2×1000=2000 grams.", "2*1000"),
    ("n", "standard", "How many grams are in 4 kilograms?", "4000", "4×1000=4000 grams.", "4*1000"),
    ("n", "challenge", "One bag of salt weighs 500 grams. How many grams do two bags weigh?", "1000",
     "500+500=1000 grams, exactly 1 kilogram.", "500+500"),
]

BANK["cnm_p070"] = [
    ("c", "basic", "How many kilograms are in 1 metric ton?", ["1000 kilograms", "100 kilograms", "1000 grams"], "A", "1 metric ton=1000 kilograms."),
    ("n", "basic", "How many kilograms are in 2 metric tons?", "2000", "2×1000=2000 kilograms.", "2*1000"),
    ("n", "standard", "How many kilograms are in 5 metric tons?", "5000", "5×1000=5000 kilograms.", "5*1000"),
    ("n", "challenge", "A truck can carry 4 metric tons and is already carrying 1500 kilograms. How many more kilograms can it carry?", "2500",
     "4 metric tons=4000 kilograms, and 4000−1500=2500 kilograms.", "4*1000-1500"),
]

BANK["cnm_p224"] = [
    ("c", "basic", "Cao Chong put an elephant on a boat and marked the waterline, then loaded stones until the boat reached the same waterline. Why could weighing the stones reveal the elephant's weight?",
     ["The stones weighed more than the elephant", "The boat became lighter", "The stones weighed the same as the elephant"], "C",
     "When the boat reaches the same waterline, the stones weigh the same as the elephant."),
    ("n", "basic", "One apple weighs the same as 2 pears. One pear weighs 150 grams. How many grams does the apple weigh?", "300",
     "The apple weighs as much as 2 pears, so 150×2=300 grams.", "150*2"),
    ("n", "standard", "One duck weighs the same as 3 chickens, and one goose weighs the same as 2 ducks. How many chickens weigh as much as one goose?", "6",
     "One goose=2 ducks=2×3 chickens, or 6 chickens.", "3*2"),
    ("n", "challenge", "One watermelon weighs the same as 4 identical Hami melons, and one Hami melon weighs the same as 2 muskmelons. How many muskmelons weigh as much as one watermelon?", "8",
     "One watermelon=4 Hami melons=4×2 muskmelons, or 8 muskmelons.", "4*2"),
]

BANK["cnm_p074"] = [
    ("n", "basic", "Each box of colored pencils costs 24 yuan. How much do 2 boxes cost?", "48", "24×2=48 yuan.", "24*2"),
    ("n", "basic", "There are 13 seats in each row and 3 rows. How many seats are there in all?", "39", "13×3=39 seats.", "13*3"),
    ("n", "standard", "Each box of colored pencils costs 36 yuan. How much do 4 boxes cost?", "144", "36×4=144 yuan.", "36*4"),
    ("n", "challenge", "Each box costs 36 yuan. If you buy 4 boxes and pay with 200 yuan, how much change should you receive?", "56",
     "The total is 36×4=144 yuan, so the change is 200−144=56 yuan.", "200-36*4"),
]

BANK["cnm_p075"] = [
    ("n", "basic", "Each box contains 30 pens. How many pens are in 4 boxes?", "120", "30×4=120. Keep the trailing zero.", "30*4"),
    ("n", "basic", "Each carton contains 50 items. How many items are in 6 cartons?", "300", "50×6=300.", "50*6"),
    ("n", "standard", "Each carton contains 105 items. How many items are in 4 cartons?", "420",
     "Multiplying the zero in the tens place still gives zero: 105×4=420.", "105*4"),
    ("n", "challenge", "Each carton contains 102 apples. How many apples are in 6 cartons?", "612",
     "The tens digit of 102 is 0, and 102×6=612.", "102*6"),
]

BANK["cnm_p076"] = [
    ("c", "basic", "What is the purpose of number codes?",
     ["To represent things with numbers so they are easy to distinguish", "To turn every number into 0", "To use only for addition"], "A",
     "Each digit in a code can represent a different piece of information."),
    ("n", "basic", "In student ID 25, the tens digit represents the grade and the ones digit represents the group. Which grade is it?", "2",
     "The tens digit of 25 is 2, so the student is in grade 2.", "2"),
    ("n", "standard", "In code 3205, the hundreds digit represents the seating section. Which section is it?", "2",
     "The hundreds digit of 3205 is 2.", "2"),
    ("n", "challenge", "The grade is coded as 3, and the two-digit seat number is 15. Put the grade first and the seat number after it. What is the resulting three-digit number?", "315",
     "Write 3 followed by 15 to get 315.", "300+15"),
]

BANK["cnm_p099"] = [
    ("c", "basic", "Which statement describes a line segment, not a line?",
     ["It has two endpoints and a measurable length", "It has no endpoints and extends infinitely in both directions", "It has one endpoint and extends infinitely in one direction"], "A",
     "A line segment has two endpoints. A line has no endpoints, while a ray has one."),
    ("n", "basic", "The segment from A to B is 6 centimeters long, and another curved path is 9 centimeters long. What is the shortest distance between the two points, in centimeters?", "6",
     "The segment between two points is the shortest path, so the distance is 6 centimeters.", "6"),
    ("n", "standard", "The route from home to school along the street is 400 meters, while a shortcut is 250 meters. How much shorter is the shortcut?", "150",
     "The shortcut is shorter by 400−250=150 meters.", "400-250"),
    ("c", "challenge", "A line segment keeps one endpoint and extends infinitely in the other direction. What is it called?",
     ["A ray", "Still a line segment", "A circle"], "A", "A ray has one endpoint and extends infinitely in one direction."),
]

BANK["cnm_p225"] = [
    ("n", "basic", "How many sides does an angle have?", "2", "An angle has one vertex and two sides.", "2"),
    ("c", "basic", "What determines the size of an angle?",
     ["The size of the paper", "How far apart its sides spread", "The length of the sides"], "B", "An angle's size depends on how far apart its sides spread, not on how long they are drawn."),
    ("n", "standard", "How many angles does a triangle have?", "3", "A triangle has 3 angles and therefore 3 vertices.", "3"),
    ("c", "challenge", "Both sides of an angle are drawn longer. What happens to the size of the angle?",
     ["It stays the same", "It gets larger", "It gets smaller"], "A", "The sides are longer, but their spread is unchanged, so the angle stays the same size."),
]

BANK["cnm_p101"] = [
    ("c", "basic", "How does a right angle compare with an acute angle?",
     ["A right angle is larger", "A right angle is smaller", "They are the same size"], "A", "An acute angle is smaller than a right angle.", None, "cnm_p101_q1"),
    ("c", "basic", "How does an obtuse angle compare with a right angle?",
     ["An obtuse angle is larger", "An obtuse angle is smaller", "An obtuse angle equals a right angle"], "A", "An obtuse angle is larger than a right angle and smaller than a straight angle.", None, "cnm_p101_q2"),
    ("n", "standard", "How many degrees are in a straight angle?", "180", "The sides of a straight angle form a straight line, so it measures 180 degrees.", "180"),
    ("n", "challenge", "One angle measures 30 degrees and another measures 100 degrees. Which one is obtuse, and what is its measure?", "100",
     "100 degrees is greater than a right angle (90 degrees) and less than a straight angle (180 degrees), so it is obtuse. The 30-degree angle is acute.", "100"),
]

BANK["cnm_p079"] = [
    ("c", "basic", "What does the denominator of a fraction tell you?",
     ["How many equal parts the whole is divided into", "How many parts are taken away", "How many wholes there are"], "A",
     "In a unit fraction, the denominator is the number of equal parts, and the numerator 1 represents one part."),
    ("n", "basic", "A sheet of paper is divided into 4 equal parts, and 1 part is taken. What fraction of the sheet is that?", "1/4",
     "Dividing it into 4 equal parts makes each part 1/4.", "Fraction(1,4)"),
    ("n", "standard", "A sheet of paper is divided into 8 equal parts, and 1 part is shaded. What fraction of the sheet is shaded?", "1/8",
     "One of 8 equal parts is 1/8.", "Fraction(1,8)"),
    ("n", "challenge", "A cake is shared equally between 2 children. What fraction of the cake does each child get?", "1/2",
     "The cake is divided into 2 equal parts, so each child gets 1/2.", "Fraction(1,2)"),
]

BANK["cnm_p226"] = [
    ("n", "basic", "A circle is divided into 4 equal parts, and 3 are shaded. What fraction of the circle is shaded?", "3/4",
     "Three of the 4 equal parts are shaded, so the fraction is 3/4.", "Fraction(3,4)"),
    ("c", "basic", "What is the denominator of 5/8?", ["3", "5", "8"], "C", "The denominator is the number below the fraction bar, so the denominator of 5/8 is 8."),
    ("n", "standard", "A rope is divided into 10 equal pieces, and 7 pieces are used. What fraction of the rope is used?", "7/10",
     "Seven of the 10 pieces are used, so the fraction is 7/10.", "Fraction(7,10)"),
    ("n", "challenge", "A cake is cut into 6 equal pieces and 1 is eaten. What fraction of the cake remains?", "5/6",
     "Five pieces remain, so the fraction is 5/6.", "Fraction(5,6)"),
]

BANK["cnm_p227"] = [
    ("c", "basic", "Which is greater, 3/7 or 2/7?", ["2/7", "They are equal", "3/7"], "C",
     "With the same denominator, the fraction with the larger numerator is greater, so 3/7 is greater."),
    ("c", "basic", "Which is greater, 1/3 or 1/5?", ["They are equal", "1/3", "1/5"], "B",
     "When the numerators are both 1, the fraction with the smaller denominator is greater, so 1/3 is greater."),
    ("c", "standard", "Which is greatest: 4/9, 1/9, or 5/9?", ["4/9", "1/9", "5/9"], "C",
     "The denominators are the same, and 5 is the largest numerator, so 5/9 is greatest."),
    ("n", "challenge", "Two pies are the same size. One is divided into 4 equal pieces and the other into 8. If you take 1 piece from each, how much larger is 1/4 than 1/8?", "1/8",
     "1/4=2/8, and 2/8−1/8=1/8.", "Fraction(1,4)-Fraction(1,8)"),
]

BANK["cnm_p080"] = [
    ("n", "basic", "What is 1/5 plus 2/5?", "3/5", "Keep the denominator and add the numerators: 1+2=3, so the result is 3/5.", "Fraction(1,5)+Fraction(2,5)"),
    ("n", "basic", "What is 3/4 minus 1/4?", "1/2", "Subtract the numerators: 3−1=2, giving 2/4, which simplifies to 1/2.", "Fraction(3,4)-Fraction(1,4)"),
    ("n", "standard", "A rope has 2/8 used, then another 3/8 used. What fraction of the rope is used in all?", "5/8",
     "Keep the denominator: 2/8+3/8=5/8.", "Fraction(2,8)+Fraction(3,8)"),
    ("n", "challenge", "A pie is divided into 8 equal pieces. Xiaoming eats 3 pieces and Xiaohong eats 2. What fraction of the pie remains?", "3/8",
     "They eat 3/8+2/8=5/8, leaving 8/8−5/8=3/8.", "Fraction(8-3-2,8)"),
]

BANK["cnm_p073"] = [
    ("n", "basic", "What is 3 times 6?", "18", "Three times 6 means 3 groups of 6: 6×3=18.", "6*3"),
    ("n", "basic", "What is 4 times 8?", "32", "8×4=32.", "8*4"),
    ("n", "standard", "There are 7 red flowers. The number of yellow flowers is 5 times the number of red flowers. How many yellow flowers are there?", "35", "7×5=35 flowers.", "7*5"),
    ("n", "challenge", "There are 6 red flowers and 3 times as many yellow flowers. How many more yellow flowers are there than red flowers?", "12",
     "There are 6×3=18 yellow flowers, which is 18−6=12 more than the red flowers.", "6*3-6"),
]

BANK["cnm_p081"] = [
    ("c", "basic", "In a set diagram, where do you put people or objects that belong to both groups?",
     ["In the overlap of the two circles", "Outside both circles", "Only in the left circle"], "A", "Put members of both groups in the overlapping part of the circles."),
    ("n", "basic", "The Chinese club has 10 members, and 4 also belong to another club. How many belong only to the Chinese club?", "6",
     "The 4 shared members are already included in the 10, so 10−4=6 belong only to the Chinese club.", "10-4"),
    ("n", "standard", "The Chinese club has 10 members and the math club has 9. Four students belong to both. How many students are there if each person is counted only once?", "15",
     "10+9−4=15. Do not count the overlap twice.", "10+9-4"),
    ("n", "challenge", "The Chinese club has 10 members and the math club has 9. Four students belong to both. How many belong to exactly one club?", "11",
     "Six belong only to the Chinese club (10−4), and 5 only to the math club (9−4), for a total of 11.", "(10-4)+(9-4)"),
]

BANK["cnm_p095"] = [
    ("c", "basic", "When counting pairings of two types of items, how can you avoid both repeats and omissions?",
     ["Pair them one by one in order", "Pair only the first item, then stop", "Add the numbers of the two types of items"], "A",
     "Pair them systematically, making every possible pairing exactly once."),
    ("n", "basic", "There are 2 shirts and 3 pairs of pants. Each shirt can be paired with each pair of pants. How many outfits are possible?", "6",
     "2×3=6 outfits.", "2*3"),
    ("n", "standard", "There are 3 kinds of bread and 2 kinds of drinks. Each kind of bread can be paired with each drink. How many combinations are possible?", "6",
     "3×2=6 combinations.", "3*2"),
    ("n", "challenge", "There are 2 shirts and 3 pairs of pants. One more shirt is added, and each shirt can still be paired with every pair of pants. How many outfits are possible now?", "9",
     "There are now 3 shirts, so 3×3=9 outfits.", "3*3"),
]

# ---------- Grade 3, second semester ----------
BANK["cnm_p228"] = [
    ("c", "basic", "An elevator moves up and down. Which type of motion is this?", ["Rotation", "Reflection symmetry", "Translation"], "C",
     "An elevator moves in a straight line, so this is a translation."),
    ("c", "basic", "A windmill turns. Which type of motion is this?", ["Reflection symmetry", "Rotation", "Translation"], "B",
     "A windmill turns around its center, so this is a rotation."),
    ("c", "standard", "A pattern is cut from a folded sheet of paper. When the paper is unfolded, how do the two sides of the crease compare?",
     ["They are identical", "The left side is larger", "The right side is larger"], "A", "When the paper is cut while folded and then unfolded, the two sides match; this is reflection symmetry."),
    ("n", "challenge", "A small square moves 5 spaces to the right, then 2 spaces to the left. How many spaces to the right is it from its starting point?", "3",
     "It moves 5 spaces right and 2 left, for a net movement of 5−2=3 spaces to the right.", "5-2"),
]

BANK["cnm_p083"] = [
    ("n", "basic", "Forty-eight pencils are shared equally among 2 groups. How many pencils does each group get?", "24", "Divide starting with the highest place value: 48÷2=24.", "48//2"),
    ("n", "basic", "Sixty-nine notebooks are divided equally into 3 groups. How many notebooks are in each group?", "23", "69÷3=23.", "69//3"),
    ("n", "standard", "Eighty-four pencils are shared equally among 4 groups. How many pencils does each group get?", "21", "84÷4=21.", "84//4"),
    ("n", "challenge", "Two hundred fifty-six books are shared equally among 4 classes. How many books does each class get?", "64",
     "2 hundreds cannot be divided by 4, so use the first two digits, 25. Then 256÷4=64.", "256//4"),
]

BANK["cnm_p084"] = [
    ("n", "basic", "Ninety-six people are divided equally into 3 groups. How many people are in each group?", "32", "Equal sharing uses division: 96÷3=32.", "96//3"),
    ("n", "basic", "There are 75 apples, packed 5 per bag. How many bags can be filled?", "15", "75÷5=15 bags.", "75//5"),
    ("n", "standard", "One hundred twenty-eight people ride equally in 4 buses. How many people are on each bus?", "32", "128÷4=32 people.", "128//4"),
    ("n", "challenge", "There are 200 pens, packed 8 per box. Ten boxes are already packed. How many more boxes are needed?", "15",
     "There are 200÷8=25 boxes in all, so 25−10=15 more boxes are needed.", "200//8-10"),
]

BANK["cnm_p229"] = [
    ("n", "basic", "How many sides does a pentagon have?", "5", "A polygon's name tells how many sides it has; a pentagon has 5 sides.", "5"),
    ("n", "basic", "How many angles does a hexagon have?", "6", "A polygon has the same number of angles as sides, so a hexagon has 6 angles.", "6"),
    ("c", "standard", "What is a closed shape made of 4 line segments called?", ["A quadrilateral", "A triangle", "A pentagon"], "A",
     "A shape with 4 sides is a quadrilateral."),
    ("n", "challenge", "A polygon has 6 sides. How many angles does it have?", "6",
     "A polygon has the same number of sides and angles, so 6 sides make 6 angles.", "6"),
]

BANK["cnm_p077"] = [
    ("c", "basic", "What is true about the opposite sides of a rectangle?",
     ["Opposite sides are equal", "All four sides are different", "It has no right angles"], "A",
     "The two pairs of opposite sides of a rectangle are equal.", None, "cnm_p077_q1"),
    ("c", "basic", "What is true about the four angles of a rectangle?",
     ["They are all acute", "They are all right angles", "Only two are right angles"], "B", "All four angles of a rectangle are right angles."),
    ("n", "standard", "One side of a square is 6 centimeters long. How long is the opposite side?", "6",
     "All four sides of a square are equal, so the opposite side is also 6 centimeters.", "6"),
    ("n", "challenge", "A rectangle is 8 centimeters long and 5 centimeters wide. What is the combined length of its two longer sides?", "16",
     "Opposite sides of a rectangle are equal, so both longer sides are 8 centimeters; 8+8=16 centimeters.", "8+8"),
]

BANK["cnm_p078"] = [
    ("c", "basic", "What is perimeter?",
     ["The total length around a shape", "The area inside a shape", "The length of one side"], "A", "Perimeter is the length around a shape."),
    ("n", "basic", "What is the perimeter, in centimeters, of a rectangle 6 centimeters long and 4 centimeters wide?", "20",
     "(6+4)×2=20 centimeters.", "(6+4)*2"),
    ("n", "standard", "What is the perimeter, in centimeters, of a square with 5-centimeter sides?", "20", "5×4=20 centimeters.", "5*4"),
    ("n", "challenge", "A rectangle has a perimeter of 20 centimeters and a length of 6 centimeters. What is its width?", "4",
     "Length plus width is 20÷2=10 centimeters, so the width is 10−6=4 centimeters.", "20//2-6"),
]

BANK["cnm_p088"] = [
    ("c", "basic", "What unit should be used to measure area?",
     ["Square units", "Only the length of one side", "Kilograms"], "A", "Area should be compared using the same area unit."),
    ("c", "basic", "What is perimeter, and how is it different from area?",
     ["The total length around a shape", "The amount of space covered inside a shape", "The weight of a shape"], "A",
     "Perimeter is the distance around a shape; area is the space inside it."),
    ("n", "standard", "Identical small squares are used to measure a rectangle. Two fit across and 3 rows fill it exactly. What is the area in small squares?", "6",
     "2×3=6 squares.", "2*3"),
    ("n", "challenge", "Identical small squares are used to cover a shape. Four fit across and there are 3 rows, but 1 square is missing from the bottom right corner. How many squares are already in place?", "11",
     "A full rectangle would have 4×3=12 squares. With 1 missing, 11 are in place.", "4*3-1"),
]

BANK["cnm_p089"] = [
    ("n", "basic", "What is the area, in square centimeters, of a rectangle 8 centimeters long and 5 centimeters wide?", "40", "8×5=40.", "8*5"),
    ("n", "basic", "What is the area, in square centimeters, of a square with 6-centimeter sides?", "36", "6×6=36.", "6*6"),
    ("n", "standard", "A blackboard is 4 meters long and 1 meter wide. What is its area in square meters?", "4", "4×1=4.", "4*1"),
    ("n", "challenge", "A rectangle has an area of 36 square centimeters and a length of 9 centimeters. What is its width?", "4",
     "Width=area÷length: 36÷9=4.", "36//9"),
]

BANK["cnm_p090"] = [
    ("n", "basic", "How many square decimeters are in 2 square meters?", "200", "1 square meter=100 square decimeters, so 2 square meters=200 square decimeters.", "2*100"),
    ("n", "basic", "How many square centimeters are in 4 square decimeters?", "400", "1 square decimeter=100 square centimeters, so 4 square decimeters=400 square centimeters.", "4*100"),
    ("n", "standard", "A plot of land is 3 square meters. What is its area in square decimeters?", "300", "3×100=300.", "3*100"),
    ("n", "challenge", "A 1-square-meter carpet has 40 square decimeters cut off. How many square decimeters remain?", "60",
     "1 square meter=100 square decimeters, and 100−40=60.", "100-40"),
]

BANK["cnm_p085"] = [
    ("n", "basic", "A two-way table shows Class 1 has 14 boys and 12 girls, and Class 2 has 13 boys and 15 girls. How many girls are in Class 1?", "12",
     "Read the Class 1 girls entry directly from the table: 12.", "12"),
    ("n", "basic", "A two-way table shows Class 1 has 14 boys and 12 girls, and Class 2 has 13 boys and 15 girls. How many boys are in Class 2?", "13",
     "The Class 2 boys entry is 13.", "13"),
    ("n", "standard", "A two-way table shows Class 1 has 14 boys and 12 girls, and Class 2 has 13 boys and 15 girls. How many boys are in both classes altogether?", "27",
     "Total boys: 14+13=27.", "14+13"),
    ("n", "challenge", "A two-way table shows Class 1 has 14 boys and 12 girls, and Class 2 has 13 boys and 15 girls. How many more students are in Class 2 than in Class 1?", "2",
     "Class 1 has 14+12=26 students; Class 2 has 13+15=28. The difference is 28−26=2.", "(13+15)-(14+12)"),
]

BANK["cnm_p091"] = [
    ("c", "basic", "How many months are in a year?", ["12 months", "10 months", "365 months"], "A", "A year has 12 months."),
    ("c", "basic", "How many days are in February in a common year?", ["28 days", "29 days", "30 days"], "A", "February has 28 days in a common year."),
    ("c", "standard", "How many days are in February in a leap year?", ["29 days", "28 days", "31 days"], "A", "February has 29 days in a leap year."),
    ("n", "challenge", "January has 31 days, and February has 28 days in a common year. How many more days does January have?", "3",
     "31−28=3 days.", "31-28"),
]

BANK["cnm_p092"] = [
    ("n", "basic", "What time is 1 p.m. in 24-hour time?", "13", "Add 12 to the afternoon hour: 1+12=13.", "12+1"),
    ("n", "basic", "What time is 3 p.m. in 24-hour time?", "15", "3+12=15.", "12+3"),
    ("n", "standard", "A train leaves at 16:00. What time is that in the afternoon?", "4", "16−12=4, so it is 4 p.m.", "16-12"),
    ("n", "challenge", "How many hours pass from 10 p.m. today to 1 a.m. tomorrow?", "3",
     "From 22:00 to 24:00 is 2 hours, then 1 more hour to 1:00, for a total of 3 hours.", "24-22+1"),
]

BANK["cnm_p093"] = [
    ("n", "basic", "How many jiao is 0.1 yuan?", "1", "1 jiao is 0.1 yuan, so 0.1 yuan is 1 jiao.", "1"),
    ("n", "basic", "How many yuan is 3 jiao? Give your answer as a decimal.", "0.3", "1 jiao=0.1 yuan, so 3 jiao=0.3 yuan.", "Fraction(3,10)"),
    ("n", "standard", "1 decimeter is 1/10 of a meter. Write this as a decimal to one place. How many meters is it?", "0.1", "1/10 meter=0.1 meter.", "Fraction(1,10)"),
    ("n", "challenge", "How many decimeters are in 0.6 meters?", "6", "0.1 meter=1 decimeter, so 0.6 meter=6 decimeters.", "6"),
]

BANK["cnm_p094"] = [
    ("n", "basic", "A pen costs 0.6 yuan and an eraser costs 0.2 yuan. What is the total cost?", "0.8",
     "Align the decimal points: 0.6+0.2=0.8.", "Fraction('0.6')+Fraction('0.2')"),
    ("n", "basic", "A rope is 0.6 meters long. If 0.1 meter is cut off, how many meters remain?", "0.5", "0.6−0.1=0.5.", "Fraction('0.6')-Fraction('0.1')"),
    ("n", "standard", "A rope is 1.2 meters long, and another 0.4 meters is added. How long is it now?", "1.6", "1.2+0.4=1.6.", "Fraction('1.2')+Fraction('0.4')"),
    ("n", "challenge", "A ribbon is 1.2 meters long. After 0.8 meter is used, another 0.3 meter is added. How long is it now?", "0.7",
     "1.2−0.8=0.4, and 0.4+0.3=0.7.", "Fraction('1.2')-Fraction('0.8')+Fraction('0.3')"),
]

BANK["cnm_p082"] = [
    ("c", "basic", "Which direction is opposite northeast?", ["Southeast", "Northwest", "Southwest", "Due north"], "C",
     "Southwest is opposite northeast."),
    ("c", "basic", "Starting at the square, walk east and then north. In which direction are you from the square?",
     ["Northeast", "Southeast", "Northwest"], "A", "Northeast is between east and north."),
    ("c", "standard", "Xiaoming is facing northeast. Which direction is behind him?",
     ["Southwest", "Southeast", "Due west"], "A", "Southwest is opposite northeast, so it is behind him."),
    ("c", "challenge", "Xiaoming walks southeast to a store, then returns to the square along the same route. Which direction is he facing on the way back?",
     ["Northwest", "Southeast", "Northeast"], "A", "On the way back, he faces the opposite direction from the way he came; northwest is opposite southeast."),
]
