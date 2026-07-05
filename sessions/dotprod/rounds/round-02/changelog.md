# Changelog: dotprod, round-02

Round total: $11.68 (triage $0.28). 3 change orders executed, 0 failed, 0 answered inline, 0 deferred, 3 style amendments drafted, 3 critic-miss entries logged.

## r02-n01 — APPLIED

**Note (n01, verbatim):** Jake: we jump around in our example. We go from songs to resumes and it feels confusing. Keep the two-instances teaching but bridge the switch so it reads as the same meter deliberately visiting a new aisle, not a topic change. Applies to the doc too.

Jake: the walk-home line reads out of place at the close. Rework the phrasing of the cheapest-fix question so it lands naturally instead of feeling bolted on.

**Interpretation:** Add an explicit bridge when the example moves from songs to resumes so it reads as the same meter visiting a new aisle (not a topic change), mirror the bridge in the doc, and rework the walk-home / cheapest-fix prediction question so it lands naturally at the close instead of feeling bolted on.
**Confidence:** high
**Critic miss:** vera should have caught this (script/beat-04).

**What changed:** doc/lesson.md, page/sections/beat-04.md, script.md, script.md#beat-04 — Bridged the songs-to-resumes switch as the same meter deliberately visiting a new aisle in script, page, and doc, and reworked the cheapest-fix walk-home question so it lands naturally at the close.

**Re-run verdicts (fresh caps):**

| node | gate | checks | cost |
|---|---|---|---|
| s4f.beat-04 | pass | tts.safe-lint:pass, tts.audio-written:pass | $0.00 |
| s4a.beat-04 | pass | bbox.clean:pass, iris.pass:pass, scene.duration-within-tolerance:pass | $1.37 |
| s4c.doc | pass | doc.dash-lint:pass, doc.aha-verbatim:pass, doc.no-handwave:pass, doc.vera-pass:pass | $0.93 |
| s4e.notebook | pass | nb.json:pass, nb.numpy-only:pass, nb.executes:pass | $0.41 |
| s5.assemble | pass | assemble.av-drift:pass, assemble.captions-written:pass, assemble.aha-consistency:pass, assemble.lchecks-rerun:pass, assemble.token-lint:pass, assemble.site-built:pass, assemble.manifest-complete:pass | $0.00 |
| s6.screening | pass | screening.sam-probes:pass, screening.petra:pass, screening.vera-opus:pass, screening.iris-continuity:pass, screening.rounds-within-cap:pass | $0.92 |
| s7.packet | pass | packet.serves-locally:pass, packet.notes-preseeded:pass, packet.flags-written:pass | $0.00 |

**Cost:** $3.87 (apply $0.23 + attributed re-runs)

## r02-n02 — APPLIED

**Note (n02, verbatim):** Jake: this looks really unprofessional. I kind of get what it's trying to say but it just looks sloppy. The amber probe arrowhead is huge and malformed, the "probe 90" label collides with the candidate arrows, and the whole thing reads rough. Make it precise and clean per the brand: thin exact strokes, labels that never collide, arrowheads proportional.

Jake: the interactive never shows magnitude mattering or not. Tie it to the story: let me change a candidate's length as well as the probe's direction so I can FEEL that direction moves the score and length cheats it. That is the session's whole second conflict and the interactive ignores it.

Jake: "Before you drag anything, call it:" does not make sense here. Call what? I am dragging a visual arrow wherever I want and the bars just follow. If there is a prediction ask, make it concrete (say which candidate will top out before you touch the probe) and make it fit an interactive where dragging is the point. Rework this phrasing wherever it appears in the session.

**Interpretation:** Rebuild the dot-alignment interactive to brand spec (thin exact strokes, proportional arrowhead on the amber probe, labels like 'probe 90' that never collide with candidate arrows); add a candidate-length control alongside probe direction so the learner feels direction move the score while length cheats it (the session's second conflict); and replace the vague 'call it' / 'Before you drag anything, call it:' prompt with a concrete prediction ask (name which candidate tops out before touching the probe), fixing this phrasing wherever it appears.
**Alternative considered (recorded because the note is ambiguous):** Treat only the visual cleanup and prompt rewording as in-scope and defer the length-control feature as a larger interactive rebuild.
**Confidence:** medium
**Critic miss:** iris should have caught this (ix/dot-alignment).

**What changed:** page/interactives/dot-alignment.yaml, storyboard.yaml, storyboard.yaml#beat-02 — Rebuilt dot-alignment to brand spec (thin strokes, proportional probe arrowhead, non-colliding labels), added a c1 length control so learners feel direction earn the score while length cheats it (session's second conflict), and replaced the vague 'call it' prompt with a concrete 'name which candidate tops out' prediction in beat-02 and the interactive.

**Re-run verdicts (fresh caps):**

| node | gate | checks | cost |
|---|---|---|---|
| s4a.beat-02 | pass | bbox.clean:pass, iris.pass:pass, scene.duration-within-tolerance:pass | $1.85 |
| s4b.sec-beat-02 | pass | section.nonempty:pass, section.heading:pass, section.dash-lint:pass, section.aha-verbatim:pass | $0.05 |
| s4b.dot-alignment | pass | weba11y.clean:pass, iris.pass:pass | $2.16 |
| s4d.extensions | pass | ext.schema:pass, ext.source-whitelist:pass, ext.dash-lint:pass, ext.links-resolve:pass | $0.12 |

**Cost:** $4.53 (apply $0.35 + attributed re-runs)

## r02-n03 — APPLIED

**Note (n03, verbatim):** @spine Jake: we don't build up why this matters. We just say "we compare two numbered lists" which makes it seem trivial and we get right to "this works" without going through a challenge. Build the problem first, 3b1b style: comparing things with many features is genuinely hard, pose it as a puzzle the reader actually tries to solve before we hand them the mechanism, and let the dot product arrive as the resolution. Maybe a light touch of why many features make comparison painful (full curse-of-dimensionality treatment is probably too much, use judgment). The aha should feel earned, not announced.

**Interpretation:** SPINE-LEVEL, pauses the round for sign-off: restructure the opening so the difficulty of comparing many-featured things is posed as a puzzle the reader actually attempts before the dot product is handed over as the resolution (light, judgment-limited touch on why many features make comparison painful), so the aha feels earned rather than announced.
**Confidence:** high · **SPINE TOUCH**
**Critic miss:** petra should have caught this (spine.md).

**What changed:** spine.md, storyboard.yaml, storyboard.yaml#beat-01, storyboard.yaml#beat-02 — Restructured the opening so beat-01 poses the many-feature comparison as a puzzle the learner attempts and beat-02 hands the dot product over as its resolution; updated the spine beat table intents and timing (154s total) to match, aha unchanged.

**Re-run verdicts (fresh caps):**

| node | gate | checks | cost |
|---|---|---|---|
| s4a.beat-01 | pass | bbox.clean:pass, iris.pass:pass, scene.duration-within-tolerance:pass | $0.85 |
| s4b.sec-beat-01 | pass | section.nonempty:pass, section.heading:pass, section.dash-lint:pass, section.aha-verbatim:pass | $0.05 |

**Cost:** $1.44 (apply $0.54 + attributed re-runs)

## r02-n04 — STYLE-AMENDMENT

**Note (n04, verbatim):** #style: pose the puzzle before the mechanism. Every session builds the problem until the reader has genuinely tried it, then the answer lands as a resolution. Never open with "here is the trick."

**Interpretation:** Draft a bible rule requiring every session to pose the problem as a puzzle the reader has genuinely tried before revealing the mechanism, with the answer arriving as a resolution and never opening with 'here is the trick.'
**Confidence:** high

**Drafted show-bible amendment** (show-bible/voice/proposed-amendments.md, awaiting Jake's ratification): Pose the problem as a puzzle the reader has genuinely tried before revealing the mechanism, and let the answer arrive as a resolution; never open with 'here is the trick.'

## r02-n05 — STYLE-AMENDMENT

**Note (n05, verbatim):** #style: prediction prompts must be concrete asks the learner can actually answer ("say which candidate tops out"), never vague imperatives like "call it."

**Interpretation:** Draft a bible rule requiring every prediction prompt to be a concrete ask the learner can actually answer (e.g. 'say which candidate tops out'), never a vague imperative like 'call it.'
**Confidence:** high

**Drafted show-bible amendment** (show-bible/voice/proposed-amendments.md, awaiting Jake's ratification): Write every prediction prompt as a concrete ask the learner can actually answer (e.g. 'say which candidate tops out'), never a vague imperative like 'call it.'

## r02-n06 — STYLE-AMENDMENT

**Note (n06, verbatim):** #style: never switch analogy domains mid-session without an explicit bridge sentence naming that it is the same structure in a new setting.

**Interpretation:** Draft a bible rule forbidding any mid-session analogy-domain switch that lacks an explicit bridge sentence naming that it is the same structure in a new setting.
**Confidence:** high

**Drafted show-bible amendment** (show-bible/voice/proposed-amendments.md, awaiting Jake's ratification): Never switch analogy domains mid-session without an explicit bridge sentence naming that it is the same structure in a new setting.

## Dirty set & estimates (as planned)

| order | targets | dirty nodes (first-attributed cost) | est. |
|---|---|---|---|
| r02-n01 | script#beat-04, page/beat-04, doc | s4f.beat-04 ($0.01), s4a.beat-04 ($1.34), s4c.doc ($0.33), s4e.notebook ($0.26), s5.assemble ($0.00), s6.screening ($1.13), s7.packet ($0.00) | $3.86 |
| r02-n02 | ix/dot-alignment, storyboard#beat-02 | s4a.beat-02 ($1.21), s4b.sec-beat-02 ($0.05), s4b.dot-alignment ($1.15), s4c.doc (–), s4d.extensions ($0.11), s4e.notebook (–), s5.assemble (–), s6.screening (–), s7.packet (–) | $3.31 |
| r02-n03 | spine, storyboard#beat-01, storyboard#beat-02 | s4a.beat-01 ($0.57), s4a.beat-02 (–), s4b.sec-beat-01 ($0.03), s4b.sec-beat-02 (–), s4c.doc (–), s4d.extensions (–), s4e.notebook (–), s5.assemble (–), s6.screening (–), s7.packet (–) | $1.40 |

## Hash-preservation proof (§7.5)

Untouched artifacts are proven byte-identical: `before` is the sha256 the
pre-round receipts recorded, `after` is the artifact re-hashed after the
round. Rows marked `(fragment)` prove per-beat isolation inside
storyboard.yaml/script.md via canonical fragment hashes; the merge module
additionally refuses any splice that alters untouched beats.

| artifact | before | after | status |
|---|---|---|---|
| doc/lesson.md | 4804b0736ab0 | 38120d6551fa | revised |
| extensions.yaml | e0b0ffcda9c1 | f15618c10169 | revised |
| manifest.yaml | 3fa6c804e76a | 3fa6c804e76a | byte-identical |
| media/beat-01.mp4 | c6578f7b293d | 6600dc697c24 | revised |
| media/beat-02.mp4 | 2c9af7927dc9 | 3537ccba6d39 | revised |
| media/beat-03.mp4 | 323a9e2bbaa7 | 1dc29a29d6ab | revised |
| media/session.mp4 | 9f9929bc45b2 | 55b46f7483b3 | revised |
| notebook/lesson.ipynb | 460ad1ceb72d | 8a093a3a9c83 | revised |
| page/interactives/DotAlignment.svelte | 95621fe8e206 | de8adbccfbd8 | revised |
| page/sections/beat-01.md | 704621587b2f | 40436205c398 | revised |
| page/sections/beat-02.md | 18861f739876 | ab8d802ee89a | revised |
| page/sections/beat-03.md | e6b35d9b0ebe | e6b35d9b0ebe | byte-identical |
| page/sections/beat-04.md | 3711c2cb6f89 | f8b5f37c1539 | revised |
| page/video.json | c83c31183255 | 35e578bbc0f3 | revised |
| rounds/round-02/flags.md | 9236fccd1e72 | 9236fccd1e72 | byte-identical |
| rounds/round-02/notes.md | fd01ee11cead | 81e16e775291 | revised |
| rounds/round-02/packet/README.md | 1ded5232b9b9 | 1ded5232b9b9 | byte-identical |
| rounds/round-02/screening-report.md | f81f7f369c6a | f81f7f369c6a | byte-identical |
| video/audio/beat-01.mp3 | c2e113c8269d | 35eea7a82b36 | revised |
| video/audio/beat-02.mp3 | 6e4f70ac1645 | ef5c80d0882d | revised |
| video/audio/beat-03.mp3 | 33d5747c04c6 | 5b4da1b214e9 | revised |
| video/audio/beat-04.mp3 | 0fed1ad1ffb6 | 84183fe2fa68 | revised |
| video/beats/beat-01.yaml | 8b49598e1cbc | 1e531d5522a4 | revised |
| video/beats/beat-02.yaml | 4f712a85a4ba | 44b23badca5b | revised |
| video/beats/beat-03.yaml | 9469c8bf2afa | 6f73ae343ccd | revised |
| video/captions.vtt | b037227372c0 | ac06c839567d | revised |
| video/scenes/scene_beat_01.py | bdad46faed35 | 1825786ec58d | revised |
| video/scenes/scene_beat_02.py | 8a3b2932f450 | f72cdb78b56c | revised |
| video/scenes/scene_beat_03.py | ccfd69fe68ab | 0809a87bacbd | revised |
| video/scenes/scene_beat_04.py | 6deee86ee309 | 0620c7ca1a58 | revised |
| script.md#beat-01 (fragment) | 3a9ffed85063 | 3a9ffed85063 | byte-identical |
| script.md#beat-02 (fragment) | 4b817f3b661c | 4b817f3b661c | byte-identical |
| script.md#beat-03 (fragment) | 3dbf70c80cd9 | 3dbf70c80cd9 | byte-identical |
| script.md#beat-04 (fragment) | c349c0c69586 | 4e3f969f8849 | revised |
| storyboard.yaml#beat-01 (fragment) | 4aaab0ec0ea7 | f511152447e9 | revised |
| storyboard.yaml#beat-02 (fragment) | 501aec93f6fd | 73f262919de1 | revised |
| storyboard.yaml#beat-03 (fragment) | e604cf58ab95 | e604cf58ab95 | byte-identical |
| storyboard.yaml#beat-04 (fragment) | ded0f775f295 | ded0f775f295 | byte-identical |

**10 untouched artifacts byte-identical, 28 revised as ordered, zero violations.**
