# Script: attention

Final video narration, one section per storyboard beat. Narration
paragraphs are the spoken words, read at roughly 150 words per minute,
with no em-dashes and no emojis. Bracketed `[visual:]` paragraphs are the
video's stage directions: what is on screen while the words are spoken.
The leading words inside each bracket (connect, covary, and so on) are
direction shorthand for the kind of motion.

## beat-01: The box that broke translation

[visual: connect-to-reality] Title card: a lit window blooms on a deep night-sky field, the title "How Do You Take a Gradient Through a Choice?" in cream, and a freehand underline that trues into an exact glowing mint line on the first narrated syllable.

In 2014, the best neural translator on Earth worked like this: read the whole sentence, squeeze everything you understood into one fixed list of 8,000 numbers, then write the translation from that list alone. Every sentence got the same box. "The cat sat." 8,000 numbers. A sixty word contract clause with three nested caveats. The same 8,000 numbers.

[visual: connect-to-reality] A sentence funnels into a literal box labeled "8,000 numbers"; a short sentence and a sixty word clause squeeze into the same box. A quality-versus-length curve draws itself: only the collapsing line, its y axis labeled "BLEU: translation quality, higher is better"; the axes hold on screen, unresolved, half the frame deliberately empty.

You can guess what the data showed: translation quality fell apart as sentences got longer. And the fix that actually shipped is my favorite desperate hack in the history of the field. They fed the sentence in backwards. That's it. Reverse the input, and a single LSTM's BLEU score jumped from 25.9 to 30.6. The model is like, wow, what if the first words were just... closer. And it worked. That's the uncomfortable part. It worked, and it changed nothing, because the box was still a box.

[visual: dynamic-process] The sentence physically flips end to end while the BLEU readout ticks from 25.9 to 30.6. A timeline chip places Sep 1 before Sep 10.

So the field kept squeezing. And an intern in Montreal decided to stop.

[visual: connect-to-reality] Source row above, target row below, one amber dot hopping between them the way a translator's eyes move.

The intern was Dzmitry Bahdanau, five weeks left in Yoshua Bengio's Montreal lab. By his own account, the idea came from watching his own eyes: when you translate, your gaze hops back and forth between the source and the line you're writing. Keep every word, and for each word the model writes, let it look back. So why did nobody just build it?

## beat-02: Looking is choosing

[visual: dynamic-concept] A selector arm hovers over the source words. Parameters nudge: the arm holds perfectly still. Nudge again: it slams to a different word with no in-between.

Here's the trap. To look back, the model has to decide where, and where is a choice. This word, not that one. Watch what a choice does to learning. Nudge the parameters. The selector arm doesn't move. Nudge again. It slams to a different word.

[visual: covary] A step function draws itself in periwinkle under the arm as it moves: flat, cliff, flat, a staircase with slope zero on every tread. A pause card asks: How do you learn where to look?

Flat, cliff, flat. The slope is zero everywhere you can stand, and training means following slopes. Here's the question of the night: how do you learn where to look? Take ten seconds. Gradients need a slope, and a choice is a cliff.

## beat-03: One query, asked of every key

[visual: covary | dynamic-concept] A freeze frame before anything moves carries a prediction card: call the order the bars will peak. Then one amber query vector, labeled q on the object, sweeps through its directions; four periwinkle key vectors hold still; under each key a lilac score bar with a numeric readout rises and dies with the query's alignment, live.

Strip it to the smallest piece. Forget translation. You're mid sentence and you need cat flavored information. One probe vector, four stored candidates. Before it moves, call the order the bars will peak.

A query is a question you ask every key at once. Sweep it across the row and each dot product answers out loud: point the same way and the score climbs, point away and it dies.

[visual: dynamic-concept] After the sweep the keys take names: cat, kitten, car, sofa. q parks at cat's direction; raw scores land as integers on the bars: 4, 2, 0, -4. One small annotation appears in periwinkle mono italic: "q . k". Every label sits on its object; no legends.

The candidates take names: cat, kitten, car, sofa. Park the probe near cat: four, two, zero, minus four. Then a high score means two tokens are the same kind of thing, right? But the keys never moved. Every score rose and died with the probe's direction alone. Alignment in a learned space, not sameness. Alignment is the score. Your hands already know it.

## beat-04a: The perfect answer that learns nothing

[visual: dynamic-process] A cream card clips onto each key, shown one at a time before anything interacts. The score-then-pick machine runs once: cat's bar wins, cat's card slides out.

Each key now carries a card, the content it hands over when found. The obvious machine: score every key, take the winner, return its card. Cat wins. Correct.

[visual: connect] The picture rearranges into two columns, keys left, cards right, and holds a beat. A code well appears: d["cat"] returns instantly; d["feline"] dies in a rose KeyError.

Rearrange it: keys left, cards right. You know this object: a Python dict. Ask for cat, instant answer. Ask for feline, KeyError, one synonym from a key it's literally holding. Our version scores the near miss, kitten earned a two, and the pick just shrugs: kitten, noted... anyway, one hundred percent cat.

[visual: dynamic-process] A gradient meter attaches to the output. The query wiggles: bars shiver, winner holds, output frozen, the meter flatlines in rose. A larger push teleports the output card; the staircase from earlier redraws under the toy, now with the actual scores on its treads. A pause card asks: Keep the ranking. Lose the cliff. What is the smallest edit you can make?

Try to learn with it. Wiggle the query. Winner unchanged, output unchanged, gradient zero. Push further and the output teleports. The staircase is back, with numbers. That's not a failure of effort. It's the shape of the function. Keep the ranking. Lose the cliff.

## beat-04b: Never choose

[visual: covary] The lilac bars morph from winner-take-all to proportions: scores shrink by 1.41, exponentiate, normalize; the weights land as 0.766, 0.186, 0.045, 0.003. The value cards pour into one mint output chip reading [0.912, 0.083].

Never choose. Give every card partial credit in proportion to its score. One piece of housekeeping: divide every score by the square root of the vector length, one point four one here. The why lands in two minutes. For now it keeps the numbers tame. Exponentiate: everything positive. Divide by the sum: they total one. Blend the cards in those proportions. Mostly cat, a real slice of kitten, almost nothing else.

[visual: dynamic-process] The query wiggles: weights slide smoothly, the output chip drifts smoothly, the gradient meter wakes. The lilac weight bars settle over the four tokens and hold.

Wiggle the query. Weights slide, output slides, the meter is alive. Wait. You know these bars. Point seven seven on cat, so cat is seventy seven percent of the why. Right? Hold that thought. The lookup didn't fail to answer. It failed to learn.

## beat-05: You have built this before

[visual: connect] The machine freezes into three columns: amber probe, periwinkle keys, cream cards. The dict code well from earlier slides in beside it. Three seconds of silence on a prediction card: You have seen this shape before. Where?

Freeze the machine. Three columns: the thing you ask with, the things stored under labels, the things handed back. You have seen this shape before. Where?

[visual: connect] The first dict row morphs with no words spoken: exact match stretches into a continuous score bar, then holds a full beat. Only then do the remaining rows follow in sync with the narration: the single returned value fans into a weighted blend; the KeyError row dissolves as the weights spread. The sentence trues up on screen, freehand to exact, mint glow on the final word.

The dict from earlier slides in. Watch the first row argue for itself. Exact match, relaxed into a continuous score. Return one value becomes return a blend. KeyError becomes impossible: the weights just spread. Row by row, the dict you use every day becomes the machine you just built. Attention is a soft lookup table. And those lilac bars? A recipe card: what got mixed, never why the recipe was chosen. The choosing lives upstream, in the scoring that learned to build those numbers.

[visual: connect] As the recipe line is spoken, a literal recipe card renders under the lilac weight bars: the four proportions listed as ingredients (0.766 cat, 0.186 kitten, 0.045 car, 0.003 sofa) under the header "what got mixed"; the card has no why field, and a dim arrow points upstream toward the scoring that built the numbers.

[visual: connect-to-reality] The quality-versus-length curve from the opening returns, and a second line draws in flat above the collapsing one; readouts 17.82 and 26.75 sit on their curves.

This is what the intern implemented, and it worked on the first try. The curve from the opening completes: the rescue line draws in flat.

## beat-06a: Written small

[visual: symbol-sense] The bars and cards morph INTO the symbols that name them, term by term, each symbol spatially attached to its object: an amber q lifts off the probe, K off the periwinkle keys, the softmax expression wraps the lilac weights, V off the cream cards; sqrt(d_k) docks under the score term as the 1.41 housekeeping comes due.

Everything you just watched, written small. Weights times values, summed: that's the blend. The weights: softmax of the scores. It's the exponentiate and normalize you already did. Smooth argmax, picks the winner? No. Cat got point seven seven, not one, and kitten is measurably in the answer. It discarded nothing.

[visual: dynamic-process] A width dial demonstrates the debt: at width 64 typical scores hit 8; softmax at 8 versus minus 8 reads 0.9999997 and the slope readout collapses; divide by 8 and the same preference breathes. A small citation chip appears with the spoken hedge: Vaswani et al. 2017, "we suspect". The completed formula trues up as a whole, mint glow, once.

Now that square root's bill. Wide vectors make big dot products, big scores freeze softmax near one hot, where the slope is nearly zero. Divide by the square root of the width: same preference, living gradient. Which keeps learning healthy, probably. The authors themselves wrote, we suspect.

## beat-06b: Sharpen it until the dictionary comes back

[visual: dynamic-process] A sharpening dial multiplies the scores: at 5x the lilac weights read 0.9992 and 0.0008; at 20x they read 1, 0, 0, 0 to eight decimal places and the literal hard dict from earlier returns on screen, exact. The gradient meter rolls to zero as w(1 - w) collapses; the numbers alone carry the death.

The sentence is a claim. Try to break it. Multiply every score by twenty. What do the weights become? One, zero, zero, zero, to eight decimals. The hard dictionary, back on screen. And right there the gradient dies: the slope is weight times one minus weight, nothing at one or zero.

[visual: generalize] Two one-line captions appear in periwinkle mono, one per honesty note.

Quick honesty: the sharpening dial is softmax's, not the transformer's. Its fixed cousin is that square root. And 2014 scored with a tiny network, not dot products. Those came later. The hard lookup was never wrong. It was unlearnable. Gradient flows only while the lookup stays soft.

## beat-07: Same skeleton, opposite hardness

[visual: generalize] A two-column alignment table, attention left, RAG right, rows lighting pairwise: amber query beside embedded question, periwinkle keys beside the vector index, cream value cards beside fetched passages. The table appears with blanks first and holds four seconds.

New test: the thing you run at work. RAG. Embed the question: a query vector. Compare against a vector index: keys. Fetch passages: values. Same skeleton. The differences are the lesson. RAG's lookup is hard and external, a top k you can't backprop through. Attention's is soft, internal, learned end to end. Opposite ends of one dial. Chat models also mask future keys before the softmax. Otherwise, the same machine.

[visual: dynamic-concept] A single hard-soft dial renders both machines on one axis, RAG and attention at opposite ends; a one-line masking caption sits under the attention column. Then two visibly different lilac weight maps over the same review collapse into the same output bar, and the false explanation sentence gets crossed out in rose. The formula stays in the corner; RAG's top-k pointer taps the softmax term it replaces.

Now the thought you've been holding. Forty percent of the attention went to terrible, so terrible is forty percent of why the review read negative. True or false? In 2019, on BiLSTM classifiers, not transformers, very different attention maps produced the same predictions and matched other importance measures only weakly. Still unresolved. A heatmap is a recipe: what got mixed, never why. Same skeleton, opposite hardness.

## beat-08: What a dictionary cannot know

[visual: dynamic-process] The key-value pairs permute; the lilac weights shuffle with them; the mint output chip's digits stay frozen, held long enough to be believed, wordless under the retrieval question.

Rebuild it from memory: three objects, two operations. What replaced the exact match, and what replaced returning one value? While you think, the stored pairs shuffle. The weights follow. The output doesn't move a digit. Dictionaries don't know order. Neither does attention.

[visual: connect] The two cat-mat sentences render as identical token bags: same cards, different sentences. A closing card reads: "For the walk home: what is the cheapest thing a token could carry so a lookup can find WHERE it sits?" A quiet chip points to the extensions menu, "Still up?", on the page.

The cat sat on the mat. The mat sat on the cat. Your language tells them apart. This machine can't. For the walk home: what's the cheapest thing you could add to a token so that where it sits becomes something a lookup can find?

[visual: connect-to-reality] A timeline chip ticks "+2 years" (GNMT, Sep 2016) with "500M users" and "100B words a day" readouts, then "+3 years" (Transformer, 2017) as the recurrent network dissolves and only the attention block stays lit. On the final sentence, the amber dot hops once more between source and target rows, then parks on the unanswered question.

Two years later, Google Translate went neural: half a billion users. Three years later, Vaswani and colleagues kept only the fix. The fix outlived the architecture it rescued. That amber dot was Bahdanau's gaze. Session two gives it the one thing it still lacks: where the words sit.
