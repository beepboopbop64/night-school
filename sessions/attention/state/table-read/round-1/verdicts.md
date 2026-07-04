# Table-read round 1 (S3), attention

Date: 2026-07-04. Critics spawned as fresh quarantined sessions (Sonnet
tier), one per agent, inputs per ARCHITECTURE §5 quarantine: Sam saw
script.md only; Petra saw spine.md + storyboard.yaml + script.md + the
R1-R30 digest; Vera saw script.md + extracted learner-facing storyboard
copy. Raw prompts and outputs in this directory.

## Verdict counts

| Critic | Blocking | Advisory | Gate result |
|---|---|---|---|
| Sam | 0 (all 3 probes passed) | 10 map entries (4 click, 2 overload, 1 confusion, 3 notation) | PASS |
| Petra | 1 (R2) | 0 | FAIL |
| Vera | 3 (V-DASH) | 4 (V-TELL-STRUCT, V-RHYTHM, V-REGISTER, V-HUMOR) | FAIL |

Sam probe answers (round 1): driving question and retrieval answer correct;
aha restated as "Attention is just a soft version of a dictionary lookup:
instead of finding one exact key and returning its one value, you score the
query against every key, turn those scores into softmax weights, and return
a blend of all the values, which keeps the gradient alive instead of zero."
Semantic match to the canonical sentence: PASS.

## Dispositions

1. Petra R2 (blocking): beat-08 GNMT/Transformer stakes narration had no
   visual referent (gaze dot was carrying it). FIXED: stakes get their own
   timeline-chip sequence reusing the beat-01 chip pattern ("+2 years"
   GNMT Sep 2016, 500M users, 100B words a day; "+3 years" Transformer);
   the gaze dot is reserved for the final session-2 sentence alone.
   storyboard beat-08 visual + onScreenText updated; script cue updated.
2. Vera V-DASH x3 (blocking): semicolons doing em-dash work in beat-06b
   (two) and beat-07 (one). FIXED with periods, per her minimal rewrites.
3. Vera V-TELL-STRUCT (advisory, "So" openers x5): ACCEPTED in part. Cut
   three ("So keep every word", "So here's the question", "So the hard
   lookup", "So a heatmap"); kept "So the field kept squeezing." (inside
   the S2-locked verbatim cold open) and the landing "So why did nobody
   just build it?" (earned, closes the hook).
4. Vera V-REGISTER (advisory): "The authors wrote, we suspect" clarified to
   "The authors themselves wrote, we suspect." Joke template 2 retained.
5. Vera V-HUMOR (advisory): beat-04a's "the pick is like..." echoed
   beat-01's construction. FIXED: "the pick just shrugs: kitten, noted...
   anyway, one hundred percent cat."
6. Vera V-RHYTHM (advisory, "Your hands already know it"): OVERRULED with
   rationale. The line is the locked beat-03 landing line (treatment §6);
   on the page track it is literal (the qk-explorer twin drives the same
   sweep by hand), and in-video the learner has just made the P2 call.
   Recorded as a standing style note for S6's Opus-tier Vera pass.
7. Sam map (advisory, non-gating): beat-06a overload and beat-07 pivot
   noted. Timing trim thinned beat-06a narration (109w to 97w) and beat-07
   gained an explicit callback ("Now the thought you've been holding")
   tying the 2019 verdict to the misconception held open since beat-04b.
   beat-06b w(1-w) now glossed in words ("the slope is weight times one
   minus weight"). The beat-04b sqrt bookkeeping open loop is deliberate
   (R20 open-loop window); kept.

## Timing honesty pass (Director)

Round-0 draft ran ~552s spoken against the 540s cap. All beats trimmed to
budget: 1283 words total, ~513s spoken plus ~14s explicit silences;
storyboard estimates now sum to 535s (cap 540, spine target 480 with the
treatment's trim plan still available).

L-checks after revision: all pass (L1-L10, V1).

## Cost

Sam $0.14, Petra $0.46, Vera $0.27. Round total ~$0.87.
