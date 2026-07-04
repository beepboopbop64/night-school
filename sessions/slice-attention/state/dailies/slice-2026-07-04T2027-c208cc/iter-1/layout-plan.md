# Layout plan: qk-similarity (fresh replan)

## Root cause of prior crash
Iteration 2 drove the sweep with
`UpdateFromAlphaFunc(query_angle, ...)` where `query_angle` (a `ValueTracker`)
was passed as the *animated mobject*. Manim's animation machinery tries to
generically match starting/target mobject style attributes (`fill_opacity`
etc.) on the two internal copies it makes of the animated mobject, and
`ValueTracker` does not carry those style attributes -> `AttributeError`.

**Structural fix**: never wrap a `ValueTracker` in `UpdateFromAlphaFunc`.
Drive the sweep with the standard, safe idiom `tracker.animate.set_value(x)`
(the built-in `ValueTracker.interpolate` override handles this correctly).
All other mobjects (arrow, keys, bars, readouts) stay driven by
`add_updater` closures that read `query_angle.get_value()` every frame -
this part already worked and is kept.

## Elements & regions (frame is 14.2 x 8, origin centered)

- **Query** (color `DATA_HEAT`, single focus, in motion):
  - Pivot/base: `(0, 2.4)`, fixed anchor point (never moves).
  - Arrow radius 0.9, direction angle driven by `query_angle` (ValueTracker).
  - Sweep range: 20 deg -> 160 deg through stops `[20, 60, 90, 120, 160]`
    (4 segments x 4.0s = 16s of continuous rotation).
  - At these angles the tip/label stay within y in [2.4, 3.95] and
    x in [-0.85, 0.85] - well inside the frame (edges at +/-4 y, +/-7.1 x).
  - Label "q" (color `TEXT`) sits 0.35 units beyond the tip, on the same
    radial direction - always ON the arrow, never a legend.

- **Keys** (color `DATA_OBSERVED`, held row, recede when not peaking):
  - Row of 4 short arrows, base y = -0.3, length 0.9.
  - Base x positions: -4.5, -1.5, 1.5, 4.5 (spacing 3, well inside +/-7.1).
  - Fixed directions (deg): 20, 65, 115, 160 - spread across the query's
    sweep range so each key gets its own moment of peak alignment as the
    query passes near its angle, left to right in sequence.
  - Tips/labels stay within y in [-0.3, 0.83] - a clear empty band (>1.8
    units) separates this zone from the query zone above.
  - Label `k1`..`k4` (color `TEXT`) sits 0.35 beyond each tip, on-object.
  - Opacity of arrow + label pulses with that key's live score (dim ~35%
    when unaligned, full brightness when aligned) - this dimming IS the
    covariation signal, not a focus trick.

- **Score bars + readouts** (color `DATA_PARAMS`):
  - One bar per key, same x as its key, growing upward from baseline
    y = -3.6, max height 1.8 (top never exceeds y = -1.8).
  - Numeric readout (`+0.87` style, `FONT_MONO`) centered at y = -1.15,
    same x as its key/bar - sits in the empty band between the key row
    (bottom -0.3) and the bar tops (-1.8), gap >= 0.5 units both sides.
  - Bar height and fill opacity both track `(score+1)/2` live, so a bar's
    rise/fall is simultaneous with its key's brightness pulse and with the
    query's rotation - the single continuous covariation chain the beat
    needs.

## Staging order (play-by-play, novelty budget <= 4 new mobjects each)

1. `Create(query_arrow)` + `Write(query_label)` -> 2 new mobjects.
2. `Create(key_arrow[0..1])` + `Write(key_label[0..1])` -> 4 new mobjects.
3. `Create(key_arrow[2..3])` + `Write(key_label[2..3])` -> 4 new mobjects.
4. `Create(bar[0..1])` + `Write(readout[0..1])` -> 4 new mobjects.
5. `Create(bar[2..3])` + `Write(readout[2..3])` -> 4 new mobjects.
6. Four `self.play(query_angle.animate.set_value(stop), run_time=4.0,
   rate_func=linear)` calls sweeping through the angle stops - 0 new
   mobjects each; all motion/covariation happens via updaters already
   attached in steps 1-5.
7. Final `self.wait(2.6)` settles on the last frame.

Total run time ~= 1.0 + 1.2 + 1.2 + 1.0 + 1.0 + 4*4.0 + 2.6 = 24.0s.

## Why the repeated defect is now structurally impossible
The only `ValueTracker` in the scene (`query_angle`) is exclusively driven
by `.animate.set_value(...)`, Manim's documented, style-attribute-free path
for tweening a tracker's scalar. No `Animation` subclass is ever constructed
with the tracker as its target mobject in any other way, so the
`fill_opacity`-on-`ValueTracker` code path cannot be reached again.
