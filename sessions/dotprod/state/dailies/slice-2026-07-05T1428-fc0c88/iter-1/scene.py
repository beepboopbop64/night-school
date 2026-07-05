import sys
from pathlib import Path

from manim import *  # noqa: F403

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "shared" / "manim"))
from bbox_dump import attach_bbox_dump  # noqa: E402
from colors import *  # noqa: E402,F403
from style import FONT_BODY, FONT_HEADING, FONT_MONO  # noqa: E402

import numpy as np  # noqa: E402


def _needle_tip(center: np.ndarray, radius: float, angle: float) -> np.ndarray:
    return center + radius * np.array([np.cos(angle), np.sin(angle), 0.0])


class Beat04(Scene):
    def construct(self):
        attach_bbox_dump(self)
        self.camera.background_color = BG

        # ------------------------------------------------------------------
        # The meter: a half-dial that persists (idle, then lit) for the
        # whole beat. Center low on screen so it never fights the card or
        # the two columns above it.
        # ------------------------------------------------------------------
        dial_center = np.array([0.0, -1.2, 0.0])
        dial_radius = 0.9
        needle_len = 0.75
        angle_idle = PI * 0.75
        score_value = 58
        angle_score = PI - (score_value / 100.0) * PI

        track = Arc(
            radius=dial_radius,
            start_angle=PI,
            angle=-PI,
            arc_center=dial_center,
            color=TEXT,
            stroke_width=6,
        )
        pivot = Dot(point=dial_center, radius=0.055, color=TEXT)
        needle = Line(
            dial_center,
            _needle_tip(dial_center, needle_len, angle_idle),
            color=DATA_PARAMS,
            stroke_width=8,
        )
        dial = VGroup(track, pivot, needle)

        self.play(Create(track), run_time=1.0)
        self.play(Create(pivot), Create(needle), run_time=0.6)
        self.wait(0.3)

        # ------------------------------------------------------------------
        # The question card. It holds the actual puzzle; the dial idles
        # beneath it, dimmed so the card is the one lit thing.
        # ------------------------------------------------------------------
        card_text = Text(
            "Two arrows go in.\nWhat two operations turn them into the score?",
            font=FONT_BODY,
            font_size=30,
            color=TEXT,
            line_spacing=1.2,
        ).move_to(np.array([0.0, 2.7, 0.0]))
        card_rect = SurroundingRectangle(
            card_text,
            buff=0.4,
            color=TEXT,
            fill_color=SURFACE,
            fill_opacity=1.0,
            stroke_width=2,
        )

        self.play(Create(card_rect), dial.animate.set_opacity(0.4), run_time=0.8)
        self.play(Write(card_text), run_time=1.2)
        self.wait(5.1)

        card_group = VGroup(card_rect, card_text)
        self.play(FadeOut(card_group), run_time=0.7)
        self.wait(0.3)

        # ------------------------------------------------------------------
        # Different aisle: the two columns swap songs for a job posting.
        # "you" and "the role", three matched rows each, built in order.
        # ------------------------------------------------------------------
        you_x = -3.5
        role_x = 3.5
        mid_x = 0.0
        header_y = 3.2
        row_ys = (2.3, 1.4, 0.5)

        header_you = Text("you", font=FONT_HEADING, font_size=34, color=DATA_OBSERVED)
        header_you.move_to(np.array([you_x, header_y, 0.0]))
        header_role = Text("the role", font=FONT_HEADING, font_size=34, color=DATA_OBSERVED)
        header_role.move_to(np.array([role_x, header_y, 0.0]))

        self.play(Write(header_you), Write(header_role), run_time=1.0)

        row1_you = Text(
            "Python hours: 12", font=FONT_BODY, font_size=30, color=TEXT, t2c={"12": DATA_OBSERVED}
        ).move_to(np.array([you_x, row_ys[0], 0.0]))
        row1_role = Text(
            "Python hours: 3", font=FONT_BODY, font_size=30, color=TEXT, t2c={"3": DATA_OBSERVED}
        ).move_to(np.array([role_x, row_ys[0], 0.0]))
        mult1 = Text("×", font=FONT_BODY, font_size=32, color=TEXT)
        mult1.move_to(np.array([mid_x, row_ys[0], 0.0]))

        row2_you = Text(
            "SQL reps: 5", font=FONT_BODY, font_size=30, color=TEXT, t2c={"5": DATA_OBSERVED}
        ).move_to(np.array([you_x, row_ys[1], 0.0]))
        row2_role = Text(
            "SQL reps: 4", font=FONT_BODY, font_size=30, color=TEXT, t2c={"4": DATA_OBSERVED}
        ).move_to(np.array([role_x, row_ys[1], 0.0]))
        mult2 = Text("×", font=FONT_BODY, font_size=32, color=TEXT)
        mult2.move_to(np.array([mid_x, row_ys[1], 0.0]))

        row3_you = Text(
            "nights free: 2", font=FONT_BODY, font_size=30, color=TEXT, t2c={"2": DATA_OBSERVED}
        ).move_to(np.array([you_x, row_ys[2], 0.0]))
        row3_role = Text(
            "nights free: 1", font=FONT_BODY, font_size=30, color=TEXT, t2c={"1": DATA_OBSERVED}
        ).move_to(np.array([role_x, row_ys[2], 0.0]))
        mult3 = Text("×", font=FONT_BODY, font_size=32, color=TEXT)
        mult3.move_to(np.array([mid_x, row_ys[2], 0.0]))

        self.play(Write(row1_you), Write(row1_role), run_time=0.8)
        self.play(Write(mult1), run_time=0.4)
        self.play(Write(row2_you), Write(row2_role), run_time=0.8)
        self.play(Write(mult2), run_time=0.4)
        self.play(Write(row3_you), Write(row3_role), run_time=0.8)
        self.play(Write(mult3), run_time=0.4)
        self.wait(0.6)

        table_group = VGroup(
            header_you, header_role,
            row1_you, row1_role,
            row2_you, row2_role,
            row3_you, row3_role,
        )

        # Each matched pair multiplies in place: the operator becomes the
        # product, colored into the score's lilac.
        product1 = Text("36", font=FONT_MONO, font_size=30, color=DATA_PARAMS).move_to(mult1)
        product2 = Text("20", font=FONT_MONO, font_size=30, color=DATA_PARAMS).move_to(mult2)
        product3 = Text("2", font=FONT_MONO, font_size=30, color=DATA_PARAMS).move_to(mult3)
        self.play(
            Transform(mult1, product1),
            Transform(mult2, product2),
            Transform(mult3, product3),
            run_time=1.0,
        )
        self.wait(0.5)

        # The three products pool into one lilac number on the same dial.
        score_pos = dial_center + np.array([0.0, -0.7, 0.0])
        score_text = Text(str(score_value), font=FONT_MONO, font_size=44, color=DATA_PARAMS)
        score_text.move_to(score_pos)

        self.play(
            mult1.animate.move_to(score_pos).scale(0.05).set_opacity(0.0),
            mult2.animate.move_to(score_pos).scale(0.05).set_opacity(0.0),
            mult3.animate.move_to(score_pos).scale(0.05).set_opacity(0.0),
            FadeIn(score_text, scale=0.5),
            table_group.animate.set_opacity(0.4),
            dial.animate.set_opacity(1.0),
            run_time=1.3,
        )
        self.remove(mult1, mult2, mult3)

        self.play(
            Rotate(needle, angle=(angle_score - angle_idle), about_point=dial_center),
            run_time=1.0,
        )

        readout_label = Text(
            "two arrows in, one number out", font=FONT_BODY, font_size=28, color=TEXT
        )
        readout_label.next_to(score_text, DOWN, buff=0.4)
        self.play(Write(readout_label), run_time=1.0)
        self.wait(3.3)

        closing_line = Text(
            "Different aisle, same meter.", font=FONT_HEADING, font_size=34, color=TEXT
        )
        closing_line.next_to(readout_label, DOWN, buff=0.4)
        self.play(
            Write(closing_line),
            VGroup(dial, table_group, score_text, readout_label).animate.set_opacity(0.4),
            run_time=1.5,
        )
        self.wait(7.0)
