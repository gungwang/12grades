#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Align Grade 6 question-bank difficulty; update data/questions.json and topics.json, and write _qbatches/primary_g6.json."""
import json
import os
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")


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
    if verify is not None:
        q["verify"] = verify
    return q


BANK = {}

# ---------- Grade 6, first semester, Unit 1: Coordinate Locations ----------
BANK["cnm_p136"] = [
    c("basic", "When writing an ordered pair, which coordinate comes first?",
      ["Column first, then row", "Row first, then column", "Only one number"], "A",
      "(3, 2) represents column 3, row 2.", "'Column first, then row'"),
    n("basic", "Point A is at (6, 2). In which column is point A?",
      "6", "In an ordered pair, the column comes first, so (6, 2) is column 6, row 2.", "6"),
    c("standard", "On a grid, (4, 2) represents the point in column 4, row 2. Which ordered pair represents the point in column 2, row 5?",
      ["(5, 2)", "(2, 7)", "(2, 5)", "(5, 7)"], "C",
      "The column comes first, so column 2, row 5 is written as (2, 5).", "'(2, 5)'"),
    n("challenge", "Point A is at (2, 3). Move 4 columns right and then 1 row up to reach point B. What is the column number of point B?",
      "6", "Moving right increases the column number: 2＋4＝6. Point B is at (6, 4).", "2+4"),
]

BANK["cnm_p180"] = [
    c("basic", "For “30 degrees east of north,” which direction do you start from, and which way do you turn?",
      ["Start due north and turn 30 degrees east", "Start due east and turn 30 degrees north", "Start due south and turn 30 degrees east"], "A",
      "For 30 degrees east of north, face north first, then turn 30 degrees east."),
    n("basic", "The post office is 150 m from the school, 30 degrees east of north. How many degrees east of north is this direction?",
      "30", "The direction is 30 degrees east of north, so the angle is 30 degrees.", "30"),
    c("standard", "The school is 150 m due east of Xiaoming's home, and the park is 250 m due east of the school. In what direction and how far is the park from Xiaoming's home?",
      ["400 m due east", "400 m due west", "100 m due east", "400 m due north"], "A",
      "Both legs go due east, so add the distances: 150＋250＝400 m."),
    c("challenge", "The youth center is 300 m from the school, 40 degrees east of north. In what direction is the school from the youth center?",
      ["40 degrees west of south", "40 degrees west of north", "40 degrees east of south", "Due south"], "A",
      "The reverse direction of 40 degrees east of north is 40 degrees west of south; the angle remains 40 degrees."),
]

BANK["cnm_p181"] = [
    c("basic", "Walk east from home to school, then north to the library. In which direction does the second leg go?",
      ["North", "East", "South", "West"], "A",
      "The second leg is the walk north, so its direction is north."),
    n("basic", "Xiaohua walks 90 m east from home to school, then 60 m north to the library. How far does she walk in total?",
      "150", "Add the lengths of the two legs: 90＋60＝150 m.", "90+60"),
    n("standard", "Xiaoming walks 120 m east, then 80 m south, then 120 m west. How far south of the starting point is he now?",
      "80", "The 120 m east and 120 m west cancel out, leaving 80 m south.", "80"),
    c("challenge", "Xiaohua walks 90 m east from home to school, then 60 m north to the library. If she returns home along the same route, how should she travel first?",
      ["Walk 90 m east", "Walk 60 m south", "Walk 60 m north", "Walk 90 m west"], "B",
      "To retrace the route, first reverse the last leg: the 60 m north becomes 60 m south."),
]

# ---------- Grade 6, first semester, Unit 2: Fraction Multiplication ----------
BANK["cnm_p177"] = [
    n("basic", "Calculate: 2/7×3＝?", "6/7", "2/7×3＝6/7.", "2/7*3"),
    n("basic", "Calculate: 3/4×2＝?", "3/2", "3/4×2＝6/4＝3/2.", "3/4*2"),
    n("standard", "Each bottle holds 3/5 L of juice. How many liters are in 4 bottles?", "12/5",
      "To find 4 groups of 3/5 L, multiply: 3/5×4＝12/5.", "3/5*4"),
    n("challenge", "A bag of rice weighs 4/5 kg. How much do 5 bags weigh altogether? Simplify when possible.", "4",
      "4/5×5＝4.", "4/5*5"),
]

BANK["cnm_p178"] = [
    n("basic", "Calculate: 1/2×1/3＝?", "1/6", "1/2×1/3＝1/6.", "1/2*1/3"),
    n("basic", "Calculate: 2/3×3/4＝?", "1/2", "2/3×3/4＝1/2.", "2/3*3/4"),
    n("standard", "Half of a road has been repaired, and 2/3 of that work was done in the morning. What fraction of the whole road was repaired in the morning?", "1/3",
      "To find 2/3 of 1/2, multiply: 1/2×2/3＝1/3.", "1/2*2/3"),
    n("challenge", "A barrel is 3/4 full of oil. If 2/5 of the oil is poured out, what fraction of the barrel's full capacity was poured out?", "3/10",
      "Find 2/5 of 3/4: 3/4×2/5＝3/10.", "3/4*2/5"),
]

BANK["cnm_p179"] = [
    n("basic", "Calculate: 20×1/4＝?", "5", "20×1/4＝5.", "20*1/4"),
    n("basic", "A barrel contains 30 L of oil. If 2/5 is used, how many liters are used?", "12",
      "Find 2/5 of 30: 30×2/5＝12.", "30*2/5"),
    n("standard", "A book has 240 pages, and 3/8 have been read. How many pages have been read?", "90",
      "240×3/8＝90.", "240*3/8"),
    n("challenge", "An orchard has 120 trees. Of these, 3/5 are apple trees, and 1/4 of the apple trees are Red Fuji. How many Red Fuji trees are there?", "18",
      "120×3/5×1/4＝18.", "120*3/5*1/4"),
]

BANK["cnm_p247"] = [
    n("basic", "Calculate: 0.5×2/5＝?", "1/5", "0.5＝1/2, and 1/2×2/5＝1/5.", "Fraction(1,2)*2/5"),
    n("basic", "Calculate: 3/4×0.8＝?", "3/5", "0.8＝4/5, and 3/4×4/5＝3/5.", "3/4*Fraction(4,5)"),
    n("standard", "Use the properties of operations to calculate: 2/7×0.5×7＝?", "1",
      "2/7×7×0.5＝2×0.5＝1.", "2/7*Fraction(1,2)*7"),
    n("challenge", "Use the distributive property of multiplication to calculate 1/4×0.4＋3/4×0.4. What is the result? (Give your answer as a decimal.)", "0.4",
      "Factor out 0.4: (1/4＋3/4)×0.4＝1×0.4＝0.4.", "(1/4+3/4)*Fraction(2,5)"),
]

# ---------- Grade 6, first semester, Unit 3: Fraction Division ----------
BANK["cnm_p246"] = [
    n("basic", "What is the reciprocal of 3/4?", "4/3", "Flip the numerator and denominator: the reciprocal of 3/4 is 4/3.", "4/3"),
    n("basic", "What is the reciprocal of 5?", "1/5", "The reciprocal of an integer a is 1/a, so the reciprocal of 5 is 1/5.", "1/5"),
    c("standard", "Which pair of numbers are reciprocals?",
      ["2/5 and 5/2", "2/5 and 2/5", "2/5 and 5", "2/5 and 2"], "A",
      "2/5×5/2＝1, so the numbers are reciprocals."),
    n("challenge", "The product of a number and 2/5 is 1. What is the number?", "5/2",
      "The reciprocal of 2/5 is 5/2.", "5/2"),
]

BANK["cnm_p182"] = [
    n("basic", "Calculate: 4/5÷2＝?", "2/5", "4/5÷2＝4/5×1/2＝2/5.", "4/5/2"),
    n("basic", "Calculate: 6/7÷3＝?", "2/7", "6/7÷3＝6/7×1/3＝2/7.", "6/7/3"),
    n("standard", "A 3/4 m rope is cut into 3 equal pieces. How long is each piece?", "1/4",
      "3/4÷3＝1/4.", "3/4/3"),
    n("challenge", "5/6 of a cake is shared equally among 4 people. What fraction of the whole cake does each person get?", "5/24",
      "5/6÷4＝5/6×1/4＝5/24.", "5/6/4"),
]

BANK["cnm_p183"] = [
    n("basic", "Calculate: (3/4)÷(1/2)＝?", "3/2", "3/4×2/1＝3/2.", "(3/4)/(1/2)"),
    n("basic", "Calculate: (2/3)÷(4/5)＝?", "5/6", "2/3×5/4＝5/6.", "(2/3)/(4/5)"),
    n("standard", "Divide 6/7 of a sheet of paper into pieces that are each 2/7 of a sheet. How many pieces are there?", "3",
      "6/7÷2/7＝6/7×7/2＝3.", "(6/7)/(2/7)"),
    n("challenge", "A rope is 3/4 m long. If it is cut into pieces that are each 1/8 m long, how many pieces can be made?", "6",
      "3/4÷1/8＝3/4×8＝6.", "(3/4)/(1/8)"),
]

BANK["cnm_p184"] = [
    n("basic", "3/4 of a number is 12. What is the number?", "16",
      "To find the whole when a fraction of it is known, divide: 12÷3/4＝16.", "12/(3/4)"),
    n("basic", "Calculate: 6÷(2/5)＝?", "15", "6×5/2＝15.", "6/(2/5)"),
    n("standard", "A road has been repaired to 2/5 of its total length, which is 8 km. What is the road's total length in kilometers?", "20",
      "8÷2/5＝20.", "8/(2/5)"),
    n("challenge", "After 3/5 of the oil in a barrel is used, 8 L remain. How many liters were in the barrel originally?", "20",
      "The remaining fraction is 1－3/5＝2/5, which is 8 L. The original amount was 8÷2/5＝20 L.", "8/(2/5)"),
]

# ---------- Grade 6, first semester: Negative Numbers in Everyday Life ----------
BANK["cnm_p201"] = [
    c("basic", "What do negative numbers represent?",
      ["A quantity opposite in meaning to a positive quantity", "A number greater than 100", "Only temperature, and nothing else"], "A",
      "Income can be represented by positive numbers, and expenses by negative numbers."),
    c("basic", "What kind of number represents a temperature below zero?",
      ["A negative number", "Only 0", "A number greater than 10"], "A",
      "A temperature 3 degrees below zero is written as -3."),
    n("standard", "The temperature drops from 3 degrees above zero to 2 degrees below zero. By how many degrees did it drop?", "5",
      "From +3 to -2, the drop is 3＋2＝5 degrees.", "3+2"),
    n("challenge", "One day, the high temperature is 5°C and the low is -3°C. What is the temperature range in degrees Celsius?", "8",
      "The temperature range is the high minus the low: 5－(－3)＝8.", "5-(-3)"),
]

BANK["cnm_p202"] = [
    n("basic", "Xiaoming records income of 8 yuan as +8 yuan and an expense of 5 yuan as -5 yuan. If he earns 8 yuan and then spends 5 yuan, how much does he have left?",
      "3", "+8＋(－5)＝3.", "8-5"),
    n("basic", "A diver uses the water surface as 0 m and records a descent of 6 m as -6 m. After diving down 6 m and then another 3 m, how far below the surface is the diver?",
      "9", "The two descents total 6＋3＝9 m.", "6+3"),
    n("standard", "An elevator rises 12 floors from its starting point and then descends 5 floors. How many floors above the starting point is it now?", "7",
      "12－5＝7.", "12-5"),
    n("challenge", "Elevation: Sea level is 0 m, and a mountaintop 1200 m above sea level is recorded as +1200 m. How should a basin 80 m below sea level be recorded? (Include the sign.)",
      "-80", "A location below sea level is represented by a negative number: -80 m.", "-80"),
]

# ---------- Grade 6, first semester, Unit 4: Circles ----------
BANK["cnm_p188"] = [
    c("basic", "What is true about the distance from any point on a circle to its center?",
      ["Every distance equals the radius", "The distances vary", "Each distance is twice the diameter"], "A",
      "All radii in the same circle have equal lengths."),
    n("basic", "In a circle, the radius is 4 cm. What is the diameter in centimeters?", "8",
      "Diameter＝radius×2＝8.", "4*2"),
    n("standard", "A circle has a diameter of 10 cm. What is its radius in centimeters?", "5",
      "Radius＝diameter÷2＝5.", "10/2"),
    n("challenge", "When a compass is used to draw a circle, the distance between its points is 5 cm. What is the circle's diameter in centimeters?", "10",
      "The distance between the compass points is the radius, so diameter＝5×2＝10.", "5*2"),
]

BANK["cnm_p189"] = [
    c("basic", "What is the approximate value of pi?", ["3.14", "3.41", "31.4"], "A",
      "Circumference÷diameter≈3.14. Use 314/100 for pi in these calculations."),
    c("basic", "Pi is the ratio of a circle's circumference to which measurement?",
      ["Diameter", "Radius", "Area"], "A",
      "Pi＝circumference÷diameter."),
    n("standard", "What is the approximate circumference of a circle with a 2 cm diameter? Use 314/100 for pi. (Give your answer as a decimal.)", "6.28",
      "Circumference＝diameter×pi＝2×3.14＝6.28.", "2*314/100"),
    n("challenge", "A circle has a diameter of 10 cm and an approximate circumference of 31.4 cm. About how many times the diameter is the circumference? (Give your answer as a decimal.)", "3.14",
      "31.4÷10＝3.14; this ratio is pi.", "314/100"),
]

BANK["cnm_p190"] = [
    n("basic", "What is the circumference, in centimeters, of a circle with a 2 cm radius? Use 314/100 for pi. (Give your answer as a decimal.)", "12.56",
      "Circumference＝2×3.14×2＝12.56.", "2*314/100*2"),
    n("basic", "What is the circumference, in centimeters, of a circle with a 5 cm radius? Use 314/100 for pi. (Give your answer as a decimal.)", "31.4",
      "Circumference＝2×3.14×5＝31.4.", "2*314/100*5"),
    n("standard", "A circle has a diameter of 4 cm. What is its circumference in centimeters? Use 314/100 for pi. (Give your answer as a decimal.)", "12.56",
      "Circumference＝3.14×diameter＝3.14×4＝12.56.", "314/100*4"),
    n("challenge", "A circular flower bed has a radius of 10 m. About how many meters of fencing are needed to go around it once? Use 314/100 for pi. (Give your answer as a decimal.)", "62.8",
      "The length of the fence equals the circumference: 2×3.14×10＝62.8.", "2*314/100*10"),
]

BANK["cnm_p191"] = [
    n("basic", "A bicycle wheel has a diameter of 50 cm. About how far does it travel in one rotation? Use 314/100 for pi.", "157",
      "The distance traveled is the circumference: 3.14×50＝157.", "314/100*50"),
    n("basic", "A circular track has a radius of 20 m. About how many meters is one lap? Use 314/100 for pi. (Give your answer as a decimal.)", "125.6",
      "2×3.14×20＝125.6.", "2*314/100*20"),
    n("standard", "A circular flower bed has a diameter of 20 m. About how many meters of fencing are needed to go around its edge once? Use 314/100 for pi. (Give your answer as a decimal.)", "62.8",
      "3.14×20＝62.8.", "314/100*20"),
    n("challenge", "The minute hand of a clock is 5 cm long. About how far does its tip travel in one full turn? Use 314/100 for pi. (Give your answer as a decimal.)", "31.4",
      "The tip travels along a circle with a 5 cm radius: 2×3.14×5＝31.4.", "2*314/100*5"),
]

BANK["cnm_p192"] = [
    n("basic", "What is the area, in square centimeters, of a circle with a 2 cm radius? Use 314/100 for pi. (Give your answer as a decimal.)", "12.56",
      "Area＝3.14×2×2＝12.56.", "314/100*2*2"),
    n("basic", "What is the area, in square centimeters, of a circle with a 10 cm radius? Use 314/100 for pi.", "314",
      "Area＝3.14×10×10＝314.", "314/100*10*10"),
    n("standard", "What is the area, in square centimeters, of a circle with a 5 cm radius? Use 314/100 for pi. (Give your answer as a decimal.)", "78.5",
      "3.14×5×5＝78.5.", "314/100*5*5"),
    n("challenge", "A circle has a diameter of 8 cm. What is its area in square centimeters? Use 314/100 for pi. (Give your answer as a decimal.)", "50.24",
      "Radius＝4 cm; area＝3.14×4×4＝50.24.", "314/100*4*4"),
]

BANK["cnm_p193"] = [
    c("basic", "Which parts form a sector?",
      ["One radius and one diameter", "Two radii and an arc", "Two diameters and an arc", "Two arcs"], "B",
      "A sector is bounded by the two radii that form a central angle and the arc subtended by that angle."),
    n("basic", "A sector has a central angle of 90 degrees. What fraction of the whole circle does it represent?", "1/4",
      "90÷360＝1/4.", "90/360"),
    n("standard", "A sector has a central angle of 180 degrees. What fraction of the whole circle does it represent?", "1/2",
      "180÷360＝1/2.", "180/360"),
    n("challenge", "A sector has a central angle of 120 degrees. What fraction of the whole circle's area does it represent?", "1/3",
      "120÷360＝1/3.", "120/360"),
]

# ---------- Grade 6, first semester: Integrated Practice ----------
BANK["cnm_p241"] = [
    n("basic", "Xiaoming's long-jump results are 3.2 m, 3.5 m, and 3.4 m. His best result counts. What is his best result in meters? (Give your answer as a decimal.)",
      "3.5", "The greatest of the three results is 3.5 m.", "3.5"),
    n("basic", "A basketball player makes 15 out of 20 shots. What fraction of the shots are made?", "3/4",
      "15/20＝3/4.", "15/20"),
    n("standard", "Eight teams play a round-robin tournament, with each pair of teams playing once. How many games are played in total?", "28",
      "Number of games＝8×7÷2＝28.", "8*7/2"),
    n("challenge", "Ten teams play a round-robin tournament, with each pair playing once. If 27 games have been played, how many remain?", "18",
      "There are 10×9÷2＝45 games in total, so 45－27＝18 remain.", "10*9/2-27"),
]

BANK["cnm_p242"] = [
    n("basic", "A faucet leaks 2 L of water each day. How many liters does it leak in 30 days?", "60",
      "2×30＝60.", "2*30"),
    n("basic", "A bucket holds 18 L of water. If 1/3 is used, how many liters are used?", "6",
      "18×1/3＝6.", "18*1/3"),
    n("standard", "A household uses 15 metric tons of water per month. How many tons will it use after reducing consumption by 20%?", "12",
      "15×(1－20%)＝15×0.8＝12.", "15*(1-20/100)"),
    n("challenge", "A school has 800 students, and each saves 0.5 L of water per day. How many liters are saved in 30 days? (Give your answer as a decimal.)", "12000",
      "800×0.5×30＝12000.", "800*Fraction(1,2)*30"),
]

# ---------- Grade 6, first semester, Unit 5: Percentages ----------
BANK["cnm_p194"] = [
    c("basic", "What does a percentage represent?",
      ["The percentage that one quantity is of another", "It must be an amount of money", "It can only represent an increase"], "A",
      "50% means fifty percent."),
    n("basic", "What is 50% of 100?", "50", "100×50÷100＝50.", "100*50/100"),
    n("standard", "Class 6-1 has 40 students, 30 of whom are Young Pioneers. What percentage of the class are Young Pioneers? (Give only the number before the percent sign.)",
      "75", "30÷40＝0.75＝75%.", "30/40*100"),
    n("challenge", "A rope has 40% used. What percentage remains? (Give only the number before the percent sign.)", "60",
      "The whole is 100%, so 100－40＝60 remains.", "100-40"),
]

BANK["cnm_p195"] = [
    n("basic", "Convert 35% to a decimal. What is the result? (Give your answer as a decimal.)", "0.35",
      "35%＝35÷100＝0.35.", "35/100"),
    n("basic", "Convert 0.4 to a percentage. What number goes before the percent sign?", "40",
      "0.4＝40%.", "0.4*100"),
    n("standard", "Convert 3/4 to a percentage. What number goes before the percent sign?", "75",
      "3÷4＝0.75＝75%.", "3/4*100"),
    c("challenge", "Order 3/5, 0.55, and 58% from least to greatest. Which order is correct?",
      ["0.55, 58%, 3/5", "58%, 0.55, 3/5", "3/5, 0.55, 58%", "0.55, 3/5, 58%"], "A",
      "3/5＝0.6＝60%, 0.55＝55%, and 58%＝0.58. From least to greatest: 0.55, 58%, 3/5."),
]

BANK["cnm_p196"] = [
    n("basic", "What is 25% of 80?", "20", "80×25÷100＝20.", "80*25/100"),
    n("basic", "What is 10% of 200?", "20", "200×10÷100＝20.", "200*10/100"),
    n("standard", "A class has 40 students, and 45% are girls. How many girls are there?", "18",
      "40×45÷100＝18.", "40*45/100"),
    n("challenge", "A book has 240 pages, and 35% have been read. How many pages remain?", "156",
      "240×35%＝84 pages have been read, so 240－84＝156 pages remain.", "240*(1-35/100)"),
]

BANK["cnm_p197"] = [
    n("basic", "Out of 40 people, 10 meet the standard. What is the success rate as a percentage? (Give only the number before the percent sign.)", "25",
      "10÷40×100＝25.", "10/40*100"),
    n("basic", "A batch contains 50 parts, of which 45 pass inspection. What is the pass rate as a percentage? (Give only the number before the percent sign.)", "90",
      "45÷50×100＝90.", "45/50*100"),
    n("standard", "A shooter takes 25 shots and hits the target 20 times. What is the hit rate as a percentage? (Give only the number before the percent sign.)", "80",
      "20÷25×100＝80.", "20/25*100"),
    n("challenge", "Last year's output was 80 metric tons, and this year's is 100 metric tons. By what percentage did output increase? (Give only the number before the percent sign.)", "25",
      "The increase is 20 metric tons: 20÷80×100＝25.", "(100-80)/80*100"),
]

BANK["cnm_p198"] = [
    n("basic", "40% of a number is 20. What is the number?", "50",
      "20÷40%＝20÷0.4＝50.", "20/(40/100)"),
    n("basic", "30 is 50% of a number. What is the number?", "60",
      "30÷50%＝60.", "30/(50/100)"),
    n("standard", "A reader has finished 25% of a book, which is 40 pages. How many pages are in the whole book?", "160",
      "40÷25%＝160.", "40/(25/100)"),
    n("challenge", "An item sells for 48 yuan at 80% of its original price. What was its original price?", "60",
      "The sale price is 80% of the original price, so 48÷80%＝60.", "48/(80/100)"),
]

BANK["cnm_p203"] = [
    c("basic", "What does a sale price of 80% of the original price mean?",
      ["80% of the original price", "Add 80 yuan to the original price", "8% of the original price"], "A",
      "A sale price of 80% means the item is sold for 80% of its original price."),
    n("basic", "An item originally costs 50 yuan. What is its price after a 20% discount?", "40",
      "50×80%＝40.", "50*80/100"),
    n("standard", "An item originally costs 80 yuan. What is its price after a 10% discount?", "72",
      "80×90%＝72.", "80*90/100"),
    n("challenge", "A backpack originally costs 200 yuan. It is discounted to 80% of its original price, then reduced by another 20 yuan. What is the final price?", "140",
      "200×80%＝160, then subtract 20 to get 140.", "200*80/100-20"),
]

BANK["cnm_p204"] = [
    n("basic", "If 200 yuan is deposited for one year at an annual interest rate of 3%, how much interest is earned?", "6",
      "Interest＝principal×rate＝200×3%＝6.", "200*3/100"),
    n("basic", "If 500 yuan is deposited for one year at an annual interest rate of 2%, how much interest is earned?", "10",
      "500×2%＝10.", "500*2/100"),
    n("standard", "If 1000 yuan is deposited for one year at an annual interest rate of 4%, what is the total amount of principal and interest at the end of the year?", "1040",
      "The interest is 40 yuan, so the total is 1040 yuan.", "1000+1000*4/100"),
    n("challenge", "A deposit of 2000 yuan earns simple interest at an annual rate of 2.5% for 2 years. How much interest is earned in total?", "100",
      "2000×2.5%×2＝100.", "2000*25/1000*2"),
]

BANK["cnm_p205"] = [
    n("basic", "What is 20% of 50?", "10", "50×20%＝10.", "50*20/100"),
    n("basic", "An item originally costs 80 yuan. What is its price after a 20% increase?", "96",
      "80×(1＋20%)＝96.", "80*(1+20/100)"),
    n("standard", "There were 40 people last year, and the number increased by 25% this year. How many people are there this year?", "50",
      "40×(1＋25%)＝50.", "40*(1+25/100)"),
    n("challenge", "An item's price increases by 20% and then decreases by 20%. What percentage of the original price is the final price? (Give only the number before the percent sign.)", "96",
      "1.2×0.8＝0.96＝96%.", "120*80/100"),
]

# ---------- Grade 6, first semester, Unit 6: The Pigeonhole Principle ----------
BANK["cnm_p216"] = [
    c("basic", "What does the pigeonhole principle state?",
      ["If there are more objects than boxes, at least one box contains two or more objects", "Each box can hold only one object", "The number of objects must equal the number of boxes"], "A",
      "This is the simplest case of the pigeonhole principle."),
    n("basic", "If 5 pigeons are placed in 4 pigeonholes, at least how many pigeons must be in one pigeonhole, no matter how they are placed?", "2",
      "5＝4×1＋1, so at least one pigeonhole contains 2 pigeons.", "5//4+1"),
    n("standard", "If 9 pencils are placed in 4 pencil holders, at least how many pencils must be in one holder, no matter how they are placed?", "3",
      "9＝4×2＋1, so at least one holder contains 3 pencils.", "9//4+1"),
    n("challenge", "A class has 37 students. At least how many must have birthdays in the same month? (Assume a year has 12 months.)", "4",
      "37＝12×3＋1, so at least 4 students have birthdays in the same month.", "37//12+1"),
]

# ---------- Grade 6, second semester, Unit 3: Cylinders and Cones ----------
BANK["cnm_p206"] = [
    c("basic", "What shape are the two bases of a cylinder?",
      ["Two identical circles", "Two triangles", "Two circles of different sizes"], "A",
      "The two bases have equal radii."),
    n("basic", "One base of a cylinder has a radius of 3 cm. What is the diameter of its other base in centimeters?", "6",
      "The two bases are identical, so diameter＝3×2＝6.", "3*2"),
    c("standard", "Which object has the shape of a cylinder?",
      ["A basketball", "A soda can", "A cube puzzle", "A funnel"], "B",
      "A soda can has two identical circular bases and one curved side, so it is a cylinder."),
    n("challenge", "A rectangle 12.56 cm long and 5 cm wide is wrapped to form the lateral surface of a cylinder, with the width as the height. About how many centimeters is the diameter of the base? Use 314/100 for pi. (Give your answer as a decimal.)",
      "4", "The rectangle's length equals the base circumference, 12.56 cm, so diameter＝12.56÷3.14＝4.", "1256/100 / (314/100)"),
]

BANK["cnm_p207"] = [
    n("basic", "What is the volume, in cubic centimeters, of a cylinder with a base radius of 2 cm and a height of 5 cm? Use 314/100 for pi. (Give your answer as a decimal.)", "62.8",
      "Volume＝3.14×2×2×5＝62.8.", "314/100*2*2*5"),
    n("basic", "What is the volume, in cubic centimeters, of a cylinder with a base radius of 1 cm and a height of 10 cm? Use 314/100 for pi. (Give your answer as a decimal.)", "31.4",
      "3.14×1×1×10＝31.4.", "314/100*1*1*10"),
    n("standard", "A cylinder has a base area of 12 cm² and a height of 4 cm. What is its volume in cubic centimeters?", "48",
      "Volume＝base area×height＝12×4＝48.", "12*4"),
    n("challenge", "What is the volume, in cubic centimeters, of a cylinder with a base diameter of 6 cm and a height of 2 cm? Use 314/100 for pi. (Give your answer as a decimal.)", "56.52",
      "Radius＝3 cm; volume＝3.14×3×3×2＝56.52.", "314/100*3*3*2"),
]

BANK["cnm_p208"] = [
    c("basic", "Which surfaces are included in the surface area of a cylinder?",
      ["Two bases and one lateral surface", "Only the two bases", "Only the lateral surface", "Four lateral surfaces"], "A",
      "Surface area＝area of both bases＋lateral surface area."),
    n("basic", "A cylinder has a base radius of 2 cm. What is the area of one base in square centimeters? Use 314/100 for pi. (Give your answer as a decimal.)", "12.56",
      "3.14×2×2＝12.56.", "314/100*2*2"),
    n("standard", "The lateral surface of a cylinder unfolds into a rectangle 6.28 cm long and 5 cm wide. What is the lateral surface area in square centimeters? (Give your answer as a decimal.)", "31.4",
      "Lateral surface area＝base circumference×height＝6.28×5＝31.4.", "628/100*5"),
    n("challenge", "What is the surface area, in square centimeters, of a cylinder with a base radius of 2 cm and a height of 5 cm? Use 314/100 for pi. (Give your answer as a decimal.)", "87.92",
      "2×3.14×2×(2＋5)＝12.56×7＝87.92.", "2*314/100*2*(2+5)"),
]

BANK["cnm_p248"] = [
    c("basic", "What shape is the base of a cone?",
      ["A circle", "A square", "Two circles"], "A",
      "A cone has one circular base and one vertex."),
    c("basic", "How many vertices does a cone have?", ["1", "2", "0"], "A",
      "A cone has one vertex."),
    c("standard", "Which distance is the height of a cone?",
      ["The distance from the vertex to the center of the base", "The diameter of the base", "The length of a slant side", "The circumference of the base"], "A",
      "The height is the perpendicular distance from the vertex to the center of the base."),
    c("challenge", "What shape do you get when you unfold the lateral surface of a cone?",
      ["A sector", "A rectangle", "A triangle", "A circle"], "A",
      "A cone's lateral surface unfolds into a sector; a cylinder's lateral surface unfolds into a rectangle."),
]

BANK["cnm_p209"] = [
    c("basic", "What fraction of the volume of a cylinder is the volume of a cone with the same base and height?",
      ["One-third", "One-half", "Twice as much"], "A",
      "With the same base and height, a cone's volume is one-third of the cylinder's."),
    n("basic", "A cylinder has a volume of 30 cm³. What is the volume, in cubic centimeters, of a cone with the same base and height?", "10",
      "30÷3＝10.", "30/3"),
    n("standard", "A cone has a base area of 12 cm² and a height of 6 cm. What is its volume in cubic centimeters?", "24",
      "Volume＝1/3×base area×height＝1/3×12×6＝24.", "12*6/3"),
    n("challenge", "What is the volume, in cubic centimeters, of a cone with a base radius of 3 cm and a height of 6 cm? Use 314/100 for pi. (Give your answer as a decimal.)", "56.52",
      "1/3×3.14×3×3×6＝56.52.", "314/100*3*3*6/3"),
]

# ---------- Grade 6, second semester, Unit 4: Ratios and Proportions ----------
BANK["cnm_p185"] = [
    c("basic", "What do you get when you divide the first term of a ratio by the second?",
      ["The value of the ratio", "The first term", "The second term"], "A",
      "First term÷second term＝value of the ratio."),
    n("basic", "What is the value of the ratio 6:8?", "3/4", "6÷8＝3/4.", "6/8"),
    n("standard", "What is the value of the ratio 12:4?", "3", "12÷4＝3.", "12/4"),
    n("challenge", "A class has 20 boys and 15 girls. When the ratio of boys to the whole class is reduced to lowest terms, what is its first term?", "4",
      "There are 35 students, so 20:35＝4:7. The first term is 4.", "20/5"),
]

BANK["cnm_p186"] = [
    n("basic", "After reducing the ratio 12:8 to lowest terms, what is its first term?", "3",
      "12:8＝3:2, so the first term is 3.", "12/4"),
    n("basic", "After reducing the ratio 15:10 to lowest terms, what is its first term?", "3",
      "15:10＝3:2, so the first term is 3.", "15/5"),
    n("standard", "After reducing the ratio 24:18 to lowest terms, what is its second term?", "3",
      "24:18＝4:3, so the second term is 3.", "18/6"),
    n("challenge", "After reducing the ratio 0.5:2 to lowest terms, what is its first term?", "1",
      "Multiply both terms by 2 to get 1:4. The first term is 1.", "1"),
]

BANK["cnm_p187"] = [
    n("basic", "Divide 30 into two parts in the ratio 2:3. What is the part corresponding to 2?", "12",
      "There are 5 parts in total, so each is 6. Two parts equal 12.", "30/(2+3)*2"),
    n("basic", "Divide 40 into two parts in the ratio 1:3. What is the part corresponding to 1?", "10",
      "There are 4 parts in total, so each is 10.", "40/(1+3)*1"),
    n("standard", "Divide 56 notebooks between two classes in the ratio 3:4. How many notebooks does the class receiving more get?", "32",
      "There are 7 parts in total, so each is 8. Four parts equal 32.", "56/(3+4)*4"),
    n("challenge", "Divide 90 yuan into three parts in the ratio 2:3:4. What is the largest part in yuan?", "40",
      "There are 9 parts in total, so each is 10. Four parts equal 40.", "90/(2+3+4)*4"),
]

BANK["cnm_p210"] = [
    c("basic", "How does the product of the two outer terms of a proportion compare with the product of the two inner terms?",
      ["It equals the product of the inner terms", "It is always greater than the product of the inner terms", "There is no fixed relationship"], "A",
      "This is the fundamental property of proportions."),
    n("basic", "In the proportion 2:3＝4:6, what is the product of the two outer terms?", "12",
      "The outer terms are 2 and 6, and 2×6＝12.", "2*6"),
    c("standard", "Which pair of ratios can form a proportion?",
      ["3:5 and 6:9", "6:3 and 8:4", "2:5 and 4:9", "1:4 and 2:9"], "B",
      "6:3＝2 and 8:4＝2. Their values are equal, so they can form a proportion."),
    c("challenge", "The ratios 6:9 and 8:12 have equal values. By the fundamental property of proportions, what does 6×12 equal?",
      ["9×8", "6×8", "9×12", "6＋12"], "A",
      "Since 6:9＝8:12, the product of the outer terms equals the product of the inner terms: 6×12＝9×8."),
]

BANK["cnm_p211"] = [
    n("basic", "2:3＝8:x. What is x?", "12",
      "The product of the outer terms equals the product of the inner terms: 2x＝24, so x＝12.", "8*3/2"),
    n("basic", "4:5＝x:20. What is x?", "16",
      "4×20＝5x, so x＝16.", "4*20/5"),
    n("standard", "6:x＝2:5. What is x?", "15",
      "6×5＝2x, so x＝15.", "6*5/2"),
    n("challenge", "If x:12＝5:8, what is x? (Give your answer as a decimal.)", "7.5",
      "8x＝12×5＝60, so x＝7.5.", "12*5/8"),
]

BANK["cnm_p212"] = [
    c("basic", "What is a scale ratio?",
      ["The ratio of map distance to actual distance", "The sum of map distance and actual distance", "A way to show direction only"], "A",
      "Map distance:actual distance＝scale ratio."),
    n("basic", "A map distance is 4 cm, and the scale is 1:100. What is the actual distance in centimeters?", "400",
      "Actual distance＝map distance×100＝400.", "4*100"),
    n("standard", "The actual distance is 800 cm, and the map distance is 4 cm. What is the scale ratio 1:n?", "200",
      "800÷4＝200, so the scale is 1:200.", "800/4"),
    n("challenge", "A map has a scale of 1:50000. What actual distance in kilometers is represented by 3 cm on the map? (Give your answer as a decimal.)", "1.5",
      "Actual distance＝3×50000＝150000 cm＝1.5 km.", "3*50000/100000"),
]

BANK["cnm_p249"] = [
    n("basic", "A square with a side length of 2 cm is enlarged using a 1:3 scale. What is the new side length in centimeters?", "6",
      "The side length becomes 3 times the original: 2×3＝6.", "2*3"),
    n("basic", "A line segment is 12 cm long. How long is it after being reduced at a 2:1 scale?", "6",
      "It is reduced to 1/2 of its original length: 12÷2＝6.", "12/2"),
    n("standard", "A rectangle is 5 cm long and 3 cm wide. What is its new length after enlargement using a 1:2 scale?", "10",
      "The length becomes 5×2＝10.", "5*2"),
    c("challenge", "When a triangle is enlarged by a scale ratio, which property always stays the same?",
      ["The side lengths", "The angle measures", "The area", "The perimeter"], "B",
      "An enlargement or reduction preserves the shape, so corresponding angles are equal; side lengths, perimeter, and area change."),
]

BANK["cnm_p213"] = [
    c("basic", "What is the defining property of two directly proportional quantities?",
      ["Their ratio is constant", "Their product is constant", "Their sum is constant"], "A",
      "At a constant speed, distance and time are directly proportional."),
    n("basic", "At a constant speed, a traveler covers 180 km in 3 hours. How far will the traveler go in 6 hours?", "360",
      "Distance and time are directly proportional. When the time doubles, the distance doubles: 360 km.", "180/3*6"),
    n("standard", "A water pump works at a constant rate and pumps 12 metric tons in 1 hour. How much will it pump in 5 hours?", "60",
      "The amount pumped is directly proportional to time: 12×5＝60.", "12*5"),
    c("challenge", "Are x and y in the table directly proportional? x: 2, 4, 6; y: 6, 12, 18.",
      ["Yes, because y÷x equals 3 each time", "No, because y changes", "They are inversely proportional because the product is constant", "There is not enough information"], "A",
      "6÷2＝12÷4＝18÷6＝3. The ratio is constant, so the quantities are directly proportional."),
]

BANK["cnm_p214"] = [
    c("basic", "What is the defining property of two inversely proportional quantities?",
      ["Their product is constant", "Their ratio is constant", "Their difference is constant"], "A",
      "When the total cost is fixed, unit price and quantity are inversely proportional."),
    n("basic", "With a fixed total cost, 6 items cost 4 yuan each. How many items can be bought at 3 yuan each?", "8",
      "4×6＝3×x, so x＝8.", "4*6/3"),
    n("standard", "It takes 6 days to repair a road at 8 m per day. How many days will it take at 12 m per day?", "4",
      "The total amount of work is fixed: 8×6＝12×x, so x＝4.", "8*6/12"),
    n("challenge", "Worker A can complete a project alone in 10 days. Worker B works at twice A's rate. How many days will B take alone?", "5",
      "The total work is fixed. At twice the rate, the time is 1/2 as long: 10÷2＝5.", "10/2"),
]

BANK["cnm_p215"] = [
    n("basic", "Three identical notebooks cost 12 yuan. How much do 5 notebooks cost?", "20",
      "Each notebook costs 4 yuan, so 5 cost 20 yuan. Alternatively, use direct proportion: 12÷3×5＝20.", "12/3*5"),
    n("basic", "A traveler covers 90 km in 2 hours. At the same speed, how far will the traveler go in 4 hours?", "180",
      "90÷2×4＝180.", "90/2*4"),
    n("standard", "Six identical machines complete a job in 4 hours. How many hours will 8 machines take?", "3",
      "The total work is fixed, so the number of machines and time are inversely proportional: 6×4÷8＝3.", "6*4/8"),
    n("challenge", "A project is planned to take 5 days at 40 m per day. How many days will it take at 50 m per day?", "4",
      "The total is 5×40＝200 m, and 200÷50＝4 days.", "5*40/50"),
]

BANK["cnm_p250"] = [
    n("basic", "A bicycle has a 48-tooth front gear and a 16-tooth rear gear. About how many times does the rear wheel turn when the pedals turn once?", "3",
      "48÷16＝3.", "48/16"),
    n("basic", "The rear wheel has a circumference of about 2 m. If one pedal rotation turns the rear wheel 3 times, about how far does the bicycle travel?", "6",
      "2×3＝6.", "2*3"),
    c("standard", "On the same bicycle, what generally happens when the rear gear has more teeth and the front gear is unchanged?",
      ["The wheel turns fewer times per pedal rotation, making it easier to pedal", "The wheel turns more times per pedal rotation", "The gear ratio has no effect on riding", "The wheel's circumference increases"], "A",
      "With more teeth on the rear gear, the gear ratio decreases. The wheel turns fewer times per pedal rotation, making pedaling easier but slower."),
    n("challenge", "A bicycle has a 48-tooth front gear, a 16-tooth rear gear, and a rear-wheel circumference of about 2 m. About how far does it travel when the pedals turn 10 times?", "60",
      "One pedal rotation turns the rear wheel 3 times, so 10 rotations turn it 30 times and the bicycle travels 30×2＝60 m.", "10*(48/16)*2"),
]

# ---------- Grade 6, second semester, Unit 6 ----------
BANK["cnm_p199"] = [
    c("basic", "What is a pie chart best suited to showing?",
      ["How much each part contributes to the whole", "How quantities change over time", "Only which number is largest"], "A",
      "The size of each sector represents its percentage of the whole."),
    n("basic", "A class has 40 students, and 25% like soccer. How many students like soccer?", "10",
      "40×25%＝10.", "40*25/100"),
    n("standard", "A class has 50 students, and 40% like soccer. How many students like soccer?", "20",
      "50×40%＝20.", "50*40/100"),
    n("challenge", "On a pie chart, the central angle for students who like basketball is 90 degrees. What percentage of the class likes basketball? (Give only the number before the percent sign.)", "25",
      "90÷360＝1/4＝25%.", "90/360*100"),
]

BANK["cnm_p200"] = [
    n("basic", "Square dot patterns use dots to form square arrays: figure 1 has 1 dot, figure 2 has 4 dots, and figure 3 has 9 dots. How many dots are in figure 5?",
      "25", "Figure n has n² dots, so 5×5＝25.", "5*5"),
    n("basic", "The numbers of dots in successive square arrays are 1, 4, 9, and 16. How many more dots are in figure 4 than in figure 3?", "7",
      "16－9＝7.", "16-9"),
    n("standard", "How many dots are in figure 6 of the square dot pattern?", "36",
      "6×6＝36.", "6*6"),
    n("challenge", "1＋3＋5＋7＋9 equals the number of dots in which square array? Give the number of dots.", "25",
      "The sum of the first 5 odd numbers is 5²＝25, the number of dots in figure 5.", "5*5"),
]


def load(name):
    with open(os.path.join(DATA, name), encoding="utf-8") as f:
        return json.load(f)


def dump(name, obj, indent=2):
    path = os.path.join(DATA, name)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=indent)
        f.write("\n")


def main():
    topics = load("topics.json")
    questions = load("questions.json")
    by_id = {t["id"]: t for t in topics}
    missing = [tid for tid in BANK if tid not in by_id]
    extra = []
    if missing:
        raise SystemExit("Unknown topic IDs: " + ", ".join(missing))
    g6 = [t for t in topics if t.get("grade") == 6 and str(t.get("id", "")).startswith("cnm_")
          and not t.get("external")]
    not_in_bank = [t["id"] for t in g6 if t["id"] not in BANK]
    if not_in_bank:
        raise SystemExit("Grade 6 topics missing from the question bank: " + ", ".join(not_in_bank))

    new_qs = []
    for tid, raw in BANK.items():
        ds = {q["difficulty"] for q in raw}
        if "standard" not in ds or "challenge" not in ds or "basic" not in ds:
            extra.append("%s is missing one or more difficulty levels: %s" % (tid, ds))
        basics = [q for i, q in enumerate(raw) if q["difficulty"] == "basic"]
        if len(basics) < 2 and raw[0]["difficulty"] != "basic":
            extra.append("%s has fewer than two basic questions, excluding a possible q1" % tid)
        if raw[0]["difficulty"] == "basic" and sum(1 for q in raw[1:] if q["difficulty"] == "basic") < 1:
            extra.append("%s has no basic question other than q1" % tid)
        for i, q in enumerate(raw, 1):
            item = dict(q)
            item["id"] = "%s_q%d" % (tid, i)
            item["topicId"] = tid
            if item["difficulty"] == "challenge" and str(item["prompt"]).startswith("Calculate:"):
                extra.append("%s challenge prompt starts with “Calculate:”" % item["id"])
            new_qs.append(item)
        t = by_id[tid]
        q1 = raw[0]
        ans = q1["answer"]
        if q1["type"] == "choice":
            text = [x["text"] for x in q1["choices"] if x["key"] == ans][0]
            # Use the choice text as the diagnostic answer for self-assessment.
            dq_ans = text
        else:
            dq_ans = str(ans)
        t["diagnostic_question"] = {"question": q1["prompt"], "answer": dq_ans}

    if extra:
        raise SystemExit("Question bank validation failed:\n" + "\n".join(extra))

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
        raise SystemExit("No existing questions found for these topic IDs in questions.json: " + ", ".join(sorted(leftover)))

    dump("questions.json", out, 2)
    dump("topics.json", topics, 2)
    g6_qs = [q for q in out if q["topicId"] in old_ids]
    dump("_qbatches/primary_g6.json", g6_qs, 1)

    from collections import Counter
    print("Grade 6 topics: %d, questions: %d" % (len(BANK), len(g6_qs)))
    print("Difficulty", Counter(q["difficulty"] for q in g6_qs))
    print("Types", Counter(q["type"] for q in g6_qs))


if __name__ == "__main__":
    main()
