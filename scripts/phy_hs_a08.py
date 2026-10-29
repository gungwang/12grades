"""Draft for Chapters 1–2 of Selective Compulsory, Book 2 (People's Education Press, 2019): Ampère and Lorentz forces, and electromagnetic induction."""
from phy_hs_lib import T, C, N

# ---------------- Chapter 1: Ampère and Lorentz Forces
T("ampere_force", "Motion and Interactions", "procedural",
  "A current-carrying wire in a magnetic field experiences an Ampère force. Its magnitude is F = BIL sinθ (θ is the angle between the current and magnetic-field directions); it is zero when they are parallel and maximum when they are perpendicular. Use the left-hand rule to find the direction, which is perpendicular to the plane containing the current and magnetic-field directions.",
  ["Calculate the Ampère force with F = BIL sinθ and find the equivalent length of a bent wire", "Use the left-hand rule to determine the force direction", "Understand the spatial relationship between the Ampère force, current, and magnetic-field directions"],
  [("S2.1.1", "exact")],
  pre=[("b_field", "hard"), ("magnetic_field", "hard"), ("ampere_rule", "soft"), ("J:magnet", "soft")],
  math=[("cnm_h060", "The sinθ in the Ampère-force magnitude comes from the definition of trigonometric functions; θ is the angle between the current and magnetic field.")],
  qs=[
    N("basic", "A 0.6 m straight wire carries a 4 A current in a uniform 0.5 T magnetic field. The angle between the wire and the field is 30°. What is the magnitude of the Ampère force on the wire, in N? (sin30° = 0.5; enter only the number)", "0.6",
      "F = BIL sinθ = 0.5 × 4 × 0.6 × 0.5 = 0.6 N. Omitting sinθ would give 1.2 N.", "0.5*4*0.6*0.5"),
    C("basic", "What is the direction of the Ampère force on a straight current-carrying wire in a uniform magnetic field, relative to the current and magnetic-field directions?", "perpendicular to the plane containing the current and magnetic-field directions", ["the same as the magnetic-field direction", "the same as the current direction", "along the bisector of the angle between the current and magnetic-field directions"],
      "Use the left-hand rule: point the palm toward the incoming magnetic field lines, the fingers along the current, and the thumb gives the force direction. The force is perpendicular to both the current and magnetic-field directions, not along the field lines; this differs from the electric force, which is along electric field lines."),
    C("standard", "Set up coordinates with the x-axis pointing east, the y-axis north, and the z-axis vertically upward. A horizontal straight wire carries current east, and the magnetic field there points vertically downward. In which direction is the Ampère force?", "north", ["south", "vertically upward", "vertically downward"],
      "With the magnetic field downward, hold the left palm upward and point the fingers east; the thumb points north. Alternatively, use the cross product I×B: x×(−z) = +y, or north. Reversing the direction gives south."),
    N("advanced", "A wire is bent into a right angle at b, with ab = 0.3 m, bc = 0.4 m, and ab ⊥ bc. A 2 A current flows from a through b to c. The wire is in a uniform 0.5 T magnetic field perpendicular to its plane. What is the magnitude of the Ampère force on the entire wire, in N? (Enter only the number)", "0.5",
      "The force on the bent wire equals the force on a straight wire connecting its endpoints a and c (the equivalent length): ac = √(0.3²+0.4²) = 0.5 m, so F = BIL = 0.5 × 2 × 0.5 = 0.5 N. Adding the forces on the two segments directly would give 0.7 N, because it ignores that their directions are perpendicular.", "0.5*2*sqrt(0.3**2+0.4**2)"),
  ])

T("ampere_meter", "Motion and Interactions", "application",
  "In a moving-coil meter, a radial uniform magnetic field lies between the horseshoe magnet and the iron core. The coil's plane is always parallel to the field lines, so the Ampère torque is proportional to the current. The spring's restoring torque is proportional to the deflection angle; therefore, the pointer's deflection is proportional to the current and the scale is uniform.",
  ["Explain why a radial magnetic field produces a uniform scale", "Calculate using the proportionality between deflection angle and current", "Know that reversing the current reverses the pointer and shorting the terminals reduces pointer movement during transport"],
  [("S2.1.1", "exact")],
  pre=[("ampere_force", "hard"), ("J:motor", "soft"), ("equilibrium", "soft")],
  qs=[
    C("basic", "A moving-coil ammeter has a radial uniform magnetic field between its horseshoe magnet and iron core. What is the main purpose of this design?", "the coil's plane stays parallel to the field lines, so the Ampère torque is proportional only to the current", ["the Ampère torque on the coil increases as its deflection angle increases", "the Ampère force on the coil becomes zero, keeping the pointer steady", "the magnetic force on the coil always points vertically upward"],
      "The radial field keeps the coil's plane parallel to the field lines, so the Ampère torque M = NBIS is proportional only to the current and independent of the deflection angle. The spring's restoring torque is proportional to the angle; at equilibrium, the angle is proportional to the current, giving a uniform scale."),
    N("basic", "A moving-coil ammeter's pointer deflects by 20° when a 2 mA current flows through it. What is the deflection when a 6 mA current flows within its range? (Enter only the number)", "60",
      "At equilibrium, NBIS = kθ, so deflection angle θ is proportional to current I: θ = 20° × 6/2 = 60°. Assuming the angle is proportional to the square of the current would give 180°.", "20*6/2"),
    C("standard", "When transporting a moving-coil ammeter, its two terminals are often connected with a wire to reduce pointer movement. Why?", "Coil rotation induces a current, and the Ampère force opposes the coil's rotation.", ["The short circuit increases the spring constant, making the pointer harder to deflect.", "The short circuit strengthens the magnet and holds the coil in place.", "The short circuit prevents an induced emf when the coil rotates."],
      "With the terminals shorted, the rotating coil cuts magnetic field lines and generates an emf. The short circuit closes the circuit, and the Ampère force on the induced current opposes the coil's motion, producing electromagnetic damping. Without a closed circuit, an emf is still induced, but there is no current and therefore no damping."),
    C("standard", "What happens if the two leads of a moving-coil ammeter are reversed so the current direction changes?", "The pointer deflects in the opposite direction because the Ampère torque depends on current direction.", ["It still deflects in the original direction because the torque depends only on current magnitude.", "It does not deflect because the current in the coil becomes zero.", "It deflects in the original direction, but by twice the angle."],
      "The left-hand rule determines the Ampère force direction. Reversing the current reverses the torque and pointer deflection. Therefore, connect the meter with current entering the positive terminal and leaving the negative terminal; reverse deflection can damage the meter."),
  ])

T("lorentz_force", "Motion and Interactions", "conceptual",
  "The force exerted by a magnetic field on a moving charge is the Lorentz force, with magnitude f = qvB when v is perpendicular to B; it is zero when v is parallel to B. Use the left-hand rule to find its direction: the fingers point in the direction a positive charge moves (opposite for a negative charge). The Lorentz force is always perpendicular to velocity and never does work.",
  ["Calculate the Lorentz force with f = qvB", "Determine the Lorentz-force direction for positive and negative charges", "Know that the Lorentz force never does work and changes only the direction of velocity"],
  [("S2.1.2", "exact")],
  pre=[("ampere_force", "hard"), ("b_field", "hard"), ("current", "soft")],
  qs=[
    N("basic", "A charged particle with charge 5×10⁻⁶ C enters a uniform 0.5 T magnetic field at 400 m/s, perpendicular to the field. What is the magnitude of the Lorentz force, in N? (Enter only the number)", "0.001",
      "f = qvB = 5×10⁻⁶ × 400 × 0.5 = 1×10⁻³ N = 0.001 N.", "5e-6*400*0.5"),
    C("basic", "Set up coordinates with the x-axis pointing east, the y-axis north, and the z-axis vertically upward. An electron moves east in a magnetic field pointing vertically downward. In which direction is the Lorentz force on the electron?", "south", ["north", "vertically upward", "vertically downward"],
      "For a positive charge, point the left-hand fingers east and the palm toward the incoming field; the thumb points north. An electron is negative, so point the fingers opposite its motion and reverse the force direction: south. Ignoring the negative charge would lead to north."),
    C("standard", "A charged particle moves in a uniform magnetic field under the Lorentz force alone. Which quantity must remain constant?", "kinetic energy", ["velocity", "momentum", "acceleration"],
      "The Lorentz force is always perpendicular to velocity and does no work, so kinetic energy stays constant. It changes the direction of velocity, so the directions of velocity, momentum (a vector), and acceleration change."),
    C("standard", "Which statement about the Lorentz force is correct?", "Its direction is always perpendicular to both the charge's velocity and the magnetic field.", ["A moving charge in a magnetic field always experiences a Lorentz force.", "The Lorentz force can increase a charged particle's speed.", "The Lorentz force points in the direction a positive charge moves."],
      "The Lorentz force is perpendicular to the plane defined by v and B. It is zero when v is parallel to B and changes only the direction of velocity, not its magnitude."),
  ])

T("charge_circular", "Motion and Interactions", "modeling",
  "When a charged particle enters a uniform magnetic field perpendicularly and is acted on only by the Lorentz force, it moves in a uniform circle. From qvB = mv²/r, r = mv/(qB), and the period T = 2πm/(qB), which is independent of speed and radius. Determine the circle's center and radius, then find the particle's position and travel time.",
  ["Calculate the radius and period using r = mv/(qB) and T = 2πm/(qB)", "Know that the period depends only on the charge-to-mass ratio and magnetic-field strength", "Use geometry to find the exit point in problems involving entry at a field boundary"],
  [("S2.1.3", "exact")],
  pre=[("lorentz_force", "hard"), ("centripetal_force", "hard"), ("newton2", "soft")],
  qs=[
    N("basic", "A particle with mass 6.4×10⁻²⁷ kg and charge 3.2×10⁻¹⁹ C enters a uniform 0.1 T magnetic field at 5×10⁵ m/s, perpendicular to the field. What is the radius of its circular path, in m? (Enter only the number)", "0.1",
      "From qvB = mv²/r, r = mv/(qB) = 6.4×10⁻²⁷ × 5×10⁵ ÷ (3.2×10⁻¹⁹ × 0.1) = 0.1 m.", "6.4e-27*5e5/(3.2e-19*0.1)"),
    C("basic", "The same charged particle moves in a uniform circle in the same uniform magnetic field. If only its speed is doubled (and it remains perpendicular to the field), which statement is correct?", "The radius doubles, and the period stays the same.", ["The radius stays the same, and the period doubles.", "Both the radius and period double.", "The radius quadruples, and the period stays the same."],
      "Since r = mv/(qB) is proportional to v, the radius doubles. The period T = 2πm/(qB) is independent of speed, so it stays the same. A common error is to assume the period depends on speed."),
    C("standard", "A proton (mass number 1, charge number 1) and an alpha particle (mass number 4, charge number 2) enter the same uniform magnetic field perpendicularly at the same speed. What is the ratio of their orbit radii, r_proton : r_alpha?", "1∶2", ["1∶4", "2∶1", "1∶1"],
      "Since r = mv/(qB) ∝ m/q, the proton has m/q = 1/1 and the alpha particle has m/q = 4/2 = 2. Thus r_proton : r_alpha = 1∶2. Comparing only the masses would incorrectly give 1∶4."),
    N("advanced", "A positive particle with q/m = 5×10⁷ C/kg enters a uniform magnetic field at point P on its boundary at 2×10⁶ m/s, making a 30° angle with the boundary. The field is perpendicular to the particle's plane of motion, and the region on one side of the boundary is large enough for the particle to curve back to it. If B = 0.1 T, how far from P does the particle exit the field, in m? (Enter only the number)", "0.4",
      "r = v/((q/m)B) = 2×10⁶ ÷ (5×10⁷ × 0.1) = 0.4 m. The particle enters and returns to the boundary, so the chord between its entry and exit points is 2r sin30° = 0.4 m (for an angle θ with the boundary, the chord is 2r sinθ, regardless of which side the particle bends toward). Using 2r, the result for perpendicular entry, would give 0.8 m.", "2*(2e6/(5e7*0.1))*0.5"),
  ])

T("mass_spectrometer", "Motion and Interactions", "application",
  "A mass spectrometer first accelerates ions in an electric field, qU = mv²/2, then deflects them in a uniform magnetic field, where the radius is r = (1/B)√(2mU/q). The landing position can be used to measure the charge-to-mass ratio and distinguish isotopes. In a velocity selector, qE = qvB, so v = E/B.",
  ["Find an ion's speed after acceleration using qU = mv²/2", "Compare ion masses or charge-to-mass ratios using orbit radii", "Know that the velocity-selector condition v = E/B is independent of charge magnitude and sign"],
  [("S2.1.3", "exact")],
  pre=[("charge_circular", "hard"), ("particle_accel", "hard"), ("work_energy_theorem", "soft")],
  qs=[
    N("basic", "An ion with charge-to-mass ratio q/m = 4×10⁷ C/kg is accelerated from rest through a 500 V potential difference. What is its speed on exit, in m/s? (Enter only the number)", "200000",
      "From qU = mv²/2, v = √(2(q/m)U) = √(2 × 4×10⁷ × 500) = √(4×10¹⁰) = 2×10⁵ m/s.", "sqrt(2*4e7*500)"),
    C("basic", "After being accelerated through the same voltage, singly charged neon-20 and neon-22 ions enter the same magnetic field. Which one lands farther from the entrance on the photographic plate?", "neon-22", ["neon-20", "they land the same distance away", "cannot be determined"],
      "With q, U, and B the same, r = (1/B)√(2mU/q) increases with mass m. Neon-22 is heavier, so it has a larger radius and lands farther away."),
    N("standard", "In a mass spectrometer, an ion is accelerated through 400 V and enters a uniform magnetic field of B = 0.1 T perpendicularly. Its orbit radius is 0.2 m. What is its charge-to-mass ratio q/m, in C/kg? (Enter only the number)", "2000000",
      "Eliminate v from qU = mv²/2 and r = mv/(qB): q/m = 2U/(B²r²) = 2 × 400 ÷ (0.01 × 0.04) = 2×10⁶ C/kg. Omitting the squares of B and r would give 4×10⁴ C/kg.", "2*400/(0.1**2*0.2**2)"),
    C("standard", "In a velocity selector, a uniform electric field and a uniform magnetic field are perpendicular. A positive particle travels straight through at speed v. If a positive particle with twice the charge enters at the same speed, what happens?", "It still travels straight through.", ["It deflects in the direction of the electric force.", "It deflects in the direction of the Lorentz force.", "It travels straight through but slows down."],
      "The condition for straight-line motion is qE = qvB, or v = E/B, independent of charge q. Doubling the charge doubles both the electric and Lorentz forces, so they still balance."),
  ])

T("cyclotron", "Motion and Interactions", "application",
  "In a cyclotron, particles move in circles in the magnetic field inside the D-shaped electrodes and are accelerated by the electric field each time they cross the gap. The alternating voltage's period must equal the particle's cyclotron period, T = 2πm/(qB). The maximum kinetic energy, Ekm = q²B²R²/(2m), is determined by the electrode radius R and is independent of the accelerating voltage.",
  ["Know that the alternating-voltage period equals the particle's cyclotron period", "Use Ekm = q²B²R²/(2m) to identify what affects maximum kinetic energy", "Calculate the number of acceleration events and revolutions from the total kinetic energy and energy gain per event"],
  [("S2.1.3", "exact")],
  pre=[("charge_circular", "hard"), ("particle_accel", "hard"), ("mass_spectrometer", "soft")],
  qs=[
    C("basic", "In a cyclotron, what must the alternating-voltage period be so that a particle is accelerated each time it crosses the gap?", "equal to the period of the particle's circular motion in the magnetic field", ["equal to the time it takes the particle to cross the gap", "gradually shorter as the particle speeds up", "half the particle's cyclotron period"],
      "The particle reaches the gap after every half revolution, so the electric field must reverse direction at that point. Therefore, the voltage period equals the cyclotron period T = 2πm/(qB). Since T is independent of speed, it does not need to change as the particle speeds up."),
    N("basic", "A cyclotron accelerates protons with an alternating-voltage frequency of 20 MHz. If the magnetic-field strength stays the same and it is changed to accelerate deuterons (same charge as a proton and about twice its mass), what should the voltage frequency be in MHz? (Enter only the number)", "10",
      "T = 2πm/(qB). A deuteron has twice the proton's mass and the same charge, so its period doubles and its frequency f = 1/T is halved to 10 MHz.", "20/2"),
    C("standard", "If only the accelerating voltage U is doubled while all other cyclotron conditions stay the same, how does the particle's maximum kinetic energy at exit change?", "It stays the same.", ["It doubles.", "It quadruples.", "It is halved."],
      "Ekm = q²B²R²/(2m) depends only on q, B, R, and m, not on the accelerating voltage. Doubling the voltage only halves the number of acceleration events and reduces the number of revolutions in the magnetic field."),
    N("advanced", "A proton exits a cyclotron with 20 MeV of energy, gaining 0.1 MeV each time it crosses the gap. How many revolutions does it make inside the D-shaped electrodes? (Enter only the number)", "100",
      "The proton is accelerated 20 ÷ 0.1 = 200 times. It crosses the gap twice per revolution, so it makes 200 ÷ 2 = 100 revolutions. Counting acceleration events as revolutions would give 200.", "20/0.1/2"),
  ])

# ---------------- Chapter 2: Electromagnetic Induction
T("exp_lenz", "Motion and Interactions", "procedural",
  "Insert and remove a bar magnet from a coil, observe the ammeter pointer, and investigate how the induced-current direction relates to the magnet's motion and magnetic-field direction. Before the experiment, briefly touch the ammeter with a dry cell in series with a protective resistor to establish how current direction corresponds to pointer deflection.",
  ["Know that the pointer-deflection/current-direction relationship must be established before the experiment", "Analyze flux changes and induced-field direction from the magnet's polarity and motion", "Infer the rule for induced-current direction from experimental observations"],
  [("S2.X.1", "exact"), ("S2.2.1", "exact")],
  pre=[("em_induction", "hard"), ("flux", "hard"), ("ampere_rule", "soft"), ("J:induction", "soft")],
  qs=[
    C("basic", "In an experiment on induced-current direction, a dry cell with a protective resistor in series is briefly connected to the ammeter before the magnet is inserted into the coil. What is the purpose?", "to establish how pointer deflection corresponds to current direction", ["to measure the dry cell's emf", "to check whether the magnet is magnetic", "to eliminate the effect of Earth's magnetic field"],
      "The induced-current direction is inferred from pointer deflection, so first determine which way the pointer moves when current enters each terminal."),
    C("basic", "A coil is fixed, and a bar magnet with its N pole downward is pushed into the coil from above. Which statement about the magnetic field produced by the induced current is correct?", "It points upward, opposite to the magnet's field inside the coil.", ["It points downward, in the same direction as the magnet's field inside the coil.", "It points upward because the magnet's field points upward.", "There is no induced field because the magnet has not passed through the coil."],
      "With the N pole downward, the original field inside the coil points downward and the flux increases. The induced field opposes this increase, so it points upward."),
    C("standard", "After a bar magnet is inserted into a coil, it is held still inside the coil. What happens to the ammeter pointer?", "It returns to zero because the magnetic flux is no longer changing.", ["It stays deflected because the flux inside the coil is large.", "It deflects the opposite way because the magnet has stopped.", "Its deflection gradually decreases but does not reach zero."],
      "An induced current requires changing magnetic flux. When the magnet is still, the flux may be large but is not changing, so there is no induced current."),
    C("standard", "In an experiment, the ammeter pointer deflects to the right when a bar magnet's N pole is pushed downward into a coil. Which operation also makes the pointer deflect to the right?", "Pull the magnet upward out of the coil with its S pole downward.", ["Pull the magnet upward out of the coil with its N pole downward.", "Push the magnet downward into the coil with its S pole downward.", "Hold the magnet still inside the coil."],
      "As the N pole is pushed down, downward flux increases and the induced field points upward. When the S pole points down and is pulled upward, the original upward field decreases, so the induced field also points upward and the pointer deflects right. Pulling the N pole upward or pushing the S pole downward induces a downward field and a leftward deflection."),
  ])

T("lenz", "Motion and Interactions", "reasoning",
  "An induced current flows in a direction such that its magnetic field opposes the change in magnetic flux that produced it. 'Opposes' means that the change is slowed, not prevented, and does not simply mean 'opposite': when flux increases, the induced field opposes the original field; when flux decreases, it reinforces the original field.",
  ["Use Lenz's law and the right-hand grip rule to determine induced-current direction", "Understand that 'opposes' does not mean 'prevents' or simply 'opposite'", "Analyze conductor motion using approach-repel/recede-follow and the loop's tendency to contract as flux increases or expand as it decreases"],
  [("S2.2.1", "exact")],
  pre=[("exp_lenz", "hard"), ("ampere_rule", "hard"), ("flux", "hard"), ("J:induction", "soft")],
  qs=[
    C("basic", "Which statement correctly describes 'opposes' in Lenz's law?", "The induced magnetic field opposes the change in magnetic flux that produced the induced current.", ["The induced magnetic field is always opposite to the original field.", "The induced magnetic field always prevents the original flux from changing.", "The induced magnetic field opposes the original magnetic field itself."],
      "It is the change in flux that is opposed: as flux increases, the induced field opposes the original field; as flux decreases, it points in the same direction. 'Opposes' does not mean 'prevents'; the flux still changes, but more slowly."),
    C("basic", "A closed circular loop lies in the page in a uniform magnetic field pointing into the page. As the field strength increases, in which direction does the induced current flow when viewed from the front of the page?", "counterclockwise", ["clockwise", "there is no induced current", "its direction keeps changing"],
      "The inward flux increases, so the induced field points outward to oppose the increase. By the right-hand grip rule, the current is counterclockwise when viewed from the front."),
    C("standard", "A closed metal loop lies in a uniform magnetic field perpendicular to its plane. If the field strength increases uniformly, what tendency does the loop have?", "It tends to shrink.", ["It tends to expand.", "It has no tendency to change.", "It first expands and then shrinks."],
      "The flux Φ = BS increases. To oppose the increase in flux, the loop tends to reduce its area."),
    C("advanced", "A bar magnet with its N pole downward moves toward a closed horizontal copper ring from above. Viewed from above, what are the direction of the induced current in the ring and the direction of the force on the magnet?", "counterclockwise; upward on the magnet", ["clockwise; upward on the magnet", "counterclockwise; downward on the magnet", "clockwise; downward on the magnet"],
      "As the magnet's N pole approaches, downward flux through the ring increases, so the induced field points upward and the current is counterclockwise when viewed from above. The top of the ring acts like an N pole, repelling the magnet's N pole upward."),
  ])

T("faraday", "Motion and Interactions", "procedural",
  "The magnitude of the induced emf in a closed circuit is proportional to the rate of change of magnetic flux through it: E = nΔΦ/Δt. E depends on ΔΦ/Δt (the slope of a Φ–t graph), not on Φ itself or on ΔΦ alone. If B changes uniformly while the area stays constant, E = nSΔB/Δt.",
  ["Calculate induced emf using E = nΔΦ/Δt", "Know that E depends on the rate of change of flux, not on Φ or ΔΦ alone", "Compare emf magnitudes using Φ–t or B–t graphs"],
  [("S2.2.2", "exact")],
  pre=[("lenz", "soft"), ("flux", "hard"), ("em_induction", "hard"), ("closed_circuit", "soft")],
  math=[("cnm_202", "The slope of a Φ–t graph is the rate of change of magnetic flux, just as the slope of a linear-function graph represents its rate of change.")],
  qs=[
    N("basic", "A 50-turn coil experiences a uniform increase in magnetic flux from 0.01 Wb to 0.05 Wb over 0.2 s. What is the magnitude of the induced emf, in V? (Enter only the number)", "10",
      "E = nΔΦ/Δt = 50 × (0.05 − 0.01) ÷ 0.2 = 10 V. Forgetting the number of turns would give 0.2 V.", "50*(0.05-0.01)/0.2"),
    C("basic", "Which statement about the magnitude of induced emf is correct?", "The faster the magnetic flux through a coil changes, the greater the induced emf.", ["The greater the magnetic flux through a coil, the greater the induced emf.", "The greater the change in magnetic flux through a coil, the greater the induced emf.", "The induced emf must be zero whenever the magnetic flux is zero."],
      "E = nΔΦ/Δt depends on the rate of change of flux. A large Φ does not necessarily mean a fast change, and a large ΔΦ may take a long time. The rate of change can be large at an instant when Φ is zero."),
    C("standard", "In a single-turn closed coil, the flux changes with time as follows: from 0 to 2 s, it increases uniformly from 0 to 0.4 Wb; from 2 to 4 s, it stays at 0.4 Wb; from 4 to 8 s, it decreases uniformly to 0. Which statement is correct?", "The induced emf is zero from 2 to 4 s, and its magnitude from 4 to 8 s is half its magnitude from 0 to 2 s.", ["The flux is greatest from 2 to 4 s, so the induced emf is greatest.", "The flux changes by the same amount from 0 to 2 s and from 4 to 8 s, so the induced emf magnitudes are equal.", "The flux decreases from 4 to 8 s, so there is no induced emf."],
      "From 0 to 2 s: E = 0.4/2 = 0.2 V. From 2 to 4 s: ΔΦ = 0, so E = 0. From 4 to 8 s: E = 0.4/4 = 0.1 V, half the first value. The same ΔΦ over different Δt gives different emf."),
    N("standard", "A 100-turn coil has an area of 0.02 m². The magnetic field perpendicular to its plane increases uniformly from 0.2 T to 0.8 T over 0.3 s. What is the magnitude of the induced emf, in V? (Enter only the number)", "4",
      "E = nSΔB/Δt = 100 × 0.02 × (0.8 − 0.2) ÷ 0.3 = 4 V.", "100*0.02*(0.8-0.2)/0.3"),
  ])

T("emf_cutting", "Motion and Interactions", "procedural",
  "When a rod cuts magnetic field lines perpendicularly in a uniform magnetic field, E = BLv. If the angle between velocity v and magnetic field B is θ, E = BLv sinθ. Use the right-hand rule to find the direction; inside a conductor acting as a source, current flows from lower to higher potential. For a rod rotating uniformly about one end, E = BL²ω/2.",
  ["Calculate emf using E = BLv and E = BLv sinθ", "Use the right-hand rule to determine current direction and which end is at higher potential", "Calculate the induced emf in a rod rotating about one endpoint"],
  [("S2.2.2", "exact")],
  pre=[("faraday", "hard"), ("lorentz_force", "soft"), ("lenz", "soft"), ("J:induction", "soft")],
  math=[("cnm_h060", "The sinθ in E = BLv sinθ requires the definition and values of trigonometric functions.")],
  qs=[
    N("basic", "A 0.4 m conducting rod moves uniformly at 10 m/s in a uniform 0.5 T magnetic field, perpendicular to both the field lines and the rod. What is the induced emf between its ends, in V? (Enter only the number)", "2",
      "E = BLv = 0.5 × 0.4 × 10 = 2 V.", "0.5*0.4*10"),
    C("basic", "A 0.5 m rod moves at 10 m/s in a uniform magnetic field with B = 0.4 T. The velocity makes a 30° angle with the field, and the rod is perpendicular to both the velocity and the field. What is the induced emf between its ends? (Take cos30° ≈ 0.87.)", "1 V", ["2 V", "1.7 V", "0.5 V"],
      "E = BLv sinθ = 0.4 × 0.5 × 10 × 0.5 = 1 V. Omitting sinθ gives 2 V; using cos30° incorrectly gives about 1.7 V; multiplying L by sinθ as well gives 0.5 V.", verify="0.4*0.5*10*0.5"),
    C("standard", "Rod ab is vertical in the plane of the page, with a above b. It moves to the right in that plane while a uniform magnetic field points into the page. The rod is not connected to a closed circuit. Which statement about the potentials at a and b is correct?", "The potential at a is higher than at b.", ["The potential at b is higher than at a.", "The potentials are equal because there is no closed circuit.", "The potential difference cannot be determined."],
      "By the right-hand rule, the field enters the palm, the thumb points right (the direction of motion), and the fingers point upward along the current in the rod, from b to a. The rod acts as a source, with current inside the source flowing from the negative terminal to the positive terminal, so a is positive and at higher potential. With no closed circuit there is no current, but the emf still exists."),
    N("advanced", "A 0.4 m metal rod is fixed at one end, O, and rotates uniformly at 50 rad/s in a plane perpendicular to the magnetic field. If B = 0.5 T, what is the induced emf between the rod's ends, in V? (Enter only the number)", "2",
      "Points along the rod have different speeds, so the average speed is v = ωL/2. E = BL·ωL/2 = BL²ω/2 = 0.5 × 0.16 × 50 ÷ 2 = 2 V. Using the endpoint speed ωL in BLv would give 4 V.", "0.5*0.4**2*50/2"),
  ])

T("induction_dynamics", "Motion and Interactions", "modeling",
  "Model a conductor cutting magnetic field lines as a source (emf E and internal resistance r), then use Ohm's law for a closed circuit to analyze current and terminal voltage. The Ampère force does negative work; other energy is converted first to electrical energy and then to Joule heat. When force balance F = B²L²v/R_total is reached, the rod reaches terminal speed. The charge passing through the circuit is q = nΔΦ/R_total.",
  ["Analyze a conductor cutting magnetic field lines as a source and distinguish emf from terminal voltage", "Use Newton's laws and force balance to find terminal speed", "Use energy relations and q = ΔΦ/R_total to analyze energy and charge"],
  [("S2.2.2", "exact"), ("S2.2.1", "inferred")],
  pre=[("emf_cutting", "hard"), ("ampere_force", "hard"), ("closed_circuit", "hard"), ("lenz", "soft")],
  qs=[
    N("basic", "Two smooth horizontal parallel rails are 0.5 m apart and connected at the left end to a 1.5 Ω resistor R. A conducting rod ab perpendicular to the rails has a resistance of 0.5 Ω. A uniform magnetic field B = 0.8 T is perpendicular to the plane of the rails. The rod moves right at a constant 5 m/s. What is the voltage between a and b, in V? (Ignore rail resistance; enter only the number)", "1.5",
      "E = BLv = 0.8 × 0.5 × 5 = 2 V; I = E/(R+r) = 2 ÷ 2 = 1 A. The rod is a source, so the voltage between a and b is the terminal voltage U = IR = 1.5 V, not the 2 V emf.", "0.8*0.5*5/(1.5+0.5)*1.5"),
    C("basic", "A rod slides down a smooth inclined pair of parallel rails at constant speed in a uniform magnetic field. A resistor is connected at the bottom of the rails, and the resistances of the rod and rails cannot be ignored. Which statement is correct?", "The rod's loss of gravitational potential energy equals the Joule heat generated in the circuit.", ["All the rod's lost gravitational potential energy becomes kinetic energy.", "The Ampère force does positive work on the rod, converting electrical energy into mechanical energy.", "The Ampère force does no work on the rod because the Lorentz force never does work."],
      "The rod's kinetic energy is constant as it slides at constant speed. All work done by gravity goes against the Ampère force, is converted to electrical energy, and then becomes Joule heat; the Ampère force does negative work on the rod. The two Lorentz-force components on the charges do zero net work, but the Ampère force is the macroscopic resultant and does work on the rod."),
    N("standard", "Two horizontal parallel rails are 0.4 m apart, friction is negligible, and a uniform magnetic field B = 1.0 T is perpendicular to the rails. A 0.1 kg metal rod starts from rest under a constant horizontal force F = 0.8 N. The total circuit resistance is 0.8 Ω. What is the rod's terminal speed, in m/s? (Enter only the number)", "4",
      "At terminal speed, acceleration is zero: F = BIL = B²L²v/R, so v = FR/(B²L²) = 0.8 × 0.8 ÷ (1 × 0.16) = 4 m/s.", "0.8*0.8/(1.0**2*0.4**2)"),
    N("advanced", "Two horizontal parallel rails are 0.4 m apart. A uniform magnetic field B = 0.5 T is perpendicular to the rails, and the total circuit resistance is 0.5 Ω. A metal rod starts from rest and slides 0.5 m under an external force. What charge passes through the circuit, in C? (Enter only the number)", "0.2",
      "q = IΔt = (E/R)Δt = ΔΦ/R = BLx/R = 0.5 × 0.4 × 0.5 ÷ 0.5 = 0.2 C, independent of how the rod's speed changes.", "0.5*0.4*0.5/0.5"),
  ])

T("eddy", "Motion and Interactions", "conceptual",
  "When a bulk metal is in a changing magnetic field or moves through a magnetic field, swirling induced currents called eddy currents form inside it. The Ampère force on these currents opposes relative motion, producing electromagnetic damping; a moving magnetic field can also drive a conductor, producing electromagnetic drive. Eddy currents can be used for heating (induction cooktops and vacuum smelting) but may also need to be suppressed to prevent heating (by laminating silicon-steel sheets to make a core).",
  ["Know how eddy currents form", "Explain electromagnetic damping and electromagnetic drive", "Distinguish applications of eddy currents from methods of reducing them"],
  [("S2.2.3", "exact")],
  pre=[("lenz", "hard"), ("faraday", "hard"), ("energy_conservation", "soft")],
  qs=[
    C("basic", "What are eddy currents?", "swirling induced currents that form inside a bulk metal in a changing magnetic field or when it moves through a magnetic field", ["directed current formed by free electrons in a metal under a constant electric field", "closed magnetic field lines around a current-carrying coil", "rotational motion of a conductor caused by the Ampère force in a magnetic field"],
      "Eddy currents are induced currents that form inside a bulk conductor through electromagnetic induction; because its resistance is low, the current can be large. They are currents, not magnetic field lines or mechanical motion, and are not driven by a constant electric field."),
    C("basic", "A strong magnet is released from rest at the top of a vertical copper tube and falls much more slowly than it does through a plastic tube. Why?", "Eddy currents form in the copper tube, and their Ampère force opposes the magnet's motion.", ["The magnetized copper tube attracts the magnet upward.", "The magnet experiences greater air resistance in the copper tube.", "The magnet experiences greater buoyancy in the copper tube."],
      "As the magnet moves relative to the copper tube, the flux through its walls changes and produces eddy currents. By Lenz's law, their magnetic field opposes the relative motion, exerting an upward force on the magnet; this is electromagnetic damping. Once the magnet reaches constant speed, its lost gravitational potential energy is converted to internal energy in the copper tube."),
    C("standard", "A horseshoe magnet rotates uniformly about a vertical axis. A closed aluminum frame that can rotate freely is fitted around the axis. How does the frame move?", "It rotates in the same direction as the magnet, but more slowly.", ["It rotates opposite to the magnet.", "It rotates in the same direction at the same speed as the magnet.", "It stays still because aluminum cannot be magnetized."],
      "The rotating magnet changes the flux through the aluminum frame and induces eddy currents. The Ampère force makes the frame follow the field (electromagnetic drive) and opposes their relative motion, so they rotate in the same direction. If they rotated at the same speed, there would be no relative motion, induced current, or driving force; therefore, the frame must rotate more slowly."),
    C("standard", "Which practice is intended to reduce eddy currents?", "making a transformer core from thin, mutually insulated silicon-steel sheets", ["using an alternating magnetic field to heat the bottom of a pan in an induction cooktop", "using high-frequency current to melt metal in a vacuum furnace", "using eddy currents to detect underground metal with a metal detector"],
      "A solid core would develop large eddy currents and heat up in an alternating magnetic field. Laminating it from insulated sheets increases the resistance of the eddy-current paths and reduces the currents; the other three options use eddy currents."),
  ])

T("self_inductance", "Motion and Interactions", "reasoning",
  "When current in a coil changes, the coil induces an emf in itself; this is self-induction, E = LΔI/Δt. Its direction always opposes the change in current, but does not prevent it. When a circuit is switched on, current increases gradually; when it is switched off, the coil acts like a source and current decreases gradually. Mutual induction occurs when a changing current in one of two nearby coils creates a changing magnetic field that induces an emf in the other coil. No wire connection is needed; transformers use mutual induction.",
  ["Understand that self-induced emf opposes, but does not prevent, changes in current; know mutual induction and its applications", "Analyze how bulbs brighten or dim when a circuit is switched on or off, including conditions for a flash", "Calculate self-induced emf using E = LΔI/Δt"],
  [("S2.2.3", "exact")],
  pre=[("lenz", "hard"), ("faraday", "hard"), ("series_parallel", "soft"), ("J:electromagnet", "soft")],
  qs=[
    C("basic", "Which statement about self-induction and mutual induction is correct?",
      "Self-induced emf opposes changes in the coil's own current; mutual induction produces an emf in a nearby second coil.",
      ["Self-induced emf always prevents changes in the coil's own current; mutual induction produces an emf in a nearby second coil.",
       "Self-induced emf always points opposite to the original current in the coil; mutual induction produces an emf in a nearby second coil.",
       "Self-induced emf opposes changes in the coil's own current; mutual induction occurs only when the two coils are connected by wires."],
      "Self-induced emf opposes a change in current: when current increases, it points opposite to the original current; when current decreases, it points in the same direction. Opposing does not prevent the change. In mutual induction, a changing current in one coil produces a changing magnetic field, which changes the flux through a nearby coil and induces an emf. The coils do not need to be connected by wires; transformers use mutual induction."),
    C("basic", "Coil L (whose DC resistance is much less than the resistance of bulb A) is connected in parallel with bulb A across a power supply. After the switch has been closed for a long time, it is opened. At the instant it opens, how does bulb A's brightness and current direction change?", "It first becomes brighter than before, then gradually goes out; the current reverses direction.", ["It goes out immediately.", "It gradually goes out without becoming brighter, and the current keeps its original direction.", "It first becomes brighter than before, then gradually goes out; the current keeps its original direction."],
      "At steady state, the L branch has low resistance, so IL > IA. After the switch opens, L and A form a loop. The current through L decreases gradually, and the current through A flows opposite to its original direction; its initial value is IL, greater than the original IA, so the bulb flashes brighter before going out. If IL ≤ IA, it only dims gradually."),
    C("standard", "Two identical bulbs, A and B, are in parallel branches across a power supply. Bulb A is in series with coil L, while bulb B is in series with a fixed resistor R. The DC resistance of L equals R. What happens just after the switch closes and once the circuit reaches steady state?", "Bulb B lights immediately, bulb A brightens gradually, and both bulbs have the same brightness at steady state.", ["Both bulbs light immediately and have the same brightness at steady state.", "Bulb A lights immediately, and bulb B brightens gradually.", "Bulb A brightens gradually and remains dimmer than bulb B at steady state."],
      "At the instant the switch closes, L produces a self-induced emf that opposes the increase in current, so the current in A's branch rises gradually. Branch B contains only a resistor, so its current reaches its steady value immediately. At steady state, self-induction ceases and L acts only as a resistor equal to R, so the bulbs have the same brightness."),
    N("standard", "The current in a coil with self-inductance 2 H decreases uniformly from 0.5 A to 0 in 0.01 s. What is the magnitude of the self-induced emf, in V? (Enter only the number)", "100",
      "E = LΔI/Δt = 2 × 0.5 ÷ 0.01 = 100 V. Self-induced emf is proportional to how quickly the current changes, not to the current's magnitude.", "2*0.5/0.01"),
  ])
