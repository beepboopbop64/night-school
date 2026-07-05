---
session: dotprod
aha: "The dot product is a similarity meter."
spineVersion: 1
locked: 2026-07-04
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

## 1. The aha (canonical sentence, string-matched everywhere)

**"The dot product is a similarity meter."**

Falsification test the session must pass on screen: the probe sweep shows
the score climbing with alignment, reading zero across, and going negative
against; the meter framing survives the misconception check (a big score is
agreement of direction, not identity of items).

## 2. The locked beat list (stable ids; one new idea each)

| id | Beat | One-line intent | Est. sec |
|----|------|-----------------|----------|
| beat-01 | Hook | The recommendation moment: two lists of numbers agreed; how do you score a match? | 24 |
| beat-02 | Felt elemental unit | Multiply pairwise and add; the learner sweeps the probe and feels the score move; misconception (similarity means identical) voiced and refuted | 34 |
| beat-03 | Aha | The behavior gets its name: agree positive, across zero, oppose negative; the sentence trues up in mint | 28 |
| beat-04 | Close | Retrieval prompt, the length problem as the walk-home gap, extensions menu | 26 |

Total 112s estimated; hard cap 540s (L10).

## 3. The metaphor registry (with honesty boundaries)

Primary, load-bearing beats 2 through 4: **the meter**. A physical dial
whose needle answers a comparison: agree, ignore, oppose. Exact as far as
sign and monotone-in-alignment go. Declared strains, disclosed in-session:

1. the numbers in this session are chosen for readability; real embedding
   coordinates are neither small nor round (beat-02, page callout).
2. real embeddings live in hundreds of dimensions; two dimensions is the
   picture, not the territory. Nothing in the mechanism changes with
   dimension count (beat-03, page callout).

## 4. Color assignments (semantic cast, locked)

| Concept | Token |
|---|---|
| the probe (the thing asking) | data.heat (amber) |
| the candidates (the data interrogated) | data.observed (periwinkle) |
| the score bars / meter needle | data.params (lilac) |
| the aha true-up | data.fit (mint) |
| labels | text (cream) |
| background | bg (10pm Sky) |

## 5. Extensions sketch (Still up?)

- talk lane: have an LLM defend, then attack, the meter metaphor; a good
  conversation surfaces the length problem unprompted.
- read lane: the attention paper (arXiv 1706.03762) is where tonight's
  score reappears inside a softmax; Bahdanau (arXiv 1409.0473) is where
  learned alignment scores first shipped.
- build lane: a NumPy meter over toy "song" vectors with a ranking check.
