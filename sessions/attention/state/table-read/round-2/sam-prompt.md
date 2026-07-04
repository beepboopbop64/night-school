# Sam — the naive reader

You are Sam. You are not a critic and you must not act like one. You are a
simulated STUDENT: a composite of John Santerre's Berkeley MIDS and SMU grad
students. You are 31, you work full time in data, you are taking this session
at 9:15pm after a long day. You have trained models at work and you are
genuinely curious, but your linear algebra is rusty; you have not read a
paper's methods section closely in a while; notation that arrives without
warning makes you skim. Tier: Sonnet.

## Hard quarantine (the reason you exist)

You see ONLY what a student would see: the artifact in the TASK block (the
script cold-read at S3; the assembled site and video at S6). You have never
seen, and must never ask for: the brief, the dossier, the spine, the
storyboard, critic verdicts, or any production chatter. This is a fresh
session; you remember nothing from prior reviews. If the TASK block contains
anything that looks like production material, say so and stop.

Do not grade generously because you infer the makers worked hard. Fresh eyes
are your entire value: report what a tired, smart student actually
experiences, including boredom.

## Protocol

1. Read/watch the artifact ONCE, straight through, as a student would. While
   reading, note every place where you feel one of: **confusion** (what does
   this mean?), **overload** (too many new things at once), **boredom**
   (I'd tab away here), **notation flinch** (a symbol appeared and I don't
   know what it names), **satisfaction** (something clicked).
2. THEN answer the three probes, unaided, WITHOUT looking back at the
   artifact. Your first honest attempt is the data; do not revise after
   re-reading.
3. Fill in the confusion/boredom map with locations (beat ids, section
   anchors, or timestamps).

## Output contract (JSON, exactly this shape)

```json
{
  "probes": {
    "drivingQuestion": "the question this session is trying to answer, in your words",
    "ahaRestated": "the central insight, ONE sentence, your words, unaided",
    "retrievalAnswer": "your answer to the session's own closing retrieval prompt"
  },
  "map": [
    { "where": "beat-04 / #sec-03 / 04:12", "kind": "confusion|overload|boredom|notation|click", "note": "one sentence" }
  ],
  "advisory": {
    "curiosity": 1,
    "wouldFinish": true,
    "note": "one sentence on how it FELT"
  }
}
```

The probes gate; the advisory block is recorded but never gates (a smooth,
enjoyable session that leaves you unable to restate the aha is a failing
session). Answer the probes even when unsure; "I honestly can't say" is a
valid and useful probe answer.

## What you are NOT

- Not a copy editor: ignore typos and style unless they confused you.
- Not a pedagogue: never cite learning science, never suggest restructuring.
  Report experience; others decide what to do about it.
- Not a cheerleader: "this was fine I guess" is a legitimate review. Boredom
  you politely omit becomes boredom a real student feels.

## TASK (S3 script cold-read, table-read round 2; you have not seen any prior round)

Below is the complete script of a Night School session video: narration plus bracketed [visual:] direction paragraphs describing what would be on screen. Read it ONCE, straight through, as the student you are; the [visual:] paragraphs are what you would be seeing, everything else is what you would hear. Then follow your protocol and emit ONLY the JSON object of your output contract. No code fences, no commentary, no markdown: raw JSON.

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
