---
session: attention
aha: "Attention is a soft lookup table."
spineVersion: 1
locked: 2026-07-04
treatment: treatment.md (merged; base obstruction-first; grafts per treatment/judgment.md)
scope: single-head dot-product attention only (D-O2, flagged for Jake in brief.md)
---

# Spine: attention

The session's constitution. Every downstream artifact (storyboard, script,
page, video, doc, notebook) answers to this file. Edits here are logged
decisions that dirty dependents; edit deliberately or not at all.

## 1. The aha (canonical sentence, string-matched everywhere)

**"Attention is a soft lookup table."**

Falsification test the session must pass on screen: every row of the dict
correspondence demonstrated (section 3), and the hard-lookup limit shown
exactly (sharpen scores 20x, weights hit one-hot to eight decimals, the
dict returns, the gradient dies). If any row failed to map, the metaphor
would be decoration and the session fails its own sentence.

## 2. The locked beat list (stable ids; one new idea each)

| id | Beat | One-line intent | Est. sec |
|----|------|-----------------|----------|
| beat-01 | Hook | The 2014 fixed-vector bottleneck, the backwards hack, and the intern who decided to stop squeezing; care lands inside 30s, question closes the beat | 80 |
| beat-02 | Gap | Looking is choosing and a choice has no gradient; the session's organizer question: "How do you learn where to look?" (P1) | 40 |
| beat-03 | Elemental unit | The dot product makes relevance a number that moves with alignment; PASSED qk-similarity verbatim; misconception similarity-means-identical voiced and refuted (P2) | 60 |
| beat-04a | Build: the wall | Score-then-argmax IS a Python dict; it answers perfectly and learns nothing; KeyError plus flatlined gradient meter (rose spend 1) (P3) | 45 |
| beat-04b | Build: the escape | Never choose: scale by sqrt(d_k) (bookkeeping, why deferred), exponentiate, normalize, blend; weights 0.766/0.186/0.045/0.003, output [0.912, 0.083]; primary misconception voiced, held open | 40 |
| beat-05 | Aha | Nothing new enters; P4 "you have seen this shape before"; dict rows morph into attention rows; the sentence trues up in mint; refutation (recipe proportions); Figure 2 rescue line completes | 60 |
| beat-06a | Compression: the formula | softmax(qK^T/sqrt(d_k))V assembled term by term, color-matched; sqrt(d_k) debt paid; softmax named; misconception softmax-picks-the-max voiced and refuted | 35 |
| beat-06b | Compression: the limit | P5 sharpen 20x; the hard dict returns exactly and the gradient dies; the aha passes its own falsification test | 35 |
| beat-07 | Stress-test | RAG as the same three-object skeleton at the opposite end of the hard-soft dial; causal-mask sentence; P6 then the scoped 2019 heatmap verdict; dual-heatmap morph, rose cross-out (rose spend 2) | 60 |
| beat-08 | Breadcrumb | Shuffle demo proves order-blindness; walk-home question (how does order get in?); verified GNMT stakes; recursive close on Bahdanau's gaze | 50 |

Total 505s estimated; target 480; hard cap 540. Trim plan in treatment.md
front matter.

Prediction and retrieval schedule (L4/L6): P1 beat-02, P2 beat-03, P3
beat-04a, P4 beat-05, P5 beat-06b, P6 beat-07; retrieval prompts at beat-07
(map your RAG stack) and beat-08 (rebuild from memory). Misconception beats
(L9): beat-03, beat-04b to beat-05 (primary), beat-06a.

## 3. The metaphor registry (with honesty boundaries)

### Primary, load-bearing beats 3 through 8: the forgiving dictionary

A Python dict rebuilt so a near-miss key gets partial credit instead of a
KeyError. Built namelessly (beat-03 scores, beat-04a hard form named by the
learner's own eyes), goes soft at beat-04b, named at beat-05, proven in the
limit at beat-06b, cousined at beat-07, and its inherited orderlessness is
beat-08's open question.

Drift ledger: every row is verified on screen; status column is the honesty
boundary. (Adopted from candidate-metaphor-first, judgment G9.)

| Dict | Mechanism | Status |
|---|---|---|
| the key you ask with | query q | exact |
| stored keys | keys k_1..k_n | exact |
| stored values | values v_1..v_n | exact |
| exact match, all or nothing | score 0 or 1 | exact (the limit case) |
| "how close is my question to this key" | q . k_j / sqrt(d_k), continuous | exact |
| hand back one value | return the single value | exact (hard lookup) |
| return, made forgiving | softmax-weighted blend of all values | exact as vector arithmetic; always shown as arithmetic on screen |
| KeyError | impossible in the soft box; weights just spread | exact |
| unordered | permutation of (k_j, v_j) pairs leaves output unchanged | exact, and it is the breadcrumb |

Declared strains (disclosed in-session where each becomes relevant):
1. A human flipping through stored entries scores and then PICKS; our
   machine is stranger: it refuses to pick (beat-04 names this; the
   learner's own behavior is the argmax foil).
2. Sharpening/temperature is a property of softmax used as pedagogy; the
   transformer has no such knob; sqrt(d_k) is the fixed principled cousin
   (beat-06b, spoken).
3. What counts as "close" is learned, not given (W_Q, W_K); seeded at
   beat-03, projections stay verbal in video, full story on page.
4. The learned projections have no dict counterpart at all; named in the
   extensions prompt as a legitimate strain.

### Secondary, exactly two appearances: recipe proportions

The weights are the recipe of the blend: what got mixed, never why the
recipe was chosen. Fires at the beat-05 refutation and once at beat-07. No
other uses.

### Ancillary images (bounded)

- The box/keyhole (fixed-vector bottleneck): beat-01 only, plus one
  callback at beat-06b ("the session's two walls were one wall: hardness").
- The cliff/staircase (choice has no gradient): born beat-02, returns
  inside the toy at beat-04a, dies with the escape. Never trues up; the
  argmax idea does not earn mint.
- Bahdanau's gaze (the amber dot): beat-01 seed, recursive close beat-08.

## 4. Color-semantic assignments (BRAND tokens; locked for the series)

One color, one job, everywhere. No hex literals anywhere downstream; tokens
only. Color is never the sole channel (shape, label, or motion always
co-signs).

| Concept | Token | Where it lives |
|---|---|---|
| Query (the thing asking; the gaze dot; q in every formula) | `data.heat` (amber) | seeded beat-01, on-object beat-03 onward, amber term in beat-06 formula |
| Keys (stored labels being interrogated; K) | `data.observed` (periwinkle) | beat-03 onward; periwinkle term in formula |
| Scores AND attention weights (the numbers the mechanism produces; softmax output; heatmaps) | `data.params` (lilac) | score bars beat-03; weight bars beat-04b, beat-05; both heatmaps in beat-07. Weights are normalized scores: same family, same color, per d-s2-weights-stay-lilac |
| Values (stored content handed back; V) | `data.truth` (cream) | card-shaped chips from beat-04a; card outline carries the channel so cream never relies on color against cream labels |
| Blended output, and every true-up | `data.fit` (mint) | output chip beat-04b onward; the aha true-up, the trued formula, title-card underline |
| Error, failure, tension (KeyError, flatlined gradient meter, crossed-out false explanation) | `data.error` (rose) | exactly two spends: beat-04a composite, beat-07 cross-out |
| Background | `bg` | everywhere |
| Labels and body text | `text` | on-object labels, never legends |
| Pre-formal annotations ("q . k" before the formula exists) and UI wayfinding | `brand.periwinkle`, Plex Mono italic | beat-03 annotation, page chrome |

Rationing note: `brand.rose` (jokes/warmth accent) is NOT spent
independently in this session; the two `data.error` moments are the
session's rose budget. Mint glow fires only at true-ups.

```yaml
decision:
  id: d-s2-values-color
  what: Lock values to data.truth cream rendered as card-shaped chips; blended output locks to data.fit mint.
  why: data.truth is the only free series token and "the stored content you retrieve" reads as reference/ground truth; the card shape guarantees the cream-on-cream label case never depends on color alone.
  alternatives: ["mint for values (rejected: mint is reserved for true-up and convergence semantics)", "a new token (rejected: palette is locked; adding tokens is a brand decision for Jake, and unnecessary)"]
```

## 5. The breadcrumb ("For the walk home")

Canonical question, posed at beat-08 and retrieved to open session 2:

> A dictionary has no idea what order you wrote it in, and neither does
> attention: shuffle the key-value pairs and the output does not move a
> digit. But "the cat sat on the mat" and "the mat sat on the cat" are
> different sentences made of identical cards. So what is the cheapest
> thing you could add to a token so that WHERE it sits becomes something a
> lookup can find?

Session 2 destinations named, not taught (D-O2): positional encoding, and
why one lookup per layer became eight in parallel.

## 6. Extensions menu sketch ("Still up?")

Three doors, page track, gestured at in the beat-08 video.

**Argue it out with an LLM (discussion prompts, with what-good-looks-like):**
1. "Defend the sentence 'attention is a soft lookup table' to a skeptic.
   Then find the places the metaphor legitimately strains." Good looks
   like: produces the sharpening limit unprompted; concedes the
   human-argmax and temperature-as-pedagogy strains and that the learned
   projections have no dict counterpart.
2. "My attention heatmap says the model focused on 'terrible', so that is
   why it said negative. Argue both sides." Good looks like: mixing weights
   versus causes; the 2019 results scoped to BiLSTM classifiers; the debate
   named as unresolved rather than settled either way.
3. "Why can a hard argmax version of attention not train by gradient
   descent? Where exactly does the gradient die?" Good looks like:
   flat-then-cliff output, zero slope almost everywhere, w(1 - w) going to
   zero at the sharp limit.

**Read the real thing (verified in sources.yaml):**
1. Bahdanau, Cho, Bengio (arXiv 1409.0473, ICLR 2015): watch Figure 2 pay
   off in the original; the mechanism hides in the appendix.
2. Vaswani et al. 2017, section 3.2 only: read the definition you can now
   read left to right, and find the word "suspect" in 3.2.1.
3. Jain and Wallace 2019 paired with Wiegreffe and Pinter 2019: the heatmap
   fight, both sides.

**Build something (notebook committed per d-s0-notebook-yes):**
1. The 30-line NumPy ladder (dossier 7): dict lookup and its KeyError;
   one-hot scores as a dot product; relax to softmax (0.766 cat, 0.186
   kitten); blend and compare with d["cat"]; sharpen and recover the dict
   exactly; optional gradient check where the soft version differentiates
   and the hard one flatlines. Micro-example numbers are the test vector.
2. Stretch: swap the toy vectors for real embeddings from any small model,
   ask the forgiving dictionary for "feline", and write three sentences on
   what came back and why. (Second stretch, for the curious: implement
   Nadaraya-Watson 1964 and notice it is tonight's formula, sixty years
   early.)

## 7. Decision log

```yaml
decision:
  id: d-s2-winner
  what: Ship obstruction-first as the treatment base, with named grafts from history-first and metaphor-first.
  why: It is the only candidate whose aha beat adds nothing new at the snap; the learner invents the escape in beat 4 and recognizes its identity in beat 5.
  alternatives: ["history-first (crowded aha)", "metaphor-first (hook trades verified stakes for charm)"]
  dirties: []
```

```yaml
decision:
  id: d-s2-scaling-at-blend
  what: Divide scores by sqrt(d_k) at beat-04b as named bookkeeping, paid in full at beat-06a.
  why: Keeps every on-screen number exact to dossier 1.5 (0.766/0.186/0.045/0.003 require scaled scores); candidates 1 and 2 were numerically inconsistent without it.
  alternatives: ["unscaled weights at beat 4, rescale at beat 6 (rejected: two weight sets for one example invites a continuity error)"]
  dirties: []
```

```yaml
decision:
  id: d-s2-weights-stay-lilac
  what: Attention weights render in data.params lilac in every beat; amber belongs to the query alone.
  why: Weights are normalized scores, the family the PASSED seed locked to lilac; one color, one job, everywhere.
  alternatives: ["amber heatmap bars for the work-lookalike pun (rejected: breaks the series ledger for one visual)"]
  dirties: []
```
