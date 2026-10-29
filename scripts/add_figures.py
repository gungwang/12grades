#!/usr/bin/env python3
"""Write inline SVGs to figure / choices[].figure in data/questions.json.

Only questions listed in the catalog below are updated. For shape choices
(hideChoiceText), choice names are not drawn in the SVG.
This script can be run repeatedly.  python3 scripts/add_figures.py
Preview:      python3 scripts/add_figures.py --preview /tmp/figprev.html
"""
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fig_draw as D

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUESTIONS = os.path.join(ROOT, "data", "questions.json")


def expect(cond, msg):
    if not cond:
        raise SystemExit("Figure does not match question: " + msg)


def intersect(p, d1, q, d2):
    det = d1[0] * d2[1] - d1[1] * d2[0]
    expect(abs(det) > 1e-8, "parallel lines do not intersect")
    rx, ry = q[0] - p[0], q[1] - p[1]
    t = (rx * d2[1] - ry * d2[0]) / det
    return (p[0] + t * d1[0], p[1] + t * d1[1]), t


def side(p, a, b):
    return (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])


def near(got, want, eps, msg):
    expect(abs(got - want) <= eps, "%s: got %.3f, expected %.3f" % (msg, got, want))


# ---------------------------------------------------------------- Scenes
def fig_parallel(which):
    """For which='add': ∠B=30°, ∠D=40°, E is on the same side of BD as A and C, and ∠BED=70°.
    For which='opp': the angles are 130° and 110°, E is on the other side, and ∠BED=120°."""
    if which == "add":
        B, Dp = (330, 52), (330, 268)
        A, C = (28, 52), (28, 268)
        dbe = (-math.cos(math.radians(30)), math.sin(math.radians(30)))
        dde = (-math.cos(math.radians(40)), -math.sin(math.radians(40)))
        eb, ed, bed = 30, 40, 70
        same = True
    else:
        B, Dp = (150, 36), (150, 268)
        A, C = (24, 36), (24, 268)
        dbe = (math.cos(math.radians(50)), math.sin(math.radians(50)))
        dde = (math.cos(math.radians(290)), math.sin(math.radians(290)))
        eb, ed, bed = 130, 110, 120
        same = False
    E, t1 = intersect(B, dbe, Dp, dde)
    _, t2 = intersect(Dp, dde, B, dbe)
    expect(t1 > 0 and t2 > 0, which + " intersection is not on the rays")
    near(D.angle_deg(A, B, E), eb, 0.4, which + " ∠ABE")
    near(D.angle_deg(C, Dp, E), ed, 0.4, which + " ∠CDE")
    near(D.angle_deg(B, E, Dp), bed, 0.5, which + " ∠BED")
    sA, sC, sE = side(A, B, Dp), side(C, B, Dp), side(E, B, Dp)
    expect(sA * sC > 0, which + " A and C should be on the same side of BD")
    expect((sA * sE > 0) == same, which + " E is on the wrong side for the prompt")
    e, th = D.edge(2.4), D.thin(1.6)
    body = [
        D.line(A, B, e), D.line(C, Dp, e), D.line(B, Dp, th),
        D.line(B, E, e), D.line(Dp, E, e),
        D.angle_arc(A, B, E, 30, "%s°" % eb, size=15),
        D.angle_arc(C, Dp, E, 30, "%s°" % ed, size=15),
        D.text(A[0] - 4, A[1] - 8, "A", 16, "end"),
        D.text(B[0] + 8, B[1] - 8, "B", 16, "start"),
        D.text(C[0] - 4, C[1] + 18, "C", 16, "end"),
        D.text(Dp[0] + 8, Dp[1] + 16, "D", 16, "start"),
        D.text(E[0], E[1] - 10, "E", 16),
    ]
    xs = [p[0] for p in (A, B, C, Dp, E)]
    ys = [p[1] for p in (A, B, C, Dp, E)]
    return D.svg(max(xs) + 36, max(ys) + 28, "".join(body))


def fig_right_labeled(leg_a, leg_b, hyp=None, ang_a=None):
    """The right angle is at C; vertical side CA=leg_a and horizontal side CB=leg_b. Label only the supplied values."""
    u = 14
    C = (48, 48 + max(leg_a, 6) * u)
    A = (C[0], C[1] - leg_a * u)
    B = (C[0] + leg_b * u, C[1])
    if hyp:
        near(math.hypot(B[0] - A[0], B[1] - A[1]), hyp * u, 0.6, "hypotenuse")
    if ang_a:
        near(D.angle_deg(C, A, B), ang_a, 0.4, "∠A")
    pts = [A, B, C]
    body = [D.poly(pts, D.face("0.1")), D.poly(pts, D.edge(2.5)), D.right_mark(C, A, B, 14)]
    body.append(D.text(C[0] - 14, C[1] + 6, "C", 16, "end"))
    body.append(D.text(A[0] - 14, A[1] + 4, "A", 16, "end"))
    body.append(D.text(B[0] + 8, B[1] + 6, "B", 16, "start"))
    if leg_a and not ang_a:
        body.append(D.text(A[0] - 16, (A[1] + C[1]) / 2, str(leg_a), 16, "end"))
    elif not ang_a:
        pass
    else:
        body.append(D.angle_arc(C, A, B, 26, "%s°" % ang_a, size=15))
    # Vertical-side label: for the 30° problem, omit the leg length because it is an answer or irrational.
    show_a = ang_a is None
    show_b = True
    if ang_a == 30:
        show_a = False
        show_b = False
        body.append(D.text((A[0] + B[0]) / 2, (A[1] + B[1]) / 2 - 8, str(hyp), 16))
    if show_a:
        body.append(D.text(C[0] - 18, (A[1] + C[1]) / 2, str(leg_a), 16, "end"))
    if show_b and ang_a != 30:
        body.append(D.text((C[0] + B[0]) / 2, C[1] + 22, str(leg_b), 16))
    if hyp and ang_a != 30:
        body.append(D.text((A[0] + B[0]) / 2 + 10, (A[1] + B[1]) / 2 - 6, str(hyp), 16))
    return D.svg(B[0] + 36, C[1] + 36, "".join(body))


def fig_tri_6_8():
    """The legs are 6 and 8; the hypotenuse is the unknown, so do not label it."""
    u = 16
    C = (46, 200)
    A = (46, 200 - 6 * u)
    B = (46 + 8 * u, 200)
    near(math.hypot(A[0] - B[0], A[1] - B[1]), 10 * u, 0.5, "6-8-10")
    body = [
        D.poly([A, B, C], D.face("0.1")), D.poly([A, B, C], D.edge(2.5)),
        D.right_mark(C, A, B, 14),
        D.text(A[0] - 16, (A[1] + C[1]) / 2, "6", 16, "end"),
        D.text((C[0] + B[0]) / 2, C[1] + 22, "8", 16),
        D.text(A[0] - 12, A[1] - 4, "A", 15, "end"),
        D.text(B[0] + 6, B[1] + 4, "B", 15, "start"),
        D.text(C[0] - 12, C[1] + 4, "C", 15, "end"),
    ]
    return D.svg(B[0] + 24, C[1] + 36, "".join(body))


def fig_tri_5_13():
    """The hypotenuse is 13 and one leg is 5; do not label the other leg."""
    u = 12
    C = (40, 210)
    B = (40 + 5 * u, 210)
    A = (40, 210 - 12 * u)
    near(math.hypot(A[0] - B[0], A[1] - B[1]), 13 * u, 0.5, "5-12-13")
    body = [
        D.poly([A, B, C], D.face("0.1")), D.poly([A, B, C], D.edge(2.5)),
        D.right_mark(C, A, B, 14),
        D.text((C[0] + B[0]) / 2, C[1] + 22, "5", 16),
        D.text((A[0] + B[0]) / 2 + 16, (A[1] + B[1]) / 2, "13", 16),
    ]
    return D.svg(B[0] + 36, C[1] + 36, "".join(body))


def fig_altitude():
    u = 16
    C = (48, 210)
    A = (48, 210 - 6 * u)
    B = (48 + 8 * u, 210)
    ab = (B[0] - A[0], B[1] - A[1])
    t = ((C[0] - A[0]) * ab[0] + (C[1] - A[1]) * ab[1]) / (ab[0] ** 2 + ab[1] ** 2)
    foot = (A[0] + t * ab[0], A[1] + t * ab[1])
    near(D.angle_deg(A, foot, C), 90, 0.4, "altitude is perpendicular")
    near(math.hypot(C[0] - foot[0], C[1] - foot[1]), 4.8 * u, 0.6, "altitude should be 4.8; position the figure accurately without labeling this value")
    body = [
        D.poly([A, B, C], D.face("0.1")), D.poly([A, B, C], D.edge(2.5)),
        D.line(C, foot, D.edge(2.2)),
        D.right_mark(C, A, B, 14),
        D.right_mark(foot, C, A, 12),
        D.text(A[0] - 8, (A[1] + C[1]) / 2, "6 cm", 15, "end"),
        D.text((C[0] + B[0]) / 2, C[1] + 22, "8 cm", 15),
        D.text((A[0] + B[0]) / 2 + 8, (A[1] + B[1]) / 2 - 10, "10 cm", 15),
        D.text(A[0] - 4, A[1] - 6, "A", 15, "end"),
        D.text(B[0] + 6, B[1] + 4, "B", 15, "start"),
        D.text(C[0] - 14, C[1], "C", 15, "end"),
        D.text(foot[0] + 10, foot[1] - 8, "D", 15, "start"),
    ]
    return D.svg(B[0] + 28, C[1] + 36, "".join(body))


def fig_dam():
    s = 9
    B = (28, 168)
    A = (B[0] + 6 * s, B[1] - 4 * s)
    Dp = (A[0] + 6 * s, A[1])
    C = (Dp[0] + 8 * s, Dp[1] + 4 * s)
    near(C[0] - B[0], 20 * s, 0.2, "dam base should be 20 m; do not label it in the figure")
    near(A[1] - B[1], -4 * s, 0.2, "dam height")
    body = [
        D.poly([A, B, C, Dp], D.face("0.12")), D.poly([A, B, C, Dp], D.edge(2.5)),
        D.line((A[0], A[1]), (A[0], B[1]), D.hidden(1.7)),
        D.line((Dp[0], Dp[1]), (Dp[0], B[1]), D.hidden(1.7)),
        D.text((A[0] + Dp[0]) / 2, A[1] - 10, "6 m", 16),
        D.text(A[0] - 8, (A[1] + B[1]) / 2, "4 m", 15, "end"),
        D.text((A[0] + B[0]) / 2 - 18, (A[1] + B[1]) / 2 + 6, "1 : 1.5", 15),
        D.text((Dp[0] + C[0]) / 2 + 16, (Dp[1] + C[1]) / 2, "1 : 2", 15, "start"),
        D.text(A[0], A[1] - 26, "A", 14),
        D.text(Dp[0], Dp[1] - 26, "D", 14),
        D.text(B[0], B[1] + 18, "B", 14),
        D.text(C[0], C[1] + 18, "C", 14),
    ]
    return D.svg(C[0] + 56, B[1] + 32, "".join(body))


def fig_fold_192():
    u = 34
    A = (36, 28)
    B = (36 + 5 * u, 28)
    C = (36 + 5 * u, 28 + 3 * u)
    Dp = (36, 28 + 3 * u)
    F = (Dp[0] + 4 * u, Dp[1])
    E = (C[0], C[1] - (4.0 / 9.0) * (C[1] - B[1]))
    mid = ((B[0] + F[0]) / 2, (B[1] + F[1]) / 2)
    ae = (E[0] - A[0], E[1] - A[1])
    am = (mid[0] - A[0], mid[1] - A[1])
    near(ae[0] * am[1] - ae[1] * am[0], 0, 0.8, "the fold line should be the perpendicular bisector of BF")
    bf = (F[0] - B[0], F[1] - B[1])
    near(ae[0] * bf[0] + ae[1] * bf[1], 0, 1.0, "fold line is perpendicular to BF")
    near(math.hypot(C[0] - F[0], C[1] - F[1]), u, 0.4, "position of CF=1")
    body = [
        D.poly([A, B, C, Dp], D.face("0.1")), D.poly([A, B, C, Dp], D.edge(2.5)),
        D.line(A, E, D.edge(2.3)),
        D.line(B, F, D.hidden(1.8)),
        D.circ(F[0], F[1], 3.2, 'fill="currentColor"'),
        D.text((A[0] + B[0]) / 2, A[1] - 10, "5", 16),
        D.text(A[0] - 12, (A[1] + Dp[1]) / 2, "3", 16, "end"),
        D.text(A[0] - 4, A[1] - 8, "A", 14, "end"),
        D.text(B[0] + 6, B[1] - 6, "B", 14, "start"),
        D.text(C[0] + 6, C[1] + 4, "C", 14, "start"),
        D.text(Dp[0] - 4, Dp[1] + 16, "D", 14, "end"),
        D.text(E[0] + 8, E[1], "E", 14, "start"),
        D.text(F[0], F[1] + 18, "F", 14),
    ]
    return D.svg(B[0] + 28, Dp[1] + 32, "".join(body))


def fig_fold_176():
    u = 15
    A = (36, 24)
    B = (36 + 8 * u, 24)
    C = (B[0], 24 + 10 * u)
    Dp = (A[0], C[1])
    F = (B[0], B[1] + 6 * u)
    E = (C[0] - 3 * u, C[1])
    mid = ((Dp[0] + F[0]) / 2, (Dp[1] + F[1]) / 2)
    ae = (E[0] - A[0], E[1] - A[1])
    am = (mid[0] - A[0], mid[1] - A[1])
    near(ae[0] * am[1] - ae[1] * am[0], 0, 0.8, "fold line passes through the midpoint of DF")
    df = (F[0] - Dp[0], F[1] - Dp[1])
    near(ae[0] * df[0] + ae[1] * df[1], 0, 1.2, "fold line is perpendicular to DF")
    near(math.hypot(C[0] - E[0], C[1] - E[1]), 3 * u, 0.3, "position of CE=3")
    body = [
        D.poly([A, B, C, Dp], D.face("0.1")), D.poly([A, B, C, Dp], D.edge(2.5)),
        D.line(A, E, D.edge(2.3)),
        D.line(Dp, F, D.hidden(1.8)),
        D.circ(F[0], F[1], 3.2, 'fill="currentColor"'),
        D.text((A[0] + B[0]) / 2, A[1] - 8, "8", 16),
        D.text(B[0] + 14, (B[1] + C[1]) / 2, "10", 16, "start"),
        D.text(A[0] - 6, A[1] + 4, "A", 14, "end"),
        D.text(B[0] + 6, B[1] - 4, "B", 14, "start"),
        D.text(C[0] + 6, C[1] + 16, "C", 14, "start"),
        D.text(Dp[0] - 6, Dp[1] + 16, "D", 14, "end"),
        D.text(E[0], E[1] + 18, "E", 14),
        D.text(F[0] - 14, F[1], "F", 14, "end"),
    ]
    return D.svg(B[0] + 36, C[1] + 32, "".join(body))


def fig_iso36():
    L = 210
    A = (170, 28)
    half = math.radians(18)
    B = (A[0] - L * math.sin(half), A[1] + L * math.cos(half))
    C = (A[0] + L * math.sin(half), A[1] + L * math.cos(half))
    near(D.angle_deg(B, A, C), 36, 0.3, "vertex angle 36°")
    near(D.angle_deg(A, B, C), 72, 0.4, "base angle 72°")
    uba = D.unit(A[0] - B[0], A[1] - B[1])
    ubc = D.unit(C[0] - B[0], C[1] - B[1])
    bis = (uba[0] + ubc[0], uba[1] + ubc[1])
    foot, t = intersect(B, bis, A, (C[0] - A[0], C[1] - A[1]))
    expect(t > 0, "angle bisector points in the wrong direction")
    near(D.angle_deg(A, B, foot), 36, 0.4, "first half after bisection")
    near(D.angle_deg(foot, B, C), 36, 0.4, "second half after bisection")
    body = [
        D.poly([A, B, C], D.face("0.1")), D.poly([A, B, C], D.edge(2.5)),
        D.line(B, foot, D.edge(2.2)),
        D.tick(A, B), D.tick(A, C),
        D.angle_arc(B, A, C, 34, "36°", size=15),
        D.text(A[0], A[1] - 8, "A", 15),
        D.text(B[0] - 4, B[1] + 16, "B", 15, "end"),
        D.text(C[0] + 4, C[1] + 16, "C", 15, "start"),
        D.text(foot[0] + 12, foot[1], "D", 15, "start"),
    ]
    return D.svg(C[0] + 24, B[1] + 28, "".join(body))


def fig_chord():
    sc = 18
    O = (160, 108)
    r, dist, half = 5 * sc, 3 * sc, 4 * sc
    A = (O[0] - half, O[1] + dist)
    B = (O[0] + half, O[1] + dist)
    near(math.hypot(A[0] - O[0], A[1] - O[1]), r, 0.3, "radius 5")
    near(math.hypot(B[0] - A[0], B[1] - A[1]), 8 * sc, 0.3, "chord 8")
    top = (O[0], O[1] - r)
    foot = (O[0], A[1])
    body = [
        D.circ(O[0], O[1], r, D.edge(2.5)),
        D.line(A, B, D.edge(2.5)),
        D.line(O, top, D.thin(1.7)),
        D.line(O, foot, D.hidden(1.7)),
        D.right_mark(foot, O, B, 12),
        D.circ(O[0], O[1], 2.6, 'fill="currentColor"'),
        D.text(O[0] + 10, (O[1] + top[1]) / 2, "5", 16, "start"),
        D.text(O[0], A[1] + 22, "8", 16),
        D.text(O[0] - 12, O[1] + 4, "O", 14, "end"),
        D.text(A[0] - 4, A[1] + 16, "A", 14, "end"),
        D.text(B[0] + 4, B[1] + 16, "B", 14, "start"),
    ]
    return D.svg(O[0] + r + 28, A[1] + 36, "".join(body))


def fig_coord_rect():
    ox, oy, s = 150, 170, 32

    def P(x, y):
        return (ox + x * s, oy - y * s)

    arrow, mid = D.defs_arrow()
    body = [arrow]
    for i in range(-2, 5):
        body.append(D.line(P(i, -2), P(i, 3), D.thin(1.0)))
    for j in range(-2, 4):
        body.append(D.line(P(-2, j), P(4, j), D.thin(1.0)))
    body.append('<line x1="%s" y1="%s" x2="%s" y2="%s" %s marker-end="url(#%s)"/>' % (
        D.n(P(-2, 0)[0]), D.n(P(-2, 0)[1]), D.n(P(4.3, 0)[0]), D.n(P(4.3, 0)[1]), D.thin(1.6), mid))
    body.append('<line x1="%s" y1="%s" x2="%s" y2="%s" %s marker-end="url(#%s)"/>' % (
        D.n(P(0, -2)[0]), D.n(P(0, -2)[1]), D.n(P(0, 3.3)[0]), D.n(P(0, 3.3)[1]), D.thin(1.6), mid))
    A, B, C, Dp = P(-1, -1), P(3, -1), P(3, 2), P(-1, 2)
    body.append(D.poly([A, B, C, Dp], D.face("0.12")))
    body.append(D.line(A, B, D.edge(2.4)))
    body.append(D.line(B, C, D.edge(2.4)))
    body.append(D.line(C, Dp, D.hidden(2.0)))
    body.append(D.line(Dp, A, D.hidden(2.0)))
    for pt, name, lab, anc in (
        (A, "A(−1,−1)", (0, 18), "middle"),
        (B, "B(3,−1)", (0, 18), "middle"),
        (C, "C(3,2)", (8, -8), "start"),
        (Dp, "D", (-8, -8), "end"),
    ):
        body.append(D.text(pt[0] + lab[0], pt[1] + lab[1], name, 14, anc))
    body.append(D.circ(Dp[0], Dp[1], 3.4, 'fill="currentColor"'))
    return D.svg(P(4.6, 0)[0] + 10, P(0, -2.4)[1] + 16, "".join(body))


def fig_point_line():
    A = (70, 36)
    Dp = (70, 150)
    B = (196, 150)
    near(math.hypot(A[0] - B[0], A[1] - B[1]), math.hypot(126, 114), 0.1, "AB")
    # The figure uses a 5:7 scale for 5 cm and 7 cm: AD:AB = 5:7.
    # The current pixel dimensions are not 5:7; make them exactly proportional.
    return _point_line()


def _point_line():
    sc = 16
    Dp = (80, 170)
    A = (80, 170 - 5 * sc)
    # B lies on the line, with AB=7.
    # (x-80)^2 + (5*sc)^2 = (7*sc)^2 => x-80 = sc*sqrt(49-25)=sc*sqrt(24)
    dx = sc * math.sqrt(24)
    B = (80 + dx, 170)
    near(math.hypot(A[0] - B[0], A[1] - B[1]), 7 * sc, 0.3, "AB=7")
    near(A[1] and abs(Dp[1] - A[1]), 5 * sc, 0.2, "AD=5")
    body = [
        D.line((24, 170), (240, 170), D.edge(2.4)),
        D.line(A, Dp, D.edge(2.3)),
        D.line(A, B, D.edge(2.3)),
        D.right_mark(Dp, A, B, 13),
        D.text(30, 158, "l", 16, "start"),
        D.text(A[0] - 16, (A[1] + Dp[1]) / 2, "5 cm", 15, "end"),
        D.text((A[0] + B[0]) / 2 + 6, (A[1] + B[1]) / 2 - 6, "7 cm", 15),
        D.text(A[0] - 12, A[1] - 4, "A", 14, "end"),
        D.text(Dp[0] - 8, Dp[1] + 18, "D", 14),
        D.text(B[0] + 6, B[1] + 4, "B", 14, "start"),
    ]
    return D.svg(B[0] + 28, 200, "".join(body))


def fig_vertical():
    O = (140, 100)
    a1, a2 = math.radians(28), math.radians(28 + 90)
    L = 92
    p = []
    for ang in (a1, a1 + math.pi, a2, a2 + math.pi):
        p.append((O[0] + L * math.cos(ang), O[1] + L * math.sin(ang)))
    body = [
        D.line(p[0], p[1], D.edge(2.5)), D.line(p[2], p[3], D.edge(2.5)),
        D.angle_arc(p[0], O, p[2], 28, "50°", size=15),
        D.angle_arc(p[1], O, p[3], 26, None),
        D.text(O[0] - 36, O[1] + 22, "∠1", 14),
    ]
    near(D.angle_deg(p[0], O, p[2]), 50, 0.2, "the angle between the rays should be 50°, not its adjacent angle")
    # Set the angle to 50°, not 90°; the earlier value of 90° was incorrect.
    return _vertical()


def _vertical():
    O = (150, 110)
    L = 96
    a = math.radians(32)
    b = a + math.radians(50)
    ends = []
    for ang in (a, a + math.pi, b, b + math.pi):
        ends.append((O[0] + L * math.cos(ang), O[1] + L * math.sin(ang)))
    near(D.angle_deg(ends[0], O, ends[2]), 50, 0.2, "∠1=50°")
    near(D.angle_deg(ends[1], O, ends[3]), 50, 0.2, "the vertical angle is also 50°, but do not label it")
    body = [
        D.line(ends[0], ends[1], D.edge(2.5)),
        D.line(ends[2], ends[3], D.edge(2.5)),
        D.angle_arc(ends[0], O, ends[2], 30, "50°", size=16),
        D.angle_arc(ends[1], O, ends[3], 28),
        D.text(O[0] + 8, O[1] + 46, "∠1", 14, "start"),
    ]
    return D.svg(O[0] + L + 20, O[1] + L + 20, "".join(body))


def fig_aob():
    O = (70, 130)
    A = (210, 36)
    B = (220, 150)
    body = [
        D.line(O, A, D.edge(2.6)), D.line(O, B, D.edge(2.6)),
        D.circ(O[0], O[1], 3.2, 'fill="currentColor"'),
        D.angle_arc(A, O, B, 28),
        D.text(O[0] - 8, O[1] + 22, "O", 18, "end"),
        D.text(A[0] + 4, A[1] - 4, "A", 18, "start"),
        D.text(B[0] + 4, B[1] + 6, "B", 18, "start"),
    ]
    return D.svg(250, 180, "".join(body))


def fig_alt_interior():
    # Two horizontal lines a and b; transversal c runs from upper left to lower right.
    a1, a2 = (30, 52), (300, 52)
    b1, b2 = (30, 168), (300, 168)
    c1, c2 = (70, 18), (250, 202)
    # Intersection points
    def hit(y):
        t = (y - c1[1]) / (c2[1] - c1[1])
        return (c1[0] + t * (c2[0] - c1[0]), y)
    E, F = hit(52), hit(168)
    body = [
        D.line(a1, a2, D.edge(2.4)), D.line(b1, b2, D.edge(2.4)), D.line(c1, c2, D.edge(2.4)),
        D.angle_arc((E[0] - 40, E[1]), E, (E[0] + 20, E[1] + 36), 22),
        D.angle_arc((F[0] + 40, F[1]), F, (F[0] - 20, F[1] - 36), 22),
        D.text(a2[0] + 8, a2[1] + 5, "a", 16, "start"),
        D.text(b2[0] + 8, b2[1] + 5, "b", 16, "start"),
        D.text(c1[0], c1[1] - 4, "c", 16),
    ]
    return D.svg(340, 220, "".join(body))


def fig_tangent():
    O = (120, 120)
    r = 72
    A = (O[0] + r, O[1])
    # The tangent is vertical.
    P = (A[0], A[1] - 78)
    body = [
        D.circ(O[0], O[1], r, D.edge(2.5)),
        D.line((A[0], A[1] + 36), (A[0], P[1] - 10), D.edge(2.5)),
        D.line(O, A, D.edge(2.3)),
        D.circ(O[0], O[1], 2.8, 'fill="currentColor"'),
        D.circ(A[0], A[1], 3, 'fill="currentColor"'),
        D.text(O[0] - 14, O[1] + 5, "O", 16, "end"),
        D.text(A[0] + 8, A[1] + 16, "A", 16, "start"),
        D.text(P[0] + 8, P[1], "P", 16, "start"),
    ]
    return D.svg(250, 200, "".join(body))


def fig_diagonals():
    A, B, C, Dp = (40, 40), (220, 40), (220, 130), (40, 130)
    body = [
        D.poly([A, B, C, Dp], D.face("0.1")), D.poly([A, B, C, Dp], D.edge(2.5)),
        D.line(A, C, D.edge(2.2)), D.line(B, Dp, D.edge(2.2)),
        D.text((A[0] + C[0]) / 2 + 12, (A[1] + C[1]) / 2, "10", 16, "start"),
    ]
    return D.svg(250, 160, "".join(body))


def fig_para_area():
    s = 22
    A = (36, 160)
    B = (36 + 7 * s, 160)
    Dp = (36 + 40, 160 - 4 * s)
    C = (B[0] + 40, Dp[1])
    foot = (Dp[0], A[1])
    body = [
        D.poly([A, B, C, Dp], D.face("0.12")), D.poly([A, B, C, Dp], D.edge(2.5)),
        D.line(Dp, foot, D.hidden(1.8)),
        D.right_mark(foot, Dp, B, 12),
        D.text((A[0] + B[0]) / 2, A[1] + 22, "7 cm", 16),
        D.text(Dp[0] - 8, (Dp[1] + foot[1]) / 2, "4 cm", 16, "end"),
    ]
    return D.svg(C[0] + 20, A[1] + 36, "".join(body))


def fig_tri_area():
    s = 18
    A = (30, 170)
    B = (30 + 8 * s, 170)
    C = (30 + 3 * s, 170 - 5 * s)
    foot = (C[0], A[1])
    body = [
        D.poly([A, B, C], D.face("0.12")), D.poly([A, B, C], D.edge(2.5)),
        D.line(C, foot, D.hidden(1.8)),
        D.right_mark(foot, C, B, 12),
        D.text((A[0] + B[0]) / 2, A[1] + 22, "8 cm", 16),
        D.text(C[0] + 10, (C[1] + foot[1]) / 2, "5 cm", 16, "start"),
    ]
    return D.svg(B[0] + 48, A[1] + 36, "".join(body))


def fig_trap_area():
    s = 26
    B = (24, 160)
    C = (24 + 6 * s, 160)
    overhang = 2 * s
    A = (B[0] + overhang, 160 - 4 * s)
    Dp = (A[0] + 2 * s, A[1])
    near(Dp[0] - A[0], 2 * s, 0.1, "top base 2")
    near(C[0] - B[0], 6 * s, 0.1, "bottom base 6")
    body = [
        D.poly([A, B, C, Dp], D.face("0.12")), D.poly([A, B, C, Dp], D.edge(2.5)),
        D.line((A[0], A[1]), (A[0], B[1]), D.hidden(1.7)),
        D.right_mark((A[0], B[1]), A, C, 11),
        D.text((A[0] + Dp[0]) / 2, A[1] - 8, "2 cm", 15),
        D.text((B[0] + C[0]) / 2, B[1] + 22, "6 cm", 15),
        D.text(A[0] - 8, (A[1] + B[1]) / 2, "4 cm", 15, "end"),
    ]
    return D.svg(C[0] + 16, B[1] + 36, "".join(body))


def fig_circle_radii():
    O = (120, 110)
    r = 72
    body = [D.circ(O[0], O[1], r, D.edge(2.6)), D.circ(O[0], O[1], 3, 'fill="currentColor"')]
    for ang in (math.radians(-80), math.radians(20), math.radians(140)):
        P = (O[0] + r * math.cos(ang), O[1] + r * math.sin(ang))
        body.append(D.line(O, P, D.thin(1.8)))
        body.append(D.tick(O, P, length=7))
    body.append(D.text(O[0] + 28, O[1] - 10, "r", 16, "start"))
    return D.svg(210, 200, "".join(body))


def fig_diameter():
    O = (120, 100)
    r = 70
    A = (O[0] - r, O[1])
    B = (O[0] + r, O[1])
    body = [
        D.circ(O[0], O[1], r, D.edge(2.6)),
        D.line(A, B, D.edge(2.4)),
        D.circ(O[0], O[1], 3, 'fill="currentColor"'),
        D.text(O[0], O[1] - 10, "10 cm", 16),
    ]
    return D.svg(220, 190, "".join(body))


def fig_angles(kind):
    """kind is either 'right-acute' or 'obtuse-right'."""
    def wedge(cx, cy, deg, label, right=False):
        r = 78
        a1 = math.radians(200)
        a2 = a1 + math.radians(deg)
        p1 = (cx + r * math.cos(a1), cy + r * math.sin(a1))
        p2 = (cx + r * math.cos(a2), cy + r * math.sin(a2))
        parts = [D.line((cx, cy), p1, D.edge(2.6)), D.line((cx, cy), p2, D.edge(2.6))]
        if right:
            parts.append(D.right_mark((cx, cy), p1, p2, 16))
        else:
            parts.append(D.angle_arc(p1, (cx, cy), p2, 26))
        parts.append(D.text(cx, cy + 28, label, 16))
        return "".join(parts)
    if kind == "ra":
        body = wedge(70, 70, 42, "Acute angle") + wedge(200, 70, 90, "Right angle", True)
    else:
        body = wedge(70, 78, 125, "Obtuse angle") + wedge(210, 78, 90, "Right angle", True)
    return D.svg(300, 180, body)


def fig_rect_marks():
    x, y, w, h = 40, 36, 180, 100
    A, B, C, Dp = (x, y), (x + w, y), (x + w, y + h), (x, y + h)
    body = [
        D._box(x, y, w, h, 2.6),
        D.tick(A, B, shift=-8), D.tick(Dp, C, shift=-8),
        D.tick(A, Dp, shift=-8), D.tick(A, Dp, shift=8),
        D.tick(B, C, shift=-8), D.tick(B, C, shift=8),
        D.right_mark(A, B, Dp, 14),
    ]
    return D.svg(250, 170, "".join(body))


def fig_sq_marks():
    x, y, s = 50, 24, 120
    A, B, C, Dp = (x, y), (x + s, y), (x + s, y + s), (x, y + s)
    body = [D._box(x, y, s, s, 2.6), D.right_mark(A, B, Dp, 14)]
    for a, b in ((A, B), (B, C), (C, Dp), (Dp, A)):
        body.append(D.tick(a, b))
    return D.svg(220, 170, "".join(body))


def _chevron(a, b):
    mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
    ux, uy = D.unit(b[0] - a[0], b[1] - a[1])
    px, py = -uy * 6, ux * 6
    tip = (mx + ux * 7, my + uy * 7)
    left = (mx - ux * 6 + px, my - uy * 6 + py)
    right = (mx - ux * 6 - px, my - uy * 6 - py)
    return D.poly([left, tip, right], 'fill="currentColor"')


def fig_para_marks():
    pts = [(70, 36), (210, 36), (170, 130), (30, 130)]
    body = [D.poly(pts, D.face("0.1")), D.poly(pts, D.edge(2.6))]
    body.append(_chevron(pts[0], pts[1]))
    body.append(_chevron(pts[3], pts[2]))
    # Mark the other pair of opposite sides with two offset arrow-like symbols.
    body.append(_chevron(pts[0], pts[3]))
    body.append(_chevron(pts[1], pts[2]))
    body.append(D.tick(pts[0], pts[1], shift=14))
    body.append(D.tick(pts[3], pts[2], shift=-14))
    return D.svg(240, 160, "".join(body))


def fig_trap_marks():
    pts = [(70, 40), (170, 40), (210, 136), (30, 136)]
    body = [D.poly(pts, D.face("0.1")), D.poly(pts, D.edge(2.6))]
    body.append(_chevron(pts[0], pts[1]))
    body.append(_chevron(pts[3], pts[2]))
    return D.svg(240, 160, "".join(body))


def fig_views_cuboid():
    body = [
        D.text(160, 22, "Front", 15), D._box(90, 30, 140, 78, 2.4),
        D.text(300, 22, "Side", 15), D._box(260, 30, 52, 78, 2.4),
        D.text(160, 132, "Top", 15), D._box(90, 140, 140, 40, 2.4),
    ]
    return D.svg(340, 196, "".join(body))


def fig_views_cone():
    body = [
        D.text(70, 20, "Front", 15),
        D.poly([(70, 36), (28, 130), (112, 130)], D.face("0.1")),
        D.poly([(70, 36), (28, 130), (112, 130)], D.edge(2.4)),
        D.text(190, 20, "Side", 15),
        D.poly([(190, 36), (148, 130), (232, 130)], D.face("0.1")),
        D.poly([(190, 36), (148, 130), (232, 130)], D.edge(2.4)),
        D.text(310, 20, "Top", 15),
        D.circ(310, 84, 40, D.face("0.1")),
        D.circ(310, 84, 40, D.edge(2.4)),
        D.circ(310, 84, 2.4, 'fill="currentColor"'),
    ]
    return D.svg(370, 160, "".join(body))


def fig_count_squares(n, label):
    s = 36
    body = [D.text(16, 22, label, 16, "start")]
    for i in range(n):
        body.append(D._box(16 + i * (s + 6), 32, s, s, 2.3))
    return D.svg(16 + n * (s + 6) + 10, 80, "".join(body))


def fig_front_side_counts():
    return D.svg(420, 90, fig_count_squares(5, "Front").split(">", 1)[1].rsplit("</svg>", 1)[0]
                 + _shift(fig_count_squares(3, "Side"), 230))


def _shift(svg, dx):
    """Translate the contents of an SVG segment using a group transform."""
    inner = svg.split(">", 1)[1].rsplit("</svg>", 1)[0]
    return '<g transform="translate(%s,0)">%s</g>' % (D.n(dx), inner)


def fig_spin_triangle():
    C = (78, 150)
    A = (78, 36)
    B = (168, 150)
    body = [
        D.poly([A, B, C], D.face("0.12")), D.poly([A, B, C], D.edge(2.6)),
        D.right_mark(C, A, B, 14),
        D.line((A[0], A[1] - 16), (C[0], C[1] + 16), D.hidden(1.6)),
        D.rotation_arrow(A[0], (A[1] + C[1]) / 2, 26),
    ]
    return D.svg(210, 190, "".join(body))


def fig_spin_rect():
    """Length 4 (axis of rotation, vertical side), width 3 (horizontal side)."""
    u = 32
    A = (70, 30)
    Dp = (70, 30 + 4 * u)
    C = (70 + 3 * u, 30 + 4 * u)
    B = (70 + 3 * u, 30)
    body = [
        D.poly([A, B, C, Dp], D.face("0.1")), D.poly([A, B, C, Dp], D.edge(2.6)),
        D.line((A[0], A[1] - 14), (Dp[0], Dp[1] + 14), D.hidden(1.6)),
        D.rotation_arrow(A[0], (A[1] + Dp[1]) / 2, 22),
        D.text(A[0] - 16, (A[1] + Dp[1]) / 2, "4 cm", 15, "end"),
        D.text((A[0] + B[0]) / 2, A[1] - 8, "3 cm", 15),
    ]
    return D.svg(B[0] + 24, Dp[1] + 28, "".join(body))


def fig_motion_triangle():
    return fig_spin_triangle()


def fig_motion_semi():
    O = (110, 120)
    r = 70
    body = [
        '<path d="M %s %s A %s %s 0 0 1 %s %s L %s %s Z" %s/>' % (
            D.n(O[0] - r), D.n(O[1]), D.n(r), D.n(r), D.n(O[0] + r), D.n(O[1]), D.n(O[0] - r), D.n(O[1]), D.face("0.12")),
        '<path d="M %s %s A %s %s 0 0 1 %s %s" %s/>' % (
            D.n(O[0] - r), D.n(O[1]), D.n(r), D.n(r), D.n(O[0] + r), D.n(O[1]), D.edge(2.6)),
        D.line((O[0] - r, O[1]), (O[0] + r, O[1]), D.edge(2.4)),
        D.rotation_arrow(O[0], O[1] - 8, 24),
    ]
    return D.svg(220, 160, "".join(body))


def fig_motion_slide():
    pts = [(36, 70), (150, 40), (170, 90), (56, 120)]
    arrow, mid = D.defs_arrow()
    body = [D.poly(pts, D.face("0.1")), D.poly(pts, D.edge(2.5)), arrow]
    body.append('<line x1="40" y1="140" x2="180" y2="140" stroke="currentColor" stroke-width="2" marker-end="url(#%s)"/>' % mid)
    return D.svg(220, 160, "".join(body))


def fig_motion_rect():
    body = [
        D._box(70, 36, 90, 70, 2.6),
        D.line((70, 20), (70, 124), D.hidden(1.6)),
        D.rotation_arrow(70, 71, 20),
    ]
    return D.svg(200, 150, "".join(body))


def fig_wiper():
    body = [
        D._box(30, 40, 170, 90, 2.4),
        '<path d="M 46 120 L 46 78 A 70 70 0 0 1 116 78" %s/>' % D.edge(2.4),
        D.line((46, 120), (116, 78), D.hidden(1.6)),
    ]
    return D.svg(220, 150, "".join(body))


def fig_meteor():
    body = [
        '<path d="M 30 110 Q 90 80 150 46" %s/>' % D.hidden(2.0),
        D.circ(156, 42, 5, 'fill="currentColor"'),
    ]
    return D.svg(220, 150, "".join(body))


def fig_pen():
    body = ['<path d="M 30 90 C 70 30, 120 130, 190 60" %s/>' % D.edge(2.6)]
    return D.svg(220, 150, "".join(body))


def fig_cyl_cone():
    rx, ry = 54, 16
    cx = 120
    apex_y, base_y, bot = 24, 100, 188
    e, hd = D.edge(2.5), D.hidden(2.2)
    body = [
        D._ell_arc(cx, bot, rx, ry, False, hd),
        D.line((cx - rx, base_y), (cx - rx, bot), e),
        D.line((cx + rx, base_y), (cx + rx, bot), e),
        D._ell_arc(cx, bot, rx, ry, True, e),
        D.line((cx, apex_y), (cx - rx, base_y), e),
        D.line((cx, apex_y), (cx + rx, base_y), e),
        D._ell_arc(cx, base_y, rx, ry, False, hd),
        D._ell_arc(cx, base_y, rx, ry, True, e),
        D.text(cx + rx + 12, (base_y + bot) / 2, "Cylinder", 15, "start"),
        D.text(cx + rx + 12, (apex_y + base_y) / 2, "Cone", 15, "start"),
    ]
    return D.svg(230, 220, "".join(body))


def fig_two_spheres(r1, r2, lab1, lab2):
    body = []
    x = 16
    for r, lab in ((r1, lab1), (r2, lab2)):
        cx, cy = x + r, r + 16
        body.append(D.circ(cx, cy, r, D.edge(2.4)))
        body.append(D._ell_arc(cx, cy, r * 0.94, r * 0.32, False, D.hidden(2.0)))
        body.append(D._ell_arc(cx, cy, r * 0.94, r * 0.32, True, D.edge(2.2)))
        body.append(D.text(cx, cy + r + 20, lab, 16))
        x += r * 2 + 28
    return D.svg(x, max(r1, r2) * 2 + 52, "".join(body))


def fig_cavity():
    body = [
        D.circ(110, 100, 72, D.edge(2.6)),
        D._ell_arc(110, 100, 68, 24, False, D.hidden(2.0)),
        D._ell_arc(110, 100, 68, 24, True, D.edge(2.2)),
        D.circ(146, 112, 26, D.hidden(2.2)),
        D.text(110, 190, "Small sphere inside large sphere", 15),
    ]
    return D.svg(210, 210, "".join(body))


def fig_cone_sector():
    """Place a sector next to the cone; label the shapes but do not state that they are equal."""
    body = [
        D.text(90, 20, "Cone", 15),
        D.text(280, 20, "Unfolded lateral surface", 15),
    ]
    # Small cone
    cx, apex_y, base_y, rx, ry = 90, 36, 150, 48, 14
    e, hd = D.edge(2.4), D.hidden(2.0)
    body += [
        D._ell_arc(cx, base_y, rx, ry, False, hd),
        D.line((cx, apex_y), (cx - rx, base_y), e),
        D.line((cx, apex_y), (cx + rx, base_y), e),
        D._ell_arc(cx, base_y, rx, ry, True, e),
        D.text(cx + 30, (apex_y + base_y) / 2, "Generatrix", 14, "start"),
    ]
    # Sector
    sx, sy, rad, half = 230, 120, 78, math.radians(55)
    p1 = (sx + rad * math.cos(-half), sy + rad * math.sin(-half))
    p2 = (sx + rad * math.cos(half), sy + rad * math.sin(half))
    body.append('<path d="M %s %s L %s %s A %s %s 0 0 1 %s %s Z" %s/>' % (
        D.n(sx), D.n(sy), D.n(p1[0]), D.n(p1[1]), D.n(rad), D.n(rad), D.n(p2[0]), D.n(p2[1]), D.face("0.1")))
    body.append('<path d="M %s %s L %s %s A %s %s 0 0 1 %s %s Z" %s/>' % (
        D.n(sx), D.n(sy), D.n(p1[0]), D.n(p1[1]), D.n(rad), D.n(rad), D.n(p2[0]), D.n(p2[1]), e))
    body.append(D.text((sx + p2[0]) / 2 + 8, (sy + p2[1]) / 2, "Radius", 14, "start"))
    body.append(D.text(sx + rad + 4, sy, "Arc", 14, "start"))
    return D.svg(400, 200, "".join(body))


def fig_net_rect():
    body = [
        D._box(30, 36, 200, 120, 2.5),
        D.text(130, 28, "6.28 cm", 15),
        D.text(246, 100, "5 cm", 15, "start"),
        D.text(130, 180, "Rectangle formed by unfolding the lateral surface", 15),
    ]
    return D.svg(310, 200, "".join(body))


def fig_pieces():
    body = [
        D.poly([(20, 30), (70, 110), (20, 110)], D.face("0.12")),
        D.poly([(20, 30), (70, 110), (20, 110)], D.edge(2.4)),
        D.poly([(90, 30), (140, 110), (90, 110)], D.face("0.12")),
        D.poly([(90, 30), (140, 110), (90, 110)], D.edge(2.4)),
        D._box(160, 40, 70, 70, 2.4),
    ]
    return D.svg(250, 130, "".join(body))


# ---------------------------------------------------------------- Catalog
S = {
    "Cuboid": D.shape_cuboid(),
    "Cube": D.shape_cube(),
    "Cylinder": D.shape_cylinder(),
    "Cone": D.shape_cone(),
    "Sphere": D.shape_sphere(),
    "Circle": D.shape_circle(),
    "Triangle": D.shape_triangle(),
    "Rectangle": D.shape_rect(),
    "Square": D.shape_square(ticks=True),
    "Trapezoid": D.shape_trapezoid(),
    "Sector": D.shape_sector_icon(),
    "Parallelogram": D.shape_parallelogram(),
    "Isosceles triangle": D.shape_iso_triangle(),
    "Right triangle": D.shape_right_triangle(),
    "Arbitrary trapezoid": D.shape_trapezoid(False),
    "Rectangular figure": D.shape_rect(),
    "Two circles": D.shape_two_circles(),
}


def choices_named(keys_names):
    return {k: S[name] for k, name in keys_names}


def fig_four_rays():
    """Four rays are arranged in order, with ∠AOD less than a straight angle. Do not label the number of angles."""
    O = (168, 196)
    angs = [-152, -114, -70, -26]
    labs = "ABCD"
    ends = []
    body = []
    label_pts = []
    for ang, lab in zip(angs, labs):
        rad = math.radians(ang)
        p = (O[0] + 108 * math.cos(rad), O[1] + 108 * math.sin(rad))
        lp = (O[0] + 128 * math.cos(rad), O[1] + 128 * math.sin(rad) + 5)
        ends.append(p)
        label_pts.append(lp)
        body.append(D.line(O, p, D.edge(2.4)))
        body.append(D.text(lp[0], lp[1], lab, 16))
    span = (angs[-1] - angs[0]) % 360
    expect(span < 180, "the angle spanned by the four rays should be less than a straight angle")
    for ang in angs[1:-1]:
        inside = (ang - angs[0]) % 360
        expect(inside < span, "an interior ray does not lie between OA and OD")
    near(D.angle_deg(ends[0], O, ends[3]), span, 0.6, "∠AOD")
    body.append(D.circ(O[0], O[1], 3.2, 'fill="currentColor"'))
    body.append(D.text(O[0] + 2, O[1] + 22, "O", 16, "start"))
    xs = [p[0] for p in ends + label_pts] + [O[0]]
    ys = [p[1] for p in ends + label_pts] + [O[1] + 22]
    expect(min(xs) > 16 and min(ys) > 12, "a ray or label extends outside the canvas")
    return D.svg(max(xs) + 24, max(ys) + 16, "".join(body))


def fig_three_lines():
    """Three lines intersect at one point. Do not label the number of pairs of vertical angles."""
    O = (150, 110)
    dirs = [18, 78, 138]
    for i in range(3):
        for j in range(i + 1, 3):
            expect(abs(dirs[i] - dirs[j]) % 180 > 8, "two lines coincide")
    body = []
    L = 96
    for deg in dirs:
        rad = math.radians(deg)
        d = (math.cos(rad), math.sin(rad))
        body.append(D.line((O[0] - L * d[0], O[1] - L * d[1]), (O[0] + L * d[0], O[1] + L * d[1]), D.edge(2.4)))
    body.append(D.circ(O[0], O[1], 3.2, 'fill="currentColor"'))
    body.append(D.text(O[0] + 16, O[1] + 28, "O", 16, "start"))
    return D.svg(270, 230, "".join(body))


def fig_similar():
    """D and E divide AB and AC in the same ratio, so DE∥BC. Do not state similarity."""
    A = (180, 28)
    B = (36, 210)
    C = (324, 210)
    t = 0.46
    Dp = (A[0] + t * (B[0] - A[0]), A[1] + t * (B[1] - A[1]))
    E = (A[0] + t * (C[0] - A[0]), A[1] + t * (C[1] - A[1]))
    de = (E[0] - Dp[0], E[1] - Dp[1])
    bc = (C[0] - B[0], C[1] - B[1])
    near(de[0] * bc[1] - de[1] * bc[0], 0, 0.6, "DE should be parallel to BC")
    body = [
        D.poly([A, B, C], D.face("0.08")),
        D.poly([A, Dp, E], D.face("0.14")),
        D.poly([A, B, C], D.edge(2.4)),
        D.line(Dp, E, D.edge(2.4)),
        _chevron(Dp, E), _chevron(B, C),
        D.text(A[0], A[1] - 8, "A", 15),
        D.text(B[0] - 4, B[1] + 16, "B", 15, "end"),
        D.text(C[0] + 4, C[1] + 16, "C", 15, "start"),
        D.text(Dp[0] - 14, Dp[1], "D", 15, "end"),
        D.text(E[0] + 8, E[1], "E", 15, "start"),
    ]
    return D.svg(360, 240, "".join(body))


def fig_zhao(legs):
    """The large square's side is the hypotenuse. Four right triangles surround the small inner square.
    If legs is None, label a, b, and c; for (3, 4), label only 3 and 4, not the hypotenuse."""
    if legs:
        a, b = float(legs[0]), float(legs[1])
        lab_a, lab_b, lab_c = str(legs[0]), str(legs[1]), None
    else:
        a, b = 3.0, 4.0
        lab_a, lab_b, lab_c = "a", "b", "c"
    expect(b > a, "draw the chord diagram with b>a")
    c = math.hypot(a, b)
    u = 26
    S = c * u
    ox, oy = 46, 36
    sides = [
        ((ox, oy), (ox + S, oy), (0, 1)),
        ((ox + S, oy), (ox + S, oy + S), (-1, 0)),
        ((ox + S, oy + S), (ox, oy + S), (0, -1)),
        ((ox, oy + S), (ox, oy), (1, 0)),
    ]
    verts = []
    tris = []
    for p0, p1, inn in sides:
        dx, dy = (p1[0] - p0[0]) / S, (p1[1] - p0[1]) / S
        along = b * b * u / c
        height = a * b * u / c
        v = (p0[0] + dx * along + inn[0] * height, p0[1] + dy * along + inn[1] * height)
        near(math.hypot(v[0] - p0[0], v[1] - p0[1]), b * u, 0.4, "longer leg")
        near(math.hypot(v[0] - p1[0], v[1] - p1[1]), a * u, 0.4, "shorter leg")
        verts.append(v)
        tris.append((p0, p1, v))
    for i in range(4):
        p, q = verts[i], verts[(i + 1) % 4]
        near(math.hypot(q[0] - p[0], q[1] - p[1]), abs(b - a) * u, 0.5, "side length of the small square")
    body = []
    for p0, p1, v in tris:
        body.append(D.poly([p0, p1, v], D.face("0.12")))
        body.append(D.poly([p0, p1, v], D.edge(2.2)))
    body.append(D.poly(verts, D.edge(2.4)))
    # Label the legs on only the upper-left triangle instead of repeating them in all four corners.
    p0, p1, v = tris[0]
    body.append(D.text((p0[0] + v[0]) / 2 - 8, (p0[1] + v[1]) / 2, lab_b, 15, "end"))
    body.append(D.text((p1[0] + v[0]) / 2 + 6, (p1[1] + v[1]) / 2 - 4, lab_a, 15, "start"))
    body.append(D.right_mark(v, p0, p1, 12))
    if lab_c:
        body.append(D.text(ox + S / 2, oy + S + 20, lab_c, 16))
    return D.svg(ox + S + 36, oy + S + (40 if lab_c else 24), "".join(body))


def fig_fold_25():
    """Rectangle with ∠BAE=25° and E on BC. F is the reflection of B across fold AE. Do not label ∠BEF."""
    u = 22
    A = (48, 40)
    B = (48 + 8 * u, 40)
    C = (B[0], 40 + 6 * u)
    Dp = (48, C[1])
    ang = math.radians(25)
    direction = (math.cos(ang), math.sin(ang))
    # Intersect with right side BC (x = B.x).
    t = (B[0] - A[0]) / direction[0]
    E = (A[0] + t * direction[0], A[1] + t * direction[1])
    expect(B[1] < E[1] < C[1], "E should lie on side BC")
    near(D.angle_deg(B, A, E), 25, 0.3, "∠BAE")

    def reflect(P, p, q):
        dx, dy = q[0] - p[0], q[1] - p[1]
        L2 = dx * dx + dy * dy
        k = ((P[0] - p[0]) * dx + (P[1] - p[1]) * dy) / L2
        return (2 * (p[0] + k * dx) - P[0], 2 * (p[1] + k * dy) - P[1])

    F = reflect(B, A, E)
    near(D.angle_deg(B, E, F), 130, 0.6, "∠BEF should be 130°, but do not label it")
    body = [
        D.poly([A, B, C, Dp], D.face("0.08")),
        D.poly([A, B, C, Dp], D.edge(2.4)),
        D.line(A, E, D.edge(2.3)),
        D.line(B, F, D.hidden(1.8)),
        D.line(E, F, D.edge(2.2)),
        D.circ(F[0], F[1], 3.2, 'fill="currentColor"'),
        D.angle_arc(B, A, E, 32, "25°", size=15),
        D.text(A[0] - 4, A[1] - 6, "A", 15, "end"),
        D.text(B[0] + 6, B[1] - 4, "B", 15, "start"),
        D.text(C[0] + 6, C[1] + 16, "C", 15, "start"),
        D.text(Dp[0] - 6, Dp[1] + 16, "D", 15, "end"),
        D.text(E[0] + 8, E[1], "E", 15, "start"),
        D.text(F[0] + 8, F[1] + 4, "F", 15, "start"),
    ]
    xs = [p[0] for p in (A, B, C, Dp, E, F)]
    ys = [p[1] for p in (A, B, C, Dp, E, F)]
    return D.svg(max(xs) + 28, max(ys) + 28, "".join(body))


def fig_same_side():
    """A and B lie on the same side of a line, at distances 3 and 6; their feet are 12 apart. Do not draw the reflection or label the minimum."""
    u = 14
    y = 168
    foot_a = (48, y)
    foot_b = (48 + 12 * u, y)
    A = (foot_a[0], y - 3 * u)
    B = (foot_b[0], y - 6 * u)
    near(math.hypot(foot_b[0] - foot_a[0], 0), 12 * u, 0.2, "distance between feet is 12")
    near(abs(A[1] - y), 3 * u, 0.2, "distance from A to the line is 3")
    near(abs(B[1] - y), 6 * u, 0.2, "distance from B to the line is 6")
    expect(side(A, foot_a, foot_b) * side(B, foot_a, foot_b) > 0, "A and B should be on the same side")
    body = [
        D.line((20, y), (foot_b[0] + 36, y), D.edge(2.4)),
        D.line(A, foot_a, D.edge(2.2)),
        D.line(B, foot_b, D.edge(2.2)),
        D.right_mark(foot_a, A, (foot_a[0] + 20, y), 12),
        D.right_mark(foot_b, B, (foot_b[0] + 20, y), 12),
        D.text(28, y - 8, "l", 16, "start"),
        D.text(A[0] - 8, (A[1] + y) / 2, "3", 15, "end"),
        D.text(B[0] + 8, (B[1] + y) / 2, "6", 15, "start"),
        D.text((foot_a[0] + foot_b[0]) / 2, y + 22, "12", 15),
        D.text(A[0], A[1] - 8, "A", 15),
        D.text(B[0], B[1] - 8, "B", 15),
    ]
    return D.svg(foot_b[0] + 48, y + 40, "".join(body))


def fig_equal_bases():
    """A cylinder and cone have the same base area and height. Label only the cylinder's volume, 30; do not label the cone's volume."""
    rx, ry, h = 46, 14, 96
    top, bot = 36, 36 + h
    e, hd = D.edge(2.4), D.hidden(2.1)

    def cyl(cx):
        return [
            D._ell_arc(cx, bot, rx, ry, False, hd),
            D.line((cx - rx, top), (cx - rx, bot), e),
            D.line((cx + rx, top), (cx + rx, bot), e),
            D._ell_arc(cx, bot, rx, ry, True, e),
            '<ellipse cx="%s" cy="%s" rx="%s" ry="%s" %s/>' % (D.n(cx), D.n(top), D.n(rx), D.n(ry), D.face("0.16")),
            '<ellipse cx="%s" cy="%s" rx="%s" ry="%s" %s/>' % (D.n(cx), D.n(top), D.n(rx), D.n(ry), e),
        ]

    def con(cx):
        apex = (cx, top)
        return [
            D._ell_arc(cx, bot, rx, ry, False, hd),
            D.line(apex, (cx - rx, bot), e),
            D.line(apex, (cx + rx, bot), e),
            D._ell_arc(cx, bot, rx, ry, True, e),
        ]

    body = [D.text(185, 20, "Same base area and height", 16)]
    body += cyl(90) + con(280)
    cap = bot + ry + 22
    body.append(D.text(90, cap, "Cylinder", 15))
    body.append(D.text(90, cap + 20, "Volume 30 cm³", 14))
    body.append(D.text(280, cap, "Cone", 15))
    return D.svg(400, cap + 36, "".join(body))


CATALOG = []


def add(cat, qid, figure=None, choices=None, hide=False):
    CATALOG.append({"cat": cat, "id": qid, "figure": figure, "choices": choices, "hide": hide})


def build():
    CATALOG.clear()
    G = "Shape options"
    # Grade 1: “Which one is ...?” Show only the shapes.
    add(G, "cnm_p014_q1", choices=choices_named([("A", "Cuboid"), ("B", "Sphere"), ("C", "Cylinder")]), hide=True)
    add(G, "cnm_p014_q2", choices=choices_named([("A", "Sphere"), ("B", "Cylinder"), ("C", "Cuboid")]), hide=True)
    add(G, "cnm_p014_q3", choices=choices_named([("A", "Sphere"), ("B", "Cuboid"), ("C", "Cube")]), hide=True)
    add(G, "cnm_p014_q4", choices=choices_named([("A", "Cylinder"), ("B", "Sphere"), ("C", "Cuboid")]), hide=True)
    add(G, "cnm_p023_q1", choices=choices_named([("A", "Triangle"), ("B", "Circle"), ("C", "Rectangle")]), hide=True)
    add(G, "cnm_p023_q2", choices=choices_named([("A", "Rectangle"), ("B", "Square"), ("C", "Triangle")]), hide=True)
    add("Plane figures", "cnm_p023_q3", figure=D.shape_rect())
    add("Plane figures", "cnm_p023_q4", figure=fig_sq_marks())
    add("Plane figures", "cnm_p024_q3", figure=fig_pieces())
    add("Plane figures", "cnm_p077_q1", figure=fig_rect_marks())
    add("Plane figures", "cnm_p077_q2", figure=fig_sq_marks())
    add("Plane figures", "cnm_p101_q1", figure=fig_angles("ra"))
    add("Plane figures", "cnm_p101_q2", figure=fig_angles("ob"))
    add("Plane figures", "cnm_p105_q1", figure=fig_para_marks())
    add("Plane figures", "cnm_p105_q2", figure=fig_trap_marks())

    V = "Views from Different Directions"
    add(V, "cnm_p113_q1", figure=fig_views_cuboid())
    add(V, "cnm_p113_q3", figure=_join_counts())
    add(V, "cnm_p152_q1", figure=fig_views_cone())
    add(V, "cnm_p152_q3", figure=D.cubes([(x, y, z) for x in (0, 1) for y in (0, 1) for z in (0, 1)], s=28))

    SO = "Cuboids and Cubes"
    add(SO, "cnm_p160_q1", figure=D.cuboid(120, 78, 70, margin=26))
    add(SO, "cnm_p160_q2", figure=D.cuboid(84, 84, 84, ticks=True, margin=26))
    add(SO, "cnm_p161_q3", figure=D.cuboid(100, 100, 100, lab_l="2 cm", ticks=True, margin=30))
    add(SO, "cnm_p163_q1", figure=D.cuboid(150, 90, 120, lab_l="5 cm", lab_h="3 cm", lab_d="4 cm"))
    add(SO, "cnm_p163_q2", figure=D.cuboid(110, 110, 110, lab_l="3 cm", ticks=True, margin=30))
    add(SO, "cnm_p163_q3", figure=D.cuboid(168, 42, 105, lab_l="8 cm", lab_h="2 cm", lab_d="5 cm"))

    CY = "Cylinders, Cones, and Spheres"
    add(CY, "cnm_p206_q1", figure=D.cylinder(rx=70, ry=20, h=100, show_radius=False))
    add(CY, "cnm_p206_q3", figure=D.cylinder(rx=28, ry=12, h=140, r_label="r = 2 cm", h_label="h = 10 cm", show_radius=True))
    add(CY, "cnm_p207_q1", figure=D.cylinder(rx=48, ry=16, h=120, r_label="r = 2 cm", h_label="h = 5 cm", show_radius=True))
    add(CY, "cnm_p207_q2", figure=D.cylinder(rx=18, ry=9, h=180, r_label="r = 1 cm", h_label="h = 10 cm", show_radius=True))
    add(CY, "cnm_p207_q3", figure=D.cylinder(rx=64, ry=18, h=90, h_label="h = 4 cm", base_label="Base area 12 cm²"))
    add(CY, "cnm_p208_q3", figure=fig_net_rect())
    add(CY, "cnm_p209_q1", figure=D.cone(rx=68, ry=18, h=110))
    add(CY, "cnm_p209_q3", figure=fig_equal_bases())

    add("Plane figures", "cnm_p147_q1", figure=fig_para_area())
    add("Plane figures", "cnm_p148_q1", figure=fig_tri_area())
    add("Plane figures", "cnm_p149_q1", figure=fig_trap_area())
    add("Plane figures", "cnm_p188_q1", figure=fig_circle_radii())
    add("Plane figures", "cnm_p188_q3", figure=fig_diameter())
    add("Plane figures", "cnm_p193_q3", figure=D.sector(180, 100, ang_label="180°"))

    N = "Nets and Orthographic Views"
    add(N, "cnm_050_q1", figure=D.cylinder(rx=58, ry=16, h=100),
        choices=choices_named([("A", "Triangle"), ("B", "Circle"), ("C", "Rectangle"), ("D", "Sector")]), hide=True)
    add(G, "cnm_050_q2", choices=choices_named([("A", "Sphere"), ("B", "Circle"), ("C", "Triangle"), ("D", "Trapezoid")]), hide=True)
    add(N, "cnm_050_q3", figure=D.prism(6))
    add(N, "cnm_050_q4", figure=D.prism(7, rx=64, ry=42, height=100))
    add(N, "cnm_051_q1", figure=D.net([(1, 0), (0, 1), (1, 1), (2, 1), (3, 1), (1, 2)]))
    add(N, "cnm_051_q2", figure=D.cylinder(rx=60, ry=18, h=110))
    add(N, "cnm_051_q3", figure=D.cubes([(0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 0), (0, 0, 1)]))
    add(N, "cnm_051_q4", choices={
        "A": D.net([(0, 0), (1, 0), (2, 0), (3, 0), (0, 1), (1, 1)], size=36),
        "B": D.net([(0, 0), (1, 0), (2, 0), (2, 1), (3, 1), (4, 1)], size=32),
        "C": D.net([(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (3, 2)], size=34),
        "D": D.net([(1, 0), (0, 1), (1, 1), (2, 1), (3, 1), (1, 2)], size=34),
    })
    add(N, "cnm_051_q5", figure=D.net(
        [(1, 0), (0, 1), (1, 1), (2, 1), (3, 1), (3, 2)],
        {(1, 0): "5", (0, 1): "1", (1, 1): "2", (2, 1): "3", (3, 1): "4", (3, 2): "6"}))
    add(N, "cnm_052_q1", figure=fig_spin_triangle())
    add(N, "cnm_052_q3", figure=D.cuboid(130, 80, 70))
    add(N, "cnm_052_q4", choices={
        "A": fig_motion_triangle(), "B": fig_wiper(), "C": fig_meteor(), "D": fig_pen(),
    })
    add(N, "cnm_052_q5", figure=fig_spin_rect())
    add(CY, "cnm_258_q1", figure=D.cone(rx=54, ry=16, h=72, r_label="r = 3", l_label="l = 5"))
    add(CY, "cnm_258_q2", figure=fig_cone_sector())
    add(CY, "cnm_258_q3", figure=D.cone(rx=54, ry=16, h=72, r_label="r = 3", l_label="l = 5"))
    add(CY, "cnm_258_q4", figure=D.cone(rx=50, ry=16, h=120, r_label="r = 5", h_label="h = 12"))
    add(CY, "cnm_258_q5", figure=D.sector(120, 120, r_label="6", ang_label="120°"))
    add(N, "cnm_283_q1", figure=D.cylinder(rx=62, ry=18, h=110))
    add(G, "cnm_283_q2", choices=choices_named([("A", "Cylinder"), ("B", "Cone"), ("C", "Sphere"), ("D", "Cube")]), hide=True)
    add(N, "cnm_283_q3", figure=D.top_grid([[2, 1], [1, 3]], "Top view (numbers inside the cells)"))
    add(N, "cnm_283_q4", figure=D.cone(rx=64, ry=18, h=120))
    add(N, "cnm_283_q5", figure=D.two_views_rect(5, 3, 2, 3))
    add(N, "cnm_291_q4", figure=D.three_views_cylinder())

    P = "Plane Geometry"
    add(P, "cnm_056_q1", figure=fig_aob())
    add(P, "cnm_056_q4", figure=fig_four_rays())
    add(P, "cnm_063_q1", figure=_vertical())
    add(P, "cnm_063_q5", figure=fig_three_lines())
    add(P, "cnm_065_q2", figure=_point_line())
    add(P, "cnm_066_q1", figure=fig_alt_interior())
    add(P, "cnm_070_q1", figure=fig_parallel("add"))
    add(P, "cnm_070_q3", figure=fig_parallel("opp"))
    add(P, "cnm_084_q4", figure=fig_coord_rect())
    add(P, "cnm_141_q4", figure=fig_same_side())
    add(P, "cnm_112_q4", figure=fig_altitude())
    add(G, "cnm_131_q2", choices=choices_named([
        ("A", "Parallelogram"), ("B", "Isosceles triangle"), ("C", "Right triangle"), ("D", "Arbitrary trapezoid")]), hide=True)
    add(P, "cnm_137_q1", figure=fig_iso36())  # The vertex angle is 40°, not 36°; add a separate figure below.
    add(P, "cnm_138_q5", figure=fig_iso36())
    add(P, "cnm_140_q1", figure=fig_right_labeled(5 * math.sqrt(3), 5, hyp=10, ang_a=30))
    add(P, "cnm_174_q1", figure=fig_tri_6_8())
    add(P, "cnm_175_q1", figure=fig_zhao(None))
    add(P, "cnm_175_q2", figure=fig_zhao((3, 4)))
    add(P, "cnm_174_q2", figure=fig_tri_5_13())
    add(P, "cnm_176_q4", figure=fig_fold_176())
    add(P, "cnm_186_q1", figure=fig_diagonals())
    add(P, "cnm_192_q1", figure=fig_fold_192())
    add(P, "cnm_192_q2", figure=fig_fold_25())
    add(P, "cnm_273_q1", figure=fig_similar())
    add(P, "cnm_251_q1", figure=fig_chord())
    add(P, "cnm_262_q1", figure=fig_tangent())
    add(P, "cnm_280_q5", figure=fig_dam())

    H = "High-School Solid Geometry"
    add(H, "cnm_h105_q1", figure=D.cuboid(120, 76, 68))
    add(H, "cnm_h105_q2", figure=D.cuboid(120, 76, 68))
    add(H, "cnm_h105_q3", figure=D.prism(3, rx=70, ry=32, height=100))
    add(H, "cnm_h105_q4", figure=D.prism(5, rx=66, ry=42, height=96))
    add(H, "cnm_h106_q2", figure=D.cylinder(rx=62, ry=18, h=108))
    add(H, "cnm_h106_q1", choices={
        "A": fig_motion_triangle(), "B": fig_motion_semi(), "C": fig_motion_slide(), "D": fig_motion_rect(),
    })
    add(H, "cnm_h106_q3", figure=D.sphere(r=70, r_label="r", extra_radii=2))
    add(H, "cnm_h106_q4", figure=D.cone(rx=66, ry=18, h=118, l_label="Generatrix"))
    add(H, "cnm_h107_q1", figure=fig_cyl_cone())
    add(H, "cnm_h107_q4", figure=fig_cavity())
    add(H, "cnm_h110_q1", figure=D.cuboid(100, 100, 100, lab_l="3", ticks=True, margin=28))
    add(H, "cnm_h110_q2", figure=D.cuboid(70, 140, 105, lab_l="2", lab_h="4", lab_d="3"))
    add(H, "cnm_h110_q3", figure=D.cylinder(rx=42, ry=14, h=106, h_label="Height 4", base_label="Base circumference 10"))
    add(G, "cnm_h110_q4", choices=choices_named([("A", "Rectangular figure"), ("B", "Two circles"), ("C", "Sector"), ("D", "Triangle")]), hide=True)
    add(H, "cnm_h111_q1", figure=D.cuboid(130, 80, 90, lab_h="Height 4", foot="Base area 20"))
    add(H, "cnm_h111_q2", figure=D.cylinder(rx=58, ry=16, h=96, h_label="Height 6", base_label="Base area 10"))
    add(H, "cnm_h111_q3", figure=D.cone(rx=60, ry=16, h=100, h_label="Height 3", base_label="Base area 9"))
    add(H, "cnm_h111_q4", figure=fig_cyl_cone())
    add(H, "cnm_h112_q1", figure=fig_two_spheres(28, 56, "r", "2r"))
    add(H, "cnm_h112_q2", figure=fig_two_spheres(24, 72, "r", "3r"))
    add(H, "cnm_h112_q3", figure=fig_two_spheres(32, 64, "r = 1", "r = 2"))
    add(H, "cnm_h113_q3", figure=D.cuboid(120, 80, 68, letters=True, mid=("A", "B")))
    add(H, "cnm_h114_q2", figure=D.cuboid(130, 80, 72, letters=True, bold=[("A", "B", False), ("C", "G", False)]))
    add(H, "cnm_h119_q2", figure=D.cuboid(130, 84, 70, letters=True, bold=[("A", "B", False), ("D", "C", False)]))
    add(H, "cnm_h120_q4", figure=D.cuboid(120, 84, 70, letters=True, bold=[("B", "C", False)]))
    add(H, "cnm_h121_q2", figure=D.cuboid(120, 84, 70, letters=True, bold=[("A", "D", False), ("B", "C", False), ("F", "G", False), ("E", "H", True)]))
    add(H, "cnm_h122_q3", figure=D.cuboid(130, 90, 72, face_note="this side face"))
    add(H, "cnm_h164_q1", figure=D.cuboid(150, 80, 96, bold=[("A", "B", False), ("B", "F", False)],
                                         tags=[("A", "B", "(4, 0, 0)"), ("B", "F", "(0, 3, 0)")]))
    add(H, "cnm_h122_q2", figure=D.cuboid(100, 100, 100, ticks=True, margin=24))
    # Draw the isosceles triangle with a 40° vertex angle separately; do not reuse the 36° figure.
    CATALOG[:] = [c for c in CATALOG if c["id"] != "cnm_137_q1"]
    add(P, "cnm_137_q1", figure=fig_iso_apex(40))
    return CATALOG


def fig_iso_apex(deg):
    L = 200
    A = (160, 30)
    half = math.radians(deg / 2.0)
    B = (A[0] - L * math.sin(half), A[1] + L * math.cos(half))
    C = (A[0] + L * math.sin(half), A[1] + L * math.cos(half))
    near(D.angle_deg(B, A, C), deg, 0.35, "vertex angle")
    body = [
        D.poly([A, B, C], D.face("0.1")), D.poly([A, B, C], D.edge(2.5)),
        D.tick(A, B), D.tick(A, C),
        D.angle_arc(B, A, C, 32, "%s°" % deg, size=15),
    ]
    return D.svg(C[0] + 20, B[1] + 24, "".join(body))


def _join_counts():
    a = fig_count_squares(5, "Front")
    b = fig_count_squares(3, "Side")
    return D.svg(430, 90, _shift(a, 0) + _shift(b, 230))


def parse_ok(svg, where):
    import xml.etree.ElementTree as ET
    try:
        root = ET.fromstring(svg)
    except ET.ParseError as ex:
        raise SystemExit("%s: invalid SVG: %s" % (where, ex))
    tag = root.tag.split("}")[-1]
    expect(tag == "svg", where + ": root element is not svg")
    expect("viewBox" in root.attrib, where + ": missing viewBox")


def apply_catalog(catalog, preview_path=None):
    with open(QUESTIONS, encoding="utf-8") as f:
        questions = json.load(f)
    by = {q["id"]: q for q in questions}
    missing = [c["id"] for c in catalog if c["id"] not in by]
    expect(not missing, "Unknown question IDs: " + ",".join(missing))
    for spec in catalog:
        q = by[spec["id"]]
        if spec.get("figure"):
            parse_ok(spec["figure"], spec["id"])
            q["figure"] = spec["figure"]
        else:
            q.pop("figure", None)
        if spec.get("hide"):
            expect(q.get("type") == "choice", spec["id"] + " is not a choice question but is configured to hide choice text")
            q["hideChoiceText"] = True
        else:
            q.pop("hideChoiceText", None)
        wanted = spec.get("choices") or {}
        have = {c["key"]: c for c in q.get("choices") or []}
        if wanted:
            expect(set(wanted) == set(have), "%s: choice letters do not match: figure %s, question %s" % (spec["id"], sorted(wanted), sorted(have)))
        for c in q.get("choices") or []:
            if c["key"] in wanted:
                parse_ok(wanted[c["key"]], spec["id"] + c["key"])
                if spec.get("hide") and c["text"] and c["text"] in wanted[c["key"]]:
                    raise SystemExit("%s: figure for choice %s contains the choice label “%s”" % (spec["id"], c["key"], c["text"]))
                c["figure"] = wanted[c["key"]]
            else:
                c.pop("figure", None)
    if preview_path:
        write_preview(catalog, preview_path)
        return
    with open(QUESTIONS, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
        f.write("\n")
    from collections import Counter
    cnt = Counter(c["cat"] for c in catalog)
    print("Wrote figures for %d questions" % len(catalog))
    for k, v in cnt.most_common():
        print("  %s %d" % (k, v))


def write_preview(catalog, path):
    parts = ['<!DOCTYPE html><meta charset="utf-8"><title>Figure Preview</title>',
             '<style>body{margin:0;font-family:"Noto Sans CJK SC",sans-serif}',
             '.row{display:flex;gap:8px;align-items:stretch}',
             '.card{width:300px;padding:8px;box-sizing:border-box}',
             '.light{background:#fff;color:#162033}.dark{background:#172232;color:#e7eef8}',
             'svg{width:100%;height:auto;display:block}h2{font-size:14px;margin:16px 8px 4px}</style>']
    for spec in catalog:
        blobs = []
        if spec.get("figure"):
            blobs.append(spec["figure"])
        if spec.get("choices"):
            for k in sorted(spec["choices"]):
                blobs.append(spec["choices"][k])
        parts.append("<h2>%s · %s%s</h2>" % (spec["id"], spec["cat"], " · labels hidden" if spec.get("hide") else ""))
        parts.append('<div class="row">')
        inner = "".join('<div class="card">%s</div>' % b for b in blobs)
        parts.append('<div class="light row">%s</div><div class="dark row">%s</div>' % (inner, inner))
        parts.append("</div>")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(parts))
    print("Preview", path, "total", len(catalog), "questions")


def main():
    catalog = build()
    # The 40° vertex-angle figure is added at the end of build; fig_iso36 was already validated when question 138 was built.
    if len(sys.argv) >= 3 and sys.argv[1] == "--preview":
        apply_catalog(catalog, preview_path=sys.argv[2])
    else:
        apply_catalog(catalog)


if __name__ == "__main__":
    main()
