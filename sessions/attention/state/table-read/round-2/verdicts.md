# Table-read round 2 (S3), attention

Fresh quarantined critic sessions (Sonnet tier), same packet shapes as
round 1, revised artifacts. Raw prompts/outputs in this directory.

## Verdict counts

| Critic | Blocking | Advisory | Gate result |
|---|---|---|---|
| Sam | 0 (probes passed, see note) | 10 map entries (4 click, 3 overload, 3 notation) | PASS |
| Petra | 2 (R23, R24) | 1 (R2) | FAIL |
| Vera | 0 | 2 (V-REGISTER, V-BRAND) | PASS |

Sam probe note: Sam restated the aha correctly ("Attention is just a Python
dict where you replace the exact-match lookup with a similarity score and
replace return-one-value with return a weighted blend of all values, which
is what lets gradients flow through it": semantic match PASS) and answered
the driving question correctly. For probe 3 he answered the walk-home
breadcrumb (the script's final question) instead of the rebuild-from-memory
retrieval prompt; his breadcrumb inference (tag tokens with position) was
correct, and the retrieval content appears verbatim inside his aha answer.
Ruled PASS with an administration fix: round 3's task block names which
question is the retrieval prompt, as the harness grader would.

## Dispositions

1. Petra R23 (blocking): beat-05 morph ran in lockstep with narration.
   FIXED: the first dict row now morphs WORDLESS and holds a full beat
   before narration confirms ("Watch the first row argue for itself.");
   only the remaining rows are narrated. Storyboard visual + script updated.
2. Petra R24 (blocking): beat-05 refutation was narration-only. FIXED: a
   literal recipe-card graphic renders under the lilac weight bars as the
   line is spoken (ingredients = the four proportions, header "what got
   mixed", no why field, dim arrow pointing upstream to the scoring).
   Added to novelElements (3 of 4) and onScreenText.
3. Petra R2 (advisory): "we suspect" had no visual referent. ACCEPTED:
   citation chip (Vaswani et al. 2017: "we suspect") added to beat-06a
   visual + onScreenText.
4. Vera V-REGISTER (advisory, "kitten, noted... anyway"): OVERRULED with
   rationale: this is S2-locked graft G5 carrying the discarded-runner-up
   claim; round-1 Vera accepted the line (flagging only the construction
   echo, fixed in round 1). Standing ruling added to round-3 packet.
5. Vera V-BRAND (advisory, breadcrumb string mismatch): ACCEPTED in
   substance. The closing card cannot carry the canonical question verbatim
   while narration speaks it (L7 bans 8-word on-screen duplication), so the
   card now carries a compressed form of the SAME question ("For the walk
   home: what is the cheapest thing a token could carry so a lookup can
   find WHERE it sits?") instead of the previously different "how does
   order get in?" wording. Canonical string unchanged in the storyboard
   breadcrumbQuestion field and spoken in full.
6. Sam advisories: BLEU gloss added as an on-object axis label (beat-01);
   beat-04b housekeeping line now gives a reason in the moment ("keeps the
   numbers tame") with the full why still paid at beat-06a; beat-06a
   estimate raised to 45s for breathing room (two independent Sams read it
   as the densest stretch); beat-07's 2019 aside already re-anchored in
   round 1 ("Now the thought you've been holding").

## Timing

Estimates now: 92+35+55+50+46+60+45+40+60+55 = 538s (cap 540; spine target
480 preserved via the treatment trim plan). L-checks re-run: all pass.

## Cost

Sam $0.12, Petra $0.51, Vera $0.32. Round total ~$0.95.
