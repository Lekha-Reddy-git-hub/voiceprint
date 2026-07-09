---
name: voiceprint
description: Learn a person's writing voice from their own samples and render their raw thoughts as finished prose in that voice, with an evidence-based audit report. Use when the user wants writing that sounds like them, wants their notes or thought-dumps turned into posts, emails, or essays in their own style, or asks "does this sound like me / like AI?"
---

# Voiceprint

Slop removal teaches AI what not to sound like. This teaches it what YOU sound like.
Four organs, always in this order: **Profile, Render, Audit, Learn.**

Scope rule: first person only. Build profiles from the user's OWN writing.
Analyzing public figures is allowed for study; generating text to pass as a real
third person is out of scope, so decline it.

## Organ 1: PROFILE (run once, update often)

1. Ask for 5 to 10 samples of their real, finished writing (same genre as the
   target: LinkedIn voice, email voice, and essay voice all differ). ALSO ask for
   2 to 3 raw thought-dumps or before/after edit pairs if they have them, because
   idea-shape matters as much as sentence-shape.
2. Fewer than 5 samples: say the fingerprint will be low-confidence and fall back
   to plain de-slopping. Never invent a voice.
3. Read everything before writing anything.
4. Measure first (numbers, not vibes): run `style_vector.py` on the combined
   samples. Record the output in the profile verbatim.
5. Then extract what numbers can't catch, using `voiceprint-template.md`.
6. Write the profile as IMPERATIVES, not description ("Open mid-thought. Never use
   semicolons. End roughly 1 in 3 posts on an unresolved question."), and embed
   2 to 3 short excerpts from the real samples as exemplars.
7. Protect the pet phrases: the user's signature moves are features, never slop.

## Organ 2: RENDER (every draft)

Input: the user's raw thoughts (bullets, voice-note transcript, messy paragraph).
Pass A, content: organize their ideas. Add nothing they didn't think. Where the
  draft needs a lived anecdote, insert `[YOUR EXAMPLE: ...prompt...]`. Never
  fabricate their experiences.
Pass B, voice: rewrite per the profile's imperatives. Match the numbers (sentence
  rhythm, punctuation rates) AND the moves (openers, closers, humor register).
Pass C, de-slop: strip machine tells using the bundled `deslop.md`. If the user
  also has a standalone slop-removal skill installed, apply that too.

## Organ 3: AUDIT (attach to every render; receipts, never verdicts)

Re-run `style_vector.py` on the draft. Report:
- Each metric against the user's OWN baseline. Never against a universal ideal,
  because universal rubrics create monoculture (see RESEARCH.md).
- Regularity check: which of the user's habits is the draft over-repeating?
  A voice tool can amplify a person's template into a machine tell. Cap any
  signature move that exceeds about 1.5 times the user's baseline frequency.
- Confidence line, always with assumptions: "Voice-match high, based on 12
  samples of your LinkedIn writing; low confidence for email."
- NEVER output "AI-written: yes/no". Detectors are unreliable and biased
  (Liang et al. 2023). Output counted evidence and let the human judge.

## Organ 4: LEARN (after the user edits)

When the user edits your render, diff it. Each edit is profile data:
- They deleted your dashes: lower the dash cap.
- They rewrote the opener: capture the shape of theirs.
Append dated one-line updates to the profile's `## Learned` section. The profile
is a living document; version it in git.

## Genre awareness

Keep one profile per genre. If asked to render into a genre with no profile,
say so and use the nearest profile with a low-confidence note.
