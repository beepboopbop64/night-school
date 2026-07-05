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

        def fit_width(mob, max_w):
            if mob.width > max_w:
                mob.scale_to_fit_width(max_w)
            return mob

        # ------------------------------------------------------------
        # Part 1: the guess card (no header; the card poses the question)
        # ------------------------------------------------------------
        card_bg = RoundedRectangle(
            width=9.5,
            height=6.2,
            corner_radius=0.3,
            fill_color=SURFACE,
            fill_opacity=1.0,
            stroke_color=TEXT,
            stroke_width=2,
        ).move_to(np.array([0.0, 0.1, 0.0]))

        self.play(Create(card_bg), run_time=1.2)

        question = Text(
            "Double c1's length.\nDoes the number double?",
            font=FONT_BODY,
            font_size=32,
            color=TEXT,
            line_spacing=1.0,
        )
        fit_width(question, 8.2)
        question.move_to(np.array([0.0, 2.4, 0.0]))
        self.play(Write(question), run_time=1.8)
        self.wait(1.5)

        # the candidate vector: one item, outlined as the selected guess,
        # score readout absent (hidden) for now.
        tail = np.array([-2.0, -0.9, 0.0])
        angle = 15 * DEGREES
        direction = np.array([np.cos(angle), np.sin(angle), 0.0])
        tip1 = tail + 2.0 * direction

        origin_dot = Dot(point=tail, radius=0.05, color=TEXT)
        origin_dot.set_opacity(0.5)

        arrow = Arrow(
            start=tail,
            end=tip1,
            buff=0.0,
            color=DATA_OBSERVED,
            stroke_width=7,
        )
        label = Text("c1", font=FONT_BODY, font_size=30, color=DATA_OBSERVED)
        label.move_to(tip1 + np.array([0.35, 0.32, 0.0]))

        outline = SurroundingRectangle(
            VGroup(arrow, label), buff=0.25, color=DATA_OBSERVED
        )

        candidate_group = VGroup(origin_dot, arrow, label, outline)
        self.play(Create(candidate_group), run_time=1.8)
        self.wait(5.0)

        # ------------------------------------------------------------
        # The doubling reveal: length doubles, direction untouched
        # ------------------------------------------------------------
        tip2 = tail + 4.0 * direction
        label_target = tip2 + np.array([0.35, 0.32, 0.0])

        self.play(
            FadeOut(outline),
            arrow.animate.put_start_and_end_on(tail, tip2),
            label.animate.move_to(label_target),
            run_time=2.5,
        )

        score_old = Text("4.2", font=FONT_MONO, font_size=36, color=DATA_PARAMS)
        score_mult = Text("x2", font=FONT_MONO, font_size=30, color=TEXT)
        score_new = Text("8.4", font=FONT_MONO, font_size=36, color=DATA_PARAMS)
        score_stack = VGroup(score_old, score_mult, score_new).arrange(DOWN, buff=0.22)
        score_stack.move_to(np.array([3.4, -0.7, 0.0]))

        self.play(Write(score_stack), run_time=2.5)
        self.wait(3.0)

        # rose flag: size passed straight through
        pole = Line(
            np.array([0.0, -0.25, 0.0]),
            np.array([0.0, 0.25, 0.0]),
            color=DATA_ERROR,
            stroke_width=4,
        )
        pennant = Polygon(
            np.array([0.0, 0.25, 0.0]),
            np.array([0.35, 0.13, 0.0]),
            np.array([0.0, 0.02, 0.0]),
            color=DATA_ERROR,
            fill_color=DATA_ERROR,
            fill_opacity=1.0,
            stroke_width=0,
        )
        flag_icon = VGroup(pole, pennant)
        flag_text = Text(
            "Size passes straight through",
            font=FONT_BODY,
            font_size=28,
            color=TEXT,
        )
        flag_group = VGroup(flag_icon, flag_text).arrange(RIGHT, buff=0.3)
        fit_width(flag_group, 8.2)
        flag_group.move_to(np.array([0.0, -2.3, 0.0]))

        self.play(Create(flag_group), run_time=1.5)
        self.wait(6.5)

        part1_group = VGroup(
            card_bg,
            question,
            origin_dot,
            arrow,
            label,
            score_stack,
            flag_group,
        )
        self.play(FadeOut(part1_group), run_time=1.2)

        # ------------------------------------------------------------
        # Part 2: the walk-home closing card
        # ------------------------------------------------------------
        closing_card = RoundedRectangle(
            width=9.5,
            height=6.2,
            corner_radius=0.3,
            fill_color=SURFACE,
            fill_opacity=1.0,
            stroke_color=TEXT,
            stroke_width=2,
        ).move_to(np.array([0.0, 0.1, 0.0]))
        self.play(Create(closing_card), run_time=1.2)

        header = Text(
            "For the walk home",
            font=FONT_HEADING,
            font_size=40,
            color=TEXT,
        )
        header.move_to(np.array([0.0, 2.5, 0.0]))
        self.play(Write(header), run_time=1.2)

        question2 = Text(
            "What's the cheapest fix that keeps\nthe direction and forgets the size?",
            font=FONT_BODY,
            font_size=30,
            color=TEXT,
            line_spacing=1.0,
        )
        fit_width(question2, 8.2)
        question2.move_to(np.array([0.0, 0.9, 0.0]))
        self.play(Write(question2), run_time=2.5)
        self.wait(3.5)

        chip_bg = RoundedRectangle(
            width=5.4,
            height=0.8,
            corner_radius=0.4,
            fill_color=SURFACE,
            fill_opacity=0.6,
            stroke_color=TEXT,
            stroke_width=1.5,
        )
        chip_bg.set_stroke(opacity=0.6)
        chip_text = Text(
            "Three ways to keep going",
            font=FONT_BODY,
            font_size=26,
            color=TEXT,
        )
        chip_text.set_opacity(0.6)
        fit_width(chip_text, 4.8)
        chip_group = VGroup(chip_bg, chip_text)
        chip_text.move_to(chip_bg.get_center())
        chip_group.move_to(np.array([0.0, -1.6, 0.0]))

        chip_arrow = Arrow(
            start=np.array([0.0, -2.05, 0.0]),
            end=np.array([0.0, -2.45, 0.0]),
            buff=0.0,
            color=TEXT,
            stroke_width=4,
        )
        chip_arrow.set_opacity(0.6)

        self.play(Create(chip_bg), Write(chip_text), Create(chip_arrow), run_time=1.5)
        self.wait(7.9)
