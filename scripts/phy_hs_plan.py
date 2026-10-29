"""High school physics knowledge-point plan for the 2019 People's Education Press edition, aligned with the General Senior High School Physics Curriculum Standards (2017 edition, revised in 2020).

Textbook structure is based on the 2019 tables of contents for the People's Education Press High School Physics required and selective-required Volumes I–III, and the Teacher's Home table of contents at renjiaoshe.com (checked 2026-10-23). Knowledge-point keys, names, and chapter assignments are fixed here;
draft files (phy_hs_*.py) register content by key and get chapter names from this plan. IDs are assigned in this order, starting at cnp_h001.

Grade values: 10 required Volume I, 11 required Volume II, 12 required Volume III, 13 selective-required Volume I, 14 selective-required Volume II, and 15 selective-required Volume III (matching the high school English numbering).
"""
from __future__ import annotations

CN_NUM = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen"}

# The Chinese volume labels below are internal lookup tokens shared by BOOKS, _RAW, and ASSIGN; keep them stable.
BOOKS = {
    "必修一": dict(grade=10, mod="B1", full="Required Volume I"),
    "必修二": dict(grade=11, mod="B2", full="Required Volume II"),
    "必修三": dict(grade=12, mod="B3", full="Required Volume III"),
    "选必一": dict(grade=13, mod="S1", full="Selective Required Volume I"),
    "选必二": dict(grade=14, mod="S2", full="Selective Required Volume II"),
    "选必三": dict(grade=15, mod="S3", full="Selective Required Volume III"),
}

# (volume, [(chapter number, chapter name, [(section number, section title, [(key, topic name), ...]), ...]), ...])
_RAW = [
 ("必修一", [
  (1, "Describing Motion", [
    (1, "Particle and Reference Frame", [("particle_ref", "Particles and Reference Frames")]),
    (2, "Time and Displacement", [("displacement", "Time, Instants, and Displacement")]),
    (3, "Describing the Rate of Change in Position: Velocity", [("velocity", "Average and Instantaneous Velocity")]),
    (4, "Describing the Rate of Change in Velocity: Acceleration", [("acceleration", "Acceleration")]),
  ]),
  (2, "Studying Uniformly Accelerated Linear Motion", [
    (1, "Experiment: Investigating How a Cart's Velocity Changes with Time", [("exp_vt", "Experiment: Investigating How a Cart's Velocity Changes with Time")]),
    (2, "Velocity–Time Relationship in Uniformly Accelerated Linear Motion", [("vt_formula", "Velocity–Time Relationship in Uniformly Accelerated Linear Motion")]),
    (3, "Displacement–Time Relationship in Uniformly Accelerated Linear Motion", [("xt_formula", "Displacement–Time Relationship in Uniformly Accelerated Linear Motion"),
                                         ("vx_formula", "Velocity–Displacement Relationship and Deductions for Uniformly Accelerated Motion")]),
    (4, "Free Fall", [("free_fall", "Free-Fall Motion")]),
  ]),
  (3, "Interactions—Forces", [
    (1, "Gravity and Elastic Force", [("gravity", "Gravity"), ("elastic_force", "Elastic Force and Hooke's Law"),
                    ("exp_spring", "Experiment: Investigating the Relationship Between Spring Force and Deformation")]),
    (2, "Friction", [("static_friction", "Static Friction"), ("kinetic_friction", "Kinetic Friction")]),
    (3, "Newton's Third Law", [("newton3", "Newton's Third Law")]),
    (4, "Adding and Resolving Forces", [("force_compose", "Force Composition"),
                        ("exp_parallelogram", "Experiment: Investigating the Resultant of Two Forces Acting at an Angle"),
                        ("force_decompose", "Resolving Forces")]),
    (5, "Equilibrium of Concurrent Forces", [("equilibrium", "Equilibrium of Concurrent Forces")]),
  ]),
  (4, "Motion and Force Relationships", [
    (1, "Newton's First Law", [("newton1", "Newton's First Law"), ("inertia", "Inertia and Mass")]),
    (2, "Experiment: Investigating the Relationship Between Acceleration, Force, and Mass", [("exp_newton2", "Experiment: Investigating the Relationship Between Acceleration, Force, and Mass")]),
    (3, "Newton's Second Law", [("newton2", "Newton's Second Law")]),
    (4, "System of Mechanical Units", [("units", "System of Mechanical Units")]),
    (5, "Applications of Newton's Laws of Motion", [("dyn_apply", "Applications of Newton's Laws of Motion"), ("connected", "Connected-Body Problems: System and Individual-Body Methods")]),
    (6, "Apparent Weight: Overweight and Weightlessness", [("weightless", "Overweight and Weightlessness")]),
  ]),
 ]),
 ("必修二", [
  (5, "Projectile Motion", [
    (1, "Curvilinear Motion", [("curve_motion", "Curvilinear Motion")]),
    (2, "Composition and Resolution of Motion", [("motion_compose", "Composition and Resolution of Motion")]),
    (3, "Experiment: Investigating the Properties of Horizontal Projectile Motion", [("exp_projectile", "Experiment: Investigating the Properties of Horizontal Projectile Motion")]),
    (4, "Projectile-Motion Equations", [("projectile", "Equations for Horizontal Projectile Motion"), ("oblique", "Oblique Projectile Motion")]),
  ]),
  (6, "Circular Motion", [
    (1, "Circular Motion", [("circular", "Describing Circular Motion")]),
    (2, "Centripetal Force", [("centripetal_force", "Centripetal Force"),
                 ("exp_centripetal", "Experiment: Investigating How Centripetal Force Depends on Radius, Angular Velocity, and Mass")]),
    (3, "Centripetal Acceleration", [("centripetal_accel", "Centripetal Acceleration")]),
    (4, "Circular Motion in Daily Life", [("circular_apply", "Circular Motion in Daily Life"), ("centrifugal", "Centrifugal Effect")]),
  ]),
  (7, "Universal Gravitation and Spaceflight", [
    (1, "Planetary Motion", [("kepler", "Planetary Motion")]),
    (2, "Law of Universal Gravitation", [("gravitation", "Law of Universal Gravitation")]),
    (3, "Applications of the Theory of Universal Gravitation", [("celestial_calc", "Applications of the Theory of Universal Gravitation")]),
    (4, "Spaceflight", [("cosmic_speed", "Escape Velocities"), ("satellite_orbit", "Motion of Artificial Satellites")]),
    (5, "Relativistic Spacetime and the Limits of Newtonian Mechanics", [("relativity", "Relativistic Spacetime and the Limits of Newtonian Mechanics")]),
  ]),
  (8, "Law of Conservation of Mechanical Energy", [
    (1, "Work and Power", [("work", "Work"), ("power", "Power")]),
    (2, "Gravitational Potential Energy", [("gravity_pe", "Gravitational Potential Energy"), ("elastic_pe", "Elastic Potential Energy")]),
    (3, "Kinetic Energy and the Work–Energy Theorem", [("kinetic_energy", "Kinetic Energy"), ("work_energy_theorem", "Work–Energy Theorem")]),
    (4, "Law of Conservation of Mechanical Energy", [("energy_conservation", "Law of Conservation of Mechanical Energy")]),
    (5, "Experiment: Verifying Conservation of Mechanical Energy", [("exp_energy", "Experiment: Verifying Conservation of Mechanical Energy")]),
  ]),
 ]),
 ("必修三", [
  (9, "Electrostatic Fields and Their Applications", [
    (1, "Electric Charge", [("charge", "Electric Charge")]),
    (2, "Coulomb's Law", [("coulomb", "Coulomb's Law")]),
    (3, "Electric Fields and Field Strength", [("e_field", "Electric Field Strength"), ("field_lines", "Electric Field Lines and Superposition of Electric Fields")]),
    (4, "Prevention and Applications of Static Electricity", [("electrostatic_app", "Prevention and Applications of Static Electricity")]),
  ]),
  (10, "Energy in Electrostatic Fields", [
    (1, "Electric Potential Energy and Electric Potential", [("electric_pe", "Electric Potential Energy"), ("potential", "Electric Potential")]),
    (2, "Potential Difference", [("potential_diff", "Potential Difference"), ("equipotential", "Equipotential Surfaces")]),
    (3, "Relationship Between Potential Difference and Electric Field Strength", [("u_e_relation", "Relationship Between Potential Difference and Electric Field Strength")]),
    (4, "Capacitance", [("capacitor", "Capacitance"), ("exp_capacitor", "Experiment: Observing Capacitor Charging and Discharging")]),
    (5, "Motion of Charged Particles in an Electric Field", [("particle_accel", "Acceleration of Charged Particles in an Electric Field"),
                              ("particle_deflect", "Deflection of Charged Particles in an Electric Field")]),
  ]),
  (11, "Circuits and Their Applications", [
    (1, "Sources of EMF and Electric Current", [("current", "Sources of EMF and Electric Current")]),
    (2, "Resistance of Conductors", [("ohm_law", "Ohm's Law and Voltage–Current Characteristic Curves"), ("resistance", "Resistance and Resistivity")]),
    (3, "Experiment: Measuring Conductor Resistivity", [("exp_length", "Experiment: Measuring Length and Selecting Measuring Instruments"),
                              ("exp_resistivity", "Experiment: Measuring Conductor Resistivity")]),
    (4, "Series and Parallel Circuits", [("series_parallel", "Series and Parallel Circuits"), ("meter_modify", "Modifying Meters")]),
    (5, "Experiment: Using a Multimeter", [("exp_multimeter", "Experiment: Using a Multimeter")]),
  ]),
  (12, "Electric Energy and the Law of Conservation of Energy", [
    (1, "Energy Conversion in Circuits", [("electric_work", "Electrical Work and Power"), ("joule", "Joule's Law"),
                         ("household", "Household Circuits and Electrical Safety")]),
    (2, "Ohm's Law for Closed Circuits", [("emf", "Electromotive Force"), ("closed_circuit", "Ohm's Law for Closed Circuits"),
                           ("circuit_dynamic", "Dynamic Analysis and Power in Closed Circuits")]),
    (3, "Experiment: Measuring a Battery's EMF and Internal Resistance", [("exp_emf", "Experiment: Measuring a Battery's EMF and Internal Resistance")]),
    (4, "Energy and Sustainable Development", [("energy_sustain", "Energy and Sustainable Development")]),
  ]),
  (13, "Electromagnetic Induction and Introductory Electromagnetic Waves", [
    (1, "Magnetic Fields and Magnetic Field Lines", [("magnetic_field", "Magnetic Fields and Magnetic Field Lines"), ("ampere_rule", "Magnetic Fields from Currents and Ampère's Right-Hand Rule")]),
    (2, "Magnetic Flux Density and Magnetic Flux", [("b_field", "Magnetic Flux Density"), ("flux", "Magnetic Flux")]),
    (3, "Electromagnetic Induction and Its Applications", [("em_induction", "Electromagnetic Induction and Its Applications")]),
    (4, "Discovery and Applications of Electromagnetic Waves", [("em_wave", "Discovery and Applications of Electromagnetic Waves")]),
    (5, "Energy Quantization", [("quantum", "Energy Quantization")]),
  ]),
 ]),
 ("选必一", [
  (1, "Law of Conservation of Momentum", [
    (1, "Momentum", [("momentum", "Momentum")]),
    (2, "Impulse and the Momentum Theorem", [("impulse", "Impulse"), ("momentum_theorem", "Momentum Theorem")]),
    (3, "Law of Conservation of Momentum", [("momentum_conservation", "Law of Conservation of Momentum")]),
    (4, "Experiment: Verifying Conservation of Momentum", [("exp_momentum", "Experiment: Verifying Conservation of Momentum")]),
    (5, "Elastic and Inelastic Collisions", [("collision", "Elastic and Inelastic Collisions"), ("collision_analysis", "Analyzing Collision Problems")]),
    (6, "Recoil and Rockets", [("recoil", "Recoil and Rockets")]),
  ]),
  (2, "Mechanical Vibrations", [
    (1, "Simple Harmonic Motion", [("shm", "Simple Harmonic Motion")]),
    (2, "Describing Simple Harmonic Motion", [("shm_describe", "Describing Simple Harmonic Motion")]),
    (3, "Restoring Force and Energy in Simple Harmonic Motion", [("shm_force_energy", "Restoring Force and Energy in Simple Harmonic Motion")]),
    (4, "Simple Pendulum", [("pendulum", "Simple Pendulum")]),
    (5, "Experiment: Measuring Gravitational Acceleration with a Simple Pendulum", [("exp_pendulum", "Experiment: Measuring Gravitational Acceleration with a Simple Pendulum")]),
    (6, "Forced Vibration and Resonance", [("forced_resonance", "Forced Vibration and Resonance")]),
  ]),
  (3, "Mechanical Waves", [
    (1, "Wave Formation", [("wave_formation", "Wave Formation")]),
    (2, "Describing Waves", [("wave_params", "Wave Description"), ("wave_graph", "Wave and Oscillation Graphs")]),
    (3, "Reflection, Refraction, and Diffraction of Waves", [("wave_boundary", "Reflection, Refraction, and Diffraction of Waves")]),
    (4, "Wave Interference", [("wave_interference", "Wave Interference")]),
    (5, "Doppler Effect", [("doppler", "Doppler Effect")]),
  ]),
  (4, "Light", [
    (1, "Refraction of Light", [("refraction", "Refraction of Light"), ("exp_refraction", "Experiment: Measuring the Refractive Index of Glass")]),
    (2, "Total Internal Reflection", [("total_reflection", "Total Internal Reflection")]),
    (3, "Light Interference", [("light_interference", "Light Interference")]),
    (4, "Experiment: Measuring Light Wavelength with Double-Slit Interference", [("exp_double_slit", "Experiment: Measuring Light Wavelength with Double-Slit Interference")]),
    (5, "Diffraction of Light", [("diffraction", "Diffraction of Light")]),
    (6, "Polarization and Lasers", [("polarization", "Polarization of Light"), ("laser", "Lasers")]),
  ]),
 ]),
 ("选必二", [
  (1, "Ampère and Lorentz Forces", [
    (1, "Force of a Magnetic Field on a Current-Carrying Wire", [("ampere_force", "Ampère Force"), ("ampere_meter", "Moving-Coil Meters and Applications of Ampère Force")]),
    (2, "Force of a Magnetic Field on a Moving Charge", [("lorentz_force", "Lorentz Force")]),
    (3, "Charged Particles in a Uniform Magnetic Field", [("charge_circular", "Charged Particles in a Uniform Magnetic Field")]),
    (4, "Mass Spectrometers and Cyclotrons", [("mass_spectrometer", "Mass Spectrometers"), ("cyclotron", "Cyclotrons")]),
  ]),
  (2, "Electromagnetic Induction", [
    (1, "Lenz's Law", [("exp_lenz", "Experiment: Investigating Factors That Determine the Direction of Induced Current"), ("lenz", "Lenz's Law")]),
    (2, "Faraday's Law of Electromagnetic Induction", [("faraday", "Faraday's Law of Electromagnetic Induction"), ("emf_cutting", "Induced EMF in a Conductor Cutting Magnetic Field Lines"),
                          ("induction_dynamics", "Circuits, Energy, and Dynamics in Electromagnetic Induction")]),
    (3, "Eddy Currents, Electromagnetic Damping, and Electromagnetic Drive", [("eddy", "Eddy Currents, Electromagnetic Damping, and Electromagnetic Drive")]),
    (4, "Mutual and Self-Inductance", [("self_inductance", "Mutual and Self-Inductance")]),
  ]),
  (3, "Alternating Current", [
    (1, "Alternating Current", [("ac_generate", "Generation of Alternating Current")]),
    (2, "Describing Alternating Current", [("ac_describe", "Describing Alternating Current")]),
    (3, "Transformers", [("transformer", "Transformers"), ("exp_transformer", "Experiment: Investigating How Transformer Coil Voltages Depend on the Number of Turns")]),
    (4, "Electrical Power Transmission", [("power_transmission", "Electrical Power Transmission"), ("generator_motor", "Energy Conversion in Generators and Motors")]),
  ]),
  (4, "Electromagnetic Oscillations and Waves", [
    (1, "Electromagnetic Oscillations", [("lc_oscillation", "Electromagnetic Oscillations")]),
    (2, "Electromagnetic Fields and Waves", [("maxwell", "Electromagnetic Fields and Waves")]),
    (3, "Radio Transmission and Reception", [("radio", "Radio Transmission and Reception")]),
    (4, "Electromagnetic Spectrum", [("em_spectrum", "Electromagnetic Spectrum")]),
  ]),
  (5, "Sensors", [
    (1, "Introduction to Sensors", [("sensor_intro", "Introduction to Sensors")]),
    (2, "Operating Principles and Applications of Common Sensors", [("sensor_types", "Operating Principles and Applications of Common Sensors")]),
    (3, "Building a Simple Automatic Control Device with Sensors", [("exp_sensor", "Experiment: Building a Simple Automatic Control Device with Sensors")]),
  ]),
 ]),
 ("选必三", [
  (1, "Kinetic Theory of Molecules", [
    (1, "Fundamentals of Kinetic Theory of Molecules", [("molecular_basic", "Fundamentals of Kinetic Theory of Molecules"), ("brownian", "Brownian Motion and Diffusion")]),
    (2, "Experiment: Estimating the Size of Oleic Acid Molecules with the Oil-Film Method", [("exp_oil_film", "Experiment: Estimating the Size of Oleic Acid Molecules with the Oil-Film Method")]),
    (3, "Molecular Speed Distribution", [("speed_distribution", "Molecular Speed Distribution")]),
    (4, "Molecular Kinetic and Potential Energy", [("molecular_ke", "Molecular Kinetic Energy and Temperature"), ("molecular_pe", "Molecular Potential Energy and Internal Energy")]),
  ]),
  (2, "Gases, Solids, and Liquids", [
    (1, "Temperature and Temperature Scales", [("temperature", "Temperature and Temperature Scales")]),
    (2, "Isothermal Changes in Gases", [("exp_boyle", "Experiment: Investigating the Pressure–Volume Relationship of a Fixed Amount of Gas at Constant Temperature"), ("boyle", "Isothermal Changes in Gases")]),
    (3, "Isobaric and Isochoric Changes in Gases", [("charles", "Isobaric and Isochoric Changes in Gases"), ("ideal_gas", "Ideal Gas Law"),
                                ("gas_kinetic", "Microscopic Interpretation of Gas Pressure")]),
    (4, "Solids", [("solid", "Solids")]),
    (5, "Liquids", [("liquid", "Liquids")]),
  ]),
  (3, "Laws of Thermodynamics", [
    (1, "Changes in Internal Energy Through Work and Heat", [("work_heat", "Changes in Internal Energy Through Work and Heat")]),
    (2, "First Law of Thermodynamics", [("first_law", "First Law of Thermodynamics"), ("gas_thermo", "Applying the First Law to Changes in Gas States")]),
    (3, "Law of Conservation of Energy", [("energy_law", "Law of Conservation of Energy")]),
    (4, "Second Law of Thermodynamics", [("second_law", "Second Law of Thermodynamics")]),
  ]),
  (4, "Atomic Structure and Wave–Particle Duality", [
    (1, "Planck's Theory of Blackbody Radiation", [("blackbody", "Blackbody Radiation and Quanta")]),
    (2, "Photoelectric Effect", [("photoelectric", "Photoelectric Effect"), ("einstein_photo", "Einstein's Photoelectric Equation")]),
    (3, "Nuclear Model of the Atom", [("rutherford", "Nuclear Model of the Atom")]),
    (4, "Hydrogen Spectrum and Bohr's Atomic Model", [("hydrogen_spectrum", "Hydrogen Spectrum"), ("bohr", "Bohr's Atomic Model and Energy Levels")]),
    (5, "Wave Nature of Particles and the Development of Quantum Mechanics", [("wave_particle", "Wave Nature of Particles and Wave–Particle Duality")]),
  ]),
  (5, "Atomic Nuclei", [
    (1, "Composition of the Atomic Nucleus", [("radioactivity", "Natural Radioactivity and Radiation"), ("nucleus_comp", "Composition of the Atomic Nucleus")]),
    (2, "Radioactive Decay", [("decay", "Nuclear Decay"), ("half_life", "Half-Life"),
                         ("isotope_use", "Radioisotopes: Applications and Safety")]),
    (3, "Nuclear Forces and Binding Energy", [("binding_energy", "Nuclear Forces and Binding Energy")]),
    (4, "Nuclear Fission and Fusion", [("fission_fusion", "Nuclear Fission and Fusion")]),
    (5, "Elementary Particles", [("particles", "Elementary Particles and the Four Fundamental Interactions")]),
  ]),
 ]),
]

# Draft files (scripts/phy_hs_<name>.py) are responsible for these chapters: (volume, chapter number).
ASSIGN = {
    "a01": [("必修一", 1), ("必修一", 2), ("必修一", 3)],
    "a02": [("必修一", 4), ("必修二", 5), ("必修二", 6)],
    "a03": [("必修二", 7), ("必修二", 8), ("必修三", 9)],
    "a04": [("必修三", 10), ("必修三", 11)],
    "a05": [("必修三", 12), ("必修三", 13)],
    "a06": [("选必一", 1), ("选必一", 2)],
    "a07": [("选必一", 3), ("选必一", 4)],
    "a08": [("选必二", 1), ("选必二", 2)],
    "a09": [("选必二", 3), ("选必二", 4), ("选必二", 5), ("选必三", 1)],
    "a10": [("选必三", 2), ("选必三", 3)],
    "a11": [("选必三", 4), ("选必三", 5)],
}

PLAN = []          # Expanded in textbook order: dict(key, name, book, grade, vol, chapter_no, chapter_name, sec_no, sec_title, mod).
PLAN_BY_KEY = {}
for _book, _chapters in _RAW:
    for _chno, _chname, _secs in _chapters:
        # English chapter titles may contain internal spaces; reject leading or trailing whitespace.
        assert _chname == _chname.strip(), _chname
        for _secno, _sectitle, _topics in _secs:
            for _key, _name in _topics:
                assert _key not in PLAN_BY_KEY, _key
                _row = dict(key=_key, name=_name, book=_book, grade=BOOKS[_book]["grade"], mod=BOOKS[_book]["mod"],
                            chapter_no=_chno, chapter_name=_chname, sec_no=_secno, sec_title=_sectitle,
                            sec=(_book, "Chapter %s" % CN_NUM[_chno], _chname, "%d.%d" % (_chno, _secno)))
                PLAN.append(_row)
                PLAN_BY_KEY[_key] = _row
ORDER = {r["key"]: i for i, r in enumerate(PLAN)}


def keys_for(file_id):
    want = set(ASSIGN[file_id])
    return [r["key"] for r in PLAN if (r["book"], r["chapter_no"]) in want]


if __name__ == "__main__":
    import collections
    if "--keys" in __import__("sys").argv:
        for r in PLAN:
            print("%s | %s %s | %s" % (r["key"], r["sec"][0], r["sec"][3], r["name"]))
        raise SystemExit(0)
    print("Knowledge points: %d" % len(PLAN))
    c = collections.Counter(r["book"] for r in PLAN)
    print(dict(c))
    covered = collections.Counter(k for f in ASSIGN for k in keys_for(f))
    assert set(covered) == set(PLAN_BY_KEY) and all(v == 1 for v in covered.values())
    for f in ASSIGN:
        print(f, len(keys_for(f)))
