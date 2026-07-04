# S2 treatment candidate: metaphor-first

```yaml
candidate: metaphor-first
session: attention
steer: "Kyla mode: domestic recursive metaphor, carried beats 1 through 8, returned to at the close"
hookBasis: "Hook B, the dictionary that fails gracefully (brief.md; dossier section 2, candidate B)"
aha: "Attention is a soft lookup table."
title: "Why can't a dictionary take a hint?"
subtitle: "A recipe box, a KeyError, and the one operation inside every transformer."
coinage: "the forgiving dictionary"
videoTotalSeconds: 490
videoHardCapSeconds: 540
passedAssetsPlaced: ["qk-similarity (beat 3, video)", "qk-explorer (beat 3, page track)"]
status: S2 draft, judge commits
```

Every fact below traces to `dossier.md`; section references are given in the
production notes. All learner-facing prose in this file is dash-free by
construction and stays inside the two licensed humor templates.

---

## 1. The hook, written in full

The first 152 words are the cold open, VERBATIM. Screen shows the kitchen
sketch (freehand, untrued), then the dict literal in a code well; Matilda
speaks the code in plain words ("ask it for cat") while the code sits on
screen, so nothing on screen duplicates narration (L7).

> It's 9pm and you want the lemon thing. Not a recipe with a name. The one
> your roommate made in March, with the too-thick glaze. You pull down the
> recipe box and the tabs stare back: APPLE CAKE. BANANA BREAD. LEMON BARS.
> The box is perfectly organized and completely unhelpful, because a box
> like this only answers questions it has heard before, phrased exactly the
> way it first heard them.
>
> You own the digital version. You used it this week.
>
> Ask a Python dict for `d["cat"]` and the answer comes back before you
> finish blinking. Ask it for `d["feline"]` and the program dies. KeyError.
> One synonym away from a key it's literally holding, and the dict is like
> "...never heard of it."
>
> So here's tonight's question. Could a lookup give partial credit? Ask for
> feline, get back mostly cat, a little kitten, none of carburetor. What
> would that box even look like?

No definitions, no agenda, question before any machinery (L5). The word
"attention" is not spoken, shown, or hinted at until beat 5. That embargo is
this treatment's load-bearing wall: the brief is explicit that if beat 1
says "this is attention," the aha is narrated, not engineered, and the
candidate fails.

---

## 2. Beat list (one new idea per beat, each forcing the next)

| # | Beat | The ONE new idea | How it forces the next beat | Est. sec |
|---|------|------------------|------------------------------|----------|
| 1 | Hook | Exact-match lookup is brittle: everything or nothing, KeyError one synonym away | What would partial credit even mean? | 50 |
| 2 | Gap + prediction | Partial credit needs a per-label NUMBER, not a yes or no | "Close" has to become computable: what object makes it a number? | 40 |
| 3 | Elemental unit | The dot product: alignment of directions IS the score (qk-similarity sweep, qk-explorer) | Now we can score every card, so the obvious move is score-then-pick | 70 |
| 4 | Build & complicate | Score-then-pick (take the max) fails: a choice has no slope, and it discards the runner-up | Stop choosing. What's the only move left? | 75 |
| 5 | The Aha | Blend everything in proportion to its score: the forgiving dictionary works, and its real name is attention. "Attention is a soft lookup table." | The thing deserves to be written down small | 70 |
| 6 | Compression | softmax(qK^T / sqrt(d_k))V read term by term as "the lookup, made soft"; sharpening limit returns the hard dict | The metaphor survived its falsification test; now stress it somewhere else | 70 |
| 7 | Stress-test + 2nd instance | RAG at work is the same skeleton with the dial set to hard; honest edge: the weights are plumbing, not reasons | The tool works and its limits are known; what can it still not do? | 70 |
| 8 | Breadcrumb | The box is order-blind: shuffle the cards, nothing changes; sentences are ordered | Session 2: how do you give a dictionary a sense of order? | 45 |

Total: 490 seconds. Target 480, hard cap 540 (L10 clears with 50s of slack).

---

## 3. The beats, in detail

### Beat 1: The Hook (50s)

**What happens.** The cold open above, verbatim. Kitchen at 9pm, the recipe
box with exact tabs, then the morph to its digital twin: a Python dict in a
code well. `d["cat"]` returns. `d["feline"]` dies in KeyError red. The
session's question is posed and left open.

**Emotional beat.** Fond exasperation into recognition. Every learner in
this audience has been personally insulted by a KeyError.

**Key visuals.** [connect] The freehand recipe box (untrued sketch,
periwinkle line) morphs into the dict code well: same three tabs become
three keys. The KeyError traceback is the beat's single hot moment; rose is
NOT spent here (rationed), error state reads through motion and the
traceback itself. Title card true-up fires on the first narrated syllable
per brand spec.

**Notation timing.** None. Code is shown as code; no math symbols exist yet.

**Predictions / retrievals.** None yet; the question itself is the open
loop (R20: everything that follows lives inside it).

**Humor check.** One template-1 joke (the dict is like "...never heard of
it"). Lands without explanation; deleting it removes the beat's charm but
zero explanation, so it stays only because it carries the brittleness claim
in four words.

### Beat 2: The Gap, and the first prediction (40s)

**What happens.** Hold the broken lookup on screen and write the spec for
the fix, in the learner's own terms. A box with partial credit needs two
things it doesn't have: a NUMBER for how well the question matches each
stored label (all of them, not just the winner), and a rule for what to
hand back when several labels score well. Then the first prediction prompt,
before anything is revealed.

**Emotional beat.** The itch. The gap must feel almost closable, and for
this audience it is: they've met embeddings at work. Many will guess right,
which is the point (pretesting pays either way).

**Key visuals.** [dynamic-concept] The spec written as two empty slots on
the sketched box: "match = ___" and "return = ___". The slots stay visibly
unfilled; beat 3 fills the first, beat 5 fills the second. This two-slot
scaffold is the video's running progress marker, sketched rough now, trued
only when filled.

**Notation timing.** None.

**Predictions / retrievals.** P1 (pause-and-ponder checkpoint): "What kind
of object could make 'close' a number a computer can take? You've probably
met one at work. Guess before we go on." Page track adds a skippable
30-second refresher on dot product geometry here (expertise reversal:
skippable, never forced).

**Landing line.** "Close is not a feeling. Close has to become a number."

### Beat 3: The Elemental Unit (70s)

**What happens.** The reveal of P1: represent the question and the labels
as vectors, direction as meaning. Then play with the one elemental piece,
scoring a single question against stored labels, before anything else is
allowed to happen. The PASSED qk-similarity beat runs here nearly verbatim
(24s): one amber query sweeps; four periwinkle keys hold still; lilac score
bars under each key rise and die with alignment, live. Then the labeled
variant: the abstract keys become cat [2, 0], kitten [1, 1], car [0, 2],
sofa [-2, 0], and the query becomes "feline" at [2, 0]. Raw scores appear
as integers: 4, 2, 0, -4. Misconception 3 is voiced and refuted here (see
section 5). One quiet line seeds beat 7: what counts as similar is not
god-given, the model learns to write its own questions and its own tabs.

**Emotional beat.** Play. Hands-on delight; the mechanism is felt before it
is named.

**Key visuals.** [covary | dynamic-concept] qk-similarity, PASSED, placed
as-is (24s). Then a cheap derivative re-render: same grammar, keys
relabeled with the four tokens and the dossier's exact coordinates, scores
as integer readouts. Colors locked per seed: query amber (data.heat), keys
periwinkle (data.observed), scores lilac (data.params).

**Page track.** qk-explorer, PASSED, embedded twinned to this beat via
`interactiveSpec` (states: initial, mid-drag, aligned-with-k1,
anti-aligned). The learner drags the query and feels alignment become the
score before the video names it. Optional Director extension flagged (new
asset, not assumed): a "pick vs blend" toggle state added at beat 4.

**Notation timing.** During the sweep, only object labels (q, k1..k4 on
their tips) and numeric readouts. The expression "q . k" is written under
the bars only AFTER the sweep completes, as compression of what the bars
just did (L3 clean: manipulation precedes symbol).

**Predictions / retrievals.** P1 resolves at the top of the beat. Medium
inference left to the learner (R22): sofa's score is negative, and nobody
narrates why; the sweep already showed anti-alignment.

**Landing line.** "Alignment is the score. Direction agreeing with
direction, measured."

### Beat 4: Build & Complicate, the felt obstruction (75s)

**What happens.** The natural first fix, tried honestly: score every card,
then take the best one. A "fuzzy lookup" that still returns exactly one
value. It works on screen: feline scores cat highest, cat's card comes
back, no KeyError. Small victory, ten seconds of it. Then it breaks twice,
and the learner watches both breaks happen. Break one: kitten scored 2,
half of cat's 4, real information about what "feline" means, and the pick
throws it away. The pick is like "kitten, noted... anyway, one hundred
percent cat." Break two, the deep one: nudge the query's direction a few
degrees and watch the output. Nothing. Nudge again. Nothing. Then one more
degree and the answer snaps from cat's card to kitten's card, all at once.
Plot output against query angle: a flat line, a cliff, a flat line. This
audience trains models for a living; they know what a flat loss surface
means before Matilda says it. There is nothing here for a gradient to hold
on to. The empathic reframe lands here: that's not a failure of cleverness,
it's the structure of choosing. Discrete choices are cliffs.

**Emotional beat.** Frustration, bounded and legible (R25). The wall is hit
in under a minute and the exit is visible: the problem is the choosing
itself.

**Key visuals.** [dynamic-process] The argmax highlight ring locking onto
cat's card while kitten's respectable bar dims to nothing. Then the nudge
sequence: query rotating in small steps, output bar frozen, then the snap.
[symbol-sense, pre-formal] The step-function plot drawn live, freehand
line, deliberately left untrued: this idea does not deserve the mint glow,
and the motif does the arguing.

**Notation timing.** No new symbols. "Take the biggest" is said in words;
argmax as notation never appears in the video (page callout may name it).

**Predictions / retrievals.** P2, at the moment of maximum reaching, right
at the beat's end: "If choosing is the problem, and the scores are sitting
right there, what's the only move left? Say it out loud. It feels illegal."

**Landing line.** "A choice has no slope."

### Beat 5: The Aha (70s)

**What happens.** The move the learner just named: don't choose. Take every
card, in proportion to its score. Step one, turn scores into shares: shrink
the scores by one bookkeeping factor (divide by the square root of the
vector length, 1.41 here; "the why costs two minutes and we'll pay it
shortly," an honest forward reference), exponentiate, normalize. The four
scores become four shares that sum to one: cat 0.766, kitten 0.186, car
0.045, sofa 0.003. Step two, blend the card CONTENTS by those shares:
0.766 of cat's value plus 0.186 of kitten's plus the dregs. Output:
[0.912, 0.083]. Compare it to cat's stored value [1.0, 0.0]: mostly cat,
measurably kitten, carburetor nowhere. The second slot on the box trues:
"return = the blend." The forgiving dictionary exists, built, working,
still nameless. Misconception 1 is voiced and structurally refuted RIGHT
HERE, before the name reveal (section 5). Then P3: "Three objects. The
question you ask with. The labels you match against. The contents you get
back. You have seen these three words on a diagram at work. Say them."
Beat. The sketched box morphs into the standard attention diagram, labels
truing in mint as they land: query. key. value. And the sentence, spoken
once, plainly: attention is a soft lookup table. You didn't learn it
tonight. You rebuilt it. One honesty line rides the reveal: the names match
how retrieval systems talk, and a whole key-value memory literature grew up
in parallel; nobody built this by porting a database. One more, for the
LLM connection: in the chat models you use at work, each word may only look
backward at earlier words; scores to the future are switched off. Same box.

**Emotional beat.** The snap, then warmth. Danek's stamp: the connection is
the learner's own, because every component was already theirs.

**Key visuals.** [dynamic-process] Bars morphing from raw scores to
normalized shares (heights redistribute, sum-to-one shown as the bars
packing into a single unit-width strip). [connect] Value bars blending into
the output bar next to cat's stored value for comparison. [connect |
generalize] THE true-up of the session: sketch-box to attention diagram,
mint glow exactly on "query, key, value." Brand rule honored: the aha
always executes a true-up.

**Notation timing.** Numbers only (shares as decimals on the bars). The
words query, key, value land as object labels. The formula is still
withheld; it is beat 6's whole job.

**Predictions / retrievals.** P2 resolves in the first ten seconds. P3
(name the three objects) immediately before the reveal, so the learner has
the chance to beat the reveal by one step (R23).

**Landing line.** "Attention is a soft lookup table. You just built it."

### Beat 6: The Compression (70s)

**What happens.** Now, and only now, the notation, presented as shorthand
for the thing on screen. The formula assembles term by term, each symbol
flying to and from its referent: q is the amber question; K is the
periwinkle stack of labels; q K^T is all four scores at once; divide by
sqrt(d_k), the bookkeeping factor from beat 5, now paid for: wide vectors
make big dot products (typical size grows like sqrt of the width; at width
2 typical scores sit near 1.4, at width 64 near 8), and softmax at score 8
versus -8 puts 0.9999997 on the winner, a slope of roughly three in ten
million, a frozen layer. Divide by sqrt(d_k) and the same preference stays
alive: 0.881 versus 0.119, gradient breathing again. Which keeps learning
healthy, probably; the authors themselves wrote "we suspect." Then softmax
gets its name, and misconception 2 is voiced in the learner's own words and
refuted on screen (section 5): the shares 0.766 and 0.186 are both in the
answer; nothing was discarded. Then the falsification test the whole
session owes: sharpen the scores five-fold and the shares go to 0.9992 and
crumbs; twenty-fold and they read 1, 0, 0, 0 to eight decimal places. The
hard dict reappears inside the soft one, KeyError strictness as a limit.
Disclosure, spoken plainly: sharpening is a property of softmax we're using
as a demonstration; the transformer has no temperature knob in this layer,
the sqrt(d_k) divisor is its fixed, principled cousin. And the closing turn
of the beat: at that hard limit the slope dies again, weight times one
minus weight, zero. The box only learns while it stays soft. That is not a
side effect. That is the reason this thing exists.

**Emotional beat.** Competence. The scary formula from work becomes
readable left to right, in one pass, in their own metaphor.

**Key visuals.** [symbol-sense] Term-by-term formula build, color-matched:
q amber, K periwinkle, the softmax output lilac, V and the output vector in
a fourth series color (Director to assign; values currently have no locked
semantic token, flagged as an open brand question). [covary] The sharpening
slider: shares racing to one-hot as the multiplier climbs, the dict's
everything-or-nothing behavior re-emerging live. [connect] The dict
correspondence table from the dossier, drawn row by row, each row truing as
it is verified on screen.

**Notation timing.** First appearance of every math symbol in the session:
q, K, V, softmax, sqrt(d_k), the full Attention(q, K, V) line. Every
referent was manipulated beats 3 through 5 (L3 clean across the board).
The sqrt(d_k) variance demo runs at full depth on the page track as a
no-handwave callout; the video carries the 15-second honest version above.

**Predictions / retrievals.** P4 before the sharpening reveal: "Multiply
every score by twenty. What do the four shares become? Commit to a guess."

**Landing line.** "The formula is the box, written small."

### Beat 7: Stress-test and the second instance (70s)

**What happens.** Two movements. First, the surface-different twin (R28):
RAG, which half this audience runs in production. Your question becomes a
query vector; the index holds key vectors; the retrieved passages are the
values handed back. Side by side with tonight's box, the learner fills the
mapping themselves (the alignment table appears with blanks; medium
inference, ten seconds of silence). Then the differences get named, because
they are the lesson: retrieval does a HARD top-k over an external store,
and no gradient flows through the index; attention does a soft blend over
an internal one, inside every layer, and learns. Same skeleton, opposite
ends of the hard-soft dial. The shared structure gets its name:
similarity-weighted lookup. Second movement, the honest edge, P5 first:
"The model put 40 percent of its attention on 'terrible', so 'terrible' is
40 percent of why it said negative. True or false?" Then the 2019 result,
scope-disciplined: on BiLSTM classifiers (not transformers, and the authors
say so), Jain and Wallace found attention weights frequently uncorrelated
with other importance measures, and found very different attention maps
yielding the same predictions. Same output, contradictory heatmaps. The
field then argued about it for years, and the argument is genuinely
unresolved. But the mechanism-level point needs no experiment, and the
learner now owns it: the weights are the recipe of the blend. They tell you
what got mixed, not why the scoring turned out that way. The why lives
upstream, in the learned maps that write the questions and the tabs. Asking
the shares to justify the answer is asking the plumbing to explain the
house.

**Emotional beat.** Sobriety that reads as respect. The session trusts them
with the fight in the literature instead of a tidy moral.

**Key visuals.** [connect-to-reality | generalize] The RAG pipeline and the
attention box drawn as the same three-object diagram, differences
highlighted at exactly two nodes: hard/soft at the selection step,
external/internal at the store. [dynamic-concept] For the heatmap: two
different lilac weight-maps over the same review morphing into the same
output bar. Rose is spent here, once, on the false explanation being
crossed out: the session's single rose moment.

**Notation timing.** No new symbols; the beat reuses the formula as a read
object ("point at the part of the formula RAG replaces with a top-k").

**Predictions / retrievals.** The fill-the-mapping micro-retrieval; P5
before the heatmap verdict.

**Landing line.** "The weights are the plumbing, not the reasons."

### Beat 8: The Breadcrumb (45s)

**What happens.** Generative close, three moves, no summary. Move one,
retrieval: "Rebuild the box from memory. Three objects, two operations.
Say them before we do." (Silence on the track for four seconds. Then:
query, keys, values; score, blend.) Move two, "For the walk home": shuffle
the key-value cards on screen and watch the output bar not move. The box
has no idea what order its cards are in. Neither does attention: it's in
the correspondence table, and it's exact. But "dog bites man" and "man
bites dog" are different sentences made of identical cards. So how do you
give a dictionary a sense of order? That's session 2, and so is this: real
models run eight of these boxes side by side, each learning to ask a
different kind of question. We built one. Move three, the recursive close,
back in the kitchen: the lemon thing was never filed under L. It was spread
across the whole box, waiting for a question shaped roughly like it.
Kettle's on.

**Emotional beat.** Completion with a door left open. The opening image
returns recharged: the box that failed at 9pm is now the one machine the
learner can rebuild from memory.

**Key visuals.** [dynamic-process] The shuffle demo: cards permute, output
bar frozen, ten seconds, wordless except the landing. [connect] The kitchen
sketch from beat 1 returns, and this time the box's underline trues.

**Notation timing.** None. The formula appears only as a faded backdrop
during retrieval, then dims.

**Predictions / retrievals.** The full retrieval prompt (L6). The
breadcrumb question is itself the next session's open loop (R29).

**Landing line.** "The box can't tell 'dog bites man' from 'man bites dog.'
Sleep on that one."

---

## 4. The extended metaphor, named

**The metaphor: the recipe box.** The learner-facing coinage for the thing
they build is **the forgiving dictionary**. The box is the domestic
embodiment; the Python dict is its formal cousin (which this audience knows
cold); attention is the dict with partial credit. Concreteness fades
kitchen to code to vectors to notation, and the fade is shown, never cut.

Where it appears, beats 3 through 8:

- Beat 3: the box's tabs become key vectors; "how close is my question to
  this tab" becomes the dot product.
- Beat 4: the box that hands you exactly one card is the cliff; choosing a
  card is the unlearnable act.
- Beat 5: dinner made mostly from the best card with a spoonful of the
  runner-up is the value blend; the box's two empty slots (match, return)
  fill and true.
- Beat 6: the formula is read as the box written small; the correspondence
  table is verified row by row; sharpening turns the forgiving box back
  into the strict one.
- Beat 7: RAG is the box with the dial set to hard and the cards stored in
  someone else's warehouse; the weights are the recipe of the blend.
- Beat 8: shuffle the cards, nothing changes; the recursive close returns
  to the kitchen and the lemon thing.

**Drift ledger (where the metaphor is load-bearing and where it stops).**
The steer's stated risk is metaphor drift; this table is the control. The
term-by-term map is the dossier's own (section 1.2) and each row is
verified on screen in beat 6:

| Box / dict | Mechanism | Status |
|---|---|---|
| the question you ask with | query q | exact |
| the tabs | keys k_1..k_n | exact |
| the card contents | values v_1..v_n | exact |
| exact tab match, all or nothing | score 0 or 1 | exact (the limit case) |
| "how close is my question to this tab" | q . k_j / sqrt(d_k), continuous | exact |
| hand back one card | return the single value | exact (hard lookup) |
| dinner mostly from the best card, a little from the next | softmax-weighted blend of values | honest analogy: the math is a literal weighted average of vectors; the kitchen version is its image, and the on-screen blend is always shown as vector arithmetic, never as cooked food |
| KeyError | impossible in the soft box; weights just spread | exact |
| card order in the box | permutation invariance | exact, and it is the breadcrumb |

Honest edges, disclosed in-session where each becomes relevant:

1. A human flipping through the box scores every card and then PICKS one.
   The box we build is stranger than you: it refuses to pick. Beat 4 names
   this explicitly, so the learner's own behavior is the argmax foil.
2. Sharpening (temperature) is a property of softmax used as pedagogy; the
   transformer has no such knob, and sqrt(d_k) is the fixed cousin (beat 6,
   spoken disclosure, dossier 1.6.4).
3. The tabs are learned, not given: what counts as similar is a trained
   decision. Seeded in beat 3, cashed in beat 7's refutation. Projection
   matrices stay verbal in the video (dossier 1.6.6 folds them into the
   session 2 disclosure).
4. Single head only, no positional encoding, and the causal mask gets one
   honest sentence at the beat 5 LLM connection (dossier 1.6.1 through
   1.6.3; D-O2 scope, already flagged for Jake in brief.md front-matter).

---

## 5. The misconception beats

All three seeded ids trigger on this corpus (L9). Each is voiced in the
learner's own words BEFORE the correct account, then refuted visually.

**1. `attention-weights-are-explanations` (primary).** Voiced beat 5, the
moment shares first exist and before the name reveal: "So the 0.766 is the
box's reason. Cat is 77 percent of WHY the answer looks like this."
Structural refutation, immediately: the share tells you what got blended,
not why the scoring came out that way; change how the tabs are written and
the same query buys a different blend. The why lives in whatever wrote the
questions and the tabs. Visual: the blend recipe on one side, the scoring
machinery greyed out on the other; the weights literally cannot see it.
Re-cashed with teeth in beat 7: the Jain and Wallace 2019 result, scoped to
BiLSTM classifiers by the authors' own statement, two different heatmaps
morphing into the same output. The unresolved literature is named as
unresolved (visible rigor; no tidy moral).

**2. `softmax-picks-the-max`.** Voiced beat 6, as softmax is named: "It's
just a smooth argmax. It picks the winner." Refutation on screen in the
same ten seconds: kitten's 0.186 is sitting in the output bar, measurable;
nothing was discarded. Then the sharpening run does double duty (dossier's
instruction: spend the limit once): only in the twenty-fold limit does the
one-hot pick appear, and at that limit the gradient dies, which is exactly
why the mechanism lives in the soft regime.

**3. `similarity-means-identical`.** Voiced beat 3, on the qk-similarity
seed: "High dot product means the tokens are the same kind of thing."
Refutation is the sweep itself: the score rises and dies as the query
rotates while the keys never move; the score is agreement of direction in
a learned space, not sameness. Kitten and cat are different cards; the
score only says the question points their way.

---

## 6. The aha, blocked out

**What snaps together.** Three threads, each established separately and
each already the learner's property: (a) the dict they have used for years
(beat 1); (b) the score-then-blend machine they assembled with their own
predictions (beats 3 through 5); (c) the three words, query, key, value,
that they have seen floating unattached on architecture diagrams at work.
The snap is the attachment: the famous diagram IS the box. The learner was
one step from it the whole time, and P3 (name the three objects) hands them
that step ten seconds before the reveal. Learners who take it experience
discovery; learners who don't get a reveal at the moment of maximum
reaching, which Danek's evidence says still stamps ("d'oh" counts).

**Why it can't land earlier or later.** Earlier, and the name does the work
the mechanism should (the brief's stated failure mode for this hook).
Later, and the compression beat would have to name the objects itself,
wasting the reveal. Beat 5 is the unique slot.

**The staging.** Blend completes, box works, nameless. Misconception 1
voiced and refuted (the last thing built before naming, so the name arrives
already de-mystified). P3. Four-second hold. Morph, true-up, mint glow on
"query, key, value." The canonical sentence, once, plainly. No music
swell; the motif is the emotion.

---

## 7. The breadcrumb and extensions

**For the walk home.** The shuffle demo: the box, and attention, cannot see
order; "dog bites man" and "man bites dog" are the same pile of cards. How
do you give a dictionary a sense of order? (Session 2 opens by retrieving
this exact question, per series rule.) Second thread, one sentence: real
models run eight boxes in parallel, each learning to ask a different kind
of question; we built one of them (D-O2 breadcrumb, multi-head plus
positional encoding).

**Still up?** Three doors:

1. **Argue it out with an LLM.** (a) "Defend the sentence 'attention is a
   soft lookup table' to a skeptic. Then find the two places the metaphor
   legitimately strains." What good looks like: cites the hard-lookup
   limit and permutation invariance as exact, names the human-argmax and
   temperature caveats as the strains. (b) "Why could a hard, argmax
   version of attention not train by gradient descent? Where exactly does
   the gradient die?" What good looks like: flat-then-cliff output, zero
   slope almost everywhere, w(1 - w) at the sharp limit.
2. **Read the real thing.** Vaswani et al. 2017, section 3.2 only: read
   the definition you can now read left to right. Jain and Wallace 2019
   plus Wiegreffe and Pinter 2019 as a pair: the heatmap fight, both sides.
   d2l.ai chapter 11 for the textbook version of tonight's box, including
   the sixty-years-early statisticians' edition (Nadaraya-Watson, 1964).
3. **Build something.** The companion notebook (committed, per brief): the
   six-rung ladder from dict to attention in about 30 lines of NumPy:
   KeyError, one-hot scores, softmax partial credit, the blend, the
   sharpening that recovers the dict exactly, and the optional gradient
   check where the soft version differentiates and the hard one flatlines.
   Scoped project: swap the toy vectors for real embeddings from any small
   model and ask your forgiving dictionary for "feline"; write three
   sentences on what came back and why.

---

## 8. Landing lines (one per major section, drafted)

1. Hook: "Exact match is a fine way to store an answer and a brutal way to
   ask a question."
2. Gap: "Close is not a feeling. Close has to become a number."
3. Elemental unit: "Alignment is the score. Direction agreeing with
   direction, measured."
4. Build & complicate: "A choice has no slope."
5. Aha: "Attention is a soft lookup table. You just built it."
6. Compression: "The formula is the box, written small."
7. Stress-test: "The weights are the plumbing, not the reasons."
8. Breadcrumb: "The box can't tell 'dog bites man' from 'man bites dog.'
   Sleep on that one."

---

## 9. Production notes

**Timing budget.** 50 + 40 + 70 + 75 + 70 + 70 + 70 + 45 = 490s. Target
480, cap 540. The 50s of slack is real: beats 6 and 7 are the compression
candidates if S3 scripting runs long.

**Dossier traceability.** Beat 1 and 2: brief hook B; dossier 1.2 (KeyError
row). Beat 3: dossier 1.5 (micro-example vectors and raw scores),
misconception 3 (dossier section 3.3). Beat 4: dossier 1.4 (gradient dies
at the hard limit), 3.1. Beat 5: dossier 1.5 (shares 0.766 / 0.186 / 0.045
/ 0.003, output [0.912, 0.083]), 1.6.3 (causal mask sentence), section 8
partial (retrieval-vocabulary phrasing: "matches how retrieval systems
talk," never "borrowed from databases"). Beat 6: dossier 1.3 (sqrt(d_k)
variance numbers, "we suspect" verbatim, gradient factor 3e-7 and 0.105),
1.4 (sharpening limit numbers), 1.6.4 (temperature disclosure), 3.2. Beat
7: dossier 5.2 (RAG, Lewis et al. NeurIPS 2020), 2C and 3.1 (Jain and
Wallace scope-disciplined claims, unresolved debate), 8 (verified). Beat 8:
dossier 1.2 (permutation row), 1.6.1 and 1.6.2 (D-O2 breadcrumb). Notebook:
dossier section 7. Nadaraya-Watson: dossier 5.1 (extensions only).

**Asset inventory.** PASSED and placed: qk-similarity (beat 3, 24s,
verbatim), qk-explorer (beat 3 page track, existing states). Cheap
derivatives: labeled-token variant of the sweep (beat 3), sharpening slider
(beat 6). New scenes: dict/KeyError code well (1), two-slot box scaffold
(2, recurring), argmax cliff plot (4), normalize-and-blend (5), box-to-
diagram true-up (5), formula term build plus correspondence table (6), RAG
alignment diagram plus dual-heatmap morph (7), shuffle demo plus kitchen
return (8). Open question for the Director: values and the output vector
need a semantic color; keys own periwinkle and scores own lilac, so the
value series is unassigned in the current token set.

**L-check self-audit.** L1: one idea per beat (see beat list). L2: max
simultaneous novelty is beat 3's query+keys+bars trio and beat 6's formula,
whose terms are all pre-manipulated. L3: every symbol post-manipulation
(beats 3, 6). L4: P1 through P5 precede every major reveal. L5: cold open
ends on the question, zero definitions. L6: retrieval + breadcrumb +
extensions in beat 8. L7: narration never mirrored on screen; code and
labels only. L8: every visual above maps to a scripted proposition. L9:
three voiced misconception beats. L10: 490 <= 540. Voice lint: zero
em-dashes and zero en-dash clause glue anywhere in this file, banned
vocabulary absent, two template jokes plus one deflating hedge ("probably;
the authors themselves wrote 'we suspect'"), no fabricated first person,
second-person hypotheticals only.
