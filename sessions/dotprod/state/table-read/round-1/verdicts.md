# Table-read round 1 (Phase 3 spine rewrite), dotprod

Date: 2026-07-05. Critics spawned as fresh quarantined sessions (Sonnet
tier), one per agent, inputs per ARCHITECTURE §5 quarantine: Sam saw
script.md only; Petra saw spine.md + storyboard.yaml + script.md + the
R1-R30 digest; Vera saw script.md + extracted learner-facing storyboard
copy. Raw prompts and outputs in this directory. Mechanical gate before
the round: lcheck L1-L12 + V1 all pass (L12 is the new single-thread
discipline check this phase introduced).

## Verdict counts

| Critic | Blocking | Advisory | Gate result |
|---|---|---|---|
| Sam | 0 (all 3 probes passed) | 10 map entries (4 click, 3 confusion, 1 overload, 1 boredom, 1 notation) | PASS |
| Petra | 1 (R19) | 2 (R23, R25) + 1 explicit pass note (R12) | FAIL |
| Vera | 3 (V-TELL-VOCAB x2, V-HONESTY) | 4 (V-TELL-STRUCT x2, V-RHYTHM, V-REGISTER) | FAIL |

Sam probe answers: driving question correct; retrieval answer correct
("multiply their matching entries together, then add up those products");
aha restated as a similarity meter that tracks direction and is fooled by
length. Semantic match to the canonical sentence: PASS.

## Dispositions

1. Vera V-HONESTY (blocking): the hook stated a second-person scenario as
   fact ("Your music app just played you..."). ACCEPTED, her minimal
   rewrite: "Say your music app plays you a song you love..." with the
   next sentence's tense trued to match. Applied to storyboard + script,
   and the same framing fix mirrored into doc/lesson.md and
   page/sections/beat-01.md so the surfaces do not drift.
2. Vera V-TELL-VOCAB beat-01 (blocking): "But sit with what that
   comparison has to do." ACCEPTED in spirit: rewritten to "But weigh
   what that comparison has to do." (keeps the measuring register the
   session lives in).
3. Vera V-TELL-VOCAB / V-REGISTER on beat-03's "Look at what your hands
   just learned." OVERRULED with rationale (same ruling as the M5
   attention table-read on the identical construction): beat-03 is the
   locked aha beat this phase explicitly does not touch, and on the page
   track the line is literal, the dot-alignment interactive twin drives
   the same sweep by hand. Recorded as a standing style note for S6's
   Opus-tier Vera pass.
4. Vera V-TELL-STRUCT beat-02 (advisory): colon-fragment list in the
   struggle recap. ACCEPTED, folded into the Petra R25 fix below (the
   recap now names two concrete failed attempts as sentences).
5. Vera V-RHYTHM beat-02 (advisory): four clipped sentences in a row at
   the instrument. ACCEPTED in part: the last two merged into one longer
   sentence; the clipped cadence for probe/candidates stays (pre-training
   one element per breath is doing pedagogy work).
6. Vera V-TELL-STRUCT beat-05 (advisory): ACCEPTED, colon swapped for a
   period ("Now invent your own pair. Anything you can describe...").
7. Petra R19 (blocking): OVERRULED AS ALREADY SATISFIED, with rationale.
   No R19 credit is claimed for beat-01's question; it is the R16
   organizer exactly as her own suggestion asks ("Leave beat-01's
   question as the R16 organizer"). The beat-03 reveal window is covered
   by beat-02's falsifiable predictionPrompt ("does any score go
   negative?", expectedWrongAnswer declared), and the beat-04b reveal by
   its own doubling prompt; both are mechanical L4 facts of the
   storyboard she reviewed. Nothing to change; recorded so round 2's
   Petra can confirm or dissent.
8. Petra R25 (advisory): ACCEPTED in part. The beat-02 struggle recap no
   longer merely asserts "it fought back"; it now names the two natural
   attempts and their failures ("Add everything up and loudness wins,
   not agreement. Count exact matches and nothing ever matches.") so the
   learner's own attempt is explicitly compared to failure modes before
   the canonical recipe lands. Also cashes out Sam's beat-01 confusion
   note about the lottery line staying abstract.
9. Petra R23 (advisory): OVERRULED with rationale. beat-03 is locked this
   phase; the reveal is one step from the learner by her own reading, the
   beat-02 prediction does the connecting, and the aha carrier beat is
   string-matched machinery (ahaBeatId) this phase must not move.
   Recorded as a standing note for the next spine-touch round.
10. Sam map (advisory, non-gating): beat-05 walk-home confusion is the
    breadcrumb working as designed (the gap stays open by pedagogy-bible
    rule; no surface may state the answer). beat-02 overload note stands
    at the L2 cap of 4 novel elements; the page section carries the same
    introduction learner-paced. beat-03 dial-recap boredom recorded
    (locked beat). beat-04b "why does linearity mean exact doubling"
    left as a medium-difficulty inference (R22).

## Revision

storyboard.yaml + script.md revised together (narration verbatim-identical
between them, checked mechanically); beat word counts re-estimated at 150
wpm: 58 + 100 + 36 + 40 + 38 + 36 = 308s of 540 (L10). lcheck L1-L12 + V1
re-run after revision: all pass.

## Round 2 plan

Re-run all three critics cold on the revised artifacts; Petra and Vera
additionally receive this round's report and dispositions (per the
severity-calibration protocol on prior-round reports). Gate: Sam probes
pass, zero blocking from Petra and Vera.
