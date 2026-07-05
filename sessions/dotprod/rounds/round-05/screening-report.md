# Screening report: dotprod, round-05

VERDICT: NEEDS_JAKE — dissent from: vera (screening cap reached).

## round-1
- PASS **sam** — probes: driving=true aha=true retrieval=true (Student restated the driving question with concrete examples that preserve its core meaning of collapsing two lists into a match score. Student's aha correctly identifies the dot product as a similarity meter and adds critical insight about its limitation (magnitude-dependence) without contradicting the canonical claim. Student's retrieval answer directly solves the limitation flagged in their aha by proposing normalization, yielding cosine similarity, which is substantively correct and consistent with the canonical concept.)
- PASS **petra** — clean
- FAIL **vera** — V-DASH: 'Try answering it first; it's genuinely harder than it sounds.' | V-DASH: 'Nothing about its direction changed; it never got any closer to the probe.'
- PASS **iris** — clean

## round-2
- FAIL **vera** — V-DASH: 'Try answering it first; it's genuinely harder than it sounds.' | V-DASH: 'Nothing about its direction changed; it never got any closer to the probe.'

## Sam (cold walk)
- driving question: How do you take two lists of many different qualities (a song's traits and your taste, or a resume and a job's requirements) and collapse them into one single number that says how well they match?
- aha restated: The dot product (multiply matching entries, then add them up) works as a similarity meter that tracks direction-alignment between two vectors, but because it's linear it can be cheated just by making one vector longer, even if its direction didn't get any closer.
- retrieval answer: You'd divide each vector by its own length before comparing (normalize to unit length), so the score only reflects direction, not size — basically turning it into cosine similarity.
- matcher (claude-haiku-4-5): Student restated the driving question with concrete examples that preserve its core meaning of collapsing two lists into a match score. Student's aha correctly identifies the dot product as a similarity meter and adds critical insight about its limitation (magnitude-dependence) without contradicting the canonical claim. Student's retrieval answer directly solves the limitation flagged in their aha by proposing normalization, yielding cosine similarity, which is substantively correct and consistent with the canonical concept.
- confusion/boredom map:
  - [overload] beat-02: Probe arrow, four candidates, a sweeping animation, bars climbing/dying, and a table of numbers all land in the same beat, and in text form it's a lot to hold at once.
  - [notation] beat-02 / c1-c4 table: The bare list '0.9 c1 / 0.9 c2 / 0.3 c3 / -0.5 c4' on the page is ambiguous without the animation behind it; I couldn't tell if those are scores, positions, or something else.
  - [click] beat-03: The moment it says 'the dot product is a similarity meter' felt like a real payoff, finally naming the thing I'd been doing by hand.
  - [notation] beat-03 / symbol-sense: The 'a . b' annotation flashes in right after the plain-English explanation, and it's the first bit of actual math notation in the whole session, so it registers as a small jolt rather than something I'd been building toward.
  - [boredom] beat-04 / job posting detour: By the third restatement of 'multiply the matched entries, add them up' (song, then resume) it started to feel like the same sentence repeated with new nouns.
  - [confusion] beat-04b / walk-home question: The 'cheapest fix' question is posed as the session's actual close, but the session never confirms or reveals an answer, so I'm not sure if the intuition I have (normalize the vectors) is even what they're driving at.
  - [notation] extensions / attention prompt: sqrt(d_k) shows up in the 'still up' menu with zero explanation of what d_k is; flagged as next-session material so I didn't dwell on it, but it's a cold term dropped in passing.
- advisory (never gates): curiosity=4 wouldFinish=true It felt clear and hands-on early on, but by the resume detour it started to drag, and it ends on an open question rather than a satisfying resolution, which left me a little unsure I'd 'gotten' the point being tested.

## Petra (pedagogy, 30 rules)
- ADVISORY R10: The concrete->schematic transition (beat-01's two columns of numbers -> beat-02's probe/candidate arrows) is asserted only by narration ('Strip it down. A taste is an arrow') while the visual direction for beat-02 has the arrows simply 'appear' rather than the number columns morphing into them. The schematic->symbolic transition in beat-03 shows the aha sentence going 'freehand to exact' but the a.b notation itself is described as a small annotation that 'sits on' the readout rather than the arrows/diagram visibly resolving into that notation. -> Show the two number columns from beat-01 physically reflow/rotate into the probe and candidate arrows at the top of beat-02, and show the a . b notation crystallizing out of the arrow-and-bar diagram (e.g. the multiply-add operation literally condensing into the symbol) rather than appearing as a separate annotation.
- ADVISORY R2: Beat-02's narration states the core mechanism explicitly ('Multiply them entry by entry and add. That single sum is the score.') but the paired visual direction only has the arrows appear with bars 'at its current value' -- the entrywise multiplication itself has no described animating referent, only the pre/post state of the resulting bar. Contrast with beat-04's analogous claim, whose visual direction explicitly shows 'matched entries multiply and pool into the same lilac readout,' i.e. the operation itself animating. -> Give beat-02 the same treatment beat-04 gets: animate the pairwise multiplication (e.g. matching entries lighting up and sliding together before pooling into the bar) so the claim that is doing the actual teaching work has its own visual referent, not just the arrows and the final number.

## Vera (voice, Opus final pass)
- BLOCKING V-DASH: 'Try answering it first; it's genuinely harder than it sounds.' -> 'Try answering it first. It's genuinely harder than it sounds.'
- BLOCKING V-DASH: 'Nothing about its direction changed; it never got any closer to the probe.' -> 'Nothing about its direction changed. It never got any closer to the probe.'

## Iris (cross-media continuity)
- no findings
