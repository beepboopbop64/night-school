# Screening report: dotprod, round-01

VERDICT: PASS (all four critics clean).

## round-1
- PASS **sam** — probes: driving=true aha=true retrieval=true (Student's restatement accurately captures the core task of producing a single match score from two numerical lists. Student correctly explains the dot product mechanism and identifies its critical flaw—that it rewards vector length even when directional alignment is weak. Student identifies the correct fix (normalizing vectors to isolate direction) and explains why it solves the length-bias problem identified in the aha, showing substantive understanding despite incomplete recall of terminology.)
- FAIL **petra** — R30: spine.md's metaphor registry requires two honesty disclosures as page callouts: 'the numbers in this session are chosen for readability' (be
- PASS **vera** — clean
- PASS **iris** — clean

## round-2
- PASS **petra** — clean

## Sam (cold walk)
- driving question: Given two lists of numbers (like a listener's taste and a song, or a resume and a job), how do you turn them into one score that says how well they match?
- aha restated: The dot product (multiply matching entries, add them up) measures how much two vectors point in the same direction, not how similar their sizes or overall content are, so it can be fooled by length alone.
- retrieval answer: I think the fix is to somehow divide out the length of each vector so only the direction is left, so the score doesn't reward things just for being 'bigger' — but I don't remember if there's a name for that step.
- matcher (claude-haiku-4-5): Student's restatement accurately captures the core task of producing a single match score from two numerical lists. Student correctly explains the dot product mechanism and identifies its critical flaw—that it rewards vector length even when directional alignment is weak. Student identifies the correct fix (normalizing vectors to isolate direction) and explains why it solves the length-bias problem identified in the aha, showing substantive understanding despite incomplete recall of terminology.
- confusion/boredom map:
  - [confusion] beat-02 / probe sweep bars: c1 and c4 both read 0.34 and c2 and c3 both read 0.94, and it's never explained why two different candidates land on identical scores.
  - [notation] beat-03 / 'a . b' annotation: The dot notation a·b appears as a small label with no real explanation of what a and b stand for, just as I was still picturing arrows, so it registered as a symbol I half-recognized rather than something newly taught.
  - [boredom] site text / 'That's worth sitting with' and beat-03 restating direction-vs-identity: The 'a big score doesn't mean the songs are the same' point gets said almost identically three separate times across the page, which felt like padding by the third pass.
  - [overload] beat-04 / resume detour: Right before the closing question, a whole new domain (job matching, Python/SQL/nights free) gets introduced, which felt like one new thing too many this late in a short session.
  - [click] beat-03 / 'one dial' framing: Collapsing agree/ignore/oppose into a single turning meter made the whole probe exercise suddenly feel like one coherent idea instead of three separate observations.
- advisory (never gates): curiosity=4 wouldFinish=true It felt clear and hands-on while I was doing it, but a little thin and repetitive by the end, like the same insight got restated more times than it needed to be.

## Petra (pedagogy, 30 rules)
- ADVISORY R10: beat-01 grounds the concept in two columns of plain numbers (the concrete anchor); beat-02 opens with 'One amber probe arrow and four periwinkle candidate arrows appear' with no described transition from the number columns into the arrow diagram. The concrete-to-schematic step is cut, not morphed, so the fade the rule requires is never shown even though the schematic-to-symbolic step later (notation 'sits on' the existing score readout in beat-03) does show continuity. -> Have the beat-01 number columns visually resolve into the beat-02 arrows (e.g., each paired-entry glow rotates/collapses into the arrow's coordinate), so the concrete->schematic step is animated the same way the schematic->symbolic step already is.
- ADVISORY R19: The length/magnitude 'crack' is a major reveal (script beat-04: 'Stretch a candidate longer and its score climbs, even though its direction never moved'; doc/lesson.md section 4 mirrors this) but no prediction is asked immediately before it. The only prediction present in that beat/section is the earlier 'rebuild the meter from memory' retrieval prompt, which is answering a different question (what the two operations are, not what happens when a vector is stretched). The letter of 'a prediction appears in this beat' is satisfied while the intent (a guess demanded before THIS specific reveal) is not. -> Insert a targeted guess right before the stretch: 'If we make one candidate's arrow longer without turning it, what happens to its score?' before showing the bar climb.
- ADVISORY R26: On the built page, the section 'What did we just build?' (the aha-naming section) closes with pure recap ('Agree, ignore, oppose: that's the whole dial, and you built it with nothing but multiplication and addition.') and no generative prompt of its own, unlike the parallel section in doc/lesson.md which correctly ends on 'Close the loop yourself... State what each one says about two vectors, out loud or on paper.' Because other sections on the same page do carry a generative closer, a page-level presence check would pass while this specific section's intent (ends on a generative act, not a summary) is violated. -> Move (or add) the 'state the three readings in your own words' generative prompt to the end of 'What did we just build?' on the built page, matching doc/lesson.md.
- ADVISORY R26: doc/lesson.md's section 'What does a taste look like as numbers?' embeds a generative prompt mid-flow ('call one more reading: what would a score of exactly zero mean... Say it in your own words, then check yourself against the sweep.') but then appends a closing summary sentence after it ('The number measures which way two arrows point, not what the things are.'), so the section's actual last beat is a restated conclusion, not the generative act. -> Cut the closing summary sentence, or move it before the generative prompt, so the section's final line is the learner's own act, not the narrator's restatement.

## Vera (voice, Opus final pass)
- no findings

## Iris (cross-media continuity)
- no findings
