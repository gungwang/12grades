"""Minimal normalization for comparing short questions. It follows the idea of diagnose/engine.js's normalizeText and is used only for a rough second-pass check."""
import re
import unicodedata


def norm_text(s):
    s = unicodedata.normalize("NFKC", str(s))
    s = s.replace("²", "^2").replace("³", "^3").replace("−", "-")
    s = re.sub(r"\s+", "", s).lower()
    # Keep these Chinese answer labels: they are structural prefixes stripped from source answers.
    s = re.sub(r"^(答案|答)[:=]", "", s)
    # Keep the CJK full stop as an additional source-text punctuation token to strip.
    return s.rstrip(".。!")
