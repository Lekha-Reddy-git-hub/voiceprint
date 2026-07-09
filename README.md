<p align="center">
  <img src="banner.png" alt="voiceprint - teach AI what you sound like" width="100%" />
</p>

<h1 align="center">voiceprint</h1>

<p align="center"><em>Teach AI what you sound like.</em></p>

<p align="center">
  <a href="https://github.com/Lekha-Reddy-git-hub/voiceprint/stargazers"><img src="https://img.shields.io/github/stars/Lekha-Reddy-git-hub/voiceprint?style=for-the-badge&logo=github&labelColor=0f172a&color=fbbf24" alt="Stars" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-10a37f?style=for-the-badge&labelColor=0f172a" alt="MIT License" /></a>
  <img src="https://img.shields.io/badge/Works%20with-Claude%20%C2%B7%20Cursor%20%C2%B7%20Codex-111827?style=for-the-badge&labelColor=0f172a" alt="Supported agents" />
  <img src="https://img.shields.io/badge/Receipts-not%20verdicts-10a37f?style=for-the-badge&labelColor=0f172a" alt="Receipts not verdicts" />
</p>

<p align="center"><sub><a href="#the-idea">Idea</a> · <a href="#how-it-works">Four organs</a> · <a href="#install">Install</a> · <a href="#pairs-with-stop-ai-slop">Stop-ai-slop</a> · <a href="#research">Research</a> · <a href="#faq">FAQ</a> · <a href="#license">License</a></sub></p>

## The idea

De-slopped AI text converges on the same beige neutral. Research shows LLM
assistance measurably homogenizes writing across authors (Padmakumar & He, ICLR 2024).
voiceprint is the other half. It learns your voice from your own writing, renders
your raw thoughts as finished prose in that voice, and attaches an evidence report
so you can see exactly why it sounds like you, or doesn't.

Stop-slop taught AI what not to sound like. This teaches it what *you* sound like.

## How it works

Four organs, always in this order: **Profile, Render, Audit, Learn.**

1. **Profile.** Feed it 5 to 10 of your posts or emails. It measures your fingerprint
   (sentence rhythm, punctuation rates, signature moves, never-dos) with
   `style_vector.py`, then writes your profile as imperatives.
2. **Render.** Dump raw thoughts; get prose in your voice. It never invents your
   anecdotes. It leaves `[YOUR EXAMPLE: ...]` slots only you can fill.
3. **Audit.** Every draft ships with receipts: each metric against *your* baseline,
   counted pattern hits, and a confidence line with stated assumptions. Never an
   "AI or not" verdict, because detectors are unreliable and biased
   ([Liang et al., Patterns 2023](https://arxiv.org/abs/2304.02819)).
4. **Learn.** Your edits update your profile. It knows you better every week.

De-slopping is built in (`deslop.md`), so voiceprint works on its own.

## Install

```bash
# Claude Code
cp -r voiceprint ~/.claude/skills/voiceprint
```

- **Claude.ai Projects:** upload `SKILL.md` plus the reference files
- **Anything else:** paste `SKILL.md` into your system prompt

## Pairs with stop-ai-slop

[stop-ai-slop](https://github.com/Lekha-Reddy-git-hub/stop-ai-slop) subtracts the
machine. voiceprint adds the human. Together they rewrite in your voice and de-slop
in one pass, with the de-slop gated by your profile so it never strips your real
quirks. Sound like YOU, not sound generically human, is the part no humanizer does.

## Research

This design stands on published work, mapped decision by decision in
[RESEARCH.md](RESEARCH.md): stylometry and authorship attribution (Stamatatos 2009),
writing homogenization (Padmakumar & He 2024), excess-vocabulary AI tells
(Kobak et al. 2025), personalization (Salemi et al. 2024), automated essay scoring
(ETS e-rater), and detector bias (Liang et al. 2023).

## FAQ

**How many samples do I need?** At least 5. Fewer than that and the fingerprint is
noisy, so it falls back to plain de-slopping and tells you so.

**Will it fake my anecdotes?** No. Where a lived example is needed it leaves a
`[YOUR EXAMPLE: ...]` slot for you to fill. It never invents your experiences.

**Is this an AI detector?** No. It reports counted evidence against your own
baseline, never an "AI: yes/no" verdict.

**Can I use it to imitate someone else?** It is a first-person tool: build profiles
from your own writing. Analyzing public writing for study is fine; passing text off
as a real third person is out of scope.

## License

MIT. See [LICENSE](LICENSE).
