# Treatment: candidate-obstruction-first

```yaml
candidate: obstruction-first
session: attention
aha: "Attention is a soft lookup table."
hook: A (the bottleneck that broke translation, dossier section 2A)
steer: >-
  Open on a technical wall the learner feels (a fixed vector summarizing any
  sentence; retrieval that must be differentiable), fail honestly at it, and
  let attention be the escape.
videoEstimatedSeconds: 495
videoHardCapSeconds: 540
absorbedAssets:
  - qk-similarity (PASSED video beat, placed verbatim in beat 3)
  - qk-explorer (PASSED interactive, page track, twinned to beats 3 and 4)
scope: single-head dot-product attention only, per D-O2 (brief front-matter)
factSource: dossier.md only; citations below point at dossier sections
```

---

## 1. The hook, in full

**Cold open, first 158 words, VERBATIM narration (0:00 to ~1:05). This is the
voice sample.**

> In 2014, the best neural translator on Earth worked like this: read the
> whole sentence, squeeze everything you understood into one fixed list of
> 8,000 numbers, then write the translation from that list alone. Every
> sentence got the same box. "The cat sat." 8,000 numbers. A sixty word
> contract clause with three nested caveats. The same 8,000 numbers.
>
> You can guess what the data showed: translation quality fell apart as
> sentences got longer. And the fix that actually shipped is my favorite
> desperate hack in the history of the field. They fed the sentence in
> backwards. That's it. Reverse the input, and a single LSTM's BLEU score
> jumped from 25.9 to 30.6. The model is like, wow, what if the first words
> were just... closer. And it worked. That's the uncomfortable part. It
> worked, and it changed nothing, because the box was still a box.
>
> So the field kept squeezing. And an intern in Montreal decided to stop.

**Hook continuation (to ~1:20), prose:**

> The intern was Dzmitry Bahdanau, five weeks left in Yoshua Bengio's lab,
> staring at the same wall in his own lab's translator. By his own account,
> the idea came from watching his own eyes: when you translate, your gaze
> shifts back and forth between the source and the thing you're writing. So
> let the model do that. Keep every word. And for each word it writes, let it
> look back.

Facts and citations: fixed 8,000-number sentence vector, reversal trick with
single-LSTM BLEU 25.9 to 30.6 (dossier 2A, 6); length degradation finding
(dossier 2A, Cho et al.); Bahdanau's status, five weeks, gaze account
delivered as his recollection via the published correspondence (dossier 2A,
8-VERIFIED). Caution honored: Bahdanau attacks the bottleneck in his own
lab's encoder-decoder, not Sutskever's paper; the on-screen timeline shows
his arXiv date (Sep 1) before seq2seq's (Sep 10) so no false causation is
implied (dossier 2A caution flags). No "billion users" anywhere (dossier 8,
FAILED item).

---

## 2. The beat list

One new idea per beat; each result creates the next beat's problem.

| # | Beat | The ONE new idea | How it forces the next beat | Est. sec |
|---|------|------------------|------------------------------|----------|
| 1 | Hook | A fixed-size vector cannot carry an unbounded sentence, and the field's best fix was a hack | "Look back at every word" sounds like the obvious repair, so why did nobody just do it? | 80 |
| 2 | Gap | "Where to look" is a choice, and a choice has no gradient | If choosing is unlearnable, we need the smallest piece of "looking" we can hold: a score | 40 |
| 3 | Elemental unit | A dot product turns "how relevant is this word" into a number that moves with alignment | Scores rank candidates, so the natural move is to take the winner: try it | 60 |
| 4 | Build & complicate | Hard selection answers correctly but learns nothing: the gradient through argmax is zero | We must keep the ranking and lose the cliff: blend instead of choose | 85 |
| 5 | Aha | The blending machine we just built IS a dictionary with the hardness removed: attention is a soft lookup table | A thing this clean deserves to be written down small | 70 |
| 6 | Compression | softmax(qK^T / sqrt(d_k))V is the lookup made soft, term by term, and hard lookup is its sharp limit | If the skeleton is really a lookup, it should show up in other lookups we use | 70 |
| 7 | Stress-test | RAG has the same three objects at the opposite end of the hard-soft dial; and mixing weights are plumbing, not reasons | The mapping holds everywhere except one row: dictionaries have no order | 50 |
| 8 | Breadcrumb | Attention is order-blind, and language is not | Session 2: position, and many lookups in parallel (D-O2) | 40 |

Total: 495 seconds. Cap 540 (L10). Target 480; the 15-second overage lives in
beats 4 and 5 and is the first place the Director should trim.

---

## 3. The extended metaphor

**The forgiving dictionary.** The one data structure every learner in this
room used this week, rebuilt so that a near-miss key gets partial credit
instead of a KeyError. Named at beat 5, but built namelessly from beat 3
onward so the learner assembles it before they recognize it.

- Beat 3: the dictionary's contents appear without the word "dictionary":
  stored labels (keys) and a probe (query), scored by alignment.
- Beat 4: the hard version IS `d[q]`: take the exact winner, return its
  value. It answers fine and learns nothing. The obstruction is the
  dictionary's hardness itself.
- Beat 5: the morph. Python dict on the left, our machine on the right, rows
  slide into correspondence (dossier 1.2 table). The name lands: a lookup
  table, made soft.
- Beat 6: the formula is read as the lookup, term by term, color by color;
  sharpening the scores brings the literal dict back on screen (dossier 1.4,
  1.5). The metaphor is proven in the limit, not asserted.
- Beat 7: RAG is the dictionary that stayed hard and moved outside the model
  (dossier 5.2). Same skeleton, opposite hardness.
- Beat 8: dictionaries are unordered, and so is attention: the metaphor's
  last row becomes the next session's opening gap (dossier 1.2, last table
  row).

One secondary image, used exactly twice: the weights are **recipe
proportions**. A recipe card tells you what got mixed, not why the recipe
was chosen. It appears at the misconception refutation (beat 5) and once in
the stress-test (beat 7). No other metaphors.

---

## 4. The misconception beats

All three seeded ids fire (L9). Placement per brief and dossier section 3.

**Primary: `attention-weights-are-explanations`. Voiced late in beat 4,
refuted in beat 5, strictly before the correct account of the weights.**

Learner's voice, over the first render of the amber weight bars sitting on
the four tokens, which look exactly like every attention heatmap these
students have shipped at work:

> "Wait, I know this picture. 0.766 on cat. So cat is 77 percent of the why."

Refutation (beat 5, visual): the weights are the blend's proportions. The
recipe card tells you what was mixed, not why the recipe was chosen; the
choosing lives upstream, in the learned scoring that built those numbers
(dossier 3.1, mechanism-level refutation, no experiment needed). The
empirical teeth stay scoped and land in beat 7: on BiLSTM classifiers,
researchers found very different attention maps yielding the same
predictions, and weights correlating weakly with other importance measures;
the debate is real and unresolved (dossier 2C, defensible one-sentence
scope; Jain and Wallace 2019; Wiegreffe and Pinter 2019).

**`similarity-means-identical`. Voiced and refuted inside beat 3**, on the
qk-similarity sweep: "a high score means the tokens are the same kind of
thing." Refuted by the seed visual itself: the keys never move, and every
score rises and dies purely with the query's direction. Alignment, not
sameness. One spoken line notes the space is learned, so what counts as
similar is trained, not given; the full W_Q, W_K version lives in a page
aside (dossier 3.3, 1.6 disclosure 6).

**`softmax-picks-the-max`. Voiced and refuted in beat 6**, the instant the
word softmax first appears: "smooth argmax, picks the winner, right?" The
numbers refute it: the winner got 0.766, not 1.0, and kitten's 0.186 is
measurably inside the output vector. Nothing was discarded (dossier 3.2,
1.5). The sharpening demo then shows where the "picks the max" intuition
actually lives: only in the limit.

---

## 5. The aha beat, blocked out

Position: beat 5, roughly 4:25 to 5:35.

What the learner already holds, each established separately: a query scored
against stored keys (beat 3); values as what each key hands over (beat 4);
hard selection that answers but cannot learn (beat 4, scene 1); the
exponentiate-and-normalize blend that restored the gradient (beat 4, scene
2). Nothing new enters the aha beat. That is the point.

The blocking:

1. Freeze the machine. Three columns on screen: the thing you ask with, the
   things stored under labels, the things handed back.
2. Prediction P4, three seconds of silence: "You have seen this shape
   before. Where?" The learner is one step from the connection; most of this
   audience will make it here, because they know dicts cold (brief,
   audience).
3. A Python dict slides in beside it: `d = {"cat": ..., "kitten": ...}`.
   Rows morph into correspondence, one row at a time (dossier 1.2 table):
   exact match becomes a continuous score; return-one-value becomes
   return-a-blend; KeyError becomes impossible, the weights just spread.
   Motion is the argument: each dict row physically becomes its attention
   row.
4. The sentence trues up on screen, freehand to exact, mint glow on the
   final word: **"Attention is a soft lookup table."** (Brand: the aha
   always executes a true-up.)
5. The history pays off: this blend is exactly what the intern implemented,
   softmax-weighted averaging, and it worked on the first try. He called it
   RNNSearch. By his recollection, the better name arrived in one of
   Bengio's final passes: attention (dossier 2A, delivered as recollection).
6. The curve from the hook completes: over the collapsing RNNencdec line
   from beat 1, the RNNsearch line draws in flat. 17.82 BLEU against 26.75
   on long sentences, redrawn from Bahdanau et al. Figure 2 and Table 1
   (dossier 2A, 6). Then the stakes, one breath: two years later Google
   Translate went neural in production, 18 million translations a day on the
   first pair, on a service translating over 100 billion words a day; three
   years later the transformer threw away the recurrence and kept only this
   (dossier 6, verified numbers only).
7. Misconception 1 refutation lands here, as the correct account of what
   the amber bars are: proportions of a blend. Plumbing, not reasons.

Emotional shape: recognition ("I built this"), then vindication (the curve
the hook left broken gets fixed by the learner's own machine), then scale
(it is inside everything they use). The learner was one step from the
connection and took it themselves at P4; the reveal confirms rather than
announces.

---

## 6. The breadcrumb

Label: "For the walk home" (BRAND vocabulary).

Setup, ten seconds: shuffle the stored key-value pairs on screen. The
weights shuffle with them; the output vector does not move a digit
(dossier 1.2, permutation row: exact, not approximate). A dictionary has no
idea what order you wrote it in. Neither does attention.

The question, posed and then left alone:

> "The cat sat on the mat." "The mat sat on the cat." Same tokens, same
> keys, same values, same blend. A machine that looks everything up at once
> cannot tell those sentences apart. Your language absolutely can. So what
> is the cheapest thing you could add to a token so that WHERE it sits
> becomes something a lookup can find? That's session 2. Also waiting there:
> why run one lookup when you can afford eight in parallel.

This is D-O2 executed as an information gap: multi-head and positional
encoding are named as destinations, not taught.

---

## 7. Landing lines (one per major section, drafted)

1. Hook: "The fix wasn't a better squeeze. It was refusing to squeeze."
2. Gap: "Gradients need a slope, and a choice is a cliff."
3. Elemental unit: "Alignment is the score. Your hands already know it."
4. Build & complicate: "The lookup didn't fail to answer. It failed to
   learn."
5. Aha: "Attention is a soft lookup table." (trued on screen; the canonical
   sentence is the landing line)
6. Compression: "Softness isn't the compromise. Softness is why it can
   learn at all."
7. Stress-test: "Same skeleton, opposite hardness."
8. Breadcrumb: "A dictionary doesn't know what order you wrote it in.
   Neither does this."

---

## 8. Beat-by-beat treatment (video track)

Narration: ElevenLabs Matilda, ~150 wpm. All on-screen text obeys the
AI-tell ban; zero em-dashes anywhere. Colors by token only: query wears
data.heat amber, keys data.observed periwinkle, scores data.params lilac,
background bg, labels text cream (matching both PASSED assets). Values need
a fourth series color; suggest data.truth with a Director/Vera check that it
reads against cream labels (color is never the sole channel regardless).

### Beat 1: Hook (0:00 to 1:20, 80s)

- **What happens:** cold open as written in section 1. Title card true-up
  fires on the first syllable (BRAND fixed surface).
- **Visuals:** [connect-to-reality] a sentence funnels into a literal box
  labeled "8,000 numbers"; short sentence, long clause, same box. Then the
  degradation curve draws itself: BLEU falling as sentence length grows,
  redrawn honestly from the dossier's verified figures; ONLY the collapsing
  line appears; the axes stay on screen, unresolved, and the frame is
  deliberately left half-empty. [dynamic-process] the reversal hack shown as
  the sentence physically flipping. Timeline chip: Sep 1 before Sep 10, so
  the intern precedes the paper he supposedly answered.
- **Emotional beat:** absurdity plus sympathy. The best lab in the world is
  reading sentences backwards; you are allowed to laugh, because the wall is
  real.
- **Jokes:** one, template 1, in the cold open ("what if the first words
  were just... closer"). Open-Sign Rose accent fires here (rationed use 1
  of 2).
- **Notation:** none. No symbols, no vocabulary. The word "attention" is not
  said in this beat and stays unsaid until beat 5.
- **Prediction/retrieval:** none yet; the open loop is the half-drawn curve.

### Beat 2: Gap (1:20 to 2:00, 40s)

- **What happens:** "look back at every word" hits its trap. Looking is
  choosing. A choice is discrete. Gradients need continuity. The question
  the whole session answers, spoken as the advance organizer (L5): "How do
  you learn where to look?"
- **Visuals:** [dynamic-concept] a selector arm over the source words;
  nudge the parameters and the arm does not move at all, nudge again and it
  slams to a different word. A step function draws underneath: flat, cliff,
  flat. Slope zero everywhere you can stand.
- **Emotional beat:** the trap door. The obvious repair is illegal, and now
  the learner wants the workaround personally.
- **Notation:** none.
- **Prediction P1 (pause-and-ponder card):** "How do you make 'where to
  look' something a gradient can touch? Ten seconds. Wrong guesses count
  double." Lands BEFORE any mechanism appears (L4).

### Beat 3: Elemental unit (2:00 to 3:00, 60s)

- **What happens:** strip the problem to its smallest piece. Forget
  translation; you are mid-sentence and you need cat-flavored information.
  One probe vector, four stored candidates, and a number that says how
  well each candidate matches: the dot product.
- **Visuals:** **PLACED ASSET: qk-similarity (PASSED, 24s), verbatim.** One
  amber query q sweeps; four periwinkle keys hold still; lilac score bars
  rise and die with alignment [covary | dynamic-concept]. After the sweep,
  the keys take names: cat, kitten, car, sofa, at the dossier 1.5
  coordinates, and q parks at [2, 0], the "feline-ish" probe.
- **Misconception 3 voiced and refuted here** (section 4): alignment, not
  sameness.
- **Emotional beat:** relief and play. After two beats of walls, the learner
  gets a toy that responds.
- **Notation timing:** labels on objects only (q, k1..k4, then token names).
  After the sweep has been FELT, the score bar earns a pre-formal annotation
  in periwinkle mono: "q . k". That is the entire symbol budget of the beat
  (L3: manipulation strictly precedes annotation).
- **Prediction P2 (before the sweep starts):** freeze frame, "q is about to
  sweep from 0 to 180 degrees. Call the order the bars peak." Payoff plays
  immediately in the asset.
- **Page track:** qk-explorer (PASSED) embeds beside this beat; the learner
  drags the angle themselves. Its states (initial, mid-drag,
  aligned-with-k1, anti-aligned) are the beat's checkpoints.

### Beat 4: Build & complicate (3:00 to 4:25, 85s, two scenes)

**Scene 4.1, the wall (45s).**

- **What happens:** values enter: each key carries a chip, the content it
  hands over when found (pre-trained as objects before interacting, R12).
  Natural first approach: score every key, take the winner, return its
  value. Run it: cat scores 4, wins, cat's value comes back. Correct.
  Then try to LEARN with it. Backprop meets the argmax: wiggle q's
  direction, the winner does not change, the output does not change, the
  gradient meter reads zero. Push past the boundary and the output
  teleports. The step function from beat 2 is now sitting inside our toy
  with numbers on it.
- **Visuals:** [dynamic-process] a gradient meter attached to the output;
  flatline as q wiggles; discontinuous jump at the boundary. The beat-2
  cliff drawn under the bars, this time earned numerically.
- **Emotional beat:** the felt obstruction. This is the steer's core: the
  learner watches the honest approach answer perfectly and learn nothing.
  Empathic reframe, spoken: "That's not a failure of effort. It's the shape
  of the function."
- **Notation:** none new. The word argmax may appear as an on-object label
  only after the cliff has been seen.
- **Prediction P3 (pause card):** "Keep the ranking. Lose the cliff. What is
  the smallest edit you can make?"

**Scene 4.2, the escape (40s).**

- **What happens:** never choose. Give every value partial credit in
  proportion to its score: exponentiate each score (everything positive),
  divide by the sum (they now total 1). The four weights appear: 0.766,
  0.186, 0.045, 0.003. Blend the value chips in those proportions: the
  output lands at [0.912, 0.083]. Mostly cat, a little kitten, trace of
  car, nothing of sofa (dossier 1.5, exact numbers). Now wiggle q: weights
  slide smoothly, output slides smoothly, the gradient meter comes alive.
- **Visuals:** [covary] bars morph from winner-take-all to proportions; the
  blend shown as chips pouring into one output chip; gradient meter waking
  up. The amber weight bars settle over the four tokens and hold: the frame
  is now visually identical to an attention heatmap.
- **Misconception 1 voiced here, deliberately unresolved** (section 4): "So
  cat is 77 percent of the why." Held open across the beat boundary.
- **Emotional beat:** escape velocity, with one splinter left in (the
  heatmap question).
- **Notation:** still none. "Exponentiate and normalize" is performed, not
  named; softmax the word is banked for beat 6 (L3).

### Beat 5: Aha (4:25 to 5:35, 70s)

Blocked in full in section 5. Prediction P4 ("You have seen this shape
before. Where?") is the engineered connection point; the dict morph, the
true-up of the canonical sentence, the RNNSearch naming recollection, the
Figure 2 completion, the verified deployment stakes, and the misconception 1
refutation (recipe proportions, plumbing not reasons) land in that order.
Visual roles: [connect] dict-to-attention row morph; [connect-to-reality]
curve completion and deployment stakes.

- **Notation:** none. The beat runs entirely on the objects the learner has
  already touched. The formula is NOT shown yet; the sentence is the only
  new text on screen.

### Beat 6: Compression (5:35 to 6:45, 70s, two scenes)

**Scene 6.1, writing it small (35s).**

- **What happens:** "Everything you just watched, written small." Build the
  formula term by term, each symbol color-matched and spatially attached to
  the object it compresses: out = sum_j a_j v_j, then a =
  softmax(q K^T / sqrt(d_k)). The word softmax is spoken for the first time,
  naming the exponentiate-and-normalize the learner already performed.
- **Misconception 2 voiced and refuted** (section 4): 0.766 is not 1.0;
  kitten's 0.186 is visibly inside [0.912, 0.083].
- **Visuals:** [symbol-sense] the fade shown: bars and chips morph INTO the
  symbols that name them; q stays amber in the formula, K periwinkle, the
  score expression lilac. The formula trues up as a whole once assembled.
- **Notation timing:** this is the first appearance of every symbol except
  the pre-formal "q . k" from beat 3 (L3 satisfied; the Rigor Writer owns
  exact symbol timing from here).

**Scene 6.2, the limit test (35s).**

- **What happens:** the aha sentence is a claim, so try to break it.
  Prediction P5: "Multiply every score by 20. What do the weights become?"
  Reveal: sharpen 5x and the weights hit 0.9992 / 0.0008; sharpen 20x and
  they are 1, 0, 0, 0 to eight decimal places. The literal hard dict
  returns on screen (dossier 1.4, 1.5). Then the kicker: at that limit the
  gradient dies again, weight times one-minus-weight goes to zero. The
  hard lookup was never wrong. It was unlearnable. Softness is why the
  gradient flows.
- **Honesty callouts, one line each (video), full versions on page:**
  (a) sqrt(d_k) keeps typical scores near unit size so wide models do not
  freeze the softmax; the paper's own word for the why is "suspect," so: it
  keeps the gradients healthy, probably (joke 2 of 2, template 2, and true
  to the source; dossier 1.3). (b) 2014's version scored with a small
  feedforward net; dot products came in 2015, the scaling in 2017 (dossier
  1.6.5). (c) Real transformers run several of these lookups in parallel
  with learned projections; ours is theirs with h = 1 (dossier 1.6.1,
  1.6.6; points at the breadcrumb).
- **Emotional beat:** the metaphor survives its own falsification test, and
  the session's two walls (beat 1's box, beat 4's cliff) are revealed as one
  wall: hardness.

### Beat 7: Stress-test and second instance (6:45 to 7:35, 50s)

- **What happens:** surface-different second instance the audience runs at
  work: RAG. Embed the question: a query vector. Compare against a vector
  index: keys. Fetch passages: values. Aligned side by side with attention,
  the shared structure NAMED: a lookup with three objects and a score
  (R28). Differences told honestly: RAG's lookup is hard (top-k) and
  external, and you cannot backprop through the index; attention's is soft
  and internal, one per layer, learned end to end (dossier 5.2). Same
  skeleton, opposite ends of the hard-soft dial.
- **Honest edges:** one sentence on the causal mask (decoder LLMs zero out
  future keys before the softmax; mechanism otherwise unchanged, dossier
  1.6.3). Then the heatmap splinter removed with scope discipline: on BiLSTM
  classifiers in 2019, very different attention maps produced the same
  predictions, and the maps correlated weakly with other importance
  measures; the follow-up debate is genuinely unresolved (dossier 2C). So
  when a demo ships a heatmap as "why," you now know exactly what you are
  looking at: recipe proportions. What was mixed, never why.
- **Visuals:** [generalize] two-column alignment, attention left, RAG
  right, rows lighting up pairwise; the hard-soft dial as a single axis
  with RAG and attention at opposite ends.
- **Notation:** none new; the beat-6 formula persists on screen and gets
  pointed at.
- **Retrieval (R26):** "Point at the query, the keys, and the values in
  your own RAG stack. Out loud is allowed."

### Beat 8: Breadcrumb (7:35 to 8:15, 40s)

- **What happens:** retrieval prompt first: "Rebuild it from memory. Three
  objects. What replaced the exact match, and what replaced returning one
  value?" Then the shuffle demo and the walk-home question exactly as
  blocked in section 6. Close on the recursive image: Bahdanau watched his
  own eyes translate. Session 2 opens with the thing his eyes knew that
  this machine still does not: where the words sit.
- **Visuals:** [dynamic-process] key-value pairs shuffle, weights follow,
  output digits do not move. The two cat/mat sentences rendered as
  identical token bags.
- **Extensions menu ("Still up?", page track, gestured at in video):**
  argue it out with an LLM (steelman "weights are explanations" against the
  2019 papers; walk an LLM through the sharpening limit and hunt for holes);
  read the real thing (Bahdanau et al. 2015, the mechanism hides in the
  appendix; Vaswani et al. 2017, find the word "suspect" in 3.2.1; Jain and
  Wallace 2019 with the Wiegreffe and Pinter rebuttal as a paired fight);
  build something (the committed notebook: dict, one-hot lookup as a dot
  product, relax to softmax, blend, sharpen back to the dict, then check
  which version has a nonzero gradient, dossier 7; stretch: implement
  Nadaraya-Watson 1964 and notice it is this formula, sixty years early,
  dossier 5.1).
- **Notation:** none new.

---

## 9. Asset placement summary

| Asset | Status | Placement |
|-------|--------|-----------|
| qk-similarity video beat (24s) | PASSED, reuse verbatim | Beat 3, the elemental sweep; keys renamed to tokens immediately after |
| qk-explorer interactive | PASSED, reuse verbatim | Page track beside beats 3 and 4; its four saved states are the checkpoint frames |
| Optional new interactive: "harden" toggle on qk-explorer (argmax snap + gradient meter) | NEW BUILD, not required for the arc | Page track at beat 4 if M5 budget allows; makes the cliff a felt obstruction on the page too |

## 10. Disclosure ledger (no-handwave, dossier 1.6)

1. Single head; real models run h in parallel and concatenate (beat 6 line,
   breadcrumb destination).
2. No positional encoding; order-blindness shown honestly and converted
   into the breadcrumb (beat 8).
3. No causal mask; one sentence at beat 7.
4. Sharpening is a property of softmax, not a dial in the transformer; the
   fixed sqrt(d_k) divisor is the principled cousin (beat 6.2 phrasing:
   "sharpen the scores," never "turn the temperature knob").
5. Bahdanau scored with a feedforward net; dot product is Luong 2015,
   scaling Vaswani 2017 (beat 6.2 line, full lineage on page).
6. Projections arrive with multi-head in the source paper; folded into
   disclosure 1 (page callout).

## 11. Timing budget

80 + 40 + 60 + 85 + 70 + 70 + 50 + 40 = 495 seconds. Hard cap 540 (L10).
First trims if the Director needs room: the deployment stakes breath in
beat 5 (10s), scene 4.1's second gradient wiggle (5s).

## 12. Self-audit against the ship gates

- Hook motivates inside 30 seconds, question before any definition: yes
  (the box fails on screen by 0:25; zero definitions in beats 1 to 2).
- Predictions before every major reveal (L4): P1 gap, P2 sweep, P3 escape,
  P4 aha, P5 limit. Retrievals at beats 7 and 8 (L6).
- Notation strictly after manipulation (L3): full ledger in beats 3, 4, 6.
- One new idea per beat, scenes split where needed (L1, L2).
- Misconceptions voiced before correct accounts (L9): section 4.
- Video 495s, under cap (L10).
- No em-dashes, no banned vocabulary, two jokes total, both licensed
  templates, rose accent rationed to those two moments.
- Every fact from dossier.md with the FAILED "billion users" claim absent
  and every PARTIAL item handled per its condition.
