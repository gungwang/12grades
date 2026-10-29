# -*- coding: utf-8 -*-
"""Grade 3 and 4 topics. Grades 3–6 follow current PEP units; the contents are unofficial, and items needing verification are noted in README."""
from primary_qgen import add4, sub4, mul4, div4, calc, story, fact, ask, expr4, choice_num

NA, GG, SP, IP = "Number and Algebra", "Geometry and Measurement", "Statistics and Probability", "Integrated Practice"
TOPICS = []


def U(grade, sem, n, uname, ip=False):
    def add(slug, name, dom, typ, desc, mc, std, pre, qs, root=None):
        TOPICS.append({
            "slug": slug, "name": name, "domain": dom, "grade": grade, "semester": sem,
            "unit": n, "uname": uname, "ip": ip, "type": typ, "description": desc,
            "mastery_criteria": mc, "standards": std, "pre": pre, "qs": qs, "root_reason": root,
        })
    return add


def S(*codes):
    return list(codes)


# "上" and "下" are parser-required semester tokens; keep them unchanged.
# ---------- Grade 3, Term 1 (current) ----------
a = U(3, "上", 1, "Hours, Minutes, and Seconds")
a("sec", "Understanding Seconds", NA, "conceptual",
  "Understand the second as a unit of time and know that the second hand makes one full turn in 1 minute.",
  ["Can state that 1 minute equals 60 seconds", "Can convert several minutes to seconds"],
  S(("1.IP.03", "The curriculum places hours, minutes, and seconds in the first-stage theme activity “Where Is Time?” The verified 2024 Grade 1–2 catalogs have no separate clock unit; these are taught systematically in Unit 1 of the current Grade 3 PEP Book 1. This follows the current book placement; verification pending.")),
  ["know100"], [
    fact("How long does the minute hand take to make one full turn?", ["60 min", "60 sec", "12 min"], "60 min", "The minute hand takes 60 minutes, or 1 hour, to make one full turn. The second hand takes 60 seconds.", "basic"),
    ask("How many seconds are in 2 minutes?", "2*60", "basic", "1 minute = 60 seconds, so 2 minutes = 120 seconds."),
    ask("How many seconds are in 3 minutes?", "3*60", "standard", "3×60=180."),
    calc("60-15", "60－15", "standard", "1 minute is 60 seconds; after 15 seconds, 45 seconds remain."),
  ])

a("time_hms", "Hour-Minute-Second Conversions", NA, "procedural",
  "Know that 1 hour = 60 minutes and 1 minute = 60 seconds, and make simple conversions.",
  ["Can state that adjacent time units differ by a factor of 60", "Can convert several hours to minutes"],
  S(("1.IP.03", "As with “Understanding Seconds,” the curriculum places this in the first stage, while the current textbook covers it in Grade 3 Book 1. Verification pending.")),
  ["sec"], [
    fact("How many minutes are in 1 hour?", ["60 min", "100 min", "24 min"], "60 min", "1 hour = 60 minutes.", "basic"),
    ask("How many minutes are in 2 hours?", "2*60", "basic", "2×60=120."),
    ask("How many seconds are in 4 minutes?", "4*60", "standard", "4×60=240."),
    story("A class lasts 40 minutes, followed by a 10-minute break. How many minutes pass from the start of class until the break ends?", "40+10", "40＋10", "standard", "40＋10=50."),
  ])

a("elapsed", "Elapsed Time", NA, "application",
  "Calculate the number of minutes elapsed between two times.",
  ["Can subtract the start time from the end time to find elapsed time", "Can calculate elapsed time within the same hour"],
  S(("1.IP.03", "Elapsed time applies hours, minutes, and seconds; textbook placement needs verification.")),
  ["time_hms", "sub_oral"], [
    calc("35-20", "35－20", "basic", "From 2:20 to 2:35, 15 minutes elapse."),
    calc("60-45", "60－45", "basic", "From minute 45 to the next hour, 15 minutes elapse."),
    story("A movie starts at 7:15 and ends at 7:50. How many minutes does it last?", "50-15", "50－15", "standard", "Both times are within the 7 o'clock hour, so 50−15=35."),
    story("A run starts at 3:40 and ends at 4:00. How many minutes does it last?", "60-40", "60－40", "standard", "From minute 40 to the hour is 20 minutes."),
  ])

a = U(3, "上", 2, "Addition and Subtraction Within 10,000 (I)")
a("add_oral_wan", "Mental Addition with Hundreds and Tens", NA, "procedural",
  "Mentally add numbers in the hundreds and tens, as well as two-digit numbers.",
  ["Can mentally add multiples of ten and one hundred", "Can estimate the approximate sum of two two-digit numbers"],
  S("2.NA.01", "1.NA.04"), ["add_col", "know_wan"], expr4([
    ("300+400", "300＋400", "basic", "3 hundreds plus 4 hundreds equals 700."),
    ("250+30", "250＋30", "basic", "250＋30=280."),
    ("180+140", "180＋140", "standard", "180＋140=320.", "One box contains 180 books and another contains 140. How many books are there altogether?"),
    ("470+250", "470＋250", "standard", "470＋250=720."),
  ]))

a("sub_oral_wan", "Mental Subtraction with Hundreds and Tens", NA, "procedural",
  "Mentally subtract numbers in the hundreds and tens.",
  ["Can mentally subtract multiples of one hundred and ten", "Can compare larger numbers using subtraction"],
  S("1.NA.04"), ["add_oral_wan", "sub_col"], expr4([
    ("800-300", "800－300", "basic", "800−300=500."),
    ("560-40", "560－40", "basic", "560−40=520."),
    ("730-280", "730－280", "standard", "730−280=450.", "A library has 730 books and lends out 280. How many remain?"),
    ("900-350", "900－350", "standard", "900−350=550."),
  ]))

a("estimate_add", "Estimating Sums", NA, "application",
  "Round addends to the nearest ten or hundred to estimate a sum.",
  ["Can round numbers to nearby tens when estimating", "Can judge whether an exact sum is close to an estimate"],
  S("2.NA.06"), ["add_oral_wan"], [
    fact("What is estimation for?", ["quickly finding an approximate value", "always finding the exact answer", "use only in subtraction"],
         "quickly finding an approximate value", "Estimation is used to quickly judge an approximate value.", "basic"),
    calc("40+30", "40＋30", "basic", "38 is close to 40 and 29 is close to 30, so the sum is about 70."),
    story("A shirt costs 198 yuan and a hat costs 102 yuan. About how much do they cost altogether? Round them to 200 yuan and 100 yuan.",
          "200+100", "200＋100", "standard", "198 is close to 200 and 102 is close to 100, for a total of about 300 yuan."),
    calc("500+300", "500＋300", "standard", "486 is close to 500 and 312 is close to 300, so the sum is about 800."),
  ])

a = U(3, "上", 3, "Measurement")
a("mm", "Millimeters", GG, "procedural",
  "Understand millimeters and know that 1 centimeter = 10 millimeters.",
  ["Can state that 1 centimeter equals 10 millimeters", "Can convert several centimeters to millimeters"],
  S("2.GG.03"), ["cm"], [
    ask("How many millimeters are in 3 centimeters?", "3*10", "basic", "1 centimeter = 10 millimeters, so 3 centimeters = 30 millimeters."),
    ask("How many millimeters are in 8 centimeters?", "8*10", "basic", "8×10=80."),
    story("One nail is 2 centimeters long and another is 15 millimeters long. Which is longer? Convert 2 centimeters to millimeters first. How many millimeters are 2 centimeters?",
          "2*10", "2×10", "standard", "2 centimeters = 20 millimeters, which is longer than 15 millimeters."),
    calc("10-4", "10－4", "standard", "1 centimeter = 10 millimeters; after using 4 millimeters, 6 millimeters remain."),
  ])

a("dm", "Decimeters", GG, "procedural",
  "Understand decimeters and know that 1 decimeter = 10 centimeters.",
  ["Can state that 1 decimeter equals 10 centimeters", "Can convert between centimeters and decimeters"],
  S("2.GG.03"), ["cm", "mm"], [
    ask("How many centimeters are in 5 decimeters?", "5*10", "basic", "1 decimeter = 10 centimeters."),
    ask("How many centimeters are in 12 decimeters?", "12*10", "basic", "12×10=120."),
    story("A desk is about 7 decimeters tall. How many centimeters is that?", "7*10", "7×10", "standard", "7×10=70."),
    calc("10-3", "10－3", "standard", "1 decimeter = 10 centimeters, so 3 centimeters is 7 centimeters less than 1 decimeter."),
  ])

a("km", "Kilometers", GG, "procedural",
  "Understand kilometers and know that 1 kilometer = 1000 meters, a suitable unit for longer distances.",
  ["Can state that 1 kilometer equals 1000 meters", "Can convert several kilometers to meters"],
  S("2.GG.03"), ["m_cm"], [
    fact("How many meters are in 1 kilometer?", ["1000 m", "100 m", "10 m"], "1000 m", "1 kilometer = 1000 meters.", "basic"),
    ask("How many meters are in 3 kilometers?", "3*1000", "basic", "3×1000=3000."),
    ask("How many meters are in 6 kilometers?", "6*1000", "standard", "6 kilometers = 6000 meters."),
    story("The school is 2 km from a park, and the park is 1 km from a library. How far is the library from the school?", "2+1", "2＋1", "standard", "2＋1=3."),
  ])

a("ton", "Understanding Tons", NA, "conceptual",
  "Understand the metric ton as a unit of mass and know that 1 metric ton = 1000 kilograms.",
  ["Can state that 1 metric ton equals 1000 kilograms", "Can identify heavy objects measured in metric tons"],
  S(("2.IP.02", "Tons appear in the “Cao Chong Weighs an Elephant” theme. The current Grade 3 Book 1 Measurement unit includes tons. Verification pending.")),
  ["g_kg"], [
    fact("How many kilograms are in 1 metric ton?", ["1000 kg", "100 kg", "1000 g"], "1000 kg", "1 metric ton = 1000 kilograms.", "basic"),
    ask("How many kilograms are in 2 metric tons?", "2*1000", "basic", "2×1000=2000."),
    ask("How many kilograms are in 5 metric tons?", "5*1000", "standard", "5 metric tons = 5000 kilograms."),
    story("A truck can carry 4 metric tons and is already carrying 1. How many more metric tons can it carry?", "4-1", "4－1", "standard", "4−1=3."),
  ])

a = U(3, "上", 4, "Addition and Subtraction Within 10,000 (II)")
a("add_col_wan", "Written Addition of Three-Digit Numbers", NA, "procedural",
  "Use the standard written method to add three-digit numbers, including calculations with consecutive carries.",
  ["Can align digits by place value", "Can handle consecutive carries without shifting digits"],
  S("2.NA.01", "1.NA.04"), ["add_oral_wan", "add_col"], expr4([
    ("234+125", "234＋125", "basic", "234＋125=359."),
    ("406+270", "406＋270", "basic", "406＋270=676."),
    ("368+475", "368＋475", "standard", "Ones: 8＋5=13; tens: 6＋7＋1=14; the sum is 843.", "Two warehouses have 368 boxes and 475 boxes. How many boxes are there altogether?"),
    ("509+286", "509＋286", "standard", "509＋286=795."),
  ]))

a("sub_col_wan", "Written Subtraction of Three-Digit Numbers", NA, "procedural",
  "Use the standard written method to subtract three-digit numbers, including consecutive regrouping.",
  ["Can subtract three-digit numbers", "Can check subtraction using addition"],
  S("1.NA.04"), ["sub_oral_wan", "add_col_wan"], [
    fact("How can addition be checked? Subtract one addend from the sum. If 368＋475=843, what is 843−475?",
         ["subtract one addend from the sum", "multiply the two addends again", "look only at the ones place"],
         "subtract one addend from the sum", "843−475=368, showing how subtraction can check addition.", "basic"),
    calc("756-234", "756－234", "basic", "756−234=522."),
    story("A shelf has 600 books, and 248 are moved away. How many remain?", "600-248", "600－248", "standard", "600−248=352."),
    calc("803-457", "803－457", "standard", "Regroup across places: 803−457=346."),
  ])

a = U(3, "上", 5, "Understanding Multiples")
a("times_n", "Understanding Multiples", NA, "conceptual",
  "Understand that “times as many” means a number of equal groups, and find a multiple of a given number.",
  ["Can find a stated multiple of a number", "Can represent a multiple using multiplication"],
  S("2.NA.08", "1.NA.05"), ["mul79"], mul4([(6, 3), (8, 4), (7, 5), (9, 2)], "red flowers"))

a = U(3, "上", 6, "Multiplying Multi-Digit Numbers by One Digit")
a("mul_1d", "Multiplying Multi-Digit Numbers by One Digit", NA, "procedural",
  "Multiply two- and three-digit numbers by a one-digit number, starting in the ones place and carrying tens to the next place.",
  ["Can use the standard written method to multiply a multi-digit number by a one-digit number", "Can solve multiplication problems involving unit price and quantity"],
  S("2.NA.01"), ["mul79", "add_col_wan"], expr4([
    ("24*2", "24×2", "basic", "24×2=48."),
    ("13*3", "13×3", "basic", "13×3=39."),
    ("36*4", "36×4", "standard", "36×4=144.", "One box of colored pencils costs 36 yuan. How much do 4 boxes cost?"),
    ("208*3", "208×3", "standard", "208×3=624."),
  ]))

a("mul_zero", "Multiplication with Zero in a Factor", NA, "procedural",
  "Multiply when a factor has zero in the middle or at the end, and know that zero times any number is zero.",
  ["Know that 0 multiplied by any number is 0", "Can account for a trailing zero in a product"],
  S("2.NA.01"), ["mul_1d"], expr4([
    ("30*4", "30×4", "basic", "3×4=12; append the trailing zero to get 120."),
    ("50*6", "50×6", "basic", "50×6=300."),
    ("105*4", "105×4", "standard", "105×4=420.", "There are 105 items in each box. How many items are in 4 boxes?"),
    ("200*7", "200×7", "standard", "200×7=1400."),
  ]))

a("code_num", "Numeric Codes", IP, "modeling",
  "Know that numbers can encode information about things and that each digit in a code can have a different meaning.",
  ["Can explain that codes distinguish things", "Can read information from a code using a simple rule"],
  S(("2.NA.05", "The curriculum uses numbers to describe attributes. Numeric coding is a practical topic in the current Grade 3 Book 1; there is no curriculum clause with the same title. Verification pending.")),
  ["know_wan"], [
    fact("What are numeric codes used for?",
         ["to represent and distinguish things using numbers", "to turn every number into 0", "only to do addition"],
         "to represent and distinguish things using numbers", "Student IDs and street numbers can be numeric codes.", "basic"),
    ask("The tens digit is 2 and the ones digit is 5. What is the two-digit number?", "20+5", "basic", "If the tens digit represents a grade and the ones digit a class, 25 could mean Grade 2, Class 5."),
    calc("100+20+4", "100＋20＋4", "standard", "1 hundred, 2 tens, and 4 ones make 124."),
    story("Numbers are assigned from 1 through 30. How many numbers are assigned?", "30-0", "30－0", "standard", "There are 30 numbers from 1 through 30."),
  ])

a = U(3, "上", 7, "Rectangles and Squares")
a("rect_feat", "Properties of Rectangles and Squares", GG, "conceptual",
  "Know that a rectangle has equal opposite sides and four right angles, and that a square has four equal sides.",
  ["Can state that opposite sides of a rectangle are equal", "Can state that all four sides of a square are equal"],
  S("2.GG.04", "1.GG.01"), ["plane"], [
    fact("How do the opposite sides of a rectangle compare?", ["they are equal", "all four sides are different", "it has no right angles"], "they are equal", "Both pairs of opposite sides in a rectangle are equal, and all four angles are right angles.", "basic"),
    fact("How do the four sides of a square compare?", ["all four sides are equal", "only opposite sides are equal", "only three sides are equal"], "all four sides are equal", "A square is a special kind of rectangle.", "basic"),
    calc("4+4", "4＋4", "standard", "One pair of opposite sides of a rectangle is 4 cm each, for a total of 8 cm."),
    calc("6-6", "6－6", "standard", "All four sides of a square are equal, so the difference between two side lengths is 0."),
  ])

a("rect_peri", "Perimeters of Rectangles and Squares", GG, "procedural",
  "Calculate the perimeter of a rectangle or square.",
  ["Can explain that perimeter is the length around a figure", "Can use formulas to find the perimeter of a rectangle or square"],
  S("2.GG.05"), ["rect_feat", "add_col"], [
    fact("What is perimeter?", ["the length around a figure", "the size of the inside of a figure", "the length of one side"], "the length around a figure", "The length of one complete trip around a figure is its perimeter.", "basic"),
    ask("What is the perimeter, in centimeters, of a rectangle 6 cm long and 4 cm wide?", "(6+4)*2", "basic", "(6＋4)×2=20."),
    ask("What is the perimeter, in centimeters, of a square with side length 5 cm?", "5*4", "standard", "5×4=20."),
    story("A rectangular garden is 8 m long and 3 m wide. How many meters of fencing are needed at minimum?", "(8+3)*2", "（8＋3）×2", "standard", "Perimeter=(8＋3)×2=22."),
  ])

a = U(3, "上", 8, "Introduction to Fractions")
a("frac_unit", "Unit Fractions", NA, "conceptual",
  "Develop an initial understanding of unit fractions: when a whole is divided equally into parts, one part is a unit fraction.",
  ["Can identify one equal part as a unit fraction", "Know that the denominator gives the number of equal parts"],
  S("2.NA.02"), ["div_mean"], [
    fact("What does the denominator of a fraction represent?",
         ["the number of equal parts in the whole", "the number of parts taken away", "the number of wholes"],
         "the number of equal parts in the whole", "A denominator of 4 means the whole is divided into 4 equal parts.", "basic"),
    calc("1/2", "1÷2", "basic", "Divide 1 pie into 2 equal parts; each part is 1/2.", True),
    calc("1/4", "1÷4", "standard", "Divide into 4 equal parts; each part is 1/4.", True),
    story("A sheet of paper is divided into 8 equal parts, and 1 part is shaded. What fraction of the sheet is shaded? Use 1÷8 to represent each part.",
          "1/8", "1÷8", "standard", "Each part is 1/8.", True),
  ])

a("frac_same_add", "Adding and Subtracting Fractions with Like Denominators", NA, "procedural",
  "Add and subtract simple fractions with the same denominator when the result does not exceed 1.",
  ["Can add fractions with like denominators", "Can subtract fractions with like denominators"],
  S("2.NA.02"), ["frac_unit"], expr4([
    ("Fraction(1,5)+Fraction(2,5)", "1/5＋2/5", "basic", "Keep the denominator and add the numerators: 1＋2=3, giving 3/5."),
    ("Fraction(3,4)-Fraction(1,4)", "3/4－1/4", "basic", "3/4−1/4=2/4=1/2."),
    ("Fraction(2,8)+Fraction(3,8)", "2/8＋3/8", "standard", "2/8＋3/8=5/8.", "A rope has 2/8 used, then another 3/8 used. What fraction of the rope has been used altogether?"),
    ("Fraction(5,6)-Fraction(1,6)", "5/6－1/6", "standard", "5/6−1/6=4/6=2/3."),
  ]))

a = U(3, "上", 9, "Maths Around Us: Sets")
a("set_gj", "Overlapping Regions in Set Diagrams", IP, "reasoning",
  "Represent two categories with circles; the overlap contains items in both categories and is counted only once when finding the total.",
  ["Can explain what the overlapping region represents", "Know not to count the overlap twice when finding the total"],
  S(("2.NA.10", "Sets appear in the current textbook's “Maths Around Us” feature, not as a separate curriculum topic. Matched here to solving problems using quantitative relationships; verification pending.")),
  ["add_col", "sub_col"], [
    fact("Where are people or items that belong to both groups shown in a set diagram?",
         ["in the overlapping part of the two circles", "outside both circles", "only in the left circle"],
         "in the overlapping part of the two circles", "People who join both activities go in the overlap and are counted only once in the total.", "basic"),
    calc("8+6-3", "8＋6－3", "basic", "8 people play jump rope and 6 play shuttlecock; 3 do both. The total is 8＋6−3=11."),
    story("A language club has 10 members and a math club has 9. Four people belong to both. Counting each person once, how many people are there altogether?",
          "10+9-4", "10＋9－4", "standard", "10＋9−4=15."),
    calc("12+7-5", "12＋7－5", "standard", "12＋7−5=14."),
  ])

# ---------- Grade 3, Term 2 (current) ----------
a = U(3, "下", 1, "Position and Direction (I)")
a("dir8", "Northeast, Southeast, Northwest, and Southwest", GG, "application",
  "Build on north, south, east, and west to understand northeast, southeast, northwest, and southwest.",
  ["Can identify the four diagonal directions", "Can name the opposite direction"],
  S("2.IP.03"), ["dir4"], [
    fact("What is the relationship between east and west? Which direction is opposite northeast?",
         ["opposite directions", "the same direction", "there is no opposite direction"],
         "opposite directions", "Northeast and southwest are opposites; southeast and northwest are opposites.", "basic"),
    calc("2+2", "2＋2", "basic", "Move 2 squares east and then 2 squares north: 2 horizontally and 2 vertically."),
    story("Walk 40 meters east, then 30 meters north. How many meters were walked east?", "40-0", "40－0", "standard", "The eastward distance is 40 meters."),
    story("Walk 50 meters southeast from the plaza to a store, then return 20 meters along the same route. How far are you from the plaza now?", "50-20", "50－20", "standard", "50−20=30."),
  ])

a = U(3, "下", 2, "Division by One-Digit Numbers")
a("div_1d", "Division by One-Digit Numbers", NA, "procedural",
  "Divide two- and three-digit numbers by a one-digit number, starting with the highest place value.",
  ["Can use the standard written method for division by a one-digit number", "Can determine the number of digits in a quotient"],
  S("2.NA.01"), ["div79", "mul_1d"], expr4([
    ("48/2", "48÷2", "basic", "48÷2=24."),
    ("69/3", "69÷3", "basic", "69÷3=23."),
    ("84/4", "84÷4", "standard", "84÷4=21.", "84 pencils are shared equally among 4 groups. How many pencils does each group get?"),
    ("105/5", "105÷5", "standard", "105÷5=21."),
  ]))

a("div_1d_app", "Solving Problems with Division by One-Digit Numbers", NA, "application",
  "Use division by a one-digit number to solve equal-sharing and measurement-division problems.",
  ["Can identify when division is needed", "Can include units and check remainders"],
  S("2.NA.03", "1.NA.07"), ["div_1d"], expr4([
    ("96/3", "96÷3", "basic", "96÷3=32."),
    ("75/5", "75÷5", "basic", "75÷5=15."),
    ("128/4", "128÷4", "standard", "128÷4=32.", "128 people are seated equally in 4 cars. How many people are in each car?"),
    ("200/8", "200÷8", "standard", "200÷8=25."),
  ]))

a = U(3, "下", 3, "Two-Way Tables")
a("stat_table", "Two-Way Tables", SP, "procedural",
  "Organize two categories of data in a two-way table and answer questions about totals and comparisons.",
  ["Can read a value from a table cell", "Can calculate a row or column total"],
  S("2.SP.01", "2.SP.02"), ["classify", "add_col"], [
    calc("12+9", "12＋9", "basic", "There are 12 boys and 9 girls, for a total of 21 students."),
    calc("18-11", "18－11", "basic", "18 people like jump rope and 11 like running, a difference of 7."),
    story("In the first half of the year, 46 storybooks and 35 science books were borrowed. How many books were borrowed altogether?", "46+35", "46＋35", "standard", "46＋35=81."),
    story("Twenty-eight students from Class 1 and 23 from Class 2 participate. How many more are from Class 1?", "28-23", "28－23", "standard", "28−23=5."),
  ])

a = U(3, "下", 4, "Multiplying Two-Digit Numbers")
a("mul_2d", "Multiplying Two-Digit Numbers", NA, "procedural",
  "Multiply two-digit numbers using the standard written method.",
  ["Can multiply by the ones digit first, then by the tens digit", "Can add the two partial products"],
  S("2.NA.01"), ["mul_1d"], expr4([
    ("12*11", "12×11", "basic", "12×11=132."),
    ("15*10", "15×10", "basic", "15×10=150."),
    ("24*13", "24×13", "standard", "24×13=312.", "There are 24 pencils in each box. How many pencils are in 13 boxes?"),
    ("36*25", "36×25", "standard", "36×25=900."),
  ]))

a("mul_2d_app", "Applications of Two-Digit Multiplication", NA, "application",
  "Use two-digit multiplication to solve problems about total price and quantity.",
  ["Can identify the quantity in each group and the number of groups", "Can write and calculate a multiplication expression"],
  S("2.NA.08"), ["mul_2d"], expr4([
    ("16*12", "16×12", "basic", "16×12=192."),
    ("25*14", "25×14", "basic", "25×14=350."),
    ("32*21", "32×21", "standard", "32×21=672.", "There are 32 seats in each row and 21 rows. How many seats are there?"),
    ("18*15", "18×15", "standard", "18×15=270."),
  ]))

a = U(3, "下", 5, "Area")
a("area_mean", "Meaning of Area", GG, "conceptual",
  "Know that area measures the size of a surface or enclosed figure, and use the same area unit when comparing areas.",
  ["Can distinguish perimeter from area", "Know to use the same unit when comparing areas"],
  S("2.GG.05"), ["rect_peri"], [
    fact("What unit is used to measure area?", ["an area unit", "the length of only one side", "kilograms"],
         "an area unit", "Area is measured in square centimeters, square decimeters, and other area units.", "basic"),
    fact("What is perimeter? How is it different from area?", ["the length around a figure", "the size of the space inside a figure", "the weight of a figure"],
         "the length around a figure", "Perimeter is the distance around a figure; area measures the space inside it.", "basic"),
    calc("2*3", "2×3", "standard", "Cover the figure with 1 cm squares: 2 across and 3 down make 6 squares."),
    calc("4*4", "4×4", "standard", "4×4=16."),
  ])

a("rect_area", "Areas of Rectangles and Squares", GG, "procedural",
  "Find a rectangle's area by multiplying its length by its width and a square's area by multiplying its side length by itself.",
  ["Can find the area of a rectangle", "Can find the area of a square"],
  S("2.GG.05"), ["area_mean", "mul_2d"], [
    ask("What is the area, in square centimeters, of a rectangle 8 cm long and 5 cm wide?", "8*5", "basic", "8×5=40."),
    ask("What is the area, in square centimeters, of a square with side length 6 cm?", "6*6", "basic", "6×6=36."),
    story("A blackboard is 4 m long and 1 m wide. What is its area in square meters?", "4*1", "4×1", "standard", "4×1=4."),
    ask("What is the area, in square centimeters, of a rectangle 12 cm long and 3 cm wide?", "12*3", "standard", "12×3=36."),
  ])

a("area_unit", "Converting Area Units", GG, "procedural",
  "Know square centimeters, square decimeters, and square meters, and convert between adjacent units.",
  ["Know that adjacent area units differ by a factor of 100", "Can convert square meters to square decimeters"],
  S("2.GG.03"), ["rect_area", "dm"], [
    ask("How many square decimeters are in 2 square meters?", "2*100", "basic", "1 square meter = 100 square decimeters."),
    ask("How many square decimeters are in 5 square meters?", "5*100", "basic", "5×100=500."),
    story("A plot of land is 3 square meters. What is its area in square decimeters?", "3*100", "3×100", "standard", "3×100=300."),
    calc("100-40", "100－40", "standard", "1 square meter = 100 square decimeters; after using 40 square decimeters, 60 remain."),
  ])

a = U(3, "下", 6, "Year, Month, and Day")
a("ymd", "Year, Month, and Day", NA, "conceptual",
  "Know that a year has 12 months, long months have 31 days, short months have 30 days, and February has 28 days in a common year.",
  ["Can state that a year has 12 months", "Can distinguish February in a common year from February in a leap year"],
  S("2.IP.01"), ["time_hms"], [
    fact("How many months are in a year?", ["12 months", "10 months", "365 months"], "12 months", "There are 12 months in a year.", "basic"),
    fact("How many days are in February in a common year?", ["28 days", "29 days", "30 days"], "28 days", "February has 28 days in a common year and 29 in a leap year.", "basic"),
    fact("How many days are in February in a leap year?", ["29 days", "28 days", "31 days"], "29 days", "February has 1 extra day in a leap year.", "standard"),
    calc("31-30", "31－30", "standard", "A long month has 1 more day than a short month."),
  ])

a("h24", "24-Hour Clock", NA, "procedural",
  "Use the 24-hour clock and know that 1 p.m. is 13:00.",
  ["Can convert an afternoon time to the 24-hour clock", "Can state that 24:00 is 00:00 on the next day"],
  S("2.IP.01"), ["ymd", "time_hms"], [
    calc("12+1", "12＋1", "basic", "1 p.m. is 13:00."),
    calc("12+3", "12＋3", "basic", "3 p.m. is 15:00."),
    story("A train leaves at 16:00. What time is that in the afternoon? Use 16−12.", "16-12", "16－12", "standard", "16−12=4, so it is 4 p.m."),
    calc("12+6", "12＋6", "standard", "6 p.m. is 18:00."),
  ])

a = U(3, "下", 7, "Introduction to Decimals")
a("dec_first", "Introduction to Tenths", NA, "conceptual",
  "Use yuan and jiao or meters and decimeters to understand that a decimal with one digit after the point represents tenths.",
  ["Can write 1 jiao as 0.1 yuan", "Can compare one-place decimals"],
  S("2.NA.02"), ["frac_unit", "rmb"], [
    calc("0.1+0.2", "0.1＋0.2", "basic", "1 jiao plus 2 jiao is 3 jiao, or 0.3 yuan.", True),
    calc("0.8-0.3", "0.8－0.3", "basic", "0.8−0.3=0.5.", True),
    story("A pen costs 0.6 yuan and an eraser costs 0.2 yuan. What is the total cost?", "0.6+0.2", "0.6＋0.2", "standard", "0.6＋0.2=0.8.", True),
    choice_num("0.4＋0.5", "Fraction('0.4')+Fraction('0.5')", ["0.8", "1", "0.45"], "standard", "0.4＋0.5=0.9."),
  ])

a("dec_add1", "Adding and Subtracting One-Place Decimals", NA, "procedural",
  "Add and subtract one-place decimals, aligning the decimal points.",
  ["Can align decimal points before adding or subtracting", "Can place the decimal point correctly in the result"],
  S("2.NA.02"), ["dec_first"], expr4([
    ("Fraction('0.7')+Fraction('0.2')", "0.7＋0.2", "basic", "0.7＋0.2=0.9.", "", True),
    ("Fraction('0.6')-Fraction('0.1')", "0.6－0.1", "basic", "0.6−0.1=0.5.", "", True),
    ("Fraction('1.2')+Fraction('0.4')", "1.2＋0.4", "standard", "1.2＋0.4=1.6.", "A 1.2 m rope is extended by 0.4 m. How long is it now?", True),
    ("Fraction('1.5')-Fraction('0.8')", "1.5－0.8", "standard", "1.5−0.8=0.7.", "", True),
  ]))

a = U(3, "下", 8, "Maths Around Us: Combinations")
a("arrange", "Simple Combinations", IP, "reasoning",
  "Count combinations of two types of items systematically, without repetition or omission.",
  ["Can pair items systematically, one at a time", "Can use multiplication to find the number of combinations"],
  S(("2.NA.10", "Combinations appear in the current Grade 3 Book 2 “Maths Around Us” feature; the curriculum has no topic with the same name. Verification pending.")),
  ["mul26"], [
    fact("When pairing items, if different orders count as different, how should they be counted?",
         ["count each different order separately", "count only one pairing", "subtract all pairings"],
         "count each different order separately", "For ordered pairings, choose one item first and then pair it with another.", "basic"),
    calc("2*3", "2×3", "basic", "2 tops paired with 3 skirts make 6 combinations."),
    story("There are 3 kinds of bread and 2 kinds of drink. Each bread can be paired with each drink. How many combinations are there?", "3*2", "3×2", "standard", "3×2=6."),
    calc("4*3", "4×3", "standard", "4×3=12."),
  ])

# ---------- Grade 4, Term 1 (current) ----------
a = U(4, "上", 1, "Understanding Large Numbers")
a("big_num", "Numbers up to 100 Million", NA, "conceptual",
  "Understand the ten-thousands and hundred-millions periods, know the decimal place-value system, and read and write large numbers.",
  ["Can read large numbers by periods", "Know that each period contains four place values"],
  S("2.NA.01"), ["know_wan"], [
    ask("What is the thousands digit in 10000?", "0", "basic", "The thousands digit in 10000 is 0; the ten-thousands digit is 1."),
    calc("10000+2000", "10000＋2000", "basic", "10,000 plus 2,000 is 12,000."),
    ask("What is the hundreds digit in 30500?", "5", "standard", "The hundreds digit in 30500 is 5."),
    story("One school has about 2,000 students and another has about 3,000. About how many students do they have altogether?", "2000+3000", "2000＋3000", "standard", "2000＋3000=5000."),
  ])

a("big_approx", "Rewriting and Rounding Large Numbers", NA, "procedural",
  "Rewrite large numbers using ten-thousands or hundred-millions as units, and round to find an approximation.",
  ["Can rewrite a whole multiple of 10,000 as a number of ten-thousands", "Can identify which digit to inspect when rounding"],
  S("2.NA.06", "2.NA.01"), ["big_num"], [
    calc("230000/10000", "230000÷10000", "basic", "230000=23 ten-thousands."),
    calc("48000/10000", "48000÷10000", "basic", "48000 is 4.8 ten-thousands.", True),
    story("A city has about 1,260,000 people. Express this in ten-thousands. What is the value?", "1260000/10000", "1260000÷10000", "standard", "1260000=126 ten-thousands."),
    calc("3500/1000", "3500÷1000", "standard", "To the nearest thousand, 3500 is 3.5 thousands.", True),
  ])

a = U(4, "上", 2, "Hectares and Square Kilometers")
a("hectare", "Hectares and Square Kilometers", GG, "procedural",
  "Understand hectares and square kilometers, and know that 1 hectare = 10,000 square meters and 1 square kilometer = 100 hectares.",
  ["Can state that 1 hectare equals 10,000 square meters", "Can identify hectares as a common unit for land area"],
  S(("3.GG.03", "Hectares and square kilometers appear in the third stage of the curriculum. The current textbook teaches them in Grade 4 Book 1, so they are treated as appearing earlier by content. Verification pending.")),
  ["area_unit", "km"], [
    fact("What kind of unit is a hectare?", ["an area unit", "a mass unit", "a time unit"], "an area unit", "Hectares measure large areas of land.", "basic"),
    ask("How many square meters are in 2 hectares?", "2*10000", "basic", "1 hectare = 10,000 square meters."),
    ask("How many square meters are in 3 hectares?", "3*10000", "standard", "3×10000=30000."),
    story("A park covers 4 hectares and a school covers 1 hectare. How many hectares larger is the park?", "4-1", "4－1", "standard", "4−1=3."),
  ])

a = U(4, "上", 3, "Measuring Angles")
a("line_seg", "Line Segments, Lines, and Rays", GG, "conceptual",
  "Distinguish line segments, lines, and rays, and know that the shortest distance between two points is the line segment joining them.",
  ["Can state that a line segment has two endpoints", "Know that a line has no endpoints and a ray has one"],
  S("2.GG.01"), ["rect_feat"], [
    fact("Perimeter is the length around a figure. Compared with a line, how many endpoints does a line segment have? Which statement describes a line segment?",
         ["the length around a figure", "an area unit", "a mass unit"],
         "the length around a figure", "A line segment has a measurable length; perimeter is the sum of the lengths of several segments.", "basic"),
    calc("8-3", "8－3", "basic", "Between two points, a curved path is 8 cm long and a line segment is 3 cm long. The segment is 5 cm shorter."),
    story("The route along the street from home to school is 400 m, while a shortcut is 250 m. How many meters shorter is the shortcut?", "400-250", "400－250", "standard", "The line segment between two points is the shortest distance, and 400−250=150."),
    calc("5+5", "5＋5", "standard", "Join two 5 cm segments end to end on a straight line. The total length is 10 cm."),
  ])

a("angle_measure", "Measuring Angles", GG, "procedural",
  "Identify the parts of an angle, measure angles with a protractor, and draw angles of a specified measure.",
  ["Can identify the vertex and two sides", "Know that the degree is the unit for measuring angles"],
  S("2.GG.02"), ["line_seg"], [
    calc("90-30", "90－30", "basic", "A right angle is 90°. An angle of 30° is 60° smaller."),
    calc("180-90", "180－90", "basic", "A straight angle is 180°, equal to 2 right angles."),
    story("One angle is 35° and another is 20°. What is their combined measure?", "35+20", "35＋20", "standard", "35＋20=55."),
    story("An 80° angle is divided into 2 equal parts. How many degrees is each part?", "80/2", "80÷2", "standard", "80÷2=40."),
  ])

a("angle_class", "Acute, Right, and Obtuse Angles", GG, "conceptual",
  "Identify acute, right, and obtuse angles by their measures, and know straight and full angles.",
  ["Can state that an acute angle is less than 90°", "Can state that an obtuse angle is greater than 90° and less than 180°"],
  S("2.GG.02", "2.GG.04"), ["angle_measure"], [
    fact("How does a right angle compare with an acute angle?", ["a right angle is larger", "a right angle is smaller", "they are equal"], "a right angle is larger", "An acute angle is smaller than a right angle.", "basic"),
    fact("How does an obtuse angle compare with a right angle?", ["an obtuse angle is larger", "an obtuse angle is smaller", "an obtuse angle is equal"], "an obtuse angle is larger", "An obtuse angle is greater than 90° and less than 180°.", "basic"),
    calc("90-45", "90－45", "standard", "A 45° angle is acute and 45° smaller than a right angle."),
    calc("120-90", "120－90", "standard", "A 120° angle is obtuse and 30° larger than a right angle."),
  ])

a = U(4, "上", 4, "Multiplying Three-Digit Numbers by Two-Digit Numbers")
a("mul_3d", "Multiplying Three-Digit Numbers by Two-Digit Numbers", NA, "procedural",
  "Multiply a three-digit number by a two-digit number and estimate the number of digits in the product.",
  ["Can use the standard written method for three-digit by two-digit multiplication", "Can estimate the approximate product"],
  S("2.NA.01"), ["mul_2d"], expr4([
    ("123*10", "123×10", "basic", "123×10=1230."),
    ("200*12", "200×12", "basic", "200×12=2400."),
    ("125*16", "125×16", "standard", "125×16=2000.", "There are 125 bottles in each box. How many bottles are in 16 boxes?"),
    ("308*24", "308×24", "standard", "308×24=7392."),
  ]))

a = U(4, "上", 5, "Parallelograms and Trapezoids")
a("perp", "Perpendicularity", GG, "conceptual",
  "Know that two lines intersecting at a right angle are perpendicular and that their intersection is the foot of the perpendicular.",
  ["Can explain that perpendicular lines intersect at a right angle", "Can identify perpendicular lines in everyday settings"],
  S("2.GG.01"), ["angle_class"], [
    fact("Two lines intersect at a right angle. What is their relationship?",
         ["they are perpendicular", "they are parallel", "they coincide"],
         "they are perpendicular", "Lines that intersect at a right angle are perpendicular.", "basic"),
    calc("90-0", "90－0", "basic", "The angle between perpendicular lines is 90°."),
    story("A flagpole meets the ground at a right angle. How many degrees is the angle?", "45+45", "45＋45", "standard", "A right angle is 90°."),
    calc("180-90", "180－90", "standard", "A straight angle is 180°; perpendicularity divides it into 90° angles."),
  ])

a("parallel", "Parallelism", GG, "conceptual",
  "Know that two nonintersecting lines in the same plane are parallel.",
  ["Can state that parallel lines do not intersect", "Can distinguish parallel from perpendicular lines"],
  S("2.GG.01"), ["perp", "line_seg"], [
    fact("What is the relationship between two nonintersecting lines in the same plane?",
         ["they are parallel", "they are perpendicular", "they must coincide"],
         "they are parallel", "Two nonintersecting lines in the same plane are parallel.", "basic"),
    calc("2+2", "2＋2", "basic", "Many equal perpendicular segments can be drawn between two parallel lines."),
    story("The two rails of a track are parallel. One section is 20 m long, and another is also 20 m. What is the difference in their lengths?", "20-20", "20－20", "standard", "Parallel segments can have the same length, so the difference is 0."),
    calc("5-5", "5－5", "standard", "Parallel lines do not intersect; their lengths can still have a difference of 0."),
  ])

a("para_trap", "Properties of Parallelograms and Trapezoids", GG, "conceptual",
  "Know that a parallelogram has two pairs of parallel, equal opposite sides and that a trapezoid has one pair of parallel sides.",
  ["Can describe the opposite sides of a parallelogram", "Can state that a trapezoid has one pair of parallel sides"],
  S("2.GG.04"), ["parallel"], [
    fact("How do the opposite sides of a parallelogram compare?", ["they are parallel and equal", "none of the four sides are parallel", "it has only one side"],
         "they are parallel and equal", "Both pairs of opposite sides in a parallelogram are parallel and equal.", "basic"),
    fact("What is a defining feature of a trapezoid?", ["one pair of parallel sides", "all four sides are equal", "no sides are parallel"],
         "one pair of parallel sides", "A trapezoid has one pair of parallel sides.", "basic"),
    calc("6+6", "6＋6", "standard", "One pair of opposite sides of a parallelogram is 6 cm each, for a total of 12 cm."),
    calc("10-4", "10－4", "standard", "The two bases of a trapezoid are 10 cm and 4 cm, a difference of 6 cm."),
  ])

a = U(4, "上", 6, "Division by Two-Digit Numbers")
a("div_2d", "Division by Two-Digit Numbers", NA, "procedural",
  "Divide by a two-digit number, using a multiple of ten to estimate the quotient.",
  ["Can estimate and adjust a quotient", "Can divide a three-digit number by a two-digit number"],
  S("2.NA.01"), ["div_1d", "mul_2d"], expr4([
    ("96/12", "96÷12", "basic", "96÷12=8."),
    ("150/25", "150÷25", "basic", "150÷25=6."),
    ("288/16", "288÷16", "standard", "288÷16=18.", "There are 288 notebooks, bundled 16 per stack. How many stacks can be made?"),
    ("420/15", "420÷15", "standard", "420÷15=28."),
  ]))

a("div_stable", "The Invariant Quotient Property", NA, "reasoning",
  "Know that multiplying or dividing both the dividend and divisor by the same nonzero number leaves the quotient unchanged.",
  ["Can state the invariant quotient property", "Can use it to simplify division"],
  S("2.NA.01", "2.NA.04"), ["div_2d"], [
    calc("80/20", "80÷20", "basic", "80÷20=4. Divide both dividend and divisor by 10: 8÷2 is still 4."),
    calc("8/2", "8÷2", "basic", "8÷2=4, the same quotient as 80÷20."),
    story("For 600÷30, remove one zero from both numbers and first calculate 60÷3. What is 60÷3?", "60/3", "60÷3", "standard", "60÷3=20, so 600÷30=20."),
    calc("120/40", "120÷40", "standard", "120÷40=3."),
  ])

a = U(4, "上", 7, "Bar Charts")
a("bar", "Bar Charts", SP, "procedural",
  "Understand bar charts, draw simple bar charts from tables, and compare quantities.",
  ["Can read the quantity represented by each bar", "Can state that a taller bar represents a greater quantity"],
  S("2.SP.03"), ["stat_table"], [
    fact("What are bar charts best for showing?", ["how quantities compare", "how a quantity changes", "what percentage each part is of the total"],
         "how quantities compare", "Bar height represents quantity.", "basic"),
    calc("12-7", "12－7", "basic", "The tallest bar is 12 and another is 7, a difference of 5."),
    story("Fifteen people like apples and 9 like bananas. How many more people like apples?", "15-9", "15－9", "standard", "15−9=6."),
    story("The numbers of books borrowed over four days are 8, 6, 10, and 4. Which two days add up to 14 books? Start with 8＋6.", "8+6", "8＋6", "standard", "8＋6=14, for the first and second days."),
  ])

a = U(4, "上", 8, "Maths Around Us: Optimization")
a("optimize", "Simple Optimization", IP, "reasoning",
  "Arrange activities to save time, for example, washing cups while water boils.",
  ["Can identify two activities that can happen at the same time", "Can calculate the time required after optimizing the schedule"],
  S(("2.NA.10", "Optimization appears in the current Grade 4 Book 1 “Maths Around Us” feature; the curriculum has no topic with the same name. Verification pending.")),
  ["add_col", "elapsed"], [
    fact("How should activities be scheduled in an optimization problem?",
         ["arrange them to save time", "do everything separately as slowly as possible", "do only one activity"],
         "arrange them to save time", "Activities that can happen at the same time do not need to be done one after another.", "basic"),
    calc("8+1", "8＋1", "basic", "Boiling water takes 8 minutes and washing cups takes 1 minute. If the cups are washed while the water boils, the total still takes about 8 minutes; doing them separately would take 8＋1=9 minutes."),
    story("It takes 3 minutes to cook one pancake, and the pan can cook 2 at once. What is the minimum time to cook 2 pancakes?", "3+0", "3＋0", "standard", "Cook both at once; it takes 3 minutes."),
    story("Walking takes 10 minutes and buying a ticket takes 2. If one person does these tasks one after the other, how many minutes do they take altogether?", "10+2", "10＋2", "standard", "10＋2=12."),
  ])
