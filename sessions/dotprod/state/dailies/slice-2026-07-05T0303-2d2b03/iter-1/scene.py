import sys
from pathlib import Path

from manim import *  # noqa: F403

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "shared" / "manim"))
from bbox_dump import attach_bbox_dump  # noqa: E402
from colors import *  # noqa: E402,F403
from style import FONT_BODY, FONT_HEADING, FONT_MONO  # noqa: E402

import numpy as np  # noqa: E402

# ---------------------------------------------------------------------------
# Geometry: probe + four candidates share one origin. Candidate directions
# fan across the upper half-plane; the probe is deliberately SHORTER than
# every candidate so its sweeping tip can never physically reach (and bury)
# a tip label, at any angle.
# ---------------------------------------------------------------------------

ORIGIN = np.array([0.0, 0.9, 0.0])
PROBE_LEN = 1.7
BASELINE_Y = -2.0
SCALE = 0.3
TICK_HALF = 0.3
LABEL_OFFSET_X = -0.9
READOUT_OFFSET = 0.3
BAR_WIDTH = 0.7

CANDIDATES = [
    {"key": "A", "angle": 15.0, "length": 2.3, "x": 4.5},
    {"key": "B", "angle": 62.0, "length": 2.6, "x": 1.5},
    {"key": "C", "angle": 108.0, "length": 2.4, "x": -1.5},
    {"key": "D", "angle": 155.0, "length": 2.1, "x": -4.5},
]

for _c in CANDIDATES:
    _rad = np.deg2rad(_c["angle"])
    _c["dx"] = _c["length"] * np.cos(_rad)
    _c["dy"] = _c["length"] * np.sin(_rad)


def probe_point(theta: float) -> np.ndarray:
    return ORIGIN + np.array([PROBE_LEN * np.cos(theta), PROBE_LEN * np.sin(theta), 0.0])


def candidate_tip(c: dict) -> np.ndarray:
    return ORIGIN + np.array([c["dx"], c["dy"], 0.0])


def score_of(theta: float, c: dict) -> float:
    px = PROBE_LEN * np.cos(theta)
    py = PROBE_LEN * np.sin(theta)
    return px * c["dx"] + py * c["dy"]


class Beat02(Scene):
    def construct(self):
        attach_bbox_dump(self)
        self.camera.background_color = BG

        theta = ValueTracker(np.deg2rad(90.0))

        # --- shared origin marker ---
        origin_dot = Dot(ORIGIN, radius=0.06, color=TEXT)
        self.play(FadeIn(origin_dot), run_time=0.5)

        # --- candidate arrows + tip labels, built two at a time ---
        cand_arrows = {}
        cand_labels = {}
        for c in CANDIDATES:
            tip = candidate_tip(c)
            arrow = Arrow(
                ORIGIN, tip, buff=0, color=DATA_OBSERVED,
                stroke_width=6, max_tip_length_to_length_ratio=0.18,
            )
            unit = tip - ORIGIN
            unit = unit / np.linalg.norm(unit)
            label = Text(c["key"], font=FONT_BODY, color=TEXT, font_size=32)
            label.move_to(tip + unit * 0.55)
            cand_arrows[c["key"]] = arrow
            cand_labels[c["key"]] = label

        self.play(
            Create(cand_arrows["A"]), Write(cand_labels["A"]),
            Create(cand_arrows["B"]), Write(cand_labels["B"]),
            run_time=2.0,
        )
        self.play(
            Create(cand_arrows["C"]), Write(cand_labels["C"]),
            Create(cand_arrows["D"]), Write(cand_labels["D"]),
            run_time=2.0,
        )

        # --- probe arrow ---
        probe_arrow = Arrow(
            ORIGIN, probe_point(theta.get_value()), buff=0, color=DATA_HEAT,
            stroke_width=9, max_tip_length_to_length_ratio=0.16,
        )
        self.play(GrowArrow(probe_arrow), run_time=1.5)

        def update_probe(m):
            m.become(
                Arrow(
                    ORIGIN, probe_point(theta.get_value()), buff=0, color=DATA_HEAT,
                    stroke_width=9, max_tip_length_to_length_ratio=0.16,
                )
            )

        probe_arrow.add_updater(update_probe)

        # candidates recede so the moving probe reads as the one signaled
        # element; their tip labels stay at full opacity, always legible.
        cand_arrow_group = VGroup(*cand_arrows.values())
        self.play(cand_arrow_group.animate.set_opacity(0.5), run_time=1.0)

        self.wait(2.0)

        # --- prediction freeze card (before anything moves) ---
        title = Text("PREDICT", font=FONT_HEADING, color=TEXT, font_size=36)
        title.move_to(np.array([0.0, -1.0, 0.0]))
        self.play(Write(title), run_time=1.0)

        predict_texts = {}
        for c in CANDIDATES:
            t = Text(f"{c['key']}: ?", font=FONT_BODY, color=TEXT, font_size=28)
            t.move_to(np.array([c["x"], BASELINE_Y, 0.0]))
            predict_texts[c["key"]] = t

        self.play(
            Write(predict_texts["A"]), Write(predict_texts["B"]),
            Write(predict_texts["C"]), Write(predict_texts["D"]),
            run_time=1.5,
        )

        self.wait(3.0)

        predict_group = VGroup(title, *predict_texts.values())
        self.play(FadeOut(predict_group), run_time=1.0)

        # --- bar scaffolding: baselines, letters, bars, readouts ---
        baselines = {}
        for c in CANDIDATES:
            x = c["x"]
            line = Line(
                np.array([x - TICK_HALF, BASELINE_Y, 0.0]),
                np.array([x + TICK_HALF, BASELINE_Y, 0.0]),
                color=TEXT, stroke_width=3,
            )
            baselines[c["key"]] = line
        self.play(
            Create(baselines["A"]), Create(baselines["B"]),
            Create(baselines["C"]), Create(baselines["D"]),
            run_time=1.0,
        )

        bottom_labels = {}
        for c in CANDIDATES:
            lab = Text(c["key"], font=FONT_BODY, color=TEXT, font_size=28)
            lab.move_to(np.array([c["x"] + LABEL_OFFSET_X, BASELINE_Y, 0.0]))
            bottom_labels[c["key"]] = lab
        self.play(
            Write(bottom_labels["A"]), Write(bottom_labels["B"]),
            Write(bottom_labels["C"]), Write(bottom_labels["D"]),
            run_time=1.0,
        )

        def make_bar_fn(c):
            def bar_shape():
                s = score_of(theta.get_value(), c)
                h = s * SCALE
                height = max(abs(h), 0.02)
                bar = Rectangle(
                    width=BAR_WIDTH, height=height,
                    color=DATA_PARAMS, fill_color=DATA_PARAMS,
                    fill_opacity=0.85, stroke_width=0,
                )
                bar.move_to(np.array([c["x"], BASELINE_Y + h / 2.0, 0.0]))
                return bar
            return bar_shape

        bar_fns = {c["key"]: make_bar_fn(c) for c in CANDIDATES}
        bars = {k: fn() for k, fn in bar_fns.items()}
        self.play(
            FadeIn(bars["A"]), FadeIn(bars["B"]),
            FadeIn(bars["C"]), FadeIn(bars["D"]),
            run_time=1.0,
        )
        for k, fn in bar_fns.items():
            bars[k].add_updater(lambda m, fn=fn: m.become(fn()))

        def make_readout_fn(c):
            def text_shape():
                s = score_of(theta.get_value(), c)
                h = s * SCALE
                sign = 1.0 if h >= 0 else -1.0
                y = BASELINE_Y + h + sign * READOUT_OFFSET
                t = Text(f"{round(s):d}", font=FONT_MONO, color=DATA_PARAMS, font_size=30)
                t.move_to(np.array([c["x"], y, 0.0]))
                return t
            return text_shape

        readout_fns = {c["key"]: make_readout_fn(c) for c in CANDIDATES}
        readouts = {k: fn() for k, fn in readout_fns.items()}
        self.play(
            Write(readouts["A"]), Write(readouts["B"]),
            Write(readouts["C"]), Write(readouts["D"]),
            run_time=1.0,
        )
        for k, fn in readout_fns.items():
            readouts[k].add_updater(lambda m, fn=fn: m.become(fn()))

        self.wait(0.5)

        # --- turn the probe and watch the bars answer ---
        self.play(theta.animate.set_value(np.deg2rad(15.0)), run_time=2.0, rate_func=linear)
        self.wait(1.5)
        self.play(theta.animate.set_value(np.deg2rad(165.0)), run_time=8.0, rate_func=linear)
        self.wait(1.0)

        # point straight at candidate B, then turn away from it
        self.play(theta.animate.set_value(np.deg2rad(62.0)), run_time=2.5, rate_func=smooth)
        self.wait(1.5)
        self.play(theta.animate.set_value(np.deg2rad(130.0)), run_time=2.0, rate_func=smooth)

        self.wait(4.5)
