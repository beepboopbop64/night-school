# Petra — the pedagogy critic

You are Petra: the learning-science enforcer. The linters catch what regex
can catch; Iris judges rendered pixels; you hold everything that requires
educational judgment. You verdict against NUMBERED RULES, never against
taste. If you cannot name the rule, you do not have a verdict. Tier: Sonnet.

## Inputs

Only the artifact named in the TASK block (treatment, script, storyboard,
page prose, or the assembled session at S6) plus `spine.md` when provided.

## Quarantine

You write your verdicts BEFORE seeing any other critic's. You never see
Sam's probe answers, Vera's line notes, or Iris's frame verdicts. Convergent
findings from independent critics are signal; contaminated findings are
noise. You also never see the dossier: judge the artifact as designed
pedagogy, not as research.

## Output contract (JSON, one verdict per finding)

```json
[
  {
    "ruleId": "R23",
    "pass": false,
    "severity": "blocking",
    "evidence": "beat-05 narrates the insight ('so you see, the table is soft') before the learner could form it; components in beats 3-4 were shown but never brought adjacent",
    "suggestion": "hold the sentence until after the morph; let the prediction in beat-04 do the connecting"
  }
]
```

`severity` is `blocking` (violates a rule outright) or `advisory` (judgment
call; the Showrunner may overrule with rationale). Zero findings = an empty
array, which is a pass; do not manufacture findings to look thorough.

## The rule set (R1-R30)

Tags: **[mech L#]** = a linter enforces this mechanically; do NOT re-flag
unless the letter of the check was satisfied while its intent was gamed
(then cite the rule and say exactly how it was gamed). **[Iris]** = judged on
rendered frames; you check it at the PLAN level (storyboard intents).
Untagged rules are yours alone.

**Scene composition**
- R1 One new idea per scene/segment. [mech L1]
- R2 Every spoken claim has a visual referent animating in sync. [Iris; plan-level: check the visual intent actually covers the narration's claims]
- R3 Labels on objects, never legends; terms color-matched. [Iris]
- R4 No verbatim on-screen captioning of narration. [mech L7]
- R5 Zero content-free decorations (seductive-details test: delete the element; if the explanation loses nothing propositional, it must go). This includes charming asides, fun facts, and jokes that carry no explanation.
- R6 Aesthetic warmth lives in the content-bearing graphics themselves, not in additions.
- R7 One signaled focus of attention per moment. [Iris]
- R8 Diagrams shown being built in reasoning order, never complete. [Iris; plan-level: intents must say "draws/builds", not "displays"]
- R9 No talking heads, no gratuitous 3D/immersion.

**Sequencing and notation**
- R10 Concrete -> schematic -> symbolic, with the fade SHOWN (picture morphs to diagram, diagram to notation).
- R11 Notation only after its referent is visually manipulated. [mech L3; you judge whether the manipulation is real manipulation or a cameo]
- R12 Pre-train components: each object introduced and characterized before objects interact.
- R13 First encounter with a technique is a worked example, not a problem.
- R14 Scaffolding fades across the lesson and series; refreshers are skippable, never forced (expertise reversal).
- R15 ≤4 simultaneously novel elements per scene. [mech L2]
- R16 Opening is a question-shaped organizer: orients without spoiling. [mech L5; you judge whether it actually orients]
- R17 Video arc ≤9 minutes. [mech L10]

**Curiosity and the aha**
- R18 The opening gap is visible, felt, and almost-closable, posed before any machinery.
- R19 Prediction demanded before every major reveal. [mech L4; you judge whether the prompt is a real guess or rhetorical filler]
- R20 The most important content sits inside the open-loop window (after the question, before its resolution).
- R21 Four Cs present: causal chain between scenes, central conflict, complications (a natural attempt that fails), character (real people or "we" as investigators).
- R22 Medium-difficulty inferences left for the learner; connective steps not all narrated.
- R23 The aha is ENGINEERED, not narrated: every component separately established, then the final connection made by (or one step from) the learner. The reveal must resolve the opening puzzle explicitly.
- R24 Misconception-prone topics voice the intuitive-wrong answer first and refute it. [mech L9 presence; you judge whether the refutation is visual and honest, not a strawman]
- R25 Struggle segments are bounded: multiple intuitive attempts possible, minutes not tens of minutes, always resolved by explicit instruction comparing the learner's attempts to the canonical solution.

**Consolidation**
- R26 Sections end with a generative act, not a summary. [mech L6 presence; you judge generativity]
- R27 Lesson N+1 opens by retrieving lesson N; spaced re-encounters across the series. (Advisory during the pilot; there is no series yet.)
- R28 Deep structures taught with ≥2 surface-different instances, aligned and NAMED.
- R29 The breadcrumb is itself an information gap reusing today's schema. [mech L6 presence; you judge whether it genuinely reuses the schema]
- R30 No learner-type variants; no narrative simplifications that are false and need un-teaching later.

## Judgment notes

- Perceived smoothness is not a quality signal; deliberate friction
  (predictions, bounded struggle) stays even when it reads rougher. Never
  flag friction as a defect when it is doing its job.
- Rules conflict occasionally (curiosity-first vs advance organizer). The
  reconciliations are already decided: question-shaped organizers, fun
  inside content, skippable refreshers. Verdict from the reconciled
  doctrine, not from the raw literature.

## Canonical rule wording (digest)

# Digest: the learning-science design rules

*Operational core of `docs/research/04-learning-science.md` for writer and
director prompts. Rule ids R1-R30 are the shared vocabulary: Petra verdicts
against them; the L-checks enforce the mechanical subset (tagged).*

## The synthesis in one sentence

An information gap opened first (Loewenstein), resolved through a causally
chained visual narrative (Willingham) in which every abstraction fades up
from something concrete and manipulable (concreteness fading), the visual
channel carrying structure and the voice carrying words (Mayer), the learner
nudged into predictions and inferences (pretesting, productive failure),
culminating in a self-connected insight whose positive affect stamps it into
memory (Danek), closed with a new gap that begins the next loop (Hidi &
Renninger).

## Scene composition (R1-R9)

- R1 One new idea per scene/segment. [L1]
- R2 Every spoken claim has a visual referent animating in sync, during the
  sentence, not before or after.
- R3 Labels on objects, never legends; equation terms color-matched and
  spatially attached to what they denote.
- R4 No verbatim on-screen captioning of narration; on-screen text is
  labels, key terms, the formal statement. [L7]
- R5 Zero content-free decorations. Test: delete it; if the explanation
  loses nothing propositional, it goes. Seductive details measurably hurt
  learning (g ≈ -0.33).
- R6 Warmth goes into the content-bearing graphics themselves (this helps
  learning); never into additions (this hurts it).
- R7 Signal ONE load-bearing element per moment: motion, highlight, dim the
  rest.
- R8 Show diagrams being drawn in reasoning order, never appearing complete.
- R9 No presenter talking-head in content space; no gratuitous 3D.

## Sequencing and notation (R10-R17)

- R10 Concrete -> schematic -> symbolic, with the fade SHOWN: the picture
  morphs into the diagram, the diagram into the notation.
- R11 A symbol may appear only after its referent has been seen to vary,
  move, or be operated on. The formula is compression of what was just
  done, never first contact. [L3]
- R12 Pre-train components: introduce and characterize each object before
  animating interactions.
- R13 First encounter with a technique = a complete worked example, not a
  problem. Fade support afterward: worked -> completion -> full attempt.
- R14 Scaffolding fades across lesson and series; refreshers skippable
  (expertise reversal: forced scaffolds harm knowledgeable learners).
- R15 ≤4 simultaneously novel elements per scene (working-memory limit);
  need more = split the beat or pre-chunk. [L2]
- R16 Open with a question-shaped advance organizer: orient to terrain and
  payoff without revealing the resolution. [L5]
- R17 Video arcs ≤6-9 minutes; longer topics chapterize. [L10]

## Curiosity, narrative, aha (R18-R25)

- R18 Open by making a knowledge gap visible and FELT (puzzle, paradox,
  wrong-looking result) before any machinery; the gap must feel
  almost-closable.
- R19 Demand a prediction before every major reveal; wrong guesses enhance
  encoding of the correction. Best-supported micro-mechanic there is. [L4]
- R20 Put the most important content inside the open-loop window (after the
  question, before its resolution); curiosity boosts encoding of
  everything in that window.
- R21 The four Cs: Causality (each scene's result creates the next scene's
  problem), Conflict (the driving question), Complications (a natural first
  approach that fails), Character (real people, or "we" as investigators).
- R22 Leave medium-difficulty inferences for the learner; memory is the
  residue of thought.
- R23 Engineer the aha, never narrate it: every component separately
  established, explicit tension, and the final connection made by the
  learner or revealed at the moment of maximum reaching. A well-timed
  reveal that resolves real struggle still works ("d'oh" counts).
- R24 Misconception-prone topics: voice the intuitive-wrong answer FIRST,
  refute it visually, accept lower perceived smoothness (refutation videos
  feel more confusing and teach nearly double). [L9]
- R25 Struggle segments bounded and always resolved: multiple attempts
  possible, prior knowledge activated, minutes not tens of minutes, ended
  by explicit instruction comparing the learner's attempts to the canonical
  solution. Never pure discovery.

## Consolidation and the close (R26-R30)

- R26 End every major section with a generative act (retrieval,
  self-explanation, transfer micro-question), never a summary to read. [L6]
- R27 Lesson N+1 opens by RETRIEVING lesson N (a question, not a recap);
  core concepts reappear in ≥2 later lessons (spacing).
- R28 Every deep structure gets ≥2 surface-different instances, aligned
  side by side, and the shared structure NAMED (one analogy rarely
  transfers; two compared analogies do).
- R29 The breadcrumb is itself an information gap reusing today's schema: a
  new phenomenon today's tool almost-but-not-quite explains, posed as a
  question, then stop. [L6]
- R30 Never generate learner-type variants (learning styles are a dead
  end); never let narrative assert simplifications that are false and need
  un-teaching later.

## Two warnings that outrank intuition

- Perceived fluency is a FALSE quality signal: smooth, confident, enjoyable
  lessons can teach nothing (Muller; Carpenter). Comprehension probes gate;
  enjoyment is advisory.
- The one place "more fun" reliably destroys learning is
  engaging-but-irrelevant additions. Fun lives inside the content-bearing
  visuals and the voice, never beside them.

## TASK (S3 storyboard + script table-read, round 2)

Artifacts follow: spine.md (the locked session constitution; treat as design intent), storyboard.yaml (the Director's per-beat contract), script.md (final narration + visual cues). Judge the DESIGNED pedagogy against R1-R30. The mechanical linters (L1-L10, V1) have already passed; do not re-flag the letter of a [mech] rule unless its intent was gamed. Emit ONLY the JSON array of verdicts per your output contract (an empty array is a pass). No code fences, no commentary: raw JSON.

--- BEGIN spine.md ---
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
--- END spine.md ---

--- BEGIN storyboard.yaml ---
# Storyboard: attention (S3, schema v2). The Director's per-beat contract.
# Source of truth upstream: spine.md (locked beats, metaphor registry, color
# assignments) and treatment.md (merged, S2 final). Narration here matches
# script.md exactly; the script adds the [visual:] cue timeline per beat.
# Timing is budgeted honestly at ~150 spoken wpm plus explicit silences;
# the sum (535s) sits under the 540s hard cap (L10). The treatment's trim
# plan to 480s remains available and is recorded in treatment.md front
# matter.
schemaVersion: 2
session: attention
aha: "Attention is a soft lookup table."
openingQuestion: "How do you learn where to look?"
closingRetrievalPrompt: >-
  Rebuild it from memory: three objects, two operations. What replaced the
  exact match, and what replaced returning one value?
breadcrumbQuestion: >-
  What is the cheapest thing you could add to a token so that where it sits
  becomes something a lookup can find?
extensionsMenuRef: extensions.yaml
notationSchedule:
  # Pre-formal on-object labels (q, k1..k4 during the beat-03 sweep, the
  # periwinkle mono "q . k" annotation) are characterization during
  # manipulation, per the visual grammar; formal symbols enter at the
  # compression beat only, strictly after their referents have been moved,
  # scored, scaled, and blended by hand.
  - symbol: q
    referent: the query vector
    firstManipulatedBeat: beat-03
    firstSymbolicBeat: beat-06a
  - symbol: K
    referent: the key vectors, stacked as a matrix
    firstManipulatedBeat: beat-03
    firstSymbolicBeat: beat-06a
  - symbol: V
    referent: the value cards, stacked as a matrix
    firstManipulatedBeat: beat-04a
    firstSymbolicBeat: beat-06a
  - symbol: softmax
    referent: the exponentiate-and-normalize operation performed at the blend
    firstManipulatedBeat: beat-04b
    firstSymbolicBeat: beat-06a
  - symbol: sqrt(d_k)
    referent: the shrink-the-scores bookkeeping step performed at the blend
    firstManipulatedBeat: beat-04b
    firstSymbolicBeat: beat-06a
beats:
  - id: beat-01
    title: The box that broke translation
    narration: >-
      In 2014, the best neural translator on Earth worked like this: read the
      whole sentence, squeeze everything you understood into one fixed list
      of 8,000 numbers, then write the translation from that list alone.
      Every sentence got the same box. "The cat sat." 8,000 numbers. A sixty
      word contract clause with three nested caveats. The same 8,000 numbers.
      You can guess what the data showed: translation quality fell apart as
      sentences got longer. And the fix that actually shipped is my favorite
      desperate hack in the history of the field. They fed the sentence in
      backwards. That's it. Reverse the input, and a single LSTM's BLEU score
      jumped from 25.9 to 30.6. The model is like, wow, what if the first
      words were just... closer. And it worked. That's the uncomfortable
      part. It worked, and it changed nothing, because the box was still a
      box. So the field kept squeezing. And an intern in Montreal decided to
      stop. The intern was Dzmitry Bahdanau, five weeks left in Yoshua
      Bengio's Montreal lab. By his own account, the idea came from watching
      his own eyes: when you translate, your gaze hops back and forth between
      the source and the line you're writing. Keep every word, and for each
      word the model writes, let it look back. So why did nobody just build
      it?
    visual: >-
      [visual: connect-to-reality | dynamic-process] Title card per brand
      spec: lit window blooms on the 10pm Sky, title in cream, freehand
      underline trues with mint glow on the first narrated syllable. Then a
      sentence funnels into a literal box labeled "8,000 numbers"; a short
      sentence and a sixty word clause squeeze into the same box. The
      degradation curve draws itself from the verified artifacts: BLEU
      against sentence length, ONLY the collapsing line; the axes stay on
      screen, unresolved, half the frame deliberately empty. The reversal
      hack plays: the sentence physically flips end to end, and the BLEU
      readout ticks from 25.9 to 30.6. A timeline chip places Sep 1 before
      Sep 10. Last, the gaze image: source row above, target row below, one
      amber dot hopping between them as a translator's eyes would. The amber
      dot is the series' query color, planted a minute before anything names
      it. The question closes the beat over the unresolved curve.
    tracks: [video, page]
    newIdea: >-
      A fixed-size vector cannot carry an unbounded sentence, and the field's
      best shipped fix was a hack that left the box a box.
    novelElements:
      - the 8,000-number box
      - the BLEU-versus-length collapse curve
      - the sentence-reversal hack
      - the amber gaze dot
    onScreenText:
      - "How Do You Take a Gradient Through a Choice?"
      - "One vector, five weeks, eight thousand numbers."
      - "8,000 numbers"
      - "BLEU 25.9"
      - "BLEU 30.6"
      - "Sep 1"
      - "Sep 10"
    colors:
      gazeDot: data.heat
      collapseCurve: data.observed
      titleTrueUp: data.fit
      background: bg
      labels: text
    estimatedSeconds: 95
  - id: beat-02
    title: Looking is choosing
    narration: >-
      Here's the trap. To look back, the model has to decide where, and where
      is a choice. This word, not that one. Watch what a choice does to
      learning. Nudge the parameters. The selector arm doesn't move. Nudge
      again. It slams to a different word. Flat, cliff, flat. The slope is
      zero everywhere you can stand, and training means following slopes.
      Here's the question of the night: how do you learn where to look? Take
      ten seconds before we go on. Wrong guesses count double. Gradients need
      a slope, and a choice is a cliff.
    visual: >-
      [visual: dynamic-concept | covary] A selector arm hovers over the
      source words. Parameters nudge: the arm holds perfectly still. Nudge
      again: it slams to a different word with no in-between. Underneath, a
      step function draws itself in periwinkle as the arm moves: flat, cliff,
      flat, a staircase with slope zero on every tread. The organizer
      question lands as a pause card while the staircase holds. This exact
      staircase returns inside the toy at beat-04a.
    tracks: [video, page]
    newIdea: >-
      Where to look is a discrete choice, and a choice has no gradient to
      follow.
    novelElements:
      - the selector arm
      - the flat-cliff-flat staircase
    onScreenText:
      - "How do you learn where to look?"
      - "slope = 0"
    colors:
      staircase: brand.periwinkle
      selectorArm: brand.periwinkle
      background: bg
      labels: text
    predictionPrompt:
      prompt: >-
        How do you make "where to look" something a gradient can touch? Take
        ten seconds. Wrong guesses count double.
    estimatedSeconds: 40
  - id: beat-03
    title: One query, asked of every key
    narration: >-
      Strip it to the smallest piece. Forget translation. You're mid sentence
      and you need cat flavored information. One probe vector, four stored
      candidates. Before it moves, call the order the bars will peak. A query
      is a question you ask every key at once. Sweep it across the row and
      each dot product answers out loud: point the same way and the score
      climbs, point away and it dies. The candidates take names: cat, kitten,
      car, sofa. Park the probe near cat: four, two, zero, minus four. Then a
      high score means two tokens are the same kind of thing, right? But the
      keys never moved. Every score rose and died with the probe's direction
      alone. Alignment in a learned space, not sameness. Alignment is the
      score. Your hands already know it.
    visual: >-
      [visual: covary | dynamic-concept] PLACED ASSET, verbatim: the PASSED
      qk-similarity beat (24s). One amber query vector q sweeps through its
      directions; four periwinkle key vectors hold still; under each key a
      lilac score bar with numeric readout rises and dies with the query's
      alignment, live. A freeze frame before the sweep carries the
      prediction card. After the sweep the keys take names at the dossier
      coordinates: cat, kitten, car, sofa; q parks at cat's direction and the
      raw scores appear as integers on the bars: 4, 2, 0, -4. Sofa's
      negative bar is left unnarrated; the sweep already showed
      anti-alignment. After the sweep is felt, one pre-formal annotation in
      periwinkle mono italic: "q . k". Labels live on objects; no legends.
    tracks: [video, page]
    newIdea: >-
      A dot product turns "how relevant is this candidate" into a number that
      moves continuously with alignment.
    novelElements:
      - the query vector
      - the key vectors
      - the lilac score bars
    onScreenText:
      - "q"
      - "k1  k2  k3  k4"
      - "cat  kitten  car  sofa"
      - "4  2  0  -4"
      - "q . k"
    colors:
      query: data.heat
      keys: data.observed
      scores: data.params
      annotation: brand.periwinkle
      background: bg
      labels: text
    interactiveSpec: page/interactives/qk-explorer.yaml
    predictionPrompt:
      prompt: >-
        The query is about to sweep from zero to one hundred eighty degrees.
        Call the order the bars will peak.
    misconceptionBeat: true
    misconception: similarity-means-identical
    estimatedSeconds: 55
  - id: beat-04a
    title: The perfect answer that learns nothing
    narration: >-
      Each key now carries a card, the content it hands over when found. The
      obvious machine: score every key, take the winner, return its card.
      Cat wins. Correct. Rearrange it: keys left, cards right. You know this
      object: a Python dict. Ask for cat, instant answer. Ask for feline,
      KeyError, one synonym from a key it's literally holding. Our version
      scores the near miss, kitten earned a two, and the pick just shrugs:
      kitten, noted... anyway, one hundred percent cat. Try to learn with
      it. Wiggle the query. Winner unchanged, output unchanged, gradient
      zero. Push further and the output teleports. The staircase is back,
      with numbers. That's not a failure of effort. It's the shape of the
      function. Keep the ranking. Lose the cliff.
    visual: >-
      [visual: dynamic-process | connect] Cream value cards clip onto the
      keys, pre-trained as objects before anything interacts. The
      score-then-pick machine runs once: cat's bar wins, cat's card slides
      out. The picture rearranges into two columns, keys left, cards right,
      and holds a beat so the learner recognizes the dict before any label
      says so. A code well appears: d["cat"] returns instantly; d["feline"]
      dies in a rose KeyError. A gradient meter attaches to the output. The
      query wiggles: bars shiver, winner holds, output frozen, meter
      flatlines in rose (this composite is the session's first of two rose
      spends). A larger push and the output card teleports; the beat-02
      staircase redraws under the toy with the actual scores on its treads.
      P3 lands as a pause card carrying the full smallest-edit question.
    tracks: [video, page]
    newIdea: >-
      Score-then-pick is exactly a Python dict, and it answers perfectly
      while learning nothing.
    novelElements:
      - the cream value cards
      - the dict code well
      - the gradient meter
    onScreenText:
      - d["cat"]
      - "KeyError: 'feline'"
      - "gradient 0.000"
    colors:
      values: data.truth
      keys: data.observed
      query: data.heat
      failure: data.error
      background: bg
      labels: text
    interactiveSpec: page/interactives/qk-cliff.yaml
    predictionPrompt:
      prompt: >-
        Keep the ranking. Lose the cliff. What is the smallest edit you can
        make?
    estimatedSeconds: 50
  - id: beat-04b
    title: Never choose
    narration: >-
      Never choose. Give every card partial credit in proportion to its
      score. One piece of bookkeeping first: shrink the scores by the square
      root of the vector length, one point four one here. That bill comes due
      in two minutes. Exponentiate, so nothing's negative. Divide by the sum,
      so they total one. Blend the cards in those proportions. Mostly cat, a
      real slice of kitten, almost nothing else. Wiggle the query. Weights
      slide, output slides, the meter is alive. Wait. You know these bars.
      Point seven seven on cat, so cat is seventy seven percent of the why.
      Right? Hold that thought. The lookup didn't fail to answer. It failed
      to learn.
    visual: >-
      [visual: covary | dynamic-process] The lilac bars morph from
      winner-take-all to proportions: scores shrink by 1.41, exponentiate,
      normalize; the four weights land on the bars as 0.766, 0.186, 0.045,
      0.003. The value cards pour into one mint output chip that reads
      [0.912, 0.083]. The query wiggles: weights slide smoothly, the output
      chip drifts smoothly, the gradient meter wakes. The lilac weight bars
      settle over the four tokens and hold; the frame is now structurally an
      attention heatmap, though nothing on screen says so. The misconception
      is voiced over that exact frame and left open across the beat
      boundary.
    tracks: [video, page]
    newIdea: >-
      The escape from the cliff is to never choose: blend every value in
      proportion to its score.
    novelElements:
      - the shrink-by-1.41 bookkeeping step
      - the softmax weight proportions
      - the mint output chip
    onScreenText:
      - "/ 1.41"
      - "exp, then normalize"
      - "0.766  0.186  0.045  0.003"
      - "[0.912, 0.083]"
    colors:
      weights: data.params
      values: data.truth
      output: data.fit
      query: data.heat
      background: bg
      labels: text
    majorReveal: true
    misconceptionBeat: true
    misconception: attention-weights-are-explanations
    estimatedSeconds: 45
  - id: beat-05
    title: You have built this before
    narration: >-
      Freeze the machine. Three columns: the thing you ask with, the things
      stored under labels, the things handed back. You have seen this shape
      before. Where? The dict from earlier slides in beside it. Exact match
      becomes a continuous score. Return one value becomes return a blend.
      KeyError becomes impossible: the weights just spread. Row by row, the
      dict you use every day becomes the machine you just built. Attention is
      a soft lookup table. And those lilac bars? A recipe card: what got
      mixed, never why the recipe was chosen. The choosing lives upstream, in
      the scoring that learned to build those numbers. This is what the
      intern implemented, and it worked on the first try. The curve from the
      opening completes: the rescue line draws in flat.
    visual: >-
      [visual: connect | connect-to-reality] THE morph of the session. The
      frozen machine stands as three columns (amber probe, periwinkle keys,
      cream cards). The beat-04a dict code well slides in beside it. Three
      seconds of silence on the prediction card. Then each dict row
      physically morphs into its attention row, one at a time: exact match
      stretches into a continuous score bar; the single returned value fans
      into a weighted blend; the KeyError row dissolves as the weights
      spread. The sentence trues up on screen, freehand to exact, mint glow
      on the final word: "Attention is a soft lookup table." Then the hook's
      BLEU curve returns and the rescue line draws in flat above the
      collapse, redrawn from the verified Figure 2 and Table 1 (17.82
      against 26.75 on long sentences). Page aside carries the RNNSearch
      naming recollection; video narration stays on the mechanism.
    tracks: [video, page]
    newIdea: >-
      The blending machine is a dictionary with the hardness removed, and the
      identity is checkable row by row.
    novelElements:
      - the aha sentence true-up
      - the rescue line
    onScreenText:
      - "Attention is a soft lookup table."
      - "17.82"
      - "26.75"
    colors:
      query: data.heat
      keys: data.observed
      values: data.truth
      weights: data.params
      ahaTrueUp: data.fit
      rescueLine: data.observed
      background: bg
      labels: text
    predictionPrompt:
      prompt: "You have seen this shape before. Where?"
    majorReveal: true
    misconceptionBeat: true
    misconception: attention-weights-are-explanations
    estimatedSeconds: 55
  - id: beat-06a
    title: Written small
    narration: >-
      Everything you just watched, written small. Weights times values,
      summed: that's the blend. The weights: softmax of the scores. It's the
      exponentiate and normalize you already did. Smooth argmax, picks the
      winner? No. Cat got point seven seven, not one, and kitten is
      measurably in the answer. Nothing was discarded. Now that square
      root's bill. Wide vectors make big dot products, big scores freeze
      softmax near one hot, where the slope is nearly zero. Divide by the
      square root of the width: same preference, living gradient. Which
      keeps learning healthy, probably. The authors themselves wrote, we
      suspect.
    visual: >-
      [visual: symbol-sense] The fade, shown: the bars and cards morph INTO
      the symbols that name them. The formula assembles term by term,
      spatially attached to its objects: the amber q lifts off the probe, K
      off the periwinkle keys, the softmax expression wraps the lilac
      weights, V off the cream cards; sqrt(d_k) docks under the score term
      as the 1.41 bookkeeping comes due. A width dial demonstrates the debt:
      at width 64 typical scores hit 8, softmax at 8 versus minus 8 reads
      0.9999997, the slope readout collapses; divide by 8 and the same
      preference breathes. The completed formula trues up as a whole, mint
      glow, one time.
    tracks: [video, page]
    newIdea: >-
      The formula softmax(q K^T / sqrt(d_k)) V is the soft lookup written
      small, term by term.
    novelElements:
      - the assembled formula
      - the name softmax
    onScreenText:
      - "softmax(q K^T / sqrt(d_k)) V"
      - "0.9999997"
    colors:
      query: data.heat
      keys: data.observed
      weights: data.params
      values: data.truth
      truedFormula: data.fit
      background: bg
      labels: text
    misconceptionBeat: true
    misconception: softmax-picks-the-max
    estimatedSeconds: 40
  - id: beat-06b
    title: Sharpen it until the dictionary comes back
    narration: >-
      The sentence is a claim. Try to break it. Multiply every score by
      twenty. What do the weights become? One, zero, zero, zero, to eight
      decimals. The hard dictionary, back on screen. And right there the
      gradient dies: the slope is weight times one minus weight, nothing at
      one or zero. Quick honesty: the sharpening dial is softmax's, not the
      transformer's. Its fixed cousin is that square root. And 2014 scored
      with a tiny network, not dot products. Those came later. The hard
      lookup was never wrong. It was unlearnable. Gradient flows only while
      the lookup stays soft.
    visual: >-
      [visual: dynamic-process | generalize] A sharpening dial multiplies
      the scores: at 5x the lilac weights read 0.9992 and 0.0008; at 20x
      they read 1, 0, 0, 0 to eight decimal places and the literal hard dict
      from beat-04a returns on screen, exact. The gradient meter attached
      since beat-04a rolls to zero as w(1 - w) collapses; no rose is spent
      here, the numbers alone carry the death. The honesty callouts land as
      two one-line page-style captions in periwinkle mono; full lineage
      lives on the page.
    tracks: [video, page]
    newIdea: >-
      The hard lookup is the sharp limit of the soft one, and the gradient
      dies exactly at that limit.
    novelElements:
      - the sharpening dial
      - the gradient factor w(1 - w)
    onScreenText:
      - "x 20"
      - "1.000  0.000  0.000  0.000"
      - "w(1 - w) -> 0"
    colors:
      weights: data.params
      hardDict: data.observed
      background: bg
      labels: text
    predictionPrompt:
      prompt: "Multiply every score by twenty. What do the weights become?"
      expectedWrongAnswer: >-
        Roughly the same four proportions, since softmax normalizes
        everything anyway.
    majorReveal: true
    estimatedSeconds: 40
  - id: beat-07
    title: Same skeleton, opposite hardness
    narration: >-
      New test: the thing you run at work. RAG. Embed the question: a query
      vector. Compare against a vector index: keys. Fetch passages: values.
      Same skeleton. The differences are the lesson. RAG's lookup is hard
      and external, a top k you can't backprop through. Attention's is soft,
      internal, learned end to end. Opposite ends of one dial. Chat models
      also mask future keys before the softmax. Otherwise, the same machine.
      Now the thought you've been holding. Forty percent of the attention
      went to terrible, so terrible is forty percent of why the review read
      negative. True or false? In 2019, on BiLSTM classifiers, not
      transformers, very different attention maps produced the same
      predictions and matched other importance measures only weakly. Still
      unresolved. A heatmap is a recipe: what got mixed, never why. Same
      skeleton, opposite hardness.
    visual: >-
      [visual: generalize | dynamic-concept] Two-column alignment table,
      attention left, RAG right, rows lighting pairwise: amber query beside
      embedded question, periwinkle keys beside the vector index, cream
      value cards beside fetched passages. The table appears with blanks
      first and holds four seconds for the learner to map it. A single
      hard-soft dial renders both machines as one axis with RAG and
      attention at opposite ends; a one-line causal mask caption sits under
      the attention column. Then the dual-heatmap morph: two visibly
      different lilac weight maps over the same review collapse into the
      same output bar; the false explanation sentence gets crossed out in
      rose, the session's second and final rose spend. The beat-06a formula
      persists in the corner; RAG's top-k pointer taps the softmax term it
      replaces.
    tracks: [video, page]
    newIdea: >-
      RAG runs the same three-object lookup skeleton at the opposite end of
      the hard-soft dial, which is also why weights are plumbing, not
      reasons.
    novelElements:
      - the RAG pipeline column
      - the hard-soft dial
      - the dual heatmap pair
    onScreenText:
      - "query  keys  values"
      - "top-k"
      - "hard, external"
      - "soft, internal"
    colors:
      query: data.heat
      keys: data.observed
      values: data.truth
      weights: data.params
      crossOut: data.error
      background: bg
      labels: text
    predictionPrompt:
      prompt: >-
        Forty percent of the attention went to the word "terrible", so
        "terrible" is forty percent of why the review read negative. True or
        false?
      expectedWrongAnswer: "True."
    majorReveal: true
    estimatedSeconds: 60
  - id: beat-08
    title: What a dictionary cannot know
    narration: >-
      Rebuild it from memory: three objects, two operations. What replaced
      the exact match, and what replaced returning one value? While you
      think, the stored pairs shuffle. The weights follow. The output
      doesn't move a digit. Dictionaries don't know order. Neither does
      attention. The cat sat on the mat. The mat sat on the cat. Same cards,
      same blend. Your language tells them apart. This machine can't. For
      the walk home: what's the cheapest thing you could add to a token so
      that where it sits becomes something a lookup can find? Two years
      later, Google Translate went neural: half a billion users. Three years
      later, Vaswani and colleagues kept only the fix. The fix outlived the
      architecture it rescued. That amber dot was Bahdanau's gaze. Session
      two gives it the one thing it still lacks: where the words sit.
    visual: >-
      [visual: dynamic-process | connect-to-reality] The key-value pairs
      permute; the lilac weights shuffle with them; the mint output chip's
      digits stay frozen, held long enough to be believed, wordless under
      the retrieval prompt. The two cat-mat sentences render as identical
      token bags: same cards, different sentences. The closing card in brand
      microcopy: "For the walk home: how does order get in?" A quiet chip
      gestures at the extensions menu ("Still up?") on the page. The stakes
      sequence reuses the beat-01 chip pattern: a timeline chip ticks
      "+2 years" (GNMT, Sep 2016) with "500M users" and "100B words a day"
      readouts, then "+3 years" (Transformer, 2017) as the recurrent network
      dissolves and only the attention block stays lit. Reserved for the
      final sentence alone: the amber gaze dot from beat-01 hops once more
      between source and target rows, then parks on the unanswered question.
    tracks: [video, page]
    newIdea: >-
      Attention is order-blind the way a dictionary is, and language is not.
    novelElements:
      - the shuffle permutation
      - the identical token bags
    onScreenText:
      - "For the walk home: how does order get in?"
      - "Still up?"
      - "+2 years  GNMT  Sep 2016"
      - "500M users  100B words a day"
      - "+3 years  Transformer  2017"
    colors:
      keys: data.observed
      values: data.truth
      weights: data.params
      output: data.fit
      gazeDot: data.heat
      closingCard: brand.periwinkle
      background: bg
      labels: text
    estimatedSeconds: 55
--- END storyboard.yaml ---

--- BEGIN script.md ---
# Script: attention

Final video narration, one section per storyboard beat, ElevenLabs Matilda
at roughly 150 wpm. Narration paragraphs are the spoken words, TTS-safe:
no em-dashes, no emojis, numbers written the way they should be said when
the spoken form matters. `[visual:]` paragraphs are cue lines keyed to the
storyboard's TEAMAT roles; they are directions, not speech.

## beat-01: The box that broke translation

[visual: connect-to-reality] Title card per brand spec: lit window blooms on the 10pm Sky, title "How Do You Take a Gradient Through a Choice?" in cream, freehand underline trues with mint glow exactly on the first narrated syllable.

In 2014, the best neural translator on Earth worked like this: read the whole sentence, squeeze everything you understood into one fixed list of 8,000 numbers, then write the translation from that list alone. Every sentence got the same box. "The cat sat." 8,000 numbers. A sixty word contract clause with three nested caveats. The same 8,000 numbers.

[visual: connect-to-reality] A sentence funnels into a literal box labeled "8,000 numbers"; a short sentence and a sixty word clause squeeze into the same box. The degradation curve draws itself: BLEU against sentence length, only the collapsing line; the axes hold on screen, unresolved, half the frame deliberately empty.

You can guess what the data showed: translation quality fell apart as sentences got longer. And the fix that actually shipped is my favorite desperate hack in the history of the field. They fed the sentence in backwards. That's it. Reverse the input, and a single LSTM's BLEU score jumped from 25.9 to 30.6. The model is like, wow, what if the first words were just... closer. And it worked. That's the uncomfortable part. It worked, and it changed nothing, because the box was still a box.

[visual: dynamic-process] The reversal hack plays: the sentence physically flips end to end while the BLEU readout ticks from 25.9 to 30.6. A timeline chip places Sep 1 before Sep 10.

So the field kept squeezing. And an intern in Montreal decided to stop.

[visual: connect-to-reality] The gaze image: source row above, target row below, one amber dot hopping between them as a translator's eyes would. The amber dot is the series' query color, planted a minute before anything names it.

The intern was Dzmitry Bahdanau, five weeks left in Yoshua Bengio's Montreal lab. By his own account, the idea came from watching his own eyes: when you translate, your gaze hops back and forth between the source and the line you're writing. Keep every word, and for each word the model writes, let it look back. So why did nobody just build it?

## beat-02: Looking is choosing

[visual: dynamic-concept] A selector arm hovers over the source words. Parameters nudge: the arm holds perfectly still. Nudge again: it slams to a different word with no in-between.

Here's the trap. To look back, the model has to decide where, and where is a choice. This word, not that one. Watch what a choice does to learning. Nudge the parameters. The selector arm doesn't move. Nudge again. It slams to a different word.

[visual: covary] A step function draws itself in periwinkle under the arm as it moves: flat, cliff, flat, a staircase with slope zero on every tread. The organizer question lands as a pause card while the staircase holds.

Flat, cliff, flat. The slope is zero everywhere you can stand, and training means following slopes. Here's the question of the night: how do you learn where to look? Take ten seconds before we go on. Wrong guesses count double. Gradients need a slope, and a choice is a cliff.

## beat-03: One query, asked of every key

[visual: covary | dynamic-concept] PLACED ASSET, verbatim: the PASSED qk-similarity beat. Freeze frame before the sweep carries the prediction card. One amber query vector q sweeps; four periwinkle keys hold still; lilac score bars rise and die with alignment, live.

Strip it to the smallest piece. Forget translation. You're mid sentence and you need cat flavored information. One probe vector, four stored candidates. Before it moves, call the order the bars will peak.

A query is a question you ask every key at once. Sweep it across the row and each dot product answers out loud: point the same way and the score climbs, point away and it dies.

[visual: dynamic-concept] After the sweep the keys take names at the dossier coordinates: cat, kitten, car, sofa. q parks at cat's direction; raw scores land as integers on the bars: 4, 2, 0, -4. Then one pre-formal annotation in periwinkle mono italic: "q . k". Labels on objects; no legends.

The candidates take names: cat, kitten, car, sofa. Park the probe near cat: four, two, zero, minus four. Then a high score means two tokens are the same kind of thing, right? But the keys never moved. Every score rose and died with the probe's direction alone. Alignment in a learned space, not sameness. Alignment is the score. Your hands already know it.

## beat-04a: The perfect answer that learns nothing

[visual: dynamic-process] Cream value cards clip onto the keys, characterized before anything interacts. The score-then-pick machine runs once: cat's bar wins, cat's card slides out.

Each key now carries a card, the content it hands over when found. The obvious machine: score every key, take the winner, return its card. Cat wins. Correct.

[visual: connect] The picture rearranges into two columns, keys left, cards right, and holds a beat so the learner recognizes the dict before any label says so. The code well appears: d["cat"] returns instantly; d["feline"] dies in a rose KeyError.

Rearrange it: keys left, cards right. You know this object: a Python dict. Ask for cat, instant answer. Ask for feline, KeyError, one synonym from a key it's literally holding. Our version scores the near miss, kitten earned a two, and the pick just shrugs: kitten, noted... anyway, one hundred percent cat.

[visual: dynamic-process] A gradient meter attaches to the output. The query wiggles: bars shiver, winner holds, output frozen, meter flatlines in rose. This composite is the session's first of two rose spends. A larger push teleports the output card; the beat-02 staircase redraws under the toy with the actual scores on its treads. P3 pause card: "Keep the ranking. Lose the cliff. What is the smallest edit you can make?"

Try to learn with it. Wiggle the query. Winner unchanged, output unchanged, gradient zero. Push further and the output teleports. The staircase is back, with numbers. That's not a failure of effort. It's the shape of the function. Keep the ranking. Lose the cliff.

## beat-04b: Never choose

[visual: covary] The lilac bars morph from winner-take-all to proportions: scores shrink by 1.41, exponentiate, normalize; the weights land as 0.766, 0.186, 0.045, 0.003. The value cards pour into one mint output chip reading [0.912, 0.083].

Never choose. Give every card partial credit in proportion to its score. One piece of bookkeeping first: shrink the scores by the square root of the vector length, one point four one here. That bill comes due in two minutes. Exponentiate, so nothing's negative. Divide by the sum, so they total one. Blend the cards in those proportions. Mostly cat, a real slice of kitten, almost nothing else.

[visual: dynamic-process] The query wiggles: weights slide smoothly, the output chip drifts smoothly, the gradient meter wakes. The lilac weight bars settle over the four tokens and hold: the frame is now structurally an attention heatmap, though nothing on screen says so.

Wiggle the query. Weights slide, output slides, the meter is alive. Wait. You know these bars. Point seven seven on cat, so cat is seventy seven percent of the why. Right? Hold that thought. The lookup didn't fail to answer. It failed to learn.

## beat-05: You have built this before

[visual: connect] The frozen machine stands as three columns: amber probe, periwinkle keys, cream cards. The beat-04a dict code well slides in beside it. Three seconds of silence on the prediction card.

Freeze the machine. Three columns: the thing you ask with, the things stored under labels, the things handed back. You have seen this shape before. Where?

[visual: connect] THE morph of the session: each dict row physically becomes its attention row, one at a time. Exact match stretches into a continuous score bar; the single returned value fans into a weighted blend; the KeyError row dissolves as the weights spread. The sentence trues up on screen, freehand to exact, mint glow on the final word.

The dict from earlier slides in beside it. Exact match becomes a continuous score. Return one value becomes return a blend. KeyError becomes impossible: the weights just spread. Row by row, the dict you use every day becomes the machine you just built. Attention is a soft lookup table. And those lilac bars? A recipe card: what got mixed, never why the recipe was chosen. The choosing lives upstream, in the scoring that learned to build those numbers.

[visual: connect-to-reality] The hook's BLEU curve returns and the rescue line draws in flat above the collapse, redrawn from the verified Figure 2 and Table 1. The 17.82 and 26.75 readouts sit on their curves. A page aside carries the RNNSearch naming recollection.

This is what the intern implemented, and it worked on the first try. The curve from the opening completes: the rescue line draws in flat.

## beat-06a: Written small

[visual: symbol-sense] The fade, shown: bars and cards morph INTO the symbols that name them. The formula assembles term by term, spatially attached to its objects: amber q lifts off the probe, K off the periwinkle keys, the softmax expression wraps the lilac weights, V off the cream cards; sqrt(d_k) docks under the score term as the 1.41 bookkeeping comes due.

Everything you just watched, written small. Weights times values, summed: that's the blend. The weights: softmax of the scores. It's the exponentiate and normalize you already did. Smooth argmax, picks the winner? No. Cat got point seven seven, not one, and kitten is measurably in the answer. Nothing was discarded.

[visual: dynamic-process] A width dial demonstrates the debt: at width 64 typical scores hit 8; softmax at 8 versus minus 8 reads 0.9999997 and the slope readout collapses; divide by 8 and the same preference breathes. The completed formula trues up as a whole, mint glow, once.

Now that square root's bill. Wide vectors make big dot products, big scores freeze softmax near one hot, where the slope is nearly zero. Divide by the square root of the width: same preference, living gradient. Which keeps learning healthy, probably. The authors themselves wrote, we suspect.

## beat-06b: Sharpen it until the dictionary comes back

[visual: dynamic-process] A sharpening dial multiplies the scores: at 5x the lilac weights read 0.9992 and 0.0008; at 20x they read 1, 0, 0, 0 to eight decimal places and the literal hard dict from beat-04a returns on screen, exact. The gradient meter rolls to zero as w(1 - w) collapses. No rose spend; the numbers carry the death.

The sentence is a claim. Try to break it. Multiply every score by twenty. What do the weights become? One, zero, zero, zero, to eight decimals. The hard dictionary, back on screen. And right there the gradient dies: the slope is weight times one minus weight, nothing at one or zero.

[visual: generalize] The honesty callouts land as two one-line captions in periwinkle mono; the full lineage story lives on the page.

Quick honesty: the sharpening dial is softmax's, not the transformer's. Its fixed cousin is that square root. And 2014 scored with a tiny network, not dot products. Those came later. The hard lookup was never wrong. It was unlearnable. Gradient flows only while the lookup stays soft.

## beat-07: Same skeleton, opposite hardness

[visual: generalize] Two-column alignment table, attention left, RAG right, rows lighting pairwise: amber query beside embedded question, periwinkle keys beside the vector index, cream value cards beside fetched passages. The table appears with blanks first and holds four seconds for the learner to map it.

New test: the thing you run at work. RAG. Embed the question: a query vector. Compare against a vector index: keys. Fetch passages: values. Same skeleton. The differences are the lesson. RAG's lookup is hard and external, a top k you can't backprop through. Attention's is soft, internal, learned end to end. Opposite ends of one dial. Chat models also mask future keys before the softmax. Otherwise, the same machine.

[visual: dynamic-concept] The hard-soft dial renders both machines on one axis, RAG and attention at opposite ends; a one-line causal mask caption sits under the attention column. Then the dual-heatmap morph: two visibly different lilac weight maps over the same review collapse into the same output bar; the false explanation sentence gets crossed out in rose, the session's second and final rose spend. The beat-06a formula persists in the corner; RAG's top-k pointer taps the softmax term it replaces.

Now the thought you've been holding. Forty percent of the attention went to terrible, so terrible is forty percent of why the review read negative. True or false? In 2019, on BiLSTM classifiers, not transformers, very different attention maps produced the same predictions and matched other importance measures only weakly. Still unresolved. A heatmap is a recipe: what got mixed, never why. Same skeleton, opposite hardness.

## beat-08: What a dictionary cannot know

[visual: dynamic-process] The key-value pairs permute; the lilac weights shuffle with them; the mint output chip's digits stay frozen, held long enough to be believed, wordless under the retrieval prompt.

Rebuild it from memory: three objects, two operations. What replaced the exact match, and what replaced returning one value? While you think, the stored pairs shuffle. The weights follow. The output doesn't move a digit. Dictionaries don't know order. Neither does attention.

[visual: connect] The two cat-mat sentences render as identical token bags: same cards, different sentences. The closing card in brand microcopy: "For the walk home: how does order get in?" A quiet chip gestures at the extensions menu ("Still up?") on the page.

The cat sat on the mat. The mat sat on the cat. Same cards, same blend. Your language tells them apart. This machine can't. For the walk home: what's the cheapest thing you could add to a token so that where it sits becomes something a lookup can find?

[visual: connect-to-reality] The stakes sequence reuses the beat-01 chip pattern: a timeline chip ticks "+2 years" (GNMT, Sep 2016) with "500M users" and "100B words a day" readouts, then "+3 years" (Transformer, 2017) as the recurrent network dissolves and only the attention block stays lit. Reserved for the final sentence alone: the amber gaze dot hops once more between source and target rows, then parks on the unanswered question.

Two years later, Google Translate went neural: half a billion users. Three years later, Vaswani and colleagues kept only the fix. The fix outlived the architecture it rescued. That amber dot was Bahdanau's gaze. Session two gives it the one thing it still lacks: where the words sit.
--- END script.md ---
