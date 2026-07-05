---
session: dotprod
aha: "The dot product is a similarity meter."
spineVersion: 2
locked: 2026-07-05
scope: >-
  Plain dot product as an alignment score, in two dimensions, four
  candidates. No cosine, no matrices, no attention; those are breadcrumbs.
compromises:
  - id: toy-numbers
    phrase: "the numbers in this session are chosen for readability"
  - id: two-dimensions
    phrase: "real embeddings live in hundreds of dimensions"
---

# Spine: dotprod

The session's constitution. Every downstream artifact answers to this file.
(spineVersion 1 locked 2026-07-04; version 2 is the Phase 3 single-thread
rewrite of 2026-07-05.)

## 1. The aha (canonical sentence, string-matched everywhere)

**"The dot product is a similarity meter."**

Falsification test the session must pass on screen: the probe sweep shows
the score climbing with alignment, reading zero across, and going negative
against; the meter framing survives the misconception check (a big score is
agreement of direction, not identity of items).

## 2. The locked beat list (stable ids; one new idea each)

| id | Beat | One-line intent | Est. sec |
|----|------|-----------------|----------|
| beat-01 | Hook | The recommendation moment: a song matched your taste, but each is many qualities at once; the difficulty made explicit (no single ruler spans the qualities, exact match on all of them is a lottery, the collapse must be principled) before the learner attempts it | 58 |
| beat-02 | Felt elemental unit | Struggle recap, the arrow idea, THE RECIPE stated plainly with tiny worked numbers, meet the instrument (probe, candidates, bars), a falsifiable prediction (does any score go negative?), the sweep with everything frozen but the probe (direction story), then the explicit length stretch; misconception (similarity means identical) voiced and refuted | 100 |
| beat-03 | Aha | The behavior gets its name: agree positive, across zero, oppose negative; the sentence trues up in mint | 36 |
| beat-04 | Close the loop | Retrieval prompt, then the hook's data center reread as the learner's own machine: taste = probe, catalog = candidates, meter at scale. Song thread only | 40 |
| beat-04b | The honest look | Sharpened doubling prediction (exactly double, or just drift up?), linearity named, the crack; stakes song-side only (loud songs win on loudness) | 38 |
| beat-05 | Take it with you | Recap chain (tangle, arrows, multiply-and-add, meter with a crack), the ONE licensed aside (job posting), invent-your-own-pair invitation, walk-home breadcrumb, extensions menu pointer | 36 |

Total 308s estimated; hard cap 540s (L10).

## 3. The metaphor registry (with honesty boundaries)

Primary, load-bearing beats 2 through 5: **the meter**. A physical dial
whose needle answers a comparison: agree, ignore, oppose. Exact as far as
sign and monotone-in-alignment go. Declared strains, disclosed in-session:

1. the numbers in this session are chosen for readability; real embedding
   coordinates are neither small nor round (beat-02, page callout).
2. real embeddings live in hundreds of dimensions; two dimensions is the
   picture, not the territory. Nothing in the mechanism changes with
   dimension count (beat-03, page callout).

## 4. Single-thread discipline (Phase 3; L12 enforces)

The session rides ONE walked example end to end: songs and your taste.
Every beat's narration, on-screen text, and visuals stay on that thread.
The second, surface-different instance (R28) is **a job posting**, licensed
to appear in exactly one place: the consolidation beat (beat-05), clearly
marked as an aside, after the recap and before the invitation to invent
your own pair. The storyboard's `thread` block declares the aside keywords
(job, resume, role, posting, hiring, fit); the L12 linter fails the build
if any of them leaks into another beat, page section, or the doc outside
its closing section.

## 5. Color assignments (semantic cast, locked)

| Concept | Token |
|---|---|
| the probe (the thing asking) | data.heat (amber) |
| the candidates (the data interrogated) | data.observed (periwinkle) |
| the score bars / meter needle | data.params (lilac) |
| the aha true-up | data.fit (mint) |
| labels | text (cream) |
| background | bg (10pm Sky) |

## 6. Extensions sketch (Still up?)

- talk lane: have an LLM defend, then attack, the meter metaphor; a good
  conversation surfaces the length problem unprompted.
- read lane: the attention paper (arXiv 1706.03762) is where tonight's
  score reappears inside a softmax; Bahdanau (arXiv 1409.0473) is where
  learned alignment scores first shipped.
- build lane: a NumPy meter over toy "song" vectors with a ranking check.
