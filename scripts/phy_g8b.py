"""Grade 8, Semester 2 (People's Education Press, adopted spring 2025; revised to the 2022 curriculum standard): Chapters 7–12. Take g = 10 N/kg in all questions."""
from phy_lib import T, C, N

# V is a parser lookup key used by phy_build.GRADE; keep it unchanged.
V = "八下"
# Keep T() domain labels unchanged; phy_lib.PHY_DOMAINS validates them as machine metadata.

_FIG_CUP = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 170"><line x1="20" y1="120" x2="200" y2="120" stroke="currentColor" stroke-width="3"/>'
  '<rect x="85" y="80" width="50" height="40" fill="currentColor" fill-opacity="0.12" stroke="currentColor" stroke-width="2.4"/>'
  '<circle cx="110" cy="100" r="3" fill="currentColor"/>'
  '<line x1="110" y1="100" x2="110" y2="30" stroke="currentColor" stroke-width="2.4"/><path d="M104 40 L110 26 L116 40 Z" fill="currentColor"/>'
  '<line x1="110" y1="100" x2="110" y2="160" stroke="currentColor" stroke-width="2.4"/><path d="M104 150 L110 164 L116 150 Z" fill="currentColor"/>'
  '<text x="118" y="38" font-size="14" fill="currentColor">F</text><text x="118" y="158" font-size="14" fill="currentColor">G</text></svg>')

# ---------------- Chapter 7: Force
T("force", (V, "Chapter 7", "Force", "7.1"), "Force", "运动和相互作用", "conceptual",
  "Understand that a force is an interaction between objects and that forces occur in pairs; explain that a force can change an object's motion or shape; identify a force's magnitude, direction, and point of application; draw force diagrams; and state that force is measured in newtons (N).",
  ["Describe the effects of a force", "Explain that forces between objects occur in pairs", "Identify the three elements of a force and draw a force diagram"],
  [("2.2.3", "exact"), ("2.2.4", "exact")], pre=[("motion_desc", "soft")],
  qs=[
    C("basic", "What is the unit of force?", "The newton (N)", ["The kilogram (kg)", "The pascal (Pa)", "The joule (J)"],
      "The unit of force is the newton, symbol N. The kilogram is a unit of mass."),
    C("basic", "When swimming, a person pushes water backward and moves forward. What does this demonstrate?", "Forces between objects occur in pairs", ["A force can change an object's shape", "The effect of a force does not depend on its magnitude", "A person can move forward without a force"],
      "The swimmer pushes the water backward, and the water simultaneously pushes the swimmer forward. Forces between objects occur in pairs."),
    C("standard", "A door is easier to open when it is pushed farther from its hinge. What does this show about the effect of a force?", "It depends on the point of application", ["It depends on the magnitude", "It depends on the direction", "It depends on the door's mass"],
      "The magnitude and direction of the push stay the same, but changing where it is applied changes the effect. This shows that the effect depends on the point of application."),
    C("standard", "Which example shows a force changing an object's state of motion?", "A goalkeeper catches a moving soccer ball", ["A spring is stretched", "Modeling clay is squeezed", "Wind bends a small tree"],
      "The soccer ball changes from moving to stationary, so its state of motion changes. The other examples show a change in shape."),
  ])

T("elastic", (V, "Chapter 7", "Force", "7.2"), "Elastic Force", "运动和相互作用", "procedural",
  "Understand elasticity and elastic force; know that, within the elastic limit, a spring's extension is proportional to the applied force; and use a spring scale correctly to measure force.",
  ["State the conditions for an elastic force", "Use and read a spring scale correctly", "Explain that spring extension is proportional to force within the elastic limit"],
  [("2.2.3", "exact"), ("4.1.6", "exact"), ("1.2.1", "inferred")], pre=[("force", "hard")],
  math=[("cnm_p213", "Spring extension is proportional to the applied force."), ("cnm_200", "A graph of spring extension against force is a straight line through the origin.")],
  qs=[
    C("basic", "Which of the following forces is not an elastic force?", "Earth's attraction on an object", ["The tension exerted by a rope on an object", "The normal force exerted by a table on a book", "The pull exerted by a hand on a spring"],
      "An elastic force is produced when an object undergoes elastic deformation. Earth's attraction on an object is gravity."),
    C("basic", "What principle is a spring scale based on?", "Within the elastic limit, spring extension is proportional to the applied force", ["Spring length is proportional to the applied force", "Spring mass is proportional to the applied force", "A longer spring exerts less force"],
      "It is extension, not total length, that is proportional to the applied force."),
    N("standard", "A spring has an original length of 10 cm and a length of 12 cm when a 2 N object is attached. Within its elastic limit, what is its length when a 5 N object is attached, in cm? (Enter a number only.)", "15",
      "The spring extends 1 cm per newton, so a 5 N force produces 5 cm of extension. Its total length is 10 + 5 = 15 cm. A common error is to treat 12 cm as the extension.", "10+(12-10)/2*5"),
    C("standard", "Two people pull on opposite ends of a spring scale, each with a force of 5 N. What does the scale read?", "5 N", ["10 N", "0 N", "2.5 N"],
      "The scale reads the 5 N force exerted on its hook. The force at the other end keeps it in equilibrium.", verify="5"),
  ])

T("gravity", (V, "Chapter 7", "Force", "7.3"), "Gravity", "运动和相互作用", "procedural",
  "Understand that gravity is the force exerted on an object due to Earth's attraction, directed vertically downward and applied at the center of gravity. Use G = mg, where g is approximately 9.8 N/kg (often taken as 10 N/kg in problems).",
  ["Use G = mg to calculate weight or mass", "State the vertical direction of gravity and describe an application", "Distinguish mass from weight"],
  [("2.2.3", "exact")], pre=[("elastic", "soft"), ("mass", "hard")],
  math=[("cnm_p213", "An object's weight is proportional to its mass.")],
  qs=[
    N("basic", "What is the weight of a student with a mass of 50 kg, in N? (Take g = 10 N/kg; enter a number only.)", "500", "G = mg = 50 kg × 10 N/kg = 500 N.", "50*10"),
    C("basic", "What is the direction of gravity?", "Vertically downward", ["Perpendicularly downward", "Downward, perpendicular to the ground", "In the direction of motion"],
      "Gravity is always vertically downward. On an incline, it does not point perpendicular to the incline. Builders use a plumb line to check whether a wall is vertical."),
    C("standard", "An astronaut brings a 2 kg rock from the Moon to Earth. How do the rock's mass and weight change?", "Its mass stays the same, and its weight increases", ["Its mass and weight both increase", "Its mass increases, and its weight stays the same", "Its mass and weight both stay the same"],
      "Mass is an intrinsic property of an object and does not change with location. Since g is greater on Earth than on the Moon, the rock's weight increases."),
    C("standard", "An object weighs 30 N. What is its mass? (Take g = 10 N/kg.)", "3 kg", ["300 kg", "30 kg", "0.3 kg"],
      "m = G/g = 30 ÷ 10 = 3 kg.", verify="30/10"),
  ])

# ---------------- Chapter 8: Motion and Force
T("newton1", (V, "Chapter 8", "Motion-and-Force", "8.1"), "Newton's First Law", "运动和相互作用", "reasoning",
  "Understand Newton's first law through experiments and scientific reasoning about how resistance affects motion. Know that every object has inertia, that inertia depends only on mass, and how to use inertia to explain everyday phenomena.",
  ["State Newton's first law and explain how it is established through experiment and reasoning", "Explain that inertia depends only on mass", "Use inertia to explain sudden braking, seat belts, and similar phenomena"],
  [("2.2.5", "exact")], pre=[("force", "hard")],
  qs=[
    C("basic", "When no force acts on an object, what state of motion does it maintain?", "Rest or uniform motion in a straight line", ["Rest", "Uniform motion in a straight line", "Gradually coming to a stop"],
      "This is Newton's first law: an object at rest remains at rest, and an object in motion continues with uniform motion in a straight line."),
    C("basic", "Which statement about inertia is correct?", "Every object has inertia", ["Only moving objects have inertia", "Greater speed means greater inertia", "A seat belt reduces inertia"],
      "Inertia is a property of matter and depends only on mass, not speed. A seat belt reduces the harm caused by inertia."),
    C("standard", "How was Newton's first law established?", "Through scientific reasoning based on experiments", ["Directly from an experiment", "By imagination alone", "Through mathematical calculation"],
      "No object in reality is completely free of forces. Newton's first law was established through reasoning based on experiments."),
    C("standard", "In which direction does a passenger tend to lurch when a car brakes suddenly?", "Forward", ["Backward", "Left", "The passenger does not lurch"],
      "When the car brakes, the passenger's feet stop with it, but inertia tends to keep the upper body moving as before, so the passenger lurches forward."),
  ])

T("balance2", (V, "Chapter 8", "Motion-and-Force", "8.2"), "Equilibrium of Two Forces", "运动和相互作用", "reasoning",
  "Understand equilibrium and balanced forces. Two forces balance when they act on the same object, have equal magnitudes, point in opposite directions, and act along the same line. Distinguish balanced forces from action–reaction pairs.",
  ["State the four conditions for two-force equilibrium", "Distinguish balanced forces from action–reaction pairs", "Use two-force equilibrium to find an unknown force"],
  [("2.2.4", "exact")], pre=[("newton1", "hard"), ("gravity", "hard")],
  qs=[
    C("basic", "A book rests on a horizontal table. Which pair of forces on the book is balanced?", "The book's weight and the normal force exerted by the table on the book", ["The pressure exerted by the book on the table and the normal force exerted by the table on the book", "The book's weight and the pressure exerted by the book on the table", "The weight of the table and the weight of the book"],
      "Balanced forces act on the same object. Pressure and normal force form an action–reaction pair and act on different objects."),
    C("basic", "As shown, a cup rests on a horizontal table. Its weight G is 3 N. What is the normal force F exerted by the table on the cup?", "3 N", ["0 N", "6 N", "1.5 N"],
      "The cup is at rest, so G and F are balanced forces with equal magnitudes. Thus F = 3 N.", verify="3", figure=_FIG_CUP),
    C("standard", "A 20 N horizontal force pushes a crate at constant velocity across a horizontal floor. What is the friction force on the crate?", "20 N", ["0 N", "Greater than 20 N", "Less than 20 N"],
      "Constant-velocity motion is an equilibrium state. The push and friction are balanced forces, so friction is 20 N.", verify="20"),
    C("standard", "Which object is in equilibrium?", "A car traveling at constant velocity on a straight road", ["An airplane accelerating during takeoff", "A car turning at constant speed on a curve", "A ball at the highest point of a vertical throw"],
      "Equilibrium means rest or uniform motion in a straight line. The car turning changes direction, and the ball at the highest point is acted on by gravity, so neither is in equilibrium."),
  ])

T("friction", (V, "Chapter 8", "Motion-and-Force", "8.3"), "Friction", "运动和相互作用", "reasoning",
  "Understand friction and investigate how kinetic-friction magnitude depends on the normal force and the roughness of the surfaces in contact. Explain ways to increase or reduce friction.",
  ["State the two factors that affect kinetic-friction magnitude", "Explain why a block must be pulled at constant velocity when measuring kinetic friction", "Identify ways to increase or reduce friction"],
  [("2.2.3", "exact"), ("4.2.2", "exact")], pre=[("balance2", "hard")],
  qs=[
    C("basic", "Which factor affects the magnitude of kinetic friction?", "The roughness of the surfaces in contact", ["The object's speed", "The size of the contact area", "The object's volume"],
      "Kinetic friction depends on the normal force and the roughness of the surfaces in contact, not on speed or contact area."),
    C("basic", "Why do bicycle tires have treads?", "To increase friction", ["To reduce friction", "To reduce pressure", "To make the bicycle look better"],
      "The treads increase the roughness of the surface in contact, thereby increasing friction."),
    C("standard", "Why should a block be pulled horizontally at constant velocity when measuring its kinetic friction with a spring scale?", "The pull and friction are balanced and have equal magnitudes", ["This makes friction smallest", "This makes the pull greatest", "This means the block experiences no friction"],
      "At constant velocity, the forces on the block are balanced, so the spring-scale reading equals the kinetic-friction force."),
    C("standard", "Which action reduces friction?", "Lubricating a door hinge", ["Spreading sand on an icy road in winter", "Squeezing a bicycle brake lever firmly", "Adding treads to the soles of shoes"],
      "Lubricant separates the surfaces in contact and reduces friction. The other actions increase friction."),
  ])

T("resultant", (V, "Chapter 8", "Motion-and-Force", "8.4"), "Resultant of Two Collinear Forces", "运动和相互作用", "procedural",
  "Understand the concept of a resultant force. For two collinear forces pointing in the same direction, the resultant is their sum; for forces pointing in opposite directions, it is their difference and points in the direction of the greater force.",
  ["Find the resultant of two collinear forces pointing in the same direction", "Find the resultant of two collinear forces pointing in opposite directions and determine its direction"],
  [("2.2.4", "exact")], pre=[("balance2", "hard")],
  math=[("cnm_001", "Opposite forces can be assigned opposite signs; the resultant is their algebraic sum.")],
  qs=[
    C("basic", "What is the resultant of collinear forces of 3 N and 5 N that point in the same direction?", "8 N", ["2 N", "15 N", "0 N"],
      "For forces in the same direction, F = F₁ + F₂ = 8 N, pointing in their direction.", verify="3+5"),
    C("basic", "What is the resultant of collinear forces of 3 N and 5 N that point in opposite directions?", "2 N, in the direction of the 5 N force", ["8 N, in the direction of the 5 N force", "2 N, in the direction of the 3 N force", "0 N"],
      "For forces in opposite directions, F = F₁ - F₂ = 2 N and points in the direction of the greater force."),
    N("standard", "A 2 N ball is thrown vertically upward. While rising, it experiences 0.5 N of air resistance. What is the magnitude of the net force on the ball, in N? (Enter a number only.)", "2.5",
      "While the ball rises, gravity and air resistance both point downward, opposite the motion. The net force is 2 + 0.5 = 2.5 N, vertically downward.", "2+0.5"),
    C("standard", "A 30 N force lifts upward on a 50 N object, but does not lift it off the ground. What is the net force on the object?", "0 N", ["20 N", "80 N", "30 N"],
      "The object is stationary and in equilibrium, so the net force is 0. The ground also exerts a 20 N normal force.", verify="0"),
  ])

# ---------------- Chapter 9: Pressure
T("pressure", (V, "Chapter 9", "Pressure", "9.1"), "Pressure", "运动和相互作用", "procedural",
  "Understand pressure p = F/S, measured in pascals (Pa), and ways to increase or decrease pressure. Calculate pressure exerted by solids.",
  ["Calculate pressure using p = F/S with consistent units (area in m²)", "Identify ways to increase or decrease pressure", "Explain how the effect of a force depends on force and contact area"],
  [("2.2.7", "exact")], pre=[("gravity", "hard"), ("balance2", "soft")],
  math=[("cnm_164", "Convert cm² to m² using negative integer powers and scientific notation."), ("cnm_p214", "For a fixed force, pressure is inversely proportional to contact area.")],
  qs=[
    C("basic", "What is the unit of pressure?", "The pascal (Pa)", ["The newton (N)", "The kilogram (kg)", "The joule (J)"],
      "Pressure is measured in pascals: 1 Pa = 1 N/m²."),
    C("basic", "Which action is intended to increase pressure?", "Sharpening a kitchen knife to make its blade thinner", ["Making a backpack strap wider", "Laying sleepers under railway tracks", "Fitting a tank with wide tracks"],
      "For a fixed force, decreasing the contact area increases pressure. The other three actions increase contact area and reduce pressure."),
    N("standard", "A person weighing 600 N stands on both feet on a horizontal floor. The contact area of each foot is 0.02 m². What pressure does the person exert on the floor, in Pa? (Enter a number only.)", "15000",
      "The total contact area is S = 2 × 0.02 = 0.04 m², so p = F/S = 600 ÷ 0.04 = 15000 Pa. Using only one foot would give 30000 Pa.", "600/(2*0.02)"),
    C("advanced", "A 50 N force acts on an area of 100 cm². What is the pressure?", "5000 Pa", ["0.5 Pa", "50 Pa", "5000 N"],
      "100 cm² = 0.01 m², so p = 50 ÷ 0.01 = 5000 Pa. Failing to convert the area would incorrectly give 0.5 Pa.", verify="50/0.01"),
  ])

T("liquid_p", (V, "Chapter 9", "Pressure", "9.2"), "Liquid Pressure", "运动和相互作用", "procedural",
  "Know that liquids exert pressure in all directions. Investigate how liquid pressure depends on depth and liquid density, p = ρgh, and learn about communicating vessels and their applications.",
  ["Explain that liquid pressure increases with depth and depends on liquid density", "Calculate using p = ρgh, where h is the vertical distance below the free surface", "Give examples of communicating vessels"],
  [("2.2.8", "exact"), ("4.2.3", "exact")], pre=[("pressure", "hard"), ("density", "hard")],
  qs=[
    N("basic", "What pressure does water exert at a depth of 2 m, in Pa? (ρ_water = 1.0×10³ kg/m³, g = 10 N/kg; enter a number only.)", "20000",
      "p = ρgh = 1000 × 10 × 2 = 20000 Pa.", "1000*10*2"),
    C("basic", "Why are dams built thicker at the bottom than at the top?", "Liquid pressure increases with depth", ["Liquid pressure depends on liquid density", "For appearance", "Liquids exert pressure only on the bottom of the dam"],
      "Water pressure is greater at greater depths, so the bottom of a dam must be wider and stronger."),
    C("standard", "Which device does not operate using the principle of communicating vessels?", "A syringe drawing in liquid medicine", ["A teapot", "A ship lock", "A boiler water-level gauge"],
      "A teapot, ship lock, and boiler water-level gauge are communicating vessels, open at the top and connected below. A syringe draws in liquid using atmospheric pressure."),
    C("standard", "A pressure probe is used to investigate liquid pressure. At the same depth, the probe is turned in different directions, and the difference in liquid levels in the U-tube remains unchanged. What does this show?", "At the same depth in the same liquid, pressure is equal in all directions", ["Liquid pressure is independent of depth", "Liquid pressure depends on density", "Liquids exert pressure only downward"],
      "In the same liquid at the same depth, pressure is equal in all directions."),
  ])

T("air_p", (V, "Chapter 9", "Pressure", "9.3"), "Atmospheric Pressure", "运动和相互作用", "conceptual",
  "Understand that atmospheric pressure exists; learn about the Torricelli experiment and standard atmospheric pressure (about 1.013×10⁵ Pa, equivalent to a 760 mm column of mercury); and explain how atmospheric pressure decreases with altitude and relates to everyday life.",
  ["Give examples demonstrating atmospheric pressure", "State the value of standard atmospheric pressure", "Explain that atmospheric pressure decreases with altitude"],
  [("2.2.8", "exact")], pre=[("liquid_p", "hard")],
  qs=[
    C("basic", "Which famous experiment first demonstrated the existence of atmospheric pressure?", "The Magdeburg hemispheres experiment", ["The Torricelli experiment", "Galileo's inclined-plane experiment", "Oersted's experiment"],
      "The Magdeburg hemispheres experiment demonstrated the existence of atmospheric pressure; the Torricelli experiment measured its value."),
    C("basic", "When drinking through a straw, what pushes the drink into the mouth?", "Atmospheric pressure", ["Suction from the mouth", "The drink's weight", "The elasticity of the straw"],
      "Sucking lowers the pressure inside the straw, and atmospheric pressure pushes the drink into the mouth."),
    C("standard", "How high a column of mercury can one standard atmosphere support?", "760 mm", ["76 mm", "10.3 m", "1 m"],
      "In the Torricelli experiment, standard atmospheric pressure supports a mercury column about 760 mm high (or a water column about 10.3 m high).", verify="760"),
    C("standard", "How does atmospheric pressure change when a climber reaches a high mountain?", "It decreases", ["It increases", "It stays the same", "It first decreases and then increases"],
      "Atmospheric pressure decreases as altitude increases."),
  ])

T("pump", (V, "Chapter 9", "Pressure", "9.4"), "Interdisciplinary Project: Build a Simple Piston Water Pump", "跨学科实践", "application",
  "Understand how a piston pump uses atmospheric pressure to raise water, build a simple pump, and explain why the maximum pumping height is limited by atmospheric pressure.",
  ["Explain how a piston pump works", "Know that the maximum pumping height is about 10 m at one standard atmosphere"],
  [("5.2.2", "exact"), ("2.2.8", "inferred")], pre=[("air_p", "hard")],
  qs=[
    C("basic", "What does a piston pump use to raise water?", "Atmospheric pressure", ["The weight of the water", "The force of the piston", "The buoyancy of the water"],
      "When the piston rises, the pressure below it decreases, and atmospheric pressure pushes water into the cylinder."),
    C("basic", "At one standard atmosphere, approximately how high can a piston pump raise water at most?", "10 m", ["76 cm", "100 m", "1 m"],
      "One standard atmosphere can support a water column about 10.3 m high, so the maximum pumping height is about 10 m.", verify="10"),
    C("standard", "What happens if air leaks between the piston and cylinder wall of a homemade pump?", "It cannot draw water, or its pumping height decreases", ["It pumps faster", "The water becomes warm", "Nothing changes"],
      "If air leaks in, the pressure below the piston cannot decrease enough. Atmospheric pressure then pushes up less water, or none at all."),
    C("standard", "How does the maximum pumping height of the same piston pump change at high altitude?", "It decreases", ["It increases", "It stays the same", "It first increases and then decreases"],
      "Atmospheric pressure is lower at high altitude, so it can support a shorter column of water."),
  ])

T("flow_p", (V, "Chapter 9", "Pressure", "9.5"), "Fluid Pressure and Flow Speed", "运动和相互作用", "conceptual",
  "Know that a fluid's pressure is lower where its speed is higher and greater where its speed is lower. Use this relationship to explain phenomena such as airplane lift and platform safety lines.",
  ["State the relationship between fluid pressure and flow speed", "Use the relationship to explain airplane lift, safety lines, and similar phenomena"],
  [("2.2.8", "exact")], pre=[("air_p", "hard")],
  qs=[
    C("basic", "In a fluid, how does pressure change where the flow speed increases?", "It decreases", ["It increases", "It stays the same", "It is unrelated to flow speed"],
      "Pressure in a fluid is lower where the flow speed is higher."),
    C("basic", "Why must passengers stay behind the safety line on a train platform?", "As a train passes, air between the person and train moves faster and has lower pressure", ["As a train passes, air moves slower and has higher pressure", "The train pulls people toward it with magnetic force", "The line prevents people from being dazzled by the train's lights"],
      "Air moves faster and has lower pressure between the passenger and the train. The higher pressure on the passenger's outer side can push them toward the train."),
    C("standard", "An airplane wing has a curved upper surface and a flatter lower surface. During flight, how does the air pressure above the wing compare with that below it?",
      "It is lower, producing upward lift", ["It is higher, producing downward pressure", "It is equal", "It is lower, producing a downward force"],
      "Air moves faster above the wing, where pressure is lower, and more slowly below it, where pressure is higher. This pressure difference produces upward lift."),
    C("standard", "What happens when air is blown between two sheets of paper hanging freely?",
      "They move toward each other", ["They move apart", "They stay still", "They both drift forward"],
      "Air between the sheets moves faster and has lower pressure. The higher pressure outside pushes the sheets together."),
  ])

# ---------------- Chapter 10: Buoyancy
T("buoy", (V, "Chapter 10", "Buoyancy", "10.1"), "Buoyancy", "运动和相互作用", "procedural",
  "Know that buoyant force is directed vertically upward and is caused by the difference between the liquid pressures on an object's lower and upper surfaces. Measure buoyant force using the weight-difference method, and investigate how its magnitude depends on displaced volume and liquid density.",
  ["Find buoyant force using the weight-difference method, F_b = G - F_reading", "State that buoyant force points vertically upward", "Explain that buoyant force depends on V_displaced and ρ_liquid, not on depth when fully submerged"],
  [("2.2.9", "exact"), ("4.2.4", "exact")], pre=[("liquid_p", "hard"), ("resultant", "soft")],
  qs=[
    C("basic", "What is the direction of buoyant force?", "Vertically upward", ["Perpendicularly upward", "In the same direction as gravity", "In the direction of the liquid's flow"],
      "Buoyant force always points vertically upward."),
    C("basic", "An object weighs 8 N in air, and a scale reads 5 N when it is submerged in water. What is the buoyant force on the object?", "3 N", ["13 N", "8 N", "5 N"],
      "Using the weight-difference method, F_b = G - F_reading = 8 - 5 = 3 N.", verify="8-5"),
    C("standard", "An object is fully submerged in water and moves farther downward without touching the bottom. How does its buoyant force change?", "It stays the same", ["It increases", "It decreases", "It first increases and then decreases"],
      "Once fully submerged, the object's displaced volume does not change, so its buoyant force stays the same. Buoyant force is independent of depth."),
    C("standard", "What causes buoyant force?", "The difference between the liquid's upward and downward pressure forces on the object", ["The object displaces liquid", "The liquid has weight", "The object has mass"],
      "The upward pressure force on the lower surface is greater than the downward pressure force on the upper surface. The difference is the buoyant force."),
  ])

T("archimedes", (V, "Chapter 10", "Buoyancy", "10.2"), "Archimedes' Principle", "运动和相互作用", "procedural",
  "State Archimedes' principle: an object immersed in a liquid experiences an upward buoyant force equal to the weight of the liquid it displaces, F_b = G_displaced = ρ_liquid g V_displaced.",
  ["State Archimedes' principle", "Calculate using F_b = ρ_liquid g V_displaced", "Explain how displaced volume relates to object volume (they are equal when fully submerged)"],
  [("2.2.9", "exact")], pre=[("buoy", "hard"), ("density", "hard"), ("gravity", "hard")],
  qs=[
    C("basic", "According to Archimedes' principle, what is the magnitude of the buoyant force on an object?",
      "The weight of the liquid it displaces", ["The object's weight", "The object's mass", "The total weight of the liquid"],
      "F_b = G_displaced: buoyant force equals the weight of the displaced liquid, not the object's own weight."),
    N("standard", "An iron block with a volume of 2×10⁻⁴ m³ is fully submerged in water. What is the buoyant force on it, in N? (Take g = 10 N/kg; enter a number only.)", "2",
      "F_b = ρ_water g V_displaced = 1000 × 10 × 2×10⁻⁴ = 2 N.", "1000*10*2e-4"),
    C("basic", "The same iron block is submerged in water and then in alcohol. In which liquid does it experience greater buoyant force?", "In water", ["In alcohol", "The forces are equal", "It cannot be determined"],
      "The displaced volumes are the same, and water is denser than alcohol. Therefore, F_b = ρ_liquid g V_displaced is greater in water."),
    C("advanced", "An object submerged in water experiences a buoyant force of 5 N. What is its volume? (Take g = 10 N/kg.)", "5×10⁻⁴ m³", ["5×10⁻³ m³", "5 m³", "0.5 m³"],
      "V = V_displaced = F_b/(ρ_water g) = 5 ÷ (1000 × 10) = 5×10⁻⁴ m³."),
  ])

T("float_sink", (V, "Chapter 10", "Buoyancy", "10.3"), "Floating and Sinking: Conditions and Applications", "运动和相互作用", "reasoning",
  "Determine whether an object floats or sinks by comparing F_b with G or ρ_object with ρ_liquid. Know that a floating object has F_b = G, and learn the principles behind ships, submarines, balloons, and hydrometers.",
  ["Determine whether an object floats or sinks by comparing buoyant force with weight or comparing densities", "Know that a floating or neutrally buoyant object has F_b = G", "Explain how a submarine changes its weight to rise or sink"],
  [("2.2.9", "exact")], pre=[("archimedes", "hard"), ("balance2", "hard")],
  qs=[
    C("basic", "What eventually happens when a solid object with a lower density than a liquid is placed in it?", "It floats", ["It sinks", "It remains suspended", "It sinks to the bottom"],
      "If ρ_object < ρ_liquid, the object rises and eventually floats. If the densities are equal, it remains suspended; if ρ_object > ρ_liquid, it sinks."),
    C("basic", "What does a submarine change to rise and sink?", "Its weight", ["The buoyant force on it", "The density of seawater", "Its own volume"],
      "When fully submerged, the submarine's buoyant force stays the same. It changes its weight by taking water into or pumping water out of its ballast tanks."),
    C("standard", "How does the buoyant force on a ship change when it sails from a river into the sea?", "It stays the same", ["It increases", "It decreases", "It cannot be determined"],
      "The ship floats in both places, so F_b = G_ship. Its weight and buoyant force stay the same. Because seawater is denser, the ship rides higher."),
    C("standard", "A wooden block weighing 6 N floats on water. What is the buoyant force on it?", "6 N", ["Greater than 6 N", "Less than 6 N", "0 N"],
      "A floating object has buoyant force equal to its weight, so F_b = 6 N.", verify="6"),
  ])

T("hydrometer", (V, "Chapter 10", "Buoyancy", "10.4"), "Interdisciplinary Project: Build a Miniature Hydrometer", "跨学科实践", "application",
  "Build a simple hydrometer using the floating condition. Understand that it experiences the same buoyant force in different liquids, that it sinks less deeply in denser liquids, and that its scale values increase from top to bottom.",
  ["Explain that a hydrometer uses the floating condition F_b = G", "Describe the distribution of marks on a hydrometer scale"],
  [("5.1.1", "inferred"), ("2.2.9", "exact")], pre=[("float_sink", "hard")],
  qs=[
    C("basic", "The same hydrometer floats in different liquids. How do the buoyant forces on it compare?", "They are equal", ["The force is greater in the denser liquid", "The force is greater in the less dense liquid", "They cannot be compared"],
      "When floating, the buoyant force equals the hydrometer's weight, so it is the same in every liquid."),
    C("basic", "A hydrometer sinks deeper into a liquid. What does this indicate about the liquid's density?", "It is lower", ["It is higher", "It is unchanged", "It is unrelated to immersion depth"],
      "For a fixed buoyant force, F_b = ρ_liquid g V_displaced. The greater the displaced volume, the lower the liquid density."),
    C("standard", "How do the values on a hydrometer's scale change from top to bottom?", "They increase from top to bottom", ["They decrease from top to bottom", "They stay the same", "They are greatest in the middle"],
      "The denser the liquid, the less deeply the hydrometer sinks, so the liquid surface aligns with a lower mark. Thus, scale values increase from top to bottom."),
    C("standard", "When making a hydrometer from a straw and copper wire, why wrap the wire around the bottom of the straw?", "To lower the center of gravity so the straw floats upright", ["To increase buoyant force", "To reduce weight", "To make the straw sink to the bottom"],
      "The copper wire lowers the center of gravity, allowing the hydrometer to float upright in a liquid."),
  ])

# ---------------- Chapter 11: Work and Mechanical Energy
T("work", (V, "Chapter 11", "Work-and-Mechanical-Energy", "11.1"), "Work", "能量", "procedural",
  "Know the two requirements for work to be done: a force acts on an object, and the object moves in the direction of that force. Calculate work using W = Fs, measured in joules (J).",
  ["Determine whether a force does work on an object", "Calculate work using W = Fs"],
  [("3.1.3", "exact"), ("3.2.2", "exact")], pre=[("force", "hard"), ("gravity", "hard")],
  qs=[
    C("basic", "In which situation does a person do work on an object?", "Carrying a box from the floor to a table", ["Carrying a bucket at constant velocity along a level path", "Pushing a car that does not move", "Holding a barbell motionless overhead"],
      "Work requires a force and displacement in the direction of that force. When carrying a bucket horizontally, the force is vertical while the displacement is horizontal, so no work is done."),
    N("basic", "A 50 N horizontal force pushes a box 4 m along a horizontal floor. How much work does the force do, in J? (Enter a number only.)", "200", "W = Fs = 50 × 4 = 200 J.", "50*4"),
    N("standard", "A person lifts a 20 N backpack from the floor onto a table 1.5 m high. What is the minimum work done on the backpack, in J? (Enter a number only.)", "30",
      "W = Gh = 20 × 1.5 = 30 J.", "20*1.5"),
    C("standard", "A soccer ball is kicked and rolls 20 m across grass. How much work does the foot do on the ball while it is rolling?", "0 J", ["It cannot be calculated", "The ball's weight times 20 m", "The kicking force times 20 m"],
      "The foot is no longer in contact with the ball as it rolls, so it exerts no force on the ball and does no work.", verify="0"),
  ])

T("power", (V, "Chapter 11", "Work-and-Mechanical-Energy", "11.2"), "Power", "能量", "procedural",
  "Understand that power measures how quickly work is done, P = W/t, and is measured in watts (W). Derive and use P = Fv.",
  ["Calculate power using P = W/t", "Distinguish work from power", "Perform simple calculations using P = Fv"],
  [("3.2.2", "exact")], pre=[("work", "hard"), ("speed", "hard")],
  qs=[
    C("basic", "What physical quantity does power describe?", "How quickly work is done", ["How much work is done", "The magnitude of a force", "The amount of energy"],
      "Power measures how quickly work is done. Doing more work does not necessarily mean having greater power."),
    N("basic", "A crane does 5×10⁴ J of work in 10 s. What is its power, in W? (Enter a number only.)", "5000", "P = W/t = 50000 ÷ 10 = 5000 W.", "5e4/10"),
    C("standard", "Why does a driver usually shift to a lower gear when a car climbs a hill?", "At constant power, reducing speed increases the driving force", ["To increase power", "To save fuel", "To increase speed"],
      "From P = Fv, a lower speed means a greater driving force when power is constant."),
    N("standard", "A car travels at a constant 20 m/s with a driving force of 3000 N. What is the engine's power, in W? (Enter a number only.)", "60000", "P = Fv = 3000 × 20 = 60000 W.", "3000*20"),
  ])

T("kinetic", (V, "Chapter 11", "Work-and-Mechanical-Energy", "11.3"), "Kinetic and Potential Energy", "能量", "conceptual",
  "Know about kinetic, gravitational potential, and elastic potential energy. Explain that kinetic energy depends on mass and speed, gravitational potential energy on mass and height, and elastic potential energy on the extent of elastic deformation.",
  ["State the factors that affect kinetic and gravitational potential energy", "Analyze an experiment on kinetic energy using controlled variables"],
  [("3.2.1", "exact"), ("3.1.1", "inferred")], pre=[("work", "hard")],
  qs=[
    C("basic", "Which factors affect the magnitude of kinetic energy?", "Mass and speed", ["Mass and height", "Speed and height", "Speed only"],
      "An object's kinetic energy increases with its mass and speed."),
    C("basic", "What type of energy does a raised hammer have?", "Gravitational potential energy", ["Kinetic energy", "Elastic potential energy", "Internal energy only"],
      "An elevated object has gravitational potential energy."),
    C("standard", "In an experiment investigating how kinetic energy depends on speed, the same ball rolls from rest down an incline from different heights. What is the purpose?",
      "Keep mass constant while changing the ball's speed at the bottom", ["Keep speed constant while changing mass", "Change gravitational potential energy, which is unrelated to speed", "Make the ball roll farther"],
      "Using the same ball keeps its mass constant. Releasing it from different heights changes its speed at the bottom."),
    C("standard", "Why is the speed limit for heavy trucks lower than for cars?", "At the same speed, a heavier vehicle has greater kinetic energy and poses greater danger", ["Heavy trucks have less inertia", "Heavy trucks have less gravitational potential energy", "Heavy trucks stop in a shorter distance"],
      "Kinetic energy depends on mass. At the same speed, a heavy truck has greater kinetic energy, so a crash can cause greater harm. That is why its speed limit is lower."),
  ])

T("mech_energy", (V, "Chapter 11", "Work-and-Mechanical-Energy", "11.4"), "Mechanical Energy and Its Transformations", "能量", "reasoning",
  "Know that mechanical energy is the sum of kinetic and potential energy. Analyze transformations between kinetic and potential energy, and explain that mechanical energy is conserved when only kinetic and potential energy transform into each other.",
  ["Analyze energy transformations in a yo-yo, pendulum, artificial satellite, and similar systems", "Explain that mechanical energy is conserved when air resistance is neglected"],
  [("3.2.1", "exact"), ("3.1.2", "inferred")], pre=[("kinetic", "hard")],
  qs=[
    C("basic", "An apple accelerates as it falls from a tree. How is its energy transformed?", "Gravitational potential energy is transformed into kinetic energy", ["Kinetic energy is transformed into gravitational potential energy", "Kinetic energy is transformed into elastic potential energy", "No energy is transformed"],
      "As the apple's height decreases and its speed increases, gravitational potential energy is transformed into kinetic energy."),
    C("basic", "How is energy transformed as an artificial satellite moves from perigee to apogee?", "Kinetic energy is transformed into gravitational potential energy", ["Gravitational potential energy is transformed into kinetic energy", "Mechanical energy is transformed into internal energy", "Both kinetic and potential energy increase"],
      "From perigee to apogee, the satellite's height increases and its speed decreases, so kinetic energy is transformed into gravitational potential energy."),
    C("standard", "Neglecting air resistance, how does the mechanical energy of a ball thrown vertically upward change as it rises?", "It stays the same", ["It increases", "It decreases", "It first increases and then decreases"],
      "Only kinetic and gravitational potential energy transform into each other, so mechanical energy is conserved."),
    C("standard", "A ball falls from a height and bounces to a lower height each time. What does this show?", "Some mechanical energy is transformed into internal energy", ["Mechanical energy is conserved", "The ball's mass decreases", "The ball's weight decreases"],
      "Air resistance and deformation during impact transform some mechanical energy into internal energy, so the ball's mechanical energy decreases."),
  ])

# ---------------- Chapter 12: Simple Machines
_FIG_LEVER = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 260 150"><line x1="20" y1="70" x2="240" y2="70" stroke="currentColor" stroke-width="5" stroke-linecap="round"/>'
  '<path d="M110 72 L98 100 L122 100 Z" fill="currentColor" fill-opacity="0.18" stroke="currentColor" stroke-width="2"/>'
  '<line x1="30" y1="70" x2="30" y2="110" stroke="currentColor" stroke-width="2"/><rect x="18" y="110" width="24" height="24" fill="currentColor" fill-opacity="0.18" stroke="currentColor" stroke-width="2"/>'
  '<line x1="230" y1="70" x2="230" y2="120" stroke="currentColor" stroke-width="2.4"/><path d="M224 110 L230 124 L236 110 Z" fill="currentColor"/>'
  '<text x="10" y="148" font-size="13" fill="currentColor">G = 60 N</text><text x="200" y="140" font-size="13" fill="currentColor">F</text>'
  '<line x1="30" y1="40" x2="110" y2="40" stroke="currentColor" stroke-width="1.4"/><text x="55" y="34" font-size="13" fill="currentColor">0.4 m</text>'
  '<line x1="110" y1="40" x2="230" y2="40" stroke="currentColor" stroke-width="1.4"/><text x="152" y="34" font-size="13" fill="currentColor">1.2 m</text>'
  '<text x="104" y="116" font-size="13" fill="currentColor">O</text></svg>')

T("lever", (V, "Chapter 12", "Simple-Machines", "12.1"), "Levers", "运动和相互作用", "procedural",
  "Identify the five elements of a lever and draw moment arms. Investigate and apply the equilibrium condition F₁l₁ = F₂l₂, and distinguish force-multiplying, force-reducing, and equal-arm levers.",
  ["Locate the fulcrum and draw a moment arm (the perpendicular distance from the fulcrum to the force's line of action)", "Calculate using F₁l₁ = F₂l₂", "Identify force-multiplying and force-reducing levers"],
  [("2.2.6", "exact"), ("4.2.5", "exact")], pre=[("balance2", "hard"), ("gravity", "hard")],
  math=[("cnm_p211", "The lever equilibrium condition F₁l₁ = F₂l₂ is solved using proportions."), ("cnm_p214", "For a fixed load and load arm, effort is inversely proportional to the effort arm.")],
  qs=[
    C("basic", "Which tool is a force-reducing lever?", "A fishing rod", ["A crowbar", "A nutcracker", "A bottle opener"],
      "A fishing rod has an effort arm shorter than its load arm, so it is a force-reducing lever, though it increases distance. The others are force-multiplying levers."),
    C("basic", "What is a moment arm?", "The perpendicular distance from the fulcrum to the force's line of action", ["The distance from the fulcrum to the point where the force is applied", "The distance between the points where effort and load are applied", "The length of the lever"],
      "A moment arm is the perpendicular distance from the fulcrum to a force's line of action, not the distance to its point of application."),
    C("standard", "As shown, a light lever balances horizontally. A 60 N load hangs on the left, with a left moment arm of 0.4 m. A downward force F on the right has a moment arm of 1.2 m. What is F?", "20 N", ["180 N", "60 N", "30 N"],
      "From F₁l₁ = F₂l₂: 60 × 0.4 = F × 1.2, so F = 20 N.", verify="60*0.4/1.2", figure=_FIG_LEVER),
    C("standard", "Why should a lever be balanced horizontally when investigating its equilibrium condition?", "The moment arms can be read directly from the lever", ["The lever is then unaffected by gravity", "The force required is smaller", "The result is more general"],
      "When the lever is horizontal and the forces are vertical, each moment arm lies along the lever and can be read directly."),
  ])

T("steelyard", (V, "Chapter 12", "Simple-Machines", "12.2"), "Interdisciplinary Project: Build a Simple Steelyard", "跨学科实践", "application",
  "Use the lever equilibrium condition to design and build a simple steelyard, determine its zero mark and scale, and learn about the ingenuity of this traditional Chinese balance.",
  ["Explain how a steelyard works using the lever equilibrium condition", "Know that the steelyard scale is uniform"],
  [("5.2.1", "exact"), ("2.2.6", "exact")], pre=[("lever", "hard")],
  qs=[
    C("basic", "Which principle does a steelyard use to measure an object's mass?", "The lever equilibrium condition", ["Equilibrium of two forces", "Archimedes' principle", "The principle of communicating vessels"],
      "A steelyard is a lever. Moving the counterweight changes the moment arm until the steelyard is balanced."),
    C("basic", "What is the spacing of the marks on a steelyard scale?", "Uniform", ["They become closer together farther from the pivot", "They become farther apart farther from the pivot", "There is no regular pattern"],
      "The object's mass is linearly related to the distance from the pivot to the counterweight, so the scale is uniform."),
    C("standard", "How will a steelyard reading change if its counterweight is worn down?", "It will read too high", ["It will read too low", "It will not change", "The scale will be unreadable"],
      "A lighter counterweight must be moved farther out to balance the same object, resulting in a higher reading."),
    N("standard", "A simple steelyard has a 5 cm distance between its suspension point and hook. Its counterweight has a mass of 100 g and balances an object when hung 20 cm on the other side of the suspension point. Neglect the mass of the beam. What is the object's mass, in g? (Enter a number only.)",
      "400", "m_object × 5 = 100 × 20, so m_object = 400 g.", "100*20/5"),
  ])

T("pulley", (V, "Chapter 12", "Simple-Machines", "12.3"), "Pulleys", "运动和相互作用", "procedural",
  "Know that a fixed pulley changes the direction of a force but does not reduce its magnitude, while a movable pulley halves the required force but increases the distance pulled. Count the rope segments supporting the load in a pulley system and use F = (G_load + G_pulley)/n and s = nh.",
  ["Describe the properties of fixed and movable pulleys", "Count the rope segments n supporting a load in a pulley system", "Calculate using F = (G_load + G_pulley)/n and s = nh"],
  [("2.2.6", "exact")], pre=[("lever", "hard")],
  qs=[
    C("basic", "What type of pulley is at the top of a flagpole, and what does it do?", "A fixed pulley; it changes the direction of the force", ["A movable pulley; it reduces the force", "A fixed pulley; it reduces the force", "A movable pulley; it changes the direction of the force"],
      "The pulley at the top of a flagpole does not move with the flag, so it is a fixed pulley that changes the direction of the force."),
    C("basic", "A movable pulley raises a 100 N object at constant velocity. Neglect the pulley’s weight and friction. What is the pulling force?", "50 N", ["100 N", "200 N", "25 N"],
      "A movable pulley halves the required force: F = G/2 = 50 N.", verify="100/2"),
    N("standard", "A pulley system lifts a 240 N load with three rope segments supporting the load. The movable pulley weighs 30 N. Neglect rope weight and friction. What is the pulling force, in N? (Enter a number only.)", "90",
      "F = (G_load + G_pulley)/n = (240 + 30) ÷ 3 = 90 N.", "(240+30)/3"),
    C("standard", "A pulley system with three rope segments supporting the load raises an object by 2 m. How far must the free end of the rope be pulled?", "6 m", ["2 m", "3 m", "0.67 m"],
      "s = nh = 3 × 2 = 6 m. The pulley system reduces force but increases the distance pulled.", verify="3*2"),
  ])

T("efficiency", (V, "Chapter 12", "Simple-Machines", "12.4"), "Mechanical Efficiency", "能量", "procedural",
  "Distinguish useful work, wasted work, and total work. Use mechanical efficiency η = W_useful/W_total, which is always less than 1, and learn ways to improve efficiency.",
  ["Distinguish useful, wasted, and total work", "Calculate the efficiency of pulley systems and inclined planes", "Describe ways to improve mechanical efficiency"],
  [("3.2.3", "exact"), ("3.5.2", "inferred")], pre=[("pulley", "hard"), ("work", "hard")],
  math=[("cnm_p129", "Mechanical efficiency is expressed as a percentage.")],
  qs=[
    C("basic", "When using any machine, how does its efficiency compare with 1 (100%)?", "It is less than 1 (100%)", ["Greater than 1", "Equal to 1", "It can be greater than 1"],
      "Using a machine always involves some wasted work, so useful work is less than total work and efficiency is below 100%."),
    C("basic", "A pulley system lifts a load with 600 J of useful work and 800 J of total work. What is its efficiency?", "75%", ["133%", "25%", "80%"],
      "η = W_useful/W_total = 600 ÷ 800 = 75%.", verify="'75%'"),
    N("standard", "An inclined plane pushes a 500 N box onto a platform 1 m high. The force along the plane is 250 N, and the plane is 4 m long. What is the plane's efficiency, in percent? (Enter a number only.)", "50",
      "W_useful = Gh = 500 J, W_total = Fs = 1000 J, and η = 500 ÷ 1000 = 50%.", "500*1/(250*4)*100", percent=True),
    C("standard", "The same pulley system is used to lift different loads. Which action can increase its efficiency?", "Increase the weight of the object being lifted", ["Increase the lifting height", "Increase the lifting speed", "Increase the weight of the movable pulley"],
      "When wasted work stays approximately constant, a heavier load increases the share of useful work and therefore increases efficiency. Lifting height and speed do not affect efficiency."),
  ])
