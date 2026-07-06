# DotAlignment replan

## Why the old layout was replaced

The previous build used a cropped, non-square viewBox (320x230) with the
circle center pushed toward the bottom edge, sized on the assumption that
every arrow stays in the "upper half" (angles 0-180). But the probe slider
covers the full 0-360 range and the anti-aligned and length-cheat states
push the probe and its label into the lower half and toward the edges.
That asymmetric canvas is structurally fragile: any angle whose label
offset reaches toward the cropped edge risks clipping or crowding at some
width. This replan removes the fragility at its root by using a full
square viewBox sized to fit the worst case (c1 stretched to 2x, at any
angle, plus its label) with margin, so no rotation or stretch can ever
approach the edge.

## Structure (all widths, 375 to 1280)

Single column flow, centered, max-width ~520px, fluid below that:

1. One instruction line (text, `--font-body`, low-opacity cream).
2. A square diagram region (`aspect-ratio: 1 / 1`, width 100% up to a cap):
   - An SVG (`viewBox="0 0 400 400"`, center (200,200)) draws, in order:
     a. A faint fixed center dot (decorative, `aria-hidden="true"`).
     b. Four periwinkle candidate arrows (thin stroke, proportional
        arrowhead) at fixed angles 20/70/110/160, unit length except c1
        which uses the live length state. Each carries a tip label (c1..c4)
        drawn as SVG text, `aria-hidden="true"` (the accessible name lives
        on the score readout below, not on this decorative glyph).
     c. One amber probe arrow, same arrowhead proportion function as the
        candidates, fixed magnitude 1, angle from the primary state. Its
        "probe" tip label is `aria-hidden="true"` too, offset both
        radially AND tangentially (perpendicular kick) from the tip so
        that even when the probe sits exactly on a candidate's line (70,
        110 both occur in the driven states) the two label centers stay
        separated by a fixed safe distance, independent of angle.
   - Two absolutely-positioned HTML div handles overlaid on the diagram,
     each a fixed 48x48 CSS pixel box (not scaled with the viewBox, so the
     44px touch-target minimum holds at 375, 768 and 1280 unconditionally):
     - probe handle: `role="slider"`, positioned at the probe's tip,
       amber dot, drag/keys change the angle.
     - c1 length handle: `role="spinbutton"`, `data-control="length-c1"`,
       positioned at c1's tip, periwinkle dot, drag/keys change c1's length
       along c1's fixed direction (projection onto that axis, not raw
       distance from center, so an off-axis drag still tracks length
       intuitively).
   Only the probe handle carries `role="slider"` with no `data-control`
   attribute, so the primary control is unambiguous; the length control is
   `role="spinbutton"` with `data-control="length-c1"`, avoiding a second
   `[role="slider"]` match.
3. A score row below the diagram: four columns (c1..c4, left to right),
   each with:
   - a small vertical bar-track (fixed CSS pixel height) with a hairline
     zero baseline at its vertical center; a lilac fill bar grows up from
     the baseline for positive scores, down for negative, height
     proportional to `min(abs(score), 2) / 2`.
   - a quiet mono numeric readout under the bar, one decimal, lilac,
     lower opacity, `aria-label="c{n} score {value}"`.
   - a small cream candidate-id caption, `aria-hidden="true"` (redundant
     with the readout's aria-label, avoids double narration).
   - the bar (and only the bar/readout, never both together with the
     caption) gets a "leading" boost (full opacity, bold digits) only when
     its rounded score strictly exceeds every other rounded score; on any
     tie for the top rounded value, no column gets the boost.

## Geometry safety margin (fixes the recurring clipping/overlap defect)

- Unit radius R = 70 (user units) for a candidate/probe of length 1.
- c1's length ranges 0.5..2, so its shaft ranges 35..140.
- Arrowhead length/width scale directly off shaft length (ratios 0.2 and
  0.11) for every arrow, probe included, so the head is never bloated
  relative to the shaft regardless of length.
- Label sits at `shaft + 30` radially, plus (for the probe only) a
  tangential kick of 26 units perpendicular to its own direction. Worst
  case reach from center: `140 (max c1 shaft) + 30 (label offset) = 170`.
  Center at (200,200) inside a 400x400 box leaves 200 units to any edge,
  comfortably inside with over 25 units of margin for text width and
  stroke, at every angle, not just the five driven states.
- Because the canvas is square and centered, this margin holds for a full
  0-360 sweep, not only the specific angles the driver happens to visit.

## Interaction

- Primary slider (probe angle): pointer drag on its handle computes the
  angle from the pointer position relative to the SVG's screen center
  (via `getBoundingClientRect`, converted into the 400-unit user space).
  Keyboard: ArrowRight/Up +5, ArrowLeft/Down -5, Home = 0, End = 360,
  clamped to [0, 360].
- Auxiliary control (c1 length): pointer drag projects the pointer vector
  onto c1's fixed direction (dot product with the unit vector at 20
  degrees) to get a signed length, clamped to [0.5, 2]. Keyboard:
  ArrowRight/Up +0.1, ArrowLeft/Down -0.1, Home = 0.5, End = 2.
- Both handles set pointer capture on pointerdown and listen on the
  handle itself for move/up (no window listeners), matching the pointer
  event contract.

## Reduced motion

Bar height/opacity transitions are wrapped in a normal transition; a
`@media (prefers-reduced-motion: reduce)` block sets that transition to
`none`. The value-driven geometry (arrow angle, bar height, handle
position) is never itself animated/delayed, only the optional smoothing
transition is removed.
