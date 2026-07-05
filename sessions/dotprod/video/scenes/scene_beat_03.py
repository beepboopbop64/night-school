import sys
from pathlib import Path

from manim import *  # noqa: F403

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "shared" / "manim"))
from bbox_dump import attach_bbox_dump  # noqa: E402
from colors import *  # noqa: E402,F403
from style import (  # noqa: E402
    FONT_BODY,
    FONT_HEADING,  # noqa: F401
    FONT_MONO,
    roughen,
    true_up,
    wobble_once,
)

import numpy as np  # noqa: E402


def _still(cx: float, cy: float, probe_angle_deg: float, label_str: str, score_str: str) -> VGroup:
    """One frozen probe reading: fixed candidate + angled probe + label + score."""
    center = np.array([cx, cy, 0.0])
    cand_origin = center + LEFT * 0.15
    probe_origin = center + RIGHT * 0.15

    candidate = Arrow(
        cand_origin,
        cand_origin + UP * 0.8,
        buff=0,
        color=DATA_OBSERVED,
        stroke_width=7,
        tip_length=0.2,
    )
    a = np.radians(probe_angle_deg)
    direction = np.array([np.cos(a), np.sin(a), 0.0])
    probe = Arrow(
        probe_origin,
        probe_origin + direction * 0.8,
        buff=0,
        color=DATA_HEAT,
        stroke_width=7,
        tip_length=0.2,
    )
    label = Text(label_str, font=FONT_BODY, font_size=30, color=TEXT)
    label.move_to(center + UP * 1.4)
    score = Text(score_str, font=FONT_MONO, font_size=30, color=TEXT)
    score.move_to(center + DOWN * 1.4)
    return VGroup(candidate, probe, label, score)


class Beat03(Scene):
    def construct(self):
        attach_bbox_dump(self)
        self.camera.background_color = BG

        # --- three frozen probe stills: along, across, against -------------
        still_along = _still(-4.6, 1.6, 90, "along", "+6.0")
        still_across = _still(0.0, 1.6, 0, "across", "0.0")
        still_against = _still(4.6, 1.6, -90, "against", "-6.0")

        self.play(
            GrowArrow(still_along[0]),
            GrowArrow(still_along[1]),
            FadeIn(still_along[2]),
            FadeIn(still_along[3]),
            run_time=2.2,
        )
        self.wait(0.8)
        self.play(
            GrowArrow(still_across[0]),
            GrowArrow(still_across[1]),
            FadeIn(still_across[2]),
            FadeIn(still_across[3]),
            run_time=2.2,
        )
        self.wait(0.8)
        self.play(
            GrowArrow(still_against[0]),
            GrowArrow(still_against[1]),
            FadeIn(still_against[2]),
            FadeIn(still_against[3]),
            run_time=2.2,
        )
        self.wait(2.5)

        stills_group = VGroup(still_along, still_across, still_against)

        # --- collapse into one lilac meter dial -----------------------------
        pivot = np.array([0.0, 0.3, 0.0])
        radius = 1.5

        arc = Arc(
            radius=radius,
            start_angle=PI,
            angle=-PI,
            arc_center=pivot,
            color=DATA_PARAMS,
            stroke_width=8,
        )
        pivot_dot = Dot(pivot, radius=0.09, color=DATA_PARAMS)

        self.play(FadeOut(stills_group), Create(arc), FadeIn(pivot_dot), run_time=2.0)

        oppose_lbl = Text("oppose", font=FONT_BODY, font_size=26, color=TEXT)
        oppose_lbl.move_to(pivot + LEFT * (radius + 0.55))
        ignore_lbl = Text("ignore", font=FONT_BODY, font_size=26, color=TEXT)
        ignore_lbl.move_to(pivot + UP * (radius + 0.5))
        agree_lbl = Text("agree", font=FONT_BODY, font_size=26, color=TEXT)
        agree_lbl.move_to(pivot + RIGHT * (radius + 0.55))

        self.play(FadeIn(oppose_lbl), FadeIn(ignore_lbl), FadeIn(agree_lbl), run_time=1.6)

        angle_tracker = ValueTracker(180.0)

        def _needle_updater():
            a = np.radians(angle_tracker.get_value())
            tip = pivot + 1.1 * np.array([np.cos(a), np.sin(a), 0.0])
            return Line(pivot, tip, color=DATA_HEAT, stroke_width=9)

        needle = always_redraw(_needle_updater)

        annotation = Text("a · b", font=FONT_MONO, font_size=26, color=DATA_OBSERVED)
        annotation.move_to(np.array([0.0, -1.7, 0.0]))

        def _readout_updater():
            value = 6.0 * np.cos(np.radians(angle_tracker.get_value()))
            t = Text(f"{value:+.1f}", font=FONT_MONO, font_size=32, color=TEXT)
            t.move_to(np.array([0.0, -2.4, 0.0]))
            return t

        readout = always_redraw(_readout_updater)

        self.play(FadeIn(needle), FadeIn(annotation), FadeIn(readout), run_time=1.4)
        self.wait(1.4)

        # --- replay the sweep: oppose -> ignore -> agree --------------------
        self.play(angle_tracker.animate.set_value(90.0), run_time=3.0)
        self.wait(0.8)
        self.play(angle_tracker.animate.set_value(0.0), run_time=3.0)
        needle.clear_updaters()
        readout.clear_updaters()
        self.wait(1.8)

        meter_group = VGroup(
            arc, pivot_dot, oppose_lbl, ignore_lbl, agree_lbl, needle, annotation, readout
        )

        # --- the aha sentence trues up in mint -------------------------------
        sentence = Text(
            "dot product = similarity meter",
            font=FONT_BODY,
            font_size=32,
            color=DATA_FIT,
        )
        if sentence.width > 10.5:
            sentence.scale_to_fit_width(10.5)
        sentence.move_to(np.array([0.0, -3.2, 0.0]))

        underline = Line(
            sentence.get_left() + DOWN * 0.3,
            sentence.get_right() + DOWN * 0.3,
            color=DATA_FIT,
            stroke_width=5,
        )
        roughen(underline)

        self.play(
            meter_group.animate.set_opacity(0.4),
            Write(sentence),
            Create(underline),
            run_time=2.2,
        )
        self.play(wobble_once(underline), run_time=0.35)
        self.play(true_up(underline, glow_color=DATA_FIT))
        self.wait(4.5)
