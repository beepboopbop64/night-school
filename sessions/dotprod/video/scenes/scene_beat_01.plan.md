# Beat 01 replan — "The score behind the song"

## Root cause of the repeated defect

`bbox.text-height` failed twice on the same offending mobject: a bare
ellipsis glyph `"…"` used as the fifth ("trailing off") row label in both
feature stacks. The `…` glyph is a short horizontal mark near the baseline —
its rendered bounding box is far shorter than a normal word even at
`font_size=32`, so it measured 0.067 scene units tall against the 0.176
minimum. Scaling the font size to fix it would blow up the row spacing and
break other checks. The character itself is structurally incapable of
passing the height check.

**Structural fix**: never use an ellipsis (or any punctuation-only glyph) as
a standalone `Text` mobject. The "trailing off" cue is carried by fading
opacity and word content, not by a bare `…` character. Every `Text` in this
scene must contain at least one normal lowercase word so its glyph height is
governed by ascenders/x-height, not by punctuation.

## Layout (frame is 14.2 x 8, origin centered)

- Two column headers, `TEXT` color, `FONT_HEADING`, size 34:
  - "LISTENER" at (-4.5, 3.3)
  - "SONG" at (4.5, 3.3)
- Five paired feature rows, `DATA_OBSERVED` color, `FONT_BODY`, size 32,
  vertically stacked at y = 2.5, 1.7, 0.9, 0.1, -0.7 (0.8 unit pitch, well
  clear of the ~0.4-unit text height so no row ever collides with its
  neighbor):
  - row words: "loud", "fast", "sad", "bright", "more"
  - each row is a real word (no bare punctuation) so its glyph height
    passes the readability floor regardless of content
  - the fifth row ("more") renders at opacity 0.5 on both sides — this is
    the "trailing off the frame" cue: last item fades, it does not shrink
    to an unreadable glyph
- A lilac (`DATA_PARAMS`) match-readout card: `RoundedRectangle` centered at
  (0, -2.35), width 3.0, height 1.3 — sits in the lower third, well below
  the last feature row (-0.7) with a 1.15-unit gap for the converging
  arrows, and well inside the frame (bottom edge at -3.0, frame half-height
  is 4.0, so it clears the 15%-off-frame margin).
- Two arrows (`DATA_OBSERVED`) from each column's last-row height into the
  card's top corners — visually funnels "listener" and "song" into one
  comparison point.
- A single `"?"` in `FONT_MONO`, size 72, `DATA_PARAMS`, centered in the
  card — the unfilled readout. `?` is a full-height glyph (tall ascender +
  dot), so it clears the height floor with a wide margin.

## Staging order (one play() at a time, <=4 new mobjects each)

1. `FadeIn` both headers together (2 new mobjects).
2. For each of the 5 rows: `FadeIn` the left+right label pair together
   (2 new mobjects per play, 5 plays total) — builds the two lists in
   reasoning order, top to bottom.
3. `Create` both arrows together (2 new mobjects).
4. `Create` the rounded-rect card (1 new mobject).
5. `FadeIn` the `?` readout (1 new mobject).
6. Focus pull: dim both list groups + arrows to 40% opacity, thicken the
   card stroke — no new mobjects, pure emphasis shift onto the readout.
7. Two `Indicate` pulses on the `?` while holding — no new mobjects, this
   is the "hold the question" beat that owns the back half of the runtime.

Total run_time + wait sum target: ~24.4s (headers 1.8s, rows 6.2s, arrows
1.4s, card 1.7s, qmark 1.0s, focus pull 3.0s, two indicates with holds
4.0s + 5.3s = 24.4s).

## Why the defect cannot recur

No `Text` mobject in this plan contains only punctuation. Every label is a
lowercase English word, "?", or an all-caps header word — all of which have
ascender/x-height/cap-height geometry well above the 0.176-unit floor at
size >=32 (headers at 34, `?` at 72). The "trailing off" narrative beat is
carried entirely by opacity (0.5) on a real word, never by glyph choice.
