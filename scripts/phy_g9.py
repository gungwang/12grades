"""Grade 9 complete volume (PEP edition, revised under the 2022 curriculum standard and used from Fall 2025): Chapters 13–22."""
# Chinese subscripts in assessed physics formula notation are retained unchanged.
from phy_lib import T, C, N

V = "Grade 9 (Complete Volume)"
CH = {13: ("Chapter 13", "Internal Energy"), 14: ("Chapter 14", "Using Internal Energy"), 15: ("Chapter 15", "Electric Current and Circuits"),
      16: ("Chapter 16", "Voltage and Resistance"), 17: ("Chapter 17", "Ohm's Law"), 18: ("Chapter 18", "Electric Power"),
      19: ("Chapter 19", "Electricity in Daily Life"), 20: ("Chapter 20", "Electricity and Magnetism"), 21: ("Chapter 21", "Electromagnetic Waves and Their Applications"),
      22: ("Chapter 22", "Energy and Sustainable Development")}


def S(ch, n):
    return (V, CH[ch][0], CH[ch][1], f"{ch}.{n}")


# Series circuit: source, switch, R1, and R2; the ammeter is in series and the voltmeter is across R1.
_FIG_CIRCUIT = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 190" fill="none" stroke="currentColor" stroke-width="2">'
  '<path d="M30 40 H70 M114 40 H160 M204 40 H250 V87 M250 113 V160 H129 M117 160 H30 V40"/>'
  '<rect x="70" y="30" width="44" height="20"/><text x="84" y="24" font-size="13" fill="currentColor" stroke="none">R₁</text>'
  '<rect x="160" y="30" width="44" height="20"/><text x="174" y="24" font-size="13" fill="currentColor" stroke="none">R₂</text>'
  '<circle cx="250" cy="100" r="13"/><text x="245" y="105" font-size="14" fill="currentColor" stroke="none">A</text>'
  '<line x1="117" y1="146" x2="117" y2="174"/><line x1="129" y1="152" x2="129" y2="168" stroke-width="4"/>'
  '<text x="111" y="188" font-size="12" fill="currentColor" stroke="none">Power source</text>'
  '<path d="M50 40 V90 H79 M105 90 H134 V40"/>'
  '<circle cx="92" cy="90" r="13"/><text x="87" y="95" font-size="14" fill="currentColor" stroke="none">V</text>'
  '<circle cx="50" cy="40" r="2.5" fill="currentColor"/><circle cx="134" cy="40" r="2.5" fill="currentColor"/></svg>')

# ---------------- 13 Internal Energy
T("heat_c", S(13, 1), "Heat and Specific Heat Capacity", "Energy", "procedural",
  "Understand that heat is the amount of internal energy transferred during heat transfer; learn about specific heat capacity through experiments; use Q = cmΔt to calculate heat absorbed or released; and explain everyday phenomena using water's high specific heat capacity.",
  ["Use Q = cmΔt to calculate", "Know that water's specific heat capacity is 4.2×10³ J/(kg·℃) and explain its applications", "Know that specific heat capacity is a property of a substance"],
  [("3.3.1", "exact"), ("3.3.2", "exact")], pre=[("temperature", "hard"), ("mass", "hard")],
  math=[("cnm_022", "Heat is often written in scientific notation.")],
  qs=[
    N("basic", "How much heat, in J, is absorbed when 2 kg of water warms by 10 ℃? (c水 = 4.2×10³ J/(kg·℃); enter the number only.)", "84000",
      "Q = cmΔt = 4200 × 2 × 10 = 84000 J.", "4.2e3*2*10"),
    C("basic", "Why is the day-to-night temperature range smaller in coastal areas than inland?", "Water has a high specific heat capacity", ["It has a high density", "It has a high boiling point", "It has a high heating value"],
      "Because water has a high specific heat capacity, its temperature changes less when it absorbs or releases the same amount of heat."),
    C("standard", "If half a glass of water is poured out, what happens to the specific heat capacity of the remaining water?", "It stays the same", ["It becomes half as large", "It doubles", "It cannot be determined"],
      "Specific heat capacity is a property of a substance and does not depend on its mass."),
    N("standard", "A 0.5 kg metal sample absorbs 4.6×10³ J of heat and warms by 20 ℃. What is its specific heat capacity in J/(kg·℃)? (Enter the number only.)", "460",
      "c = Q/(mΔt) = 4600 ÷ (0.5 × 20) = 460 J/(kg·℃).", "4.6e3/(0.5*20)"),
  ], root=None)

T("molecule", S(13, 2), "Introduction to the Kinetic Theory of Matter", "Matter", "conceptual",
  "Know that matter is made of molecules and atoms; molecules are in constant random motion, which becomes more vigorous as temperature rises (diffusion); molecules attract and repel one another and have spaces between them.",
  ["Use diffusion to explain that molecules are moving", "Know that molecular motion becomes more vigorous as temperature rises", "Know that molecules attract and repel one another"],
  [("1.3.1", "exact"), ("2.1.2", "exact")], root="The kinetic theory of matter is the starting point for Grade 9 thermal physics. In Grade 8, students studied only macroscopic states of matter and mass, so there is no more basic physics prerequisite.",
  qs=[
    C("basic", "What does smelling a flower when you enter a garden show?", "Molecules are in constant random motion", ["Molecules attract one another", "Molecules repel one another", "Molecules are very large"],
      "Fragrant molecules move through the air and enter the nose; this is diffusion."),
    C("basic", "Which phenomenon shows that molecules are moving?", "Sugar dissolves in hot water, making it taste sweet", ["Dust rises while sweeping", "Snowflakes fall", "Willow fluff blows through the air"],
      "Dust, snowflakes, and willow fluff are visible objects undergoing mechanical motion, not molecular motion."),
    C("standard", "Two clean lead blocks can be pressed together strongly enough to lift a weight. What does this show?", "Molecules attract one another", ["Molecules repel one another", "Molecules are constantly moving", "Lead blocks are magnetic"],
      "When pressed together, the molecules are very close, and the attraction between them holds the blocks together."),
    C("standard", "Red ink is added to separate cups of cold and hot water. In which cup does the color spread faster?", "The hot water", ["The cold water", "At the same rate", "Cannot be determined"],
      "The higher the temperature, the more vigorous the random molecular motion and the faster diffusion occurs."),
  ])

T("internal", S(13, 3), "Internal Energy", "Energy", "conceptual",
  "Know that internal energy is the sum of the kinetic and potential energies of all molecules in an object and that every object has internal energy; know that work and heat transfer are two ways to change it; distinguish temperature, heat, and internal energy.",
  ["Name and give examples of the two ways to change internal energy", "Know that every object has internal energy", "Distinguish temperature, heat, and internal energy"],
  [("3.3.1", "exact"), ("3.1.2", "inferred")], pre=[("molecule", "hard"), ("heat_c", "soft")],
  qs=[
    C("basic", "Rubbing your hands together to warm them in winter changes their internal energy by which process?", "Work", ["Heat transfer", "Thermal radiation", "Molecular diffusion"],
      "Rubbing does work against friction, converting mechanical energy into internal energy."),
    C("basic", "Which statement is correct?", "Every object has internal energy", ["Ice at 0 ℃ has no internal energy", "A hotter object contains more heat", "An object's internal energy can increase only by absorbing heat"],
      "Every object has internal energy. Heat is energy in transfer, so an object cannot \"contain\" heat; internal energy can also increase when work is done on it."),
    C("standard", "Using a hot-water bottle to warm your hands changes their internal energy by which process?", "Heat transfer", ["Work", "Friction", "Compression"],
      "Heat flows from the hot-water bottle to your hands; this is heat transfer."),
    C("standard", "A crystal continues to absorb heat as it melts, while its temperature stays constant. What happens to its internal energy?", "It increases", ["It stays the same", "It decreases", "It first decreases, then increases"],
      "Absorbing heat increases internal energy; a constant temperature does not mean internal energy is constant."),
  ])

# ---------------- 14 Using Internal Energy
T("energy_cons", S(14, 1), "Energy Transformation and Conservation", "Energy", "conceptual",
  "Know that energy is neither created nor destroyed; it only changes form or transfers between objects, so the total amount stays constant. Know that a perpetual-motion machine is impossible.",
  ["State the law of conservation of energy", "Analyze energy transformations in common processes", "Explain why a perpetual-motion machine is impossible"],
  [("3.5.1", "exact"), ("3.1.2", "exact"), ("3.5.3", "inferred")], pre=[("internal", "hard"), ("mech_energy", "hard")],
  qs=[
    C("basic", "According to the law of conservation of energy, what happens to the total amount of energy during transformation and transfer?", "It stays constant", ["It gradually decreases", "It gradually increases", "It first increases, then decreases"],
      "Energy is neither created nor destroyed, so the total amount stays constant."),
    C("basic", "What is the main energy transformation when an electric fan operates?", "Electrical energy changes into mechanical energy", ["Mechanical energy changes into electrical energy", "Internal energy changes into electrical energy", "Chemical energy changes into electrical energy"],
      "The fan uses electrical energy, and its rotating blades gain mechanical energy."),
    C("standard", "Why is it impossible to build a \"perpetual-motion machine\"?", "It would violate the law of conservation of energy", ["The materials are not strong enough", "Technology is not advanced enough", "It would need too much electricity"],
      "Doing work continuously without consuming energy would violate the law of conservation of energy."),
    C("standard", "When a car brakes, what does most of its kinetic energy become?", "Internal energy", ["Electrical energy", "Chemical energy", "Gravitational potential energy"],
      "Friction between the brake pads and wheels produces heat, converting kinetic energy into internal energy; this energy does not spontaneously turn back into kinetic energy (energy transformations have a direction)."),
  ])

T("engine", S(14, 2), "Heat Engines", "Energy", "conceptual",
  "Understand that a heat engine converts internal energy into mechanical energy; know the four strokes of a gasoline engine (intake, compression, power, and exhaust) and their energy transformations.",
  ["List the four strokes of a gasoline engine in order", "Know that compression converts mechanical energy into internal energy and the power stroke converts internal energy into mechanical energy", "Calculate the number of power strokes from the flywheel speed"],
  [("3.3.3", "exact")], pre=[("internal", "hard"), ("energy_cons", "soft")],
  qs=[
    C("basic", "Which stroke of a gasoline engine converts internal energy into mechanical energy?", "The power stroke", ["The compression stroke", "The intake stroke", "The exhaust stroke"],
      "During the power stroke, expanding gas pushes the piston and converts internal energy into mechanical energy; the compression stroke does the reverse."),
    C("basic", "How is energy transformed during the compression stroke of a gasoline engine?", "Mechanical energy changes into internal energy", ["Internal energy changes into mechanical energy", "Chemical energy changes into electrical energy", "No energy transformation occurs"],
      "The piston does work to compress the gas, converting mechanical energy into internal energy and raising the gas temperature."),
    N("standard", "A single-cylinder, four-stroke gasoline engine has a flywheel speed of 1800 r/min. How many power strokes occur per second? (Enter the number only.)", "15",
      "The flywheel makes 30 revolutions per second. It turns twice for each cycle and produces one power stroke, so there are 15 power strokes per second.", "1800/60/2"),
    C("standard", "How many strokes are there in one operating cycle of a gasoline engine?", "4", ["2", "1", "3"],
      "One operating cycle consists of the intake, compression, power, and exhaust strokes.", verify="4"),
  ])

T("engine_eff", S(14, 3), "Heat-Engine Efficiency", "Energy", "procedural",
  "Know the heating value of fuel and use Q放 = mq to calculate heat released; know that heat-engine efficiency is the ratio of useful work to the energy released by complete fuel combustion; understand ways to improve efficiency.",
  ["Use Q = mq to calculate the heat released by fuel", "Know that heating value is a property of fuel", "Calculate heat-engine efficiency"],
  [("3.3.1", "exact"), ("3.5.2", "exact")], pre=[("engine", "hard"), ("heat_c", "hard")],
  math=[("cnm_022", "Heating values and heat are often calculated using scientific notation.")],
  qs=[
    N("basic", "How much heat, in J, is released by completely burning 0.2 kg of gasoline? (q汽油 = 4.6×10⁷ J/kg; enter the number only.)", "9200000", "Q = mq = 0.2 × 4.6×10⁷ = 9.2×10⁶ J.", "0.2*4.6e7"),
    C("basic", "If half a tank of gasoline is used, what happens to the heating value of the remaining gasoline?", "It stays the same", ["It becomes half as large", "It doubles", "It cannot be determined"],
      "Heating value is a property of fuel and does not depend on its mass."),
    N("standard", "A heat engine releases 1×10⁸ J when its fuel is completely burned, and 3×10⁷ J is converted into useful work. What is its efficiency as a percentage? (Enter the number only.)", "30",
      "η = 3×10⁷ ÷ 1×10⁸ = 30%.", "3e7/1e8*100", percent=True),
    C("standard", "Which measure does not improve the efficiency of a heat engine?", "Using fuel with a higher heating value", ["Burning the fuel more completely", "Reducing heat losses", "Maintaining good lubrication to reduce friction"],
      "Efficiency is the fraction of total energy converted into useful energy; using fuel with a higher heating value does not change this fraction."),
  ])

T("heat_engine_model", S(14, 4), "Interdisciplinary Project: Build a Simple Heat-Engine Model", "Interdisciplinary Project", "application",
  "Design and build a simple heat-engine model (such as a steam boat or a hot-air pinwheel) using the principle that internal energy can do work; analyze its energy transformations and ways to improve efficiency.",
  ["Describe the energy transformations in a simple heat-engine model", "Suggest ways to improve the model's efficiency"],
  [("5.2.2", "exact"), ("3.3.3", "exact")], pre=[("engine_eff", "hard")],
  qs=[
    C("basic", "Water boils in a test tube and the steam pushes out the stopper. Which gasoline-engine stroke does this resemble?", "The power stroke", ["The compression stroke", "The intake stroke", "The exhaust stroke"],
      "The steam does work on the stopper, converting internal energy into mechanical energy, as in the power stroke."),
    C("basic", "Where does the energy that ultimately propels a steam boat (\"putt-putt boat\") come from?", "Heat released by burning fuel", ["The buoyant force of the water", "The force of the air", "The boat's weight"],
      "Burning fuel releases heat; steam jets push the boat, converting internal energy into mechanical energy."),
    C("standard", "After steam pushes out the stopper, a white mist appears at the mouth of the test tube. Why?", "The steam does work, loses internal energy, cools, and condenses", ["The steam absorbs heat and vaporizes", "The stopper heats the air by friction", "Water in the air sublimates"],
      "The steam does work on the stopper, loses internal energy, and cools; it condenses into tiny droplets that form the mist."),
    C("standard", "Which measure would reasonably improve the efficiency of a homemade heat-engine model?", "Add an insulating cover around the heater to reduce heat loss", ["Switch to fuel with a higher heating value", "Make the model heavier", "Increase heat loss"],
      "Reducing heat loss increases the share of energy that is useful; changing the fuel does not change efficiency."),
  ])

# ---------------- 15 Electric Current and Circuits
T("charge", S(15, 1), "Electric Charge", "Motion and Interaction", "conceptual",
  "Understand charging by friction and the two kinds of charge: like charges repel and unlike charges attract; learn about electroscopes, conductors, and insulators; know that atoms contain a nucleus and electrons and that charging by friction transfers electrons.",
  ["State how charges interact", "Know that charging by friction transfers electrons", "Distinguish common conductors from insulators"],
  [("2.4.1", "exact"), ("1.3.2", "exact"), ("1.2.1", "inferred")], pre=[("molecule", "soft")],
  qs=[
    C("basic", "How do electric charges interact?", "Like charges repel and unlike charges attract", ["Like charges attract and unlike charges repel", "All charges attract one another", "All charges repel one another"],
      "Like charges repel; unlike charges attract."),
    C("basic", "Why does a glass rod become positively charged when rubbed with silk?", "The glass rod loses electrons", ["The glass rod gains electrons", "The glass rod gains protons", "Friction creates positive charge"],
      "Charging by friction transfers electrons. The glass rod becomes positive when it loses electrons; charge is not created."),
    C("standard", "Which object is usually a conductor?", "A pencil lead", ["An eraser", "A plastic ruler", "A glass cup"],
      "Pencil lead is made mainly of graphite, which is a conductor."),
    C("standard", "What does it mean when the leaves of an electroscope spread apart?", "The leaves have like charges and repel each other", ["The leaves have unlike charges", "The leaves are uncharged", "The leaves are being pulled by a magnetic force"],
      "An electroscope works on the principle that like charges repel."),
  ])

T("circuit", S(15, 2), "Electric Current and Circuits", "Motion and Interaction", "conceptual",
  "Know how electric current forms and its conventional direction (the direction positive charges move); identify the parts of a circuit (source, electrical device, switch, and wires); read and draw simple circuit diagrams; and distinguish closed, open, and short circuits.",
  ["Name the basic parts of a circuit", "State the conventional direction of current", "Identify closed, open, and short circuits"],
  [("3.4.1", "exact"), ("3.4.4", "exact")], pre=[("charge", "hard")],
  qs=[
    C("basic", "What is the conventional direction of electric current?", "The direction in which positive charges move", ["The direction in which negative charges move", "The direction in which electrons move", "From the negative terminal to the positive terminal outside the source"],
      "Current is defined to flow in the direction positive charges move. Outside a source, it flows from the positive to the negative terminal, opposite to electron motion."),
    C("basic", "What does a source do in a circuit?", "It supplies electrical energy", ["It consumes electrical energy", "It controls whether the circuit is open or closed", "It transmits electrical energy"],
      "A source converts other forms of energy into electrical energy and supplies it to the circuit."),
    C("standard", "What is it called when a wire directly connects the positive and negative terminals of a source?", "A short circuit", ["A closed circuit", "An open circuit", "A broken circuit"],
      "A short circuit can produce a very large current and damage the source, so it must be avoided."),
    C("standard", "What parts are needed at minimum to make a complete circuit?", "A source, an electrical device, a switch, and wires", ["A source and an electrical device", "A source, a switch, and wires", "An electrical device, a switch, and wires"],
      "A complete circuit consists of a source, an electrical device, a switch, and wires."),
  ])

T("series_parallel", S(15, 3), "Series and Parallel Circuits", "Motion and Interaction", "reasoning",
  "Know how series and parallel circuits are connected, build simple examples of each, and identify examples of series or parallel connections in daily life.",
  ["Identify series and parallel circuits from their current paths", "Know that a series-circuit switch controls the whole circuit and a switch on a parallel circuit's main branch controls all branches", "Give examples such as household appliances connected in parallel"],
  [("3.4.4", "exact")], pre=[("circuit", "hard")],
  qs=[
    C("basic", "How are the lights, television, and refrigerator in a home connected?", "In parallel", ["In series", "Some in series and some in parallel", "Cannot be determined"],
      "Household appliances can operate independently without affecting one another, so they are connected in parallel."),
    C("basic", "Two lamps are connected in series. If the filament in one breaks, what happens to the other lamp?", "It goes out too", ["It stays lit", "It gets brighter", "Its brightness stays the same"],
      "A series circuit has only one path for current. A break anywhere stops current throughout the circuit."),
    C("standard", "One classroom switch controls two fluorescent lamps. If one fails, the other stays lit. How are the lamps connected?", "In parallel, with the switch on the main branch", ["In series", "In parallel, with the switch on a branch", "Cannot be determined"],
      "The lamps do not affect one another, so they are in parallel. One switch controls both, so it is on the main branch."),
    C("standard", "Which pair of components is connected in series?", "A switch and the lamp it controls", ["The lamps in a classroom", "Streetlights where the others stay lit if one fails", "A television and refrigerator at home"],
      "A switch must be in series with the device it controls; the other examples are connected in parallel."),
  ])

T("current_meas", S(15, 4), "Measuring Current", "Motion and Interaction", "procedural",
  "Know the units ampere (A) and milliampere (mA). Use an ammeter by connecting it in series, directing current into the \"+\" terminal, selecting a suitable range, and reading it correctly.",
  ["Convert between current units", "Know that an ammeter is connected in series, with current entering the positive terminal and leaving the negative terminal", "Read the ammeter using the selected range"],
  [("3.4.3", "exact"), ("4.1.7", "exact")], pre=[("circuit", "hard")],
  qs=[
    C("basic", "How should an ammeter be connected in a circuit?", "In series with the circuit being measured", ["In parallel across the device being measured", "Directly across the source terminals", "In any way"],
      "An ammeter must be connected in series with the circuit being measured; connecting it directly across the source can burn it out."),
    N("basic", "How many mA is 0.25 A? (Enter the number only.)", "250", "1 A = 1000 mA, so 0.25 A = 250 mA.", "0.25*1000"),
    C("standard", "When using an ammeter, its pointer deflects to the left. What is the likely cause?", "The positive and negative terminals are reversed", ["The selected range is too low", "The selected range is too high", "The ammeter is short-circuited"],
      "The pointer deflects backward when current enters the negative terminal."),
    C("standard", "An ammeter is set to the 0~0.6 A range, but a reading of 1.5 A is taken using the 0~3 A scale. What is the actual current?", "0.3 A", ["1.5 A", "7.5 A", "0.15 A"],
      "The 0~3 A scale gives readings five times those on the 0~0.6 A scale, so the actual current is 1.5 ÷ 5 = 0.3 A.", verify="1.5/5"),
  ])

T("current_rule", S(15, 5), "Current in Series and Parallel Circuits", "Motion and Interaction", "reasoning",
  "Investigate and understand that current is the same at every point in a series circuit and that the current in a parallel circuit's main branch equals the sum of the branch currents.",
  ["Know that current is the same at every point in a series circuit", "Know that main-branch current in a parallel circuit equals the sum of its branch currents", "Use these rules to find an unknown current"],
  [("3.4.4", "exact"), ("4.2.11", "exact")], pre=[("current_meas", "hard"), ("series_parallel", "hard")],
  qs=[
    C("basic", "Two different lamps are connected in series. How are the currents through them related?", "They are equal", ["The brighter lamp has more current", "The dimmer lamp has more current", "Cannot be determined"],
      "Current is the same at every point in a series circuit, regardless of lamp brightness."),
    N("basic", "Two lamps are in parallel and carry currents of 0.3 A and 0.5 A. What is the main-branch current in A? (Enter the number only.)", "0.8", "I = I₁ + I₂ = 0.3 + 0.5 = 0.8 A.", "0.3+0.5"),
    N("standard", "A parallel circuit has a main-branch current of 1.2 A and one branch current of 0.4 A. What is the current in the other branch, in A? (Enter the number only.)", "0.8", "I₂ = I - I₁ = 1.2 - 0.4 = 0.8 A.", "1.2-0.4"),
    C("standard", "When investigating current in a series circuit, why repeat the experiment with lamps of different specifications?", "To make the conclusion more general", ["To reduce measurement error", "To make the lamps brighter", "To protect the ammeter"],
      "Repeating the experiment with different lamps avoids relying on a single case and helps establish a general rule."),
  ])

# ---------------- 16 Voltage and Resistance
T("voltage", S(16, 1), "Voltage", "Motion and Interaction", "procedural",
  "Know that voltage drives current and is measured in volts (V); remember that one dry cell provides 1.5 V and a household circuit provides 220 V; use a voltmeter in parallel across the circuit, with current entering the positive terminal.",
  ["Know common voltage values", "Know that a voltmeter is connected in parallel", "Convert between voltage units"],
  [("3.4.2", "exact"), ("3.4.3", "exact"), ("4.1.8", "exact")], pre=[("circuit", "hard"), ("current_meas", "soft")],
  qs=[
    C("basic", "What is the voltage of a household circuit in China?", "220 V", ["1.5 V", "36 V", "380 V"],
      "A household circuit in China is 220 V; one dry cell provides 1.5 V.", verify="220"),
    C("basic", "How should a voltmeter be connected in a circuit?", "In parallel across the circuit being measured", ["In series with the circuit being measured", "Only across the source terminals", "The same way as an ammeter"],
      "A voltmeter is connected in parallel across the circuit being measured, with current entering the \"+\" terminal."),
    N("standard", "What is the voltage of a battery made by connecting 3 new dry cells in series? (Enter the number only.)", "4.5", "Each cell provides 1.5 V, and series voltages add: 3 × 1.5 = 4.5 V.", "3*1.5"),
    C("standard", "In the circuit shown, which component's voltage is measured by the voltmeter?", "The voltage across R₁", ["The voltage across R₂", "The source voltage", "The voltage across the ammeter"],
      "The voltmeter's terminals connect to the two ends of R₁, so it is in parallel with R₁ and measures its voltage.", figure=_FIG_CIRCUIT),
  ])

T("voltage_rule", S(16, 2), "Voltage in Series and Parallel Circuits", "Motion and Interaction", "reasoning",
  "Investigate and understand that the total voltage across a series circuit equals the sum of the voltages across its parts, while each branch in a parallel circuit has the same voltage as the source.",
  ["Know the series-circuit rule U = U₁ + U₂", "Know that the voltage is the same across each branch of a parallel circuit", "Use these rules to find an unknown voltage"],
  [("3.4.4", "inferred"), ("4.2.11", "exact")], pre=[("voltage", "hard"), ("current_rule", "soft")],
  qs=[
    N("basic", "Two resistors are in series with a 6 V source. The voltage across one resistor is 2 V. What is the voltage across the other, in V? (Enter the number only.)", "4", "U₂ = U - U₁ = 6 - 2 = 4 V.", "6-2"),
    C("basic", "Two lamps are in parallel across a 3 V source. What is the voltage across each lamp?", "3 V", ["1.5 V", "6 V", "0 V"],
      "In a parallel circuit, the voltage across every branch is equal to the source voltage.", verify="3"),
    C("standard", "In the diagram, the source voltage is 6 V and the voltmeter reads 2.5 V. What is the voltage across R₂?", "3.5 V", ["2.5 V", "6 V", "8.5 V"],
      "The voltmeter measures the voltage across R₁. In series, U₂ = 6 - 2.5 = 3.5 V.", verify="6-2.5", figure=_FIG_CIRCUIT),
    C("standard", "A television and a lamp operate at the same time at home. How are the voltages across them related?", "They are equal, at 220 V each", ["The television has a higher voltage", "The lamp has a higher voltage", "Their voltages add to 220 V"],
      "Household appliances are connected in parallel, so each has the same voltage, 220 V."),
  ])

T("resistance", S(16, 3), "Resistance", "Motion and Interaction", "conceptual",
  "Know that resistance measures how much a conductor opposes current and is measured in ohms (Ω); resistance depends on the material, length, cross-sectional area, and temperature, not on voltage or current.",
  ["Name the factors that affect resistance", "Know that resistance is a property of the conductor, independent of voltage and current", "Convert between resistance units"],
  [("3.4.2", "exact"), ("1.2.1", "inferred")], pre=[("voltage", "hard")],
  qs=[
    C("basic", "Which factor does not affect a conductor's resistance?", "The voltage across the conductor", ["The conductor's material", "The conductor's length", "The conductor's cross-sectional area"],
      "Resistance is a property of the conductor and does not depend on whether current flows or on the voltage."),
    C("basic", "Two wires have the same material and cross-sectional area. How does the resistance of the longer wire compare?", "It is greater", ["It is smaller", "It is the same", "It cannot be compared"],
      "With other conditions equal, the longer the conductor, the greater its resistance."),
    N("standard", "How many Ω is 2 kΩ? (Enter the number only.)", "2000", "1 kΩ = 1000 Ω.", "2*1000"),
    C("standard", "A wire is stretched uniformly until it is twice its original length. How does its resistance change?", "It becomes four times as large", ["It doubles", "It stays the same", "It becomes half as large"],
      "Its length doubles and its cross-sectional area halves. Each change doubles the resistance, so the resistance becomes four times as large."),
  ])

T("rheostat", S(16, 4), "Rheostats", "Motion and Interaction", "procedural",
  "Know that a sliding rheostat changes resistance by changing the length of resistance wire in the circuit; connect it correctly (one top and one bottom terminal) and predict how resistance changes as the slider moves; understand its role in a circuit.",
  ["Explain how a sliding rheostat works", "Connect one top and one bottom terminal and predict resistance changes", "Know that the slider should be at the maximum-resistance position before closing the switch"],
  [("3.4.2", "inferred"), ("3.4.4", "inferred")], pre=[("resistance", "hard")],
  qs=[
    C("basic", "How does a sliding rheostat change the resistance?", "By changing the length of resistance wire in the circuit", ["By changing the wire's cross-sectional area", "By changing the wire's material", "By changing the wire's temperature"],
      "Moving the slider changes the length of resistance wire in the circuit, which changes the resistance."),
    C("basic", "A sliding rheostat is labeled \"20 Ω 1 A.\" What does \"20 Ω\" mean?", "The maximum resistance is 20 Ω", ["The minimum resistance is 20 Ω", "The resistance during normal operation is 20 Ω", "The maximum permitted current is 20 A"],
      "20 Ω is the maximum resistance; 1 A is the maximum permitted current."),
    C("standard", "Where should the slider of a sliding rheostat be before the switch is closed?", "At the maximum-resistance position", ["At the minimum-resistance position", "In the middle", "Anywhere"],
      "Set it to maximum resistance to minimize current and protect the circuit."),
    C("standard", "What happens if both lower terminals of a sliding rheostat are connected?", "The resistance stays constant, like a fixed resistor", ["The resistance changes greatly", "The resistance is zero", "The circuit is open"],
      "With both lower terminals connected, the entire resistance wire is in the circuit, so moving the slider does not change resistance."),
  ])

T("dimmer", S(16, 5), "Interdisciplinary Project: Build a Simple Dimmable Desk Lamp", "Interdisciplinary Project", "application",
  "Use knowledge of circuit connections and rheostats to design and build a simple dimmable desk lamp; analyze how slider position affects lamp brightness and follow electrical-safety practices.",
  ["Draw a circuit diagram for a dimmable desk lamp with the lamp and rheostat in series", "Analyze how lamp brightness changes when the slider moves"],
  [("5.1.1", "exact"), ("3.4.4", "inferred")], pre=[("rheostat", "hard")],
  qs=[
    C("basic", "How should the lamp and sliding rheostat be connected in a simple dimmable desk lamp?", "In series", ["In parallel", "Either in parallel or in series", "They do not need to be connected"],
      "The rheostat is connected in series with the lamp; changing its resistance changes the current through the lamp."),
    C("basic", "In a dimmable desk lamp, what happens to the lamp's brightness when the rheostat's resistance in the circuit increases?", "It becomes dimmer", ["It becomes brighter", "It stays the same", "It first brightens, then dims"],
      "The total resistance increases, current decreases, and the lamp becomes dimmer."),
    C("standard", "A pencil lead is used instead of resistance wire in a homemade dimmable lamp. Which property of pencil lead makes this possible?", "It conducts electricity, and its resistance changes with its length", ["It is an insulator", "Its resistance is zero", "It emits light"],
      "Pencil lead conducts electricity, and a longer length has greater resistance, so it can act as a rheostat."),
    C("standard", "Which is a safe way to build a homemade dimmable lamp?", "Use a low-voltage source such as dry cells", ["Connect it directly to a 220 V household circuit", "Adjust it with wet hands", "Leave exposed wires twisted together without insulating tape"],
      "Use a safe low-voltage source and maintain proper insulation and electrical safety."),
  ])

# ---------------- 17 Ohm's Law
T("i_u_r", S(17, 1), "Relationships among Current, Voltage, and Resistance", "Motion and Interaction", "reasoning",
  "Investigate the relationships among current, voltage, and resistance: at constant resistance, current is proportional to voltage; at constant voltage, current is inversely proportional to resistance. Design experiments and analyze data using controlled variables.",
  ["Know that I is proportional to U at constant resistance", "Know that I is inversely proportional to R at constant voltage", "Explain the role of the sliding rheostat in the experiment"],
  [("3.4.2", "exact"), ("4.2.12", "exact")], pre=[("rheostat", "hard"), ("voltage_rule", "soft")],
  math=[("cnm_p213", "At constant resistance, current is proportional to voltage."), ("cnm_p214", "At constant voltage, current is inversely proportional to resistance."), ("cnm_200", "The I–U graph is a straight line through the origin."), ("cnm_237", "The I–R graph is the graph of an inverse-proportion function.")],
  qs=[
    C("basic", "At constant resistance, how is the current through a conductor related to the voltage across it?", "It is directly proportional", ["It is inversely proportional", "They are unrelated", "They are equal"],
      "At constant resistance, current is proportional to voltage."),
    C("basic", "At constant voltage, how is the current through a conductor related to its resistance?", "It is inversely proportional", ["It is directly proportional", "They are unrelated", "They are equal"],
      "At constant voltage, current is inversely proportional to resistance."),
    C("standard", "When investigating the relationship between current and resistance, a 5 Ω resistor is replaced with a 10 Ω resistor. How should the rheostat be adjusted?", "Keep the voltage across the resistor constant", ["Keep the current constant", "Keep the rheostat's resistance constant", "No adjustment is needed"],
      "To investigate the relationship between current and resistance, keep the voltage across the resistor constant."),
    N("standard", "The current through a fixed resistor is 0.2 A at 2 V. What is the current in A when the voltage increases to 6 V? (Enter the number only.)", "0.6",
      "At constant resistance, current is proportional to voltage. The voltage triples, so the current also triples: 0.6 A.", "0.2*6/2"),
  ])

T("ohm", S(17, 2), "Ohm's Law", "Motion and Interaction", "procedural",
  "Understand Ohm's law, I = U/R, and use it and its rearrangements, U = IR and R = U/I, in calculations. Know that R = U/I is only a way to calculate resistance; resistance is not determined by voltage and current.",
  ["Use I = U/R and its rearrangements in calculations", "Match all quantities in the formula to the same conductor and instant", "Understand that R = U/I does not mean resistance is proportional to voltage"],
  [("3.4.2", "exact")], pre=[("i_u_r", "hard")],
  math=[("cnm_041", "Finding a third quantity from two known quantities requires solving an equation."), ("cnm_040", "Rearranging a formula uses the properties of equality.")],
  qs=[
    N("basic", "A 10 Ω resistor has 3 V across it. What is the current in A? (Enter the number only.)", "0.3", "I = U/R = 3 ÷ 10 = 0.3 A.", "3/10"),
    N("basic", "A 20 Ω resistor carries a current of 0.5 A. What is the voltage across it in V? (Enter the number only.)", "10", "U = IR = 0.5 × 20 = 10 V.", "0.5*20"),
    C("standard", "Which statement about R = U/I is correct?", "Resistance is a property of the conductor and is independent of voltage and current", ["Resistance is proportional to voltage", "Resistance is inversely proportional to current", "Resistance is zero when voltage is zero"],
      "R = U/I is only a method for calculating resistance; resistance depends on material, length, cross-sectional area, and temperature."),
    C("standard", "A conductor carries 0.2 A when 4 V is applied. What is its resistance when the voltage across it is 0 V?", "20 Ω", ["0 Ω", "Infinite", "10 Ω"],
      "R = 4 ÷ 0.2 = 20 Ω. Resistance does not depend on voltage, so it remains 20 Ω when the voltage is 0.", verify="4/0.2"),
  ])

T("measure_r", S(17, 3), "Measuring Resistance", "Motion and Interaction", "procedural",
  "Measure resistance using the voltmeter-ammeter method: apply R = U/I, draw and build the circuit, and take repeated measurements to calculate an average. Know that a small lamp's resistance changes with temperature.",
  ["Explain the voltmeter-ammeter method and draw its circuit", "Know that repeated measurements of a fixed resistor should be averaged", "Know that a small lamp's resistance increases with temperature, so its measurements should not be averaged"],
  [("4.1.9", "exact"), ("3.4.3", "exact")], pre=[("ohm", "hard"), ("voltage", "hard")],
  math=[("cnm_211", "Calculate an average from repeated measurements.")],
  qs=[
    C("basic", "What is the principle behind measuring resistance with a voltmeter and ammeter?", "R = U/I", ["P = UI", "I = U + R", "W = UIt"],
      "Measure U with a voltmeter and I with an ammeter, then calculate resistance using R = U/I."),
    C("basic", "When measuring resistance with a voltmeter and ammeter, how should each meter be connected?", "The voltmeter is in parallel with the resistor; the ammeter is in series", ["The voltmeter is in series and the ammeter is in parallel", "Both meters are in series with the resistor", "Both meters are in parallel with the resistor"],
      "A voltmeter is connected in parallel; an ammeter is connected in series."),
    N("standard", "Three measurements of a fixed resistor are 9.8 Ω, 10.0 Ω, and 10.2 Ω. What resistance should be recorded in Ω? (Enter the number only.)", "10",
      "Averaging repeated measurements reduces error: (9.8 + 10.0 + 10.2) ÷ 3 = 10 Ω.", "(9.8+10.0+10.2)/3"),
    C("standard", "When measuring a small lamp's resistance, it differs at different voltages. What is the main reason?", "The filament's resistance increases as its temperature rises", ["The measurement error is too large", "The voltmeter is broken", "The filament's length changes"],
      "A higher voltage raises the filament's temperature and resistance, so the measurements should not be averaged as a single lamp resistance."),
  ])

T("ohm_sp", S(17, 4), "Ohm's Law in Series and Parallel Circuits", "Motion and Interaction", "procedural",
  "Apply Ohm's law and the current and voltage rules for series and parallel circuits. Know that series resistance is R = R₁ + R₂ and that the total resistance of a parallel circuit is less than any branch resistance.",
  ["Find total resistance and current in a series circuit", "Use Ohm's law to solve parallel-circuit problems", "Analyze how meter readings change when the slider moves"],
  [("3.4.2", "exact"), ("3.4.4", "inferred")], pre=[("ohm", "hard"), ("voltage_rule", "hard"), ("current_rule", "hard")],
  math=[("cnm_043", "Finding a part from the total requires setting up a linear equation in one variable.")],
  qs=[
    N("basic", "Two resistors of 5 Ω and 10 Ω are connected in series. What is their total resistance in Ω? (Enter the number only.)", "15", "The total series resistance is R = R₁ + R₂ = 15 Ω.", "5+10"),
    C("standard", "In the diagram, R₁ = 10 Ω, R₂ = 20 Ω, and the source voltage is 6 V. What does the ammeter read?", "0.2 A", ["0.6 A", "0.3 A", "0.9 A"],
      "The total series resistance is 30 Ω, so I = 6 ÷ 30 = 0.2 A. Using only R₁ would give 0.6 A.", verify="6/(10+20)", figure=_FIG_CIRCUIT),
    N("standard", "R₁ = 6 Ω and R₂ = 12 Ω are connected in parallel to a 6 V source. What is the main-branch current in A? (Enter the number only.)", "1.5",
      "I₁ = 6 ÷ 6 = 1 A, I₂ = 6 ÷ 12 = 0.5 A, so the main-branch current is I = 1.5 A.", "6/6+6/12"),
    C("basic", "How does the total resistance of two parallel resistors compare with the smaller resistor?", "It is smaller than the smaller resistor", ["It equals the sum of the two resistances", "It lies between the two resistances", "It is greater than the larger resistor"],
      "A parallel connection is like increasing the conductor's cross-sectional area, so its total resistance is less than either branch resistance."),
  ])

# ---------------- 18 Electric Power
T("elec_energy", S(18, 1), "Electrical Energy and Work", "Energy", "procedural",
  "Know that electrical energy is measured in joules and kilowatt-hours, with 1 kW·h = 3.6×10⁶ J; read an electricity meter and calculate energy use; know the electrical-work formula W = UIt.",
  ["Convert between kW·h and J", "Read an electricity meter and calculate energy use", "Use W = UIt to calculate electrical work"],
  [("3.4.5", "exact"), ("3.4.1", "inferred")], pre=[("ohm", "hard"), ("work", "soft")],
  math=[("cnm_022", "1 kW·h = 3.6×10⁶ J uses scientific notation.")],
  qs=[
    C("basic", "How many joules are in 1 kW·h?", "3.6×10⁶ J", ["3.6×10³ J", "1000 J", "3600 J"],
      "1 kW·h = 1000 W × 3600 s = 3.6×10⁶ J."),
    N("basic", "An electricity meter reads 1235.6 kW·h at the start of the month and 1335.6 kW·h at the end. How much electricity was used, in kW·h? (Enter the number only.)", "100", "Energy used = end-of-month reading - start-of-month reading = 100 kW·h.", "1335.6-1235.6"),
    N("standard", "A 6 V voltage drives a 0.5 A current for 100 s. How much electrical work is done in J? (Enter the number only.)", "300", "W = UIt = 6 × 0.5 × 100 = 300 J.", "6*0.5*100"),
    C("standard", "An electricity meter is labeled \"3000 r/(kW·h).\" What does this mean?", "Its disk turns 3000 times for each 1 kW·h of electricity used", ["It turns 3000 times per hour", "Its maximum power rating is 3000 W", "Each turn of the disk uses 3000 J"],
      "The label 3000 r/(kW·h) means that the disk turns 3000 times for each 1 kW·h used by devices connected to the meter."),
  ])

T("elec_power", S(18, 2), "Electric Power", "Energy", "procedural",
  "Know that electric power measures how quickly current does work, with P = W/t = UI; distinguish rated voltage, rated power, and actual power; perform simple calculations.",
  ["Use P = UI and P = W/t in calculations", "Distinguish rated power from actual power", "Calculate current or resistance from a device label"],
  [("3.4.5", "exact")], pre=[("elec_energy", "hard"), ("power", "soft")],
  qs=[
    N("basic", "A lamp has 220 V across it and carries 0.2 A. What is its electric power in W? (Enter the number only.)", "44", "P = UI = 220 × 0.2 = 44 W.", "220*0.2"),
    N("basic", "A 1000 W electric kettle operates normally for 0.5 h. How much electrical energy does it use in kW·h? (Enter the number only.)", "0.5", "W = Pt = 1 kW × 0.5 h = 0.5 kW·h.", "1*0.5"),
    C("standard", "What determines how bright a lamp is?", "Its actual power", ["Its rated power", "Its rated voltage", "The direction of the current through it"],
      "A lamp's brightness depends on its actual power; greater actual power makes it brighter."),
    C("advanced", "A lamp is labeled \"220 V 100 W.\" What is its resistance when it glows normally?", "484 Ω", ["2.2 Ω", "0.45 Ω", "22000 Ω"],
      "R = U²/P = 220² ÷ 100 = 484 Ω.", verify="220**2/100"),
  ])

T("save_power", S(18, 3), "Interdisciplinary Project: Recommend Ways to Save Electricity at Home", "Interdisciplinary Project", "application",
  "Investigate household electricity use and estimate energy consumption using electrical work and power. Recommend ways to save electricity, such as reducing power or operating time.",
  ["Use W = Pt to estimate household electricity use", "Suggest reasonable ways to save electricity"],
  [("5.1.3", "exact"), ("3.4.7", "inferred")], pre=[("elec_power", "hard")],
  qs=[
    N("basic", "A 100 W television is used for a total of 5 h a day, including standby and viewing. How much electrical energy does it use in a 30-day month, in kW·h? (Enter the number only.)", "15",
      "W = Pt = 0.1 kW × 5 h × 30 = 15 kW·h.", "0.1*5*30"),
    C("basic", "Which action helps save electricity?", "Replace incandescent bulbs with LED bulbs", ["Set the air conditioner to 16 ℃ in summer", "Leave the television on standby for a long time", "Open the refrigerator door frequently"],
      "LED bulbs are more efficient and use less power at the same brightness."),
    N("standard", "A 40 W incandescent bulb is replaced with an equally bright 8 W LED bulb. If it is used for 5 h each day, how much electricity is saved per day in kW·h? (Enter the number only.)", "0.16",
      "Energy saved = (0.04 - 0.008) kW × 5 h = 0.16 kW·h.", "(0.04-0.008)*5"),
    C("standard", "From W = Pt, what are two ways to save electricity?", "Reduce the device's power and shorten its operating time", ["Increase power and extend operating time", "Increase voltage", "Increase current"],
      "From W = Pt, reducing P or t reduces the electrical energy used."),
  ])

T("joule", S(18, 4), "Joule's Law", "Energy", "procedural",
  "Investigate the heating effect of current and learn Joule's law, Q = I²Rt; use it to explain the useful applications of electric heating and how to prevent unwanted heating.",
  ["Use Q = I²Rt in calculations", "Explain phenomena such as why a heating element gets hot while its connecting wire does not", "Give examples of useful and unwanted electric heating"],
  [("3.4.6", "exact")], pre=[("elec_power", "hard")],
  qs=[
    N("basic", "A 2 A current flows through a 10 Ω resistor for 60 s. How much heat, in J, is produced? (Enter the number only.)", "2400", "Q = I²Rt = 2² × 10 × 60 = 2400 J.", "2**2*10*60"),
    C("basic", "A heating element glows red, but the wire connected to it stays relatively cool. What is the main reason?", "The wire's resistance is much lower than the heating element's", ["The current in the wire is lower", "The wire loses heat faster", "There is no current in the wire"],
      "The element and wire are in series, so their currents are equal. From Q = I²Rt, the higher-resistance heating element produces more heat."),
    C("standard", "Which appliance operates using the heating effect of electric current?", "A rice cooker", ["An electric fan", "A television", "A refrigerator"],
      "A rice cooker converts electrical energy mainly into internal energy; a fan converts it mainly into mechanical energy."),
    C("standard", "If current stays constant and the heating time of a resistance wire doubles, how many times greater is the heat produced?", "2 times", ["4 times", "1 time", "0.5 times"],
      "From Q = I²Rt, heat is proportional to time."),
  ])

# ---------------- 19 Electricity in Daily Life
T("safety", S(19, 1), "Electrical Safety", "Energy", "application",
  "Know that a safe voltage for the human body is no higher than 36 V; understand types and causes of electric shock; follow safety rules (do not touch low-voltage live parts or approach high-voltage live parts) and know how to respond to an electric shock.",
  ["Know the safe voltage", "Identify safe and unsafe electrical practices", "Know to cut off the power first if someone is being shocked"],
  [("3.4.7", "exact"), ("5.1.2", "exact")], pre=[("voltage", "hard"), ("ohm", "soft")],
  qs=[
    C("basic", "What voltage is considered safe for the human body?", "No higher than 36 V", ["220 V", "380 V", "No higher than 360 V"],
      "In general, a voltage no higher than 36 V is considered safe for the human body."),
    C("basic", "What should you do first if someone is being shocked?", "Cut off the power immediately", ["Pull the person away with your hands", "Use a wet wooden stick to move the wire", "Shout for help and wait"],
      "Cut off the power first, or use a dry insulating rod to move the wire. Never pull the person with your bare hands."),
    C("standard", "Which action follows electrical-safety rules?", "Turn off the switch before replacing a bulb", ["Unplug a device with wet hands", "Fly a kite near high-voltage power lines", "Plug several high-power devices into one outlet"],
      "Disconnect the power before replacing a bulb or repairing an appliance."),
    C("standard", "Why should you not shelter under a tall tree during a thunderstorm?", "The tree may be struck by lightning, and current could pass through a person", ["The tree could fall over", "The tree cannot block the rain", "The tree absorbs heat"],
      "Tall trees are more likely to be struck by lightning, and the powerful current can injure someone nearby."),
  ])

T("home_circuit", S(19, 2), "Basic Parts of a Household Circuit", "Energy", "conceptual",
  "Identify the parts of a household circuit (incoming wires, electricity meter, main switch, fuse or circuit breaker, outlets, lamps, and switches); distinguish live and neutral wires; use a test screwdriver; explain three-prong plugs and residual-current devices; and identify causes of excessive current.",
  ["List the parts of a household circuit in order", "Use a test screwdriver to distinguish live and neutral wires", "Know the two causes of excessive current: a short circuit and excessive total power"],
  [("3.4.7", "exact")], pre=[("safety", "hard"), ("elec_power", "hard"), ("series_parallel", "hard")],
  qs=[
    C("basic", "When using a test screwdriver to distinguish live and neutral wires, which wire makes its neon lamp glow?", "The live wire", ["The neutral wire", "The ground wire", "Both wires"],
      "The neon lamp glows when the screwdriver touches the live wire. Keep a finger on the metal contact at the end of the handle."),
    C("basic", "What can cause excessive current in a household circuit?", "A short circuit or excessive total power from appliances", ["Voltage that is too low", "Too few appliances", "Wires that are too thick"],
      "A short circuit or excessive total appliance power can cause excessive current in the main circuit."),
    C("standard", "Why do appliances such as washing machines and refrigerators use three-prong plugs?", "To ground the metal casing and prevent electric shock if it becomes live", ["To make the appliance use less electricity", "To hold the plug more securely", "To increase the current"],
      "The third wire in a three-prong plug connects the metal casing to the ground."),
    C("standard", "Which wire should a light switch be connected to?", "The live wire", ["The neutral wire", "The ground wire", "Either wire"],
      "The switch is connected to the live wire, so opening it disconnects the lamp from the live wire and makes bulb replacement safer."),
  ])

T("home_design", S(19, 3), "Interdisciplinary Project: Design a Household Circuit", "Interdisciplinary Project", "application",
  "Combine knowledge of household circuits, electrical safety, and electric power to design a room's circuit: choose appliance connections and switch and outlet locations, estimate total power, and select suitable wires and protective devices.",
  ["Design a circuit with appliances in parallel and switches controlling the live wire", "Estimate main-branch current from total power and select suitable equipment"],
  [("5.1.2", "exact"), ("3.4.7", "exact")], pre=[("home_circuit", "hard")],
  qs=[
    N("basic", "A room uses a 1100 W air conditioner and a 220 W television at the same time. What is the main-branch current in A at 220 V? (Enter the number only.)", "6",
      "Total power is 1320 W, so I = P/U = 1320 ÷ 220 = 6 A.", "(1100+220)/220"),
    C("basic", "When designing a household circuit, how should outlets and lamps in a room be connected?", "In parallel", ["In series", "Outlets in series and lamps in parallel", "Any way"],
      "Household appliances and outlets should be connected in parallel so they can operate independently."),
    C("standard", "An electricity meter is labeled \"220 V 10 A.\" What is the maximum total power of appliances that this household circuit may use at one time?", "2200 W", ["22 W", "220 W", "10 W"],
      "P = UI = 220 × 10 = 2200 W.", verify="220*10"),
    C("standard", "Which is a reasonable way to install a dedicated circuit for a high-power air conditioner?", "Use thicker wire and install a suitable circuit breaker", ["Use thinner wire", "Remove the protective device", "Connect the switch to the neutral wire"],
      "High-power appliances draw more current. Thicker wire reduces heating, and a protective device is needed."),
  ])

# ---------------- 20 Electricity and Magnetism
T("magnet", S(20, 1), "Magnetism and Magnetic Fields", "Motion and Interaction", "conceptual",
  "Know the poles of a magnet and how poles interact; investigate magnetic fields and learn how field lines represent them, with external field lines running from the north pole to the south pole; learn about Earth's magnetic field.",
  ["Know how magnetic poles interact", "Know the direction of magnetic field lines", "Know that Earth's magnetic north pole is near the geographic South Pole"],
  [("2.4.2", "exact"), ("1.2.1", "inferred")], root="Magnetism is the starting point for junior-high electromagnetism. Students previously encountered magnets only in primary-school science, so the physics graph has no more basic prerequisite.",
  qs=[
    C("basic", "How do magnetic poles interact?", "Like poles repel and unlike poles attract", ["Like poles attract and unlike poles repel", "All poles attract one another", "All poles repel one another"],
      "Like magnetic poles repel; unlike poles attract."),
    C("basic", "Outside a magnet, in which direction do magnetic field lines point?", "From the north pole to the south pole", ["From the south pole to the north pole", "From the center toward both poles", "They have no direction"],
      "Outside a magnet, magnetic field lines run from the north pole to the south pole."),
    C("standard", "Where is Earth's magnetic north pole located relative to the geographic poles?", "Near the geographic South Pole", ["Near the geographic North Pole", "Near the equator", "At Earth's center"],
      "Earth's magnetic north pole is near the geographic South Pole, so a compass's north pole points toward geographic north."),
    C("standard", "Which object can be attracted by a magnet?", "An iron nail", ["A copper key", "An aluminum spoon", "A glass cup"],
      "Magnets attract materials such as iron, cobalt, and nickel, but not copper or aluminum."),
  ])

T("current_mag", S(20, 2), "Magnetism from Electric Current", "Motion and Interaction", "reasoning",
  "Learn from Oersted's experiment that current produces a magnetic field; investigate the external field of a current-carrying solenoid and use Ampère's right-hand rule to determine its poles.",
  ["Know that Oersted's experiment showed that current produces a magnetic field", "Use Ampère's right-hand rule to identify a solenoid's north pole", "Know that a solenoid's external magnetic field resembles that of a bar magnet"],
  [("2.4.3", "exact"), ("4.2.9", "exact")], pre=[("magnet", "hard"), ("circuit", "hard")],
  qs=[
    C("basic", "Which scientist first discovered that an electric current produces a magnetic field?", "Oersted", ["Faraday", "Newton", "Ohm"],
      "In 1820, Oersted found that a current-carrying wire deflects a compass needle; Faraday discovered electromagnetic induction."),
    C("basic", "Which magnet's field does the external field of a current-carrying solenoid resemble?", "A bar magnet", ["A horseshoe magnet", "A ring magnet", "It has no magnetic field"],
      "The external field of a current-carrying solenoid resembles that of a bar magnet, with north and south poles at its ends."),
    C("standard", "According to Ampère's right-hand rule, grip a solenoid with your right hand so your fingers point in the direction of current. Which finger points toward its north pole?", "The thumb", ["The index finger", "The little finger", "The wrist"],
      "Grip the solenoid with your right hand, with your fingers pointing in the direction of current; your thumb points toward the north pole."),
    C("standard", "What happens to the magnetic poles of a current-carrying solenoid if the current direction is reversed?", "The north and south poles switch places", ["They stay the same", "The magnetism disappears", "The magnetism becomes stronger"],
      "A solenoid's poles depend on current direction, so reversing the current switches the poles."),
  ])

T("electromagnet", S(20, 3), "Electromagnets and Electromagnetic Relays", "Motion and Interaction", "application",
  "Know that an electromagnet's magnetism can be switched on and off, and that its strength depends on current and coil turns; understand that an electromagnetic relay uses a low-voltage control circuit to switch a high-voltage working circuit.",
  ["Name the factors that affect an electromagnet's strength", "Explain the purpose and principle of an electromagnetic relay", "Give examples of electromagnet applications"],
  [("2.4.3", "exact")], pre=[("current_mag", "hard")],
  qs=[
    C("basic", "Which action can make an electromagnet stronger?", "Increase the number of turns in the coil", ["Reduce the current in the coil", "Remove the iron core", "Reverse the current direction"],
      "A larger current and more coil turns (with an iron core) make the electromagnet stronger; reversing current changes only the poles."),
    C("basic", "Compared with a permanent magnet, what is an advantage of an electromagnet?", "Its magnetism and strength can be controlled", ["Its magnetism never disappears", "It does not need electricity", "It has no poles"],
      "An electromagnet is magnetic when current flows and loses its magnetism when the current stops; its strength can be adjusted by changing the current."),
    C("standard", "What is an electromagnetic relay essentially?", "A switch that uses an electromagnet to control a working circuit", ["A type of power source", "A type of electrical device", "A type of resistor"],
      "An electromagnetic relay uses a low-voltage, low-current control circuit to operate a high-voltage, high-current working circuit."),
    C("standard", "What material is commonly used for the core of an electromagnet?", "Soft iron", ["Steel", "Copper", "Aluminum"],
      "Soft iron loses its magnetism as soon as current stops; steel retains magnetism, while copper and aluminum are not magnetized."),
  ])

T("motor", S(20, 4), "Electric Motors", "Motion and Interaction", "conceptual",
  "Investigate the force on a current-carrying wire in a magnetic field and learn that its direction depends on the current and magnetic-field directions; understand how a motor works, its energy transformation, and the role of the commutator.",
  ["Know that a current-carrying wire experiences a force in a magnetic field and identify the factors that affect its direction", "Know that a motor converts electrical energy into mechanical energy", "Explain the role of a commutator"],
  [("2.4.4", "exact")], pre=[("current_mag", "hard")],
  qs=[
    C("basic", "What principle does an electric motor use?", "A current-carrying wire experiences a force in a magnetic field", ["Electromagnetic induction", "The heating effect of current", "The interaction between electric charges"],
      "A motor uses the force on a current-carrying coil in a magnetic field to make it rotate; electromagnetic induction is the principle behind a generator."),
    C("basic", "What is the main energy transformation when a motor operates?", "Electrical energy changes into mechanical energy", ["Mechanical energy changes into electrical energy", "Internal energy changes into electrical energy", "Electrical energy changes into chemical energy"],
      "A motor consumes electrical energy and produces mechanical energy."),
    C("standard", "How can the direction of rotation of a DC motor be reversed?", "Reverse only the current direction", ["Reverse both the current and magnetic-field directions", "Increase the current", "Increase the number of coil turns"],
      "The force direction depends on both current and magnetic-field directions. Reversing only one of them reverses the direction of rotation."),
    C("standard", "What does the commutator do in a DC motor?", "Automatically reverses the current in the coil as it passes the balance position", ["Reverses the magnetic-field direction", "Increases the current", "Converts AC to DC"],
      "The commutator reverses the current just as the coil passes the balance position, allowing it to keep rotating."),
  ])

T("motor_make", S(20, 5), "Interdisciplinary Project: Build a Simple DC Motor", "Interdisciplinary Project", "application",
  "Build a simple DC motor using a magnet, enameled wire, a battery, and other materials. Explain why the coil rotates, troubleshoot causes of failure, and suggest improvements.",
  ["Describe the structure and operating principle of a simple motor", "Analyze why a coil does not rotate and improve the design"],
  [("5.2.2", "exact"), ("2.4.4", "exact")], pre=[("motor", "hard")],
  qs=[
    C("basic", "When building a simple motor, one coil lead is stripped completely while the other is stripped on only half its circumference. What does this arrangement act like?", "A commutator", ["A power source", "A magnet", "A switch that only opens and closes the circuit"],
      "The partially stripped wire interrupts current during half of each rotation, letting the coil coast through that part by inertia; this acts like a commutator."),
    C("basic", "How can you make a homemade motor spin faster?", "Use a stronger magnet", ["Use a lower-voltage battery", "Reduce the coil to one turn", "Move the magnet farther away"],
      "Strengthening the magnetic field or increasing the current increases the force on the coil and can increase its speed."),
    C("standard", "The coil does not rotate after the circuit is connected, but starts when nudged. What may be the reason?", "The coil is at its balance position", ["The magnet is too strong", "The battery voltage is too high", "The coil has too many turns"],
      "At the balance position, the forces on the coil are balanced, so it cannot start by itself. A nudge moves it away from that position."),
    C("standard", "The battery becomes noticeably hot after a homemade motor runs for a while. What is the main reason?", "The coil has low resistance, so the current is very large", ["Heat from the magnet transfers to the battery", "The battery voltage is too low", "The coil rotates too slowly"],
      "The enameled wire has very low resistance, allowing a large current that heats the battery internally. Shorten the time the circuit is on."),
  ])

T("induction", S(20, 6), "Generating Electricity with Magnetism", "Motion and Interaction", "reasoning",
  "Investigate the conditions for inducing current when a conductor moves in a magnetic field (part of a closed circuit must cut across magnetic field lines); understand how generators work and transform energy, and learn about alternating current.",
  ["State the conditions for inducing current", "Know that a generator converts mechanical energy into electrical energy", "Distinguish the operating principles of motors and generators"],
  [("2.4.5", "exact"), ("4.2.10", "exact")], pre=[("motor", "hard")],
  qs=[
    C("basic", "Which scientist discovered electromagnetic induction?", "Faraday", ["Oersted", "Ampère", "Joule"],
      "Faraday discovered electromagnetic induction in 1831."),
    C("basic", "What principle does a generator use?", "Electromagnetic induction", ["The force on a current-carrying wire in a magnetic field", "The magnetic effect of current", "The heating effect of current"],
      "A generator uses electromagnetic induction to convert mechanical energy into electrical energy."),
    C("standard", "What conditions are needed to induce current?", "Part of a closed circuit must move through a magnetic field and cut across its field lines", ["A conductor must move in a magnetic field", "There must be current in the conductor", "The circuit must be open and the conductor still in the magnetic field"],
      "The circuit must be closed, and the conductor must cut across magnetic field lines; moving in a magnetic field alone does not necessarily do so."),
    C("standard", "What is the frequency of the alternating current used in household circuits in China?", "50 Hz", ["220 Hz", "60 Hz", "100 Hz"],
      "The frequency of AC in China is 50 Hz, so its direction changes 100 times per second.", verify="50"),
  ])

# ---------------- 21 Electromagnetic Waves and Their Applications
T("em_wave", S(21, 1), "The Ocean of Electromagnetic Waves", "Motion and Interaction", "procedural",
  "Know how electromagnetic waves are produced and transmitted, that they can travel through a vacuum at c = 3×10⁸ m/s, and that wave speed, wavelength, and frequency are related by c = λf.",
  ["Know the speed of electromagnetic waves in a vacuum", "Use c = λf in calculations", "Know that electromagnetic waves can travel through a vacuum"],
  [("2.4.6", "exact")], pre=[("light_line", "hard"), ("sound_feature", "soft")],
  math=[("cnm_022", "Electromagnetic-wave speed and frequency are often written in scientific notation."), ("cnm_237", "At constant wave speed, wavelength is inversely proportional to frequency.")],
  qs=[
    C("basic", "What is the speed of electromagnetic waves in a vacuum?", "3×10⁸ m/s", ["340 m/s", "3×10⁵ m/s", "They cannot travel through a vacuum"],
      "Electromagnetic waves travel through a vacuum at the speed of light, about 3×10⁸ m/s."),
    N("standard", "A radio station broadcasts an electromagnetic wave with a frequency of 1×10⁸ Hz. What is its wavelength in m? (Enter the number only.)", "3", "λ = c/f = 3×10⁸ ÷ 1×10⁸ = 3 m.", "3e8/1e8"),
    C("basic", "Which statement correctly compares electromagnetic waves and sound waves?", "Electromagnetic waves travel through a vacuum, but sound waves do not", ["Sound waves travel through a vacuum, but electromagnetic waves do not", "Neither can travel through a vacuum", "They travel at the same speed"],
      "Sound needs a medium to travel; electromagnetic waves do not."),
    C("standard", "What happens to an electromagnetic wave's wavelength as its frequency increases?", "It becomes shorter", ["It becomes longer", "It stays the same", "It is unrelated to frequency"],
      "At constant wave speed, c = λf, so a higher frequency means a shorter wavelength."),
  ])

T("broadcast", S(21, 2), "Broadcasting, Television, and Mobile Communications", "Motion and Interaction", "conceptual",
  "Understand in general how broadcasting, television, and mobile phones use electromagnetic waves to transmit information; know that a mobile phone both transmits and receives signals.",
  ["Know that radio, television, and mobile phones use electromagnetic waves to transmit information", "Know that a mobile phone can both transmit and receive electromagnetic waves"],
  [("2.4.6", "exact"), ("5.2.3", "exact")], pre=[("em_wave", "hard")],
  qs=[
    C("basic", "What transmits information during a mobile-phone call?", "Electromagnetic waves", ["Ultrasound", "Infrasound", "Current in a wire"],
      "Mobile phones use electromagnetic waves to transmit information."),
    C("basic", "Which statement about mobile phones is correct?", "A mobile phone can both transmit and receive electromagnetic waves", ["It can only receive electromagnetic waves", "It can only transmit electromagnetic waves", "It communicates using sound waves"],
      "A mobile phone acts as both a radio transmitter and a receiver."),
    C("standard", "How does a radio signal reach a receiver from a broadcasting station?", "By electromagnetic waves", ["By sound waves", "By lasers in optical fibers", "By vibrations in the air"],
      "A radio station encodes sound signals onto electromagnetic waves and broadcasts them; the receiver picks up the waves and reconstructs the sound."),
    C("standard", "Why are passengers asked to turn off mobile phones or enable airplane mode during a flight?", "Signals from phones may interfere with aircraft communication and navigation", ["Phones may explode", "Phones make noise", "Phones use the aircraft's electricity"],
      "A phone transmits electromagnetic waves while operating, which may interfere with an aircraft's communication and navigation systems."),
  ])

T("satellite", S(21, 3), "Satellite and Optical-Fiber Communications", "Motion and Interaction", "conceptual",
  "Understand the features of satellite communications (such as the BeiDou Navigation Satellite System) and optical-fiber communications; know that optical fibers transmit information through repeated reflections of laser light.",
  ["Know that optical-fiber communication uses reflections of laser light inside the fiber", "Know that satellite communications and BeiDou use electromagnetic waves"],
  [("2.4.6", "exact"), ("5.2.3", "exact"), ("5.3.3", "inferred")], pre=[("broadcast", "hard"), ("reflect", "soft")],
  qs=[
    C("basic", "What does the BeiDou Navigation Satellite System use to transmit information?", "Electromagnetic waves", ["Ultrasound", "Infrasound", "Optical fibers"],
      "Satellites and ground stations use electromagnetic waves to transmit information."),
    C("basic", "How does laser light travel through an optical fiber?", "It moves forward through repeated reflections inside the fiber", ["It travels in a straight line along the center", "It travels along the outside surface", "It is carried by sound"],
      "Laser light reflects repeatedly from the inside walls of the fiber as it travels from one end to the other."),
    C("standard", "What is an advantage of optical-fiber communication over ordinary cables?", "High capacity and strong resistance to interference", ["It is faster than the speed of light", "It requires no energy", "It works only in a vacuum"],
      "Optical-fiber communication has high capacity, is not affected by electromagnetic interference, and has low signal loss."),
    C("standard", "How does a geostationary communications satellite appear relative to the ground?", "Stationary", ["Moving", "Sometimes stationary and sometimes moving", "Cannot be determined"],
      "A geostationary satellite rotates in sync with Earth, so it appears stationary relative to the ground."),
  ])

# ---------------- 22 Energy and Sustainable Development
T("energy_now", S(22, 1), "Current Energy Use and Its Challenges", "Energy", "conceptual",
  "Distinguish primary from secondary energy and renewable from nonrenewable energy; understand current use of fossil fuels and related environmental problems; know that energy transformations and transfers have a direction.",
  ["Distinguish renewable from nonrenewable energy sources", "Give examples of environmental problems caused by fossil fuels", "Know that energy transformations have a direction"],
  [("3.6.1", "exact"), ("3.5.3", "exact"), ("5.3.1", "inferred")], pre=[("energy_cons", "hard")],
  qs=[
    C("basic", "Which of the following is a nonrenewable energy source?", "Oil", ["Solar energy", "Wind energy", "Hydropower"],
      "Fossil fuels such as coal, oil, and natural gas cannot be replenished on a short timescale, so they are nonrenewable."),
    C("basic", "Which of the following is a secondary energy source?", "Electrical energy", ["Coal", "Solar energy", "Wind energy"],
      "Electrical energy is converted from other energy sources, so it is secondary energy."),
    C("standard", "What are the main environmental problems caused by burning large amounts of fossil fuels?", "The greenhouse effect and air pollution", ["An increase in ozone", "A decrease in noise", "An increase in water resources"],
      "Burning fossil fuels releases large amounts of carbon dioxide and harmful gases, intensifying the greenhouse effect and causing air pollution."),
    C("standard", "If energy is conserved, why should we still save energy?", "Energy transformations have a direction, and less energy remains available for use", ["Energy can be destroyed", "The total amount of energy is decreasing", "Saving energy creates energy"],
      "The total amount of energy stays constant, but transformations have a direction. Dispersed internal energy is difficult to reuse, so less energy remains available for use."),
  ])

T("new_energy", S(22, 2), "Developing New Energy Sources", "Energy", "conceptual",
  "Learn about nuclear energy (fission and fusion), solar energy, wind energy, and other sources; know that nuclear power plants use fission and that fusion occurs inside the Sun; understand possible problems associated with nuclear energy.",
  ["Know that nuclear power plants use fission", "Know that solar energy comes from nuclear fusion inside the Sun", "Know the benefits and risks of nuclear energy"],
  [("3.6.2", "exact"), ("3.6.1", "inferred"), ("5.3.2", "inferred")], pre=[("energy_now", "hard")],
  qs=[
    C("basic", "How do nuclear power plants currently obtain nuclear energy?", "Nuclear fission", ["Nuclear fusion", "Chemical reactions", "Burning uranium"],
      "Nuclear power plants release energy through controlled nuclear fission."),
    C("basic", "Which reaction inside the Sun produces solar energy?", "Nuclear fusion", ["Nuclear fission", "Combustion", "Chemical decomposition"],
      "Hydrogen nuclei fuse inside the Sun, releasing enormous amounts of energy."),
    C("standard", "What form of energy does a solar panel produce from solar energy?", "Electrical energy", ["Chemical energy", "Mechanical energy", "Nuclear energy"],
      "Solar cells convert light energy directly into electrical energy."),
    C("standard", "Which statement about nuclear energy is correct?", "Radioactive nuclear waste must be handled safely", ["Nuclear energy is renewable", "Nuclear power plants have no risks", "Nuclear power plants generate electricity through fusion"],
      "Nuclear fuel is nonrenewable, and nuclear power plants use fission; radiation from accidents and nuclear waste requires strict safeguards."),
  ])

T("save_energy", S(22, 3), "Interdisciplinary Project: Plan to Save Energy", "Interdisciplinary Project", "application",
  "Investigate energy use at school or at home; estimate the effect of energy-saving measures using concepts such as efficiency and electric power; develop a practical energy-saving plan and recognize the importance of sustainable development.",
  ["Estimate the energy saved by a conservation measure", "Propose a practical and reasonable energy-saving plan"],
  [("3.6.3", "exact"), ("5.1.3", "exact"), ("5.3.1", "inferred")], pre=[("new_energy", "hard"), ("save_power", "soft")],
  qs=[
    N("basic", "A school has 50 fluorescent lamps rated at 40 W each. If they are turned off for 2 fewer hours during breaks each day, how many kW·h are saved per day? (Enter the number only.)", "4",
      "W = 50 × 0.04 kW × 2 h = 4 kW·h.", "50*0.04*2"),
    C("basic", "Which action does not support energy conservation?", "Leaving classroom lights on when there is plenty of daylight", ["Turning off lights when leaving", "Using energy-efficient lighting", "Walking or cycling when possible"],
      "Leaving lights on when there is enough daylight wastes electricity."),
    C("standard", "What is the main benefit of replacing an electric water heater with a solar water heater?", "It uses renewable energy and reduces electricity consumption", ["It heats water to a higher temperature", "It requires no materials", "It turns water into fuel"],
      "Solar energy is renewable and can reduce the use of electricity and fossil fuels."),
    N("standard", "A household uses 200 kW·h of electricity each month. If energy-saving measures reduce use by 15%, how many kW·h are saved per month? (Enter the number only.)", "30",
      "200 × 15% = 30 kW·h.", "200*0.15"),
  ])
