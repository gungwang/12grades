"""Utilities for drafting middle-school physics (People's Education Press, 2024/2025 edition): topics, questions, and prerequisites are registered in phy_g8a/phy_g8b/phy_g9."""
from __future__ import annotations

TOPICS = []          # In textbook order.
_BY_KEY = {}

# These shared taxonomy values are checked by T and used by phy_g8a/phy_g8b/phy_g9.
PHY_DOMAINS = ("物质", "运动和相互作用", "能量", "跨学科实践")
# Units allowed in physics multiple-choice options; verification compares a value and unit as one value.
UNITS = ("m/s", "km/h", "kg/m³", "g/cm³", "kg", "g", "t", "mg", "m³", "cm³", "dm³", "mL", "L",
         "m", "cm", "mm", "km", "μm", "nm", "s", "min", "h", "N", "Pa", "kPa", "J", "kJ", "W", "kW",
         "kW·h", "V", "kV", "mV", "A", "mA", "Ω", "kΩ", "℃", "Hz", "dB", "%", "J/(kg·℃)", "J/kg", "N/kg", "m²", "cm²")


def T(key, sec, name, domain, typ, desc, mastery, std, pre=(), math=(), qs=(), root=None, figure_note=None):
    assert key not in _BY_KEY, key
    assert domain in PHY_DOMAINS, (key, domain)
    assert 2 <= len(mastery) <= 3, key
    t = dict(key=key, sec=sec, name=name, domain=domain, type=typ, description=desc, mastery=list(mastery),
             std=list(std), pre=list(pre), math=list(math), qs=list(qs), root=root)
    TOPICS.append(t)
    _BY_KEY[key] = t
    return t


def C(diff, prompt, right, wrongs, expl, verify=None, figure=None, pos=None):
    """Multiple-choice question: right is the correct option text, wrongs are 2–3 common errors, and right is used for verification when verify is omitted."""
    return dict(kind="choice", diff=diff, prompt=prompt, right=right, wrongs=list(wrongs), expl=expl,
                verify=verify, figure=figure, pos=pos)


def N(diff, prompt, answer, expl, verify, figure=None, percent=False):
    """Numeric question: answer is unitless (the unit appears in the prompt); verify is an expression that evaluates to it."""
    return dict(kind="numeric", diff=diff, prompt=prompt, answer=str(answer), expl=expl, verify=verify, figure=figure,
                percent=percent)
