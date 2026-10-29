# -*- coding: utf-8 -*-
"""Register high-school English topics in teaching order; the sequence is the main soft-prerequisite backbone."""
from en_lib import TOPICS
import enh_b1
import enh_b2
import enh_b3
import enh_s1
import enh_s2
import enh_s3
import enh_s4
import enh_edges  # noqa: F401

enh_b1.load()
enh_b2.load()
enh_b3.load()
enh_s1.load()
enh_s2.load()
enh_s3.load()
enh_s4.load()

if TOPICS[0]["key"] != "gr_sentmem":
    raise SystemExit("High-school English must start with sentence elements gr_sentmem")
if not (220 <= len(TOPICS) <= 320):
    raise SystemExit("High-school English topic count %d is outside 220–320" % len(TOPICS))
_keys = [t["key"] for t in TOPICS]
if len(_keys) != len(set(_keys)):
    raise SystemExit("Duplicate high-school English topic key")
# Keep this assertion aligned with the topic name registered in enh_s2.py.
if not any(t["name"] == "Subjunctive Mood" for t in TOPICS):
    raise SystemExit("The required “Subjunctive mood” topic is missing")
