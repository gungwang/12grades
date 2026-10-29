# -*- coding: utf-8 -*-
"""Grade 1 question bank. Each topic has 2 basic, 1 standard, and 1 challenge question. The final field, when present, reuses the image from the original question."""

BANK = {}

# ---------- Grade 1, first semester ----------
BANK["cnm_p001"] = [
    ("n", "basic", "What number comes after 3?", "4", "Counting forward from 1, the number after 3 is 4.", "3+1"),
    ("n", "basic", "What number comes before 4?", "3", "The number before 4 is 3.", "4-1"),
    ("n", "standard", "What number comes before 5?", "4", "The number just before 5 is 4.", "5-1"),
    ("n", "challenge", "Xiaoming counts 1, 2, 3, 5. Which number did he skip?", "4", "Counting one by one from 1 to 5, the number between 3 and 5 is 4.", "3+1"),
]

BANK["cnm_p002"] = [
    ("c", "basic", "Which number is greater, 4 or 2?", ["4", "2", "They are equal"], "A", "4 comes after 2 in the number sequence, so 4 is greater."),
    ("n", "basic", "How much greater is 5 than 3?", "2", "Counting from 3 to 5, we find that 5 is 2 greater than 3.", "5-3"),
    ("c", "standard", "There are 4 apples on a plate and 2 pears in a bowl. Which fruit is there more of?",
     ["More apples", "More pears", "The same number", "Cannot compare"], "A", "4 is greater than 2, so there are more apples."),
    ("n", "challenge", "The numbers greater than 1 and less than 4 are 2 and 3. Which is greater?", "3",
     "Both 2 and 3 are between 1 and 4, and 3 is greater than 2.", "3"),
]

BANK["cnm_p003"] = [
    ("c", "basic", "Counting from the left, what is the position of the person at the very front?", ["First", "Fifth", "There are 5 people"], "A",
     "A position is counted starting from 1, so the person at the front is first."),
    ("n", "basic", "Five children stand in a line. Counting from the left, Xiaoming is third. How many children are in front of him?", "2",
     "The first and second children are in front of the third, so there are 2. A count of people is different from a position.", "3-1"),
    ("n", "standard", "Five children stand in a line. Xiaohua is fifth, and Xiaoli is one place in front of Xiaohua. What is Xiaoli's position?", "4",
     "Xiaohua is fifth, so the place just before hers is fourth.", "5-1"),
    ("n", "challenge", "Counting from the left, Xiaohong is second; counting from the right, she is third. How many people are in the line?", "4",
     "There are 2 people on the left including Xiaohong and 3 on the right including her. Count her only once: 2+3−1=4.", "2+3-1"),
]

BANK["cnm_p004"] = [
    ("n", "basic", "5 can be split into 2 and what number?", "3", "2 and 3 make 5.", "5-2"),
    ("n", "basic", "What is 1 plus 4?", "5", "1+4=5.", "1+4"),
    ("n", "standard", "4 can be split into 1 and what number?", "3", "1 and 3 make 4.", "4-1"),
    ("n", "challenge", "Split 4 into two equal parts. How much is each part?", "2", "2 and 2 make 4, so each part is 2.", "4-2"),
]

BANK["cnm_p005"] = [
    ("c", "basic", "0 means none. If there are no apples on a plate, which number represents this?", ["0", "1", "5"], "A",
     "Use 0 to represent none."),
    ("n", "basic", "There are 3 balloons, and they all fly away. How many are left?", "0", "All 3 flew away, so none are left: 0.", "3-3"),
    ("n", "standard", "A box is empty. Then 4 balls are put in it. How many balls are there now?", "4", "Starting with 0 and adding 4 gives 4.", "0+4"),
    ("n", "challenge", "What number comes after 0?", "1", "Adding 1 to 0 gives 1, so the number after 0 is 1.", "0+1"),
]

BANK["cnm_p006"] = [
    ("n", "basic", "There are 2 flowers, and 1 more is added. How many flowers are there in all?", "3", "2+1=3 flowers.", "2+1"),
    ("n", "basic", "There is 1 apple on the left and 3 apples on the right. How many apples are there in all?", "4", "1+3=4 apples.", "1+3"),
    ("n", "standard", "There are 2 birds in a tree, and 2 more fly in. How many birds are there now?", "4", "2+2=4 birds.", "2+2"),
    ("n", "challenge", "Xiaoming has 2 apples, Xiaohong has 1 apple, and there are also 3 pencils on the table. How many apples are there in all?", "3",
     "Add only the apples: 2+1=3. Pencils are not apples, so do not include them.", "2+1"),
]

BANK["cnm_p007"] = [
    ("n", "basic", "There are 5 balloons, and 2 are taken away. How many are left?", "3", "5−2=3 balloons.", "5-2"),
    ("n", "basic", "There are 4 pens, and 1 is given away. How many are left?", "3", "4−1=3 pens.", "4-1"),
    ("n", "standard", "There are 5 candies, and 3 are eaten. How many are left?", "2", "5−3=2 candies.", "5-3"),
    ("n", "challenge", "There are 4 peaches and 2 pears on a plate. One peach is eaten. How many peaches are left?", "3",
     "Count only the peaches: 4−1=3. The pears are not part of this subtraction.", "4-1"),
]

BANK["cnm_p008"] = [
    ("n", "basic", "What number comes after 9?", "10", "Adding 1 to 9 gives 10.", "9+1"),
    ("n", "basic", "What number comes before 8?", "7", "The number before 8 is 7.", "8-1"),
    ("n", "standard", "How many ones make 10?", "10", "10 contains 10 ones.", "10"),
    ("n", "challenge", "Count from 6 to 10. How many numbers are there: 6, 7, 8, 9, and 10?", "5",
     "Count both 6 and 10: there are 5 numbers from 6 to 10.", "10-6+1"),
]

BANK["cnm_p009"] = [
    ("c", "basic", "Which number is greater than 7 and less than 9?", ["6", "7", "8", "9"], "C", "8 is between 7 and 9."),
    ("n", "basic", "How much greater is 10 than 8?", "2", "10−8=2, so 10 is 2 greater than 8.", "10-8"),
    ("n", "standard", "One string has 10 beads and another has 6. How many more beads are on the first string?", "4",
     "Compare the number of beads: 10−6=4.", "10-6"),
    ("n", "challenge", "Which is the smallest of these four numbers: 9, 5, 8, and 6?", "5",
     "Look for the number that comes first. 5 is less than 6, 8, and 9.", "5"),
]

BANK["cnm_p010"] = [
    ("n", "basic", "There are 6 pencils, and 3 more are added. How many pencils are there in all?", "9", "6+3=9 pencils.", "6+3"),
    ("n", "basic", "There are 7 balls, and 2 more are brought over. How many balls are there in all?", "9", "7+2=9 balls.", "7+2"),
    ("n", "standard", "There are 4 ducks in a pond, and 5 more swim over. How many ducks are there now?", "9", "4+5=9 ducks.", "4+5"),
    ("n", "challenge", "There are 4 red flowers, 3 yellow flowers, and 5 leaves nearby. How many flowers are there in all?", "7",
     "There are 4+3=7 flowers. Leaves are not flowers.", "4+3"),
]

BANK["cnm_p011"] = [
    ("n", "basic", "There are 10 candies, and 3 are taken away. How many are left?", "7", "10−3=7 candies.", "10-3"),
    ("n", "basic", "Four of 9 balloons fly away. How many are left?", "5", "9−4=5 balloons.", "9-4"),
    ("n", "standard", "There are 8 pens, and 2 are lent out. How many are left?", "6", "8−2=6 pens.", "8-2"),
    ("n", "challenge", "There are 10 pieces of fruit in all. Three are pears and the rest are apples. How many apples are there?", "7",
     "Subtract the pears from the total: 10−3=7 apples.", "10-3"),
]

BANK["cnm_p012"] = [
    ("n", "basic", "There are 2 birds, then 3 more fly in, followed by 4 more. How many birds are there now?", "9",
     "For repeated addition, work from left to right: 2+3=5, then 5+4=9.", "2+3+4"),
    ("n", "basic", "There are 9 cookies. Two are eaten, then 3 more are eaten. How many are left?", "4",
     "For repeated subtraction, work from left to right: 9−2=7, then 7−3=4.", "9-2-3"),
    ("n", "standard", "One bird lands in a tree, then 6 more fly in, followed by 2 more. How many birds are there now?", "9",
     "1+6=7, then 7+2=9.", "1+6+2"),
    ("n", "challenge", "There are 10 beads. First 2 are taken away, then 3, and finally 1 more. How many remain?", "4",
     "10−2=8, 8−3=5, and 5−1=4.", "10-2-3-1"),
]

BANK["cnm_p013"] = [
    ("n", "basic", "There are 5 pens. Three more are bought, then 2 are given away. How many are left?", "6",
     "Work from left to right: 5+3=8, then 8−2=6.", "5+3-2"),
    ("n", "basic", "There are 8 apples. Three are eaten, then 2 more are bought. How many apples are there now?", "7",
     "8−3=5, then 5+2=7.", "8-3+2"),
    ("n", "standard", "Four students are reading. Five more arrive, then 6 leave. How many students are there now?", "3",
     "4+5=9, then 9−6=3.", "4+5-6"),
    ("n", "challenge", "There are 6 cars in a parking lot. Two leave, 4 arrive, and then 1 more leaves. How many cars are there now?", "7",
     "6−2=4, 4+4=8, and 8−1=7.", "6-2+4-1"),
]

BANK["cnm_p014"] = [
    ("c", "basic", "Which of these is a rectangular prism? A block box is often this shape.",
     ["Rectangular prism", "Sphere", "Cylinder"], "A", "A rectangular prism has flat faces, and opposite faces are equal.", None, "cnm_p014_q1"),
    ("c", "basic", "Which of these is a cylinder? A tea can is often this shape.",
     ["Sphere", "Cylinder", "Rectangular prism"], "B", "A cylinder has the same width at the top and bottom and a curved side.", None, "cnm_p014_q2"),
    ("c", "standard", "A sphere rolls easily. Which of these rolls most easily?",
     ["Sphere", "Rectangular prism", "Cube"], "A", "A sphere has no flat faces, so it rolls most easily.", None, "cnm_p014_q3"),
    ("c", "challenge", "Which of these—a sphere, cylinder, or cube—has no flat faces and rolls no matter how it is placed?",
     ["Sphere", "Cylinder", "Cube"], "A", "A sphere has no flat faces. A cylinder can stand upright, and a cube has flat faces."),
]

BANK["cnm_p015"] = [
    ("c", "basic", "Stand facing the board. What do you call the side directly in front of you?", ["Front", "Back", "Left"], "A",
     "The side directly in front of you is the front."),
    ("c", "basic", "Stand facing the board. What do you call the side next to your left hand?", ["Left", "Right", "Back"], "A",
     "The side next to your left hand is the left; the side next to your right hand is the right."),
    ("c", "standard", "Xiaohong is in front of Xiaoming. Who is behind Xiaohong?", ["Xiaoming", "Xiaohong", "Cannot tell"], "A",
     "Xiaohong is in front of Xiaoming, so Xiaoming is behind Xiaohong."),
    ("c", "challenge", "Xiaohong is in front of Xiaoming, and Xiaogang is in front of Xiaohong. Who is at the very front?",
     ["Xiaogang", "Xiaoming", "Xiaohong"], "A", "Xiaogang is in front of Xiaohong, who is in front of Xiaoming, so Xiaogang is at the front."),
]

BANK["cnm_p016"] = [
    ("n", "basic", "What number comes after 19?", "20", "Adding 1 to 19 gives 20.", "19+1"),
    ("n", "basic", "What number comes before 11?", "10", "The number before 11 is 10.", "11-1"),
    ("n", "standard", "14 is 1 ten and how many ones?", "4", "14 is 1 ten and 4 ones.", "4"),
    ("n", "challenge", "Count from 15 to 20. How many numbers are there: 15, 16, 17, 18, 19, and 20?", "6",
     "Count both endpoints: 20−15+1=6.", "20-15+1"),
]

BANK["cnm_p017"] = [
    ("n", "basic", "What is the tens digit of 17?", "1", "The tens digit of 17 is 1, representing 1 ten.", "1"),
    ("n", "basic", "What is the ones digit of 17?", "7", "The ones digit of 17 is 7, representing 7 ones.", "7"),
    ("n", "standard", "The tens digit is 1 and the ones digit is 8. What is the two-digit number?", "18", "1 ten and 8 ones make 18.", "10+8"),
    ("n", "challenge", "A two-digit number has a tens digit of 1, and its ones digit is 6 greater than its tens digit. What is the number?", "17",
     "The tens digit is 1, and the ones digit is 1+6=7, so the number is 17.", "10+7"),
]

BANK["cnm_p018"] = [
    ("n", "basic", "There are 12 colored pencils, and 3 more are brought over. How many are there in all?", "15",
     "The ones add to 2+3=5, while the tens digit stays 1, giving 15.", "12+3"),
    ("n", "basic", "There are 10 students on the playground, and 7 more arrive. How many students are there now?", "17", "10+7=17.", "10+7"),
    ("n", "standard", "There are 11 books on a shelf, and 4 more are placed on it. How many books are there in all?", "15",
     "For 11+4, the ones add to less than 10: 1+4=5, so the sum is 15.", "11+4"),
    ("n", "challenge", "A number is 1 ten and 4 ones. Add 5; the ones do not make 10. What is the sum?", "19",
     "The number is 14. 14+5=19; the ones add to 4+5=9, so there is no carry.", "14+5"),
]

BANK["cnm_p019"] = [
    ("c", "basic", "When using the make-ten method to calculate 9+3, how should you split 3?",
     ["1 and 2", "3 and 0", "2 and 3"], "A",
     "9+1=10, so split 3 into 1 and 2."),
    ("n", "basic", "What do you get when you add 1 to 9 to make ten?", "10", "The first step in making ten is 9+1=10.", "9+1"),
    ("n", "standard", "There are 9 candies in a box, and 4 more are added. First make ten. How many candies are there in all?", "13",
     "Split 4 into 1 and 3: 9+1=10, then add 3 to get 13.", "9+4"),
    ("n", "challenge", "To calculate 8+5, split 5 into 2 and 3, then calculate 8+2 first. What is the sum?", "13",
     "8+2=10, then add 3 to get 13.", "8+5"),
]

BANK["cnm_p020"] = [
    ("n", "basic", "There are 9 stickers, and 2 more are added. How many stickers are there in all?", "11", "9+1=10, then add 1 more to get 11.", "9+2"),
    ("n", "basic", "There are 9 balls, and 5 more are brought over. How many balls are there in all?", "14", "9+1=10, then add 4 to get 14.", "9+5"),
    ("n", "standard", "There are 9 cars in a parking lot, and 4 more arrive. How many cars are there now?", "13", "9+4=13.", "9+4"),
    ("n", "challenge", "For 9+7, first split 7 into 1 and 6. Make ten, then add 6. What is the sum?", "16",
     "9+1=10, and 10+6=16.", "9+7"),
]

BANK["cnm_p021"] = [
    ("n", "basic", "There are 8 apples, and 3 more are brought over. How many apples are there in all?", "11", "8+2=10, then add 1 to get 11.", "8+3"),
    ("n", "basic", "There are 7 pens, and 5 more are bought. How many pens are there in all?", "12", "7+3=10, then add 2 to get 12.", "7+5"),
    ("n", "standard", "There are 6 balls, and 6 more are added. How many are there in all?", "12", "6+4=10, then add 2 to get 12.", "6+6"),
    ("n", "challenge", "For 8+7, split 7 into 2 and 5, then make ten first. What is the sum?", "15",
     "8+2=10, and 10+5=15.", "8+7"),
]

BANK["cnm_p251"] = [
    ("n", "basic", "There are 4 red balls and 9 blue balls. How many balls are there in all?", "13",
     "Rewrite it as 9+4. 9+1=10, then add 3 to get 13.", "4+9"),
    ("n", "basic", "There are 5 pens, and 7 more are added. How many pens are there in all?", "12",
     "Rewrite it as 7+5. 7+3=10, then add 2 to get 12.", "5+7"),
    ("c", "standard", "To calculate 3+9, first rewrite it as 9+3. How much must be added to 9 to make 10?", ["2", "1", "3", "10"], "B",
     "9+1=10, so add 1."),
    ("n", "challenge", "For 2+9, split 2 into 1 and 1. Add 1 to 9 to make 10, then add the remaining 1. What is the sum?", "11",
     "9+1=10, and 10+1=11.", "2+9"),
]

BANK["cnm_p252"] = [
    ("n", "basic", "9+□=15. What number belongs in the box?", "6", "Ask what must be added to 9 to make 15. 9+6=15, so write 6 in the box.", "15-9"),
    ("n", "basic", "□+8=13. What number belongs in the box?", "5", "Ask what plus 8 equals 13. 5+8=13.", "13-8"),
    ("n", "standard", "There are 8 cars in a parking lot. How many more must arrive to make 14?", "6",
     "Solve 8+□=14; the missing number is 6.", "14-8"),
    ("c", "challenge", "Xiaoming has 9 books and wants 16. Which way of thinking is correct?",
     ["Ask what must be added to 9 to make 16", "Add 9 to 16", "Subtract 16 from 9"], "A",
     "Given one part and the total, ask what must be added to the part to make the total."),
]

BANK["cnm_p253"] = [
    ("n", "basic", "There are 6 birds in a tree, and 3 more fly in. How many birds are there now?", "9", "When more arrive, add: 6+3=9.", "6+3"),
    ("n", "basic", "There are 9 apples on a plate, and 4 are eaten. How many are left?", "5", "When some are eaten, subtract: 9−4=5.", "9-4"),
    ("c", "standard", "There are 7 peaches, and 2 are eaten. How should you calculate how many remain?",
     ["7 plus 2", "7 minus 2", "2 minus 7"], "B", "Take 2 away from 7: use 7−2."),
    ("n", "challenge", "There are 8 peaches and 3 pears. Two peaches are eaten. How many peaches are left?", "6",
     "The question asks how many peaches remain, so calculate only 8−2=6. Do not include the pears.", "8-2"),
]

BANK["cnm_p022"] = [
    ("c", "basic", "Classification starts with a rule. What should you decide before sorting pencils by color?",
     ["The sorting rule", "How many pencils there are in all", "Which pencil is longest"], "A", "Decide what rule to use before sorting items into different groups."),
    ("n", "basic", "A set of shapes contains triangles, circles, and rectangles. How many groups are there when sorting by shape?", "3",
     "Each shape type is one group, so there are 3 groups.", "3"),
    ("c", "standard", "There are apples, bananas, and a ball together. When sorting by “whether it is fruit,” which group should the ball go in?",
     ["Not fruit", "Fruit", "The same group as apples"], "A", "A ball is not fruit, so put it in the “not fruit” group."),
    ("n", "challenge", "There are 4 triangles and 3 circles. After sorting by shape, how many shapes are in the triangle group?", "4",
     "The question asks for the triangle group, which has 4 shapes. Do not include the circles.", "4"),
]

BANK["cnm_p254"] = [
    ("c", "basic", "Which of these—a sphere, cylinder, rectangular prism, or cube—rolls no matter how it is placed?",
     ["Rectangular prism", "Cube", "Sphere", "Cylinder"], "C", "A sphere has no flat faces, so it rolls in any position."),
    ("c", "basic", "Can a rectangular prism rest steadily on top of a sphere?",
     ["Yes, it will always be stable", "No, the sphere will roll", "Yes, if you place it quickly"], "B", "The sphere's surface is curved, so the rectangular prism will not rest steadily."),
    ("c", "standard", "To build a tall, stable tower, which blocks should you stack?",
     ["Rectangular prisms and cubes", "Spheres and spheres", "Spheres and cylinders"], "A", "Rectangular prisms and cubes have flat faces, so they can be stacked securely."),
    ("c", "challenge", "A cylinder rolls easily when it lies on its side. How should you place it to use it as a stable base?",
     ["Stand it upright", "Lay it on its side", "Let it roll"], "A", "When upright, a cylinder has flat top and bottom faces, making a stable base."),
]

# ---------- Grade 1, second semester ----------
BANK["cnm_p023"] = [
    ("c", "basic", "Which of these is a triangle?", ["Triangle", "Circle", "Rectangle"], "A",
     "A triangle has 3 sides and 3 angles.", None, "cnm_p023_q1"),
    ("c", "basic", "Which of these is a square?", ["Rectangle", "Square", "Triangle"], "B",
     "All four sides of a square are equal.", None, "cnm_p023_q2"),
    ("c", "standard", "How many sides does a rectangle have?", ["3", "4", "None"], "B",
     "A rectangle has 4 sides.", None, "cnm_p023_q3"),
    ("c", "challenge", "What is true about the four sides of a square?", ["All four sides are equal", "It has only three sides", "It has no angles"], "A",
     "All four sides of a square are equal, and it has 4 angles.", None, "cnm_p023_q4"),
]

BANK["cnm_p024"] = [
    ("c", "basic", "Two identical triangles can sometimes be joined to make a quadrilateral. Which shape is used to make it?",
     ["Triangle", "Circle", "Sphere"], "A", "The shape used before joining them is a triangle."),
    ("n", "basic", "A small house picture uses 1 square for the walls and 1 triangle for the roof. How many different shapes are used?", "2",
     "The square and triangle are 2 different shapes.", "2"),
    ("n", "standard", "How many triangles can you get by cutting a rectangle along a diagonal?", "2",
     "A rectangle can be cut into 2 triangles.", "2"),
    ("n", "challenge", "Use 4 identical small squares to make a large square. How many small-square sides make up each side of the large square?", "2",
     "Two small squares sit side by side, so each large side is made of 2 small sides.", "2"),
]

BANK["cnm_p025"] = [
    ("c", "basic", "The break-ten method splits a teen number into 10 and some ones. For 13−9, what is 13 split into?",
     ["10 and 3", "10 and 4", "10 and 9"], "A", "13 is 10 and 3, so split it into 10 and 3."),
    ("n", "basic", "There are 12 pens, and 9 are used. How many are left?", "3",
     "Since 9+3=12, 12−9=3. You can also calculate 10−9=1, then add 2.", "12-9"),
    ("n", "standard", "There are 15 pens, and 9 are used. How many are left?", "6", "Since 9+6=15, 15−9=6.", "15-9"),
    ("n", "challenge", "Use the break-ten method for 13−9: calculate 10−9=1, then add 3. What is the result?", "4",
     "1+3=4, so 13−9=4.", "13-9"),
]

BANK["cnm_p026"] = [
    ("n", "basic", "There are 14 balls, and 8 are taken away. How many are left?", "6", "Since 8+6=14, 14−8=6.", "14-8"),
    ("n", "basic", "There are 13 candies, and 7 are eaten. How many are left?", "6", "Since 7+6=13, 13−7=6.", "13-7"),
    ("n", "standard", "There are 15 small balls, and 6 are taken away. How many remain?", "9", "15−6=9.", "15-6"),
    ("n", "challenge", "For 12−8, first calculate 10−8=2, then add the 2 ones. What is the result?", "4",
     "2+2=4, so 12−8=4.", "12-8"),
]

BANK["cnm_p027"] = [
    ("n", "basic", "There are 13 candies, and 5 are taken away. How many are left?", "8", "13−5=8.", "13-5"),
    ("n", "basic", "There are 16 pens, and 4 are given away. How many are left?", "12", "16−4=12.", "16-4"),
    ("n", "standard", "There are 12 buttons, and 3 are taken away. How many remain?", "9", "12−3=9.", "12-3"),
    ("n", "challenge", "Two of 11 balloons fly away, then 0 more fly away. How many are left?", "9",
     "11−2=9. The extra 0 balloons do not change the result.", "11-2"),
]

BANK["cnm_p028"] = [
    ("n", "basic", "What number comes after 39?", "40", "Adding 1 to 39 gives 40.", "39+1"),
    ("n", "basic", "What number comes before 50?", "49", "The number before 50 is 49.", "50-1"),
    ("n", "standard", "The tens digit is 4 and the ones digit is 6. What is the two-digit number?", "46", "4 tens and 6 ones make 46.", "40+6"),
    ("n", "challenge", "What number is between 39 and 41?", "40", "40 comes after 39 and before 41.", "39+1"),
]

BANK["cnm_p029"] = [
    ("c", "basic", "Which is the greatest of these numbers: 47, 74, 39, and 58?", ["47", "74", "39", "58"], "B",
     "The tens digit 7 is the greatest, so 74 is greatest."),
    ("n", "basic", "How much greater is 40 than 20?", "20", "Compare the tens: 4 tens is 20 more than 2 tens.", "40-20"),
    ("n", "standard", "Xiaohua bounces a ball 28 times, and Xiaoli bounces it 20 times. How many more times does Xiaohua bounce it?", "8",
     "The tens digits match, so compare the ones: 28−20=8.", "28-20"),
    ("n", "challenge", "Which is the smallest of 28, 32, 19, and 30?", "19",
     "Compare the tens digits first. The tens digit of 19 is 1, which is less than 2 and 3.", "19"),
]

BANK["cnm_p030"] = [
    ("n", "basic", "There are 3 bundles of sticks and 2 more bundles, with 10 sticks in each bundle. How many sticks are there in all?", "50",
     "3 tens plus 2 tens is 5 tens, or 50.", "30+20"),
    ("n", "basic", "Take away 2 tens from 5 tens. How many are left?", "30", "50−20=30.", "50-20"),
    ("n", "standard", "There are 4 bundles of sticks with 10 sticks each, plus 8 loose sticks. How many sticks are there in all?", "48",
     "40+8=48.", "40+8"),
    ("n", "challenge", "There are 70 sticks. Forty are taken away, then 8 loose sticks are added. How many are there now?", "38",
     "70−40=30, then add 8 to get 38.", "70-40+8"),
]

BANK["cnm_p031"] = [
    ("c", "basic", "When the ones add to 10 or more, carry 1 to the tens place. In 27+5, the ones add to 7+5. What should happen to the tens place?",
     ["Carry 1 to the tens place", "Borrow 1 from the ones place", "Change the tens digit to 0"], "A", "When the ones add to 10 or more, carry 1 to the tens place."),
    ("n", "basic", "There are 26 cars in a parking area, and 3 more arrive. How many cars are there now?", "29",
     "The ones add to 6+3=9, which is less than 10, so the result is 29.", "26+3"),
    ("n", "standard", "There are 34 cars in a parking area, and 20 more arrive. How many cars are there now?", "54",
     "For 34+20, the tens add to 3+2=5, giving 54.", "34+20"),
    ("n", "challenge", "In 48+6, the ones add to 8+6, so carry 1 to the tens place. What is the sum?", "54",
     "Write 4 in the ones place, then add the carried 1 to the 4 tens to get 54.", "48+6"),
]

BANK["cnm_p032"] = [
    ("c", "basic", "In subtraction with regrouping, borrow 1 ten as 10 ones. In 32−7, there are not enough ones to subtract. What should you do?",
     ["Borrow 1 ten as 10 ones", "Carry 1 to the ones place", "Subtract 2 from 7 directly"], "A", "When there are not enough ones, borrow 1 ten as 10 ones."),
    ("n", "basic", "There are 58 storybooks, and 4 are borrowed. How many remain?", "54", "There are enough ones to subtract: 58−4=54.", "58-4"),
    ("n", "standard", "There are 46 storybooks, and 20 are borrowed. How many remain?", "26", "46−20=26.", "46-20"),
    ("n", "challenge", "In 43−8, there are not enough ones to subtract 8 from 3, so regroup. What is the difference?", "35",
     "After regrouping, 13−8=5 in the ones place, with 3 tens left, giving 35.", "43-8"),
]

BANK["cnm_p033"] = [
    ("n", "basic", "Class 1 has 23 students and Class 2 has 14. They do classroom duty together. How many students are there in all?", "37",
     "The ones add to 3+4=7, and the tens to 2+1=3, giving 37.", "23+14"),
    ("n", "basic", "There are 32 red balls and 25 blue balls. How many balls are there in all?", "57", "32+25=57.", "32+25"),
    ("n", "standard", "Class 1 has 27 students and Class 2 has 16. They go tree planting together. How many students are there in all?", "43",
     "The ones add to 7+6=13, so carry 1 to the tens place; the sum is 43.", "27+16"),
    ("n", "challenge", "In 48+35, the ones add to 8+5, so regroup. What is the sum?", "83",
     "Write 3 in the ones place, then add the carried 1 to 4+3 tens to get 83.", "48+35"),
]

BANK["cnm_p034"] = [
    ("n", "basic", "There are 67 sheets of paper, and 24 are used. How many are left?", "43", "67−24=43; each place has enough to subtract.", "67-24"),
    ("n", "basic", "There are 80 sheets of paper, and 30 are used. How many are left?", "50", "80−30=50.", "80-30"),
    ("n", "standard", "There are 52 sheets of paper, and 18 are used. How many are left?", "34",
     "There are not enough ones, so borrow 1 ten: 52−18=34.", "52-18"),
    ("n", "challenge", "In 70−26, there are not enough ones to subtract 6 from 0, so regroup. What is the difference?", "44",
     "After regrouping, 10−6=4 in the ones place and 6−2=4 in the tens place, giving 44.", "70-26"),
]

BANK["cnm_p035"] = [
    ("n", "basic", "There are 16 boys and 14 girls. How many students are in the class?", "30",
     "Add the two groups to get the total: 16+14=30.", "16+14"),
    ("n", "basic", "There are 35 peach and pear trees in all, including 15 peach trees. How many pear trees are there?", "20",
     "Subtract one part from the total: 35−15=20.", "35-15"),
    ("n", "standard", "An orchard has 40 peach and pear trees in all, including 18 peach trees. How many pear trees are there?", "22",
     "40−18=22 trees.", "40-18"),
    ("n", "challenge", "An orchard has 40 peach and pear trees in all, including 18 peach trees. Five more pear trees are planted. How many pear trees are there now?", "27",
     "There were 40−18=22 pear trees. Planting 5 more makes 27.", "40-18+5"),
]

BANK["cnm_p217"] = [
    ("n", "basic", "How much greater is 15 than 9?", "6", "Use subtraction to find how much greater one number is than another: 15−9=6.", "15-9"),
    ("n", "basic", "There are 42 red flowers and 30 yellow flowers. How many more red flowers are there?", "12", "42−30=12 flowers.", "42-30"),
    ("n", "standard", "Xiaoming jumps rope 56 times, and Xiaojun jumps 71 times. How many fewer times does Xiaoming jump?", "15",
     "Use subtraction to find how many fewer: 71−56=15.", "71-56"),
    ("n", "challenge", "Class 1 has 38 students, Class 2 has 45, and Class 3 has 40. How many more students are in Class 2 than in Class 1?", "7",
     "Compare Class 2 with Class 1: 45−38=7. The 40 students in Class 3 are not needed.", "45-38"),
]

BANK["cnm_p218"] = [
    ("n", "basic", "A kitten catches 12 fish. A puppy catches 5 more fish than the kitten. How many fish does the puppy catch?", "17",
     "Add 5 to 12: 12+5=17.", "12+5"),
    ("n", "basic", "There are 40 birds in a tree. There are 8 fewer birds on the ground. How many birds are on the ground?", "32",
     "Subtract 8 from 40: 40−8=32.", "40-8"),
    ("n", "standard", "Mom buys 35 apples. She buys 9 fewer pears than apples. How many pears does she buy?", "26", "35−9=26 pears.", "35-9"),
    ("n", "challenge", "Xiaoming has 24 cards. Xiaohong has 7 more than Xiaoming, and Xiaoli has 10 fewer than Xiaohong. How many cards does Xiaoli have?", "21",
     "Xiaohong has 24+7=31 cards, and Xiaoli has 31−10=21.", "24+7-10"),
]

BANK["cnm_p036"] = [
    ("c", "basic", "How many jiao are in 1 yuan?", ["10 jiao", "100 jiao", "2 jiao"], "A", "1 yuan=10 jiao."),
    ("n", "basic", "How many jiao are in 3 yuan?", "30", "1 yuan is 10 jiao, so 3 yuan is 30 jiao.", "3*10"),
    ("n", "standard", "How many fen are in 5 jiao?", "50", "1 jiao=10 fen, so 5 jiao=50 fen.", "5*10"),
    ("n", "challenge", "A notebook costs 3 yuan and 5 jiao. If you pay with 5 yuan, how much change should you receive in jiao?", "15",
     "5 yuan=50 jiao, and 3 yuan 5 jiao=35 jiao. The change is 50−35=15 jiao.", "5*10-(3*10+5)"),
]
