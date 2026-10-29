#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Align Grade 5 question-bank difficulty: write to data/questions.json, the diagnostic_question field in topics.json, and _qbatches/primary_g5.json.

Each topic gets 2 basic, 1 standard, and 1 challenge question. Basic questions directly test the topic;
standard questions are at textbook-example level; challenge questions add a step or test a common error rather than asking only for a bare calculation.
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
    if verify is not None:
        q["verify"] = verify
    return q


BANK = {}

# ---------- Grade 5, first semester, Unit 1: Observing Simple Composite Solids ----------
BANK["cnm_p237"] = [
    c("basic", "Can you always determine what a composite solid looks like from only its front view?",
      ["Not necessarily", "Yes, always", "Only if it is a cube"], "A",
      "The same view from one direction can correspond to different arrangements.", "'Not necessarily'"),
    n("basic", "The front view shows 3 squares in a row, and the top view also shows 3 squares in a row. What is the smallest number of unit cubes that could make the solid?",
      "3", "Place one cube in each of the three positions to satisfy both views.", "3"),
    n("standard", "The top view shows 2 rows of 2 squares, with 2 cubes stacked at every position. How many unit cubes are there?",
      "8", "There are 4 positions with 2 layers each: 4×2＝8.", "4*2"),
    n("challenge", "Build a composite solid from unit cubes. The top view shows all 6 positions in a 2-by-3 grid occupied. The front-view heights of the three columns are 2, 1, and 2. From the left, the front row is at most 2 cubes high and the back row at most 1 cube high. What is the smallest possible number of cubes?",
      "8", "The back row can be only 1 cube high, so both 2-cube stacks must be in the front row. The six heights are 2, 1, 2 and 1, 1, 1, for a total of 8.",
      "2+1+2+1+1+1"),
]

# ---------- Grade 5, first semester, Unit 2: Multiplying Decimals ----------
BANK["cnm_p132"] = [
    c("basic", "When multiplying a decimal by a whole number, how do you determine the number of decimal places in the product?",
      ["It is the same as the number of decimal places in the decimal factor", "It is always one more than in the factor", "The decimal point can go anywhere"], "A",
      "Multiply as with whole numbers, then place the decimal point using the number of decimal places in the decimal factor.", "'It is the same as the number of decimal places in the decimal factor'"),
    n("basic", "A pen costs 0.3 yuan. How much do 4 pens cost? (Answer with a decimal.)",
      "1.2", "0.3×4＝1.2 yuan.", "Fraction(3,10)*4"),
    n("standard", "A pen costs 1.2 yuan. How much do 4 pens cost? (Answer with a decimal.)",
      "4.8", "1.2×4＝4.8 yuan.", "Fraction(12,10)*4"),
    n("challenge", "A storybook costs 8.5 yuan and a writing notebook costs 1.5 yuan. How much do 3 storybooks and 2 notebooks cost altogether? (Answer with a decimal.)",
      "28.5", "8.5×3＝25.5, 1.5×2＝3, and 25.5＋3＝28.5 yuan.",
      "Fraction(85,10)*3+Fraction(15,10)*2"),
]

BANK["cnm_p133"] = [
    c("basic", "When multiplying two decimals, what is the number of decimal places in the product?",
      ["The sum of the decimal places in the two factors", "Only the larger factor's number of decimal places", "The product is always a whole number"], "A",
      "Add the numbers of decimal places in the factors to get the number in the product; trailing zeros may be removed.", "'The sum of the decimal places in the two factors'"),
    n("basic", "What is the area, in square meters, of a rectangle 0.3 m long and 0.4 m wide? (Answer with a decimal.)",
      "0.12", "0.3×0.4＝0.12 square meters.", "Fraction(3,10)*Fraction(4,10)"),
    n("standard", "What is the area, in square meters, of a rectangle 1.5 m long and 0.4 m wide? (Answer with a decimal.)",
      "0.6", "1.5×0.4＝0.60＝0.6 square meters.", "Fraction(15,10)*Fraction(4,10)"),
    n("challenge", "A rectangular garden is 2.5 m long and 1.2 m wide. It yields 0.8 kg of vegetables per square meter. How many kilograms of vegetables does it yield? (Answer with a decimal.)",
      "2.4", "First find the area: 2.5×1.2＝3 square meters. Then 3×0.8＝2.4 kg.",
      "Fraction(25,10)*Fraction(12,10)*Fraction(8,10)"),
]

BANK["cnm_p134"] = [
    n("basic", "A vehicle travels at 2.4 km per hour for 3 hours. How many kilometers does it travel? (Answer with a decimal.)",
      "7.2", "2.4×3＝7.2 km.", "Fraction(24,10)*3"),
    n("basic", "A pencil costs 0.8 yuan. How much do 6 pencils cost? (Answer with a decimal.)",
      "4.8", "0.8×6＝4.8 yuan.", "Fraction(8,10)*6"),
    n("standard", "A vehicle travels at 3.5 km per hour for 3 hours. How many kilometers does it travel? (Answer with a decimal.)",
      "10.5", "3.5×3＝10.5 km.", "Fraction(35,10)*3"),
    n("challenge", "Apples cost 6.5 yuan per kilogram and pears cost 4.8 yuan per kilogram. How much do 2 kg of apples and 3 kg of pears cost altogether? (Answer with a decimal.)",
      "27.4", "6.5×2＝13, 4.8×3＝14.4, and 13＋14.4＝27.4 yuan.",
      "Fraction(65,10)*2+Fraction(48,10)*3"),
]

# ---------- Grade 5, first semester, Unit 3: Dividing Decimals ----------
BANK["cnm_p137"] = [
    c("basic", "When dividing a decimal by a whole number, where should the decimal point in the quotient go?",
      ["Directly above the decimal point in the dividend", "Always at the far left", "It can be left out"], "A",
      "When dividing, place the decimal point in the quotient directly above the decimal point in the dividend.", "'Directly above the decimal point in the dividend'"),
    n("basic", "A 0.8 m rope is cut into 2 equal pieces. How long is each piece? (Answer with a decimal.)",
      "0.4", "0.8÷2＝0.4 m.", "Fraction(8,10)/2"),
    n("standard", "Three identical ropes have a total length of 4.5 m. How long is each rope? (Answer with a decimal.)",
      "1.5", "4.5÷3＝1.5 m.", "Fraction(45,10)/3"),
    n("challenge", "Four identical pens cost 9.6 yuan, and three identical notebooks cost 6.3 yuan. How much more does one pen cost than one notebook? (Answer with a decimal.)",
      "0.3", "Each pen costs 9.6÷4＝2.4 yuan; each notebook costs 6.3÷3＝2.1 yuan. The difference is 2.4－2.1＝0.3 yuan.",
      "Fraction(96,10)/4-Fraction(63,10)/3"),
]

BANK["cnm_p138"] = [
    c("basic", "When the divisor is a decimal, what should you do before dividing?",
      ["Make the divisor a whole number", "Make only the dividend a whole number and ignore the divisor", "Simply remove every decimal point"], "A",
      "First make the divisor a whole number, multiplying the dividend by the same factor, then divide.", "'Make the divisor a whole number'"),
    n("basic", "Each rope piece is 0.2 m long. How many pieces can be cut from 0.8 m of rope?",
      "4", "0.8÷0.2＝4 pieces.", "Fraction(8,10)/Fraction(2,10)"),
    n("standard", "An eraser costs 0.4 yuan. How many erasers can be bought for 2.4 yuan?",
      "6", "2.4÷0.4＝6 erasers.", "Fraction(24,10)/Fraction(4,10)"),
    n("challenge", "A 3.6 m rope is used to make jump ropes, each 0.4 m long. Five have already been made. How many more can be made from the remaining rope?",
      "4", "The rope makes 3.6÷0.4＝9 jump ropes in total, so 9－5＝4 remain to be made.",
      "Fraction(36,10)/Fraction(4,10)-5"),
]

BANK["cnm_p139"] = [
    n("basic", "A 7.2 L bottle of juice is shared equally among 8 people. How many liters does each person get? (Answer with a decimal.)",
      "0.9", "7.2÷8＝0.9 L.", "Fraction(72,10)/8"),
    n("basic", "You have 4.5 yuan. Notebooks cost 0.5 yuan each. How many can you buy?",
      "9", "4.5÷0.5＝9 notebooks.", "Fraction(45,10)/Fraction(5,10)"),
    n("standard", "A person walks 9.6 km in 3 hours. What is the average speed in kilometers per hour? (Answer with a decimal.)",
      "3.2", "9.6÷3＝3.2 km per hour.", "Fraction(96,10)/3"),
    n("challenge", "An 8.4 m ribbon is cut, and 1.2 m is removed. The rest is divided equally to make 4 flowers. How many meters of ribbon are used for each flower? (Answer with a decimal.)",
      "1.8", "The remaining ribbon is 8.4－1.2＝7.2 m; 7.2÷4＝1.8 m per flower.",
      "(Fraction(84,10)-Fraction(12,10))/4"),
]

# ---------- Grade 5, first semester, Unit 4: Transformations of Shapes ----------
BANK["cnm_p238"] = [
    c("basic", "After a shape is translated, rotated, or reflected across an axis, what happens to its size and shape?",
      ["Both its size and shape stay the same", "It always gets larger", "Its shape always changes"], "A",
      "Translation, rotation, and reflection change only position or orientation, not size or shape.", "'Both its size and shape stay the same'"),
    n("basic", "A point is in column 4 on a grid. Which column is it in after moving 2 squares to the right?",
      "6", "Moving right increases the column number: 4＋2＝6.", "4+2"),
    n("standard", "A point is in column 3, row 2 on a grid. It moves 4 squares to the right and then 3 squares up. Which column is it in now?",
      "7", "Moving up does not change the column. The column is 3＋4＝7.", "3+4"),
    n("challenge", "A clock hand turns clockwise from 12 to 6, then continues clockwise to 9. Through how many degrees has it turned from 12 to 9?",
      "270", "From 12 to 6 is 180 degrees, then from 6 to 9 is 90 degrees: 180＋90＝270 degrees.", "180+90"),
]

# ---------- Grade 5, first semester, Unit 5: Using Letters for Numbers and Relationships ----------
BANK["cnm_p142"] = [
    c("basic", "When a letter is used to represent a number, what does it stand for?",
      ["A number that can vary", "Only the number 1", "A shape's name that cannot be used in calculations"], "A",
      "A letter can stand for a variable number and can be used in calculations.", "'A number that can vary'"),
    n("basic", "If a＝6, what is 5×a?",
      "30", "Substitute 6 for a: 5×6＝30.", "5*6"),
    c("standard", "A pencil costs a yuan. How much do 5 pencils cost?",
      ["a＋5 yuan", "5×a yuan", "a÷5 yuan", "a－5 yuan"], "B",
      "The total cost is unit price times quantity: 5×a yuan.", "'5×a yuan'"),
    n("challenge", "A pencil costs a yuan, and an eraser costs 2 yuan more. How much do 3 pencils and 1 eraser cost when a＝4?",
      "18", "The eraser costs a＋2＝6 yuan. 3×4＋6＝18 yuan.", "3*4+(4+2)"),
]

BANK["cnm_p144"] = [
    c("basic", "If the same number is added to or subtracted from both sides of an equation, what happens to the equality?",
      ["The equality stays true", "Only the left side changes", "The equation is no longer true"], "A",
      "Doing the same addition or subtraction to both sides keeps them equal.", "'The equality stays true'"),
    n("basic", "Given 18＝12＋6, what is the left side after subtracting 6 from both sides?",
      "12", "The left side becomes 18－6＝12; subtract 6 from the right side as well.", "18-6"),
    c("standard", "Given a＝b, which equation remains true if 5 is added to both sides?",
      ["a＋5＝b", "a＋5＝b＋5", "a＝b＋5", "a－5＝b＋5"], "B",
      "Add 5 to both sides, so a＋5＝b＋5.", "'a＋5＝b＋5'"),
    n("challenge", "A balance scale is level, and the left side weighs 40 g. Remove 15 g from each side, then add 7 g to each side. How much does the left side weigh now?",
      "32", "The left side changes to 40－15＋7＝32 g. The same changes are made to the right side, so the scale stays balanced.", "40-15+7"),
]

# ---------- Grade 5, first semester, Unit 6: Areas of Polygons ----------
BANK["cnm_p098"] = [
    c("basic", "What kind of units are hectares and square kilometers?",
      ["Units of area", "Units of mass", "Units of time"], "A",
      "Hectares, square kilometers, and square meters are all units of area.", "'Units of area'"),
    n("basic", "How many square meters are in 1 hectare?",
      "10000", "1 hectare＝10000 square meters.", "10000"),
    n("standard", "1 square kilometer equals 100 hectares. How many hectares are in 3 square kilometers?",
      "300", "3×100＝300 hectares.", "3*100"),
    n("challenge", "One plot of land is 2 hectares and another is 5000 square meters. What is their combined area in square meters?",
      "25000", "2 hectares＝20000 square meters, and 20000＋5000＝25000 square meters.", "2*10000+5000"),
]

BANK["cnm_p240"] = [
    c("basic", "Which segment is the height of a parallelogram?",
      ["A perpendicular segment from a point on one side to the opposite side", "Any slanted side", "A segment connecting opposite vertices"], "A",
      "The height is the perpendicular distance between a base and its opposite side.", "'A perpendicular segment from a point on one side to the opposite side'"),
    c("basic", "What can be said about the lengths of heights drawn to the same base?",
      ["They are all equal", "Some are longer than others", "Each must equal the base"], "A",
      "All heights drawn to the same base have equal lengths.", "'They are all equal'"),
    n("standard", "A rectangle is 8 cm long and 5 cm wide. If its length is the base, what is the corresponding height in centimeters?",
      "5", "A rectangle is a special parallelogram. With the length as the base, the corresponding height is its 5 cm width.", "5"),
    n("challenge", "A rectangle is 8 cm long and 5 cm wide. Translate its top side parallel to the base to form a parallelogram, keeping the base 8 cm long. What is the corresponding height in centimeters?",
      "5", "Translating the top side parallel to the base does not change its perpendicular distance from the base, so the height stays 5 cm.", "5"),
]

BANK["cnm_p147"] = [
    n("basic", "What is the area, in square centimeters, of a parallelogram with a 7 cm base and a 4 cm height?",
      "28", "Area of a parallelogram＝base×height＝7×4＝28.", "7*4"),
    n("basic", "What is the area, in square centimeters, of a parallelogram with a 9 cm base and a 5 cm height?",
      "45", "9×5＝45 square centimeters.", "9*5"),
    n("standard", "A parallelogram-shaped lawn has a 12 m base and a 6 m height. What is its area in square meters?",
      "72", "12×6＝72 square meters.", "12*6"),
    n("challenge", "One parallelogram has a 10 cm base and 4 cm height; another has an 8 cm base and 6 cm height. How many square centimeters larger is the second area?",
      "8", "The first area is 10×4＝40; the second is 8×6＝48; 48－40＝8.", "8*6-10*4"),
]

BANK["cnm_p148"] = [
    n("basic", "What is the area, in square centimeters, of a triangle with an 8 cm base and a 5 cm height?",
      "20", "Triangle area＝base×height÷2＝8×5÷2＝20.", "8*5/2"),
    n("basic", "What is the area, in square centimeters, of a triangle with a 6 cm base and a 4 cm height?",
      "12", "6×4÷2＝12 square centimeters.", "6*4/2"),
    n("standard", "A triangular piece of fabric has a 10 cm base and a 6 cm height. What is its area in square centimeters?",
      "30", "10×6÷2＝30 square centimeters.", "10*6/2"),
    n("challenge", "A parallelogram has a 12 cm base and an 8 cm height. A diagonal divides it into two congruent triangles. What is the area of one triangle in square centimeters?",
      "48", "The parallelogram's area is 12×8＝96, so each triangle has half that area: 96÷2＝48.", "12*8/2"),
]

BANK["cnm_p149"] = [
    n("basic", "What is the area, in square centimeters, of a trapezoid with bases of 2 cm and 6 cm and a height of 4 cm?",
      "16", "(2＋6)×4÷2＝16 square centimeters.", "(2+6)*4/2"),
    n("basic", "What is the area, in square centimeters, of a trapezoid with bases of 3 cm and 7 cm and a height of 4 cm?",
      "20", "(3＋7)×4÷2＝20 square centimeters.", "(3+7)*4/2"),
    n("standard", "A trapezoid-shaped field has bases of 4 m and 8 m and a height of 5 m. What is its area in square meters?",
      "30", "(4＋8)×5÷2＝30 square meters.", "(4+8)*5/2"),
    n("challenge", "A trapezoid has bases of 5 cm and 9 cm and an area of 28 square centimeters. What is its height in centimeters?",
      "4", "(Base₁＋base₂)×height÷2＝28, so 14×height÷2＝28 and the height is 4 cm.", "28*2/(5+9)"),
]

BANK["cnm_p150"] = [
    n("basic", "A composite shape is divided into two rectangles with areas of 12 and 8 square centimeters. What is the total area in square centimeters?",
      "20", "Add the two parts: 12＋8＝20 square centimeters.", "12+8"),
    n("basic", "A 30-square-centimeter rectangle has a 6-square-centimeter square cut out of it. How many square centimeters remain?",
      "24", "Subtract the removed area from the total: 30－6＝24.", "30-6"),
    n("standard", "A triangle with an area of 10 square centimeters is joined to a rectangle with an area of 24 square centimeters. What is the combined area?",
      "34", "24＋10＝34 square centimeters.", "24+10"),
    n("challenge", "A rectangle is 10 cm long and 6 cm wide. A square with 2 cm sides is cut from one corner. What area remains, in square centimeters?",
      "56", "The rectangle's area is 10×6＝60; the removed square's area is 2×2＝4; 60－4＝56 square centimeters.", "10*6-2*2"),
]

# ---------- Grade 5, first semester, Integrated Project: Interesting Tessellations ----------
BANK["cnm_p239"] = [
    n("basic", "Each interior angle of an equilateral triangle is 60 degrees. How many triangles fit exactly around one point?",
      "6", "A full turn is 360 degrees: 360÷60＝6.", "360//60"),
    n("basic", "Each interior angle of a square is 90 degrees. How many squares fit around one point to make a tessellation?",
      "4", "360÷90＝4.", "360//90"),
    n("standard", "Each interior angle of a regular hexagon is 120 degrees. How many hexagons fit around one point to make a tessellation?",
      "3", "360÷120＝3.", "360//120"),
    c("challenge", "Each interior angle of a regular pentagon is 108 degrees. Can regular pentagons tessellate the plane by themselves?",
      ["No; 108° does not divide 360° evenly", "Yes, because it has 5 sides", "Only in a single row", "Yes, because 108° is greater than 90°"], "A",
      "108×3＝324, which is less than 360; 108×4＝432, which is greater than 360. They cannot fit exactly around a point, so they cannot tessellate by themselves.",
      "'No; 108° does not divide 360° evenly'"),
]

# ---------- Grade 5, first semester, Unit 7: Possibility ----------
BANK["cnm_p140"] = [
    c("basic", "How likely is an event that is certain to happen?",
      ["It will definitely happen", "It may or may not happen", "It will not happen"], "A",
      "\"Certain\" means the event will definitely happen.", "'It will definitely happen'"),
    c("basic", "What happens with an impossible event?",
      ["It will not happen", "It will definitely happen", "It has a 50% chance"], "A",
      "\"Impossible\" means the event will not happen.", "'It will not happen'"),
    c("standard", "A box contains 4 red balls and 1 blue ball. One ball is drawn at random. Which statement is correct?",
      ["It is impossible to draw a blue ball", "A red ball is certain to be drawn", "A blue ball may be drawn", "It is impossible to draw a red ball"], "C",
      "Both red and blue balls are in the box, so a blue ball may be drawn; drawing a red ball is not certain.", "'A blue ball may be drawn'"),
    n("challenge", "A bag contains 8 balls, each red or blue. If drawing a blue ball is impossible, how many are red?",
      "8", "If drawing a blue ball is impossible, there are no blue balls, so all 8 are red.", "8"),
]

BANK["cnm_p141"] = [
    c("basic", "If two outcomes have the same number of items, how do their chances compare?",
      ["The two outcomes are equally likely", "The first outcome must happen first", "The second outcome is impossible"], "A",
      "When the counts are equal, each outcome is equally likely.", "'The two outcomes are equally likely'"),
    n("basic", "A bag contains 5 red balls and 2 blue balls. How many blue balls must be added to make drawing a red ball and drawing a blue ball equally likely?",
      "3", "The number of blue balls must match the number of red balls: 5－2＝3 more balls.", "5-2"),
    c("standard", "A box contains 6 white balls and 2 black balls. One ball is drawn at random. Which color is more likely?",
      ["Black", "They are equally likely", "White", "It is impossible to draw white"], "C",
      "There are more white balls than black balls, so drawing white is more likely.", "'White'"),
    n("challenge", "A bag contains 3 red balls and 5 yellow balls. What is the smallest number of red balls to add so that drawing red is more likely than drawing yellow?",
      "3", "There must be more than 5 red balls, so there must be at least 6. Add 6－3＝3 red balls.", "5-3+1"),
]

# ---------- Grade 5, first semester, Unit 8: Review and Connections ----------
BANK["cnm_p135"] = [
    n("basic", "What is 1.6 multiplied by 2.4, rounded to one decimal place? (Answer with a decimal.)",
      "3.8", "1.6×2.4＝3.84. The hundredths digit is 4, so rounded to one decimal place the result is 3.8.",
      "Fraction(int(Fraction(16,10)*Fraction(24,10)*10+Fraction(1,2)),10)"),
    n("basic", "What is 1.9 multiplied by 0.4, rounded to one decimal place? (Answer with a decimal.)",
      "0.8", "1.9×0.4＝0.76. The hundredths digit is 6, so round the tenths digit up to get 0.8.",
      "Fraction(int(Fraction(19,10)*Fraction(4,10)*10+Fraction(1,2)),10)"),
    n("standard", "What is 1.25 multiplied by 1.3, rounded to two decimal places? (Answer with a decimal.)",
      "1.63", "1.25×1.3＝1.625. The thousandths digit is 5, so rounded to two decimal places the result is 1.63.",
      "Fraction(int(Fraction(125,100)*Fraction(13,10)*100+Fraction(1,2)),100)"),
    n("challenge", "Ribbon costs 2.37 yuan per meter. About how much do 1.6 m cost, rounded to two decimal places? (Answer with a decimal.)",
      "3.79", "2.37×1.6＝3.792. The thousandths digit is 2, so the hundredths digit stays the same and the rounded cost is 3.79 yuan.",
      "Fraction(int(Fraction(237,100)*Fraction(16,10)*100+Fraction(1,2)),100)"),
]

BANK["cnm_p143"] = [
    n("basic", "Consider these four expressions: ①x＋3＝8 ②5＋2＝7 ③x－4＞1 ④9－x＝2. How many are equations?",
      "2", "An equation is an equality containing an unknown. ① and ④ are equations; ② has no unknown, and ③ is an inequality.", "2"),
    c("basic", "Which two conditions must an expression meet to be an equation?",
      ["It contains an unknown and is an equality", "It only needs to be an equality", "It only needs to contain a letter"], "A",
      "An equation is an equality that contains an unknown.", "'It contains an unknown and is an equality'"),
    c("standard", "Which expression is an equation?",
      ["12＋8＝20", "x＋9＞12", "x＋9＝30", "30－9＜25"], "C",
      "x＋9＝30 contains an unknown and is an equality.", "'x＋9＝30'"),
    n("challenge", "Consider these five expressions: ①3x＝12 ②7＋5＝12 ③x÷2＝4 ④2x＋1＞5 ⑤18－x＝9. How many are equations?",
      "3", "①, ③, and ⑤ are equalities containing an unknown. ② has no unknown, and ④ is an inequality.", "3"),
]

BANK["cnm_p145"] = [
    n("basic", "Solve x＋17＝40. What is x?",
      "23", "Subtract 17 from both sides: x＝40－17＝23.", "40-17"),
    n("basic", "Solve 3x＝24. What is x?",
      "8", "Divide both sides by 3: x＝24÷3＝8.", "24/3"),
    n("standard", "Solve 2x＋5＝17. What is x?",
      "6", "First subtract 5 from both sides to get 2x＝12, then divide by 2 to get x＝6.", "(17-5)/2"),
    n("challenge", "Solve 3x－4＝17. What is x?",
      "7", "First add 4 to both sides to get 3x＝21, then divide by 3 to get x＝7.", "(17+4)/3"),
]

BANK["cnm_p146"] = [
    c("basic", "Xiaoming had x stamps and bought 18 more. He now has 50 stamps. Which equation is correct?",
      ["x－18＝50", "x＋18＝50", "18x＝50", "x÷18＝50"], "B",
      "The original number plus 18 equals 50: x＋18＝50.", "'x＋18＝50'"),
    n("basic", "A rope has 15 m used and 9 m left. How long was it originally, in meters?",
      "24", "Add the used and remaining lengths: 15＋9＝24 m.", "15+9"),
    n("standard", "A vehicle travels at 12 km per hour for x hours and covers 36 km. What is x?",
      "3", "12x＝36, so x＝36÷12＝3.", "36/12"),
    n("challenge", "A mother buys 3 kg of apples and 2 kg of pears for 32 yuan. Pears cost 4 yuan per kilogram. How much do apples cost per kilogram?",
      "8", "The pears cost 2×4＝8 yuan. Let x be the price per kilogram of apples: 3x＋8＝32, so 3x＝24 and x＝8.", "(32-2*4)/3"),
]

BANK["cnm_p151"] = [
    c("basic", "When trees are planted at both ends of a path, how are the number of trees and the number of intervals related?",
      ["There is 1 more tree than interval", "The number of trees equals the number of intervals", "There is 1 fewer tree than interval"], "A",
      "With trees at both ends: number of trees＝number of intervals＋1.", "'There is 1 more tree than interval'"),
    n("basic", "A path is divided into 5 intervals, with a tree planted at each end. How many trees are needed?",
      "6", "With trees at both ends, the number of trees is one more than the number of intervals: 5＋1＝6.", "5+1"),
    n("standard", "A 20 m path has a tree planted every 4 m, including both ends. How many trees are planted?",
      "6", "There are 20÷4＝5 intervals; with trees at both ends, 5＋1＝6 trees.", "20//4+1"),
    n("challenge", "A 60 m path originally has a tree planted every 5 m, including both ends. The spacing changes to 10 m, still with trees at both ends. How many fewer trees are planted?",
      "6", "Originally there are 60÷5＋1＝13 trees; afterward there are 60÷10＋1＝7. The difference is 13－7＝6 trees.",
      "(60//5+1)-(60//10+1)"),
]

# ---------- Grade 5, second semester, Unit 1: Viewing Solids (Part 3) ----------
BANK["cnm_p152"] = [
    c("basic", "When viewing the same simple solid from the front, side, and top, how might the views compare?",
      ["They may look different", "They must look the same from all three directions", "Only the top can be seen"], "A",
      "Views from different directions may look different, so compare them together.", "'They may look different'"),
    n("basic", "Four identical unit cubes are arranged in a single row, one layer high. How many squares are visible from above?",
      "4", "There is one layer in a row, so 4 squares are visible from above.", "4"),
    c("standard", "Four identical unit cubes form a solid. The top view shows 4 squares in a row, and the front view also shows 4 squares in a row. How are the cubes arranged?",
      ["Stacked four high", "Two layers with 2 cubes in each", "Two rows with 2 cubes in each", "In one row, one layer high"], "D",
      "Both views show a single row, so the cubes are arranged in one row and one layer.", "'In one row, one layer high'"),
    n("challenge", "The top view shows 2 rows and 3 columns, with a cube at all 6 positions. Each position in the front row has 2 layers, and each position in the back row has 1 layer. How many unit cubes are there?",
      "9", "The front row has 3×2＝6 cubes and the back row has 3×1＝3, for a total of 6＋3＝9.", "3*2+3*1"),
]

# ---------- Grade 5, second semester, Unit 2: Factors and Multiples ----------
BANK["cnm_p153"] = [
    n("basic", "How many factors does 12 have?",
      "6", "The factors of 12 are 1, 2, 3, 4, 6, and 12, for a total of 6.",
      "len([d for d in range(1,13) if 12%d==0])"),
    n("basic", "Which multiple of 6 is greater than 20 and less than 30?",
      "24", "6×4＝24; 6×5＝30 is not less than 30.", "6*4"),
    n("standard", "Which factor other than 6, when multiplied by 6, gives 18?",
      "3", "Factors come in pairs: 6×3＝18, so the other factor is 3.", "18//6"),
    n("challenge", "How many numbers less than or equal to 100 are multiples of both 6 and 8?",
      "4", "The numbers are 24, 48, 72, and 96, for a total of 4.",
      "len([k for k in range(1,101) if k%6==0 and k%8==0])"),
]

BANK["cnm_p154"] = [
    c("basic", "Which digits can appear in the ones place of a multiple of 2?",
      ["0, 2, 4, 6, or 8", "1, 3, 5, 7, or 9", "Only 0"], "A",
      "A number with 0, 2, 4, 6, or 8 in the ones place is divisible by 2.", "'0, 2, 4, 6, or 8'"),
    c("basic", "A number ending in 0 or 5 is always a multiple of what?",
      ["5", "3", "It can only be odd"], "A",
      "A number ending in 0 or 5 is divisible by 5.", "'5'"),
    n("standard", "Which of 20, 25, 32, and 45 is a multiple of both 2 and 5?",
      "20", "A number that is a multiple of both 2 and 5 must end in 0. Only 20 does.", "20"),
    n("challenge", "How many numbers from 1 through 40 are multiples of both 2 and 5?",
      "4", "The numbers ending in 0 are 10, 20, 30, and 40, for a total of 4.",
      "len([k for k in range(1,41) if k%2==0 and k%5==0])"),
]

BANK["cnm_p155"] = [
    n("basic", "To test whether 123 is a multiple of 3, first add its digits. What is 1＋2＋3?",
      "6", "1＋2＋3＝6. Since 6 is a multiple of 3, 123 is also a multiple of 3.", "1+2+3"),
    c("basic", "How can you tell whether a number is a multiple of 3?",
      ["Add its digits and check whether the sum is a multiple of 3", "Check only whether the ones digit is 3", "Check whether the ones digit is 0 or 5"], "A",
      "If the sum of a number's digits is a multiple of 3, the number is also a multiple of 3.", "'Add its digits and check whether the sum is a multiple of 3'"),
    c("standard", "Which number is a multiple of 3?",
      ["71", "81", "83", "92"], "B",
      "8＋1＝9, and 9 is a multiple of 3, so 81 is a multiple of 3.", "'81'"),
    n("challenge", "How many two-digit numbers can be made from 1, 2, and 3 without repeating a digit that are multiples of 3?",
      "2", "The numbers are 12, 13, 21, 23, 31, and 32. Only 12 and 21 have digit sums that are multiples of 3.",
      "len([10*a+b for a in (1,2,3) for b in (1,2,3) if a!=b and (a+b)%3==0])"),
]

BANK["cnm_p156"] = [
    c("basic", "Which digits can appear in the ones place of an even number?",
      ["0, 2, 4, 6, or 8", "Only 1 or 3", "Any digit"], "A",
      "An even number is a multiple of 2 and has 0, 2, 4, 6, or 8 in the ones place.", "'0, 2, 4, 6, or 8'"),
    n("basic", "How many even numbers are there from 1 through 28?",
      "14", "The even numbers are 2, 4, …, 28, for a total of 28÷2＝14.", "28//2"),
    c("standard", "Which number is odd?",
      ["14", "27", "40", "66"], "B",
      "27 ends in 7, so it is not divisible by 2 and is odd.", "'27'"),
    n("challenge", "What is the sum of the two smallest different two-digit odd numbers?",
      "24", "The two smallest different two-digit odd numbers are 11 and 13. Odd plus odd is even: 11＋13＝24.", "11+13"),
]

BANK["cnm_p157"] = [
    c("basic", "What are the factors of a prime number?",
      ["Only 1 and the number itself", "Only 1", "At least 3 factors"], "A",
      "A prime number has exactly two factors: 1 and itself.", "'Only 1 and the number itself'"),
    c("basic", "Is 1 prime or composite?",
      ["Neither prime nor composite", "The smallest prime", "Composite"], "A",
      "1 has only one factor, so it is neither prime nor composite.", "'Neither prime nor composite'"),
    n("standard", "How many prime numbers are less than or equal to 20?",
      "8", "The primes up to 20 are 2, 3, 5, 7, 11, 13, 17, and 19, for a total of 8.",
      "sum(1 for n in range(2,21) if sum(1 for d in range(2,n) if n%d==0)==0)"),
    n("challenge", "What is the product of the smallest prime and the smallest composite number?",
      "8", "The smallest prime is 2, and the smallest composite number is 4 (1 is neither prime nor composite): 2×4＝8.", "2*4"),
]

# ---------- Grade 5, second semester, Unit 3: Cuboids and Cubes ----------
BANK["cnm_p160"] = [
    c("basic", "How many faces does a cuboid have?",
      ["6", "4", "8"], "A",
      "A cuboid has 6 faces, 12 edges, and 8 vertices.", "'6'"),
    c("basic", "What can be said about the edges of a cube?",
      ["They are all the same length", "Only 4 are the same length", "They are all different lengths"], "A",
      "All 12 edges of a cube are equal in length; a cube is a special kind of cuboid.", "'They are all the same length'"),
    n("standard", "A cuboid has three pairs of identical opposite faces. How many pairs of faces have the same shape and size?",
      "3", "Its 6 faces form 3 pairs of opposite faces.", "6//2"),
    n("challenge", "A cuboid is 5 cm long, 4 cm wide, and 3 cm high. What is the total length of its 12 edges in centimeters?",
      "48", "There are 4 edges of each dimension: 4×(5＋4＋3)＝48 cm.", "4*(5+4+3)"),
]

BANK["cnm_p161"] = [
    n("basic", "What is the surface area, in square centimeters, of a cuboid 5 cm long, 4 cm wide, and 3 cm high?",
      "94", "(5×4＋5×3＋4×3)×2＝94 square centimeters.", "(5*4+5*3+4*3)*2"),
    n("basic", "What is the surface area, in square centimeters, of a cube with 3 cm edges?",
      "54", "One face has area 3×3＝9, and there are 6 faces: 9×6＝54 square centimeters.", "3*3*6"),
    n("standard", "A cube has 2 cm edges. What is its surface area in square centimeters?",
      "24", "One face has area 2×2＝4, and there are 6 faces: 4×6＝24 square centimeters.", "2*2*6"),
    n("challenge", "An open-top cuboid box is 6 cm long, 4 cm wide, and 3 cm high. What is the minimum area of paper needed in square centimeters?",
      "84", "The complete surface area is 108 square centimeters. Remove the top, which is 6×4＝24, leaving 108－24＝84.",
      "(6*4+6*3+4*3)*2-6*4"),
]

BANK["cnm_p162"] = [
    c("basic", "What should be used to express volume?",
      ["Units of volume", "Units of length", "A number without a unit"], "A",
      "Volume is expressed in cubic centimeters, cubic decimeters, or cubic meters.", "'Units of volume'"),
    n("basic", "1 cubic decimeter＝1000 cubic centimeters. How many cubic centimeters are in 2 cubic decimeters?",
      "2000", "2×1000＝2000 cubic centimeters.", "2*1000"),
    n("standard", "1 cubic meter＝1000 cubic decimeters. How many cubic decimeters are in 3 cubic meters?",
      "3000", "3×1000＝3000 cubic decimeters.", "3*1000"),
    n("challenge", "1 cubic meter＝1000 cubic decimeters, and 1 cubic decimeter＝1000 cubic centimeters. How many cubic centimeters are in 1 cubic meter?",
      "1000000", "1000×1000＝1000000 cubic centimeters.", "1000*1000"),
]

BANK["cnm_p163"] = [
    n("basic", "What is the volume, in cubic centimeters, of a cuboid 5 cm long, 4 cm wide, and 3 cm high?",
      "60", "Length×width×height＝5×4×3＝60.", "5*4*3"),
    n("basic", "What is the volume, in cubic centimeters, of a cube with 3 cm edges?",
      "27", "Edge×edge×edge＝3×3×3＝27.", "3*3*3"),
    n("standard", "A cuboid box is 8 cm long, 5 cm wide, and 2 cm high. What is its volume in cubic centimeters?",
      "80", "8×5×2＝80 cubic centimeters.", "8*5*2"),
    n("challenge", "How many cubic centimeters less is the volume of a cube with 4 cm edges than that of a cuboid 8 cm long, 5 cm wide, and 2 cm high?",
      "16", "The cube's volume is 4×4×4＝64; the cuboid's is 8×5×2＝80; 80－64＝16.", "8*5*2-4*4*4"),
]

BANK["cnm_p164"] = [
    c("basic", "What does capacity mean?",
      ["The volume of liquid or other material a container can hold", "The container's external surface area", "The thickness of the container's walls"], "A",
      "Capacity is the volume a container can hold.", "'The volume of liquid or other material a container can hold'"),
    n("basic", "1 liter＝1000 milliliters. How many milliliters are in 2 liters?",
      "2000", "2×1000＝2000 milliliters.", "2*1000"),
    c("standard", "A bottle contains 500 milliliters of a drink. How many liters are in 2 bottles?",
      ["1 liter", "2 liters", "10 liters", "100 liters"], "A",
      "500×2＝1000 milliliters＝1 liter.", "'1 liter'"),
    n("challenge", "A rectangular water tank measures 5 dm by 4 dm by 3 dm on the inside. How many liters of water can it hold? (1 cubic decimeter＝1 liter.)",
      "60", "Its capacity is 5×4×3＝60 cubic decimeters, or 60 liters.", "5*4*3"),
]

# ---------- Grade 5, second semester, Unit 4: Meaning and Properties of Fractions ----------
BANK["cnm_p158"] = [
    n("basic", "What is the greatest common factor of 12 and 18?",
      "6", "The factors of 12 are 1, 2, 3, 4, 6, and 12; the greatest factor it shares with 18 is 6.", "gcd(12,18)"),
    n("basic", "What is the greatest common factor of 8 and 12?",
      "4", "The greatest shared factor is 4.", "gcd(8,12)"),
    n("standard", "What is the greatest common factor of 18 and 24?",
      "6", "18＝6×3 and 24＝6×4, so the greatest common factor is 6.", "gcd(18,24)"),
    n("challenge", "What is the greatest common factor of 12, 18, and 30?",
      "6", "The greatest common factor of 12 and 18 is 6, and 6 also divides 30, so the greatest common factor of all three numbers is 6.",
      "gcd(gcd(12,18),30)"),
]

BANK["cnm_p159"] = [
    n("basic", "What is the least common multiple of 4 and 6?",
      "12", "Multiples of 4 include 4, 8, 12, 16, …; multiples of 6 include 6, 12, 18, … . The least common multiple is 12.", "lcm(4,6)"),
    n("basic", "What is the least common multiple of 3 and 5?",
      "15", "The only common factor of 3 and 5 is 1, so their least common multiple is 3×5＝15.", "lcm(3,5)"),
    n("standard", "What is the least common multiple of 6 and 8?",
      "24", "Multiples of 6: 6, 12, 18, 24, …; multiples of 8: 8, 16, 24, … . The least is 24.", "lcm(6,8)"),
    n("challenge", "What is the least common multiple of 4, 6, and 8?",
      "24", "The least common multiple of 4 and 6 is 12; the least common multiple of 12 and 8 is 24.", "lcm(lcm(4,6),8)"),
]

BANK["cnm_p165"] = [
    n("basic", "A sheet of paper is divided into 8 equal parts, and 5 are colored. Into how many parts was it divided?",
      "8", "The denominator 8 means the whole is divided into 8 equal parts; the numerator 5 means 5 parts are colored.", "8"),
    n("basic", "A pie is divided into 4 equal slices, and 1 slice is eaten. What fraction of the pie was eaten?",
      "1/4", "One part out of 4 equal parts is 1/4.", "Fraction(1,4)"),
    n("standard", "A box of 12 colored pencils is divided equally into 3 groups, and 2 groups are taken. What fraction of the pencils is taken?",
      "2/3", "Two of the 3 equal groups are taken, so the fraction is 2/3. The total of 12 pencils does not affect the fraction.", "Fraction(2,3)"),
    n("challenge", "A rope is divided into 8 equal lengths, and 3 lengths are used. What fraction of its total length remains?",
      "5/8", "There are 8－3＝5 lengths left, which is 5/8 of the total.", "Fraction(8-3,8)"),
]

BANK["cnm_p166"] = [
    c("basic", "What kind of fraction has a numerator smaller than its denominator?",
      ["A proper fraction", "An improper fraction", "Neither a proper nor an improper fraction"], "A",
      "A fraction with a numerator smaller than its denominator is less than 1 and is a proper fraction.", "'A proper fraction'"),
    c("basic", "What kind of fraction is 7/4?",
      ["An improper fraction", "A proper fraction", "It is not a fraction"], "A",
      "The numerator 7 is greater than the denominator 4, so 7/4 is greater than 1 and is an improper fraction.", "'An improper fraction'"),
    c("standard", "Which is a proper fraction?",
      ["5/5", "7/4", "3/8", "9/8"], "C",
      "Only 3/8 has a numerator smaller than its denominator. 5/5, 7/4, and 9/8 are improper fractions.", "'3/8'"),
    n("challenge", "How many improper fractions are there among 2/3, 5/5, 7/4, 8/3, and 1/6?",
      "3", "An improper fraction has a numerator greater than or equal to its denominator: 5/5, 7/4, and 8/3. There are 3.",
      "sum(1 for a,b in ((2,3),(5,5),(7,4),(8,3),(1,6)) if a>=b)"),
]

BANK["cnm_p167"] = [
    n("basic", "The numerator and denominator of 1/2 are both multiplied by 3. What is the denominator of the new fraction?",
      "6", "The denominator is 2×3＝6; the fraction's value stays the same, and the new fraction is 3/6.", "2*3"),
    c("basic", "If the numerator and denominator are both multiplied or divided by the same nonzero number, what happens to the fraction's value?",
      ["It stays the same", "It always increases", "It always becomes 1"], "A",
      "This is the fundamental property of fractions: the value stays the same.", "'It stays the same'"),
    n("standard", "Divide the numerator and denominator of 4/8 by 4. What fraction do you get?",
      "1/2", "4÷4＝1 and 8÷4＝2, so the fraction is 1/2 and its value is unchanged.", "Fraction(4,8)"),
    n("challenge", "The numerator and denominator of a fraction are both multiplied by 4, resulting in 12/20. What was the original fraction?",
      "3/5", "Divide 12 and 20 by 4: 12÷4＝3 and 20÷4＝5, so the original fraction was 3/5.",
      "Fraction(12,4)/Fraction(20,4)"),
]

BANK["cnm_p168"] = [
    n("basic", "Write 6/8 in simplest form. What is the simplified fraction?",
      "3/4", "Divide the numerator and denominator by 2: 6/8＝3/4.", "Fraction(6,8)"),
    n("basic", "Write 4/10 in simplest form. What is the simplified fraction?",
      "2/5", "Divide the numerator and denominator by 2: 4/10＝2/5.", "Fraction(4,10)"),
    n("standard", "Write 8/12 in simplest form. What is the simplified fraction?",
      "2/3", "The greatest common factor of 8 and 12 is 4: 8/12＝2/3.", "Fraction(8,12)"),
    n("challenge", "Write 18/24 in simplest form. What is the simplified fraction?",
      "3/4", "The greatest common factor of 18 and 24 is 6: 18÷6＝3 and 24÷6＝4, giving 3/4.", "Fraction(18,24)"),
]

BANK["cnm_p169"] = [
    n("basic", "Which is greater, 3/5 or 1/5?",
      "3/5", "The denominators are equal, so the fraction with the larger numerator is greater: 3/5.", "max(Fraction(3,5),Fraction(1,5))"),
    n("basic", "Which is greater, 2/3 or 3/4?",
      "3/4", "With a common denominator, 8/12＜9/12, so 3/4 is greater.", "max(Fraction(2,3),Fraction(3,4))"),
    n("standard", "Two ropes are the same length. One has 3/8 used and the other has 5/8 used. What fraction of the full length was used from the rope with more used?",
      "5/8", "The denominators are equal, and 5/8＞3/8, so the greater amount is 5/8.", "max(Fraction(3,8),Fraction(5,8))"),
    n("challenge", "Which is the greatest fraction among 1/2, 2/3, and 3/5?",
      "2/3", "With denominator 30, the fractions are 15/30, 20/30, and 18/30. The greatest is 20/30, or 2/3.",
      "max(Fraction(1,2),Fraction(2,3),Fraction(3,5))"),
]

BANK["cnm_p170"] = [
    n("basic", "Write 3/10 as a decimal. (Answer with a decimal.)",
      "0.3", "3/10＝0.3.", "Fraction(3,10)"),
    n("basic", "Write 25/100 as a decimal. (Answer with a decimal.)",
      "0.25", "25/100＝0.25.", "Fraction(25,100)"),
    n("standard", "Write 0.7 as a fraction in simplest form.",
      "7/10", "0.7 is 7 tenths, or 7/10.", "Fraction(7,10)"),
    n("challenge", "Write 0.125 as a fraction in simplest form.",
      "1/8", "0.125＝125/1000. Divide the numerator and denominator by 125 to get 1/8.", "Fraction(125,1000)"),
]

BANK["cnm_p172"] = [
    n("basic", "What is the least common denominator for 1/2 and 1/3?",
      "6", "The least common multiple of 2 and 3 is 6.", "lcm(2,3)"),
    n("basic", "What is the least common denominator for 1/4 and 3/8?",
      "8", "The least common multiple of 4 and 8 is 8.", "lcm(4,8)"),
    n("standard", "What is the least common denominator for 1/6 and 1/4?",
      "12", "The least common multiple of 6 and 4 is 12.", "lcm(6,4)"),
    n("challenge", "Rewrite 2/3 and 3/4 with denominator 12. What is the numerator of 2/3 after conversion?",
      "8", "To change the denominator 3 to 12, multiply by 4. Multiply the numerator by 4 as well: 2×4＝8, so 2/3＝8/12.", "2*12//3"),
]

# ---------- Grade 5, second semester, Unit 5: Transformations of Shapes (Part 3) ----------
BANK["cnm_p171"] = [
    c("basic", "What happens to a shape's size and form when it is rotated?",
      ["Both its size and shape stay the same", "It always gets larger", "Its shape always changes"], "A",
      "A rotation changes only orientation; size and shape stay the same.", "'Both its size and shape stay the same'"),
    n("basic", "A pinwheel rotates 90 degrees clockwise around its center, then another 90 degrees clockwise. Through how many degrees does it rotate in total?",
      "180", "The rotations are in the same direction, so add the angles: 90＋90＝180.", "90+90"),
    n("standard", "A clock's hour hand moves from 12 to 4. Through how many degrees does it rotate? Each interval between neighboring numbers is 30 degrees.",
      "120", "It moves through 4 intervals: 4×30＝120 degrees.", "4*30"),
    n("challenge", "A shape rotates 90 degrees clockwise, then 35 degrees counterclockwise. What is the equivalent clockwise rotation?",
      "55", "The 35-degree counterclockwise rotation cancels part of the clockwise turn: 90－35＝55 degrees.", "90-35"),
]

# ---------- Grade 5, second semester, Unit 6: Adding and Subtracting Fractions ----------
BANK["cnm_p243"] = [
    n("basic", "Calculate: 3/8＋1/8＝?",
      "1/2", "Keep the denominator and add the numerators: 4/8＝1/2.", "Fraction(3,8)+Fraction(1,8)"),
    n("basic", "Calculate: 7/9－4/9＝?",
      "1/3", "Keep the denominator and subtract the numerators: 3/9＝1/3.", "Fraction(7,9)-Fraction(4,9)"),
    n("standard", "First, 5/12 of a rope's total length is used; then another 7/12 is used. What fraction of the total length is used altogether?",
      "1", "5/12＋7/12＝12/12＝1, which is the entire length.", "Fraction(5,12)+Fraction(7,12)"),
    n("challenge", "A cake has 2/9 eaten in the morning and 4/9 in the afternoon. What fraction of the cake remains?",
      "1/3", "The amount eaten is 2/9＋4/9＝6/9, so 1－6/9＝3/9＝1/3 remains.", "1-Fraction(2,9)-Fraction(4,9)"),
]

BANK["cnm_p173"] = [
    n("basic", "Calculate: 1/2＋1/4＝?",
      "3/4", "Use a common denominator: 2/4＋1/4＝3/4.", "Fraction(1,2)+Fraction(1,4)"),
    n("basic", "Calculate: 1/2－1/3＝?",
      "1/6", "Use a common denominator: 3/6－2/6＝1/6.", "Fraction(1,2)-Fraction(1,3)"),
    n("standard", "Wheat covers 1/2 of a field and corn covers 1/3. What fraction of the field do the two crops cover altogether?",
      "5/6", "With a common denominator, 3/6＋2/6＝5/6.", "Fraction(1,2)+Fraction(1,3)"),
    n("challenge", "A cup of juice is half-drunk, then juice equal to 1/3 of the cup's original capacity is poured in. What fraction of the original capacity is in the cup now?",
      "5/6", "After drinking, 1/2 remains; add 1/3: 1/2＋1/3＝5/6.", "1-Fraction(1,2)+Fraction(1,3)"),
]

BANK["cnm_p174"] = [
    n("basic", "Calculate: 1/2＋1/4－1/4＝?",
      "1/2", "The added 1/4 and subtracted 1/4 cancel, leaving 1/2.", "Fraction(1,2)+Fraction(1,4)-Fraction(1,4)"),
    n("basic", "Calculate: 3/4－1/4＋1/2＝?",
      "1", "3/4－1/4＝1/2, and 1/2＋1/2＝1.", "Fraction(3,4)-Fraction(1,4)+Fraction(1,2)"),
    n("standard", "A glass of water is first reduced by 1/5, then by another 2/5. What fraction of the original amount remains?",
      "2/5", "The amount used is 1/5＋2/5＝3/5, so 1－3/5＝2/5 remains.", "1-Fraction(1,5)-Fraction(2,5)"),
    n("challenge", "Wheat covers 1/2 of a field and corn covers 1/3. The rest is planted with vegetables. What fraction of the field is planted with vegetables?",
      "1/6", "1－1/2－1/3＝1/6.", "1-Fraction(1,2)-Fraction(1,3)"),
]

# ---------- Grade 5, second semester, Integrated Project ----------
BANK["cnm_p244"] = [
    n("basic", "Eight unit cubes with 1 cm edges are assembled into a larger cube. What is the larger cube's edge length in centimeters?",
      "2", "2×2×2＝8, so the larger cube has 2 cm edges.", "2"),
    n("basic", "How many unit cubes with 1 cm edges are needed to build a cuboid 4 cm long, 3 cm wide, and 2 cm high?",
      "24", "4×3×2＝24 cubes.", "4*3*2"),
    n("standard", "Two cubes with 1 cm edges are joined side by side to make a cuboid. The joined faces are hidden. What is the surface area of the cuboid in square centimeters?",
      "10", "The two cubes have 12 faces altogether; the 2 joined faces are hidden: 12－2＝10.", "6*2-2"),
    n("challenge", "Three cubes with 1 cm edges are placed in a row to form a cuboid. What is its surface area in square centimeters?",
      "14", "The cuboid is 3 cm long, 1 cm wide, and 1 cm high. Its surface area is 2×(3×1＋3×1＋1×1)＝14.",
      "2*(3*1+3*1+1*1)"),
]

BANK["cnm_p245"] = [
    n("basic", "A teacher calls 1 student to share a notice. The call takes 1 minute. How many people know the notice now, including the teacher?",
      "2", "The teacher and the 1 student both know, for a total of 2 people.", "1+1"),
    n("basic", "In the second minute, everyone who knows the notice calls 1 person who does not yet know it. How many people know the notice at the end of the second minute?",
      "4", "There were 2 people; each tells 1 more, so the number doubles: 2×2＝4.", "2*2"),
    n("standard", "A teacher needs to notify 7 students, not including the teacher. Each person can make only 1 call per minute, and informed people may continue calling. What is the minimum number of minutes needed?",
      "3", "The number of informed people can at most double each minute: 2, 4, 8. The 8 people include the teacher and cover all 7 students, so 3 minutes are needed.", "3"),
    n("challenge", "A teacher needs to notify 20 students, not including the teacher, under the same rules. What is the minimum number of minutes needed?",
      "5", "At least 21 people, including the teacher, must be informed. 2, 4, 8, and 16 are not enough; after 5 minutes, up to 32 people know.",
      "min(k for k in range(1,8) if 2**k>=21)"),
]

# ---------- Grade 5, second semester, Unit 7: Line Graphs ----------
BANK["cnm_p175"] = [
    c("basic", "What are line graphs useful for showing?",
      ["Changes in quantities", "How each part compares with the total", "Only the largest value"], "A",
      "An upward line shows an increase, and a downward line shows a decrease.", "'Changes in quantities'"),
    n("basic", "A temperature line graph shows 12 °C at 8:00 and 18 °C at 12:00. By how many degrees Celsius did the temperature rise?",
      "6", "18－12＝6 degrees Celsius.", "18-12"),
    c("standard", "A shop sells 8, 6, and 4 ice creams from Monday through Wednesday. What trend does the line graph show?",
      ["A gradual increase", "A gradual decrease", "An increase followed by a decrease", "No change"], "B",
      "Sales fall from 8 to 6 and then to 4, so the line gradually decreases.", "'A gradual decrease'"),
    n("challenge", "A line graph shows temperatures of 16 °C on Monday, 13 °C on Tuesday, and 18 °C on Wednesday. What is the difference between the highest and lowest temperatures?",
      "5", "The highest is 18 °C and the lowest is 13 °C, so the difference is 18－13＝5 degrees.", "18-13"),
]

# ---------- Grade 5, second semester, Unit 8: Math Exploration—Finding the Defective Item ----------
BANK["cnm_p176"] = [
    c("basic", "When using a balance scale to find one item that is heavier or lighter than the rest, how should the items be divided for each weighing?",
      ["Into three groups", "Weigh just one item at a time", "Weigh all items together once"], "A",
      "Divide the items into three groups; one weighing can determine which group contains the defective item.", "'Into three groups'"),
    n("basic", "One of 9 parts is heavier than the others. If the parts are divided into 3 equal groups for the first weighing, how many are in each group?",
      "3", "9÷3＝3 parts per group.", "9//3"),
    n("standard", "One of 9 parts is heavier than the others. At each step, divide the parts that may be defective into 3 groups and weigh them. What is the minimum number of weighings needed to guarantee finding the defective part?",
      "2", "The first weighing narrows it to 3 parts. A second weighing divides those into 3 groups and identifies the defective one. The minimum is 2 weighings.", "2"),
    n("challenge", "One of 27 parts is heavier than the others. If the possible defective parts are divided into 3 groups at each weighing, what is the minimum number of weighings needed to guarantee finding it?",
      "3", "One weighing narrows 27 parts to 9, a second narrows 9 to 3, and a third identifies the defective part. The minimum is 3 weighings.", "3"),
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
        return "bare integer or decimal calculation"
    if "Which is the result?" in p:
        return "asks only for the result"
    if "? Calculate:" in p or ". Calculate:" in p:
        return "prompt already gives the calculation"
    if q.get("difficulty") == "challenge" and V.CHALLENGE_BARE_CALC_RE.match(p):
        return "challenge question is only a direct calculation"
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
        raise SystemExit("Unknown topic: " + ", ".join(missing))
    g5 = [t for t in topics if t.get("grade") == 5 and str(t.get("id", "")).startswith("cnm_")
          and not t.get("external")]
    not_in_bank = [t["id"] for t in g5 if t["id"] not in BANK]
    if not_in_bank:
        raise SystemExit("Grade 5 topics without questions: " + ", ".join(not_in_bank))
    extra_topics = [tid for tid in BANK if by_id[tid].get("grade") != 5]
    if extra_topics:
        raise SystemExit("Non-Grade-5 topics would be written: " + ", ".join(extra_topics))

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
            extra.append("%s is not 2 basic + 1 standard + 1 challenge: %s" % (tid, ds))
        if raw[0]["difficulty"] != "basic" or raw[1]["difficulty"] != "basic":
            extra.append("%s: the first two questions should be basic" % tid)
        if len(raw) != 4:
            extra.append("%s: expected 4 questions" % tid)
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
    g5_qs = [q for q in out if q["topicId"] in old_ids]
    dump("_qbatches/primary_g5.json", g5_qs, 1)

    # These semester values are source-data tokens for the first and second semesters; keep them unchanged for counting.
    sem = Counter(by_id[tid]["semester"] for tid in BANK)
    print("Grade 5 topics: %d (first semester %d, second semester %d); questions: %d" % (len(BANK), sem["上"], sem["下"], len(g5_qs)))
    print("Difficulty", Counter(q["difficulty"] for q in g5_qs))
    print("Type", Counter(q["type"] for q in g5_qs))
    print("Prompts rewritten: %d / %d" % (changed, len(g5_qs)))


if __name__ == "__main__":
    main()
