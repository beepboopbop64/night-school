# How does a data center decide two songs share your taste?

## The score behind the song

Your music app just played you a song you love, by a band you have never heard of. No human picked it for you. Somewhere in a data center, two lists of numbers got compared, and the comparison said: same taste.

That is the whole magic trick, and it is smaller than it looks. One list stood for you. One list stood for the song. Something turned the pair into a single number, and that number was high enough to hit play.

So here is the question of the night. How do you score a match between two lists of numbers?

Hold that question before we reach for any definition. One answer to it runs half of modern machine learning. We are going to build that answer with our hands, not memorize it.

## Turn the probe and feel it

Strip it down until it fits in your palm. A taste is an arrow. Each direction is a quality, some axis like "loud" or "mellow," and the length along that direction is how hard the song leans that way. Two dimensions, so we can actually see the thing.

Now picture one amber probe arrow, that is you, and four candidate arrows, four songs sitting still. Here is the rule for scoring a match: multiply the two arrows entry by entry, then add up the products. That single sum is the score. One multiply, one add.

> Honest edges: the numbers in this session are chosen for readability. Real embedding coordinates are neither small nor round. They are long ugly decimals a machine never has to look at. We use tidy integers so your eyes can do the arithmetic the GPU does silently.

Before you read on, call it. Which candidate ends up with the highest score, and does any score go negative? Say an answer out loud. A prediction you can be wrong about is worth ten definitions you nod along to.

The tempting guess is that the candidate that looks most like the probe wins, and that no score dips below zero, because how could similarity be less than nothing?

Now turn the probe and watch the scores answer. Point at a candidate and its score climbs. Turn away and it dies. So a big score means two songs are the same, right?

Watch again, more carefully. The scores moved while the candidates never moved at all. Nothing about the songs changed. Only your direction changed. So the score cannot be reading sameness of items. It is reading agreement of direction.

And yes, scores go negative. Point against a candidate and the sum drops below zero, because some of those pairwise products come out negative and drag the sum down. Similarity, it turns out, has a basement.

The number measures which way they point, not what the things are.

## Name the machine you just used

Look at what your hands just learned. Point the probe along a candidate and the sum climbs to its biggest. Point it across, at a right angle, and the sum dies to exactly zero. Point it against and the sum goes negative.

Three positions, three readings: agree, ignore, oppose. One multiply and one add, and it behaves like a meter with a needle that swings across those three words on a dial.

So say it plainly:

**The dot product is a similarity meter.**

Two lists of numbers go in. One honest reading of alignment comes out. That is the machine. It has a name and a symbol now: we write it $a \cdot b$, the dot sitting between the two arrows to mean multiply-pairwise-and-add.

> Honest edges: real embeddings live in hundreds of dimensions. Two dimensions is the picture, not the territory. Nothing in the mechanism changes when you add more axes. You still multiply entry by entry and add, there are just more entries. The dial in your head stays exactly as true at three hundred dimensions as it is at two.

And notice why the reading tracks direction and not size or identity. Direction is the only thing the sweep ever changed. The meter answers the question you actually moved.

## What the meter gets wrong

Time to close the loop. Do this from memory, not from scrolling up.

Rebuild the meter from memory: two arrows go in, so what two operations turn them into the score?

If "multiply pairwise, then add" came back to you without a peek, you own $a \cdot b$ now. It is yours.

While that settles, one more honest look, because a meter you trust blindly is a meter that will lie to you. Take one candidate and stretch it longer without turning it at all. Its direction holds dead still. Its score climbs anyway.

That is a problem. It means a long, loud song can win on sheer size, not on agreement. The meter cannot tell "points the same way" apart from "just bigger." A shout beats a whisper even when the whisper agrees with you more.

> Honest edges: the raw dot product rewards length as well as direction. We are shipping that flaw on purpose. We didn't hide it. It's the exact gap the next session opens on.

For the walk home: what is the cheapest fix that keeps the direction and forgets the size?

Still up? The menu below has three ways to keep going: argue the metaphor with an LLM until it cracks, chase this same score into the attention papers where it reappears, or build the meter yourself in a few lines of NumPy.
