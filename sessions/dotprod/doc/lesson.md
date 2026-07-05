# How does your app know two songs share your taste?

## The score behind the song

Your music app just played you a song you love, by a band you have never heard of. No human picked it for you. Somewhere in a data center, two lists of numbers got compared, and the comparison said: same taste.

Here's the part worth chewing on before you nod along. A song isn't one number. It's loud, fast, sad, bright, a dozen qualities at once, and your taste is that same tangle. So before any machine gets a turn, take your own swing at it. How do you score a match between two lists of numbers?

Try answering it first. It's genuinely harder than it sounds. You've got two stacks of features and you want one number for how well they fit. Add the stacks? That rewards loudness, not agreement. Line them up and count exact matches? Real features aren't yes or no. The moment there are more than a couple of qualities, the honest score stops being obvious.

One answer to this question runs half of modern machine learning. The puzzle was never the machine. The puzzle is you, right now, trying to fold a tangle into a single fair number.

Take a guess before the next section gives it away: if you had to turn two lists of numbers into one match score, what would you actually do to them? Write it down. A guess you can be wrong about beats ten definitions you nod along to.

## What does a taste look like as numbers?

You just tried to score that match by hand, and it fought back: too many qualities, no clean way to fold them into one number. Here's the move that lands it.

Strip a taste down until it fits in your palm. It's an arrow. Each direction is one quality, some axis like "loud" or "mellow," and the length along that direction is how hard the song leans that way. Two dimensions, so we can actually see the thing. Take one amber probe arrow, that's you, and four candidate arrows, four songs sitting still. Multiply the two arrows entry by entry, then add up the products. That single sum is the score. One multiply, one add, and the whole tangle collapses to one number.

> Honest edges: the numbers in this session are chosen for readability. Real embedding coordinates are neither small nor round. The machine does the same work on messy ones.

Call your shot before anything moves: name the one candidate whose bar tops out. Say it out loud. The tempting guess is that the arrow that looks most like the probe wins, and that no score dips below zero, because how could similarity be less than nothing?

Now turn the probe and watch the scores answer. Point at a candidate and its score climbs. Turn away and it dies. So a big score means two songs are the *same*, right?

Watch again, more carefully. The scores moved while the candidates never moved at all. Nothing about the songs changed. Only your direction did. So the score can't be reading sameness of items. It's reading agreement of direction. And here's the sneaky part: stretch one candidate longer without turning it, and its bar climbs anyway, on length alone, even though its direction never got closer. Length cheats the meter. A long arrow can fake a high number.

The number measures which way two arrows point. It also measures how big they are. Those are two different jobs sharing one readout.

Before you scroll on, call one reading you haven't seen yet: what would a score of exactly zero mean for two songs? Not opposed, not aligned. Say it in your own words, then check yourself against the sweep.

## What is the machine you just used?

Look at what your hands just learned. Point the probe along a candidate and the sum climbs to its biggest. Point it across, at a right angle, and the sum dies to exactly zero. Point it against and the sum goes negative.

Three positions, three readings: agree, ignore, oppose. One multiply and one add, and it behaves like a meter with a needle that swings across those three words on a dial.

So say it plainly:

**The dot product is a similarity meter.**

Two lists of numbers go in. One reading of alignment comes out. And it has a symbol now: we write it $a \cdot b$, where $a$ is the probe's list and $b$ is the candidate's, the dot standing for multiply-pairwise-and-add.

> Honest edges: real embeddings live in hundreds of dimensions. Two dimensions is the picture, not the territory. Nothing in the mechanism changes when you add axes: you still multiply entry by entry and add. There are just more entries. The dial in your head stays as true with hundreds of axes as it is with two.

While every arrow held the same length, direction was all the sum ever responded to. That's why the meter tracks alignment. It answers the question you actually moved.

The meter has three readings worth knowing: positive, zero, negative. Say what each one claims about two vectors, out loud or on paper, in your own words, before you go on.

## Same meter, different aisle

Time to close the loop. Do this from memory, not from scrolling up.

> Rebuild the meter from memory: two arrows go in, so what two operations turn them into the score?

If "multiply pairwise, then add" came back without a peek, you own $a \cdot b$ now. It's yours.

Now keep the same meter running and walk it one aisle over. We don't rebuild anything. It's the same meter, just pointing its needle at a job posting instead of a song. The role wants Python hours, SQL reps, nights free. In the job aisle, which list plays the probe? It's you, the one asking the question. The role is the candidate you're scoring. Multiply the matched entries, add them up, one number for the fit. Different aisle, same meter. The multiply-and-add never asked what the numbers meant, and that is exactly why it travels.

Now the honest look, because a meter you trust blindly is a meter that will lie to you. First point the probe straight along c1 and set its length back to 1.0, so it reads a clean 1.0. Then guess before you read on: if you double c1's length exactly, same direction, just twice as long, does the number double too?

It does, exactly. Double one input, double the output. The meter is linear in each arrow you feed it: 4.2 becomes 8.4, no surprise hiding in the middle. That clean scaling is the crack. Size passes straight through the multiply-and-add, untouched.

That's the problem. A long, loud song can win on sheer size, not on agreement, and a padded resume can win on sheer length. The meter can't tell "points the same way" apart from "just bigger." A shout beats a whisper even when the whisper agrees with you more.

Remember where we started: two lists of numbers got compared, and the verdict was same taste. Now you can run that comparison yourself. Next time the app hands you a stranger's song that is exactly right, you will know the number that said ship it, and you will know that number can be shouted over.

For the walk home: what is the cheapest fix that keeps the direction and forgets the size, now that you know size scales the score in lockstep?

Still up? The menu below has three ways to keep going: argue the metaphor with an LLM until it cracks, chase this same score into the attention papers where it reappears, or build the meter yourself in a few lines of NumPy.
