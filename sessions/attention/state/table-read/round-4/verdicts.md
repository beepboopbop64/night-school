# Table-read round 4 (S3, FINAL), attention

Fresh quarantined critic sessions (Sonnet tier). Raw prompts/outputs here.

## Verdict counts

| Critic | Blocking | Advisory | Gate result |
|---|---|---|---|
| Sam | 0 (all 3 probes passed) | 9 map entries (3 click, 1 overload, 2 confusion, 2 boredom, 1 notation) | PASS |
| Petra | 0 | 0 (empty array) | PASS |
| Vera | 0 | 4 (V-TELL-STRUCT x2, V-HUMOR, V-RHYTHM) | PASS |

ZERO blocking verdicts from all three critics. S3 gate: PASSED (round 4 of
a 4-round cap).

## Sam probe answers (final, verbatim)

- drivingQuestion: "How do you get a gradient through a 'choice' - like
  deciding which word to look at - when choosing is normally a discrete,
  all-or-nothing operation with zero slope?"
- ahaRestated: "Attention replaces a hard winner-take-all lookup with a
  soft weighted blend of every stored value (scores turned into proportions
  via softmax), so the model can learn where to look because the output
  changes smoothly instead of jumping."
- retrievalAnswer: "Exact key matching got replaced by a similarity score
  between the query and every key (a scaled dot product), and returning one
  single value got replaced by a weighted sum over all the values using
  those scores as weights."

Semantic check against the canonical aha ("Attention is a soft lookup
table."): PASS. All three probes correct.

## Vera advisory dispositions (none gate)

1. V-TELL-STRUCT "The lookup didn't fail to answer. It failed to learn."
   OVERRULED: S2-locked landing line (treatment section 6, beat 4).
2. V-TELL-STRUCT "The hard lookup was never wrong. It was unlearnable."
   OVERRULED: S2-locked landing prose (treatment 6b). Vera's craft note
   (negate-then-reframe used three times) recorded for the S6 Opus pass to
   adjudicate on the assembled cut.
3. V-HUMOR "cat flavored information": OVERRULED: treatment-locked phrase
   doing semantic work (near-cat, not exactly-cat, sets up kitten partial
   credit).
4. V-RHYTHM "watching his own eyes": OVERRULED: S2 hook prose; the colon
   gloss ("your gaze hops back and forth") resolves the literalism.

## Sam advisory map, routed as production notes (non-gating)

- beat-06a overload (recurred across Sams): already at 45s with the
  fade-shown morph; flagged to S4a Manim pacing: let the width-dial segment
  breathe, formula assembly strictly sequential, never simultaneous.
- beat-07 masking aside: one-sentence honesty disclosure by design
  (dossier 1.6#3); page track carries the full callout. Noted for the page
  writer.
- beat-08 stakes as "fact dump": chips carry the numbers, narration is two
  sentences (G6 minimum). Noted for S4a: play chips under the recursive
  gaze close, not as separate cards.

## Cost

Sam $0.14, Petra $0.58, Vera $0.34. Round total ~$1.07.
Four-round table-read total ~$4.04.
