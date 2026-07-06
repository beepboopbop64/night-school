import sys
from pathlib import Path

from manim import *  # noqa: F403

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "shared" / "manim"))
from bbox_dump import attach_bbox_dump  # noqa: E402
from colors import *  # noqa: E402,F403
from style import FONT_BODY, FONT_HEADING, FONT_MONO  # noqa: E402
from style import roughen, true_up, wobble_once  # noqa: E402

import numpy as np  # noqa: E402


class Beat03(Scene):
    def construct(self):
        attach_bbox_dump(self)
        self.camera.background_color = BG

        # ------------------------------------------------------------
        # Part 1: the three probe positions replay as frozen stills.
        # ------------------------------------------------------------
        still_y = 2.6
        centers = [-4.3, 0.0, 4.3]
        angles = [0.0, PI / 2, PI]
        scores = [10.0, 0.0, -10.0]

        def make_still(cx: float, angle: float, score: float) -> VGroup:
            origin = np.array([cx, still_y, 0.0])
            candidate = Arrow(
                origin,
                origin + np.array([0.9, 0.0, 0.0]),
                buff=0,
                color=DATA_OBSERVED,
                stroke_width=6,
            )
            probe = Arrow(
                origin,
                origin + 0.9 * np.array([np.cos(angle), np.sin(angle), 0.0]),
                buff=0,
                color=DATA_HEAT,
                stroke_width=6,
            )
            score_text = Text(
                f"{score:.2f}", font=FONT_MONO, color=TEXT, font_size=32
            ).move_to([cx, still_y - 1.3, 0.0])
            return VGroup(candidate, probe, score_text)

        still1 = make_still(centers[0], angles[0], scores[0])
        still2 = make_still(centers[1], angles[1], scores[1])
        still3 = make_still(centers[2], angles[2], scores[2])

        self.play(Create(still1[0]), Create(still1[1]), Write(still1[2]), run_time=1.1)
        self.wait(1.3)

        self.play(
            still1.animate.set_opacity(0.4),
            Create(still2[0]),
            Create(still2[1]),
            Write(still2[2]),
            run_time=1.1,
        )
        self.wait(1.3)

        self.play(
            still2.animate.set_opacity(0.4),
            Create(still3[0]),
            Create(still3[1]),
            Write(still3[2]),
            run_time=1.1,
        )
        self.wait(1.7)

        self.play(FadeOut(VGroup(still1, still2, still3)), run_time=0.9)
        self.wait(0.4)

        # ------------------------------------------------------------
        # Part 2: the stills collapse into one lilac meter dial.
        # ------------------------------------------------------------
        dial_center = np.array([0.0, 1.2, 0.0])
        radius = 1.6

        arc = Arc(
            radius=radius,
            start_angle=PI,
            angle=-PI,
            arc_center=dial_center,
            color=DATA_PARAMS,
            stroke_width=10,
        )

        angle_tracker = ValueTracker(PI)
        dial_opacity = ValueTracker(1.0)

        def make_needle() -> VGroup:
            ang = angle_tracker.get_value()
            tip = dial_center + radius * 0.9 * np.array(
                [np.cos(ang), np.sin(ang), 0.0]
            )
            grp = VGroup(
                Line(dial_center, tip, color=DATA_PARAMS, stroke_width=10),
                Dot(dial_center, color=DATA_PARAMS, radius=0.09),
            )
            grp.set_opacity(dial_opacity.get_value())
            return grp

        needle = always_redraw(make_needle)

        label_r = radius + 0.7
        oppose_label = Text(
            "oppose", font=FONT_BODY, color=TEXT, font_size=30
        ).move_to(dial_center + label_r * np.array([np.cos(PI), np.sin(PI), 0.0]))
        ignore_label = Text(
            "ignore", font=FONT_BODY, color=TEXT, font_size=30
        ).move_to(
            dial_center + label_r * np.array([np.cos(PI / 2), np.sin(PI / 2), 0.0])
        )
        agree_label = Text(
            "agree", font=FONT_BODY, color=TEXT, font_size=30
        ).move_to(dial_center + label_r * np.array([np.cos(0.0), np.sin(0.0), 0.0]))

        self.play(Create(arc), Create(needle), run_time=1.1)
        self.wait(0.7)

        self.play(
            Write(oppose_label), Write(ignore_label), Write(agree_label), run_time=1.1
        )
        self.wait(0.7)

        mini_origin = np.array([0.0, -1.6, 0.0])
        candidate_mini = Arrow(
            mini_origin,
            mini_origin + np.array([1.0, 0.0, 0.0]),
            buff=0,
            color=DATA_OBSERVED,
            stroke_width=6,
        )

        def make_probe_mini() -> Arrow:
            ang = angle_tracker.get_value()
            a = Arrow(
                mini_origin,
                mini_origin + 1.0 * np.array([np.cos(ang), np.sin(ang), 0.0]),
                buff=0,
                color=DATA_HEAT,
                stroke_width=6,
            )
            a.set_opacity(dial_opacity.get_value())
            return a

        probe_mini = always_redraw(make_probe_mini)

        def make_readout() -> Text:
            ang = angle_tracker.get_value()
            t = Text(
                f"{10 * np.cos(ang):.2f}", font=FONT_MONO, color=TEXT, font_size=36
            ).move_to([0.0, -2.8, 0.0])
            t.set_opacity(dial_opacity.get_value())
            return t

        readout = always_redraw(make_readout)

        self.play(
            Create(candidate_mini), Create(probe_mini), Write(readout), run_time=1.1
        )
        self.wait(0.7)

        # The probe sweep replays: oppose -> ignore -> agree.
        self.play(angle_tracker.animate.set_value(PI / 2), run_time=2.2)
        self.wait(0.6)
        self.play(angle_tracker.animate.set_value(0.0), run_time=2.2)
        self.wait(0.9)

        annotation = Text(
            "a · b", font=FONT_MONO, color=DATA_PARAMS, font_size=32
        ).move_to([-1.55, -2.8, 0.0])
        self.play(Write(annotation), run_time=1.0)
        self.wait(1.8)

        # ------------------------------------------------------------
        # Part 3: the aha sentence trues up.
        # ------------------------------------------------------------
        dial_static = VGroup(arc, oppose_label, ignore_label, agree_label)

        self.play(
            FadeOut(candidate_mini),
            FadeOut(probe_mini),
            FadeOut(readout),
            FadeOut(annotation),
            dial_static.animate.set_opacity(0.4),
            dial_opacity.animate.set_value(0.4),
            run_time=1.0,
        )
        self.wait(0.4)

        aha_text = Text(
            "The dot product is\na similarity meter.",
            font=FONT_HEADING,
            color=DATA_FIT,
            font_size=40,
        ).move_to([0.0, -0.3, 0.0])

        self.play(Write(aha_text), run_time=1.6)
        self.wait(1.0)

        underline = Line(
            [-aha_text.width / 2 - 0.15, -1.4, 0.0],
            [aha_text.width / 2 + 0.15, -1.4, 0.0],
            color=DATA_FIT,
            stroke_width=6,
        )
        underline.insert_n_curves(15)
        roughen(underline)

        self.play(Create(underline), run_time=0.6)
        self.wait(0.2)
        self.play(wobble_once(underline), run_time=0.35)
        self.wait(0.15)
        self.play(true_up(underline, settle_color=DATA_FIT, glow_color=DATA_FIT))
        self.wait(1.0)

        # ------------------------------------------------------------
        # Part 4: the dial replays once more, tracking direction, then
        # the aha resolves as the closing focus.
        # ------------------------------------------------------------
        angle_tracker.set_value(PI)
        self.play(
            dial_static.animate.set_opacity(1.0),
            dial_opacity.animate.set_value(1.0),
            run_time=0.8,
        )
        self.wait(0.3)

        self.play(angle_tracker.animate.set_value(0.0), run_time=3.2)
        self.wait(1.0)

        self.play(
            dial_static.animate.set_opacity(0.35),
            dial_opacity.animate.set_value(0.35),
            aha_text.animate.set_opacity(1.0),
            underline.animate.set_opacity(1.0),
            run_time=1.0,
        )
        self.wait(1.85)
