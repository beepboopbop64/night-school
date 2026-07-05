# Screening report: dotprod, round-04

VERDICT: PASS (all four critics clean).

## round-1
- PASS **sam** — probes: driving=true aha=true retrieval=true (Driving: Valid paraphrase capturing the core task of scoring list-pair similarity with concrete examples. Aha: Student correctly affirms dot product as similarity meter with operation details and insightfully identifies the magnitude-scaling problem. Retrieval: Student provides substantively correct operations (normalize then dot product) that build appropriately on the canonical aha to address the identified flaw.)
- PASS **petra** — clean
- PASS **vera** — clean
- PASS **iris** — clean

## Sam (cold walk)
- driving question: How do you take two lists of many different numeric qualities (like a song's traits and a listener's taste) and boil them down into one single number that says how well they match?
- aha restated: The dot product (multiply matching entries, then add) works as a similarity meter that tracks direction/alignment, but because it scales linearly with length, a bigger vector can win on sheer size alone, not on actually matching better.
- retrieval answer: The cheapest fix is to normalize each vector by its own length before comparing (i.e. divide out the magnitude), which turns the raw dot product into cosine similarity, keeping the direction/alignment information while throwing away the size effect.
- matcher (claude-haiku-4-5): Driving: Valid paraphrase capturing the core task of scoring list-pair similarity with concrete examples. Aha: Student correctly affirms dot product as similarity meter with operation details and insightfully identifies the magnitude-scaling problem. Retrieval: Student provides substantively correct operations (normalize then dot product) that build appropriately on the canonical aha to address the identified flaw.
- confusion/boredom map:
  - [click] beat-01 / intro hook: The 'app just recommended a song' framing is relatable and pulled me in right away.
  - [click] beat-02 / probe and arrows: Multiply-then-add as 'the score' felt satisfyingly simple once stated.
  - [confusion] site text / 'c1 c2 c3 c4 probe 0.3 c1 0.9 c2...' block: As plain text this list of numbers next to labels is hard to parse without seeing the actual bars; I had to guess these were score readouts.
  - [notation] beat-03 / naming the dot product, 'a . b' annotation: The dot notation just appears as a small annotation without really defining what a and b are as vectors, so it landed as a label more than something I could use.
  - [click] beat-04 / same meter different aisle (job posting): Swapping songs for a job-fit score made the 'it doesn't care what the numbers mean' point land well.
  - [click] beat-04b / honest look, doubling c1: Seeing that doubling length exactly doubles the score was a clean, convincing demonstration of the flaw.
  - [boredom] closing 'Still up?' menu: At the end of a long day, the three follow-up options (argue with an LLM, read two papers, write NumPy code) felt like more homework being handed to me rather than a natural next step.
  - [overload] beat-04 / mid-recall + job analogy: Being asked to recall the two operations from memory while simultaneously being handed a new domain (job postings) to digest felt like two asks stacked on top of each other.
- advisory (never gates): curiosity=4 wouldFinish=true It felt like a well-paced, hands-on walkthrough that clicked mechanically, though by the end my energy was fading and the extension menu felt like extra effort rather than a natural continuation.

## Petra (pedagogy, 30 rules)
- ADVISORY R10: The concrete->schematic->symbolic chain is present (beat-01 number columns -> beat-02 arrows -> beat-03 notation a.b) but neither transition is described as a shown fade/morph. Beat-02's visual intent simply has arrows 'appear' next to the beat-01 columns with no described transformation, and beat-03's notation is introduced as 'a small periwinkle mono annotation, a . b, sits on the score readout' next to the meter dial rather than the dial visibly resolving into the notation. Only the aha sentence itself gets an explicit fade ('freehand to exact with a mint glow'). -> Add an explicit morph beat: the two number columns re-forming into the probe/candidate arrows, and the meter dial's needle-and-readout condensing into the a.b glyph, so both transitions are seen happening rather than just juxtaposed.
- ADVISORY R8: Beat-02's visual intent reads 'One amber probe arrow and four periwinkle candidate arrows appear; under each candidate a lilac score bar... sits at its current value' - a completion event ('appear'/'sits') rather than a build/draw action, unlike beat-01 ('slide in'), beat-03 ('replay... collapse'), and beat-04b ('doubles in length... reads out') which all describe the diagram assembling in reasoning order. -> Rephrase the beat-02 establishing shot as a build: e.g., the probe arrow draws first, then each candidate arrow draws in turn with its (empty) score bar appearing after it, so the pre-training of components is visibly sequential rather than a completed tableau.
- ADVISORY R3: Beat-03's notation shot places 'a small periwinkle mono annotation, a . b' on top of the score readout, but periwinkle is the locked token for the candidates (data.observed), while the score bars/needle/readout are locked as lilac (data.params). The notation stands for the operation/reading, not for the candidates, so its color does not match the concept it labels per the locked registry. -> Render the a . b annotation in lilac (matching the score readout it sits on and represents) or in a neutral cream/mono that doesn't collide with an already-assigned concept color.

## Vera (voice, Opus final pass)
- ADVISORY V-DASH: 'The meter was never asked to measure size, it was supposed to measure agreement in direction, but size is riding along for free.' -> 'The meter was never asked to measure size. It was supposed to measure agreement in direction, but size is riding along for free.'
- ADVISORY V-RHYTHM: '...how would you boil their match down to a single number?' followed immediately by 'Try answering that before you read on, because it's genuinely harder than it sounds.' (the phrase 'before you read on' repeats within two sentences) -> Drop the second 'before you read on': 'Try answering that first, because it's genuinely harder than it sounds.'

## Iris (cross-media continuity)
- no findings
