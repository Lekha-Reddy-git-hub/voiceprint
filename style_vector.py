#!/usr/bin/env python3
"""style_vector.py — measure a writing fingerprint. Part of voiceprint (MIT).

Usage:
  python3 style_vector.py samples.txt            # one file
  python3 style_vector.py draft.txt --json       # machine-readable
Multiple texts in one file may be separated by lines starting with '==='.
"""
import re, sys, json, statistics, unicodedata

def norm(t):
    return ''.join(unicodedata.normalize('NFKC', c) if 0x1D400 <= ord(c) <= 0x1D7FF else c for c in t)

def measure(text):
    bold = sum(1 for c in text if 0x1D400 <= ord(c) <= 0x1D7FF)
    t = norm(text)
    words = re.findall(r"[A-Za-z0-9'+-]+", t)
    if not words:
        return {}
    sents = [s.strip() for s in re.split(r'(?<=[.!?])\s+', t) if s.strip()]
    slens = [l for l in (len(re.findall(r"[A-Za-z0-9'+-]+", s)) for s in sents) if l > 0]
    n = len(words)
    per1k = lambda c: round(1000 * c / n, 1)
    frag = sum(1 for l in slens if l <= 4)
    long_ = sum(1 for l in slens if l >= 25)
    m = {
        "words": n,
        "sentences": len(slens),
        "sent_median": statistics.median(slens) if slens else 0,
        "sent_stdev": round(statistics.stdev(slens), 1) if len(slens) > 1 else 0,
        "fragment_pct": round(100 * frag / len(slens)) if slens else 0,
        "long_sent_pct": round(100 * long_ / len(slens)) if slens else 0,
        "em_dash_per_1k": per1k(text.count("—")),
        "colon_per_1k": per1k(t.count(":")),
        "semicolon_per_1k": per1k(t.count(";")),
        "question_per_1k": per1k(t.count("?")),
        "exclam_per_1k": per1k(t.count("!")),
        "paren_per_1k": per1k(t.count("(")),
        "bold_unicode_chars": bold,
        "sentence_initial_And_But": len(re.findall(r"(?:^|[.!?]\s+)(?:And|But)\s", t)),
        "contrast_pivots_notX_itisY": len(re.findall(r"(?:is |are |was |not |no longer )[^.]{0,60}\.\s*(?:It is|They are|That is)", t)),
        "numbered_list_blocks": len(re.findall(r"\b1\.\s+[^.]+2\.\s", t, re.S)),
    }
    return m

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    as_json = "--json" in sys.argv
    if not args:
        print(__doc__); sys.exit(1)
    text = open(args[0], encoding="utf-8").read()
    text = re.sub(r"^===.*$", "", text, flags=re.M)
    m = measure(text)
    if as_json:
        print(json.dumps(m, indent=2))
    else:
        w = max(len(k) for k in m)
        for k, v in m.items():
            print(f"{k.ljust(w)}  {v}")

if __name__ == "__main__":
    main()
