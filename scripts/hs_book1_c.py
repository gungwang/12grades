"""Chapter 5, Trigonometric Functions, from Required Module 1. Imported by hs_book1.py."""
from hs_common import questions, topic

NA = "Number and Algebra"
C5 = "Chapter 5: Trigonometric Functions"


def T(key, chapter, section, name, domain, typ, desc, crit, std, conf="exact", note=None):
    topic(key, 1, chapter, section, name, domain, typ, desc, crit, std, conf, note)


def Qs(key, items):
    questions(key, items)


def n(prompt, verify, expl):
    return ("n", prompt, verify, expl)


def c(prompt, ok, bad, expl):
    return ("c", prompt, ok, bad, expl)


T("tri.ang", C5, "5.1", "General Angles", NA, "conceptual",
  "Know that angles are classified as positive, negative, or zero according to the direction of rotation, and that their measures can exceed one full turn.",
  ["Can identify positive and negative angles", "Know that a general angle need not lie between 0° and 360°"],
  "FUN.12")
Qs("tri.ang", [
    c("Which angle is formed by counterclockwise rotation?", "positive angle", ["negative angle", "zero angle", "right angle"],
      "By the textbook convention used here, counterclockwise angles are positive and clockwise angles are negative."),
    n("Starting at 30°, rotate counterclockwise by one full turn. What is the resulting angle in degrees?", "30+360",
      "One full turn is 360°; 30+360=390."),
    n("Starting at 30°, rotate clockwise by one full turn. What is the resulting angle in degrees?", "30-360",
      "Clockwise rotation is negative, so 30−360=−330."),
    c("Compared with angles from 0° to 360°, what else can a general angle be?", "A negative angle or an angle greater than one full turn",
      ["Only an acute angle", "No greater than 180°", "Never 0°"],
      "A general angle can continue rotating without being limited to one turn."),
])

T("tri.end", C5, "5.1", "Angles with the Same Terminal Side", NA, "procedural",
  "Know that angles with the same terminal side as α can be written as α+k·360°, where k is an integer.",
  ["Can list coterminal angles in a specified interval", "Can determine whether two angles have the same terminal side"],
  "FUN.12", "inferred", "Coterminal angles follow directly from the definition of a general angle. Pending verification.")
Qs("tri.end", [
    n("Which angle between 0° and 360° has the same terminal side as 400°?", "400-360",
      "400−360=40; the angles differ by one full turn."),
    n("How many degrees apart are 60° and −300°, which have the same terminal side?", "60-(-300)",
      "60−(−300)=360, exactly one full turn."),
    c("Two angles with the same terminal side differ by what?", "An integer multiple of 360°", ["An integer multiple of 180°", "90°", "They must be equal"],
      "Adding or subtracting any whole number of turns returns the terminal side to the same position."),
    n("How many degrees must be added to −20° to get a coterminal angle between 0° and 360°?", "360",
      "−20+360=340; one full turn is added."),
])

T("tri.rad", C5, "5.1", "Radian Measure", NA, "conceptual",
  "Know that a radian measure is the ratio of arc length to radius; one radian is the central angle subtended by an arc equal in length to the radius.",
  ["Can state the definition of a radian", "Know that π radians equals 180°"],
  "FUN.12", "inferred", "Radian measure and general angles are grouped under the same topic. Pending verification.")
Qs("tri.rad", [
    n("How many degrees is π radians?", "degrees(pi)",
      "By the conversion, π radians equals 180°."),
    n("If the radius equals the arc length, what is the central angle in radians?", "1",
      "Radians equal arc length divided by radius. When those are equal, the angle is 1 radian."),
    c("What does radian measure use to measure an angle?", "The ratio of arc length to radius", ["The sum of arc length and diameter", "The degree measure itself", "The area of a sector"],
      "θ=l/r. This ratio is dimensionless, and the unit is called a radian."),
    n("How many degrees is 2π radians?", "degrees(2*pi)",
      "One full turn is 2π radians, or 360°."),
])

T("tri.conv", C5, "5.1", "Converting Between Degrees and Radians", NA, "procedural",
  "Convert common special angles between degrees and radians.",
  ["Can convert simple multiples of π to degrees", "Can express 30°, 45°, 60°, and 90° as multiples of π radians"],
  "FUN.12", "inferred", "Conversion is a basic skill introduced with radians. Pending verification.")
Qs("tri.conv", [
    n("How many degrees is π/6 radians?", "degrees(pi/6)",
      "180°/6=30°."),
    n("How many π radians is 90°? Write only the coefficient of π.", "Fraction(90,180)",
      "90/180=1/2, so the angle is π/2 radians."),
    n("How many degrees is π/2 radians?", "degrees(pi/2)",
      "π/2 radians is 90°."),
    c("How many radians is 30°?", "π/6", ["π/3", "π/4", "π/2"],
      "30° is 1/6 of 180°, so it equals π/6."),
])

T("tri.arc", C5, "5.1", "Arc Length Formula", NA, "procedural",
  "Use the radian formula for arc length: radius times central angle.",
  ["Can find arc length from radius and angle in radians", "Can find the central angle from arc length and radius"],
  "FUN.12", "inferred", "The arc-length formula is a direct application of radian measure. Pending verification.")
Qs("tri.arc", [
    n("A circle has radius 5 and a central angle of 2 radians. What is the arc length?", "5*2",
      "In radians, arc length = radius × central angle, so 5×2=10."),
    n("A circle has radius 4 and arc length 8. What is the central angle in radians?", "8/4",
      "Central angle = arc length / radius = 2."),
    n("A circle has radius 3 and a central angle of 1 radian. What is the arc length?", "3*1",
      "The arc length equals the radius, 3."),
    c("In l=|α|r, α must be measured in what unit?", "Radians", ["Degrees", "Percent", "Arc length"],
      "This formula is valid only when α is in radians. Convert degrees first."),
])

T("tri.def", C5, "5.2", "Definitions of Trigonometric Functions", NA, "conceptual",
  "Use the unit circle and the coordinates of the point where an angle’s terminal side intersects it to define sine and cosine.",
  ["Can state that sine is the y-coordinate and cosine is the x-coordinate", "Can find the sine or cosine of 0°, 30°, or 90°"],
  "FUN.13")
Qs("tri.def", [
    n("Find sin90°.", "sin(radians(90))",
      "The terminal side is on the positive y-axis, and the unit-circle point is (0, 1), so the sine is 1."),
    n("Find sin30°.", "sin(radians(30))",
      "sin30°=1/2."),
    n("Find cos0°.", "cos(radians(0))",
      "The terminal side is on the positive x-axis, and the point is (1, 0), so the cosine is 1."),
    c("On the unit circle, which coordinate represents sine?", "The y-coordinate", ["The x-coordinate", "The distance from the origin", "The central angle in degrees"],
      "Cosine is the x-coordinate and sine is the y-coordinate. The point is 1 unit from the origin."),
])

T("tri.sign", C5, "5.2", "Signs of Trigonometric Functions", NA, "procedural",
  "Determine the signs of sine and cosine by quadrant and find their special values on the axes.",
  ["Can state the signs of sine and cosine in each quadrant", "Can find sine or cosine at 180° or 270°"],
  "FUN.13", "inferred", "The signs follow directly from the unit-circle definitions. Pending verification.")
Qs("tri.sign", [
    n("Find sin180°.", "sin(radians(180))",
      "The terminal side is on the negative x-axis at (−1, 0), so the sine is 0."),
    n("Find cos180°.", "cos(radians(180))",
      "The point’s x-coordinate is −1."),
    n("Find sin270°.", "sin(radians(270))",
      "The terminal side is on the negative y-axis, so the y-coordinate is −1."),
    c("What are the signs of sine and cosine in Quadrant II?", "Sine is positive and cosine is negative",
      ["Both are positive", "Sine is negative and cosine is positive", "Both are negative"],
      "In Quadrant II, the x-coordinate is negative and the y-coordinate is positive."),
])

T("tri.id", C5, "5.2", "Relations Between Trigonometric Functions of the Same Angle", NA, "reasoning",
  "Use sin²θ+cos²θ=1 and express one trigonometric function in terms of another.",
  ["Can verify a sum of squares using the same-angle identity", "Can find the square of cosine from sine"],
  "FUN.14")
Qs("tri.id", [
    n("Evaluate sin²30°+cos²30°.", "sin(radians(30))**2+cos(radians(30))**2",
      "For the same angle, the sum of the squares of sine and cosine is always 1."),
    n("Given sinθ=3/5, find 25cos²θ.", "25*(1-Fraction(9,25))",
      "cos²θ=1−(3/5)²=1−9/25=16/25, so 25cos²θ=16."),
    n("If cosθ=0, what is sin²θ?", "1",
      "By the sum-of-squares identity, sin²θ=1."),
    c("What is sin²θ+cos²θ identically equal to?", "1", ["0", "θ", "2"],
      "This is the basic same-angle identity and holds wherever the expressions are defined."),
])

T("tri.rest", C5, "5.2", "Finding Other Values from One Trigonometric Function", NA, "procedural",
  "Given the quadrant of an angle, find other trigonometric values from one known value.",
  ["Can determine the sign before taking a square root", "Can calculate the resulting integer or fraction"],
  "FUN.14", "inferred", "Evaluating values is a basic exercise in same-angle identities. Pending verification.")
Qs("tri.rest", [
    n("θ is acute and sinθ=1/2. Find 2sinθ.", "2*Fraction(1,2)",
      "2×1/2=1."),
    n("Find tan45°.", "tan(radians(45))",
      "At 45°, sine equals cosine, so tangent is 1."),
    n("θ is between 0° and 90°, inclusive, and cosθ=1. Find sinθ.", "0",
      "In this interval, cosθ=1 only when θ=0°, so sine is 0."),
    c("Given sinθ=1/2 and θ is in Quadrant II, what is the sign of cosθ?", "Negative",
      ["Positive", "Zero", "Could be positive or negative"],
      "Cosine is negative in Quadrant II. Its magnitude follows from the sum-of-squares identity, while the quadrant determines its sign."),
])

T("tri.ind", C5, "5.3", "Reduction Formulas", NA, "conceptual",
  "Know the reduction formulas for coterminal angles and for angles involving π±α and π/2±α, and describe how sine and cosine change.",
  ["Can state sin(π−α)=sinα", "Can state cos(π−α)=−cosα"],
  "FUN.14", "inferred", "Reduction formulas convert trigonometric functions of general angles to those of acute angles. Pending verification.")
Qs("tri.ind", [
    c("What is sin(180°−α)?", "sinα", ["−sinα", "cosα", "−cosα"],
      "The sine of 180°−α equals the sine of α."),
    c("What is cos(180°−α)?", "−cosα", ["cosα", "sinα", "−sinα"],
      "In Quadrant II, cosine changes sign."),
    n("Using a reduction formula, sin150° equals the sine of what angle? Give only the acute angle in degrees.", "30",
      "sin(180°−30°)=sin30°; the corresponding acute angle is 30°."),
    c("What is the main purpose of reduction formulas?", "To express trigonometric functions of general angles using acute angles",
      ["Only to evaluate 90°", "To replace radian measure", "Only for tangent"],
      "The formulas reduce the angle to one between 0° and 90°, where special-angle values can be used."),
])

T("tri.indapp", C5, "5.3", "Evaluating with Reduction Formulas", NA, "procedural",
  "Reduce trigonometric functions of 120°, 150°, 180°, 210°, 270°, and 360° to special values.",
  ["Can choose an appropriate reduction formula", "Can obtain 0, ±1, or ±1/2"],
  "FUN.14", "inferred", "Evaluation is a basic exercise in reduction formulas. Pending verification.")
Qs("tri.indapp", [
    n("Find sin150°.", "sin(radians(150))",
      "sin(180°−30°)=sin30°=1/2."),
    n("Find cos120°.", "cos(radians(120))",
      "cos(180°−60°)=−cos60°=−1/2."),
    n("Find sin210°.", "sin(radians(210))",
      "sin(180°+30°)=−sin30°=−1/2."),
    n("Find cos360°.", "cos(radians(360))",
      "360° is coterminal with 0°, so the cosine is 1."),
])

T("tri.sin", C5, "5.4", "Graph and Properties of the Sine Function", NA, "conceptual",
  "Know the domain, range, maximum and minimum values, and periodicity of y=sin x.",
  ["Can state that the range is [−1, 1]", "Can state that the least positive period is 2π"],
  "FUN.15")
Qs("tri.sin", [
    n("What is the maximum value of y=sin x?", "1",
      "The maximum value of sine is 1."),
    n("What is the minimum value of y=sin x?", "-1",
      "The minimum value of sine is −1."),
    n("For y=sin x with x in radians, what is the least positive period divided by π?", "2",
      "The least positive period is 2π; dividing by π gives 2."),
    c("What is the domain of y=sin x?", "All real numbers", ["All positive numbers", "All real numbers except π/2", "From 0 to π"],
      "Sine is defined for every real number. Tangent, unlike sine, is undefined at values such as π/2."),
])

T("tri.sinp", C5, "5.4", "Monotonic Intervals of the Sine Function", NA, "reasoning",
  "Determine where sine increases or decreases on intervals such as [−π/2, π/2] and evaluate the function at the endpoints.",
  ["Can state that sine increases on [−π/2, π/2]", "Can evaluate sine at interval endpoints"],
  "FUN.15", "inferred", "Monotonic intervals are among the properties of the sine function. Pending verification.")
Qs("tri.sinp", [
    c("How does y=sin x behave on [−π/2, π/2]?", "Increasing", ["Decreasing", "Increasing then decreasing", "Decreasing then increasing"],
      "On this interval, sine rises from its minimum, −1, to its maximum, 1."),
    n("Find sin0°.", "sin(radians(0))",
      "The terminal side of 0° is on the positive x-axis, so the y-coordinate is 0."),
    n("Find sin(−90°), or the sine of −π/2 radians.", "sin(radians(-90))",
      "Sine is an odd function: sin(−90°)=−sin90°=−1."),
    c("How does y=sin x behave overall on [π/2, 3π/2]?", "Decreasing",
      ["Increasing", "Decreasing then increasing", "Constant"],
      "Sine decreases from 1 to −1 on this interval; cosine is never positive, so the function decreases throughout."),
])

T("tri.cos", C5, "5.4", "Graph and Properties of the Cosine Function", NA, "conceptual",
  "Know that y=cos x is even, has maximum 1 and minimum −1, and has least positive period 2π.",
  ["Can find cosine at 0°, 60°, and 180°", "Can state that cosine is an even function"],
  "FUN.15", "inferred", "The cosine and sine properties are grouped together. Pending verification.")
Qs("tri.cos", [
    n("Find cos0°.", "cos(radians(0))",
      "The unit-circle point is (1, 0), so the cosine is 1."),
    n("Find cos60°.", "cos(radians(60))",
      "cos60°=1/2."),
    n("Find cos180°.", "cos(radians(180))",
      "The point is (−1, 0), so the cosine is −1."),
    c("What is the parity of y=cos x?", "Even", ["Odd", "Both even and odd", "Neither even nor odd"],
      "cos(−x)=cos x, so the graph is symmetric about the y-axis."),
])

T("tri.tan", C5, "5.4", "Tangent Function", NA, "procedural",
  "Know that tangent is undefined when cosine is 0, and evaluate tangent at 0° and 45°.",
  ["Can identify angles where tangent is undefined", "Can find tan0° and tan45°"],
  "FUN.15", "inferred", "Tangent is one of the functions studied through trigonometric graphs and properties. Pending verification.")
Qs("tri.tan", [
    n("Find tan0°.", "tan(radians(0))",
      "sin0°=0 and cos0°=1, so tangent is 0."),
    n("Find tan45°.", "tan(radians(45))",
      "At 45°, sine equals cosine, so tangent is 1."),
    n("Between 0° and 90°, what angle satisfies tan x=1?", "45",
      "The tangent of 45° is 1, and there is no other solution in this interval."),
    c("What is y=tan x at x=90°?", "Undefined", ["0", "1", "−1"],
      "cos90°=0, so the denominator of tangent is 0 and the function is undefined."),
])

T("tri.diff", C5, "5.5", "Sine of a Difference", NA, "procedural",
  "Use sin(α−β)=sinα cosβ−cosα sinβ to evaluate expressions that reduce to special angles.",
  ["Can apply the formula to 60° and 30°", "Can simplify results to values such as 1/2"],
  "FUN.16")
Qs("tri.diff", [
    n("Evaluate sin60°cos30°−cos60°sin30°. Given sin60°=cos30°=√3/2 and cos60°=sin30°=1/2.",
      "Fraction(3,4)-Fraction(1,4)",
      "(√3/2)·(√3/2)−(1/2)·(1/2)=3/4−1/4=1/2, which is sin30°."),
    n("sin(90°−30°) equals cos of what angle? Give only the angle in degrees.", "30",
      "sin(90°−α)=cosα, where α=30°."),
    n("Evaluate sin45°cos45°−cos45°sin45°.", "0",
      "The two terms are equal, so their difference is 0. This is also sin0°."),
    c("What is sin(α−β)?", "sinα cosβ − cosα sinβ",
      ["sinα cosβ + cosα sinβ", "cosα cosβ − sinα sinβ", "sinα sinβ − cosα cosβ"],
      "For the sine of a difference, multiply the cross terms and subtract. The sum formula uses a plus sign."),
])

T("tri.sum", C5, "5.5", "Sine and Cosine of a Sum", NA, "procedural",
  "Use sum formulas to evaluate expressions that simplify to 0, ±1/2, or ±1.",
  ["Can evaluate sin(α+β) for special angles", "Can distinguish the signs in sum and difference formulas"],
  "FUN.16", "inferred", "Sum and difference formulas are both identity transformations. Pending verification.")
Qs("tri.sum", [
    n("Evaluate sin30°cos60°+cos30°sin60°. Given sin30°=cos60°=1/2 and cos30°=sin60°=√3/2.",
      "Fraction(1,4)+Fraction(3,4)",
      "(1/2)·(1/2)+(√3/2)·(√3/2)=1/4+3/4=1, which is sin90°."),
    n("Evaluate cos60°cos0°+sin60°sin0°. Given cos0°=1, sin0°=0, and cos60°=1/2.",
      "Fraction(1,2)*1+0",
      "The second term is 0 and the first is 1/2, so the result is cos60°."),
    n("Find sin(45°+45°).", "1",
      "45°+45°=90°, and sin90°=1."),
    c("What is sin(α+β)?", "sinα cosβ + cosα sinβ",
      ["sinα cosβ − cosα sinβ", "cosα cosβ − sinα sinβ", "cosα cosβ + sinα sinβ"],
      "The sine sum formula has two sine-cosine products joined by a plus sign. The difference formula uses a minus sign."),
])

T("tri.tant", C5, "5.5", "Tangent of a Sum or Difference", NA, "procedural",
  "Use tangent sum and difference formulas to evaluate special values when the denominator is nonzero.",
  ["Can evaluate tan(α−β)", "Know the formula cannot be used when its denominator is 0"],
  "FUN.16", "inferred", "Tangent sum and difference formulas are trigonometric identity transformations. Pending verification.")
Qs("tri.tant", [
    n("Evaluate (tan45°−tan0°)/(1+tan45°·tan0°).", "(1-0)/(1+1*0)",
      "tan45°=1 and tan0°=0, so both numerator and denominator are 1. The result is 1, which is tan45°."),
    n("Find tan(45°−45°).", "0",
      "The tangent of 0° is 0."),
    n("Evaluate 1+tan45°·tan0°.", "1+1*0",
      "tan0°=0, so the product is 0 and the sum is 1. The denominator is nonzero, so the formula applies."),
    c("When can the formula for tan(α+β) not be used?", "When the denominator 1−tanα tanβ is 0",
      ["When the numerator is 0", "When α is acute", "When β=0°"],
      "If the denominator is 0, the tangent of the sum is undefined or the formula cannot be divided through."),
])

T("tri.double", C5, "5.5", "Double-Angle Formula", NA, "procedural",
  "Use cos2α=2cos²α−1=1−2sin²α to evaluate special angles.",
  ["Can evaluate using the cosine double-angle formula", "Can state the three cosine forms of the double-angle formula"],
  "FUN.16", "inferred", "The double-angle formula is a special case of the sum formula. Pending verification.")
Qs("tri.double", [
    n("Evaluate 2cos²60°−1.", "2*Fraction(1,2)**2-1",
      "cos60°=1/2, so 2×(1/2)²−1=1/2−1=−1/2, which is cos120°."),
    n("Evaluate 1−2sin²30°.", "1-2*Fraction(1,2)**2",
      "sin30°=1/2, so 1−2×(1/4)=1/2, which is cos60°."),
    n("Find cos(2×0°).", "1",
      "Twice 0° is still 0°, so the cosine is 1."),
    c("Which expression is not equal to cos2α?", "2sinα cosα",
      ["2cos²α−1", "1−2sin²α", "cos²α−sin²α"],
      "2sinα cosα is sin2α, not cos2α."),
])

T("tri.idapp", C5, "5.5", "Basic Trigonometric Identity Transformations", NA, "procedural",
  "Apply same-angle and double-angle identities in evaluations, keeping results as integers or fractions.",
  ["Can simplify before substituting special angles", "Can choose an appropriate identity"],
  "FUN.16", "inferred", "Identity-transformation practice supports sum, difference, and double-angle formulas. Pending verification.")
Qs("tri.idapp", [
    n("Evaluate 1+cos60°.", "1+cos(radians(60))",
      "cos60°=1/2, so 1+1/2=3/2."),
    n("Evaluate 1−cos180°.", "1-cos(radians(180))",
      "cos180°=−1, so 1−(−1)=2."),
    n("Evaluate sin²0°+cos²0°.", "sin(radians(0))**2+cos(radians(0))**2",
      "The sum of squares is always 1."),
    c("When sin²α+cos²α appears in an evaluation, what should you do first?", "Replace it with 1",
      ["Replace it with 0", "Replace it with 2α", "Replace it with tanα"],
      "The same-angle identity simplifies the expression directly, without evaluating sine and cosine separately."),
])

T("tri.wave", C5, "5.6", "Sinusoidal Functions", NA, "conceptual",
  "Know that A determines the amplitude and ω determines the period in y=Asin(ωx+φ).",
  ["Can identify the amplitude as |A|", "Can state how the period relates to 2π and ω"],
  "FUN.17")
Qs("tri.wave", [
    n("What is the maximum value of y=2sin x?", "2",
      "A=2>0, so the maximum is the amplitude, 2."),
    n("For y=sin(2x), what is the least positive period divided by π?", "1",
      "The period is 2π/2=π; dividing by π gives 1."),
    n("Find sin(0+π/2). Use radians for x.", "sin(radians(90))",
      "sin(π/2)=1."),
    c("In y=Asin(ωx+φ), what is the amplitude?", "The absolute value of A",
      ["A itself in every case", "ω", "φ"],
      "If A is negative, the graph is reflected vertically, but the amplitude is still its absolute value."),
])

T("tri.param", C5, "5.6", "Parameters of a Sinusoidal Function", NA, "procedural",
  "Read the amplitude, period, and initial phase from an equation.",
  ["Can identify A and ω", "Can evaluate the function at special values of x"],
  "FUN.17", "inferred", "Reading parameters is a basic skill for sinusoidal functions. Pending verification.")
Qs("tri.param", [
    n("What is the amplitude of y=2sin(2x+φ)?", "2",
      "A=2, so the amplitude is 2."),
    n("When ω=2, what is the least positive period divided by π?", "1",
      "T=2π/ω=π, and dividing by π gives 1."),
    n("Find sin(π/6−π/6).", "sin(radians(0))",
      "The expression in parentheses is 0, so the sine is 0."),
    c("In y=sin(x+φ), what is φ called?", "Initial phase", ["Amplitude", "Period", "Frequency"],
      "φ is the phase at x=0, called the initial phase."),
])

T("tri.find", C5, "5.6", "Determining a Sinusoidal Function from Conditions", NA, "procedural",
  "Find the amplitude, midline, and ω from the maximum, minimum, and period.",
  ["Can find amplitude from maximum and minimum values", "Can find ω from the period"],
  "FUN.17", "inferred", "Determining parameters is a prerequisite for modeling phenomena with sinusoidal functions. Pending verification.")
Qs("tri.find", [
    n("A sinusoidal function has maximum 5 and minimum −1. What is its amplitude?", "(5-(-1))/2",
      "Half the difference between the maximum and minimum is (5+1)/2=3."),
    n("A sinusoidal function has maximum 5 and minimum −1. What is its midline?", "(5+(-1))/2",
      "The midline is the average of the maximum and minimum: (5+(−1))/2=2."),
    n("The least positive period is 4π. Since ω=2π divided by the period, what is ω?", "Fraction(2,4)",
      "ω=2π/(4π)=1/2."),
    c("If only the maximum and minimum are known, what cannot yet be determined?", "The period and initial phase",
      ["The amplitude", "The midline", "The range of function values"],
      "The maximum and minimum determine the amplitude and vertical position, but the period requires a time interval."),
])

T("tri.app", C5, "5.7", "Applications of Trigonometric Functions", NA, "application",
  "Use sinusoidal functions to model simple periodic phenomena such as temperature or a Ferris wheel’s height.",
  ["Can find the maximum and minimum from the midline and amplitude", "Can explain that the period is the time for one repetition"],
  "FUN.17", "inferred", "Applications provide real-world contexts for sinusoidal functions. Pending verification.")
Qs("tri.app", [
    n("Temperature varies as y=10+8sin(ωt). What is the maximum temperature?", "10+8",
      "Sine has a maximum of 1, so the maximum temperature is 10+8=18."),
    n("Temperature varies as y=10+8sin(ωt). What is the minimum temperature?", "10-8",
      "Sine has a minimum of −1, so the minimum temperature is 10+8×(−1)=10−8=2."),
    n("A Ferris wheel has radius 2 m and its center is 3 m above the ground. How high is its highest point?", "3+2",
      "The highest point is one radius above the center, so 3+2=5."),
    c("In y=Asin(ωt+φ)+b for a periodic phenomenon, what does b represent?", "The midline",
      ["The highest point", "The period", "The starting time"],
      "b is the center of the oscillation. The maximum is b+|A| and the minimum is b−|A|."),
])
