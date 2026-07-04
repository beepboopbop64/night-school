# Treatment candidate: history-first

```yaml
candidate: history-first
session: attention
aha: "Attention is a soft lookup table."
hook: A (the bottleneck that broke translation, dossier section 2A)
steer: >-
  Open on the verified human story; the mechanism emerges as the resolution
  of Bahdanau's problem. Risk managed: hands are on math by 1:55.
videoEstimateSeconds: 505
videoHardCapSeconds: 540
trimPlan: "B1 -5s (compress reversal), B4 -5s (tighten dict reveal), B6 -10s (move disclosure line to page callout). Floor: 485s."
proposedTitle: "How Do You Take a Gradient Through a Choice?"
proposedSubtitle: "One vector, five weeks, eight thousand numbers."
extendedMetaphor: "the forgiving dictionary"
misconceptionBeats: [B3, B5-primary, B6]
```

Four Cs, for the record. Causality: each beat's result creates the next
beat's problem (bottleneck, then choice, then score, then wall, then blend).
Conflict: how do you make looking learnable? Complication: the natural fix,
pick the best match, is exactly a dict lookup and it kills the gradient.
Character: Sutskever's team, Cho's measurements, and an intern with five
weeks left.

---

## 1. The hook, in full prose

The first ~150 words are the cold open VERBATIM (the voice sample). Runs
over the title-card true-up and the funnel visual described in B1.

> In 2014, the best neural translator anyone had built read your sentence
> one word at a time, packed everything it understood into a single vector,
> then threw the sentence away and wrote the translation from the vector
> alone. Eight thousand numbers, which is plenty for any sentence a human
> might write, or something.
>
> Researchers in Montreal measured what the squeeze cost. Short sentences
> came through clean. Long ones fell apart, fast.
>
> At Google, Ilya Sutskever's team found a strange hack that bought real
> accuracy: feed the sentence in backwards. One model's BLEU score jumped
> from 25.9 to 30.6. Reading backwards helped. Nobody could call that a
> theory.
>
> That same September, an intern in Yoshua Bengio's Montreal lab had five
> weeks left and a hunch borrowed from his own eyes. Watch yourself
> translate: your gaze jumps back and forth across the source. Dzmitry
> Bahdanau wanted to let the model look.

Beat 1 then closes (remaining ~20 words of narration):

> Keep every word. Learn, for each word you write, where to look. That one
> sentence is the whole session.

Sourcing: dossier section 2A (all verified; sources.yaml). Cautions
honored: BLEU numbers attributed to one model (the single-LSTM condition);
Bahdanau framed as posting in the same September, never as reacting to
Sutskever; no "billion users" claim anywhere (the GNMT stakes in B8 use the
verified 500 million users / 100 billion words a day figures).

---

## 2. The beat list (one new idea per beat, and what forces the next)

| # | Beat | The ONE new idea | Forces next beat | Est. |
|---|------|------------------|------------------|------|
| B1 | Hook | One fixed vector bottlenecked translation; the proposed cure was looking back at every word | "Where to look" is a choice. How can a choice be learned? | 70s |
| B2 | Gap | Looking is discrete, and gradients cannot cross a discrete choice | We need machinery: start with the smallest piece of a learnable looker | 45s |
| B3 | Elemental unit | A query scored against keys by dot product: relevance is graded, not binary | Scores in hand, the obvious move is to fetch the winner's content | 65s |
| B4 | Build & complicate | Fetching the argmax value IS a dict lookup: exact, familiar, and unlearnable (zero gradient) | We cannot choose. What is the alternative to choosing? | 80s |
| B5 | Aha | Never choose: softmax the scores, blend the values. The dict has gone soft. "Attention is a soft lookup table." | A thing this clean deserves compressed notation and a name | 70s |
| B6 | Compression | softmax(QK^T/sqrt(d_k))V read term by term as the lookup made soft; sharpening the scores brings the hard dict back exactly | If the skeleton is real, it should exist somewhere else | 75s |
| B7 | Stress-test | RAG is the same query-key-value skeleton at the opposite end of the hard-soft dial | The dict frame exposes what attention inherits: no order | 50s |
| B8 | Breadcrumb | Permutation blindness: shuffle the pairs, the blend never changes. New gap: how does order get in? | Session 2 (positional encoding, multi-head per D-O2) | 50s |

Total: 505s (cap 540; trim plan in front-matter).

---

## 3. Beat-by-beat

### B1. Hook (0:00 to 1:10, 70s)

**What happens.** Brand title card (under 4s, underline trues on the first
narrated syllable). The cold open above, over three visuals in sequence:
(1) tokens of a long sentence flow into one fixed-size glowing box, the box
never grows, "8000 numbers" in mono beside it; (2) the collapse curve,
redrawn freehand from the verified artifacts (dossier 2A: Bahdanau Figure 2
encoder-decoder side, Cho et al. degradation finding): translation quality
falling as sentence length grows. Only the collapsing line is drawn now;
the rescue line is withheld for B5. (3) The reversal hack: the sentence
flips on screen, 25.9 ticks up to 30.6. Then the Montreal turn: a mono
name card ("D. Bahdanau, intern, five weeks left") and the gaze image: two
rows of text, source above, target below, and an amber dot hopping between
them. That amber dot is the series' attention color, planted 60 seconds in,
before anyone calls it anything.

**Emotional beat.** Absurdity (backwards helps?) turning into underdog
sympathy, turning into an itch.

**Key visuals.** Funnel/keyhole (tag: dynamic-process), freehand collapse
curve (connect-to-reality, sketch fidelity, wobble kept), gaze dot
(dynamic-concept, seeds the query).

**Notation.** None. Numbers on screen are data, never symbols.

**Predictions/retrievals.** None; the hook stays clean.

**Landing line.** "Every sentence had to fit through the same keyhole."

### B2. Gap + prediction (1:10 to 1:55, 45s)

**What happens.** Formalize "let the model look" one notch: mid-translation,
candidate source words highlight, a hard pointer snaps between them. State
the wall plainly: training means gradients, gradients need slopes, and a
pointer that snaps has no slope. Advance organizer, question form (L5):
"How do you take a gradient through a choice?" Prediction P1, an explicit
pause: "How would you make 'look over there' learnable? You know the one
constraint: whatever the model does must be differentiable. Take ten
seconds." Close the beat with a promise, not a spoiler: "The answer hides
inside the most boring data structure you know."

**Emotional beat.** The gap felt, and felt almost-closable.

**Key visuals.** Snapping pointer vs a ball rolling on a smooth slope; the
snap redraws as a staircase fragment (this exact staircase returns in B4).
Tags: dynamic-concept, symbol-sense groundwork.

**Notation.** None.

**Predictions/retrievals.** P1 (pause-and-ponder checkpoint, before any
machinery).

**Landing line.** "Gradients need slopes. A choice is a cliff."

### B3. Elemental unit (1:55 to 3:00, 65s)

**What happens.** Strip everything to the smallest piece: before a model
can look wisely, it needs a score for "how relevant is each stored thing to
what I'm asking." One amber question vector, four periwinkle stored
directions. **This beat absorbs the PASSED qk-similarity video beat nearly
verbatim (24s of the 65s):** the query sweeps, lilac score bars rise and
die with alignment, labels on objects, no legends. Then anchor with the
micro-example numbers (dossier 1.5): q = [2, 0]; keys cat [2, 0], kitten
[1, 1], car [0, 2], sofa [-2, 0]; scores 4, 2, 0, -4. Prediction P2 before
the numeric reveal: "Car's key points at a right angle to the query. Guess
its score before we compute it." (Zero. Orthogonal means the question
never touched it.) Misconception 3 voiced and refuted here, in the
learner's voice: "a high dot product means the tokens are the same kind of
thing." Refutation is on screen already: rotate the query and the scores
change while the keys never move. The score is alignment in a learned
space, not sameness; one sentence flags that what counts as aligned is
itself trained (the full W_Q, W_K story goes to a page callout, not the
video).

**Emotional beat.** Play. Hands on the math four minutes before any formula.

**Key visuals.** qk-similarity beat (covary, dynamic-concept), then the
four named keys with integer scores. **Page track: the PASSED qk-explorer
interactive embeds here** (learner drags the query angle through the
initial / mid-drag / aligned / anti-aligned states; alignment IS the
score, felt by hand).

**Notation.** q and k labels ride the objects during manipulation (as in
the passed seed). The written form "q . k" appears only after the sweep,
naming a motion already watched (L3 clean).

**Predictions/retrievals.** P2 (guess car's score).

**Landing line.** "Alignment is the score."

### B4. Build & complicate: the wall (3:00 to 4:20, 80s)

**What happens.** Give every key a payload: cream value cards attach to
each key (cat's value, kitten's, car's, sofa's). Natural first approach,
tried honestly: score all keys, take the winner, return its value. Run it:
q asks, cat scores 4, cat's card comes out. Then the recognition: rearrange
the picture into two columns, keys left, values right, exact match, one
value out. It is a Python dictionary. `d["cat"]` works. `d["feline"]`
raises KeyError: the dictionary has no idea those two words have ever met.
Our vector version is better only in one way: it can score near-misses. So
keep score-then-argmax and try to LEARN it. Prediction P3: "Nudge the query
a little. Watch the output. What changes?" Reveal: nothing. Flat, flat,
flat, snap. The output as a function of the query is a staircase (the B2
staircase, now fully drawn), and the gradient meter under it flatlines:
zero everywhere it is flat, undefined at the snap. The training signal dies
at the argmax. Empathic reframe, spoken: "That is not a failure of
cleverness. It is the structure of the problem. We rebuilt the cliff from
minute two, and now we can point at it."

**Emotional beat.** Recognition high ("I know this object"), then bounded
frustration, explicitly named and about to be resolved.

**Key visuals.** Values as cards (pre-training the third object before it
interacts); vectors morphing into the dict table (connect); KeyError in
rose (one of the session's two rationed rose moments); staircase plus
dead-gradient meter in rose (the second; both live in this beat).

**Notation.** v labels on the value cards at introduction. The word
"argmax" appears only after the staircase is seen. No formula.

**Predictions/retrievals.** P3 (nudge the query: what changes?).

**Landing line.** "The lookup works. The learning dies."

### B5. The aha (4:20 to 5:30, 70s)

**What happens.** Prediction P4, the reaching moment: "We cannot choose.
Choosing is the cliff. What is the alternative to choosing?" Hold one beat
of silence. Then the resolution: never choose. Keep every value, in
proportion to its score. The lilac score bars normalize into weights that
sum to one: 0.766 cat, 0.186 kitten, 0.045 car, 0.003 sofa. The value
cards blend, weighted: out = [0.912, 0.083]. Ask for feline, get mostly
cat, a little kitten, essentially no car. The KeyError cell from B4 fills
in with partial credit. As the bars settle, voice the primary
misconception in the learner's voice (these students have met these bars
at work as heatmaps): "So cat is 77 percent of the why." Then the morph
that IS the aha: the dict diagram and the score-blend diagram slide onto
each other and true up as one drawing, mint glow on settle, and the
sentence lands verbatim: **"Attention is a soft lookup table."** Refute
the misconception with the correct account, now earned: the weights are
the mixing knobs of a lookup. They tell you what got blended, never why
the recipe was chosen; the why lives upstream in the learned parts that
built the scores. (Jain and Wallace, the debate, and the honest 2026 scope
go to the page and doc, per dossier 2C and 3.1; the video spends one
sentence.) History pays its debt in the last fifteen seconds: this is what
Bahdanau implemented, softmax-weighted averaging, and by his own account
it worked on the first try. The B1 collapse curve returns and the rescue
line draws in flat: 17.82 versus 26.75 BLEU on the verified Figure 2
redraw. The curve stopped falling.

**Emotional beat.** The snap, then vindication: the intern's hunch and the
learner's own build land as the same object.

**Aha engineering check.** Every component separately established (keys
B3, values B4, scores B3, the cliff B4); the learner was one step away:
P4 sets them reaching, and "stop choosing, blend" is the only new move.
Engineered, not narrated.

**Key visuals.** Bars normalizing (dynamic-process); weighted blend
arithmetic with the dossier 1.5 numbers on screen; the dict-to-attention
true-up morph (connect: THE morph of the session); Figure 2 completing
(connect-to-reality).

**Notation.** The word "softmax" is spoken only after the bars are seen to
normalize (behavior first, name second). Still no full formula.

**Predictions/retrievals.** P4 (the alternative to choosing), the beat of
silence, then payoff. Misconception 1 voiced before the correct account,
refuted right after the sentence lands.

**Landing line.** The aha sentence itself: "Attention is a soft lookup
table."

### B6. Compression (5:30 to 6:45, 75s)

**What happens.** The naming, delivered as recollection per dossier 8:
Bahdanau called the model RNNSearch; the better name, attention, came from
Bengio in a late pass, by Bahdanau's own telling. Now compress the whole
story into symbols, assembled in reasoning order, every term color-matched
to the object the learner already touched: q dot k (amber against
periwinkle, making lilac), keys stacked into a matrix K, all queries at
once as Q, softmax wrapping the scores, V blending at the end:
softmax(QK^T / sqrt(d_k)) V. Read aloud as English: "score every key
against every query, soften the scores into weights, blend the values.
The lookup, made soft." One honest line for sqrt(d_k) plus a no-handwave
callout flag: long vectors make big scores, big scores freeze softmax's
gradients, and dividing by sqrt(d_k) keeps scores in the healthy zone; the
paper itself says "we suspect," and the exact d_k = 2 versus 64 numbers
(gradient factor 3e-7 versus 0.105) live in the notes (dossier 1.3). One
owed disclosure sentence (dossier 1.6): Bahdanau's 2014 scorer was a small
network, not a dot product; the dot-product form was catalogued by Luong
in 2015 and scaled by Vaswani in 2017, and that is the version on screen.
Then misconception 2, voiced at softmax's first formal appearance: "softmax
is a smooth argmax; it picks the winner." Prediction P5: "Multiply every
score by 20. What do the weights become?" Reveal, spent once, on screen:
at working sharpness the winner got 0.766 and kitten's 0.186 is measurably
in the answer (nothing was discarded); sharpened 20x the weights hit
[1, 0, 0, 0] to eight decimals and the hard dict returns exactly. One demo,
two payoffs: the misconception dies, and the aha passes its own
falsification test. Attention is the differentiable relaxation of the
lookup, and at the hard limit the gradient factor hits zero.

**Emotional beat.** Mastery and relief: for the rusty-notation audience,
the scary formula turns out to be four things they already handled.

**Key visuals.** The concrete-to-symbolic fade SHOWN: picture morphs to
diagram morphs to formula, terms truing one at a time (symbol-sense);
sharpness slider demo (covary). Director note: split into 6a (assembly)
and 6b (limit demo) scenes to respect the four-novel-elements budget.

**Notation.** Everything, and only now: Q, K, V, sqrt(d_k), the full
formula. Every symbol's referent was manipulated beats earlier (L3 clean
by construction).

**Predictions/retrievals.** P5 (sharpen by 20x: predict the weights).

**Landing line.** "Gradient flows only while the lookup stays soft."

### B7. Stress-test + second instance (6:45 to 7:35, 50s)

**What happens.** Surface-different second instance the audience runs at
work: RAG (dossier 5.2, Lewis et al., NeurIPS 2020). Your question is
embedded as a query vector, scored against the key vectors of a document
index, and the winning passages come back as the values. Side by side with
attention, structure aligned and NAMED: score keys with a query, use the
scores to fetch values. The query-key-value skeleton. The differences are
the lesson, not a footnote: RAG takes a hard top-k over an external store,
and no gradient flows through the index; attention blends softly over an
internal store, inside every layer. The sharpness dial from B6 reappears
as the axis both live on. Retrieval micro-prompt (generative, not
summary): "Point at the query, the keys, and the values in your own RAG
stack." Honest edges close the beat: real transformers run eight of these
lookups in parallel and concatenate (ours is exactly their machinery with
one head), and decoder LLMs blind each query to future keys with a mask.
Both named in one sentence each; both flagged as disclosures.

**Emotional beat.** Relevance. The 9pm learner sees Tuesday's job in the
diagram, and the honesty buys trust.

**Key visuals.** Two skeletons side by side, matched part to part with
locked colors (generalize, connect); hard-soft dial callback.

**Notation.** None new. Vocabulary "top-k" allowed; this audience owns it.

**Predictions/retrievals.** Retrieval micro-prompt (map your RAG stack).

**Landing line.** "Same skeleton, opposite ends of the dial."

### B8. Breadcrumb + extensions (7:35 to 8:25, 50s)

**What happens.** The dict frame exposes what attention inherits. On
screen: shuffle the key-value pairs; the weights shuffle with them; the
blended output does not move (dossier 1.2, verified, exact). A dict has no
order. Neither does attention. Now the sting: shuffle the WORDS of a
sentence and every token's blend stays identical. A machine built only of
soft lookups cannot tell who bit whom. Retrieval prompt first: "Rebuild
the ladder in your head: dict, scores, cliff, blend. Which single change
made looking learnable?" Then the breadcrumb, posed and left open, "For
the walk home": how do you smuggle word order into a machine whose memory
is an unordered dictionary? That is session 2, along with why the real
thing runs eight lookups side by side (D-O2). History closes the loop with
verified stakes: Google Translate went neural in production in September
2016, on a service with more than 500 million users translating over 100
billion words a day; in 2017 Vaswani and colleagues threw away the
recurrent network and kept only the fix. The intern's five weeks became
the load-bearing operation of every model these students touch. "Still
up?" menu (full spec below).

**Emotional beat.** Completion, plus a deliberate itch shaped exactly like
today's schema.

**Key visuals.** Pair-shuffle with frozen output (dynamic-process,
honest-edge made visible); sentence shuffle; closing card in brand
microcopy.

**Notation.** None new.

**Predictions/retrievals.** The retrieval prompt (rebuild the ladder), then
the breadcrumb question, then stop.

**Landing line.** "The fix outlived the architecture it rescued."

---

## 4. The extended metaphor: the forgiving dictionary

Named coinage: **the forgiving dictionary**. A dict that grades near-misses
instead of raising KeyError. Sourced from the learner's own daily toolkit
(the brief's audience note: they know Python dictionaries cold), not from
the field describing itself.

Where it lives, beat by beat:
- **B3**: the metaphor's engine arrives first without the name: relevance
  scored as partial credit on a key match.
- **B4**: the dictionary named, in its hard form; KeyError is the
  metaphor's felt failure; argmax is the dict rebuilt from vectors.
- **B5**: the dict goes soft; the forgiving dictionary is BUILT on screen,
  then revealed to have a famous name. Aha = the metaphor and the
  mechanism truing into one drawing.
- **B6**: the formula is read as "the lookup, made soft," term by term;
  the sharpening limit hands the hard dict back, proving the metaphor is
  structure, not decoration.
- **B7**: RAG as the forgiving dictionary's day-job cousin: external store,
  hard choice; same skeleton.
- **B8**: recursive close: the dict's unorderedness is inherited by
  attention, and that inheritance is the next session's opening problem.

Falsifiability discipline (brief): every row of the dict correspondence is
demonstrated (query B3, keys B3, values B4, scores B3, blend B5, hard-limit
B6, unordered B8). If any row failed to map, the session fails its own
sentence. None fail; dossier 1.2 and 1.4 carry the proofs.

---

## 5. Misconception beats

Primary (non-negotiable, `misconceptionBeat: true` on B5):
**attention-weights-are-explanations.** Learner's voice, spoken as the
weight bars first settle: "The model put 77 percent of its weight on cat,
so cat is 77 percent of the why." Voiced BEFORE the correct account, then
refuted by the correct account itself: the weights are the mixing knobs of
a soft lookup. Visual refutation: the weights exist only as the normalized
bars that feed the blend; the camera follows the causal arrow upstream to
the score-builders and finds the "why" lives there. The empirical teeth
(Jain and Wallace 2019, scope-disciplined per dossier 2C; the unresolved
debate) are carried by the page aside and the written doc, not the video.

Secondary, B3: **similarity-means-identical.** "A high dot product means
the tokens are the same kind of thing." Refuted live on the qk-similarity
seed: the query rotates, scores rise and die, the keys never change. The
score is alignment in a learned space.

Secondary, B6: **softmax-picks-the-max.** "Softmax is a smooth argmax."
Refuted by the one-demo-two-payoffs sharpening sequence: at working
sharpness the runner-up's 0.186 is measurably in the output (nothing
discarded); only in the 20x limit does [1, 0, 0, 0] appear. Spent once, on
screen, doubling as the aha's falsification test.

---

## 6. The aha beat, blocked

What snaps together: the dict table from B4 (keys, values, exact match,
one value out) and the score bars from B3 (graded relevance) were the same
diagram all along, joined by one move the learner is reaching for when P4
lands: normalize and blend instead of choose. The learner was one step
from making it themselves: they already owned the hard lookup (B4 built
it), already owned graded scores (B3 swept them), and P4 plus a beat of
silence gives them the step. The reveal executes the brand true-up: the
two diagrams slide together, wobble once, true with mint glow, and the
canonical sentence lands verbatim at the settle. History resolves in the
same breath: the thing they just built is the thing that worked on
Bahdanau's first try, and the hook's collapsing curve finally gets its
flat rescue line.

---

## 7. The breadcrumb

"For the walk home": shuffle a dict's pairs and nothing changes; shuffle a
sentence's words and, to this mechanism, nothing changes either. So how
does a model whose memory is an unordered dictionary read English at all?
How does order get in? (Session 2: positional encoding, plus why one
lookup per layer became eight, per D-O2.) Posed as a question, then stop.

"Still up?" menu:
1. **Argue it out with an LLM.** (a) Defend "attention is a soft lookup
   table" against a skeptic; what good looks like: you produce the
   sharpening limit unprompted and concede where the metaphor strains
   (the learned projections have no dict counterpart). (b) "My attention
   heatmap says the model focused on 'terrible', so that's why it said
   negative." Argue both sides; what good looks like: mixing weights
   versus causes, and the honest scope of the 2019 results.
2. **Read the real thing.** Bahdanau, Cho, Bengio 2014 (watch Figure 2 pay
   off in the original); Vaswani et al. 2017 section 3.2 (find the "we
   suspect" footnote and decide if you buy it).
3. **Build something.** The 30-line NumPy ladder (dossier 7): dict, then
   one-hot scores, then softmax, then sharpen until the dict returns;
   micro-example numbers as the test vector. Companion notebook per
   d-s0-notebook-yes.

---

## 8. Landing lines (one per major section, drafted)

- B1: "Every sentence had to fit through the same keyhole."
- B2: "Gradients need slopes. A choice is a cliff."
- B3: "Alignment is the score."
- B4: "The lookup works. The learning dies."
- B5: "Attention is a soft lookup table."
- B6: "Gradient flows only while the lookup stays soft."
- B7: "Same skeleton, opposite ends of the dial."
- B8: "The fix outlived the architecture it rescued."

---

## 9. Production notes for the Director

**Steering risk, managed.** History gets 70 uninterrupted seconds, then
returns only as payoff shots (the rescue line at B5, the naming at B6, the
stakes at B8), never as new mid-arc exposition. Hands are on manipulable
math at 1:55. Total narration approximately 1,200 words at Matilda pace.

**Existing PASSED assets.** qk-similarity video beat absorbed into B3
(24s, nearly verbatim, colors already locked). qk-explorer interactive
referenced from B3's page-track `interactiveSpec` and carried alongside
B4 (optional Director extension: an argmax-mode state group so the learner
feels the flat output; suggestion only, not contracted).

**Color semantics (for spine.md).** Query amber `data.heat`; keys
periwinkle `data.observed`; scores and weights lilac `data.params`; values
cream `data.truth`; blended output and every true-up mint `data.fit`; rose
`data.error` rationed to B4's KeyError and dead-gradient flatline.

**Disclosures ledger (no-handwave callouts owed).** Single head is h=1 of
the real machinery (B7); no positional encoding, order-blind by
construction (B8, doubles as breadcrumb); causal mask one-liner (B7);
sharpening is a property of softmax, not a transformer dial, and sqrt(d_k)
is the fixed principled cousin (B6); Bahdanau's 2014 scorer was additive,
dot-product form is Luong 2015 / Vaswani 2017 (B6); "we suspect" framing
on the gradient story (B6).

**L-check self-audit.** L1/L2: one idea per beat, B6 split 6a/6b keeps
novel elements at four or fewer. L3: q, k at B3 on-object during
manipulation; v at B4; softmax named after bars normalize (B5); formula
only at B6. L4: P1 (B2), P2 (B3), P3 (B4), P4 (B5), P5 (B6) precede every
major reveal. L5: "How do you take a gradient through a choice?" lands in
B2 before any definition. L6: B8 carries retrieval prompt, breadcrumb
question, extensions menu. L9: misconception beats at B3, B5 (primary),
B6. L10: 505s estimate, 540 cap, trim plan to 485 recorded above.
