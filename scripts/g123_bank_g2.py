# -*- coding: utf-8 -*-
"""Grade 2 question bank. Each topic has 2 basic, 1 standard, and 1 challenge question."""

BANK = {}

# ---------- Grade 2, first semester ----------
BANK["cnm_p037"] = [
    ("c", "basic", "Choose a sorting criterion first. When sorting buttons by shape, what must you decide first?",
     ["the sorting criterion", "the price of the buttons", "who picked them up first"], "A", "Choose a criterion first so you can sort the buttons into different groups."),
    ("n", "basic", "There are 7 red buttons and 4 blue buttons. How many groups are there when they are sorted by color?", "2",
     "The red buttons form one group and the blue buttons form another, for 2 groups in total.", "2"),
    ("n", "standard", "There are 7 red buttons and 4 blue buttons. How many more red buttons are there than blue buttons?", "3",
     "Compare the counts after sorting: 7－4＝3.", "7-4"),
    ("n", "challenge", "One pile of buttons is sorted into 2 color groups and into large, medium, and small sizes. How many groups are there when sorted by size?", "3",
     "The question asks for the number of size groups; large, medium, and small make 3 groups.", "3"),
]

BANK["cnm_p038"] = [
    ("c", "basic", "What does multiplication represent?",
     ["the sum of several equal addends", "removing part of a total", "comparing which is larger"], "A",
     "For example, 2＋2＋2 can be written as 2×3."),
    ("n", "basic", "What is the sum of three 2s?", "6", "2＋2＋2＝6, or 2×3＝6.", "2+2+2"),
    ("n", "standard", "There are 4 groups, each with 3 people. How many people are there in all?", "12",
     "Adding 3 four times gives 3×4＝12.", "3*4"),
    ("n", "challenge", "How many 4s does 4＋4＋4 represent?", "3", "The addend 4 appears 3 times, so it is three 4s.", "3"),
]

BANK["cnm_p039"] = [
    ("n", "basic", "There are 6 rows with 2 seats in each row. How many seats are there?", "12", "2×6＝12.", "2*6"),
    ("n", "basic", "There are 4 plates with 3 apples on each plate. How many apples are there in all?", "12", "3×4＝12.", "3*4"),
    ("n", "standard", "There are 6 boxes with 5 balls in each box. How many balls are there in all?", "30", "5×6＝30.", "5*6"),
    ("n", "challenge", "There are 3 rows with 4 trees in each row. Two more trees are planted nearby. How many trees are there in all?", "14",
     "First calculate 4×3＝12, then add 2 trees to get 14.", "4*3+2"),
]

BANK["cnm_p048"] = [
    ("n", "basic", "There are 6 groups with 3 people in each group. How many people are there in all?", "18", "3×6＝18 people.", "3*6"),
    ("n", "basic", "There are 4 colored pencils in each box. How many pencils are there in 5 boxes?", "20", "4×5＝20 pencils.", "4*5"),
    ("n", "standard", "There are 8 boxes with 5 eggs in each box. How many eggs are there in all?", "40", "5×8＝40 eggs.", "5*8"),
    ("n", "challenge", "There are 4 boxes with 6 erasers in each box. How many erasers are left after 5 are used?", "19",
     "There are 6×4＝24 erasers in all, so 24－5＝19 are left.", "6*4-5"),
]

BANK["cnm_p057"] = [
    ("c", "basic", "When an expression has multiplication and addition or subtraction, what order should you use?",
     ["multiply and divide first, then add and subtract", "always work from left to right, without prioritizing multiplication", "calculate the largest number first"], "A",
     "When multiplication and addition or subtraction appear together, do the multiplication first."),
    ("n", "basic", "Following the correct order, what is 3×4＋5?", "17", "First calculate 3×4＝12, then add 5 to get 17.", "3*4+5"),
    ("n", "standard", "There are 4 pens in each box. How many pens are there in 3 boxes plus 2 extra pens?", "14",
     "First calculate 4×3＝12, then add 2 to get 14.", "4*3+2"),
    ("n", "challenge", "In 20－2×6, multiply first. What is the result?", "8",
     "First calculate 2×6＝12, then 20－12＝8. Do not subtract 2 from 20 first.", "20-2*6"),
]

BANK["cnm_p043"] = [
    ("c", "basic", "What does division represent?",
     ["splitting a total equally into a given number of groups to find the amount in each group", "the sum of several equal addends", "comparing which of two numbers is larger"], "A",
     "Division is used for equal sharing and is the inverse operation of multiplication."),
    ("n", "basic", "Twelve candies are shared equally among 3 students. How many candies does each student get?", "4", "12÷3＝4 candies.", "12//3"),
    ("n", "standard", "There are 8 apples. If 2 apples go on each plate, how many plates can be filled?", "4", "8÷2＝4 plates.", "8//2"),
    ("n", "challenge", "Since 6×4＝24, how many 6s are there in 24?", "4",
     "Division is the inverse operation of multiplication, so 24÷6＝4.", "24//6"),
]

BANK["cnm_p046"] = [
    ("n", "basic", "Eighteen candies are shared equally among 3 people. How many candies does each person get?", "6", "Three groups of 6 make 18: 18÷3＝6.", "18//3"),
    ("n", "basic", "Twenty-four notebooks are divided equally into 6 groups. How many notebooks are in each group?", "4", "Four groups of 6 make 24: 24÷6＝4.", "24//6"),
    ("n", "standard", "Twenty stickers are divided equally into 4 groups. How many stickers are in each group?", "5", "20÷4＝5 stickers.", "20//4"),
    ("n", "challenge", "There are 30 balls, with 5 in each bag. Two bags have already been filled. How many more bags can be filled?", "4",
     "A total of 30÷5＝6 bags can be filled, so 6－2＝4 more bags are needed.", "30//5-2"),
]

BANK["cnm_p047"] = [
    ("n", "basic", "Lili calculates 24÷4＝6. To check by multiplication, what is the quotient 6 times the divisor 4?", "24",
     "Quotient × divisor = dividend. Since 6×4＝24, the quotient is correct.", "6*4"),
    ("c", "basic", "What should you check when verifying division with multiplication?",
     ["whether the quotient times the divisor equals the dividend", "whether the quotient plus the divisor equals the dividend", "only whether the quotient is 0"], "A",
     "To check division, use: quotient × divisor = dividend."),
    ("n", "standard", "Someone says 36÷6＝5. When checking with multiplication, what is 6×5?", "30",
     "6×5＝30, which is not 36, so the quotient 5 is incorrect.", "6*5"),
    ("n", "challenge", "Xiaohua says 42÷6＝8. Since 6×8＝48, not 42, what is the correct quotient?", "7",
     "Six times seven is forty-two: 42÷6＝7.", "42//6"),
]

BANK["cnm_p049"] = [
    ("c", "basic", "How are east and west related?", ["opposite directions", "the same direction", "both south"], "A",
     "East and west are opposites, as are north and south."),
    ("c", "basic", "How are directions usually shown on a map?",
     ["north at the top, south at the bottom, west on the left, east on the right", "south at the top, north at the bottom, east on the left, west on the right", "there is no fixed convention"], "A",
     "Maps usually show north at the top, south at the bottom, west on the left, and east on the right."),
    ("c", "standard", "Xiaoming faces east in the morning. Which direction is behind him?",
     ["east", "west", "south", "north"], "B", "If he faces east, west is behind him."),
    ("c", "challenge", "Xiaoming faces east in the morning. Which direction is to his right?",
     ["south", "north", "east", "west"], "A", "When he faces east, north is on his left and south is on his right."),
]

BANK["cnm_p040"] = [
    ("c", "basic", "About how long is 1 centimeter?",
     ["about the width of a fingernail", "about the length of a classroom", "about the length of a pencil"], "A",
     "One centimeter is very short, about the width of a fingernail."),
    ("n", "basic", "One end of a stick is aligned with 0 on a ruler and the other with 4. How many centimeters long is the stick?", "4",
     "The distance from 0 to 4 is 4 centimeters.", "4"),
    ("n", "standard", "Two sticks are 3 centimeters and 2 centimeters long. They are placed end to end. What is their total length?", "5",
     "3＋2＝5 centimeters.", "3+2"),
    ("n", "challenge", "On a ruler, one end of a stick is at 2 centimeters and the other is at 7 centimeters. How long is the stick?", "5",
     "Do not read only the 7 mark. The length is 7－2＝5 centimeters.", "7-2"),
]

BANK["cnm_p041"] = [
    ("c", "basic", "How many centimeters are in 1 meter?", ["100 centimeters", "10 centimeters", "1000 centimeters"], "A", "1 meter＝100 centimeters."),
    ("n", "basic", "How many centimeters are in 2 meters?", "200", "2×100＝200 centimeters.", "2*100"),
    ("n", "standard", "How many centimeters are in 4 meters?", "400", "4×100＝400 centimeters.", "4*100"),
    ("n", "challenge", "A flagpole is 2 meters tall and a platform is 50 centimeters long. How many centimeters taller is the flagpole? First convert 2 meters to centimeters.", "150",
     "2 meters＝200 centimeters, and 200－50＝150 centimeters.", "2*100-50"),
]

BANK["cnm_p045"] = [
    ("c", "basic", "About how long is 1 centimeter? When estimating with body measurements, what is often close to this shortest unit?",
     ["about the width of a fingernail", "about one step", "about the length of a classroom"], "A",
     "One centimeter is very short; a step is much longer than 1 centimeter."),
    ("n", "basic", "One handspan is about 10 centimeters. About how many centimeters are 3 handspans?", "30",
     "Three groups of 10 centimeters make 30 centimeters.", "3*10"),
    ("n", "standard", "A desk is about 2 handspans long. If one handspan is 10 centimeters, about how many centimeters long is the desk?", "20",
     "Two groups of 10 centimeters make 20 centimeters.", "2*10"),
    ("n", "challenge", "A rope is estimated to be about 4 handspans long, with each handspan taken as 10 centimeters. It measures 35 centimeters with a ruler. How many centimeters greater is the estimate than the measurement?", "5",
     "The estimate is 4×10＝40 centimeters, which is 5 centimeters more than 35 centimeters.", "4*10-35"),
]

BANK["cnm_p042"] = [
    ("n", "basic", "There are 8 rows with 7 seats in each row. How many seats are there?", "56", "7×8＝56.", "7*8"),
    ("n", "basic", "There are 3 boxes with 9 pens in each box. How many pens are there in all?", "27", "3×9＝27.", "9*3"),
    ("n", "standard", "There are 6 boxes with 8 notebooks in each box. How many notebooks are there in all?", "48", "8×6＝48 notebooks.", "8*6"),
    ("n", "challenge", "There are 8 rows with 7 flowers in each row. How many flowers are left after 6 are moved?", "50",
     "7×8＝56, and 56－6＝50 flowers are left.", "7*8-6"),
]

BANK["cnm_p044"] = [
    ("n", "basic", "Fifty-six balloons are divided equally into 7 groups. How many balloons are in each group?", "8", "Seven groups of 8 make 56: 56÷7＝8.", "56//7"),
    ("n", "basic", "Seventy-two pens are divided equally into 8 groups. How many pens are in each group?", "9", "Eight groups of 9 make 72: 72÷8＝9.", "72//8"),
    ("n", "standard", "Sixty-three balloons are divided equally into 9 groups. How many balloons are in each group?", "7", "63÷9＝7 balloons.", "63//9"),
    ("n", "challenge", "Forty-eight notebooks are shared equally among 8 students. Xiaoming returns one of his notebooks. How many notebooks does he have left?",
     "5", "Each student gets 48÷8＝6 notebooks; after returning 1, Xiaoming has 5 left.", "48//8-1"),
]

# ---------- Grade 2, second semester ----------
BANK["cnm_p061"] = [
    ("c", "basic", "How long does it take for the second hand to make one full turn?", ["1 minute", "1 hour", "1 second"], "A", "One full turn takes 60 seconds, or 1 minute."),
    ("n", "basic", "How many seconds are in 2 minutes?", "120", "1 minute＝60 seconds, so 2 minutes＝120 seconds.", "2*60"),
    ("n", "standard", "How many seconds are in 3 minutes?", "180", "3×60＝180 seconds.", "3*60"),
    ("n", "challenge", "The second hand has moved for 40 seconds. How many more seconds until it completes 1 minute?", "20",
     "1 minute＝60 seconds, and 60－40＝20 seconds.", "60-40"),
]

BANK["cnm_p062"] = [
    ("c", "basic", "How many minutes are in 1 hour?", ["60 minutes", "100 minutes", "24 minutes"], "A", "1 hour＝60 minutes."),
    ("n", "basic", "How many minutes are in 2 hours?", "120", "2×60＝120 minutes.", "2*60"),
    ("n", "standard", "How many seconds are in 4 minutes?", "240", "1 minute＝60 seconds, so 4 minutes＝240 seconds.", "4*60"),
    ("n", "challenge", "How many minutes are in 1 hour and 20 minutes?", "80", "1 hour＝60 minutes; add 20 minutes to get 80 minutes.", "60+20"),
]

BANK["cnm_p063"] = [
    ("n", "basic", "How many minutes pass from 3:20 to 3:35?", "15", "35－20＝15 minutes.", "35-20"),
    ("n", "basic", "How many minutes pass from 4:45 to 5:00?", "15", "There are 60－45＝15 minutes until 5:00.", "60-45"),
    ("n", "standard", "A movie starts at 7:15 and ends at 7:50. How many minutes long is it?", "35", "50－15＝35 minutes.", "50-15"),
    ("n", "challenge", "How many minutes pass from 3:50 to 4:10?", "20",
     "It takes 10 minutes to reach 4:00, then another 10 minutes, for 20 minutes in all.", "60-50+10"),
]

BANK["cnm_p050"] = [
    ("c", "basic", "In division with a remainder, which is smaller: the remainder or the divisor?",
     ["the remainder is smaller than the divisor", "the remainder is larger than the divisor", "the remainder is always 0"], "A",
     "If the remainder is not smaller than the divisor, another group can still be made."),
    ("n", "basic", "There are 13 candies, with 5 in each bag. Give the quotient first, then the remainder.", "2，3",
     "13÷5＝2 bags, remainder 3; the remainder 3 is less than the divisor 5.", "(13//5, 13%5)"),
    ("n", "standard", "There are 17 notebooks, with 3 in each bundle. Give the quotient first, then the remainder.", "5，2",
     "17÷3＝5 bundles, remainder 2.", "(17//3, 17%3)"),
    ("c", "challenge", "The remainder of 20÷6 is written as 8. Why is this incorrect?",
     ["the remainder must be smaller than the divisor", "the quotient must be 0", "the remainder must be larger than the quotient"], "A",
     "6×2＝12 and 20－12＝8. Since 8 is greater than the divisor 6, another group can be made. The correct remainder is 2."),
]

BANK["cnm_p051"] = [
    ("n", "basic", "There are 14 candies, with 4 in each bag. Give the quotient first, then the remainder.", "3，2",
     "4×3＝12 and 14－12＝2, so the quotient is 3 and the remainder is 2.", "(14//4, 14%4)"),
    ("n", "basic", "There are 25 apples, with 7 in each bag. Give the quotient first, then the remainder.", "3，4",
     "7×3＝21 and 25－21＝4, so the quotient is 3 and the remainder is 4.", "(25//7, 25%7)"),
    ("n", "standard", "There are 30 apples, with 8 in each bag. Give the quotient first, then the remainder.", "3，6",
     "8×3＝24 and 30－24＝6.", "(30//8, 30%8)"),
    ("n", "challenge", "For 47÷7, use 7×6＝42 to find the remainder.", "5",
     "The quotient is 6 and the remainder is 47－42＝5, which is less than 7.", "47%7"),
]

BANK["cnm_p052"] = [
    ("n", "basic", "There are 23 balls, with 5 in each bag. Give the quotient first, then the remainder.", "4，3",
     "23÷5＝4 bags, remainder 3.", "(23//5, 23%5)"),
    ("n", "basic", "Nineteen people line up in rows of 4. Give the number of full rows first, then the number of people left over.", "4，3",
     "19÷4＝4 rows, remainder 3 people.", "(19//4, 19%4)"),
    ("n", "standard", "Twenty-eight people rent boats that hold 6 people each. How many people are left who cannot fill another boat?", "4",
     "28÷6＝4 boats, remainder 4 people.", "28%6"),
    ("n", "challenge", "There are 23 balls, with 5 in each bag, and 3 balls are left after filling the bags. How many more balls are needed to fill one more bag?", "2",
     "There are 5－3＝2 balls missing.", "5-3"),
]

BANK["cnm_p219"] = [
    ("n", "basic", "There are 4 boxes with 6 eggs in each box. How many eggs are there in all?", "24", "Amount per group × number of groups = total: 6×4＝24.", "6*4"),
    ("n", "basic", "Eighteen apples are shared equally among 3 children. How many apples does each child get?", "6", "Total ÷ number of groups = amount per group: 18÷3＝6.", "18//3"),
    ("n", "standard", "There are 35 balloons, with 5 tied in each bunch. How many bunches can be made?", "7", "Total ÷ amount per group = number of groups: 35÷5＝7.", "35//5"),
    ("n", "challenge", "There are 4 boxes with 6 eggs in each box. How many eggs are left after 5 are eaten?", "19",
     "First find the total, 6×4＝24, then subtract 5 to get 19.", "6*4-5"),
]

BANK["cnm_p053"] = [
    ("n", "basic", "What number comes after 999?", "1000", "Adding 1 to 999 gives 1000.", "999+1"),
    ("n", "basic", "What number comes before 1000?", "999", "The number before 1000 is 999.", "1000-1"),
    ("n", "standard", "What digit is in the hundreds place in 3400?", "4", "From right to left, the places are ones, tens, and hundreds; the hundreds digit in 3400 is 4.", "4"),
    ("n", "challenge", "What digit is in the thousands place in 5060?", "5", "5060 has 5 thousands, 0 hundreds, 6 tens, and 0 ones, so the thousands digit is 5.", "5"),
]

BANK["cnm_p054"] = [
    ("c", "basic", "Which is greater, 999 or 1000?", ["1000", "999", "they are equal"], "A",
     "1000 has four digits and 999 has three; a number with more digits is greater."),
    ("n", "basic", "Which is the greater number, 3200 or 999?", "3200",
     "3200 has four digits and 999 has three, so 3200 is greater.", "3200"),
    ("c", "standard", "Which of these four numbers is the greatest?", ["3986", "4012", "4001", "998"], "B",
     "4012 and 4001 both have four digits and the same thousands digit; comparing the hundreds digits shows that 4012 is greater. 998 has only three digits."),
    ("n", "challenge", "What is the greatest number among 989, 1001, 999, and 1100?", "1100",
     "1100 has 1 thousand and 1 hundred, so it is greater than 1001.", "1100"),
]

BANK["cnm_p055"] = [
    ("n", "basic", "How many hundreds are in 2300?", "23", "2300＝23 hundreds.", "2300//100"),
    ("n", "basic", "How many thousands are in 4000?", "4", "4000＝4 thousands.", "4000//1000"),
    ("n", "standard", "What digit is in the hundreds place in 1600?", "6", "1600 has 1 thousand and 6 hundreds, so the hundreds digit is 6.", "6"),
    ("n", "challenge", "What number is made from 3 thousands and 5 tens?", "3050",
     "3 thousands make 3000 and 5 tens make 50; together they make 3050.", "3000+50"),
]

BANK["cnm_p064"] = [
    ("n", "basic", "A library receives 300 books in one delivery and 400 in another. How many books are there in the two deliveries altogether?", "700",
     "3 hundreds plus 4 hundreds make 7 hundreds, or 700.", "300+400"),
    ("n", "basic", "There are 250 storybooks, and 30 more are added. How many are there now?", "280", "250＋30＝280.", "250+30"),
    ("n", "standard", "One box has 180 books and another has 140. How many books are in the two boxes altogether?", "320", "180＋140＝320.", "180+140"),
    ("n", "challenge", "One box has 180 books and another has 140. Then 50 more books arrive. How many are there now?", "370",
     "180＋140＝320, then add 50 to get 370.", "180+140+50"),
]

BANK["cnm_p065"] = [
    ("n", "basic", "There are 800 books on a shelf. How many are left after 300 are moved?", "500", "800－300＝500.", "800-300"),
    ("n", "basic", "There are 560 books, and 40 are borrowed. How many are left?", "520", "560－40＝520.", "560-40"),
    ("n", "standard", "A library has 730 books, and 280 are borrowed. How many are left?", "450", "730－280＝450.", "730-280"),
    ("n", "challenge", "A library has 730 books. After 280 are borrowed, 50 are returned. How many books are there now?", "500",
     "730－280＝450, then add 50 to get 500.", "730-280+50"),
]

BANK["cnm_p066"] = [
    ("c", "basic", "What is the purpose of estimating?",
     ["to quickly find about how much something is", "to always calculate the exact answer", "to use only with subtraction"], "A",
     "Estimation rounds numbers to the nearest ten or hundred to find an approximate result."),
    ("n", "basic", "When estimating 198＋102, what should 198 be rounded to?", "200", "198 is close to 200.", "200"),
    ("n", "standard", "A shirt costs 198 yuan and a hat costs 102 yuan. If their prices are rounded to 200 yuan and 100 yuan, about how much do they cost altogether?", "300",
     "200＋100＝300.", "200+100"),
    ("n", "challenge", "For 43＋28, round 43 to 40 and 28 to 30 to estimate 70. The exact sum is 71. How much less is the estimate than the exact sum?", "1",
     "71－70＝1.", "43+28-(40+30)"),
]

BANK["cnm_p071"] = [
    ("n", "basic", "Two warehouses have 234 boxes and 125 boxes, respectively. How many boxes are there altogether?", "359", "234＋125＝359.", "234+125"),
    ("n", "basic", "What is 406 boxes plus 270 boxes?", "676", "406＋270＝676.", "406+270"),
    ("n", "standard", "Two warehouses have 368 boxes and 475 boxes, respectively. How many boxes are there altogether?", "843",
     "Regroup from the ones and tens places: 368＋475＝843.", "368+475"),
    ("n", "challenge", "For 498＋357, regroup in both the ones and tens places. What is the sum?", "855",
     "In the ones place, 8＋7＝15; in the tens place, 9＋5＋1＝15; in the hundreds place, 4＋3＋1＝8. The sum is 855.", "498+357"),
]

BANK["cnm_p072"] = [
    ("n", "basic", "There are 756 books on a shelf. How many are left after 234 are moved?", "522", "756－234＝522.", "756-234"),
    ("n", "basic", "There are 600 books on a shelf. How many are left after 248 are moved?", "352",
     "Regroup in both the ones and tens places: 600－248＝352.", "600-248"),
    ("n", "standard", "In 803－457, there is a 0 in the middle, so regrouping must continue across places. What is the difference?", "346", "803－457＝346.", "803-457"),
    ("n", "challenge", "In 702－468, the tens digit is 0, so regrouping must continue across places. What is the difference?", "234",
     "After regrouping in the ones place, regroup from the hundreds place through the 0 in the tens place: 702－468＝234.", "702-468"),
]

BANK["cnm_p220"] = [
    ("n", "basic", "□＋250＝600. What is □?", "350", "Addend = sum − other addend: 600－250＝350.", "600-250"),
    ("n", "basic", "□－180＝320. What is □?", "500", "Minuend = difference + subtrahend: 320＋180＝500.", "320+180"),
    ("n", "standard", "760－□＝430. What is □?", "330", "Subtrahend = minuend − difference: 760－430＝330.", "760-430"),
    ("n", "challenge", "The sum is 600, and one addend is 250. How much remains after subtracting 40 from the other addend?", "310",
     "The other addend is 600－250＝350; subtracting 40 leaves 310.", "600-250-40"),
]

BANK["cnm_p060"] = [
    ("n", "basic", "A sequence is 2, 5, 8. The amount added each time is the same. What comes after 8?", "11",
     "Add 3 each time: 8＋3＝11.", "8+3"),
    ("n", "basic", "A sequence is 16, 14, 12. The amount subtracted each time is the same. What comes after 12?", "10",
     "Subtract 2 each time: 12－2＝10.", "12-2"),
    ("n", "standard", "A sequence is 3, 6, 9, 12. What comes after 12 if the pattern continues?", "15",
     "Add 3 each time: 12＋3＝15.", "12+3"),
    ("n", "challenge", "A sequence is 2, 5, 8, 11, 14. What comes after 14 if the pattern continues?", "17",
     "Add 3 each time: 14＋3＝17.", "14+3"),
]
