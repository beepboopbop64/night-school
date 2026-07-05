import sys
from pathlib import Path

import numpy as np
from manim import *  # noqa: F403

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "shared" / "manim"))
from bbox_dump import attach_bbox_dump  # noqa: E402
from colors import *  # noqa: E402,F403
from style import FONT_BODY, FONT_HEADING, FONT_MONO  # noqa: E402


class Beat04(Scene):
    def construct(self):
        attach_bbox_dump(self)
        self.camera.background_color = BG

        def make_card(text_str, font_size, position, text_color=TEXT):
            txt = Text(text_str, font=FONT_BODY, font_size=font_size, color=text_color)
            bg = RoundedRectangle(
                width=txt.width + 0.9,
                height=txt.height + 0.55,
                corner_radius=0.15,
                stroke_color=TEXT,
                stroke_width=2,
                fill_color=SURFACE,
                fill_opacity=1.0,
            )
            bg.move_to(position)
            txt.move_to(position)
            return bg, txt

        def score_angle(score, max_score=100.0):
            frac = max(0.0, min(1.0, score / max_score))
            return PI - frac * PI

        # ------------------------------------------------------------------
        # Dial (the meter) -- built once, kept running for the whole beat.
        # ------------------------------------------------------------------
        dial_center = np.array([4.8, 1.0, 0.0])
        dial_radius = 1.2
        dial_arc = Arc(
            radius=dial_radius,
            start_angle=PI,
            angle=-PI,
            arc_center=dial_center,
            color=TEXT,
            stroke_width=5,
        )
        angle_tracker = ValueTracker(score_angle(15))
        needle = always_redraw(
            lambda: Line(
                dial_center,
                dial_center
                + dial_radius
                * 0.85
                * np.array(
                    [np.cos(angle_tracker.get_value()), np.sin(angle_tracker.get_value()), 0.0]
                ),
                color=DATA_PARAMS,
                stroke_width=6,
            )
        )
        needle_dot = Dot(dial_center, radius=0.06, color=TEXT)

        # ------------------------------------------------------------------
        # Phase A -- retrieval prompt card holds while the meter idles.
        # ------------------------------------------------------------------
        prompt_bg, prompt_text = make_card("match query: best-fit role", 30, (0, 3.0, 0))
        self.play(Create(prompt_bg), Write(prompt_text), run_time=1.5)
        self.play(Create(dial_arc), FadeIn(needle), FadeIn(needle_dot), run_time=1.5)
        self.play(
            angle_tracker.animate.set_value(score_angle(25)),
            rate_func=there_and_back,
            run_time=1.0,
        )
        self.wait(8.0)
        self.play(FadeOut(prompt_bg), FadeOut(prompt_text), run_time=1.0)

        # ------------------------------------------------------------------
        # Phase B -- same dial, new shelf: "you" vs "the role".
        # ------------------------------------------------------------------
        you_x, role_x = -3.5, 0.3
        header_you = Text("YOU", font=FONT_HEADING, font_size=34, color=DATA_OBSERVED)
        header_you.move_to((you_x, 2.6, 0))
        header_role = Text("THE ROLE", font=FONT_HEADING, font_size=34, color=TEXT)
        header_role.move_to((role_x, 2.6, 0))
        self.play(Write(header_you), Write(header_role), run_time=1.5)

        metrics = ["Python hrs", "SQL reps", "nights free"]
        you_vals = [6, 4, 2]
        role_vals = [5, 3, 3]
        row_ys = [1.6, 0.6, -0.4]

        you_rows = VGroup(
            *[
                Text(f"{m}: {v}", font=FONT_BODY, font_size=28, color=DATA_OBSERVED)
                for m, v in zip(metrics, you_vals)
            ]
        )
        for row, y in zip(you_rows, row_ys):
            row.move_to((you_x, y, 0))
        role_rows = VGroup(
            *[
                Text(f"{m}: {v}", font=FONT_BODY, font_size=28, color=TEXT)
                for m, v in zip(metrics, role_vals)
            ]
        )
        for row, y in zip(role_rows, row_ys):
            row.move_to((role_x, y, 0))

        self.play(*[Write(r) for r in you_rows], run_time=1.8)
        self.play(*[Write(r) for r in role_rows], run_time=1.8)
        self.wait(2.0)

        self.play(
            *[Indicate(you_rows[i], color=DATA_PARAMS) for i in range(3)],
            *[Indicate(role_rows[i], color=DATA_PARAMS) for i in range(3)],
            run_time=2.5,
        )

        dot_x = 2.2
        product_dots = VGroup(
            *[Dot((dot_x, y, 0), radius=0.09, color=DATA_PARAMS) for y in row_ys]
        )
        self.play(Create(product_dots), run_time=1.3)
        self.play(product_dots.animate.move_to(dial_center), run_time=1.5)

        score = sum(a * b for a, b in zip(you_vals, role_vals))
        score_readout = Text(f"score: {score}", font=FONT_MONO, font_size=32, color=DATA_PARAMS)
        score_readout.move_to((4.8, -0.9, 0))
        self.play(
            FadeOut(product_dots),
            FadeIn(score_readout),
            angle_tracker.animate.set_value(score_angle(score)),
            run_time=1.5,
        )
        self.wait(4.0)

        self.play(
            FadeOut(header_you),
            FadeOut(header_role),
            FadeOut(you_rows),
            FadeOut(role_rows),
            FadeOut(score_readout),
            run_time=1.2,
        )
        self.play(angle_tracker.animate.set_value(PI / 2), run_time=1.0)

        # ------------------------------------------------------------------
        # Phase C -- guess card: one candidate outlined, score hidden.
        # ------------------------------------------------------------------
        guess_bg, guess_text = make_card("your guess: score change?", 30, (0, 3.0, 0))
        self.play(Create(guess_bg), Write(guess_text), run_time=1.5)

        origin = np.array([-4.0, -1.0, 0.0])
        angle_fixed = 35 * DEGREES
        direction = np.array([np.cos(angle_fixed), np.sin(angle_fixed), 0.0])
        baseline = DashedLine(origin, origin + np.array([3.4, 0.0, 0.0]), color=TEXT, stroke_width=2)
        baseline.set_opacity(0.4)
        angle_arc = Arc(
            radius=0.6, start_angle=0, angle=angle_fixed, arc_center=origin, color=TEXT, stroke_width=3
        )
        self.play(Create(baseline), Create(angle_arc), run_time=1.2)

        arrow_len_tracker = ValueTracker(1.6)
        candidate_arrow = always_redraw(
            lambda: Arrow(
                origin,
                origin + arrow_len_tracker.get_value() * direction,
                buff=0,
                color=DATA_OBSERVED,
                stroke_width=6,
                max_tip_length_to_length_ratio=0.15,
            )
        )
        label_candidate = Text("candidate", font=FONT_BODY, font_size=28, color=DATA_OBSERVED)
        label_candidate.move_to(origin + np.array([0.0, -1.1, 0.0]))
        self.play(FadeIn(candidate_arrow), Write(label_candidate), run_time=1.2)

        temp_line = Line(origin, origin + 1.6 * direction)
        outline_rect = DashedVMobject(
            SurroundingRectangle(temp_line, buff=0.35, color=DATA_OBSERVED, stroke_width=2)
        )
        hidden_score = Text("score: ?", font=FONT_MONO, font_size=32, color=TEXT)
        hidden_score.move_to((4.8, -0.9, 0))
        self.play(Create(outline_rect), Write(hidden_score), run_time=1.2)

        self.wait(7.0)

        # ------------------------------------------------------------------
        # Phase D -- reveal: size climbs the score, direction never moves.
        # ------------------------------------------------------------------
        score_tracker = ValueTracker(score)
        score_climb = always_redraw(
            lambda: Text(
                f"score: {score_tracker.get_value():.0f}",
                font=FONT_MONO,
                font_size=32,
                color=DATA_PARAMS,
            ).move_to((4.8, -0.9, 0))
        )
        self.play(FadeOut(hidden_score), FadeIn(score_climb), run_time=0.8)

        self.play(
            arrow_len_tracker.animate.set_value(3.2),
            score_tracker.animate.set_value(score * 2),
            angle_tracker.animate.set_value(score_angle(min(score * 2, 100))),
            run_time=3.5,
        )
        self.wait(3.0)

        tip_point = origin + 3.2 * direction
        flag_pole = Line(tip_point, tip_point + UP * 0.6, color=DATA_ERROR, stroke_width=4)
        flag_tri = Polygon(
            tip_point + UP * 0.6,
            tip_point + UP * 0.6 + RIGHT * 0.35 + DOWN * 0.12,
            tip_point + UP * 0.6 + DOWN * 0.24,
            color=DATA_ERROR,
            fill_color=DATA_ERROR,
            fill_opacity=1.0,
            stroke_width=0,
        )
        flag_group = VGroup(flag_pole, flag_tri)
        flag_label = Text("size, not fit", font=FONT_BODY, font_size=28, color=DATA_ERROR)
        flag_label.next_to(flag_group, RIGHT, buff=0.35)
        self.play(Create(flag_group), Write(flag_label), run_time=1.5)
        self.play(Indicate(flag_group, color=DATA_ERROR), run_time=1.3)
        self.wait(4.5)

        self.play(Indicate(angle_arc, color=TEXT, scale_factor=1.2), run_time=1.5)
        self.wait(3.5)

        # ------------------------------------------------------------------
        # Phase F -- closing question + a quiet pointer to the menu.
        # ------------------------------------------------------------------
        self.play(
            FadeOut(
                VGroup(
                    guess_bg,
                    guess_text,
                    baseline,
                    angle_arc,
                    candidate_arrow,
                    label_candidate,
                    outline_rect,
                    score_climb,
                    flag_group,
                    flag_label,
                    dial_arc,
                    needle,
                    needle_dot,
                )
            ),
            run_time=1.2,
        )

        closing_bg, closing_text = make_card("keep direction, forget size?", 30, (0, 1.5, 0))
        self.play(Create(closing_bg), Write(closing_text), run_time=1.8)
        self.wait(5.0)

        chip_bg, chip_text = make_card("extensions menu", 26, (0, -2.0, 0))
        self.play(Create(chip_bg), Write(chip_text), run_time=1.3)
        chip_arrow = Arrow(
            chip_bg.get_bottom(),
            chip_bg.get_bottom() + DOWN * 0.8,
            color=TEXT,
            stroke_width=3,
            buff=0.1,
        )
        self.play(Create(chip_arrow), run_time=0.8)

        self.wait(10.0)
