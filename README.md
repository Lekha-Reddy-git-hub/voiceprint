# voiceprint

**Stop-slop taught AI what not to sound like. This teaches it what *you* sound like.**

De-slopped AI text converges on the same beige neutral — research shows LLM
assistance measurably homogenizes writing across authors (Padmakumar & He, ICLR 2024).
voiceprint is the other half: it learns your voice from your own writing, renders
your raw thoughts as finished prose in that voice, and attaches an evidence report
so you can see exactly why it sounds like you — or doesn't.

## How it works — four organs

1. **Profile** — feed it 5–10 of your posts/emails. It measures your fingerprint
   (sentence rhythm, punctuation rates, signature moves, never-dos) with
   `style_vector.py`, then writes your profile as imperatives.
2. **Render** — dump raw thoughts; get prose in your voice. It never invents your
   anecdotes — it leaves `[YOUR EXAMPLE: …]` slots only you can fill.
3. **Audit** — every draft ships with receipts: each metric vs *your* baseline,
   counted pattern hits, and a confidence line with stated assumptions.
   Never an "AI or not" verdict — detectors are unreliable and biased
   ([Liang et al., Patterns 2023](https://arxiv.org/abs/2304.02819)).
4. **Learn** — your edits update your profile. It knows you better every week.

## Install

- **Claude Code:** copy this folder into `~/.claude/skills/voiceprint`
- **Claude.ai Projects:** upload `SKILL.md` + the reference files to project knowledge
- **Anything else:** paste `SKILL.md` into your system prompt

Pairs well with a slop-removal skill (e.g. stop-slop and derivatives) for Pass C.

## The receipts, not verdicts, philosophy

Scoring writing against a universal ideal creates monoculture — that's how GRE
template essays happened, and how AI slop happened. voiceprint only ever scores
you against you. See [RESEARCH.md](RESEARCH.md) for the published work this
design stands on (stylometry, automated essay scoring, personalization, detector bias).

## Scope

First person only: build profiles from your own writing. Analyzing public writing
for study is fine; generating text to pass as a real third person is not what this
is for.

MIT — see LICENSE.
