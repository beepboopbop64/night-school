# Changelog: dotprod, round-05

Round total: $5.33 (triage $0.32). 4 change orders executed, 2 failed, 0 answered inline, 0 deferred, 3 style amendments drafted, 6 critic-miss entries logged.

## r05-n01 — APPLIED

**Note (n01, verbatim):** Jake's core complaint this round: the lesson keeps tiptoeing around the actual math. The page now runs the worked calculation and states the formal line; the video must match. Add to this beat's narration, right after the aha sentence lands: "In symbols, a dot b: multiply the matching entries, add the products. The taste and song from the worked chip, two and one dot one and three, come out to five. Same recipe, now wearing its symbol." And in the visual, the a . b annotation must true up NEXT TO the worked chip's numerals so the symbol is anchored to numbers the viewer already computed (this is also Petra's standing R11 advisory from the table-read). Keep the aha sentence and everything else untouched.

**Interpretation:** In beat-03, add to the narration right after the aha sentence the lines 'In symbols, a dot b: multiply the matching entries, add the products. The taste and song from the worked chip, two and one dot one and three, come out to five. Same recipe, now wearing its symbol.'; and in the storyboard/scene, true up the a·b annotation NEXT TO the worked chip's numerals. Keep the aha sentence and everything else untouched.
**Confidence:** high
**Critic miss:** petra should have caught this (video/scenes/scene_03.py, R11).

**What changed:** script.md, script.md#beat-03, storyboard.yaml, storyboard.yaml#beat-03 — Beat-03: added the four symbol-anchoring narration lines right after the aha sentence and trued up the a·b annotation next to the worked chip's numerals; aha sentence and all else untouched.

**Re-run verdicts (fresh caps):**

| node | gate | checks | cost |
|---|---|---|---|
| s4f.beat-03 | pass | tts.safe-lint:pass, tts.audio-written:pass | $0.00 |
| s4a.beat-03 | pass | bbox.clean:pass, iris.pass:pass, scene.duration-within-tolerance:pass | $1.55 |
| s4b.sec-beat-03 | pass | section.nonempty:pass, section.heading:pass, section.dash-lint:pass, section.aha-verbatim:pass, section.no-wrapper-tags:pass | $0.14 |
| s4c.doc | pass | doc.dash-lint:pass, doc.aha-verbatim:pass, doc.no-handwave:pass, doc.vera-pass:pass | $1.24 |
| s4d.extensions | pass | ext.schema:pass, ext.source-whitelist:pass, ext.dash-lint:pass, ext.links-resolve:pass | $0.41 |
| s4e.notebook | pass | nb.json:pass, nb.numpy-only:pass, nb.executes:pass | $0.79 |

**Cost:** $4.25 (apply $0.11 + attributed re-runs)
**In blast radius but clean-skipped (bytes unchanged, $0):** s5.assemble, s6.screening, s7.packet

## r05-n02 — FAILED

**Note (n02, verbatim):** Already applied by the judge, record as ruling: the semicolon splice in "Try answering it first; it's genuinely harder" was split into two sentences.

**Interpretation:** Already applied by the judge; record as ruling: the semicolon splice in 'Try answering it first; it's genuinely harder' was split into two sentences.
**Confidence:** high
**Critic miss:** vera should have caught this (page/sections/beat-01.md).

**FAILED to apply:** r05-n02: application failed twice: merge: edit target not found in page/sections/beat-01.md: "Try answering it first; it's genuinely harder than it sounds."

## r05-n03 — APPLIED

**Note (n03, verbatim):** Already applied by the judge, record as rulings: (1) the section now runs the full worked calculation with real numbers before the prediction (taste (2, 1), song (1, 3), 2×1 + 1×3 = 5, "run it once by hand"), and the prediction references the recipe ("Can the multiply-and-add ever push a bar below zero?") instead of bars the reader has not met; (2) the interactive's objects are introduced by their story names (amber probe is your taste; the four songs are Night Drive, Glass Rain, Slow Burn, Static); (3) the stretch paragraph names Night Drive and its round handle, and the splice "changed; it never" was split.

**Interpretation:** Already applied by the judge; record as rulings on beat-02's page section: (1) the full worked calculation with real numbers (taste (2,1), song (1,3), 2×1+1×3=5, 'run it once by hand') now runs before the prediction, and the prediction references the recipe ('Can the multiply-and-add ever push a bar below zero?') not un-met bars; (2) the interactive's objects are introduced by story names (amber probe = your taste; songs Night Drive, Glass Rain, Slow Burn, Static); (3) the stretch paragraph names Night Drive and its round handle, and the 'changed; it never' splice was split.
**Confidence:** high
**Critic miss:** petra should have caught this (page/sections/beat-02.md).

**What changed:** page/sections/beat-02.md — Aligned beat-02's interactive intro to the judge's ruling phrasing (amber probe = your taste); worked calculation before prediction, recipe-referenced prediction, story names, and split splice were already in place and are recorded as applied.

**Cost:** $0.49 (apply $0.49 + attributed re-runs)

## r05-n04 — APPLIED

**Note (n04, verbatim):** Already applied by the judge, record as ruling: the naming beat now states the formal definition, a · b = a₁b₁ + a₂b₂ + …, re-run on the same worked example (2, 1) · (1, 3) = 5, placed after the aha sentence. The symbol arrives carrying the calculation.

**Interpretation:** Already applied by the judge; record as ruling: beat-03's page section now states the formal definition a · b = a₁b₁ + a₂b₂ + …, re-run on the worked example (2,1)·(1,3)=5, placed after the aha sentence so the symbol arrives carrying the calculation.
**Confidence:** high
**Critic miss:** petra should have caught this (page/sections/beat-03.md, R11).

**What changed:** page/sections/beat-03.md — Moved the formal definition and re-run (2,1)·(1,3)=5 to directly after the aha sentence so the symbol arrives carrying the calculation.

**Cost:** $0.15 (apply $0.15 + attributed re-runs)

## r05-n05 — FAILED

**Note (n05, verbatim):** Already applied by the judge, record as ruling: every "c1" became "Night Drive" so the prose names match the widget (the tracer's T2 catch). Same fix applied in the doc's honest-look section.

**Interpretation:** Already applied by the judge; record as ruling: every 'c1' became 'Night Drive' in beat-04b's page section (and the doc's honest-look section) so the prose names match the widget.
**Confidence:** high
**Critic miss:** vera should have caught this (page/sections/beat-04b.md).

**FAILED to apply:** r05-n05: application failed twice: merge: edit target not found in page/sections/beat-04b.md: "c1"

## r05-n06 — APPLIED

**Note (n06, verbatim):** Already applied by the judge, record as ruling: the meter cards moved below the arena so the arena renders at full card width (620px); the arrows must stay clearly legible at every viewport.

**Interpretation:** Already applied by the judge; record as ruling: the meter cards moved below the arena so it renders at full card width (620px); the arrows must stay clearly legible at every viewport.
**Confidence:** high
**Critic miss:** iris should have caught this (ix/dot-alignment/widget.tsx).

**What changed:** page/interactives/dot-alignment.yaml — Moved the score meter cards below the arena so the arena renders at full card width (620px), and required arrows stay clearly legible at every viewport.

**Cost:** $0.12 (apply $0.12 + attributed re-runs)
**In blast radius but clean-skipped (bytes unchanged, $0):** s4b.dot-alignment

## r05-n07 — STYLE-AMENDMENT

**Note (n07, verbatim):** #style: before any prediction that depends on a computation, the surface states the full worked calculation with real numbers the learner can check by hand. Abstract recipes ("multiply entry by entry") never carry a prediction alone.

**Interpretation:** Taste rule for the show bible: worked calculations must precede any computation-dependent prediction; no session fix demanded here.
**Confidence:** high

**Drafted show-bible amendment** (show-bible/voice/proposed-amendments.md, awaiting Jake's ratification): Before any prediction that depends on a computation, state the full worked calculation with real numbers the learner can check by hand; never let an abstract recipe carry a prediction alone.

## r05-n08 — STYLE-AMENDMENT

**Note (n08, verbatim):** #style: every named object keeps ONE name across every surface: page, doc, video, and widget agree (Night Drive, never c1). A reader who meets two names for one thing assumes two things.

**Interpretation:** Taste rule for the show bible: one name per named object across every surface; no session fix demanded here.
**Confidence:** high

**Drafted show-bible amendment** (show-bible/voice/proposed-amendments.md, awaiting Jake's ratification): Give every named object exactly one name across every surface — page, doc, video, and widget must agree (e.g. Night Drive, never c1).

## r05-n09 — STYLE-AMENDMENT

**Note (n09, verbatim):** #style: the formal symbol is always anchored to the worked numbers the learner already computed, on every surface where the symbol appears; a symbol floating without its numbers reads as decoration.

**Interpretation:** Taste rule for the show bible: formal symbols must be anchored to already-computed worked numbers on every surface; no session fix demanded here.
**Confidence:** high

**Drafted show-bible amendment** (show-bible/voice/proposed-amendments.md, awaiting Jake's ratification): Anchor every formal symbol to the worked numbers the learner already computed, on every surface where the symbol appears.

## Re-run failures flagged NEEDS_JAKE

- s4b.dot-alignment

## Dirty set & estimates (as planned)

| order | targets | dirty nodes (first-attributed cost) | est. |
|---|---|---|---|
| r05-n01 | script#beat-03, storyboard#beat-03, video/beat-03 | s4f.beat-03 ($0.00), s4a.beat-03 ($1.50), s4b.sec-beat-03 ($0.09), s4c.doc ($2.48), s4d.extensions ($0.37), s4e.notebook ($0.95), s5.assemble ($0.00), s6.screening ($1.49), s7.packet ($0.00) | $7.68 |
| r05-n02 | page/beat-01 | s5.assemble (–), s6.screening (–), s7.packet (–) | $0.80 |
| r05-n03 | page/beat-02 | s5.assemble (–), s6.screening (–), s7.packet (–) | $0.80 |
| r05-n04 | page/beat-03 | s5.assemble (–), s6.screening (–), s7.packet (–) | $0.80 |
| r05-n05 | page/beat-04b, doc | s4e.notebook (–), s5.assemble (–), s6.screening (–), s7.packet (–) | $0.80 |
| r05-n06 | ix/dot-alignment | s4b.dot-alignment ($3.36), s5.assemble (–), s6.screening (–), s7.packet (–) | $4.16 |

## Hash-preservation proof (§7.5)

Untouched artifacts are proven byte-identical: `before` is the sha256 the
pre-round receipts recorded, `after` is the artifact re-hashed after the
round. Rows marked `(fragment)` prove per-beat isolation inside
storyboard.yaml/script.md via canonical fragment hashes; the merge module
additionally refuses any splice that alters untouched beats.

| artifact | before | after | status |
|---|---|---|---|
| doc/lesson.md | a0b49b136749 | a042eedcddcf | revised |
| extensions.yaml | fa44e3890d5a | 87f04bb25c68 | revised |
| manifest.yaml | 7892bc247afd | 7892bc247afd | byte-identical |
| media/beat-01.mp4 | 40b23ba84b64 | 40b23ba84b64 | byte-identical |
| media/beat-02.mp4 | 1b769e03ed1b | 1b769e03ed1b | byte-identical |
| media/beat-03.mp4 | c59dd83afc19 | a71fd2368d2d | revised |
| media/beat-04.mp4 | 3c048169395f | 3c048169395f | byte-identical |
| media/beat-04b.mp4 | 3165fc80c4c9 | 3165fc80c4c9 | byte-identical |
| media/beat-05.mp4 | e69aae92dbbb | e69aae92dbbb | byte-identical |
| media/session.mp4 | 3a538095330d | 3a538095330d | byte-identical |
| notebook/lesson.ipynb | bfdeff01864f | e1d7cfc5217a | revised |
| page/extensions.json | cf44c7db90f3 | cf44c7db90f3 | byte-identical |
| page/interactives/DotAlignment.svelte | 7ecc5b073eb3 | 6a27ed4fd84a | revised |
| page/sections/beat-01.md | 771935542d19 | 5e7bd4e4114c | VIOLATION |
| page/sections/beat-02.md | 295981c5b60c | 5df43c1a3cd4 | revised |
| page/sections/beat-03.md | 1535b52444e3 | 3fa35e473d07 | revised |
| page/sections/beat-04.md | 8c6cf68539b8 | 8c6cf68539b8 | byte-identical |
| page/sections/beat-04b.md | a913b0662a23 | b3c79c4174ee | VIOLATION |
| page/sections/beat-05.md | 4d5bcaac8ba7 | 4d5bcaac8ba7 | byte-identical |
| page/video.json | 2a248bea8ac2 | 2a248bea8ac2 | byte-identical |
| rounds/round-05/flags.md | ced8fe942554 | ced8fe942554 | byte-identical |
| rounds/round-05/notes.md | 1020eaf4a9fd | 5c1a0a80c9af | revised |
| rounds/round-05/packet/README.md | 41a526df6ad6 | 41a526df6ad6 | byte-identical |
| rounds/round-05/screening-report.md | 56bb66b6d426 | 56bb66b6d426 | byte-identical |
| video/audio/beat-01.mp3 | fa401886b353 | fa401886b353 | byte-identical |
| video/audio/beat-02.mp3 | d509e6bc23ca | d509e6bc23ca | byte-identical |
| video/audio/beat-03.mp3 | 5b4da1b214e9 | d2db6f3fd6a1 | revised |
| video/audio/beat-04.mp3 | b4a6f2313379 | b4a6f2313379 | byte-identical |
| video/audio/beat-04b.mp3 | 9ad0e1b8d5f9 | 9ad0e1b8d5f9 | byte-identical |
| video/audio/beat-05.mp3 | 82b8b1479e96 | 82b8b1479e96 | byte-identical |
| video/beats/beat-01.yaml | 8cca5c0ac1cd | 8cca5c0ac1cd | byte-identical |
| video/beats/beat-02.yaml | 6b2cee3d02d9 | 6b2cee3d02d9 | byte-identical |
| video/beats/beat-03.yaml | 7edc30dc4a10 | 31107fb2722a | revised |
| video/beats/beat-04.yaml | ba2ff08ae800 | ba2ff08ae800 | byte-identical |
| video/beats/beat-04b.yaml | 9088ec70a353 | 9088ec70a353 | byte-identical |
| video/beats/beat-05.yaml | ed1b18ca0a08 | ed1b18ca0a08 | byte-identical |
| video/captions.vtt | 689dc21d3f90 | 689dc21d3f90 | byte-identical |
| video/scenes/scene_beat_01.py | 259cd24181f2 | 259cd24181f2 | byte-identical |
| video/scenes/scene_beat_02.py | 97c65bffb647 | 97c65bffb647 | byte-identical |
| video/scenes/scene_beat_03.py | 9784ed7bd10b | e401cf77c15b | revised |
| video/scenes/scene_beat_04.py | 1dd8def55963 | 1dd8def55963 | byte-identical |
| video/scenes/scene_beat_04b.py | 1a89b8442035 | 1a89b8442035 | byte-identical |
| video/scenes/scene_beat_05.py | e22e594ddee3 | e22e594ddee3 | byte-identical |
| script.md#beat-01 (fragment) | 68f7f031fabf | 68f7f031fabf | byte-identical |
| script.md#beat-02 (fragment) | 68408f211973 | 68408f211973 | byte-identical |
| script.md#beat-03 (fragment) | 2a5966c2beba | 453c2a56a12b | revised |
| script.md#beat-04 (fragment) | fbd7e1e9a03b | fbd7e1e9a03b | byte-identical |
| script.md#beat-04b (fragment) | 87a0f42c94f5 | 87a0f42c94f5 | byte-identical |
| script.md#beat-05 (fragment) | ae5784affafe | ae5784affafe | byte-identical |
| storyboard.yaml#beat-01 (fragment) | 8b67ba127661 | 8b67ba127661 | byte-identical |
| storyboard.yaml#beat-02 (fragment) | c0f1edc3acfa | c0f1edc3acfa | byte-identical |
| storyboard.yaml#beat-03 (fragment) | 0ca0457503ee | 1341bdf80dcd | revised |
| storyboard.yaml#beat-04 (fragment) | 3a2a174f0875 | 3a2a174f0875 | byte-identical |
| storyboard.yaml#beat-04b (fragment) | 6f35947a6734 | 6f35947a6734 | byte-identical |
| storyboard.yaml#beat-05 (fragment) | 38a068481d92 | 38a068481d92 | byte-identical |

**40 untouched artifacts byte-identical, 13 revised as ordered, 2 VIOLATIONS.**
