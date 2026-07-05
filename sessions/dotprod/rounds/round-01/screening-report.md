# Screening report: dotprod, round-01

VERDICT: NEEDS_JAKE — dissent from: petra (screening cap reached).

## round-1
- PASS **sam** — probes: driving=true aha=true retrieval=true (Student's restatement accurately captures the core task of converting two lists into a match score with helpful concrete examples. Student correctly describes the dot product mechanism and identifies it as measuring directional similarity, appropriately noting its magnitude-independence limitation. Student correctly identifies the two operations—vector normalization and dot product (multiply-and-sum)—as the basis for a proper similarity meter, consistent with cosine similarity.)
- FAIL **petra** — R10: beat-01's concrete stage (two columns of numbers) never visually becomes beat-02's schematic stage (probe/candidate arrows); the arrows simp | R12: beat-02's opening visual has the probe arrow, four candidate arrows, AND already-populated lilac score bars ('sits at its current value') ap | R19: beat-04's 'Now the honest look. Stretch a candidate longer and its score climbs, even though its direction never moved' is a major reveal (t
- PASS **vera** — clean
- PASS **iris** — clean

## round-2
- FAIL **petra** — R26: The two teaching sections that carry the core mechanism close on summary sentences rather than a generative act: the 'What does a taste look

## Sam (cold walk)
- driving question: How do you take two lists of numbers (like a listener's taste and a song's traits) and turn them into a single score that tells you how well they match?
- aha restated: The dot product just multiplies matching entries of two vectors and adds them up, and that sum measures how much the two vectors point in the same direction, not whether they're the same size or identical.
- retrieval answer: I think the fix is to normalize each vector by its own length before you multiply and sum, basically turning it into cosine similarity, so a longer/louder vector can't win just by being bigger.
- matcher (claude-haiku-4-5): Student's restatement accurately captures the core task of converting two lists into a match score with helpful concrete examples. Student correctly describes the dot product mechanism and identifies it as measuring directional similarity, appropriately noting its magnitude-independence limitation. Student correctly identifies the two operations—vector normalization and dot product (multiply-and-sum)—as the basis for a proper similarity meter, consistent with cosine similarity.
- confusion/boredom map:
  - [click] beat-01 / 0:00: The recommendation-app hook landed, made me actually curious about the mechanism instead of tuning out.
  - [confusion] beat-02 / 0:22 (c1 0.34, c2 0.94...): The example scores are all between 0 and 1 like cosine similarity, but the text right next to it says scores can go negative, so I wasn't sure if I was looking at raw dot products or something already normalized.
  - [click] beat-02 / 0:22: Watching the bar climb/die/go negative as the probe swung made the multiply-and-add idea feel concrete for a second.
  - [notation] beat-03 / 1:05, 'a . b' annotation: The dot notation flashed on screen with barely any framing, so it registered as decoration rather than something I needed to hold onto.
  - [overload] beat-04 / 1:39 (job posting detour): Switching to Python/SQL/nights-free right after the song example felt like a second worked example crammed in when I was still settling the first one.
  - [boredom] beat-04 / closing card: Ending on an unanswered 'cheapest fix' question with no next step visible in this artifact felt like it just stopped rather than concluded.
- advisory (never gates): curiosity=3 wouldFinish=true Short and mostly clear, but the mismatched example numbers and the abrupt unresolved ending left me a little unsatisfied rather than hooked.

## Petra (pedagogy, 30 rules)
- BLOCKING R26: The two teaching sections that carry the core mechanism close on summary sentences rather than a generative act: the 'What does a taste look like as numbers?' section ends with 'Similarity, it turns out, has a basement. The number measures which way two arrows point, not what the things are.' and the 'What is the machine you just used?' section ends with 'Direction is the only thing the sweep ever changed. The meter answers the question you actually moved.' Both are declarative recaps, not prompts for the learner to produce, predict, or apply anything. The presence of predictions and a retrieval prompt elsewhere in the doc satisfies a mechanical presence-check, but the section boundaries themselves land on summary, gaming the letter while missing the intent. -> End each of these two sections on a question or micro-task instead: e.g. close the direction/sameness section by asking the learner to predict what a score of exactly zero would mean for two unrelated songs, and close the naming section by asking the learner to state the meter's three readings in their own words before moving on.
- ADVISORY R12: In beat-02 the probe arrow and all four candidate arrows appear together, and per the visual direction each candidate already carries 'a lilac score bar with a numeric readout sits at its current value' at the moment of appearance, i.e. the interaction (multiply-and-add) is already live before any object is characterized in isolation. Narration explains what a taste-as-arrow means generically but never establishes the probe alone or a single candidate alone before the compare/score operation is already on screen. -> Let the probe arrow appear and be characterized alone for a beat (what its direction/length mean) before the four candidates and their live score bars are brought in, so the interaction genuinely follows the components rather than arriving simultaneously with them.
- ADVISORY R19: A real prediction is demanded before the beat-02 sweep ('which candidate ends up on top, and does any score go negative?'), but the session's central reveal, the naming of the mechanism as a similarity meter in beat-03, arrives with no dedicated prediction attached to it: 'Look at what your hands just learned... So say it plainly: the dot product is a similarity meter.' The learner is walked through the recap and then simply told the name. -> Before the naming line, insert a beat where the learner is asked to guess what single word or device the agree/ignore/oppose pattern resembles, so the label itself is guessed at (or one step from being guessed) rather than only recapped-then-declared.

## Vera (voice, Opus final pass)
- ADVISORY V-TELL-STRUCT: 'still be totally different lengths, different songs, different everything else about them' -> 'still be totally different lengths, different songs.'
- ADVISORY V-RHYTHM: 'That's worth sitting with for a second' -> 'That's worth a second's thought' (vary one instance so 'sit with' stops reading as a tic)

## Iris (cross-media continuity)
- no findings
