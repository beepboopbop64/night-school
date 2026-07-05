# Screening report: dotprod, round-02

VERDICT: NEEDS_JAKE — dissent from: petra (screening cap reached).

## round-1
- PASS **sam** — probes: driving=true aha=true retrieval=true (The student's restatement accurately captures the core concept using concrete examples to clarify how two lists become a single similarity score. The student correctly explains the dot product's mechanism (multiply and add) and its relationship to similarity through directional alignment, appropriately noting its magnitude sensitivity. The student correctly identifies the two operations—normalizing vectors by dividing by magnitude and then multiplying/adding—and reasonably infers this corresponds to cosine similarity.)
- FAIL **petra** — R10: The concrete->schematic->symbolic progression is never shown as a fade/morph. beat-01's two number columns cut directly to beat-02's arrows 
- PASS **vera** — clean
- PASS **iris** — clean

## round-2
- FAIL **petra** — R19: In beat-04, the meter's central flaw (score inflates with length while direction holds still) is delivered as direct exposition with no ante

## Sam (cold walk)
- driving question: Given two lists of numbers (like a taste profile and a song profile), how do you turn them into one score that says how well they match?
- aha restated: The dot product (multiply matching entries, then add) isn't measuring sameness, it's measuring whether two vectors point in the same direction, so it can be fooled by size even when direction is unchanged.
- retrieval answer: I think the fix is to normalize each vector by its own length before you multiply and add, basically divide out the magnitude so only the direction counts, which I'm guessing is what people call cosine similarity, though the session never actually says that word.
- matcher (claude-haiku-4-5): The student's restatement accurately captures the core concept using concrete examples to clarify how two lists become a single similarity score. The student correctly explains the dot product's mechanism (multiply and add) and its relationship to similarity through directional alignment, appropriately noting its magnitude sensitivity. The student correctly identifies the two operations—normalizing vectors by dividing by magnitude and then multiplying/adding—and reasonably infers this corresponds to cosine similarity.
- confusion/boredom map:
  - [confusion] beat-02 / 'call it' prediction / bars c1-c4: Told to predict which candidate wins before touching anything, but with only text describing arrows I couldn't really form a guess, and then c2 and c3 tie at +94 which felt like an odd 'gotcha' I wasn't set up to expect.
  - [click] beat-02 / drag interaction: Watching a single score bar climb, die to zero, then go negative as I rotate one arrow made the 'agree/ignore/oppose' idea click physically.
  - [notation] beat-03 / symbol-sense, 'a . b' annotation: The dot notation a . b shows up right as the aha lands, and for a second I wasn't sure if a and b were the same as 'probe' and 'candidate' or some new thing.
  - [overload] beat-04 / retrieval + job posting + stretching, all back to back: In one beat I'm asked to recall the two operations from memory, then a whole new job-posting example drops in, then immediately the stretching/padding problem, it felt like three ideas stacked on top of each other right when I was trying to consolidate.
  - [boredom] beat-04 / 'the multiply-and-add never asked what the numbers meant' repeated: By the third time the session restates 'multiply then add, direction not identity' I started skimming instead of reading closely.
- advisory (never gates): curiosity=4 wouldFinish=true It felt satisfying while I was dragging the arrow around, but the ending crammed a new example and a new problem in fast, so I left a little foggy instead of clearly hooked for next time.

## Petra (pedagogy, 30 rules)
- BLOCKING R19: In beat-04, the meter's central flaw (score inflates with length while direction holds still) is delivered as direct exposition with no antecedent prediction: script reads '[visual: dynamic-process] One periwinkle candidate stretches longer... Now the honest look. Stretch a candidate longer and its score climbs, even though its direction never moved.' The page mirrors this: 'Now one more honest look, because a meter you trust blindly is a meter that will lie to you. Take one candidate and stretch it longer without turning it at all... Its score climbs anyway.' Unlike the beat-02 reveal (which is preceded by 'Before you drag anything, call it: which candidate ends up on top, and does any score go negative?'), no prompt asks the learner to guess what stretching a candidate will do to its score before the reveal states the answer. This is a major reveal (it is the session's entire second conflict and the seed of the breadcrumb), not a minor aside, so it falls squarely under 'every major reveal.' -> Insert a genuine guess beat immediately before the stretch demo, e.g. 'Before you watch this, guess: if a candidate's numbers just get bigger, same direction, does its score change?' in both script and page, then let the stretch animation confirm or overturn the guess.

## Vera (voice, Opus final pass)
- ADVISORY V-TELL-STRUCT: 'Before you read on, take a guess…' / 'Before you read on, call it.' / 'Before you scroll on, call one more reading' -> Vary the prompt openers so they don't repeat the near-identical 'Before you read on/scroll on' frame three times; e.g. change one to 'Call it first:' and another to 'One more before you move on:'
- ADVISORY V-RHYTHM: 'Sit with that guess for a second' … 'the part worth sitting with' … 'Step back from the sweep for a second' … 'Sit with that on the way out' -> Thin the recurring 'sit with / for a second' motif; e.g. change one 'Sit with that guess for a second' to 'Lock in your guess'

## Iris (cross-media continuity)
- no findings
