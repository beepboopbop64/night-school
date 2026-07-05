# Changelog: dotprod, round-01

Round total: $3.88 (triage $0.15). 3 change orders executed, 0 failed, 0 answered inline, 0 deferred, 1 style amendments drafted, 3 critic-miss entries logged.

## r01-n01 — APPLIED

**Note (n01, verbatim):** When the probe sweeps near candidate B, the B label gets buried under the amber arrow and disappears. Keep every candidate label readable at all probe angles; nudging the labels outward past the arrow tips would probably do it.

**Interpretation:** Keep every candidate label readable at all probe angles; nudge labels outward past the arrow tips so the amber probe arrow never buries a label (esp. candidate B).
**Confidence:** high
**Critic miss:** iris should have caught this (video/scenes/scene_02.py).

**What changed:** storyboard.yaml, storyboard.yaml#beat-02 — Nudged each candidate label outward past its arrow tip so the amber probe never buries a label (esp. B) at any sweep angle; storyboard visual only, narration untouched.

**Re-run verdicts (fresh caps):**

| node | gate | checks | cost |
|---|---|---|---|
| s4a.beat-02 | pass | bbox.clean:pass, iris.pass:pass, scene.duration-within-tolerance:pass | $1.21 |
| s4b.sec-beat-02 | pass | section.nonempty:pass, section.heading:pass, section.dash-lint:pass, section.aha-verbatim:pass | $0.05 |
| s4c.doc | pass | doc.dash-lint:pass, doc.aha-verbatim:pass, doc.no-handwave:pass, doc.vera-pass:pass | $0.49 |
| s4d.extensions | pass | ext.schema:pass, ext.source-whitelist:pass, ext.dash-lint:pass, ext.links-resolve:pass | $0.10 |
| s4e.notebook | pass | nb.json:pass, nb.numpy-only:pass, nb.executes:pass | $0.31 |
| s5.assemble | pass | assemble.av-drift:pass, assemble.captions-written:pass, assemble.aha-consistency:pass, assemble.lchecks-rerun:pass, assemble.token-lint:pass, assemble.site-built:pass, assemble.manifest-complete:pass | $0.00 |
| s7.packet | pass | packet.serves-locally:pass, packet.notes-preseeded:pass, packet.flags-written:pass | $0.00 |

**Cost:** $2.35 (apply $0.20 + attributed re-runs)
**In blast radius but clean-skipped (bytes unchanged, $0):** s6.screening

## r01-n02 — APPLIED

**Note (n02, verbatim):** "The question worth sitting with tonight" uses the exact crutch phrase Vera flagged at screening. Rephrase so "sit with" appears at most once in the whole session.

**Interpretation:** Rephrase 'The question worth sitting with tonight' to drop the 'sit with' crutch so the phrase appears at most once across the whole session.
**Confidence:** high
**Critic miss:** vera should have caught this (page/beat-01).

**What changed:** page/sections/beat-01.md — Rephrased 'sitting with' to 'chewing on' in beat-01 to drop the 'sit with' crutch flagged by Vera.

**Cost:** $0.04 (apply $0.04 + attributed re-runs)

## r01-n03 — APPLIED

**Note (n03, verbatim):** The numbers under the bars feel busy.

**Interpretation:** Guessing at the fix: reduce visual busyness of the numeric readouts beneath the bars in the dot-alignment interactive (fewer/cleaner numbers).
**Alternative considered (recorded because the note is ambiguous):** Jake wants the numbers removed entirely rather than simplified.
**Confidence:** low
**Critic miss:** iris should have caught this (ix/dot-alignment).

**What changed:** page/interactives/dot-alignment.yaml — Simplified the numeric readouts under the bars (round to whole numbers, small and low-contrast) so bars carry the motion, per Jake's busyness note.

**Re-run verdicts (fresh caps):**

| node | gate | checks | cost |
|---|---|---|---|
| s4b.dot-alignment | pass | weba11y.clean:pass, iris.pass:pass | $1.15 |

**Cost:** $1.33 (apply $0.18 + attributed re-runs)

## r01-n04 — STYLE-AMENDMENT

**Note (n04, verbatim):** #style: when a demo puts a computed number on screen, round the readout to at most two decimals; full float precision reads as debug output, not teaching.

**Interpretation:** General taste rule; no one-off session fix demanded.
**Confidence:** high

**Drafted show-bible amendment** (show-bible/voice/proposed-amendments.md, awaiting Jake's ratification): Round any computed number shown on screen to at most two decimal places.

## Re-run failures flagged NEEDS_JAKE

- s6.screening

## Dirty set & estimates (as planned)

| order | targets | dirty nodes (first-attributed cost) | est. |
|---|---|---|---|
| r01-n01 | storyboard#beat-02, video/beat-02 | s4a.beat-02 ($1.12), s4b.sec-beat-02 ($0.03), s4c.doc ($0.44), s4d.extensions ($0.10), s4e.notebook ($0.46), s5.assemble ($0.00), s6.screening ($1.24), s7.packet ($0.00) | $4.18 |
| r01-n02 | page/beat-01 | s5.assemble (–), s6.screening (–), s7.packet (–) | $0.80 |
| r01-n03 | ix/dot-alignment | s4b.dot-alignment ($1.26), s5.assemble (–), s6.screening (–), s7.packet (–) | $2.06 |

## Hash-preservation proof (§7.5)

Untouched artifacts are proven byte-identical: `before` is the sha256 the
pre-round receipts recorded, `after` is the artifact re-hashed after the
round. Rows marked `(fragment)` prove per-beat isolation inside
storyboard.yaml/script.md via canonical fragment hashes; the merge module
additionally refuses any splice that alters untouched beats.

| artifact | before | after | status |
|---|---|---|---|
| doc/lesson.md | 8c3018b4fa58 | 4804b0736ab0 | revised |
| extensions.yaml | cf9bdadda77c | cf9bdadda77c | byte-identical |
| manifest.yaml | 3fa6c804e76a | 3fa6c804e76a | byte-identical |
| media/beat-01.mp4 | c6578f7b293d | c6578f7b293d | byte-identical |
| media/beat-02.mp4 | 97cef7dc320b | 2c9af7927dc9 | revised |
| media/beat-03.mp4 | 323a9e2bbaa7 | 323a9e2bbaa7 | byte-identical |
| media/beat-04.mp4 | 3ccff65eafa9 | 3ccff65eafa9 | byte-identical |
| media/session.mp4 | aa2fe7a00f9e | 9f9929bc45b2 | revised |
| notebook/lesson.ipynb | a7f0b5c38bfd | 460ad1ceb72d | revised |
| page/interactives/DotAlignment.svelte | 1be655b6dcef | 95621fe8e206 | revised |
| page/sections/beat-01.md | 704621587b2f | 804d01b0bda6 | revised |
| page/sections/beat-02.md | 174c6e778cc1 | 18861f739876 | revised |
| page/sections/beat-03.md | e6b35d9b0ebe | e6b35d9b0ebe | byte-identical |
| page/sections/beat-04.md | da0d78276dd7 | da0d78276dd7 | byte-identical |
| page/video.json | c83c31183255 | c83c31183255 | byte-identical |
| rounds/round-01/flags.md | 90111d408d6e | 90111d408d6e | byte-identical |
| rounds/round-01/notes.md | c98e40a91a30 | d64a8ee48ecc | VIOLATION |
| rounds/round-01/packet/README.md | 65456d684cdb | 65456d684cdb | byte-identical |
| rounds/round-01/screening-report.md | a8ba8a8bb8e4 | a8ba8a8bb8e4 | byte-identical |
| video/audio/beat-01.mp3 | c2e113c8269d | c2e113c8269d | byte-identical |
| video/audio/beat-02.mp3 | 6e4f70ac1645 | 6e4f70ac1645 | byte-identical |
| video/audio/beat-03.mp3 | 33d5747c04c6 | 33d5747c04c6 | byte-identical |
| video/audio/beat-04.mp3 | d5734446c931 | d5734446c931 | byte-identical |
| video/beats/beat-01.yaml | 8b49598e1cbc | 8b49598e1cbc | byte-identical |
| video/beats/beat-02.yaml | 88b8ed7b06ef | 4f712a85a4ba | revised |
| video/beats/beat-03.yaml | 9469c8bf2afa | 9469c8bf2afa | byte-identical |
| video/beats/beat-04.yaml | 4ef486899ec2 | 4ef486899ec2 | byte-identical |
| video/captions.vtt | b037227372c0 | b037227372c0 | byte-identical |
| video/scenes/scene_beat_01.py | bdad46faed35 | bdad46faed35 | byte-identical |
| video/scenes/scene_beat_02.py | 9dfe7d29a306 | 8a3b2932f450 | revised |
| video/scenes/scene_beat_03.py | ccfd69fe68ab | ccfd69fe68ab | byte-identical |
| video/scenes/scene_beat_04.py | 8e2e3bcc1b74 | 8e2e3bcc1b74 | byte-identical |
| script.md#beat-01 (fragment) | 3a9ffed85063 | 3a9ffed85063 | byte-identical |
| script.md#beat-02 (fragment) | 4b817f3b661c | 4b817f3b661c | byte-identical |
| script.md#beat-03 (fragment) | 3dbf70c80cd9 | 3dbf70c80cd9 | byte-identical |
| script.md#beat-04 (fragment) | ac0a8b2a606b | ac0a8b2a606b | byte-identical |
| storyboard.yaml#beat-01 (fragment) | 4aaab0ec0ea7 | 4aaab0ec0ea7 | byte-identical |
| storyboard.yaml#beat-02 (fragment) | 64ae593fdc80 | 501aec93f6fd | revised |
| storyboard.yaml#beat-03 (fragment) | e604cf58ab95 | e604cf58ab95 | byte-identical |
| storyboard.yaml#beat-04 (fragment) | 68f19a35b9d6 | 68f19a35b9d6 | byte-identical |

**29 untouched artifacts byte-identical, 10 revised as ordered, 1 VIOLATIONS.**
