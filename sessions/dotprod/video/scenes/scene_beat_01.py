import sys
from pathlib import Path

from manim import *  # noqa: F403

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "shared" / "manim"))
from bbox_dump import attach_bbox_dump  # noqa: E402
from colors import *  # noqa: E402,F403
from style import FONT_BODY, FONT_HEADING, FONT_MONO  # noqa: E402


class Beat01(Scene):
    def construct(self):
        attach_bbox_dump(self)
        self.camera.background_color = BG

        # ------------------------------------------------------------------
        # Layout constants (left half carries the two lists + score, right
        # half stays empty until the question card claims it).
        # ------------------------------------------------------------------
        col_a_x = -5.5
        col_b_x = -2.5
        rows_y = [1.8, 0.8, -0.2, -1.2]
        taste_vals = ["0.90", "0.20", "-0.40", "0.70"]
        song_vals = ["0.80", "0.30", "-0.50", "0.60"]

        # ------------------------------------------------------------------
        # Step 1: the two column headers.
        # ------------------------------------------------------------------
        label_a = Text("your taste", font=FONT_BODY, font_size=30, color=TEXT)
        label_a.move_to([col_a_x, 2.8, 0])
        label_b = Text("this song", font=FONT_BODY, font_size=30, color=TEXT)
        label_b.move_to([col_b_x, 2.8, 0])

        self.wait(0.3)
        self.play(FadeIn(label_a, shift=DOWN * 0.2), FadeIn(label_b, shift=DOWN * 0.2), run_time=1.0)
        self.wait(0.3)

        # ------------------------------------------------------------------
        # Step 2: column A builds in, one number at a time.
        # ------------------------------------------------------------------
        col_a_texts = [
            Text(v, font=FONT_MONO, font_size=32, color=DATA_OBSERVED).move_to([col_a_x, y, 0])
            for v, y in zip(taste_vals, rows_y)
        ]
        self.play(LaggedStart(*[Write(t) for t in col_a_texts], lag_ratio=0.3), run_time=1.4)
        self.wait(0.3)

        # ------------------------------------------------------------------
        # Step 3: column B builds in beside it.
        # ------------------------------------------------------------------
        col_b_texts = [
            Text(v, font=FONT_MONO, font_size=32, color=DATA_OBSERVED).move_to([col_b_x, y, 0])
            for v, y in zip(song_vals, rows_y)
        ]
        self.play(LaggedStart(*[Write(t) for t in col_b_texts], lag_ratio=0.3), run_time=1.4)
        self.wait(0.3)

        # ------------------------------------------------------------------
        # Step 4: paired entries light up, row by row, joined by a short
        # connecting line in the same lists color.
        # ------------------------------------------------------------------
        connectors = []
        row_anims = []
        for a_txt, b_txt, y in zip(col_a_texts, col_b_texts, rows_y):
            line = Line(
                start=[col_a_x + 0.7, y, 0],
                end=[col_b_x - 0.7, y, 0],
                color=DATA_OBSERVED,
                stroke_width=3,
            )
            connectors.append(line)
            row_anims.append(
                AnimationGroup(
                    Create(line),
                    Indicate(a_txt, color=DATA_OBSERVED, scale_factor=1.25),
                    Indicate(b_txt, color=DATA_OBSERVED, scale_factor=1.25),
                )
            )
        self.play(LaggedStart(*row_anims, lag_ratio=0.35), run_time=2.0)
        self.wait(0.5)

        # ------------------------------------------------------------------
        # Step 5: the comparison lands as a single score readout, counting
        # up in the score color.
        # ------------------------------------------------------------------
        score_label = Text("score", font=FONT_BODY, font_size=30, color=TEXT)
        score_label.move_to([-5.0, -2.6, 0])

        score_tracker = ValueTracker(0.0)
        score_num = always_redraw(
            lambda: Text(
                f"{score_tracker.get_value():.2f}",
                font=FONT_MONO,
                font_size=40,
                color=DATA_PARAMS,
            ).next_to(score_label, RIGHT, buff=0.5)
        )

        self.play(FadeIn(score_label), FadeIn(score_num), run_time=1.0)
        self.wait(0.2)
        self.play(score_tracker.animate.set_value(0.87), run_time=3.0, rate_func=smooth)
        self.wait(0.5)

        # ------------------------------------------------------------------
        # Step 6: everything but the frozen score recedes.
        # ------------------------------------------------------------------
        fading_group = VGroup(label_a, label_b, *col_a_texts, *col_b_texts, *connectors)
        self.play(fading_group.animate.set_opacity(0.4), run_time=1.0)
        self.wait(0.3)

        # ------------------------------------------------------------------
        # Step 7: the question card claims the empty right half of the
        # frame, holding over the frozen score.
        # ------------------------------------------------------------------
        card_text = Text(
            "How do you score\ntwo lists of numbers?",
            font=FONT_HEADING,
            font_size=34,
            color=TEXT,
            line_spacing=1.2,
        )
        card_text.move_to([3.5, 0.3, 0])
        card_bg = RoundedRectangle(
            width=card_text.width + 1.2,
            height=card_text.height + 1.0,
            corner_radius=0.3,
        )
        card_bg.set_fill(SURFACE, opacity=1.0)
        card_bg.set_stroke(TEXT, width=2)
        card_bg.move_to(card_text.get_center())

        self.play(Create(card_bg), run_time=0.7)
        self.wait(0.2)
        self.play(Write(card_text), run_time=0.8)
        self.wait(6.3)
