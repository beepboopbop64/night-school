import sys
from pathlib import Path

from manim import *  # noqa: F403

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "shared" / "manim"))
from bbox_dump import attach_bbox_dump  # noqa: E402
from colors import *  # noqa: E402,F403
from style import FONT_BODY, FONT_HEADING, FONT_MONO  # noqa: E402


class Beat04b(Scene):
    def construct(self):
        attach_bbox_dump(self)
        self.camera.background_color = BG

        # ---------------- Phase 1: Guess ----------------
        header = Text("Guess", font=FONT_HEADING, color=TEXT, font_size=36)
        header.move_to(UP * 3.4)
        self.play(FadeIn(header, shift=DOWN * 0.2), run_time=1.0)

        origin = LEFT * 4.8 + DOWN * 1.3
        direction = rotate_vector(RIGHT, 40 * DEGREES)
        tip1 = origin + 2 * direction

        x_axis = Line(
            origin + LEFT * 1.8, origin + RIGHT * 1.8,
            color=TEXT, stroke_width=2, stroke_opacity=0.35,
        )
        y_axis = Line(
            origin + DOWN * 1.1, origin + UP * 3.5,
            color=TEXT, stroke_width=2, stroke_opacity=0.35,
        )
        axes = VGroup(x_axis, y_axis)

        c1_arrow = Arrow(
            origin, tip1, buff=0, color=DATA_OBSERVED,
            stroke_width=6, max_tip_length_to_length_ratio=0.25,
        )
        c1_label = Text("c1", font=FONT_BODY, color=DATA_OBSERVED, font_size=30)
        c1_label.next_to(tip1, UP + RIGHT, buff=0.15)

        self.play(Create(axes), GrowArrow(c1_arrow), Write(c1_label), run_time=1.8)

        outline = DashedVMobject(
            SurroundingRectangle(c1_arrow, color=DATA_OBSERVED, buff=0.35),
            num_dashes=24,
        )
        score_box = Rectangle(
            width=1.9, height=1.3, color=DATA_PARAMS,
            stroke_width=3, fill_color=SURFACE, fill_opacity=0.5,
        )
        score_box.move_to([3.2, -0.3, 0])
        score_label = Text("score", font=FONT_BODY, color=TEXT, font_size=26)
        score_label.next_to(score_box, UP, buff=0.35)
        score_mark = Text("?", font=FONT_MONO, color=DATA_PARAMS, font_size=44)
        score_mark.move_to(score_box.get_center())

        self.play(
            Create(outline), Create(score_box), Write(score_label), Write(score_mark),
            run_time=1.6,
        )

        question = Text(
            "Double c1's length, keep its direction — same score?",
            font=FONT_BODY, color=TEXT, font_size=30,
        )
        question.move_to(DOWN * 3.3)
        self.play(Write(question), run_time=1.8)
        self.wait(6.4)

        # ---------------- Phase 2a: reveal + double ----------------
        reveal_header = Text("Reveal", font=FONT_HEADING, color=TEXT, font_size=36)
        reveal_header.move_to(header.get_center())
        self.play(Transform(header, reveal_header), FadeOut(question), run_time=1.0)

        target_42 = Text("4.2", font=FONT_MONO, color=DATA_PARAMS, font_size=40)
        target_42.move_to(score_box.get_center())
        self.play(Transform(score_mark, target_42), run_time=1.0)
        self.wait(1.0)

        tip2 = origin + 4 * direction
        target_arrow2 = Arrow(
            origin, tip2, buff=0, color=DATA_OBSERVED,
            stroke_width=6, max_tip_length_to_length_ratio=0.2,
        )
        target_label2 = Text("c1", font=FONT_BODY, color=DATA_OBSERVED, font_size=30)
        target_label2.next_to(tip2, UP + RIGHT, buff=0.15)
        target_outline2 = DashedVMobject(
            SurroundingRectangle(target_arrow2, color=DATA_OBSERVED, buff=0.35),
            num_dashes=28,
        )
        self.play(
            Transform(c1_arrow, target_arrow2),
            Transform(c1_label, target_label2),
            Transform(outline, target_outline2),
            run_time=2.2,
        )
        self.wait(0.8)

        target_tall_box = Rectangle(
            width=1.9, height=2.6, color=DATA_PARAMS,
            stroke_width=3, fill_color=SURFACE, fill_opacity=0.5,
        )
        target_tall_box.move_to([3.2, -0.65, 0])
        connector = Text("x2", font=FONT_MONO, color=TEXT, font_size=26)
        connector.move_to([3.2, -0.35, 0])
        new_score = Text("8.4", font=FONT_MONO, color=DATA_PARAMS, font_size=40)
        new_score.move_to([3.2, -1.0, 0])

        self.play(
            Transform(score_box, target_tall_box),
            score_label.animate.next_to(target_tall_box, UP, buff=0.35),
            score_mark.animate.move_to([3.2, 0.25, 0]),
            Write(connector),
            Write(new_score),
            run_time=1.8,
        )
        self.wait(2.2)

        # ---------------- Phase 2b: the crack ----------------
        pole = Line(DOWN * 0.3, UP * 0.3, color=DATA_ERROR, stroke_width=4)
        pennant = Polygon(
            UP * 0.3, UP * 0.3 + RIGHT * 0.35 + DOWN * 0.1, UP * 0.05,
            color=DATA_ERROR, fill_color=DATA_ERROR, fill_opacity=1, stroke_width=0,
        )
        flag_label = Text(
            "size passes through", font=FONT_BODY, color=DATA_ERROR, font_size=28,
        )
        flag_icon = VGroup(pole, pennant)
        flag_group = VGroup(flag_icon, flag_label).arrange(RIGHT, buff=0.3)
        flag_group.move_to([3.2, -2.6, 0])

        self.play(Create(pole), Create(pennant), Write(flag_label), run_time=1.6)
        self.wait(3.4)
        self.play(
            Indicate(VGroup(new_score, flag_label), color=DATA_ERROR, scale_factor=1.1),
            run_time=1.4,
        )
        self.wait(3.6)

        self.play(
            FadeOut(
                VGroup(
                    header, axes, c1_arrow, c1_label, outline, score_box,
                    score_label, score_mark, connector, new_score,
                    pole, pennant, flag_label,
                )
            ),
            run_time=1.2,
        )

        # ---------------- Phase 3: closing card ----------------
        closing_header = Text("Next", font=FONT_HEADING, color=TEXT, font_size=36)
        closing_header.move_to(UP * 3.4)
        closing_question = Text(
            "Keep the direction. Lose the size.",
            font=FONT_BODY, color=TEXT, font_size=32,
        )
        closing_question.next_to(closing_header, DOWN, buff=0.6)
        self.play(Write(closing_header), Write(closing_question), run_time=1.4)

        fix_question = Text(
            "What's the cheapest fix?", font=FONT_BODY, color=TEXT, font_size=32,
        )
        fix_question.next_to(closing_question, DOWN, buff=0.45)
        self.play(Write(fix_question), run_time=1.4)
        self.wait(1.4)

        still_up = Text("Still up?", font=FONT_BODY, color=TEXT, font_size=28)
        still_up.next_to(fix_question, DOWN, buff=0.5)
        self.play(Write(still_up), run_time=1.2)
        self.wait(1.8)

        chip_box = RoundedRectangle(
            corner_radius=0.15, width=4.6, height=0.9, color=TEXT,
            stroke_opacity=0.6, fill_color=SURFACE, fill_opacity=0.5,
        )
        chip_box.move_to([0, -1.0, 0])
        chip_text = Text(
            "3 ways to keep going", font=FONT_BODY, color=TEXT, font_size=26,
        )
        chip_text.move_to(chip_box.get_center())
        arrow_down = Arrow(
            chip_box.get_bottom(), chip_box.get_bottom() + DOWN * 0.6,
            buff=0.1, color=TEXT, stroke_width=3, stroke_opacity=0.6,
        )
        self.play(Create(chip_box), Write(chip_text), Create(arrow_down), run_time=1.6)
        self.wait(3.7)
