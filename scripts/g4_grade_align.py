#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Align Grade 4 question-bank difficulty and write diagnostic questions to data/questions.json, topics.json, and _qbatches/primary_g4.json.

Each topic gets 2 basic, 1 standard, and 1 challenge question. Basic questions directly assess the topic;
standard questions match textbook examples; challenge questions add a step or target a common error, rather than asking only "Calculate: ... = ?".
"""
import os
import sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import validate as V  # noqa: E402
import verify_questions as VQ  # noqa: E402


def n(diff, prompt, answer, expl, verify):
    return {
        "difficulty": diff, "type": "numeric", "prompt": prompt,
        "answer": str(answer), "explanation": expl, "verify": verify,
    }


def c(diff, prompt, options, correct, expl, verify=None):
    keys = "ABCD"
    q = {
        "difficulty": diff, "type": "choice", "prompt": prompt,
        "choices": [{"key": keys[i], "text": t} for i, t in enumerate(options)],
        "answer": correct, "explanation": expl,
    }
    if verify is None:
        verify = repr(options["ABCD".index(correct)])
    q["verify"] = verify
    return q


BANK = {}

# ---------- Grade 4, first semester, Unit 1: Numbers greater than 10,000 ----------
BANK["cnm_p096"] = [
    n("basic", "What digit is in the ten-thousands place of 10000?",
      "1", "The ten-thousands digit of 10000 is 1; the thousands, hundreds, tens, and ones digits are all 0.", "1"),
    n("basic", "What is the hundreds digit of 30500?",
      "5", "From the right, the places are ones, tens, hundreds; the third digit is the hundreds digit, so it is 5 in 30500.", "5"),
    n("standard", "A number has 2 in the ten-thousands place, 4 in the thousands place, and 0 in the hundreds, tens, and ones places. What is the number?",
      "24000", "The ten-thousands digit is 2 and the thousands digit is 4, followed by three zeros: 24000.", "24000"),
    n("challenge", "How much greater is the greatest five-digit number than the least five-digit number?",
      "89999", "The greatest five-digit number is 99999 and the least is 10000; their difference is 99999－10000＝89999.",
      "99999-10000"),
]

BANK["cnm_p097"] = [
    n("basic", "Express 230000 in units of ten-thousands. How many ten-thousands is that?",
      "23", "230000＝23 groups of 10000, so it is written as 23 ten-thousands.", "230000/10000"),
    n("basic", "Express 48000 in units of ten-thousands. How many ten-thousands is that? (Answer as a decimal.)",
      "4.8", "48000＝4.8 groups of 10000, so it is written as 4.8 ten-thousands.", "Fraction(48000,10000)"),
    n("standard", "A city has about 1260000 people. Express this in units of ten-thousands. How many ten-thousands is that?",
      "126", "1260000÷10000＝126, so it is written as 126 ten-thousands.", "1260000/10000"),
    n("challenge", "Round 35280 to the nearest ten-thousand. What is the approximate value?",
      "40000", "The thousands digit is 5, so round the ten-thousands digit up by 1: 35280≈40000.", "40000"),
]

BANK["cnm_p236"] = [
    n("basic", "How many ten-millions are in one hundred million?",
      "10", "One hundred million＝10 ten-millions.", "100000000//10000000"),
    c("basic", "Which numeral represents one hundred million?",
      ["100000000", "10000000", "1000000000"], "A",
      "One hundred million is 1 followed by 8 zeros, written as 100000000.", "'100000000'"),
    n("standard", "How many ten-thousands are in one hundred million?",
      "10000", "One hundred million＝10000 ten-thousands.", "100000000//10000"),
    n("challenge", "It takes about 1 hour to count 10000 grains of rice. At that rate, about how many hours would it take to count 100000000 grains?",
      "10000", "One hundred million contains 10000 groups of 10000, so it would take about 10000 hours.", "100000000//10000"),
]

# ---------- Grade 4, first semester, Unit 2: Measuring angles ----------
BANK["cnm_p100"] = [
    c("basic", "When measuring an angle with a protractor, which part of the angle should align with the protractor's center?",
      ["Vertex", "Midpoint of either side", "Outside the angle"], "A",
      "Place the center at the vertex, align the zero-degree line with one ray, then read the mark where the other ray crosses.", "'Vertex'"),
    n("basic", "The two sides of an angle line up with 0 degrees and 40 degrees on a protractor. How many degrees is the angle?",
      "40", "The other side lines up with 40 degrees, so the angle measures 40 degrees.", "40"),
    n("standard", "A right angle is 90 degrees and another angle is 35 degrees. How many degrees smaller is the other angle?",
      "55", "90－35＝55 degrees.", "90-35"),
    n("challenge", "Draw a 50-degree angle, then draw a 40-degree angle outward from one of its sides. What is the measure of the combined angle?",
      "90", "Combine the two angles: 50＋40＝90 degrees.", "50+40"),
]

BANK["cnm_p232"] = [
    n("basic", "How many degrees are in a straight angle?",
      "180", "The sides of a straight angle lie on one straight line, so it measures 180 degrees.", "180"),
    c("basic", "An angle measures 125°. What kind of angle is it?",
      ["Obtuse angle", "Acute angle", "Straight angle", "Right angle"], "A",
      "An angle greater than 90 degrees and less than 180 degrees is obtuse.", "'Obtuse angle'"),
    n("standard", "How many right angles make one full turn?",
      "4", "A full turn is 360 degrees and a right angle is 90 degrees; 360÷90＝4.", "360//90"),
    n("challenge", "An obtuse angle is 35 degrees greater than a right angle. How many degrees is the obtuse angle?",
      "125", "A right angle is 90 degrees; add 35 degrees: 90＋35＝125 degrees.", "90+35"),
]

# ---------- Grade 4, first semester, Unit 3: Multiplying multidigit numbers by two-digit numbers ----------
BANK["cnm_p086"] = [
    n("basic", "What is the product of 12×11?",
      "132", "12×10＝120; add 12 to get 132.", "12*11"),
    n("basic", "Each box contains 15 pencils. How many pencils are in 12 boxes?",
      "180", "15×12＝180 pencils.", "15*12"),
    n("standard", "Each box contains 24 pencils. How many pencils are in 13 boxes?",
      "312", "24×13＝312 pencils.", "24*13"),
    n("challenge", "Each case contains 36 bottles. After buying 25 cases and selling 200 bottles, how many bottles remain?",
      "700", "There are 36×25＝900 bottles in all, so 900－200＝700 bottles remain.", "36*25-200"),
]

BANK["cnm_p087"] = [
    n("basic", "There are 16 seats in each row and 12 rows. How many seats are there altogether?",
      "192", "16×12＝192 seats.", "16*12"),
    n("basic", "Each workbook has 25 pages. How many pages are there in 14 workbooks?",
      "350", "25×14＝350 pages.", "25*14"),
    n("standard", "There are 32 seats in each row and 21 rows. How many seats are there altogether?",
      "672", "32×21＝672 seats.", "32*21"),
    n("challenge", "Each case contains 18 bottles. After buying 15 cases and drinking 50 bottles, how many bottles remain?",
      "220", "There are 18×15＝270 bottles in all, so 270－50＝220 bottles remain.", "18*15-50"),
]

BANK["cnm_p102"] = [
    n("basic", "What is the product of 123×11?",
      "1353", "123×10＝1230; add 123 to get 1353.", "123*11"),
    n("basic", "Each case contains 200 books. How many books are in 12 cases?",
      "2400", "200×12＝2400 books.", "200*12"),
    n("standard", "Each case contains 125 bottles. How many bottles are in 16 cases?",
      "2000", "125×16＝2000 bottles.", "125*16"),
    n("challenge", "A book has 308 pages. How many pages are in 24 copies?",
      "7392", "308×24＝7392 pages.", "308*24"),
]

BANK["cnm_p233"] = [
    n("basic", "Estimate 49×21 by rounding the numbers to 50 and 20. What is the approximate product?",
      "1000", "50×20＝1000.", "50*20"),
    n("basic", "Estimate 302×19 by rounding the numbers to 300 and 20. What is the approximate product?",
      "6000", "300×20＝6000.", "300*20"),
    c("standard", "A backpack costs 38 yuan. You want to buy 21. Is 700 yuan enough?",
      ["Not enough", "Enough", "Exactly enough"], "A",
      "38×21 is close to 40×20＝800, which is greater than 700, so it is not enough.", "'Not enough'"),
    n("challenge", "A book costs 38 yuan and you buy 21. Estimate using 40 for 38 and 20 for 21. How many yuan greater is the estimate than the actual cost?",
      "2", "The estimate is 40×20＝800 and the actual cost is 38×21＝798, so the estimate is 800－798＝2 yuan greater.", "40*20-38*21"),
]

# ---------- Grade 4, first semester, Unit 4: Addition and multiplication models ----------
BANK["cnm_p111"] = [
    n("basic", "A notebook costs 8 yuan. How much do 6 notebooks cost?",
      "48", "Total cost＝unit price×quantity: 8×6＝48 yuan.", "8*6"),
    n("basic", "A car travels at 60 kilometers per hour for 3 hours. How far does it travel?",
      "180", "Distance＝speed×time: 60×3＝180 kilometers.", "60*3"),
    n("standard", "Six identical notebooks cost 48 yuan. How much does each notebook cost?",
      "8", "Unit price＝total cost÷quantity: 48÷6＝8 yuan.", "48//6"),
    n("challenge", "A car travels at 60 kilometers per hour. After traveling for 2 hours, it has 180 kilometers left to go. How many more hours will it take?",
      "3", "Remaining time＝distance÷speed: 180÷60＝3 hours.", "180//60"),
]

BANK["cnm_p230"] = [
    n("basic", "Class 1 has 23 boys and 21 girls. How many students are there altogether?",
      "44", "Total＝part＋part: 23＋21＝44 students.", "23+21"),
    n("basic", "A school buys 120 books and lends out 75. How many books are left?",
      "45", "Remaining part＝total－other part: 120－75＝45 books.", "120-75"),
    n("standard", "The trip from home to a bookstore is 450 meters, and from the bookstore to school is 380 meters. How far is it from home to school via the bookstore?",
      "830", "The two distances are parts of the whole trip, so add them: 450＋380＝830 meters.", "450+380"),
    n("challenge", "A fruit shop receives 85 kilograms of apples and 60 kilograms of pears in the morning. In the afternoon, it sells 40 kilograms of apples and 25 kilograms of pears. How many kilograms of fruit remain?",
      "80", "The shop receives 85＋60＝145 kilograms and sells 40＋25＝65 kilograms, leaving 145－65＝80 kilograms.",
      "85+60-40-25"),
]

BANK["cnm_p231"] = [
    n("basic", "Each pen costs 6 yuan. How much do 12 pens cost?",
      "72", "Total cost＝unit price×quantity: 6×12＝72 yuan.", "6*12"),
    n("basic", "A car travels at 60 kilometers per hour. How far does it travel in 4 hours?",
      "240", "Distance＝speed×time: 60×4＝240 kilometers.", "60*4"),
    n("standard", "Five identical backpacks cost 175 yuan altogether. How much does each backpack cost?",
      "35", "Unit price＝total cost÷quantity: 175÷5＝35 yuan.", "175//5"),
    n("challenge", "Ming rides a bicycle 36 kilometers in 3 hours. At the same speed, how many kilometers will he have ridden in total after another 2 hours?",
      "60", "He travels 36÷3＝12 kilometers per hour; in 5 hours, he travels 12×5＝60 kilometers.", "36//3*(3+2)"),
]

# ---------- Grade 4, first semester, Unit 5: Parallelograms and trapezoids ----------
BANK["cnm_p103"] = [
    c("basic", "Two lines intersect at a right angle. What is their relationship?",
      ["Perpendicular", "Parallel", "Coincident"], "A",
      "Two lines that intersect at a right angle are perpendicular.", "'Perpendicular'"),
    n("basic", "Two perpendicular lines intersect and form 4 angles. How many of them are right angles?",
      "4", "When two lines are perpendicular, all 4 angles are right angles.", "4"),
    n("standard", "A flagpole is perpendicular to the ground. What is the angle between the flagpole and the ground?",
      "90", "Perpendicular lines form a right angle, which measures 90 degrees.", "90"),
    n("challenge", "How many perpendicular lines can be drawn through a point outside a given line?",
      "1", "Exactly 1 line through a point outside a given line is perpendicular to that line.", "1"),
]

BANK["cnm_p104"] = [
    c("basic", "In the same plane, what is the relationship between two lines that do not intersect?",
      ["Parallel", "Perpendicular", "They must coincide"], "A",
      "Two non-intersecting lines in the same plane are parallel.", "'Parallel'"),
    n("basic", "How many pairs of parallel sides does a rectangle have?",
      "2", "The two pairs of opposite sides of a rectangle are parallel, so there are 2 pairs.", "2"),
    c("standard", "How does the distance between two parallel lines vary?",
      ["It is the same everywhere", "It is wider in some places and narrower in others", "It is always 0"], "A",
      "The distance between parallel lines is the same everywhere.", "'It is the same everywhere'"),
    n("challenge", "A perpendicular segment between two parallel lines is 5 centimeters long. How long is a perpendicular segment drawn at another point?",
      "5", "The perpendicular segments measure the distance between the parallel lines, which is the same everywhere: 5 centimeters.", "5"),
]

BANK["cnm_p105"] = [
    c("basic", "What is true of the opposite sides of a parallelogram?",
      ["They are parallel and equal in length", "None of the four sides are parallel", "Only one side is parallel"], "A",
      "Both pairs of opposite sides in a parallelogram are parallel and equal in length.", "'They are parallel and equal in length'"),
    c("basic", "What is the defining property of a trapezoid?",
      ["One pair of opposite sides is parallel", "All four sides are equal", "It has no parallel sides"], "A",
      "A trapezoid has one pair of parallel opposite sides.", "'One pair of opposite sides is parallel'"),
    n("standard", "Adjacent sides of a parallelogram are 6 centimeters and 4 centimeters long. What is its perimeter?",
      "20", "Opposite sides are equal: (6＋4)×2＝20 centimeters.", "(6+4)*2"),
    n("challenge", "One pair of opposite sides of a parallelogram is 8 centimeters long, and its perimeter is 28 centimeters. How long is each side in the other pair?",
      "6", "The first pair totals 16 centimeters. The other pair totals 28－16＝12 centimeters, so each side is 12÷2＝6 centimeters.",
      "(28-8*2)//2"),
]

BANK["cnm_p234"] = [
    c("basic", "When drawing parallel lines with a ruler and set square, how should you move the set square?",
      ["Rotate it freely", "Move it away from the ruler", "Slide it along the ruler"], "C",
      "Keep one right-angle edge of the set square against the ruler and slide it to draw a parallel line.", "'Slide it along the ruler'"),
    n("basic", "How many lines parallel to a given line can be drawn through a point outside it?",
      "1", "Exactly 1 line through a point outside a given line is parallel to it.", "1"),
    c("standard", "Several perpendicular segments are drawn between two parallel lines. How do their lengths compare?",
      ["They get longer", "They are not necessarily equal", "They are all equal"], "C",
      "The distance between parallel lines is constant, so all these perpendicular segments have the same length.", "'They are all equal'"),
    n("challenge", "The distance between two parallel lines is 6 centimeters. A perpendicular is drawn from a point on one line to the other. How long is it?",
      "6", "The perpendicular measures the distance between the parallel lines, so it is 6 centimeters long.", "6"),
]

# ---------- Grade 4, first semester, Unit 6: Bar graphs ----------
BANK["cnm_p108"] = [
    c("basic", "What is a bar graph useful for?",
      ["Comparing quantities", "Showing how a quantity changes", "Showing each part as a percentage of the total"], "A",
      "The length of each bar represents its quantity; a longer bar means a greater quantity.", "'Comparing quantities'"),
    n("basic", "On a bar graph, the bar for people who like apples reaches 15, and the bar for people who like bananas reaches 9. How many people like apples?",
      "15", "The value at the end of the bar is the quantity, so 15 people like apples.", "15"),
    n("standard", "Fifteen people like apples and 9 like bananas. How many more people like apples?",
      "6", "15－9＝6 people.", "15-9"),
    n("challenge", "The numbers of books borrowed over four days are 8, 6, 10, and 5. How many more books were borrowed on the busiest day than on the least busy day?",
      "5", "The greatest number is 10 and the least is 5, so the difference is 10－5＝5 books.", "10-5"),
]

BANK["cnm_p130"] = [
    c("basic", "Compared with a single bar graph, what is the main advantage of a double bar graph?",
      ["It can compare two data sets at once", "It can show only one number", "It shows each part as a percentage of the total"], "A",
      "A double bar graph displays two data sets on the same graph for easy comparison.", "'It can compare two data sets at once'"),
    n("basic", "On a double bar graph, the boys' bar for jump rope represents 20 students. How many boys are there?",
      "20", "The bar reaches 20, so there are 20 boys.", "20"),
    n("standard", "On a double bar graph, 20 boys and 14 girls choose jump rope. How many students choose jump rope altogether?",
      "34", "Add the two groups for the same activity: 20＋14＝34 students.", "20+14"),
    n("challenge", "In Class 1, 16 students choose jump rope and 12 choose shuttlecock kicking. In Class 2, 11 choose jump rope and 15 choose shuttlecock kicking. How many students in both classes choose jump rope?",
      "27", "Compare the jump-rope data only: 16＋11＝27 students. Do not include the shuttlecock-kicking totals.", "16+11"),
]

# ---------- Grade 4, first-semester integrated practice: Treasure hunt ----------
BANK["cnm_p235"] = [
    n("basic", "Walk 30 meters east from the starting point, then continue 45 meters east. How far are you from the start?",
      "75", "The directions are the same, so add the distances: 30＋45＝75 meters.", "30+45"),
    c("basic", "Stand facing north and turn right. Which direction are you facing now?",
      ["South", "East", "West"], "B",
      "When facing north, east is on your right; after turning right, you face east.", "'East'"),
    n("standard", "On a treasure map, 1 grid square represents 10 meters. The treasure is 6 squares east of the start. How far away is it?",
      "60", "10×6＝60 meters.", "10*6"),
    n("challenge", "Walk 80 meters north from the start, then 30 meters south, then 40 meters east. How far north of the start are you?",
      "50", "For the north-south distance, calculate 80－30＝50 meters. Walking east does not change it.", "80-30"),
]

# ---------- Grade 4, first-semester math exploration: Chickens and rabbits in a cage ----------
BANK["cnm_p131"] = [
    c("basic", "Which method can solve the chickens-and-rabbits problem?",
      ["Assume they are all chickens, then adjust", "Multiply the number of chickens by the number of rabbits", "Count the chickens but not their legs"], "A",
      "First assume they are all chickens, then use the extra legs to determine how many should be rabbits.", "'Assume they are all chickens, then adjust'"),
    n("basic", "If all 8 animals are assumed to be chickens, how many legs are there altogether?",
      "16", "Each chicken has 2 legs: 8×2＝16 legs.", "8*2"),
    n("standard", "A cage contains 8 chickens and rabbits with 26 legs altogether. How many rabbits are there?",
      "5", "If all were chickens, there would be 16 legs, which is 10 fewer. Each rabbit has 2 more legs than a chicken, so 10÷2＝5 rabbits.",
      "(26-8*2)//2"),
    n("challenge", "There are 10 chickens and rabbits with 32 legs altogether. How many chickens are there?",
      "4", "If all were chickens, there would be 20 legs, 12 fewer than the actual total. There are 12÷2＝6 rabbits, so 10－6＝4 chickens.",
      "10-(32-10*2)//2"),
]

# ---------- Grade 4, second semester, Unit 1: Four operations ----------
BANK["cnm_p110"] = [
    n("basic", "Two numbers add up to 36. If one addend is 15, what is the other?",
      "21", "Subtract one addend from the sum to find the other: 36－15＝21.", "36-15"),
    n("basic", "The product of two factors is 48. If one factor is 6, what is the other?",
      "8", "Divide the product by one factor to find the other: 48÷6＝8.", "48//6"),
    n("standard", "Two numbers add up to 70. If one is 28, what is the other?",
      "42", "70－28＝42.", "70-28"),
    n("challenge", "The product of three numbers is 72. Two of the factors are 3 and 8. What is the third factor?",
      "3", "Multiply the known factors first: 3×8＝24. The third factor is 72÷24＝3.", "72//(3*8)"),
]

BANK["cnm_p112"] = [
    n("basic", "The order of operations is parentheses first, then multiplication and division, then addition and subtraction. What is 50－（8＋12）×2?",
      "10", "First calculate 8＋12＝20, then 20×2＝40, and finally 50－40＝10.", "50-(8+12)*2"),
    n("basic", "What is （12＋8）×3?",
      "60", "First calculate inside the parentheses: 12＋8＝20, then 20×3＝60.", "(12+8)*3"),
    n("standard", "What is 96÷4－7?",
      "17", "Without parentheses, calculate multiplication and division first: 96÷4＝24, then 24－7＝17.", "96//4-7"),
    n("challenge", "There are 3 boxes of pencils with 12 pencils in each. Six more pencils are taken out, then all the pencils are shared equally among 6 people. How many pencils does each person get?",
      "7", "First find the total: 12×3＋6＝42 pencils. Then share equally: 42÷6＝7 pencils each.", "(12*3+6)//6"),
]

# ---------- Grade 4, second semester, Unit 2: Viewing three-dimensional objects (II) ----------
BANK["cnm_p113"] = [
    c("basic", "When viewing the same object from the front, side, and top, how might its shape appear?",
      ["The shape may look different", "It must look the same", "Only the front can be seen"], "A",
      "The object may look different when viewed from different directions.", "'The shape may look different'"),
    n("basic", "Three identical small cubes are placed in one horizontal row, one layer high. How many squares are visible from above?",
      "3", "From above, the single row shows 3 squares.", "3"),
    n("standard", "Four identical small cubes are stacked vertically. How many squares are visible from above?",
      "1", "The cubes are stacked, so from above only the top square is visible.", "1"),
    n("challenge", "Place 3 small cubes in a row on the bottom layer, then stack 1 cube on top of the leftmost cube. How many squares are visible from the front?",
      "4", "The left column is 2 layers high and the middle and right columns are each 1 layer high, so 2＋1＋1＝4 squares are visible from the front.", "2+1+1"),
]

# ---------- Grade 4, second semester, Unit 3: Arithmetic properties ----------
BANK["cnm_p114"] = [
    n("basic", "Rewrite 28＋72 as 72＋28. What is the result?",
      "100", "Commutative property of addition: changing the order of the addends does not change the sum. 28＋72＝100.", "28+72"),
    n("basic", "Calculate 36＋64 first, then add 50. What is the result?",
      "150", "Associative property of addition: combine 36 and 64 to make 100, then add 50 to get 150.", "36+64+50"),
    n("standard", "Use the commutative or associative property to make a multiple of ten: what is 17＋83?",
      "100", "17＋83＝100.", "17+83"),
    n("challenge", "Calculate 46＋98＋54. First add the numbers that make 100. What is the result?",
      "198", "46＋54＝100, then add 98 to get 198.", "46+98+54"),
]

BANK["cnm_p115"] = [
    n("basic", "What is the product of 25×4?",
      "100", "25×4＝100.", "25*4"),
    n("basic", "In 5×8×2, calculate 5×2 first. What is the product?",
      "80", "Associative property of multiplication: first calculate 5×2＝10, then 10×8＝80.", "5*8*2"),
    n("standard", "There are 25 people in each row and 4 rows. How many people are there altogether?",
      "100", "25×4＝100 people.", "25*4"),
    n("challenge", "In 25×4×7, calculate 25×4 first. What is the product?",
      "700", "25×4＝100, and 100×7＝700.", "25*4*7"),
]

BANK["cnm_p116"] = [
    n("basic", "Rewrite 25×4＋25×6 as 25×（4＋6）. What is the result?",
      "250", "Distributive property of multiplication: 25×10＝250.", "25*4+25*6"),
    n("basic", "What is 25×（4＋6）?",
      "250", "First calculate 4＋6＝10, then 25×10＝250.", "25*(4+6)"),
    n("standard", "You buy 4 pens and 6 more pens. Each pen costs 8 yuan. What is the total cost?",
      "80", "8×（4＋6）＝8×10＝80 yuan.", "8*(4+6)"),
    n("challenge", "Rewrite 99×15 as （100－1）×15. What is the result?",
      "1485", "100×15－1×15＝1500－15＝1485.", "(100-1)*15"),
]

BANK["cnm_p117"] = [
    n("basic", "Rewrite 99×5 as （100－1）×5. What is the result?",
      "495", "100×5－5＝495.", "99*5"),
    n("basic", "Calculate 36＋64＋50 by adding 36 and 64 to make 100 first. What is the result?",
      "150", "100＋50＝150.", "36+64+50"),
    n("standard", "Rewrite 25×12 as 25×4×3. What is the product?",
      "300", "25×4＝100, and 100×3＝300.", "25*12"),
    n("challenge", "Each book costs 48 yuan. You buy 2 books. Estimate with 50×2, then subtract the extra amount. How much do you actually pay?",
      "96", "50×2＝100, which is 2×2＝4 yuan too much, so the actual cost is 100－4＝96 yuan.", "48*2"),
]

# ---------- Grade 4, second semester, Unit 4: Meaning and properties of decimals ----------
BANK["cnm_p118"] = [
    n("basic", "Divide 1 meter into 10 equal parts. How many meters is 1 part? (Answer as a decimal.)",
      "0.1", "One part is one tenth of a meter, written as 0.1 meter.", "Fraction(1,10)"),
    n("basic", "How many 0.1s are in 0.3?",
      "3", "A one-place decimal counts tenths; there are 3 tenths in 0.3.", "3"),
    n("standard", "Divide 1 meter into 10 equal parts and take 7 parts. How many meters is that, written as a one-place decimal? (Answer as a decimal.)",
      "0.7", "Seven lengths of 0.1 meter make 0.7 meter.", "Fraction(7,10)"),
    n("challenge", "Divide 1 whole into 100 equal parts and take 25 parts. What decimal represents this? (Answer as a decimal.)",
      "0.25", "One part is 0.01, so 25 parts make 0.25. Two-place decimals represent hundredths.", "Fraction(25,100)"),
]

BANK["cnm_p119"] = [
    n("basic", "Which is greater, 3.5 or 2.8? (Answer as a decimal.)",
      "3.5", "Compare the whole-number parts first: 3＞2, so 3.5＞2.8.", "Fraction(35,10)"),
    c("basic", "Which number is greatest?",
      ["0.8", "0.75", "0.9", "0.69"], "C",
      "All have a whole-number part of 0. The tenths digit 9 is greatest, so 0.9 is greatest.", "Fraction(9,10)"),
    n("standard", "One rope is 2.4 meters long and another is 1.9 meters long. How long is the longer rope? (Answer as a decimal.)",
      "2.4", "The whole-number part 2 is greater than 1, so the 2.4-meter rope is longer.", "Fraction(24,10)"),
    n("challenge", "Which is the smallest of 0.7, 0.70, and 0.07? (Answer as a decimal.)",
      "0.07", "0.7 and 0.70 are equal, while the tenths digit of 0.07 is 0, making it smaller.", "Fraction(7,100)"),
]

BANK["cnm_p120"] = [
    n("basic", "What does 1.2 become when the decimal point moves one place to the right?",
      "12", "Moving the decimal point one place to the right makes the number 10 times as large: 1.2×10＝12.",
      "Fraction(12,10)*10"),
    n("basic", "What does 35 become when the decimal point moves one place to the left? (Answer as a decimal.)",
      "3.5", "Moving the decimal point one place to the left makes the number one tenth as large: 35÷10＝3.5.",
      "Fraction(35,10)"),
    n("standard", "What is 0.8 multiplied by 100?",
      "80", "Multiplying by 100 moves the decimal point two places to the right: 0.8×100＝80.",
      "Fraction(8,10)*100"),
    n("challenge", "Move the decimal point in 6.4 two places to the right, then one place to the left. What number do you get?",
      "64", "Moving it two places right gives 640; moving it one place left gives 64. Overall, the number is multiplied by 10.",
      "Fraction(64,10)*100/10"),
]

BANK["cnm_p121"] = [
    n("basic", "Round 3.8 to the nearest whole number. What is the approximate value?",
      "4", "The tenths digit is 8, so round the ones digit up by 1. The approximate value is 4.", "4"),
    n("basic", "Round 6.3 to the nearest whole number. What is the approximate value?",
      "6", "The tenths digit is 3, which is less than 5, so the ones digit stays the same. The approximate value is 6.", "6"),
    n("standard", "Round 2.46 to one decimal place. What is the approximate value? (Answer as a decimal.)",
      "2.5", "The hundredths digit is 6, so round the tenths digit up by 1: 2.46≈2.5.", "Fraction(25,10)"),
    n("challenge", "Round 7.96 to one decimal place. What is the approximate value? (Answer as a decimal.)",
      "8.0", "The hundredths digit is 6. Adding 1 to the tenths digit 9 makes 10, so regroup 1 to the ones place to get 8.0.", "Fraction(8)"),
]

# ---------- Grade 4, second semester, Unit 5: Triangles ----------
BANK["cnm_p122"] = [
    n("basic", "How many acute angles does a right triangle have?",
      "2", "A right triangle has 1 right angle and 2 acute angles.", "2"),
    c("basic", "A triangle has angles of 100 degrees, 40 degrees, and 40 degrees. What type of triangle is it?",
      ["Acute triangle", "Obtuse triangle", "Right triangle"], "B",
      "A triangle with one obtuse angle is an obtuse triangle.", "'Obtuse triangle'"),
    c("standard", "A triangle has three sides that are each 5 centimeters long. What type of triangle is it?",
      ["Right triangle", "Obtuse triangle", "Triangle with three different side lengths", "Equilateral triangle"], "D",
      "A triangle with three equal sides is an equilateral triangle.", "'Equilateral triangle'"),
    n("challenge", "An isosceles triangle has equal sides of 5 centimeters and a base of 3 centimeters. What is its perimeter?",
      "13", "The equal sides of an isosceles triangle have the same length: 5＋5＋3＝13 centimeters.", "5+5+3"),
]

BANK["cnm_p123"] = [
    c("basic", "For a triangle, how should the sum of any two sides compare with the third side?",
      ["Greater than the third side", "Equal to the third side", "Less than the third side"], "A",
      "The sum of any two sides must be greater than the third side to form a triangle.", "'Greater than the third side'"),
    n("basic", "Two sides are 3 centimeters and 4 centimeters long. What must the third side be less than to form a triangle?",
      "7", "The third side must be less than 3＋4＝7 centimeters, and greater than 4－3＝1 centimeter.", "3+4"),
    c("standard", "Which of these four sets of line segments can form a triangle?",
      ["2 cm, 3 cm, 6 cm", "3 cm, 4 cm, 5 cm", "1 cm, 2 cm, 3 cm", "4 cm, 4 cm, 9 cm"], "B",
      "3＋4＞5, 3＋5＞4, and 4＋5＞3, so these segments can form a triangle. In each other set, the sum of two sides is no greater than the third side.",
      "'3 cm, 4 cm, 5 cm'"),
    n("challenge", "Two sides are 6 centimeters and 8 centimeters long. What is the greatest whole-number length the third side can have?",
      "13", "The third side must be less than 6＋8＝14 and greater than 8－6＝2, so the greatest whole-number length is 13.", "6+8-1"),
]

BANK["cnm_p124"] = [
    c("basic", "What is the sum of the interior angles of a triangle?",
      ["180 degrees", "90 degrees", "360 degrees"], "A",
      "The three interior angles of a triangle add up to 180 degrees.", "'180 degrees'"),
    n("basic", "Two interior angles of a triangle are 60 degrees and 40 degrees. What is the third interior angle?",
      "80", "180－60－40＝80 degrees.", "180-60-40"),
    n("standard", "One acute angle in a right triangle is 35 degrees. How many degrees is the other acute angle?",
      "55", "The two acute angles in a right triangle are complementary: 90－35＝55 degrees.", "90-35"),
    n("challenge", "How many degrees is an acute angle in an isosceles right triangle?",
      "45", "The right angle is 90 degrees, and the two acute angles are equal. Each is (180－90)÷2＝45 degrees.", "(180-90)//2"),
]

# ---------- Grade 4, second semester, Unit 6: Adding and subtracting decimals ----------
BANK["cnm_p125"] = [
    n("basic", "What is 1.25＋0.4? (Answer as a decimal.)",
      "1.65", "Align the decimal points: 1.25＋0.40＝1.65.", "Fraction(125,100)+Fraction(4,10)"),
    n("basic", "What is 3.6－1.8? (Answer as a decimal.)",
      "1.8", "Align the decimal points: 3.6－1.8＝1.8.", "Fraction(36,10)-Fraction(18,10)"),
    n("standard", "A notebook costs 3.5 yuan and an eraser costs 0.8 yuan. What is the total cost? (Answer as a decimal.)",
      "4.3", "3.5＋0.8＝4.3 yuan.", "Fraction(35,10)+Fraction(8,10)"),
    n("challenge", "You pay 5 yuan for a 1.25-yuan pen and a 0.8-yuan eraser. How much change should you get? (Answer as a decimal.)",
      "2.95", "First find the cost: 1.25＋0.8＝2.05 yuan. Then calculate 5－2.05＝2.95 yuan in change.",
      "5-(Fraction(125,100)+Fraction(8,10))"),
]

BANK["cnm_p126"] = [
    n("basic", "Mom has 10 yuan and buys a notebook for 3.6 yuan. How much money is left? (Answer as a decimal.)",
      "6.4", "10－3.6＝6.4 yuan.", "10-Fraction(36,10)"),
    n("basic", "A rope is 2.5 meters long, and another 1.5 meters is joined to it. How long is it now?",
      "4", "2.5＋1.5＝4 meters.", "Fraction(25,10)+Fraction(15,10)"),
    n("standard", "Ming is 1.35 meters tall. Hua is 0.08 meters taller. How tall is Hua? (Answer as a decimal.)",
      "1.43", "1.35＋0.08＝1.43 meters.", "Fraction(135,100)+Fraction(8,100)"),
    n("challenge", "A bottle contains 5 liters of oil. First, 1.6 liters are poured out, then another 0.8 liters. How many liters remain? (Answer as a decimal.)",
      "2.6", "A total of 1.6＋0.8＝2.4 liters is poured out, leaving 5－2.4＝2.6 liters.",
      "5-(Fraction(16,10)+Fraction(8,10))"),
]

# ---------- Grade 4, second semester, Unit 7: Transformations of shapes (II) ----------
BANK["cnm_p127"] = [
    c("basic", "What feature does a line-symmetric shape have?",
      ["A line of symmetry", "It must have a right angle", "It must be a circle"], "A",
      "When folded along its line of symmetry, the two halves of a line-symmetric shape overlap exactly.", "'A line of symmetry'"),
    n("basic", "A rectangle whose length and width are different is line-symmetric. How many lines of symmetry does it have?",
      "2", "A rectangle has 2 lines of symmetry, through the midpoints of its length and width.", "2"),
    c("standard", "Which of these shapes has line symmetry?",
      ["A parallelogram that is neither a rectangle nor a rhombus", "A trapezoid with unequal legs", "An isosceles triangle", "A triangle with three different side lengths"], "C",
      "An isosceles triangle can be folded along the altitude from the base to make the two halves overlap, so it has line symmetry.", "'An isosceles triangle'"),
    n("challenge", "How many lines of symmetry does a square have?",
      "4", "A square can be folded horizontally, vertically, and along both diagonals, giving 4 lines of symmetry.", "4"),
]

BANK["cnm_p128"] = [
    c("basic", "What happens to a shape's size and shape after a translation?",
      ["Its size and shape stay the same", "It becomes larger", "Its shape must change"], "A",
      "A translation changes only the position, not the size or shape.", "'Its size and shape stay the same'"),
    n("basic", "A rectangle is 4 centimeters long and 3 centimeters wide. It is translated 5 grid spaces to the right. How long is it after the translation?",
      "4", "A translation does not change size, so the length is still 4 centimeters.", "4"),
    n("standard", "A point is on the 2nd grid square and is translated 5 squares to the right. Which square does it reach?",
      "7", "Moving right increases the column number: 2＋5＝7.", "2+5"),
    n("challenge", "A point on grid paper is in column 8, row 3. It is translated 3 squares left, then 2 squares up. Which column is it in now?",
      "5", "Moving up does not change the column. The column is 8－3＝5.", "8-3"),
]

# ---------- Grade 4, second semester, Unit 8: Averages and bar graphs ----------
BANK["cnm_p129"] = [
    c("basic", "What does the average represent?",
      ["The typical level of a group of numbers", "The largest number in the group", "The number of values in the group"], "A",
      "The average balances the values and represents the typical level of the group.", "'The typical level of a group of numbers'"),
    n("basic", "What is the average of 4, 6, and 8?",
      "6", "Add the values, then divide by the number of values: (4＋6＋8)÷3＝6.", "Fraction(4+6+8,3)"),
    n("standard", "Three test scores are 80, 90, and 100. What is their average?",
      "90", "(80＋90＋100)÷3＝90.", "Fraction(80+90+100,3)"),
    n("challenge", "The average of four numbers is 8. Three of the numbers are 6, 9, and 7. What is the fourth number?",
      "10", "The total of the four numbers is 8×4＝32, so the fourth number is 32－6－9－7＝10.", "8*4-6-9-7"),
]

# ---------- Grade 4, second semester, Unit 9: Division by two-digit numbers ----------
BANK["cnm_p106"] = [
    n("basic", "What is the quotient of 96÷12?",
      "8", "12×8＝96, so 96÷12＝8.", "96//12"),
    n("basic", "What is the quotient of 150÷25?",
      "6", "25×6＝150, so 150÷25＝6.", "150//25"),
    n("standard", "There are 288 notebooks, bundled 16 to a bundle. How many bundles can be made?",
      "18", "288÷16＝18 bundles.", "288//16"),
    n("challenge", "Notebooks are bundled 16 to a bundle. Ten bundles have been made, and 128 notebooks remain. How many notebooks were there originally?",
      "288", "The 10 bundles contain 16×10＝160 notebooks. Add the remaining 128 to get 288 notebooks altogether.", "16*10+128"),
]

BANK["cnm_p107"] = [
    n("basic", "What is the quotient of 80÷20?",
      "4", "80÷20＝4.", "80//20"),
    n("basic", "Given that 15÷5＝3, what is the quotient of 150÷50 by the invariant quotient property?",
      "3", "Multiplying both the dividend and divisor by 10 does not change the quotient, so it remains 3.", "15//5"),
    n("standard", "For 600÷30, remove one zero from both numbers and calculate 60÷3 first. What is the quotient?",
      "20", "Dividing both the dividend and divisor by 10 does not change the quotient: 60÷3＝20.", "600//30"),
    n("challenge", "Multiply both the dividend and divisor in 12÷4 by 5. What is the quotient of the new expression?",
      "3", "Multiplying both by the same nonzero number does not change the quotient, so 12÷4＝3.", "12//4"),
]


def load(name):
    with open(os.path.join(DATA, name), encoding="utf-8") as f:
        import json
        return json.load(f)


def dump(name, obj, indent=2):
    import json
    path = os.path.join(DATA, name)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=indent)
        f.write("\n")


def prompt_problem(q):
    p = str(q.get("prompt") or "").strip()
    if V.PURE_ARITH_PROMPT_RE.match(p) or V.PURE_ARITH_CHOICE_RE.match(p):
        return "Pure integer or decimal calculation"
    if "Which is the result?" in p:
        return "Which is the result?"
    if "? Calculate:" in p or ". Calculate:" in p:
        return "The prompt already contains an expression"
    if q.get("difficulty") == "challenge" and V.CHALLENGE_BARE_CALC_RE.match(p):
        return "Challenge: direct calculation"
    return None


def check_bank(new_qs):
    extra = []
    for q in new_qs:
        why = prompt_problem(q)
        if why:
            extra.append("%s %s: %s" % (q["id"], why, q["prompt"][:40]))
        if "verify" not in q:
            extra.append("%s is missing verify" % q["id"])
            continue
        try:
            res = VQ.safe_eval(q["verify"])
        except Exception as ex:  # noqa: BLE001
            extra.append("%s verify failed: %s" % (q["id"], ex))
            continue
        if q["type"] == "numeric":
            ok, detail = VQ.compare_numeric(q, res)
        else:
            ok, detail = VQ.compare_choice(q, res)
        if not ok:
            extra.append("%s %s" % (q["id"], detail))
    return extra


def main():
    topics = load("topics.json")
    questions = load("questions.json")
    by_id = {t["id"]: t for t in topics}
    missing = [tid for tid in BANK if tid not in by_id]
    if missing:
        raise SystemExit("Unknown topics: " + ", ".join(missing))
    g4 = [t for t in topics if t.get("grade") == 4 and str(t.get("id", "")).startswith("cnm_")
          and not t.get("external")]
    not_in_bank = [t["id"] for t in g4 if t["id"] not in BANK]
    if not_in_bank:
        raise SystemExit("Grade 4 topics without questions: " + ", ".join(not_in_bank))
    extra_topics = [tid for tid in BANK if by_id[tid].get("grade") != 4]
    if extra_topics:
        raise SystemExit("Non-Grade-4 topics were added: " + ", ".join(extra_topics))

    old_prompts = defaultdict(list)
    for q in questions:
        if q.get("topicId") in BANK:
            old_prompts[q["topicId"]].append(q.get("prompt"))

    new_qs = []
    extra = []
    changed = 0
    for tid, raw in BANK.items():
        ds = [q["difficulty"] for q in raw]
        if ds.count("basic") != 2 or ds.count("standard") != 1 or ds.count("challenge") != 1:
            extra.append("%s does not have 2 basic + 1 standard + 1 challenge questions: %s" % (tid, ds))
        if raw[0]["difficulty"] != "basic" or raw[1]["difficulty"] != "basic":
            extra.append("%s should have basic questions first" % tid)
        if len(raw) != 4:
            extra.append("%s does not have 4 questions" % tid)
        oldps = old_prompts.get(tid, [])
        for i, q in enumerate(raw, 1):
            item = dict(q)
            item["id"] = "%s_q%d" % (tid, i)
            item["topicId"] = tid
            if i - 1 >= len(oldps) or oldps[i - 1] != item["prompt"]:
                changed += 1
            new_qs.append(item)
        t = by_id[tid]
        q1 = raw[0]
        if q1["type"] == "choice":
            dq_ans = [x["text"] for x in q1["choices"] if x["key"] == q1["answer"]][0]
        else:
            dq_ans = str(q1["answer"])
        t["diagnostic_question"] = {"question": q1["prompt"], "answer": dq_ans}

    extra.extend(check_bank(new_qs))
    if extra:
        raise SystemExit("Question-bank self-check failed:\n" + "\n".join(extra))

    old_ids = set(BANK)
    out = []
    seen = set()
    i = 0
    while i < len(questions):
        tid = questions[i].get("topicId")
        if tid in old_ids and tid not in seen:
            j = i
            while j < len(questions) and questions[j].get("topicId") == tid:
                j += 1
            out.extend(q for q in new_qs if q["topicId"] == tid)
            seen.add(tid)
            i = j
        else:
            out.append(questions[i])
            i += 1
    leftover = old_ids - seen
    if leftover:
        raise SystemExit("No existing questions for these topics were found in questions.json: " + ", ".join(sorted(leftover)))
    if len(out) != len(questions):
        raise SystemExit("Question count changed: %d → %d" % (len(questions), len(out)))
    ids = [q["id"] for q in out]
    if len(ids) != len(set(ids)):
        raise SystemExit("Duplicate IDs after replacement")

    dump("questions.json", out, 2)
    dump("topics.json", topics, 2)
    g4_qs = [q for q in out if q["topicId"] in old_ids]
    dump("_qbatches/primary_g4.json", g4_qs, 1)

    sem = Counter(by_id[tid]["semester"] for tid in BANK)
    # "上" and "下" are parser-required semester tokens in the topic data.
    print("Grade 4 topics: %d (semester 1: %d, semester 2: %d), questions: %d" % (len(BANK), sem["上"], sem["下"], len(g4_qs)))
    print("Difficulty", Counter(q["difficulty"] for q in g4_qs))
    print("Question type", Counter(q["type"] for q in g4_qs))
    print("Prompts revised: %d / %d" % (changed, len(g4_qs)))


if __name__ == "__main__":
    main()
