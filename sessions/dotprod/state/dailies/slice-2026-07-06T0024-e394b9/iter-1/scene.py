import sys
from pathlib import Path

from manim import *  # noqa: F403

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "shared" / "manim"))
from bbox_dump import attach_bbox_dump  # noqa: E402
from colors import *  # noqa: E402,F403
from style import FONT_BODY, FONT_HEADING, FONT_MONO  # noqa: E402

import numpy as np  # noqa: E402


class Beat04b(Scene):
    def construct(self):
        attach_bbox_dump(self)
        self.camera.background_color = BG

        # ------------------------------------------------------------------
        # Part 1: the guess card
        # ------------------------------------------------------------------
        card = RoundedRectangle(
            width=11.0,
            height=6.6,
            corner_radius=0.3,
            stroke_color=TEXT,
            stroke_opacity=0.5,
            stroke_width=2,
            fill_color=SURFACE,
            fill_opacity=0.4,
        ).move_to(ORIGIN)

        self.play(Create(card), run_time=1.0)

        origin_pt = np.array([-4.0, -1.8, 0.0])
        v1 = np.array([1.6, 1.0, 0.0])
        tip1 = origin_pt + v1

        c1_arrow = Arrow(
            start=origin_pt,
            end=tip1,
            buff=0,
            color=DATA_OBSERVED,
            stroke_width=7,
            max_tip_length_to_length_ratio=0.25,
        )
        c1_label = Text("c1", font=FONT_BODY, font_size=30, color=DATA_OBSERVED)
        c1_label.next_to(tip1, UP * 0.3 + RIGHT * 0.2, buff=0.15)

        self.play(Create(c1_arrow), Write(c1_label), run_time=1.2)

        score_hidden = Text("?", font=FONT_MONO, font_size=40, color=DATA_PARAMS)
        score_hidden.move_to([3.0, 1.3, 0])

        self.play(FadeIn(score_hidden), run_time=0.8)

        question = Text(
            "Double c1's length, same direction —\n"
            "does the score double exactly, or just drift up?",
            font=FONT_BODY,
            font_size=28,
            color=TEXT,
            line_spacing=1.1,
        )
        question.move_to([0.0, 2.4, 0])

        self.play(Write(question), run_time=1.5)
        self.wait(6.5)

        # ------------------------------------------------------------------
        # Part 2: reveal the original score, then double c1
        # ------------------------------------------------------------------
        score_42 = Text("4.2", font=FONT_MONO, font_size=40, color=DATA_PARAMS)
        score_42.move_to(score_hidden.get_center())

        self.play(
            ReplacementTransform(score_hidden, score_42),
            question.animate.set_opacity(0.4),
            run_time=1.0,
        )
        self.wait(1.5)

        v2 = v1 * 2.0
        tip2 = origin_pt + v2
        c1_arrow_double = Arrow(
            start=origin_pt,
            end=tip2,
            buff=0,
            color=DATA_OBSERVED,
            stroke_width=7,
            max_tip_length_to_length_ratio=0.2,
        )
        c1_label_double = Text("c1", font=FONT_BODY, font_size=30, color=DATA_OBSERVED)
        c1_label_double.next_to(tip2, UP * 0.3 + RIGHT * 0.2, buff=0.15)

        self.play(
            Transform(c1_arrow, c1_arrow_double),
            Transform(c1_label, c1_label_double),
            run_time=3.5,
        )

        times2 = Text("×2", font=FONT_MONO, font_size=34, color=TEXT)
        times2.move_to([3.0, 0.2, 0])
        self.play(FadeIn(times2), run_time=0.8)

        score_84 = Text("8.4", font=FONT_MONO, font_size=44, color=DATA_PARAMS)
        score_84.move_to([3.0, -0.9, 0])
        self.play(FadeIn(score_84), run_time=1.0)
        self.play(Indicate(score_84, color=DATA_PARAMS, scale_factor=1.15), run_time=0.5)
        self.wait(1.0)

        # ------------------------------------------------------------------
        # Part 3: the flag — size passed straight through
        # ------------------------------------------------------------------
        flag_pos = np.array([3.0, -1.9, 0.0])
        pole = Line(
            flag_pos + DOWN * 0.3,
            flag_pos + UP * 0.3,
            color=TEXT,
            stroke_width=4,
        )
        pennant = Triangle(
            color=DATA_ERROR,
            fill_color=DATA_ERROR,
            fill_opacity=1.0,
            stroke_width=0,
        )
        pennant.scale(0.22)
        pennant.rotate(-PI / 2)
        pennant.move_to(flag_pos + UP * 0.25 + RIGHT * 0.18)
        flag_icon = VGroup(pole, pennant)

        flag_label = Text(
            "size passes straight through",
            font=FONT_BODY,
            font_size=26,
            color=TEXT,
        )
        flag_label.move_to([3.0, -2.9, 0])

        self.play(
            c1_arrow.animate.set_opacity(0.5),
            c1_label.animate.set_opacity(0.5),
            run_time=0.6,
        )
        self.play(FadeIn(flag_icon), Write(flag_label), run_time=1.2)
        self.wait(3.0)

        # ------------------------------------------------------------------
        # Part 4: the loud, long candidate outranking a shorter, truer one
        # ------------------------------------------------------------------
        part1_group = VGroup(
            card,
            c1_arrow,
            c1_label,
            question,
            score_42,
            times2,
            score_84,
            flag_icon,
            flag_label,
        )
        self.play(FadeOut(part1_group), run_time=1.0)
        self.wait(0.5)

        baseline_y = -2.0
        bar_c2 = Rectangle(
            width=1.2,
            height=3.4,
            stroke_color=DATA_OBSERVED,
            stroke_width=4,
            fill_color=DATA_PARAMS,
            fill_opacity=0.85,
        )
        bar_c2.move_to([-3.0, baseline_y + 3.4 / 2, 0])
        label_c2 = Text("c2\nloud", font=FONT_BODY, font_size=26, color=DATA_OBSERVED)
        label_c2.next_to(bar_c2, DOWN, buff=0.4)

        self.play(Create(bar_c2), Write(label_c2), run_time=1.5)

        score_c2 = Text("6.0", font=FONT_MONO, font_size=32, color=DATA_PARAMS)
        score_c2.next_to(bar_c2, UP, buff=0.4)
        self.play(FadeIn(score_c2), run_time=0.8)
        self.wait(1.0)

        bar_c3 = Rectangle(
            width=1.2,
            height=1.75,
            stroke_color=DATA_OBSERVED,
            stroke_width=4,
            fill_color=DATA_PARAMS,
            fill_opacity=0.85,
        )
        bar_c3.move_to([2.0, baseline_y + 1.75 / 2, 0])
        label_c3 = Text(
            "c3\nbetter aligned", font=FONT_BODY, font_size=26, color=DATA_OBSERVED
        )
        label_c3.next_to(bar_c3, DOWN, buff=0.4)

        self.play(Create(bar_c3), Write(label_c3), run_time=1.5)

        score_c3 = Text("3.5", font=FONT_MONO, font_size=32, color=DATA_PARAMS)
        score_c3.next_to(bar_c3, UP, buff=0.4)
        self.play(FadeIn(score_c3), run_time=0.8)
        self.wait(1.5)

        callout = Text(
            "c2 outscores c3 on size alone",
            font=FONT_BODY,
            font_size=30,
            color=TEXT,
        )
        callout.move_to([-0.5, -3.6, 0])
        self.play(Write(callout), run_time=1.5)
        self.wait(7.1)
