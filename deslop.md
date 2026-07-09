# deslop.md: bundled slop removal for Render Pass C

Strip these machine tells from a draft AFTER voice-matching, and BEFORE the
audit. Baseline-relative: if a signature move is genuinely the user's (their
profile marks it PROTECTED), keep it. Only cut what the user does not do.

## Tiered, not banned

**Always cut (vocabulary tells).** delve, tapestry, testament, robust, seamless,
elevate, boasts, nestled, realm, underscore, bustling, "in the ever-evolving
world of", "in today's fast-paced".

**Always cut (structure tells).**
- Throat-clearing openers: "In this post", "Let's dive in", "Here's the thing".
- Restate-everything endings that summarize what was just said.
- "It's not just X, it's Y" and "not only X but also Y" when used for lift.
- The correlative pivot "X isn't about A. It's about B" at more than one per piece.
- Rule-of-three lists where two items would do.

**Cut unless the profile protects it.**
- Em-dashes: cap at the user's own baseline rate. Default to commas, colons,
  or full stops when unsure. (A tool about de-slopping should not itself lean on
  the single most-cited AI tell.)
- Rhetorical questions used as section transitions.
- "Imagine a world where", "What if I told you".

**Frequency-capped (fine once, slop when repeated).**
- Sentence-initial "And" / "But": keep sparse, match the user's baseline.
- One-word or two-word fragments for drama: cap near the user's rate.
- Bold section headers, emoji bullets: keep only if the user actually uses them.

## Structural tells from the full catalog (profile-gated)

Preloaded from stop-ai-slop. Apply ONLY where the pattern is not the user's own
voice. Some people genuinely write passively or open sentences with "Why"; if the
profile marks the habit as theirs, keep it. Otherwise cut.

- **Em dashes: remove.** Match the user's baseline, default to commas, colons, or
  periods. Repeated here because it is the single most-cited tell.
- **Passive voice.** Find the actor and put them at the front ("the team shipped
  it", not "it was shipped"), unless the actor is genuinely unknown or the profile
  shows a passive habit.
- **Wh- sentence openers.** Sentences that open with What, When, Where, Which, Who,
  Why, or How as a setup ("What makes this hard is..."). Restructure to lead with
  the subject, unless the user opens this way by habit.
- **Narrator from a distance.** "Nobody designed this", "This happens because",
  "People tend to". Put the reader in the room instead.
- **Vague declaratives.** "The reasons are structural", "the stakes are high", "the
  implications are significant". Replace with the specific thing, or cut.
- **Negative listing.** "Not a ticket. Not a checklist. A way of thinking." State
  the thing without the runway.
- **False agency.** "The data tells us", "the market rewards", "the culture shifts".
  Name the human who actually did it.

If stop-ai-slop is installed, prefer running its full `catalog.md` and
`false-positives.md` here, still gated by the profile. This bundled list is the
standalone fallback.

## Sycophancy and hedging (cut in the user's own voice)

- "Great question", "You're absolutely right", "I'd be happy to".
- Hedging stacks: "It's worth noting that it could be argued that perhaps".
- Fake specificity: "studies show", "experts agree", "research suggests" with no
  named source.

## The over-polish flag

If the finished draft is markedly cleaner and more uniform than the user's own
baseline (fewer asides, no run-ons, every sentence the same length), flag it.
Real voices are uneven. Do NOT fabricate errors to fake unevenness; instead,
stop over-editing what the user actually wrote.
