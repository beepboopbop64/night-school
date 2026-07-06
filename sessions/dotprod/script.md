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

[visual: symbol-sense] The aha sentence trues up on screen, freehand to exact with a mint glow. The lilac mono annotation, a . b, trues up next to the worked chip's numerals, two and one dot one and three, so the symbol is anchored to numbers the viewer already computed.

Look at what your hands just learned. Point the probe along a candidate and the sum climbs. Point it across and the sum dies to zero. Point it against and the sum goes negative. One multiply and add, and it behaves like a meter with agree, ignore, and oppose on the dial.

So say it plainly: the dot product is a similarity meter. In symbols, a dot b: multiply the matching entries, add the products. The taste and song from the worked chip, two and one dot one and three, come out to five. Same recipe, now wearing its symbol. Two lists of numbers go in. One honest reading of alignment comes out. And the reading tracks direction, because direction is all the sweep ever changed.


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
