"""Grade 8, first semester (People's Education Press edition, revised for the 2022 curriculum standard and adopted starting fall 2024): Chapters 1–6."""
from phy_lib import T, C, N

V = "Grade 8, Semester 1"

# ---------------- Chapter 1: Mechanical Motion
T("len_time", (V, "Chapter 1", "Mechanical Motion", "1.1"), "Measuring Length and Time", "Motion and Interactions", "procedural",
  "Understand the SI units of length and time; use a ruler to measure length and a stopwatch to measure time; read measurements by estimating one digit beyond the smallest graduation; and distinguish measurement error from mistakes.",
  ["Convert between units of length and time", "Read a ruler correctly and estimate one digit beyond the smallest graduation", "Distinguish measurement error from mistakes and know that averaging repeated measurements reduces error"],
  [("2.2.1", "exact"), ("4.1.4", "exact")],
  root="One of the starting points for Grade 8 physics: measurement uses only the length and time units and decimals learned in primary school; no physics prerequisites are needed.",
  math=[("cnm_p121", "Measurements require estimating one digit beyond the smallest graduation and retaining that digit in the result, using decimals and approximations."), ("cnm_p129", "Averaging repeated measurements reduces error.")],
  qs=[
    C("basic", "What is the SI unit of length?", "meter (m)", ["centimeter (cm)", "kilometer (km)", "second (s)"],
      "The SI base unit of length is the meter (m); the second is a unit of time."),
    C("basic", "How many minutes are in 1.5 h?", "90 min", ["150 min", "15 min", "1.5 min"],
      "1 h = 60 min, so 1.5 × 60 = 90 min. Treating 1.5 h as 1 h 50 min is a common mistake.", verify="1.5*60"),
    C("standard", "A pencil is measured with a ruler whose smallest graduation is 1 mm. Which record is correct?", "17.52 cm", ["17.5 cm", "17.520 cm", "175 mm"],
      "A 1 mm graduation is 0.1 cm. Estimate one digit beyond it, to 0.01 cm, so record 17.52 cm."),
    N("standard", "The width of the same book is measured four times: 18.52 cm, 18.51 cm, 18.53 cm, and 18.52 cm. What is the average width in cm? (Enter a number only)",
      "18.52", "(18.52+18.51+18.53+18.52)÷4 = 18.52 cm. Averaging repeated measurements reduces error.", "(18.52+18.51+18.53+18.52)/4"),
  ])

T("motion_desc", (V, "Chapter 1", "Mechanical Motion", "1.2"), "Describing Motion", "Motion and Interactions", "conceptual",
  "Understand mechanical motion and that deciding whether an object is moving or stationary requires a reference frame; the same object can appear to move differently in different reference frames.",
  ["Define mechanical motion", "Use a reference frame to decide whether an object is moving or stationary", "Give examples showing that motion and rest are relative"],
  [("2.1.1", "exact")], pre=[("len_time", "soft")],
  qs=[
    C("basic", "A passenger is sitting on a moving train. Relative to which object is the passenger at rest?", "The train car they are sitting in", ["The tracks", "A tree beside the tracks", "The platform"],
      "The passenger's position relative to the train car does not change, so the passenger is at rest relative to it, but moving relative to the tracks, trees, and platform."),
    C("basic", "Which of the following is not mechanical motion?", "The scent of flowers spreading", ["A car driving on a road", "Earth revolving around the Sun", "A falling leaf"],
      "Mechanical motion is a change in an object's position over time. A scent spreading is molecular thermal motion, not the mechanical motion of an object."),
    C("standard", "When a tanker aircraft refuels a fighter jet in flight, what is the reference object if the jet is said to be stationary?", "The tanker aircraft", ["The ground", "The clouds", "Spectators on the ground"],
      "While refueling, both aircraft have the same speed and their relative positions do not change. The fighter jet is at rest relative to the tanker."),
    C("standard", "Xiaoming says, \"The Moon is moving through the clouds.\" What is his reference object?", "The clouds", ["The Moon", "The ground", "Xiaoming himself"],
      "To say that the Moon is moving, choose an object whose position relative to the Moon changes; here, that object is the clouds. An object cannot be its own reference frame."),
  ])

T("speed", (V, "Chapter 1", "Mechanical Motion", "1.3"), "Speed", "Motion and Interactions", "procedural",
  "Understand the meaning of speed and the formula v = s/t; convert between m/s and km/h; distinguish uniform straight-line motion from nonuniform motion; and calculate simple average speeds.",
  ["Calculate using v = s/t and its rearrangements", "Convert between m/s and km/h (1 m/s = 3.6 km/h)", "Calculate average speed as total distance divided by total time"],
  [("2.2.2", "exact")], pre=[("len_time", "hard"), ("motion_desc", "soft")],
  math=[("cnm_p215", "Speed, distance, and time have direct and inverse proportional relationships, often solved using proportions."), ("cnm_p144", "Rearranging v = s/t to find s or t uses the properties of equality.")],
  qs=[
    C("basic", "A car travels 144 km in 2 h. What is its average speed?", "72 km/h", ["288 km/h", "20 km/h", "146 km/h"],
      "v = s/t = 144 km ÷ 2 h = 72 km/h.", verify="144/2"),
    C("basic", "How many m/s is 72 km/h?", "20 m/s", ["259.2 m/s", "72 m/s", "2 m/s"],
      "Since 1 m/s = 3.6 km/h, 72 ÷ 3.6 = 20 m/s. Multiplying 72 by 3.6 is a common mistake.", verify="72/3.6"),
    N("standard", "Sound travels through air at 340 m/s. Thunder is heard 3 s after lightning is seen. About how many meters away did the lightning strike? (Enter a number only)", "1020",
      "Light travels so fast that its travel time can be ignored. s = vt = 340 m/s × 3 s = 1020 m.", "340*3"),
    C("advanced", "Xiaohua travels the first half of a route at 4 m/s and the second half at 6 m/s. What is the average speed for the whole route?", "4.8 m/s", ["5 m/s", "10 m/s", "2.4 m/s"],
      "Let each half of the distance be s. The total time is t = s/4 + s/6 = 5s/12, so average speed = 2s ÷ (5s/12) = 4.8 m/s. Simply averaging the two speeds to get 5 m/s is incorrect.",
      verify="2/(1/4+1/6)"),
  ])

T("speed_measure", (V, "Chapter 1", "Mechanical Motion", "1.4"), "Measuring Speed", "Motion and Interactions", "procedural",
  "Measure an object's average speed with a ruler and stopwatch (or a sensor). Understand the experimental principle v = s/t and analyze how a cart's speed changes over the two halves of a ramp.",
  ["State the principle and equipment for measuring average speed", "Calculate average speed for each segment from measurement data", "Understand that a cart speeds up as it rolls down a ramp"],
  [("4.1.5", "exact"), ("2.2.2", "inferred")], pre=[("speed", "hard")],
  qs=[
    C("basic", "What is the principle for measuring the average speed of a cart rolling down a ramp?", "v = s/t", ["s = vt", "t = s/v", "v = t/s"],
      "Measure the distance s and time t, then calculate average speed with v = s/t."),
    C("basic", "When measuring a cart's average speed, which two measuring tools are needed in addition to the ramp, cart, and metal plate?", "A ruler and a stopwatch", ["A balance and a stopwatch", "A ruler and a thermometer", "A spring scale and a ruler"],
      "Measure distance with a ruler and time with a stopwatch."),
    C("standard", "A cart rolls from the top to the bottom of a ramp, covering 0.8 m in 4 s. It takes 2.5 s to cover the first half. What is its average speed over the second half?", "0.27 m/s", ["0.2 m/s", "0.16 m/s", "0.32 m/s"],
      "The second half is 0.4 m and takes 4 - 2.5 = 1.5 s, so v = 0.4 ÷ 1.5 ≈ 0.27 m/s. The cart speeds up, so its average speed over the second half is greater than the 0.2 m/s average for the whole trip.",
      verify="round(0.4/1.5,2)"),
    C("standard", "How should the ramp's slope be adjusted to measure the cart's travel time more accurately?", "Make it a little less steep", ["Make it a little steeper", "Make it as steep as possible", "The slope does not affect the time"],
      "A gentler slope makes the cart move more slowly and take longer, reducing the relative timing error."),
  ])

# ---------------- Chapter 2: Sound
T("sound_source", (V, "Chapter 2", "Sound", "2.1"), "Sound Production and Propagation", "Motion and Interactions", "conceptual",
  "Understand that sound is produced by vibrating objects and needs a medium to travel; sound cannot travel through a vacuum. Know that sound speed depends on the medium and temperature, and is about 340 m/s in air at 15 °C.",
  ["State the conditions for sound production and propagation", "Understand that sound cannot travel through a vacuum", "Compare sound speeds in solids, liquids, and gases"],
  [("2.3.1", "exact")], root="The starting point for Grade 8 acoustics; only everyday experience is needed.",
  qs=[
    C("basic", "How is sound produced?", "By vibrating objects", ["By moving objects", "By flowing air", "By heated objects"],
      "All objects that produce sound are vibrating. When the vibrations stop, so does the sound."),
    C("basic", "Why can't astronauts talk directly to one another outside a spacecraft?", "Sound cannot travel through a vacuum", ["Space is too cold", "Sound travels too fast", "The astronauts speak too softly"],
      "Sound needs a medium to travel, and space is nearly a vacuum, so astronauts communicate by radio."),
    C("standard", "Under ordinary conditions, in which of these media does sound travel fastest?", "Steel", ["Air", "Water", "A vacuum"],
      "Generally, sound travels fastest in solids, then liquids, then gases; it cannot travel through a vacuum."),
    C("standard", "Paper scraps jump when placed on a drum as it is struck. What experimental method does this demonstrate?", "The conversion method", ["The control-variable method", "The equivalent-substitution method", "The ideal-model method"],
      "The drumhead's vibrations are difficult to see directly. The jumping scraps make the small vibrations visible; this is the conversion method."),
  ])

T("sound_feature", (V, "Chapter 2", "Sound", "2.2"), "Characteristics of Sound", "Motion and Interactions", "conceptual",
  "Understand the three characteristics of sound: pitch, loudness, and timbre. Pitch depends on frequency; loudness depends on amplitude and distance from the source; timbre is determined by the source itself.",
  ["Distinguish pitch, loudness, and timbre", "Know that pitch depends on frequency and loudness depends on amplitude", "Know the human hearing range and what ultrasound and infrasound are"],
  [("2.3.2", "exact")], pre=[("sound_source", "hard")],
  qs=[
    C("basic", "\"Recognizing someone by their voice\" relies mainly on which characteristic of sound?", "Timbre", ["Pitch", "Loudness", "Frequency"],
      "People have different vocal-cord structures, so their voices have different timbres."),
    C("basic", "In the phrase \"singing at the top of one's voice,\" which characteristic of sound does \"top\" refer to?", "High loudness", ["High pitch", "Good timbre", "High frequency"],
      "Singing at the top of one's voice means singing loudly, so it refers to loudness. In \"soprano,\" high refers to pitch."),
    C("standard", "A steel ruler is plucked with the same force. What happens to the sound as the part extending over the table gets shorter?", "The pitch gets higher", ["The loudness increases", "The pitch gets lower", "The timbre changes"],
      "A shorter overhanging section vibrates faster, increasing its frequency and pitch."),
    C("standard", "What is the approximate frequency range of sounds audible to humans?", "20 Hz–20,000 Hz", ["0–20 Hz", "Above 20,000 Hz", "20 Hz–2,000 Hz"],
      "The human hearing range is about 20–20,000 Hz. Below 20 Hz is infrasound; above 20,000 Hz is ultrasound."),
  ])

T("sound_use", (V, "Chapter 2", "Sound", "2.3"), "Uses of Sound", "Motion and Interactions", "application",
  "Understand that sound can transmit information and energy. Give examples such as echolocation, ultrasound imaging, ultrasonic cleaning, and breaking stones.",
  ["Distinguish examples of sound transmitting information from those of sound transmitting energy", "Use echoes to perform simple distance calculations"],
  [("2.3.2", "exact")], pre=[("sound_feature", "soft"), ("speed", "soft")],
  qs=[
    C("basic", "What use of sound does a doctor make when examining a patient with ultrasound?", "Transmitting information", ["Transmitting energy", "Changing pitch", "Reducing noise"],
      "Ultrasound uses echoes to obtain information from inside the body, so sound is transmitting information."),
    C("basic", "Which example uses sound to transmit energy?", "Cleaning glasses with ultrasound", ["A bat using echolocation", "Tapping a watermelon to check if it is ripe", "A car's reversing sensor"],
      "Ultrasonic cleaning uses sound energy to shake dirt loose, transmitting energy. The other examples obtain information."),
    N("standard", "An ultrasonic pulse sent toward the seabed returns after 4 s. If sound travels through seawater at 1,500 m/s, how deep is the water in meters? (Enter a number only)", "3000",
      "The sound takes 4 s for a round trip, so the one-way time is 2 s. Depth = 1,500 × 2 = 3,000 m. Forgetting to divide by 2 gives 6,000 m.", "1500*4/2"),
    C("standard", "In which case can ultrasound not be used to measure distance?", "Measuring the distance from Earth to the Moon", ["Measuring the depth of the seabed", "Measuring the distance to an obstacle while reversing", "Locating a school of fish"],
      "There is a vacuum between Earth and the Moon, and sound cannot travel through a vacuum, so ultrasound cannot measure that distance."),
  ])

T("noise", (V, "Chapter 2", "Sound", "2.4"), "Noise: Effects and Control", "Motion and Interactions", "application",
  "Understand the sources and harmful effects of noise. Know that sound level is measured in decibels (dB) and learn ways to control noise at the source, during propagation, and at the listener's ears.",
  ["Name and give examples of the three ways to control noise", "Know that decibels measure sound level"],
  [("2.3.2", "exact"), ("5.1.2", "inferred")], pre=[("sound_feature", "soft")],
  qs=[
    C("basic", "What unit is used to express sound level?", "Decibel (dB)", ["Hertz (Hz)", "Meter per second (m/s)", "Joule (J)"],
      "Decibels are used to express sound level; hertz is a unit of frequency."),
    C("basic", "Planting trees along a road reduces noise at which point?", "During propagation", ["At the source", "At the listener's ears", "None of the above"],
      "Trees absorb and reflect sound, reducing noise as it propagates."),
    C("standard", "Installing a muffler on a motorcycle controls noise at which point?", "At the source", ["During propagation", "At the listener's ears", "At the receiver"],
      "A muffler directly reduces noise from the motorcycle's exhaust, so it controls noise at the source."),
    C("standard", "To ensure rest and sleep, how loud should sound be at most?", "50 dB", ["90 dB", "120 dB", "0 dB"],
      "Sound should not exceed 50 dB for rest and sleep, or 90 dB to protect hearing. 0 dB is the quietest sound the human ear can just detect."),
  ])

T("soundproof", (V, "Chapter 2", "Sound", "2.5"), "Interdisciplinary Practice: Build a Soundproof Room Model", "Interdisciplinary Practice", "application",
  "Apply knowledge of sound propagation and noise control to select materials, design and build a soundproof room model, and compare the sound-insulating performance of different materials.",
  ["Name factors to consider when choosing soundproofing materials", "Design a comparison that controls variables"],
  [("5.1.1", "exact"), ("2.3.2", "inferred")], pre=[("noise", "hard")],
  qs=[
    C("basic", "Which material would provide the best sound insulation as the lining of a soundproof room model?", "Porous foam", ["A smooth glass sheet", "Thin sheet metal", "Painted cardboard"],
      "Porous, soft materials absorb sound and insulate well; smooth, hard surfaces tend to reflect sound."),
    C("basic", "A soundproof room mainly reduces noise at which point?", "During propagation", ["At the source", "At the listener's ears", "By changing the frequency"],
      "A soundproof room blocks sound from propagating, so it reduces noise during propagation."),
    C("standard", "What is the correct way to compare the sound-insulating performance of two materials?", "Use the same sound source, volume, and distance; change only the material", ["Use different sound sources for the two materials", "Play music once and an alarm once", "Vary the distance from the sound source during measurements"],
      "Use the control-variable method: change only the material and keep other conditions (source, volume, and distance) the same."),
    C("standard", "A phone sound-level meter reads 70 dB outside a box, 52 dB inside Box A, and 45 dB inside Box B. Which box insulates sound better?", "Box B", ["Box A", "They are equally good", "It cannot be determined"],
      "The quieter the sound inside the box, the better its sound insulation. Box B measures 45 dB, lower than Box A's 52 dB."),
  ])

# ---------------- Chapter 3: Changes of State
T("temperature", (V, "Chapter 3", "Changes of State", "3.1"), "Temperature", "Matter", "procedural",
  "Understand that temperature indicates how hot or cold an object is and how the Celsius scale is defined. Learn how liquid thermometers work (thermal expansion and contraction) and use thermometers and clinical thermometers correctly.",
  ["State how the Celsius scale is defined and give common temperatures", "Measure and read temperatures correctly, including below-zero readings", "Know the features of clinical thermometers and how to use them"],
  [("1.1.2", "exact"), ("4.1.3", "exact")], root="The starting point for thermal physics; only everyday experience and positive and negative numbers are needed.",
  math=[("cnm_001", "Negative numbers are used for below-zero temperatures.")],
  qs=[
    C("basic", "How do common liquid thermometers work?", "Thermal expansion and contraction of liquids", ["Thermal expansion and contraction of solids", "Thermal expansion and contraction of gases", "Boiling of liquids"],
      "Liquid thermometers use the thermal expansion and contraction of liquids such as mercury, alcohol, or kerosene."),
    C("basic", "At standard atmospheric pressure, what is the temperature of a mixture of ice and water?", "0 °C", ["100 °C", "4 °C", "-10 °C"],
      "On the Celsius scale, a mixture of ice and water at standard atmospheric pressure is 0 °C, and boiling water is 100 °C."),
    C("standard", "The top of a thermometer's liquid column is six small divisions below 0 °C. If each division is 1 °C, what is the reading?", "-6 °C", ["6 °C", "-4 °C", "-16 °C"],
      "The liquid is below 0 °C, so the reading is negative. Six divisions down at 1 °C per division gives -6 °C."),
    C("standard", "A clinical thermometer reads 38.5 °C. Without shaking it down, it is used to measure a person whose temperature is 37 °C. What will it read?", "38.5 °C", ["37 °C", "37.5 °C", "75.5 °C"],
      "A clinical thermometer has a constriction that prevents the liquid from flowing back on its own. If the measured temperature is below the previous reading, it remains at 38.5 °C."),
  ])

T("melt", (V, "Chapter 3", "Changes of State", "3.2"), "Melting and Freezing", "Matter", "conceptual",
  "Understand melting and freezing. Know that crystalline substances have a melting point while amorphous substances do not; a crystal's temperature stays constant as it absorbs heat while melting. Read melting and freezing graphs.",
  ["Distinguish melting from freezing and identify heat absorption or release", "Distinguish crystalline from amorphous substances", "Read the melting point and melting duration from a melting graph"],
  [("1.1.3", "exact"), ("1.1.1", "inferred")], pre=[("temperature", "hard")],
  math=[("cnm_197", "A melting graph shows temperature as a function of time.")],
  qs=[
    C("basic", "What is the change of state from solid to liquid called?", "Melting", ["Freezing", "Condensation", "Sublimation"],
      "Solid → liquid is melting; liquid → solid is freezing."),
    C("basic", "Which of the following substances is crystalline?", "Ice", ["Rosin", "Glass", "Asphalt"],
      "Ice has a fixed melting point and is crystalline. Rosin, glass, and asphalt have no fixed melting point and are amorphous."),
    C("standard", "A crystal's temperature remains at 48 °C for 6 min on a melting graph. What happens to the substance during this interval?", "It continues to absorb heat while its temperature stays constant", ["It absorbs no heat and its temperature stays constant", "It releases heat", "It is not melting because its temperature stays constant"],
      "A crystal continues to absorb heat while melting, but its temperature remains constant at the melting point."),
    C("standard", "In northern China, several buckets of water are placed in a vegetable cellar during winter to keep vegetables from freezing. What principle does this use?", "Water releases heat as it freezes", ["Water absorbs heat as it freezes", "Water absorbs heat as it evaporates", "Water releases heat as it vaporizes"],
      "Water releases heat as it freezes, keeping the cellar from getting too cold."),
  ])

T("vapor", (V, "Chapter 3", "Changes of State", "3.3"), "Vaporization and Condensation", "Matter", "conceptual",
  "Understand the two forms of vaporization (evaporation and boiling) and their characteristics; the factors affecting evaporation rate; the relationship between boiling point and pressure; and two ways to cause condensation. Investigate how water temperature changes before and during boiling.",
  ["Distinguish evaporation from boiling", "Name three factors that affect evaporation rate", "Know the conditions for boiling and that temperature remains constant during boiling"],
  [("1.1.3", "exact"), ("4.2.1", "exact")], pre=[("temperature", "hard"), ("melt", "soft")],
  qs=[
    C("basic", "In summer, droplets appear on the outside of a drink bottle taken from the refrigerator. What change of state causes this?", "Condensation", ["Vaporization", "Melting", "Sublimation"],
      "Water vapor in the air releases heat when it meets the cold bottle and condenses into droplets."),
    C("basic", "Which action speeds up evaporation?", "Spread wet clothes out in a sunny, breezy place", ["Fold wet clothes and leave them in the shade", "Cover vegetables with plastic wrap", "Tighten the cap on a bottle of alcohol"],
      "Increasing a liquid's surface area or temperature, or increasing airflow above it, speeds up evaporation."),
    C("standard", "What happens to the temperature of water when it is heated after it starts boiling?", "It stays constant", ["It continues to rise", "It rises and then falls", "It falls"],
      "A boiling liquid continues to absorb heat, but its temperature remains at the boiling point."),
    C("standard", "Why is it difficult to cook rice in an ordinary pot on a high mountain?", "The air pressure is low, so water's boiling point is low", ["The air pressure is high, so water's boiling point is high", "The air pressure is low, so water's boiling point is high", "The flame is weak at high altitude"],
      "Air pressure decreases with altitude, lowering water's boiling point; the pot cannot reach 100 °C."),
  ])

T("sublim", (V, "Chapter 3", "Changes of State", "3.4"), "Sublimation and Deposition", "Matter", "conceptual",
  "Understand sublimation and deposition: sublimation absorbs heat, while deposition releases heat. Use the six changes of state to explain snow, frost, fog, dew, the water cycle, and other phenomena.",
  ["Distinguish sublimation from deposition", "Identify the changes of state involved in frost, fog, dew, snow, and similar phenomena", "State whether each of the six changes of state absorbs or releases heat"],
  [("1.1.3", "exact"), ("1.1.4", "exact")], pre=[("melt", "hard"), ("vapor", "hard")],
  qs=[
    C("basic", "What change of state forms the ice crystals on the inside of a window in winter?", "Deposition", ["Freezing", "Condensation", "Sublimation"],
      "Water vapor indoors changes directly into solid ice crystals on the cold glass; this is deposition."),
    C("basic", "A mothball in a closet shrinks or disappears over time. What phenomenon is this?", "Sublimation", ["Melting", "Vaporization", "Deposition"],
      "The mothball changes directly from a solid to a gas; this is sublimation."),
    C("standard", "Which group contains only changes of state that release heat?", "Freezing, condensation, and deposition", ["Melting, vaporization, and sublimation", "Melting, condensation, and deposition", "Freezing, vaporization, and sublimation"],
      "Melting, vaporization, and sublimation absorb heat; freezing, condensation, and deposition release heat."),
    C("standard", "How do dewdrops form on grass on an autumn morning?", "Water vapor condenses", ["Water vapor deposits", "Ice melts", "Water vaporizes"],
      "Dew consists of droplets formed when water vapor in the air condenses as it cools; frost forms by deposition."),
  ])

T("kitchen", (V, "Chapter 3", "Changes of State", "3.5"), "Interdisciplinary Practice: Explore Changes of State in the Kitchen", "Interdisciplinary Practice", "application",
  "Observe and explain changes of state during steaming, boiling, freezing, thawing, and other kitchen processes, and propose safer or more energy-efficient practices.",
  ["Use changes of state to explain common kitchen phenomena", "Suggest safety or energy-saving measures related to changes of state"],
  [("5.1.1", "exact"), ("1.1.3", "inferred")], pre=[("sublim", "hard")],
  qs=[
    C("basic", "Steam escaping when a pot lid is lifted can cause worse burns than boiling water at the same temperature. Why?", "Water vapor releases a large amount of heat as it condenses", ["The water vapor must be hotter", "Water vapor releases heat as it deposits", "Boiling water does not release heat"],
      "Steam at 100 °C first releases heat as it condenses, then the resulting 100 °C water releases more heat, causing a more severe burn."),
    C("basic", "A layer of white frost forms on frozen meat taken from a freezer. How does the frost form?", "Water vapor deposits", ["Water freezes", "Water vapor condenses", "Ice sublimates"],
      "Water vapor in the freezer changes directly into tiny ice crystals on the cold meat, forming frost."),
    C("standard", "While making soup, the heat is turned from high to low after the soup boils. What happens to its temperature?", "It stays about the same and continues boiling", ["It drops noticeably", "It continues to rise", "It stops boiling immediately"],
      "As long as the soup continues to absorb enough heat to boil, its temperature stays at the boiling point. Lowering the heat saves fuel."),
    C("standard", "A frozen drink bottle is left on a table. Frost forms on the outside and later turns into droplets. What is the later change of state?", "Melting", ["Condensation", "Deposition", "Vaporization"],
      "Frost is a solid; changing from solid to liquid is melting."),
  ])

# ---------------- Chapter 4: Light
T("light_line", (V, "Chapter 4", "Light", "4.1"), "Rectilinear Propagation of Light", "Motion and Interactions", "conceptual",
  "Understand what a light source is and that light travels in a straight line through a uniform medium. Explain shadows, pinhole images, and solar and lunar eclipses. Know that the speed of light in a vacuum is about 3×10⁸ m/s.",
  ["Use rectilinear propagation of light to explain shadows, pinhole images, and similar phenomena", "Know the speed of light and that a light-year is a unit of distance"],
  [("2.3.3", "inferred"), ("1.3.4", "inferred")], root="The starting point for optics; only everyday experience is needed.",
  qs=[
    C("basic", "Which of the following objects is a light source?", "A firefly that is glowing", ["The Moon", "A sparkling diamond", "A movie screen"],
      "Only an object that emits its own light is a light source; the Moon, a diamond, and a screen reflect other light."),
    C("basic", "What is the approximate speed of light in a vacuum?", "3×10⁸ m/s", ["340 m/s", "3×10⁵ m/s", "3×10⁸ km/s"],
      "In a vacuum, the speed of light c ≈ 3×10⁸ m/s = 3×10⁵ km/s; 340 m/s is the speed of sound in air."),
    C("standard", "What physical quantity does a light-year measure?", "Length (distance)", ["Time", "Speed", "A calendar year"],
      "A light-year is the distance light travels in one year, so it is a unit of length."),
    C("standard", "What determines the shape of an image formed through a pinhole?", "The shape of the object", ["The shape of the pinhole", "The shape of the screen", "The size of the pinhole"],
      "A pinhole forms an inverted real image through rectilinear propagation of light. The image has the same shape as the object, regardless of the pinhole's shape."),
  ])

_FIG_REFLECT = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 150"><line x1="20" y1="120" x2="220" y2="120" stroke="currentColor" stroke-width="3"/>'
  '<line x1="120" y1="20" x2="120" y2="120" stroke="currentColor" stroke-width="1.6" stroke-dasharray="5 4"/>'
  '<line x1="42" y1="75" x2="120" y2="120" stroke="currentColor" stroke-width="2.6"/><path d="M85 100 L74.3 98.5 L78.3 91.5 Z" fill="currentColor"/>'
  '<line x1="120" y1="120" x2="198" y2="75" stroke="currentColor" stroke-width="2.6"/><path d="M163 95 L152.3 96.5 L156.3 103.5 Z" fill="currentColor"/>'
  '<path d="M90 120 A30 30 0 0 1 94 105" fill="none" stroke="currentColor" stroke-width="1.6"/>'
  '<text x="62" y="114" font-size="13" fill="currentColor">30°</text><text x="30" y="72" font-size="13" fill="currentColor">A</text>'
  '<text x="124" y="30" font-size="13" fill="currentColor">N</text><text x="124" y="138" font-size="13" fill="currentColor">O</text></svg>')

T("reflect", (V, "Chapter 4", "Light", "4.2"), "Reflection of Light", "Motion and Interactions", "conceptual",
  "Investigate the law of reflection: the reflected ray, incident ray, and normal lie in the same plane; the reflected and incident rays are on opposite sides of the normal; and the angle of reflection equals the angle of incidence. Understand specular and diffuse reflection and that light paths are reversible.",
  ["State the law of reflection", "Find the angle of reflection from the angle of incidence (both are measured from the normal)", "Distinguish specular from diffuse reflection"],
  [("2.3.3", "exact"), ("4.2.6", "exact")], pre=[("light_line", "hard")],
  math=[("cnm_058", "The angles of incidence and reflection are measured from the normal; this uses angle measurement and complementary angles.")],
  qs=[
    C("basic", "The angle between an incident ray and the normal is 40°. What is the angle of reflection?", "40°", ["50°", "80°", "140°"],
      "The angle of reflection equals the angle of incidence. Since the angle of incidence is between the incident ray and the normal, the angle of reflection is 40°.", verify="'40°'"),
    C("basic", "Why can we see writing on a blackboard from different directions?", "Diffuse reflection", ["Specular reflection", "Refraction", "Rectilinear propagation"],
      "A rough surface reflects light in many directions; this is diffuse reflection."),
    C("standard", "In the figure, incident ray AO makes a 30° angle with the mirror. What is the angle of reflection?", "60°", ["30°", "120°", "90°"],
      "The angle of incidence is measured between the incident ray and the normal: 90° - 30° = 60°. The angle of reflection is also 60°. Treating 30° as the angle of incidence is a common mistake.",
      verify="'60°'", figure=_FIG_REFLECT),
    C("standard", "When investigating reflection, a sheet of paper is folded back at F and the reflected ray can no longer be seen. What does this show?", "The reflected ray, incident ray, and normal lie in the same plane", ["The angle of reflection equals the angle of incidence", "Light paths are reversible", "The reflected ray has disappeared"],
      "After the paper is folded, it is no longer in the same plane as the rays, so the reflected ray is not visible. This shows that the three lie in one plane."),
  ])

T("plane_mirror", (V, "Chapter 4", "Light", "4.3"), "Images in Plane Mirrors", "Motion and Interactions", "conceptual",
  "Investigate the characteristics of plane-mirror images: image and object are the same size, are the same distance from the mirror, and are joined by a line perpendicular to the mirror; the image is virtual. Learn about applications of plane mirrors.",
  ["State the characteristics of images in plane mirrors", "Find image distance and object-to-image distance from object distance", "Explain why a glass plate is used instead of a plane mirror in an investigation"],
  [("2.3.4", "exact"), ("4.2.7", "exact")], pre=[("reflect", "hard")],
  math=[("cnm_132", "In a plane mirror, the image and object are symmetric about the mirror.")],
  qs=[
    C("basic", "A person stands 2 m in front of a plane mirror. How far apart are the person and their image?", "4 m", ["2 m", "1 m", "0 m"],
      "The image is 2 m behind the mirror, the same distance as the person in front, so the separation is 2 + 2 = 4 m.", verify="2*2"),
    C("basic", "What happens to the size of a person's image as they move closer to a plane mirror?", "It stays the same", ["It gets larger", "It gets smaller", "It first gets larger, then smaller"],
      "A plane-mirror image is the same size as the object regardless of distance; it only appears larger because the viewing angle increases."),
    C("standard", "Why is a glass plate used instead of a plane mirror when investigating plane-mirror images?", "It makes the image position easier to determine", ["It makes the image clearer", "It enlarges the image", "It forms a real image"],
      "A glass plate reflects light to form an image and also transmits light, so the candle behind it can be seen to determine the image position."),
    C("standard", "If a screen is placed where the image appears, can the image be seen on the screen?", "No. A plane mirror forms a virtual image", ["Yes. It forms a real image", "Yes, but the image is inverted", "Only in a dark room"],
      "A plane-mirror image is virtual, not formed by actual light rays converging, so it cannot be projected onto a screen."),
  ])

T("refract", (V, "Chapter 4", "Light", "4.4"), "Refraction of Light", "Motion and Interactions", "conceptual",
  "Use experiments to study refraction and its characteristics: when light enters water or glass obliquely from air, the angle of refraction is smaller than the angle of incidence; when it enters perpendicularly, its direction does not change. Explain why a pool looks shallower and a chopstick looks bent.",
  ["State how a refracted ray bends when light enters water obliquely from air", "Use refraction to explain familiar phenomena", "Know that light paths are reversible during refraction"],
  [("2.3.3", "exact")], pre=[("reflect", "soft"), ("light_line", "hard")],
  qs=[
    C("basic", "When light enters water obliquely from air, how does the angle of refraction compare with the angle of incidence?", "The angle of refraction is smaller", ["The angle of refraction is larger", "The angles are equal", "The angle of refraction is 0"],
      "When light enters water or glass obliquely from air, the refracted ray bends toward the normal, making the angle of refraction smaller than the angle of incidence."),
    C("basic", "A clear pool looks shallower than it really is when viewed from the shore. Why?", "Refraction of light", ["Reflection of light", "Rectilinear propagation of light", "Dispersion of light"],
      "Light reflected from the bottom refracts as it leaves the water obliquely. The viewer sees a virtual image that appears shallower."),
    C("standard", "What is the angle of refraction when light enters glass perpendicularly from air?", "0°", ["90°", "45°", "Some angle greater than 0°"],
      "For perpendicular incidence, the angle of incidence is 0° and the light's direction does not change, so the angle of refraction is also 0°.", verify="'0°'"),
    C("standard", "When a fisher aims a spear at a fish, where should they aim relative to the fish they see?", "Below the fish they see", ["Above the fish they see", "Directly at the fish they see", "To the left of the fish they see"],
      "The fish appears as a virtual image closer to the surface; the real fish is below the image, so the spear should be aimed lower."),
  ])

T("dispersion", (V, "Chapter 4", "Light", "4.5"), "Dispersion of Light", "Motion and Interactions", "conceptual",
  "Use experiments to learn that white light consists of multiple colors. Know that the three primary colors of light are red, green, and blue; explore how colors of light mix; and learn applications of infrared and ultraviolet radiation.",
  ["Know that sunlight separates into seven colors when it passes through a prism", "Name the three primary colors of light", "Give examples of applications of infrared and ultraviolet radiation"],
  [("2.3.6", "exact")], pre=[("refract", "hard")],
  qs=[
    C("basic", "What are the three primary colors of light?", "Red, green, and blue", ["Red, yellow, and blue", "Red, green, and yellow", "Yellow, green, and blue"],
      "The primary colors of light are red, green, and blue; red, yellow, and blue are the primary colors of paint."),
    C("basic", "A rainbow appears in the sky after rain. What phenomenon is this?", "Dispersion of light", ["Reflection of light", "Rectilinear propagation of light", "Image formation in a plane mirror"],
      "Sunlight is refracted by water droplets in the air and separates into different colors; this is dispersion."),
    C("standard", "What kind of light does a television remote control emit?", "Infrared", ["Ultraviolet", "Red light", "X-rays"],
      "A remote control transmits signals using invisible infrared radiation; counterfeit-money detectors use ultraviolet radiation."),
    C("standard", "A white shirt is illuminated with red light in a dark room. What color does it appear?", "Red", ["White", "Black", "Green"],
      "A white object reflects all colors of light. Under red light, it reflects only red light and therefore appears red."),
  ])

# ---------------- Chapter 5: Lenses and Their Applications
T("lens", (V, "Chapter 5", "Lenses and Their Applications", "5.1"), "Lenses", "Motion and Interactions", "conceptual",
  "Recognize convex and concave lenses and identify the principal axis, optical center, focus, and focal length. Understand that convex lenses converge light and concave lenses diverge it, and draw the three principal rays.",
  ["Distinguish convex lenses from concave lenses", "Know that convex lenses converge light and concave lenses diverge it", "Draw rays parallel to the principal axis, through the optical center, and through the focus"],
  [("2.3.5", "exact")], pre=[("refract", "hard")],
  qs=[
    C("basic", "What is a lens that is thicker in the middle and thinner at the edges called?", "A convex lens", ["A concave lens", "A plane mirror", "A prism"],
      "A convex lens is thicker in the middle and thinner at the edges; a concave lens is thinner in the middle and thicker at the edges."),
    C("basic", "What happens to light parallel to the principal axis after it passes through a convex lens?", "It converges at the focus", ["It diverges", "Its direction does not change", "It retraces its path"],
      "A convex lens converges light. After refraction, rays parallel to the principal axis meet at the focus."),
    C("standard", "How does a ray passing through the optical center of a convex lens travel after passing through the lens?", "It continues in the same direction", ["It bends toward the principal axis", "It bends away from the principal axis", "It converges at the focus"],
      "A ray passing through the optical center does not change direction."),
    C("standard", "A convex lens is pointed at the Sun and forms its smallest, brightest spot 10 cm from the lens. What is its approximate focal length?", "10 cm", ["20 cm", "5 cm", "Cannot be determined"],
      "The smallest, brightest spot is the focus. The distance from the optical center to the focus is the focal length, about 10 cm."),
  ])

T("lens_life", (V, "Chapter 5", "Lenses and Their Applications", "5.2"), "Lenses in Everyday Life", "Motion and Interactions", "application",
  "Understand the images formed by cameras, projectors, and magnifying glasses, and distinguish real images from virtual images.",
  ["State the image properties of cameras, projectors, and magnifying glasses", "Distinguish real images from virtual images"],
  [("2.3.5", "exact")], pre=[("lens", "hard")],
  qs=[
    C("basic", "What kind of image does a camera form?", "An inverted, reduced real image", ["An inverted, enlarged real image", "An upright, enlarged virtual image", "An upright, reduced virtual image"],
      "A camera's object distance is greater than twice the focal length, so it forms an inverted, reduced real image."),
    C("basic", "What kind of image do you see when looking at a stamp through a magnifying glass?", "An upright, enlarged virtual image", ["An inverted, enlarged real image", "An upright, reduced virtual image", "An inverted, reduced real image"],
      "When an object is inside the focal length of a magnifying glass, it forms an upright, enlarged virtual image."),
    C("standard", "What kind of image does a projector form on a screen?", "An inverted, enlarged real image", ["An upright, enlarged virtual image", "An inverted, reduced real image", "An upright, enlarged real image"],
      "A projector's object distance is between one and two focal lengths, so it forms an inverted, enlarged real image; therefore, the slide must be placed upside down."),
    C("standard", "What is the main difference between a real image and a virtual image?", "A real image can be projected onto a screen; a virtual image cannot", ["All real images are enlarged", "All virtual images are inverted", "A real image can only be seen with the eye"],
      "A real image is formed by actual light rays converging and can be projected onto a screen; a virtual image cannot."),
  ])

T("lens_rule", (V, "Chapter 5", "Lenses and Their Applications", "5.3"), "Image Formation by Convex Lenses", "Motion and Interactions", "reasoning",
  "Investigate image formation by convex lenses: u > 2f produces an inverted, reduced real image; f < u < 2f produces an inverted, enlarged real image; and u < f produces an upright, enlarged virtual image. For real images, moving the object closer moves the image farther away and enlarges it.",
  ["Determine image properties from the relationship between object distance and focal length", "Know that for real images, moving the object closer makes the image farther away and larger", "Determine a possible focal-length range from image information"],
  [("2.3.5", "exact"), ("4.2.8", "exact")], pre=[("lens_life", "hard")],
  math=[("cnm_096", "Use inequalities based on image-formation conditions to determine the focal-length range.")],
  qs=[
    C("basic", "A convex lens has a focal length of 10 cm. A candle is placed 30 cm from it. What kind of image is formed?", "An inverted, reduced real image", ["An inverted, enlarged real image", "An upright, enlarged virtual image", "No image is formed"],
      "u = 30 cm > 2f = 20 cm, so an inverted, reduced real image is formed."),
    C("basic", "A convex lens has a focal length of 10 cm. An object is placed 15 cm from it. What kind of image is formed?", "An inverted, enlarged real image", ["An inverted, reduced real image", "An upright, enlarged virtual image", "An upright, reduced real image"],
      "f < u = 15 cm < 2f, so an inverted, enlarged real image is formed."),
    C("standard", "When a real image is formed, a candle is moved closer to a convex lens. How should the screen be moved to bring the image back into focus?", "Move it farther from the lens; the image gets larger", ["Move it closer to the lens; the image gets smaller", "Move it farther from the lens; the image gets smaller", "Do not move it"],
      "For a real image, moving the object closer moves the image farther away and makes it larger."),
    C("advanced", "An object 20 cm from a convex lens forms an inverted, reduced real image on a screen. Which focal length could the lens have?", "8 cm", ["10 cm", "15 cm", "25 cm"],
      "An inverted, reduced real image requires u > 2f, so 20 cm > 2f and f < 10 cm. Only 8 cm fits. At f = 10 cm, the image would be the same size as the object."),
  ])

T("eye", (V, "Chapter 5", "Lenses and Their Applications", "5.4"), "The Eye and Glasses", "Motion and Interactions", "application",
  "Understand that the eye acts like a camera, with the lens acting like a convex lens and forming an inverted, reduced real image on the retina. Learn the causes of nearsightedness and farsightedness and how to correct them.",
  ["State that nearsighted images form in front of the retina and are corrected with concave lenses", "State that farsighted images form behind the retina and are corrected with convex lenses"],
  [("2.3.5", "exact"), ("5.1.3", "inferred")], pre=[("lens_rule", "hard")],
  qs=[
    C("basic", "What kind of lens corrects nearsightedness?", "A concave lens", ["A convex lens", "A plane mirror", "A prism"],
      "In nearsightedness, the eye's lens is too thick and refracts light too strongly, forming images in front of the retina. A diverging concave lens corrects this."),
    C("basic", "What kind of image forms on the retina of a normal eye?", "An inverted, reduced real image", ["An upright, reduced real image", "An inverted, enlarged real image", "An upright, enlarged virtual image"],
      "The eye acts like a camera and forms an inverted, reduced real image on the retina."),
    C("standard", "Where does an image form when a farsighted person looks at a nearby object?", "Behind the retina", ["In front of the retina", "On the retina", "On the lens"],
      "A farsighted eye's lens refracts light too weakly, so the image of a nearby object forms behind the retina. A convex lens corrects this."),
    C("standard", "How can looking at a phone at close range for a long time change the lens and contribute to nearsightedness?", "It becomes thicker and refracts light more strongly", ["It becomes thinner and refracts light more weakly", "It becomes thicker and refracts light more weakly", "It does not change"],
      "Prolonged close viewing can fatigue the ciliary body, causing the lens to become thicker and refract light more strongly. Images of distant objects then form in front of the retina."),
  ])

T("telescope", (V, "Chapter 5", "Lenses and Their Applications", "5.5"), "Interdisciplinary Practice: Build a Telescope", "Interdisciplinary Practice", "application",
  "Learn that a Keplerian telescope uses two convex lenses: the objective forms an inverted, reduced real image, and the eyepiece acts as a magnifying glass. Build and adjust a simple telescope.",
  ["Know the roles of a telescope's objective and eyepiece", "Choose an objective and eyepiece based on their focal lengths"],
  [("5.2.2", "inferred"), ("2.3.5", "inferred")], pre=[("lens_rule", "hard")],
  qs=[
    C("basic", "In a telescope made of two convex lenses, what is the lens near the eye called?", "The eyepiece", ["The objective", "The reflector", "A concave lens"],
      "The eyepiece is near the eye, and the objective is near the object being viewed."),
    C("basic", "What kind of image does a telescope's objective form of a distant object?", "An inverted, reduced real image", ["An upright, enlarged virtual image", "An inverted, enlarged real image", "An upright, reduced virtual image"],
      "A distant object is more than twice the focal length from the objective, which forms an inverted, reduced real image."),
    C("standard", "What does a telescope's eyepiece do?", "It acts as a magnifying glass and enlarges the image formed by the objective", ["It acts as a camera", "It acts as a projector", "It makes the light diverge"],
      "The image formed by the objective lies within the eyepiece's focal length, so the eyepiece forms an upright, enlarged virtual image."),
    C("standard", "A telescope is made from two convex lenses with focal lengths of 50 cm and 5 cm. Which should be the objective?", "The lens with a 50 cm focal length", ["The lens with a 5 cm focal length", "Either lens", "A concave lens is required"],
      "A Keplerian telescope has a long-focal-length objective and a short-focal-length eyepiece, so the 50 cm lens should be the objective."),
  ])

# ---------------- Chapter 6: Mass and Density
T("mass", (V, "Chapter 6", "Mass and Density", "6.1"), "Mass", "Matter", "procedural",
  "Understand that mass is the amount of matter in an object and is an intrinsic property that does not change with shape, state, location, or temperature. Measure mass with a pan balance.",
  ["Convert mass units and estimate the mass of common objects", "Know that mass does not change with shape, state, or location", "Use a pan balance correctly: level it, zero it, balance it, and place the object on the left and weights on the right"],
  [("1.2.2", "exact"), ("4.1.1", "exact")], root="The starting point for measurement in mechanics: mass uses only the gram-to-kilogram conversions learned in primary school.",
  math=[("cnm_p139", "Adding the weights and rider readings uses decimal addition.")],
  qs=[
    C("basic", "What is the approximate mass of a middle-school student?", "50 kg", ["50 g", "500 kg", "5 kg"],
      "A middle-school student has a mass of about 50 kg; estimation is one of the goals of this topic."),
    C("basic", "What happens to the mass of a piece of ice when it melts into water?", "It stays the same", ["It increases", "It decreases", "It cannot be determined"],
      "Mass is an intrinsic property and does not change with state. The ice takes up less volume after melting, but its mass stays the same."),
    C("standard", "An object is weighed with 50 g, 20 g, and 5 g weights on the right pan, and the rider reads 2.4 g. What is the object's mass?", "77.4 g", ["75 g", "72.6 g", "77 g"],
      "Object mass = total weight mass + rider reading = 75 + 2.4 = 77.4 g.", verify="50+20+5+2.4"),
    C("standard", "While balancing a pan balance, the pointer is left of the scale's center. Which way should the leveling screw be turned?", "To the right", ["To the left", "Move the rider", "Add a weight to the right pan"],
      "When leveling a balance, adjust right if the pointer is left and left if the pointer is right. During weighing, balance it by adding or removing weights and moving the rider."),
  ])

T("density", (V, "Chapter 6", "Mass and Density", "6.2"), "Density", "Matter", "conceptual",
  "Understand density as a characteristic property of a substance and use ρ = m/V. Know the units kg/m³ and g/cm³ (1 g/cm³ = 1×10³ kg/m³) and calculate with the formula.",
  ["Calculate using ρ = m/V and its rearrangements", "Convert between g/cm³ and kg/m³", "Know that the density of a substance generally does not change with its mass or volume"],
  [("1.2.3", "exact")], pre=[("mass", "hard")],
  math=[("cnm_p213", "For the same substance, mass is proportional to volume, and density is the ratio between them."), ("cnm_200", "An m–V graph is a straight line through the origin (a direct-proportion function).")],
  qs=[
    C("basic", "The density of water is 1.0×10³ kg/m³. What does this mean?", "1 m³ of water has a mass of 1.0×10³ kg", ["1 kg of water has a volume of 1.0×10³ m³", "1 m³ of water has a mass of 1.0 kg", "The mass of water is 1.0×10³ kg"],
      "Density is the mass of a substance per unit volume."),
    C("basic", "A piece of metal has a mass of 54 g and a volume of 20 cm³. What is its density?", "2.7 g/cm³", ["1080 g/cm³", "0.37 g/cm³", "2.7 kg/m³"],
      "ρ = m/V = 54 g ÷ 20 cm³ = 2.7 g/cm³ (aluminum).", verify="54/20"),
    C("standard", "Half the oil in a bottle is used. What happens to the density of the remaining oil?", "It stays the same", ["It becomes half as large", "It doubles", "It cannot be determined"],
      "Density is a property of the substance and is independent of mass and volume. Both mass and volume are halved, so their ratio stays the same."),
    N("standard", "How many kg/m³ is 2.7 g/cm³? (Enter a number only)", "2700", "1 g/cm³ = 1000 kg/m³, so 2.7 g/cm³ = 2700 kg/m³.", "2.7*1000"),
  ])

T("density_measure", (V, "Chapter 6", "Mass and Density", "6.3"), "Measuring the Density of Liquids and Solids", "Matter", "procedural",
  "Measure volume with a graduated cylinder and determine the density of solids and liquids using a balance and graduated cylinder. Analyze how the order of experimental steps affects error.",
  ["Read a graduated cylinder correctly with the line of sight level with the bottom of the meniscus", "Use water displacement to measure a solid's volume and calculate its density", "Design steps for measuring liquid density while reducing error"],
  [("4.1.2", "exact"), ("1.2.3", "exact")], pre=[("density", "hard")],
  qs=[
    C("basic", "When measuring the volume of water with a graduated cylinder, how should you position your line of sight?", "Level with the bottom of the meniscus", ["Level with the top of the meniscus", "Look down from above", "Look up from below"],
      "Keep your line of sight level with the bottom of the meniscus. Looking down gives a reading that is too high; looking up gives one that is too low."),
    N("standard", "A graduated cylinder contains 40 mL of water. A small stone is added and the level rises to 60 mL. The stone has a mass of 52 g. What is its density in g/cm³? (Enter a number only)", "2.6",
      "V = 60 - 40 = 20 mL = 20 cm³, so ρ = 52 ÷ 20 = 2.6 g/cm³.", "52/(60-40)"),
    C("standard", "When measuring the density of salt water, which sequence of steps gives the least error?", "Measure the mass of the beaker and salt water, pour some into a graduated cylinder and measure its volume, then measure the mass of the beaker and remaining salt water", ["Measure the empty beaker, measure it with the salt water, then pour everything into a graduated cylinder to measure the volume", "Measure the volume with a graduated cylinder, then pour it into an empty beaker and measure its mass", "Measure only the mass of the beaker and salt water"],
      "In the first two methods, salt water remains on the beaker or graduated-cylinder walls, making the measured volume or mass too low. The difference method gives the mass and volume of the portion poured out and has the least error."),
    C("basic", "How many cm³ are in 1 mL?", "1 cm³", ["1000 cm³", "0.001 cm³", "10 cm³"],
      "1 mL = 1 cm³, and 1 L = 1000 mL = 1 dm³.", verify="1"),
  ])

T("density_use", (V, "Chapter 6", "Mass and Density", "6.4"), "Applications of Density", "Matter", "application",
  "Use density to identify substances, calculate mass or volume when it cannot be measured directly, and explain phenomena such as water expanding as it freezes and gas density changing with temperature.",
  ["Use density to identify substances", "Use m = ρV and V = m/ρ to find quantities that cannot be measured directly", "Explain phenomena such as the anomalous expansion of water"],
  [("1.2.3", "exact"), ("1.2.4", "inferred")], pre=[("density_measure", "hard")],
  qs=[
    N("basic", "A block of ice has a volume of 2 m³. Take the density of ice to be 0.9×10³ kg/m³. What is its mass in kg? (Enter a number only)", "1800", "m = ρV = 900 × 2 = 1800 kg.", "0.9e3*2"),
    C("basic", "Why are outdoor water pipes likely to crack in winter?", "Water's mass stays the same but its volume increases when it freezes", ["Water's mass increases when it freezes", "Water's density increases when it freezes", "The pipes expand when they get cold"],
      "Ice is less dense than liquid water. With the same mass, it takes up more volume and can burst the pipe."),
    C("standard", "A metal block has a mass of 158 g and a volume of 20 cm³. Which metal could it be, based on a density table?", "Iron (7.9 g/cm³)", ["Aluminum (2.7 g/cm³)", "Copper (8.9 g/cm³)", "Lead (11.3 g/cm³)"],
      "ρ = 158 ÷ 20 = 7.9 g/cm³, which matches iron."),
    C("advanced", "A bottle can hold up to 500 g of water. How much alcohol with a density of 0.8 g/cm³ can it hold?", "400 g", ["500 g", "625 g", "800 g"],
      "Bottle volume V = 500 g ÷ 1 g/cm³ = 500 cm³, so the mass of alcohol is m = 0.8 × 500 = 400 g.", verify="0.8*500"),
  ])
