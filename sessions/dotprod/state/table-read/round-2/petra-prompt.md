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

## Severity calibration (learned at M6; binding)

`blocking` means: shipping this would MISTEACH (a learner walks away with a
wrong or missing core idea) or violates a DOCTRINE NON-NEGOTIABLE outright.
Everything that would merely make good teaching better (a cut where a morph
would be stronger, a livelier close, tighter staging) is `advisory`, however
strongly you feel about it. Two consistency duties: (1) report EVERY
blocking finding you can see in ONE pass; never hold one back for a later
round; (2) when the TASK block includes prior-round reports, do not upgrade
a finding a prior Petra rated advisory unless the artifact CHANGED in a way
that made it worse; note explicitly when you disagree with a prior severity
instead of silently re-rating.

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

## TASK (S3 storyboard + script review, table-read round 2)

You are reviewing the REVISED S3 artifacts of the Night School session "dotprod" (round 2 of the table-read). Below: the R1-R30 digest, spine.md, storyboard.yaml, script.md, then the prior round's Petra report and the Showrunner's dispositions of those findings (yours only; you never see other critics' verdicts). Apply your severity-calibration duties on prior-round reports. The mechanical linters (L1-L12, V1) have already passed. Emit ONLY the JSON array of your output contract. No code fences, no commentary: raw JSON. An empty array is a pass. Do not use any tools; everything you may see is in this message.

--- BEGIN digest: learning-science-rules.md ---
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
--- END digest ---

--- BEGIN spine.md ---
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
--- END spine.md ---

--- BEGIN storyboard.yaml ---
# Storyboard: dotprod (S3, schema v2). The per-beat contract for the M6
# round-trip testbed session, "the dot product as similarity". Authored and
# locked 2026-07-04 as the M6 seed; Phase 3 spine rewrite 2026-07-05 put the
# session on a single walked thread (songs and taste), moved the job-posting
# aside into the new consolidation beat (beat-05), and declared the `thread`
# block that L12 enforces.
# Narration here matches script.md exactly; the script adds the [visual:]
# cue timeline per beat. Timing budgeted at ~150 spoken wpm.
schemaVersion: 2
session: dotprod
aha: "The dot product is a similarity meter."
openingQuestion: "How do you score a match between two lists of numbers?"
closingRetrievalPrompt: >-
  Rebuild the meter from memory: two arrows go in, so what two operations
  turn them into the score?
breadcrumbQuestion: >-
  What is the cheapest fix that keeps the direction and forgets the size?
extensionsMenuRef: extensions.yaml
thread:
  threadExample: songs and your taste
  asideExample: a job posting
  asideKeywords: [job, resume, role, posting, hiring, fit]
  consolidationBeat: beat-05
notationSchedule:
  - symbol: a . b
    referent: the multiply-and-add score
    firstManipulatedBeat: beat-02
    firstSymbolicBeat: beat-03
beats:
  - id: beat-01
    title: The score behind the song
    narration: "Say your music app plays you a song you love, by a band you have
      never heard of. Two descriptions get compared in a data center and the
      verdict comes back: same taste. But weigh what that comparison has to do.
      A song is not one number. It is loud, fast, sad, bright, many qualities at
      once, and your taste is that same tangle. No single ruler works here,
      because the ruler that measures loud says nothing about sad. And waiting
      for two tangles to agree on every quality at once is a lottery you would
      never win, so the comparison needs a principled way to collapse many
      measurements into one. So try it first. How would you boil the match
      between two many-featured things down to a single number? Harder than it
      sounds. One answer to it runs half of modern machine learning."
    visual: "[visual: connect-to-reality] Two tall stacks of qualities slide in
      side by side, one for the listener's taste and one for the song, each row
      a named feature in periwinkle: loud, fast, sad, bright, and more trailing
      off the frame. A short cream ruler lays against one row at a time and
      never spans the stack, and a run of exact-match ticks flickers out as
      rows refuse to agree. A single lilac match readout waits with a question
      mark where its number should be. The question card holds over the
      unfilled readout, half the frame deliberately empty so the puzzle, not an
      answer, owns the screen."
    tracks:
      - video
      - page
    newIdea: Collapsing two many-featured things into a single match number is a
      genuine puzzle, and it is what recommendation runs on.
    novelElements:
      - the two many-featured descriptions
      - the single match readout
    onScreenText:
      - How would you score the match?
    colors:
      lists: data.observed
      score: data.params
      background: bg
      labels: text
    majorReveal: false
    misconceptionBeat: false
    estimatedSeconds: 58
  - id: beat-02
    title: Turn the probe and feel it
    narration: "You just tried to score that match by hand, and it fought back.
      Add everything up and loudness wins, not agreement. Count exact matches
      and nothing ever matches. Here is the move that lands it. A taste is an
      arrow: each direction is one quality, and the length is how hard the song
      leans that way. The recipe is almost embarrassingly small. Multiply the
      two arrows entry by entry, then add. If your taste is two and one, and a
      song is one and three, that is two times one plus one times three: five.
      One number, the whole tangle collapsed. Now meet the instrument. One
      probe arrow, the thing doing the asking. Four candidates, holding still,
      and under each candidate a bar showing its current score. Before
      anything moves, call your shot, and
      make it one the sweep can prove wrong: as the probe turns, does any score
      go negative? Now the sweep, and everything on screen is frozen except the
      probe. As the probe turns toward a candidate, that bar climbs. As it
      turns away, the bar dies. The candidates never moved, so direction is the
      only thing the score can be reading. So a big score means two songs are
      the same, right? Now watch what length does. One candidate stretches
      longer, direction pinned, and its bar climbs anyway, on length alone,
      even though its direction never got closer. The score reads agreement of
      direction, not sameness, and a long arrow can fake a high number."
    visual: "[visual: covary | dynamic-concept] The stacked lists of qualities
      from the hook fold down, each feature becoming one direction, until each
      song is a single arrow. All arrows use thin exact strokes with arrowheads
      sized in proportion to shaft length; the amber probe's head is drawn to
      the same proportion as the candidates', never bloated or malformed. The
      recipe lands first as a tiny worked chip: two short columns, two and one
      against one and three, products pooling into a single lilac five. Then
      the instrument assembles: one amber probe arrow, four periwinkle
      candidate arrows holding still, and under each candidate a lilac score
      bar with a small mono numeric readout. Each candidate label, and the
      'probe' label, sits nudged clear of every arrow so nothing ever collides,
      staying readable at every probe angle including when the probe passes
      candidate B. A freeze frame before the sweep carries the prediction card
      asking whether any score goes negative; then the probe sweeps through
      directions while everything else holds frozen, each bar climbing and
      dying as the probe turns toward and away from its candidate, and the four
      scores land as integers on the bars. Last, candidate c1 stretches longer
      while its direction holds pinned and its score climbs on length alone; on
      the page, c1 carries a length handle so the learner can drive the stretch
      by hand."
    tracks:
      - video
      - page
    newIdea: "Multiply pairwise and add: the score climbs with the probe's
      direction, so agreement is not identity, and stretching a candidate climbs
      the score on length alone, so size can fake it."
    novelElements:
      - the probe arrow
      - the candidate arrows
      - the score bars
      - the candidate length handle
    onScreenText:
      - probe
      - candidates
      - "2 x 1 + 1 x 3 = 5"
      - "3  2  0  -2"
    colors:
      probe: data.heat
      candidates: data.observed
      scores: data.params
      background: bg
      labels: text
    interactiveSpec: page/interactives/dot-alignment.yaml
    predictionPrompt:
      prompt: "Before anything moves, call your shot, and make it one the sweep
        can prove wrong: as the probe turns, does any score go negative?"
      expectedWrongAnswer: "No score ever goes negative, because a similarity
        cannot be less than zero."
    majorReveal: false
    misconceptionBeat: true
    misconception: similarity-means-identical
    estimatedSeconds: 100
  - id: beat-03
    title: Name the machine you just used
    narration: "Look at what your hands just learned. Point the probe along a
      candidate and the sum climbs. Point it across and the sum dies to zero.
      Point it against and the sum goes negative. One multiply and add, and it
      behaves like a meter with agree, ignore, and oppose on the dial. So say it
      plainly: the dot product is a similarity meter. Two lists of numbers go
      in. One honest reading of alignment comes out. And the reading tracks
      direction, because direction is all the sweep ever changed."
    visual: "[visual: connect | symbol-sense] The three probe positions replay as
      stills: along, across, against, each with its frozen score. The stills
      collapse into one lilac meter dial whose needle swings from oppose through
      ignore to agree as the probe sweep replays. The aha sentence trues up on
      screen, freehand to exact with a mint glow. A small lilac mono annotation,
      a . b, sits on the score readout."
    tracks:
      - video
      - page
    newIdea: "The multiply-and-add score behaves like a meter for alignment: agree
      positive, across zero, oppose negative."
    novelElements:
      - the meter dial
      - the annotation a . b
    onScreenText:
      - a . b
      - agree  ignore  oppose
      - The dot product is a similarity meter.
    colors:
      probe: data.heat
      candidates: data.observed
      meter: data.params
      annotation: data.params
      ahaTrueUp: data.fit
      background: bg
      labels: text
    majorReveal: true
    misconceptionBeat: false
    estimatedSeconds: 36
  - id: beat-04
    title: Back to the data center
    narration: "Time to close the loop. Rebuild the meter from memory: two arrows
      go in, and which two operations turn them into a single score? Hold your
      answer while the opening scene comes back. Your app played you a
      stranger's song and called it your taste. You know what that took now.
      Your taste is the probe. The catalog is a shelf of candidates, thousands
      of arrows long. And the machine in the data center is the thing you just
      built, running multiply-and-add a few million times and handing you the
      top bar. That was the whole mystery: your meter, at scale."
    visual: "[visual: connect | connect-to-reality] The retrieval card holds the
      compressed question while the meter idles. Then the hook's frame returns:
      the two tall stacks from beat-01 stand beside the arrows they folded
      into, the amber probe takes the label 'your taste', and the candidate row
      extends into a long periwinkle catalog shelf running off frame, arrows
      all the way down. Score bars rank themselves under the shelf, the top bar
      slides forward as the played song, and the data center readout from the
      opening fills its question mark with the winning score."
    tracks:
      - video
      - page
    newIdea: "The recommendation from the hook is this same meter at catalog
      scale: your taste is the probe and every song on the shelf is a
      candidate."
    novelElements:
      - the catalog shelf
    onScreenText:
      - Rebuild the meter from memory. Which two operations?
      - your taste
      - the catalog
    colors:
      probe: data.heat
      candidates: data.observed
      score: data.params
      background: bg
      labels: text
    majorReveal: false
    misconceptionBeat: false
    estimatedSeconds: 40
  - id: beat-04b
    title: The honest look
    narration: "Now the honest look, and guess before you watch. You saw length
      raise the score. But by how much? Double c1's length exactly, same
      direction, just twice as long: does the score double exactly, or just
      drift up? It doubles, exactly. Four point two becomes eight point four,
      to the last digit. Double one input, double the output: the meter is
      linear in each arrow you feed it. That clean scaling is the crack. A loud
      song wins on sheer loudness, whether or not the taste underneath agrees,
      because size passes straight through the arithmetic."
    visual: "[visual: dynamic-process] A guess card holds with candidate c1
      outlined and its score readout hidden; the card carries no header and
      poses the doubling question directly, asking whether the score doubles
      exactly or just drifts up. Then the periwinkle candidate doubles in
      length while its direction holds still; its lilac score reads out at
      exactly twice its former value, the two numbers stacked with no header so
      the stacked 4.2 / x2 / 8.4 stands as the reveal itself; a small rose flag
      marks that size passed straight through, and a long loud candidate's bar
      outranks a better-aligned short one while both stay on screen."
    tracks:
      - video
      - page
    newIdea: The meter is linear in each input, so doubling one arrow exactly
      doubles the score, and that clean scaling is the crack the cheapest fix
      will exploit.
    novelElements:
      - the doubled arrow
      - the unearned-win flag
    onScreenText:
      - Double c1. Same direction. Exactly double, or just up?
      - "4.2  x2  8.4"
    colors:
      candidates: data.observed
      score: data.params
      failureFlag: data.error
      background: bg
      labels: text
    predictionPrompt:
      prompt: "You saw length raise the score, but by how much? Double c1's
        length exactly, same direction: does the score double exactly, or just
        drift up?"
      expectedWrongAnswer: "It just drifts up: stretching one arrow nudges the
        number in some messy way, not a clean doubling."
    majorReveal: true
    misconceptionBeat: false
    estimatedSeconds: 38
  - id: beat-05
    title: Take it with you
    narration: "Take it with you. A song and a taste, folded into arrows,
      collapsed by multiply-and-add into one score: a meter with a crack in it.
      One more aisle, to make sure it lands: score yourself against a job
      posting. Same multiply-and-add, one number for the fit. Now invent your
      own pair. Anything you can describe as two matching lists, the meter can
      score. For the walk home: what is the cheapest fix that keeps the
      direction and forgets the size? Still up? The menu below has three ways
      to keep going."
    visual: "[visual: connect | connect-to-reality] The chain replays as a strip
      of four small stills drawing left to right in reasoning order: the two
      stacked tangles from the hook, the arrows they folded into, the
      multiply-and-add pooling into one score bar, and the meter dial with its
      hairline rose crack. Then a clearly framed aside panel slides in: two
      short columns labeled 'you' and 'the posting', matched entries
      multiplying and pooling into one lilac fit readout on the same dial. The
      aside panel slides out and leaves a pair of blank columns under the
      invitation to invent your own pair; the walk-home question lands as the
      closing card under the 'For the walk home' header, and a quiet chip
      points to the extensions menu below."
    tracks:
      - video
      - page
    newIdea: The meter recipe transfers to any pair of matching feature lists,
      shown once in a second aisle and then handed to the learner to invent
      with.
    novelElements:
      - the recap chain
      - the job-fit columns
    onScreenText:
      - tangle, arrows, multiply-and-add, meter
      - you  vs  the posting
      - invent your own pair
      - For the walk home
      - Keep the direction. Forget the size.
      - Still up?
    colors:
      asideColumns: data.observed
      score: data.params
      crack: data.error
      background: bg
      labels: text
    majorReveal: false
    misconceptionBeat: false
    estimatedSeconds: 36
--- END storyboard.yaml ---

--- BEGIN script.md ---
# Script: dotprod

Final video narration, one section per storyboard beat. Narration
paragraphs are the spoken words, read at roughly 150 words per minute, with
no em-dashes and no emojis. Bracketed `[visual:]` paragraphs are the
video's stage directions: what is on screen while the words are spoken.
Narration matches storyboard.yaml beat for beat, word for word.

## beat-01: The score behind the song

[visual: connect-to-reality] Two tall stacks of qualities slide in side by side, one for the listener's taste and one for the song, each row a named feature in periwinkle: loud, fast, sad, bright, and more trailing off the frame.

Say your music app plays you a song you love, by a band you have never heard of. Two descriptions get compared in a data center and the verdict comes back: same taste. But weigh what that comparison has to do. A song is not one number. It is loud, fast, sad, bright, many qualities at once, and your taste is that same tangle.

[visual: connect-to-reality] A short cream ruler lays against one row at a time and never spans the stack; a run of exact-match ticks flickers out as rows refuse to agree.

No single ruler works here, because the ruler that measures loud says nothing about sad. And waiting for two tangles to agree on every quality at once is a lottery you would never win, so the comparison needs a principled way to collapse many measurements into one.

[visual: connect-to-reality] A single lilac match readout waits with a question mark where its number should be; the question card holds over the unfilled readout, half the frame deliberately empty so the puzzle, not an answer, owns the screen.

So try it first. How would you boil the match between two many-featured things down to a single number? Harder than it sounds. One answer to it runs half of modern machine learning.

## beat-02: Turn the probe and feel it

[visual: dynamic-concept] The stacked lists of qualities from the hook fold down, each feature becoming one direction, until each song is a single arrow; arrowheads stay in proportion to shaft length.

You just tried to score that match by hand, and it fought back. Add everything up and loudness wins, not agreement. Count exact matches and nothing ever matches. Here is the move that lands it. A taste is an arrow: each direction is one quality, and the length is how hard the song leans that way.

[visual: dynamic-process] The recipe lands as a tiny worked chip: two short columns, two and one against one and three, products pooling into a single lilac five.

The recipe is almost embarrassingly small. Multiply the two arrows entry by entry, then add. If your taste is two and one, and a song is one and three, that is two times one plus one times three: five. One number, the whole tangle collapsed.

[visual: dynamic-concept] The instrument assembles: one amber probe arrow, four periwinkle candidate arrows holding still, a lilac score bar with a mono readout under each candidate; every label sits nudged clear of every arrow at every probe angle.

Now meet the instrument. One probe arrow, the thing doing the asking. Four candidates, holding still, and under each candidate a bar showing its current score.

[visual: covary] A freeze frame carries the prediction card asking whether any score goes negative.

Before anything moves, call your shot, and make it one the sweep can prove wrong: as the probe turns, does any score go negative?

[visual: covary] The probe sweeps through directions while everything else holds frozen; each bar climbs and dies as the probe turns toward and away from its candidate; the four scores land as integers on the bars.

Now the sweep, and everything on screen is frozen except the probe. As the probe turns toward a candidate, that bar climbs. As it turns away, the bar dies. The candidates never moved, so direction is the only thing the score can be reading.

[visual: covary] Candidate c1 stretches longer while its direction holds pinned; its score climbs on length alone. On the page, c1 carries a length handle so the learner can drive the stretch by hand.

So a big score means two songs are the same, right? Now watch what length does. One candidate stretches longer, direction pinned, and its bar climbs anyway, on length alone, even though its direction never got closer. The score reads agreement of direction, not sameness, and a long arrow can fake a high number.

## beat-03: Name the machine you just used

[visual: connect] The three probe positions replay as stills: along, across, against, each with its frozen score. The stills collapse into one lilac meter dial whose needle swings from oppose through ignore to agree as the sweep replays.

Look at what your hands just learned. Point the probe along a candidate and the sum climbs. Point it across and the sum dies to zero. Point it against and the sum goes negative. One multiply and add, and it behaves like a meter with agree, ignore, and oppose on the dial.

[visual: symbol-sense] The aha sentence trues up on screen, freehand to exact with a mint glow. A small lilac mono annotation, a . b, sits on the score readout.

So say it plainly: the dot product is a similarity meter. Two lists of numbers go in. One honest reading of alignment comes out. And the reading tracks direction, because direction is all the sweep ever changed.

## beat-04: Back to the data center

[visual: connect] The retrieval card holds the compressed question while the meter idles.

Time to close the loop. Rebuild the meter from memory: two arrows go in, and which two operations turn them into a single score?

[visual: connect-to-reality] The hook's frame returns: the two tall stacks from beat-01 stand beside the arrows they folded into; the amber probe takes the label "your taste"; the candidate row extends into a long periwinkle catalog shelf running off frame; score bars rank themselves and the top bar slides forward as the played song; the data center readout from the opening fills its question mark with the winning score.

Hold your answer while the opening scene comes back. Your app played you a stranger's song and called it your taste. You know what that took now. Your taste is the probe. The catalog is a shelf of candidates, thousands of arrows long. And the machine in the data center is the thing you just built, running multiply-and-add a few million times and handing you the top bar. That was the whole mystery: your meter, at scale.

## beat-04b: The honest look

[visual: dynamic-process] A guess card holds with candidate c1 outlined and its score readout hidden; the card carries no header and poses the doubling question directly.

Now the honest look, and guess before you watch. You saw length raise the score. But by how much? Double c1's length exactly, same direction, just twice as long: does the score double exactly, or just drift up?

[visual: dynamic-process] The periwinkle candidate doubles in length while its direction holds still; its lilac score reads out at exactly twice its former value, the stacked 4.2 / x2 / 8.4 standing as the reveal itself; a small rose flag marks that size passed straight through, and a long loud candidate's bar outranks a better-aligned short one.

It doubles, exactly. Four point two becomes eight point four, to the last digit. Double one input, double the output: the meter is linear in each arrow you feed it. That clean scaling is the crack. A loud song wins on sheer loudness, whether or not the taste underneath agrees, because size passes straight through the arithmetic.

## beat-05: Take it with you

[visual: connect] The chain replays as a strip of four small stills drawing left to right in reasoning order: the two stacked tangles from the hook, the arrows they folded into, the multiply-and-add pooling into one score bar, and the meter dial with its hairline rose crack.

Take it with you. A song and a taste, folded into arrows, collapsed by multiply-and-add into one score: a meter with a crack in it.

[visual: connect-to-reality] A clearly framed aside panel slides in: two short columns labeled "you" and "the posting", matched entries multiplying and pooling into one lilac fit readout on the same dial.

One more aisle, to make sure it lands: score yourself against a job posting. Same multiply-and-add, one number for the fit.

[visual: connect-to-reality] The aside panel slides out and leaves a pair of blank columns under the invitation; the walk-home question lands as the closing card under the "For the walk home" header, and a quiet chip points to the extensions menu below.

Now invent your own pair. Anything you can describe as two matching lists, the meter can score. For the walk home: what is the cheapest fix that keeps the direction and forgets the size? Still up? The menu below has three ways to keep going.
--- END script.md ---

--- BEGIN prior round: Petra report (round 1) ---
[
  {
    "ruleId": "R19",
    "pass": false,
    "severity": "blocking",
    "evidence": "beat-01's narration poses 'How would you boil the match between two many-featured things down to a single number?' but this is the opening organizer question (R16), not a prediction with a checkable wrong answer (R19). There is no expectedWrongAnswer field on beat-01, no falsifiable guess structure, and no sweep/reveal that proves the guess right or wrong. It is rhetorical framing, not a predictive commitment.",
    "suggestion": "Leave beat-01's question as the R16 organizer; do not double-count it as R19. If a prediction is intended here, give it a checkable form (e.g. 'guess: does a simple average of the two lists work as the match score?') with an explicit wrong-answer to falsify at the reveal."
  },
  {
    "ruleId": "R23",
    "pass": false,
    "severity": "advisory",
    "evidence": "beat-03's narration states the conclusion ('the dot product is a similarity meter... the reading tracks direction') immediately after replaying the three probe positions, but the learner-facing connection (naming what the sweep behavior amounts to) is delivered entirely by narration rather than left one step short for the learner. beat-02 already showed the sweep and the length-fake; beat-03's visual ('aha sentence trues up on screen, freehand to exact') has the words appear before the learner is asked to supply the name themselves.",
    "suggestion": "Consider a beat between 02 and 03 (or a pause inside beat-03) where the learner is prompted to name the pattern themselves (e.g. 'What would you call a machine that reads agree/ignore/oppose off direction alone?') before the sentence trues up. This is advisory since the components were genuinely pre-established across beat-02 and the reveal is one step from the learner, not zero, but the sentence lands via narration first rather than a learner-supplied label."
  },
  {
    "ruleId": "R25",
    "pass": false,
    "severity": "advisory",
    "evidence": "beat-01 sets up a genuine struggle framing ('So try it first. How would you boil the match... down to a single number?') but beat-01 ends without ever returning to compare the learner's own attempt against a canonical solution; beat-02 opens with 'You just tried to score that match by hand, and it fought back' which asserts a failed attempt happened rather than showing or resolving one. No bounded struggle segment with explicit comparison of the learner's guess to the canonical answer appears.",
    "suggestion": "This is likely intentional as an R16 organizer rather than an R25 struggle segment (no minutes-long attempt window is implied), but if R25 credit is being claimed for beat-01/02's framing, add an explicit moment contrasting what a naive attempt (e.g. summing raw features, or Euclidean distance) would produce versus the canonical multiply-and-add, rather than only asserting 'it fought back.'"
  },
  {
    "ruleId": "R12",
    "pass": true,
    "severity": "advisory",
    "evidence": "No violation found; noting only that beat-02 introduces the probe, four candidates, and score bars all within one beat before the sweep. Storyboard novelElements lists probe arrow, candidate arrows, score bars, and length handle together as beat-02's novel set (4 items, within the R15 mechanical cap), and narration does characterize probe then candidates then bars in sequence before the sweep interaction begins, so pre-training order is respected. Marked pass explicitly since R15's mechanical count could mask an ordering issue on casual read; on inspection the ordering is sound.",
    "suggestion": ""
  }
]
--- END prior round report ---

--- BEGIN Showrunner dispositions of the round-1 Petra findings ---
R19 (blocking): OVERRULED AS ALREADY SATISFIED, with rationale. No R19
credit is claimed for beat-01's question; it is the R16 organizer exactly
as the finding's own suggestion asks. The beat-03 reveal window is covered
by beat-02's falsifiable predictionPrompt ("does any score go negative?",
expectedWrongAnswer declared), and the beat-04b reveal by its own doubling
prompt. Confirm or dissent against the revised artifact.
R25 (advisory): ACCEPTED in part. The beat-02 struggle recap now names the
two natural attempts and their failure modes ("Add everything up and
loudness wins, not agreement. Count exact matches and nothing ever
matches.") before the canonical recipe lands.
R23 (advisory): OVERRULED with rationale: beat-03 is the locked aha beat
this phase does not touch; the reveal is one step from the learner (the
beat-02 prediction does the connecting). Recorded as a standing note for
the next spine-touch round.
--- END dispositions ---
