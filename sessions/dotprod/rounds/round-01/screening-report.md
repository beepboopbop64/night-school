# Screening report: dotprod, round-01

VERDICT: NEEDS_JAKE — dissent from: petra (screening cap reached).

## round-1
- PASS **sam** — probes: driving=true aha=true retrieval=true (Driving question: student restates the core task clearly—converting two lists into a single match score. Aha sentence: student correctly describes the dot product computation and identifies it as a similarity meter, specifically for directional alignment. Retrieval question: student accurately reconstructs the two core operations—computing the dot product and normalizing by vector magnitudes—to produce a similarity score.)
- FAIL **petra** — R10: Beat-01's visual is two columns of numbers (concrete) sliding in and lighting up; beat-02 opens with 'One amber probe arrow and four periwin
- PASS **vera** — clean
- PASS **iris** — clean

## round-2
- FAIL **petra** — R28: The dot-product-as-meter schema is taught inside a single surface context across the entire session: taste-vector versus song-vector matchin

## Sam (cold walk)
- driving question: Given two lists of numbers (like a taste and a song), how do you turn them into one score that says how well they match?
- aha restated: If you multiply matching entries of two vectors and add up the results, that single sum acts like a meter for how much they point the same direction, not how similar their sizes are.
- retrieval answer: I think the fix is to divide the dot product by the lengths of the two vectors so you're only comparing direction and the size/magnitude cancels out, basically normalizing before you multiply and sum.
- matcher (claude-haiku-4-5): Driving question: student restates the core task clearly—converting two lists into a single match score. Aha sentence: student correctly describes the dot product computation and identifies it as a similarity meter, specifically for directional alignment. Retrieval question: student accurately reconstructs the two core operations—computing the dot product and normalizing by vector magnitudes—to produce a similarity score.
- confusion/boredom map:
  - [notation] 0:22 / beat-02: The example scores (0.34, 0.94) already look normalized between 0 and 1, which is confusing since the whole point later is that raw dot products aren't bounded like that.
  - [click] 0:22 / beat-02: The 'multiply entry by entry and add' description finally made the arrow metaphor concrete instead of abstract.
  - [click] 1:05 / beat-03: Naming the thing you just did by hand as 'the dot product' landed well, it tied the hands-on sweep to a real term.
  - [notation] 1:05 / beat-03: The little 'a . b' annotation flashes on screen but a and b are never explicitly tied back to the probe/candidate arrows, so it feels like a label dropped in rather than explained.
  - [confusion] 1:39 / beat-04: Ending on 'what's the cheapest fix' with zero attempt at an answer felt like being cut off mid-thought rather than a satisfying close.
- advisory (never gates): curiosity=4 wouldFinish=true It felt clear and hands-on for most of it, but the abrupt unresolved cliffhanger at the end left me a little unsatisfied rather than hooked.

## Petra (pedagogy, 30 rules)
- ADVISORY R10: beat-03 visual: 'The aha sentence trues up on screen, freehand to exact with a mint glow. A small periwinkle mono annotation, a . b, sits on the score readout.' The symbolic notation a·b is placed beside the existing readout rather than shown emerging from the schematic dial/arrows via an on-screen morph; only the sentence itself is animated freehand-to-exact, not the schematic-to-symbol step. -> Show a·b assemble out of the meter dial or the multiply-and-add gesture from beat-02 (e.g., the two arrows' matched entries sliding together into the dot notation) so the schematic-to-symbolic transition is a visible fade, not a juxtaposition.
- ADVISORY R12: beat-02 opening visual: 'One amber probe arrow and four periwinkle candidate arrows appear; under each candidate a lilac score bar with a numeric readout sits at its current value.' The score bars, which are the output of the arrows interacting, are already populated before the narration has characterized what an arrow is or stated the multiply-and-add rule. -> Bring in the bare arrows first while narration characterizes them ('a taste is an arrow...'), and only populate the score bars once the multiply-and-add rule has been stated, so the interaction visibly follows the characterization.
- ADVISORY R19: beat-04 stages the length-flaw reveal directly with no prior prediction: 'Stretch a candidate longer and its score climbs, even though its direction never moved' (visual: 'One periwinkle candidate stretches longer; its lilac score climbs while its direction holds still'). Unlike the beat-02 sweep, which is preceded by 'Before you drag anything, call it: which candidate ends up on top, and does any score go negative?', no equivalent guess is demanded before this reveal. -> Add a short predict-first line before the stretch demo, e.g. 'if we stretch this candidate without turning it, does its score change?' before showing the climb.
- ADVISORY R26: beat-02 closes on 'The bars moved while the candidates never moved at all. The score reads agreement of direction, not sameness' and beat-03 closes on 'And the reading tracks direction, because direction is all the sweep ever changed.' Both are recap/explanatory sentences summarizing what was just shown, not acts that ask the learner to produce, predict, or apply anything, in contrast to beat-04's closing breadcrumb question. -> End beat-02 and beat-03 on a small generative prompt instead of an explanatory recap, e.g. 'say what the dial would read for a candidate pointing the opposite way' before moving on.
- BLOCKING R28: The dot-product-as-meter schema is taught inside a single surface context across the entire session: taste-vector versus song-vector matching (one probe, four candidates, beats 1-4, both script and page). No second, surface-different worked instance of the same schema is taught and named within the session; the only other contexts (attention papers, NumPy build) appear solely as unbuilt 'Still up?' breadcrumbs, not as taught, aligned instances. -> Add one brief second surface-different instance of the same dot-product-as-meter idea inside the session (e.g., matching a job-candidate profile to a role, or comparing two sports-team stat vectors), explicitly named alongside the music example so the deep structure is shown to transfer, not just promised for later.

## Vera (voice, Opus final pass)
- ADVISORY V-RHYTHM: 'The question worth sitting with tonight' / 'That's worth sitting with for a second' / 'Step back from the sweep for a second' / 'Rebuild it in your head for a second' / 'Sit with that one' -> Cut or vary two of these; e.g. 'Rebuild it in your head' (drop 'for a second') and 'Stay on that one' so 'sit with' / 'for a second' stops reading as a crutch phrase.

## Iris (cross-media continuity)
- no findings
