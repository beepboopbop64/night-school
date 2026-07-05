# Changelog: dotprod, round-03

Round total: $4.11 (triage $0.22). 4 change orders executed, 0 failed, 0 answered inline, 0 deferred, 1 style amendments drafted, 4 critic-miss entries logged.

## r03-n01 — APPLIED

**Note (n01, verbatim):** The stretch guess is dead on arrival: beat-02 already told the learner that stretching climbs the score, so asking "does its score change?" here is theater. Make this prediction do new work: ask a quantitative question the learner cannot already answer, "if you double c1's length exactly, what happens to the number, does it double?" Then the reveal teaches that the meter is linear in each input, which is exactly the fact the cheapest-fix breadcrumb needs. Same change in the page prose.

**Interpretation:** Replace beat-04's prediction prompt (the already-answered 'does its score change?') with the quantitative 'if you double c1's length exactly, does the number double?' and make the reveal teach that the meter is linear in each input (feeding the cheapest-fix breadcrumb); mirror the same change in the page prose.
**Confidence:** high
**Critic miss:** petra should have caught this (storyboard/beat-04.md).

**What changed:** page/sections/beat-04.md, storyboard.yaml, storyboard.yaml#beat-04 — Replaced beat-04's already-answered 'does its score change?' prediction with the quantitative 'if you double c1's length, does the number double?' and made the reveal teach that the meter is linear in each input, feeding the cheapest-fix breadcrumb; mirrored in page prose.

**Re-run verdicts (fresh caps):**

| node | gate | checks | cost |
|---|---|---|---|
| s4b.sec-beat-04 | pass | section.nonempty:pass, section.heading:pass, section.dash-lint:pass, section.aha-verbatim:pass | $0.05 |
| s4c.doc | pass | doc.dash-lint:pass, doc.aha-verbatim:pass, doc.no-handwave:pass, doc.vera-pass:pass | $0.73 |
| s4d.extensions | pass | ext.schema:pass, ext.source-whitelist:pass, ext.dash-lint:pass, ext.links-resolve:pass | $0.12 |
| s4e.notebook | pass | nb.json:pass, nb.numpy-only:pass, nb.executes:pass | $0.35 |

**Cost:** $1.62 (apply $0.38 + attributed re-runs)
**In blast radius but clean-skipped (bytes unchanged, $0):** s4a.beat-04, s5.assemble, s6.screening, s7.packet

## r03-n02 — APPLIED

**Note (n02, verbatim):** "Sit with that for a second" is the exact crutch phrase we banned two rounds ago, back again. And "for a second" appears twice on the page ("Step back from the sweep for a second"). Purge the sit-with construction entirely and vary the rhythm so no filler phrase repeats.

**Interpretation:** Purge the banned 'sit with that for a second' construction from beat-01 and remove the repeated 'for a second' filler ('Step back from the sweep for a second'), varying the rhythm so no filler phrase repeats.
**Confidence:** high
**Critic miss:** vera should have caught this (page/beat-01.md).

**What changed:** page/sections/beat-01.md — Purged the banned 'sit with that for a second' crutch in beat-01, replacing it with a varied-rhythm construction that repeats no filler phrase.

**Cost:** $0.06 (apply $0.06 + attributed re-runs)

## r03-n03 — APPLIED

**Note (n03, verbatim):** Two things, same goal: make the cheat visible. First, the integer rounding flattens the story: in the length-cheat state, doubled c1 reads "1" while unstretched c2 reads "1", so the scandal the narration promises is invisible in the numbers. One decimal place, so 0.3 becoming 0.7 is legible. Second, redesign the length-cheat drive state to show an overtake: stretch c1 until its raw score PASSES a better-aligned candidate's reading. The cheat has to land as a ranking flip you can see, not a subtle bump.

**Interpretation:** Change the interactive's numeric display to one decimal place so the length-cheat is legible (0.3->0.7 rather than 1 vs 1), and redesign the length-cheat drive state so stretching c1 makes its raw score overtake a better-aligned candidate — the cheat must land as a visible ranking flip.
**Confidence:** high
**Critic miss:** iris should have caught this (interactives/dot-alignment.py).

**What changed:** page/interactives/dot-alignment.yaml — Set the dot-product readouts to one decimal place and re-drove the length-cheat state to probe 70 (on c2) so stretching c1 overtakes the honestly-aligned c2 as a visible ranking flip.

**Re-run verdicts (fresh caps):**

| node | gate | checks | cost |
|---|---|---|---|
| s4b.dot-alignment | pass | weba11y.clean:pass, iris.pass:pass | $1.77 |

**Cost:** $2.13 (apply $0.36 + attributed re-runs)

## r03-n04 — APPLIED

**Note (n04, verbatim):** The second LLM prompt tells the learner they "learned that scaled dot-product attention is a bank of similarity meters" in this session. They did not; this session taught the dot product. A learner reads that and wonders what they missed. Reframe it as a forward stretch ("next session's machine, if you want a preview tonight") grounded in what was actually taught, or replace it with a prompt about tonight's content.

**Interpretation:** Fix the second LLM extension prompt's false claim that the learner 'learned that scaled dot-product attention is a bank of similarity meters' this session; reframe it as a forward-stretch preview ('next session's machine, if you want a preview tonight') grounded in what was actually taught.
**Alternative considered (recorded because the note is ambiguous):** Replace the prompt entirely with one about tonight's content (the plain dot product / the length problem).
**Confidence:** medium
**Critic miss:** sam should have caught this (ext.md).

**What changed:** extensions.yaml — Reframed the second LLM prompt's false 'you learned' claim about scaled dot-product attention into a forward-stretch preview of next session's machine, grounded in tonight's dot-product work.

**Cost:** $0.08 (apply $0.08 + attributed re-runs)

## r03-n05 — STYLE-AMENDMENT

**Note (n05, verbatim):** #style: a prediction prompt must ask something the learner does not already know. If an earlier beat revealed the answer, the prompt moves to a sharper question (a quantity, a direction, a boundary case); it never re-asks the known.

**Interpretation:** Draft a show-bible rule requiring every prediction prompt to ask something the learner does not already know, sharpening to a new quantity, direction, or boundary case when an earlier beat revealed the answer.
**Confidence:** high

**Drafted show-bible amendment** (show-bible/voice/proposed-amendments.md, awaiting Jake's ratification): A prediction prompt must ask something the learner does not yet know; if an earlier beat already revealed the answer, sharpen the prompt to a new quantity, direction, or boundary case rather than re-asking the known.

## Re-run failures flagged NEEDS_JAKE

- s4a.beat-04

## Dirty set & estimates (as planned)

| order | targets | dirty nodes (first-attributed cost) | est. |
|---|---|---|---|
| r03-n01 | storyboard#beat-04, video/beat-04, page/beat-04 | s4a.beat-04 ($1.37), s4b.sec-beat-04 ($0.05), s4c.doc ($0.93), s4d.extensions ($0.12), s4e.notebook ($0.41), s5.assemble ($0.00), s6.screening ($0.92), s7.packet ($0.00) | $4.61 |
| r03-n02 | page/beat-01 | s5.assemble (–), s6.screening (–), s7.packet (–) | $0.80 |
| r03-n03 | ix/dot-alignment | s4b.dot-alignment ($2.16), s5.assemble (–), s6.screening (–), s7.packet (–) | $2.96 |
| r03-n04 | ext | s5.assemble (–), s6.screening (–), s7.packet (–) | $0.80 |

## Hash-preservation proof (§7.5)

Untouched artifacts are proven byte-identical: `before` is the sha256 the
pre-round receipts recorded, `after` is the artifact re-hashed after the
round. Rows marked `(fragment)` prove per-beat isolation inside
storyboard.yaml/script.md via canonical fragment hashes; the merge module
additionally refuses any splice that alters untouched beats.

| artifact | before | after | status |
|---|---|---|---|
| doc/lesson.md | 38120d6551fa | c9e3438d6555 | revised |
| extensions.yaml | f15618c10169 | 5f684b895201 | revised |
| manifest.yaml | 3fa6c804e76a | 3fa6c804e76a | byte-identical |
| media/beat-01.mp4 | 6600dc697c24 | 6600dc697c24 | byte-identical |
| media/beat-02.mp4 | 3537ccba6d39 | 3537ccba6d39 | byte-identical |
| media/beat-03.mp4 | 1dc29a29d6ab | 1dc29a29d6ab | byte-identical |
| media/beat-04.mp4 | a8abde25d3d5 | a8abde25d3d5 | byte-identical |
| media/session.mp4 | 55b46f7483b3 | 55b46f7483b3 | byte-identical |
| notebook/lesson.ipynb | 8a093a3a9c83 | fad2b82583e8 | revised |
| page/extensions.json | 48e2315aa114 | 48e2315aa114 | byte-identical |
| page/interactives/DotAlignment.svelte | de8adbccfbd8 | 6243b4489f51 | revised |
| page/sections/beat-01.md | 40436205c398 | 64c2346916b9 | revised |
| page/sections/beat-02.md | ab8d802ee89a | ab8d802ee89a | byte-identical |
| page/sections/beat-03.md | e6b35d9b0ebe | e6b35d9b0ebe | byte-identical |
| page/sections/beat-04.md | 3711c2cb6f89 | 9dedd8a38baa | revised |
| page/video.json | 35e578bbc0f3 | 35e578bbc0f3 | byte-identical |
| rounds/round-03/flags.md | c6d73c781296 | c6d73c781296 | byte-identical |
| rounds/round-03/notes.md | 75468c28129f | 6d26bd0bf841 | revised |
| rounds/round-03/packet/README.md | 7b58ed9c90af | 7b58ed9c90af | byte-identical |
| rounds/round-03/screening-report.md | f23df80382c1 | f23df80382c1 | byte-identical |
| video/audio/beat-01.mp3 | 35eea7a82b36 | 35eea7a82b36 | byte-identical |
| video/audio/beat-02.mp3 | ef5c80d0882d | ef5c80d0882d | byte-identical |
| video/audio/beat-03.mp3 | 5b4da1b214e9 | 5b4da1b214e9 | byte-identical |
| video/audio/beat-04.mp3 | 84183fe2fa68 | 84183fe2fa68 | byte-identical |
| video/beats/beat-01.yaml | 1e531d5522a4 | 1e531d5522a4 | byte-identical |
| video/beats/beat-02.yaml | 44b23badca5b | 44b23badca5b | byte-identical |
| video/beats/beat-03.yaml | 6f73ae343ccd | 6f73ae343ccd | byte-identical |
| video/beats/beat-04.yaml | 3834d2a4d191 | 6e0d38c207b0 | VIOLATION |
| video/captions.vtt | ac06c839567d | ac06c839567d | byte-identical |
| video/scenes/scene_beat_01.py | 1825786ec58d | 1825786ec58d | byte-identical |
| video/scenes/scene_beat_02.py | f72cdb78b56c | f72cdb78b56c | byte-identical |
| video/scenes/scene_beat_03.py | 0809a87bacbd | 0809a87bacbd | byte-identical |
| video/scenes/scene_beat_04.py | 0620c7ca1a58 | 23deb81ad9ba | VIOLATION |
| script.md#beat-01 (fragment) | 3a9ffed85063 | 3a9ffed85063 | byte-identical |
| script.md#beat-02 (fragment) | 4b817f3b661c | 4b817f3b661c | byte-identical |
| script.md#beat-03 (fragment) | 3dbf70c80cd9 | 3dbf70c80cd9 | byte-identical |
| script.md#beat-04 (fragment) | 4e3f969f8849 | 4e3f969f8849 | byte-identical |
| storyboard.yaml#beat-01 (fragment) | f511152447e9 | f511152447e9 | byte-identical |
| storyboard.yaml#beat-02 (fragment) | 73f262919de1 | 73f262919de1 | byte-identical |
| storyboard.yaml#beat-03 (fragment) | e604cf58ab95 | e604cf58ab95 | byte-identical |
| storyboard.yaml#beat-04 (fragment) | ded0f775f295 | 966232540f58 | revised |

**31 untouched artifacts byte-identical, 8 revised as ordered, 2 VIOLATIONS.**
