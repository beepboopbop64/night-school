# Treatment: attention (merged, S2 final)

```yaml
session: attention
aha: "Attention is a soft lookup table."
base: candidate-obstruction-first
grafts: G1-G12 per treatment/judgment.md
hook: A (the bottleneck that broke translation, dossier 2A)
proposedTitle: "How Do You Take a Gradient Through a Choice?"
proposedSubtitle: "One vector, five weeks, eight thousand numbers."
extendedMetaphor: "the forgiving dictionary"
videoEstimatedSeconds: 505
videoTargetSeconds: 480
videoHardCapSeconds: 540
trimPlan: >-
  B1 -5s (compress reversal), B4 -5s (single gradient wiggle), B6 -10s
  (lineage disclosure to page callout, keep one clause), B8 -5s (stakes to
  two sentences). Floor: 480s.
misconceptionBeats: [B3, B4-B5 primary, B6]
absorbedAssets:
  - qk-similarity (PASSED video beat, verbatim in B3)
  - qk-explorer (PASSED interactive, page track, twinned to B3 and B4)
scope: single-head dot-product attention only, per D-O2 (brief front-matter)
factSource: dossier.md only
```

Four Cs. Causality: box fails, so look back; looking is choosing, so score;
scoring invites picking, so the cliff; the cliff forbids choosing, so blend;
the blend IS the dict gone soft. Conflict: how do you make looking
learnable? Complication: the honest fix answers perfectly and learns
nothing. Character: Sutskever's team reading sentences backwards, Cho's
measurements, and an intern with five weeks left.

---

## 1. The hook, in full

Cold open, first ~158 words, VERBATIM narration (0:00 to ~1:05). This is
the voice sample. Runs over the title-card true-up and the funnel visual.

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

Hook continuation (to ~1:20), prose:

> The intern was Dzmitry Bahdanau, five weeks left in Yoshua Bengio's lab,
> staring at the same wall in his own lab's translator. By his own account,
> the idea came from watching his own eyes: when you translate, your gaze
> shifts back and forth between the source and the thing you're writing. So
> let the model do that. Keep every word. And for each word it writes, let
> it look back.
>
> Which is so obviously the fix that you should be suspicious. If looking
> back is the answer, why did nobody just build it? (G12)

Facts and citations: fixed 8,000-number sentence vector, reversal trick
with single-LSTM BLEU 25.9 to 30.6 (dossier 2A, 6); length degradation
(dossier 2A, Cho et al.); Bahdanau's status, five weeks, gaze account
delivered as his recollection via the published correspondence (dossier 2A,
8 VERIFIED). Cautions honored: Bahdanau attacks the bottleneck in his own
lab's encoder-decoder, not Sutskever's paper; the on-screen timeline chip
shows his arXiv date (Sep 1) before seq2seq's (Sep 10); reversal numbers
attributed to a single LSTM; no "billion users" anywhere (dossier 8,
FAILED item).

---

## 2. The beat list

One new idea per beat; each result creates the next beat's problem.
Stable ids match spine.md.

| id | Beat | The ONE new idea | How it forces the next beat | Est. sec |
|----|------|------------------|------------------------------|----------|
| beat-01 | Hook | A fixed-size vector cannot carry an unbounded sentence, and the field's best fix was a hack | "Look back at every word" is the obvious repair, so why did nobody just do it? | 80 |
| beat-02 | Gap | "Where to look" is a choice, and a choice has no gradient | If choosing is unlearnable, we need the smallest piece of looking we can hold: a score | 40 |
| beat-03 | Elemental unit | A dot product turns "how relevant is this word" into a number that moves with alignment | Scores rank candidates, so the natural move is to take the winner: try it | 60 |
| beat-04 | Build & complicate | Hard selection answers correctly but learns nothing; the escape is to never choose: blend in proportion to score | The blending machine we built has a shape we have seen before | 85 |
| beat-05 | Aha | The machine IS a dictionary with the hardness removed: "Attention is a soft lookup table." | A thing this clean deserves to be written down small | 60 |
| beat-06 | Compression | softmax(qK^T / sqrt(d_k))V is the lookup made soft, term by term; hard lookup is its sharp limit | If the skeleton is really a lookup, it should show up in other lookups we use | 70 |
| beat-07 | Stress-test | RAG has the same three objects at the opposite end of the hard-soft dial; and mixing weights are plumbing, not reasons | The mapping holds everywhere except one row: dictionaries have no order | 60 |
| beat-08 | Breadcrumb | Attention is order-blind, and language is not | Session 2: position, and many lookups in parallel (D-O2) | 50 |

Total: 505 seconds. Cap 540 (L10). Target 480; trim plan in front matter.

---

## 3. Beat-by-beat (video track)

Narration: ElevenLabs Matilda, ~150 wpm. All learner-facing text obeys the
AI-tell ban; zero em-dashes. Colors by token only, per spine.md: query
amber `data.heat`; keys periwinkle `data.observed`; scores AND weights
lilac `data.params` (weights are normalized scores, same family, per
d-s2-weights-stay-lilac); values cream `data.truth` on card-shaped chips
(shape carries the channel, never color alone); blended output and every
true-up mint `data.fit`; rose `data.error` rationed to exactly two moments
(B4 KeyError-and-flatline composite, B7 cross-out).

### beat-01: Hook (0:00 to 1:20, 80s)

- **What happens:** cold open as written in section 1. Title card true-up
  fires on the first narrated syllable.
- **Visuals:** [connect-to-reality] a sentence funnels into a literal box
  labeled "8,000 numbers"; short sentence, long clause, same box. The
  degradation curve draws itself, redrawn honestly from the verified
  artifacts; ONLY the collapsing line appears; the axes stay on screen,
  unresolved, half the frame deliberately empty. [dynamic-process] the
  reversal hack: the sentence physically flips, 25.9 ticks to 30.6.
  Timeline chip: Sep 1 before Sep 10. Then the gaze image (G3): source row
  above, target row below, one amber dot hopping between them. The amber
  dot is the series' query color, planted 60 seconds before anything names
  it.
- **Emotional beat:** absurdity plus sympathy. The best lab in the world is
  reading sentences backwards; you are allowed to laugh, because the wall
  is real.
- **Jokes:** one, template 1 ("what if the first words were just...
  closer"). Open-Sign Rose does NOT fire here; rose is spent at B4 and B7.
- **Notation:** none. The word "attention" is not said and stays unsaid
  until beat-05.
- **Predictions/retrievals:** none; the open loops are the half-drawn curve
  and the closing question.
- **Landing line:** "So why did nobody just build it?"

### beat-02: Gap (1:20 to 2:00, 40s)

- **What happens:** "look back at every word" hits its trap. Looking is
  choosing. A choice is discrete. Gradients need continuity. The advance
  organizer, question form (L5): "How do you learn where to look?"
- **Visuals:** [dynamic-concept] a selector arm over the source words;
  nudge the parameters and the arm does not move at all; nudge again and it
  slams to a different word. A step function draws underneath: flat, cliff,
  flat. Slope zero everywhere you can stand. This exact staircase returns
  inside the toy at beat-04.
- **Emotional beat:** the trap door. The obvious repair is illegal, and now
  the learner wants the workaround personally.
- **Notation:** none.
- **Prediction P1 (pause card):** "How do you make 'where to look'
  something a gradient can touch? Ten seconds. Wrong guesses count double."
- **Landing line:** "Gradients need a slope, and a choice is a cliff."

### beat-03: Elemental unit (2:00 to 3:00, 60s)

- **What happens:** strip the problem to its smallest piece. Forget
  translation; you are mid-sentence and you need cat-flavored information.
  One probe vector, four stored candidates, and a number that says how well
  each candidate matches: the dot product.
- **Visuals:** **PLACED ASSET: qk-similarity (PASSED, 24s), verbatim.** One
  amber query q sweeps; four periwinkle keys hold still; lilac score bars
  rise and die with alignment [covary | dynamic-concept]. After the sweep,
  the keys take names at the dossier 1.5 coordinates: cat [2, 0], kitten
  [1, 1], car [0, 2], sofa [-2, 0]; q parks at [2, 0], the feline-ish
  probe; raw scores appear as integers: 4, 2, 0, -4. Sofa's negative score
  is left unnarrated; the sweep already showed anti-alignment (medium
  inference, deliberate).
- **Misconception `similarity-means-identical` voiced and refuted here:**
  "a high score means the tokens are the same kind of thing." Refuted by
  the seed itself: the keys never move, every score rises and dies purely
  with the query's direction. Alignment in a learned space, not sameness;
  one spoken line notes the space is trained (full W_Q, W_K story in a page
  aside).
- **Emotional beat:** relief and play. After two beats of walls, a toy that
  responds.
- **Notation timing:** labels on objects only (q, k1..k4, then token
  names). After the sweep is FELT, one pre-formal annotation in periwinkle
  mono: "q . k". That is the beat's entire symbol budget (L3).
- **Prediction P2 (before the sweep):** freeze frame, "q is about to sweep
  from 0 to 180 degrees. Call the order the bars peak." Payoff plays
  immediately in the asset.
- **Page track:** qk-explorer (PASSED) embeds beside this beat; states
  (initial, mid-drag, aligned-with-k1, anti-aligned) are the checkpoints.
- **Landing line:** "Alignment is the score. Your hands already know it."

### beat-04: Build & complicate (3:00 to 4:25, 85s, two scenes)

**Scene 4a, the wall (45s).**

- **What happens:** values enter: each key carries a cream card, the
  content it hands over when found (pre-trained as objects before
  interacting). Natural first approach: score every key, take the winner,
  return its value. Run it: cat scores 4, wins, cat's card comes back.
  Correct. Rearrange the picture into two columns, keys left, values right:
  it is a Python dictionary, and the learner is told so by their own eyes
  before any label lands. The code well appears (G4): `d["cat"]` returns
  before you finish blinking; `d["feline"]` dies in KeyError rose, one
  synonym away from a key it is literally holding. Our vector version is
  better in exactly one way: it can score near-misses. But watch what the
  pick does with them (G5): kitten scored 2, half of cat's 4, real
  information about what feline means, and the pick is like "kitten,
  noted... anyway, one hundred percent cat." Then the deep break: try to
  LEARN with it. Wiggle q's direction, the winner does not change, the
  output does not change, the gradient meter reads zero. Push past the
  boundary and the output teleports. The beat-02 staircase is now sitting
  inside our toy with numbers on it.
- **Visuals:** [dynamic-process] gradient meter attached to the output;
  flatline as q wiggles; discontinuous jump at the boundary. KeyError and
  the flatline are the session's first rose moment (one composite spend).
- **Emotional beat:** recognition ("I know this object"), then the felt
  obstruction: the honest approach answers perfectly and learns nothing.
  Empathic reframe, spoken: "That's not a failure of effort. It's the shape
  of the function."
- **Notation:** none new. "Take the biggest" is said in words; argmax may
  appear as an on-object label only after the cliff is seen.
- **Prediction P3 (pause card):** "Keep the ranking. Lose the cliff. What
  is the smallest edit you can make?"

**Scene 4b, the escape (40s).**

- **What happens:** never choose. Give every value partial credit in
  proportion to its score. First, one piece of bookkeeping, disclosed as
  bookkeeping (G1): shrink the scores by the square root of the vector
  length, 1.41 here. The why costs two minutes and gets paid in full at
  the formula. Then exponentiate (everything positive), divide by the sum
  (they now total 1). The four weights appear: 0.766, 0.186, 0.045, 0.003.
  Blend the value cards in those proportions: the output lands at
  [0.912, 0.083]. Mostly cat, a little kitten, trace of car, nothing of
  sofa (dossier 1.5, exact). Now wiggle q: weights slide smoothly, output
  slides smoothly, the gradient meter comes alive.
- **Visuals:** [covary] lilac bars morph from winner-take-all to
  proportions; value cards pouring into one mint output chip; gradient
  meter waking up. The lilac weight bars settle over the four tokens and
  hold: the frame is now structurally identical to an attention heatmap
  (layout makes the pun; colors stay locked).
- **Misconception `attention-weights-are-explanations` (primary) voiced
  here, deliberately unresolved:** "Wait, I know this picture. 0.766 on
  cat. So cat is 77 percent of the why." Held open across the beat
  boundary.
- **Emotional beat:** escape velocity, with one splinter left in.
- **Notation:** still none. "Exponentiate and normalize" is performed, not
  named; the word softmax is banked for beat-06 (L3).
- **Landing line:** "The lookup didn't fail to answer. It failed to learn."

### beat-05: Aha (4:25 to 5:25, 60s)

Nothing new enters this beat. That is the point.

1. Freeze the machine. Three columns: the thing you ask with, the things
   stored under labels, the things handed back.
2. **Prediction P4**, three seconds of silence: "You have seen this shape
   before. Where?" Most of this audience makes the connection here; they
   know dicts cold.
3. The Python dict from scene 4a slides in beside it. Rows morph into
   correspondence, one row at a time (dossier 1.2): exact match becomes a
   continuous score; return-one-value becomes return-a-blend; KeyError
   becomes impossible, the weights just spread. Motion is the argument:
   each dict row physically becomes its attention row.
4. The sentence trues up on screen, freehand to exact, mint glow on the
   final word: **"Attention is a soft lookup table."** (The aha always
   executes a true-up.)
5. Misconception 1 refutation lands as the correct account of what the
   lilac bars are: proportions of a blend. A recipe card tells you what got
   mixed, not why the recipe was chosen; the choosing lives upstream, in
   the learned scoring that built those numbers. Plumbing, not reasons.
   (Empirical teeth deferred to beat-07.)
6. History pays off: this blend is exactly what the intern implemented,
   softmax-weighted averaging, and it worked on the first try. He called it
   RNNSearch; by his recollection, the better name arrived in one of
   Bengio's final passes (delivered as recollection, dossier 2A). The curve
   from the hook completes: over the collapsing line, the rescue line draws
   in flat. 17.82 against 26.75 BLEU on long sentences, redrawn from
   Figure 2 and Table 1.
- **Visuals:** [connect] dict-to-attention row morph, THE morph of the
  session; [connect-to-reality] Figure 2 completion.
- **Notation:** none. The sentence is the only new text on screen.
- **Emotional shape:** recognition ("I built this"), then vindication (the
  curve the hook left broken gets fixed by the learner's own machine).
- **Landing line:** the canonical sentence itself.

### beat-06: Compression (5:25 to 6:35, 70s, two scenes)

**Scene 6a, writing it small (35s).**

- **What happens:** "Everything you just watched, written small." The
  formula assembles term by term, each symbol color-matched and spatially
  attached to the object it compresses: out = sum_j a_j v_j, then
  a = softmax(q K^T / sqrt(d_k)). The word softmax is spoken for the first
  time, naming the exponentiate-and-normalize the learner already
  performed. The sqrt(d_k) forward reference is paid in full: wide vectors
  make big dot products (typical size grows like the square root of the
  width; at width 2 typical scores sit near 1.4, at width 64 near 8), and
  softmax at 8 versus -8 puts 0.9999997 on the winner, a slope of roughly
  three in ten million: a frozen layer. Divide by sqrt(d_k) and the same
  preference stays alive, gradient breathing again. Which keeps learning
  healthy, probably; the authors themselves wrote "we suspect" (joke 2,
  template 2, true to the source).
- **Misconception `softmax-picks-the-max` voiced and refuted:** "smooth
  argmax, picks the winner, right?" The numbers refute it: the winner got
  0.766, not 1.0, and kitten's 0.186 is measurably inside [0.912, 0.083].
  Nothing was discarded.
- **Visuals:** [symbol-sense] the fade SHOWN: bars and cards morph INTO the
  symbols that name them; q stays amber in the formula, K periwinkle, the
  softmax expression lilac, V cream. The formula trues up as a whole once
  assembled.
- **Notation timing:** first appearance of every symbol except the
  pre-formal "q . k" (L3 satisfied; Rigor Writer owns exact timing from
  here).

**Scene 6b, the limit test (35s).**

- **What happens:** the aha sentence is a claim, so try to break it.
  **Prediction P5:** "Multiply every score by 20. What do the weights
  become?" Reveal: sharpen 5x and the weights hit 0.9992 / 0.0008; sharpen
  20x and they read 1, 0, 0, 0 to eight decimal places. The literal hard
  dict returns on screen (dossier 1.4, 1.5). Then the kicker: at that limit
  the gradient dies again, weight times one-minus-weight goes to zero. The
  hard lookup was never wrong. It was unlearnable. One demo, two payoffs:
  the misconception dies, and the aha passes its own falsification test.
- **Honesty callouts, one line each in video, full versions on page:**
  (a) sharpening is a property of softmax used as a demonstration; the
  transformer has no temperature knob in this layer, the sqrt(d_k) divisor
  is its fixed, principled cousin. (b) 2014's version scored with a small
  feedforward net; dot products came in 2015, the scaling in 2017 (one
  clause in video, lineage on page, per trim plan).
- **Emotional beat:** the session's two walls (beat 1's box, beat 4's
  cliff) are revealed as one wall: hardness.
- **Landing line (G7):** "Gradient flows only while the lookup stays soft."

### beat-07: Stress-test and second instance (6:35 to 7:35, 60s)

- **What happens:** surface-different second instance the audience runs at
  work: RAG. Embed the question: a query vector. Compare against a vector
  index: keys. Fetch passages: values. Aligned side by side with attention,
  the shared structure NAMED: a lookup with three objects and a score. The
  learner fills the mapping first (alignment table appears with blanks, ten
  seconds of silence). Differences told honestly: RAG's lookup is hard
  (top-k) and external, and you cannot backprop through the index;
  attention's is soft and internal, one per layer, learned end to end. Same
  skeleton, opposite ends of the hard-soft dial. One sentence on the causal
  mask (decoder LLMs zero out future keys before the softmax; mechanism
  otherwise unchanged). Then the splinter from beat-04 comes out.
  **Prediction P6 (G8):** "The model put 40 percent of its attention on
  'terrible', so 'terrible' is 40 percent of why it said negative. True or
  false?" Then the 2019 result, scope-disciplined: on BiLSTM classifiers
  (not transformers, and the authors say so), very different attention maps
  produced the same predictions, and the maps correlated weakly with other
  importance measures; the follow-up debate is genuinely unresolved. So
  when a demo ships a heatmap as "why," you know exactly what you are
  looking at: recipe proportions. What was mixed, never why.
- **Visuals:** [generalize] two-column alignment, attention left, RAG
  right, rows lighting pairwise; the hard-soft dial as a single axis with
  RAG and attention at opposite ends. [dynamic-concept] the dual-heatmap
  morph (G8): two different lilac weight maps over the same review
  collapsing into the same output bar; the false explanation crossed out in
  rose, the session's second and final rose spend.
- **Notation:** none new; the beat-06 formula persists and gets pointed at
  ("point at the part of the formula RAG replaces with a top-k").
- **Retrieval:** "Point at the query, the keys, and the values in your own
  RAG stack. Out loud is allowed."
- **Landing line:** "Same skeleton, opposite hardness."

### beat-08: Breadcrumb (7:35 to 8:25, 50s)

- **What happens:** retrieval prompt first: "Rebuild it from memory. Three
  objects, two operations. What replaced the exact match, and what replaced
  returning one value?" Then the shuffle demo: key-value pairs permute, the
  weights shuffle with them, the output does not move a digit (dossier 1.2,
  exact). A dictionary has no idea what order you wrote it in. Neither does
  attention. The walk-home question, posed and left alone:

  > "The cat sat on the mat." "The mat sat on the cat." Same tokens, same
  > keys, same values, same blend. A machine that looks everything up at
  > once cannot tell those sentences apart. Your language absolutely can.
  > So what is the cheapest thing you could add to a token so that WHERE it
  > sits becomes something a lookup can find? That's session 2. Also
  > waiting there: why run one lookup when you can afford eight in
  > parallel.

  Then the stakes, two sentences (G6, verified numbers only): two years
  later Google Translate went neural in production, on a service with more
  than 500 million users translating over 100 billion words a day; three
  years later Vaswani and colleagues threw away the recurrent network and
  kept only the fix. Close recursive on the hook: Bahdanau watched his own
  eyes translate. Session 2 opens with the thing his eyes knew that this
  machine still does not: where the words sit.
- **Visuals:** [dynamic-process] pairs shuffle, weights follow, output
  digits frozen, ten seconds, wordless except the landing. The cat/mat
  sentences rendered as identical token bags. Closing card in brand
  microcopy ("For the walk home: how does order get in?").
- **Extensions menu ("Still up?", page track, gestured at in video):** full
  spec in spine.md. Three doors: argue it out with an LLM, read the real
  thing, build something (the committed notebook ladder).
- **Notation:** none new.
- **Landing line:** "The fix outlived the architecture it rescued."

---

## 4. The extended metaphor

**The forgiving dictionary.** The one data structure every learner in this
room used this week, rebuilt so a near-miss key gets partial credit instead
of a KeyError. Built namelessly from beat-03, recognized at beat-04's code
well, named soft at beat-05, proven in the limit at beat-06, cousined at
beat-07, and its one inherited flaw (no order) becomes beat-08's question.
The full registry with per-row honesty boundaries lives in spine.md (drift
ledger, G9); the correspondence is demonstrated row by row, never asserted.

Secondary image, used exactly twice: the weights are **recipe
proportions**. A recipe card tells you what got mixed, not why the recipe
was chosen. Appears at the beat-05 refutation and once in beat-07. No other
metaphors.

---

## 5. The misconception beats

All three seeded ids fire (L9), each voiced in the learner's own words
before the correct account.

1. **`attention-weights-are-explanations` (primary).** Voiced late in
   beat-04b over the first render of the lilac weight bars ("0.766 on cat.
   So cat is 77 percent of the why."), held open across the beat boundary,
   refuted in beat-05 as the correct account of the weights (recipe
   proportions, plumbing not reasons), re-cashed with scoped empirical
   teeth in beat-07 (Jain and Wallace 2019 on BiLSTM classifiers; the
   debate named as unresolved).
2. **`softmax-picks-the-max`.** Voiced and refuted in beat-06a the instant
   softmax is named; the sharpening demo in 6b shows where the intuition
   actually lives: only in the limit.
3. **`similarity-means-identical`.** Voiced and refuted inside beat-03 on
   the qk-similarity sweep: alignment in a learned space, not sameness.

---

## 6. Landing lines (one per beat, drafted)

1. "So why did nobody just build it?"
2. "Gradients need a slope, and a choice is a cliff."
3. "Alignment is the score. Your hands already know it."
4. "The lookup didn't fail to answer. It failed to learn."
5. "Attention is a soft lookup table."
6. "Gradient flows only while the lookup stays soft."
7. "Same skeleton, opposite hardness."
8. "The fix outlived the architecture it rescued."

---

## 7. Production notes

**Asset placement.** qk-similarity (PASSED, 24s) verbatim in beat-03, keys
renamed to tokens immediately after; qk-explorer (PASSED) on the page track
twinned to beats 03 and 04, existing states as checkpoints. Optional new
build if M5 budget allows (not required for the arc): a "harden" toggle on
qk-explorer (argmax snap plus gradient meter) making beat-04's cliff a felt
obstruction on the page too.

**Disclosure ledger (no-handwave, dossier 1.6).**
1. Single head; real models run h in parallel and concatenate (beat-06
   clause, breadcrumb destination).
2. No positional encoding; order-blindness shown honestly and converted
   into the breadcrumb (beat-08).
3. No causal mask; one sentence at beat-07.
4. Sharpening is a property of softmax, not a transformer dial; sqrt(d_k)
   is the fixed principled cousin (beat-06b; say "sharpen the scores,"
   never "turn the temperature knob").
5. Bahdanau 2014 scored with a feedforward net; dot product is Luong 2015,
   scaling Vaswani 2017 (one clause beat-06b, full lineage on page).
6. The learned projections arrive with multi-head in the source paper;
   folded into disclosure 1 (page callout).
7. The sqrt(d_k) division is performed at beat-04b as named bookkeeping,
   with the why paid at beat-06a (G1; keeps every on-screen number exact to
   dossier 1.5).

**Timing budget.** 80 + 40 + 60 + 85 + 60 + 70 + 60 + 50 = 505s. Cap 540.
Trim plan to 480 in front matter.

**Self-audit against the ship gates.**
- Hook motivates inside 30 seconds; explicit question closes beat-01; zero
  definitions before beat-03.
- Predictions before every major reveal (L4): P1 gap, P2 sweep, P3 escape,
  P4 aha, P5 limit, P6 heatmap verdict. Retrievals at beats 07 and 08 (L6).
- Notation strictly after manipulation (L3): ledger in beats 03, 04, 06.
- One new idea per scene; splits at 4a/4b and 6a/6b (L1, L2).
- Misconceptions voiced before correct accounts (L9): section 5.
- Video 505s estimated, under cap, trim plan recorded (L10).
- No em-dashes, no banned vocabulary; two jokes plus one licensed deflating
  hedge, all template-conforming; rose spent exactly twice.
- Every fact from dossier.md; the FAILED "billion users" claim absent;
  every PARTIAL item handled per its condition; naming anecdote delivered
  as recollection.
