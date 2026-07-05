import sys
from pathlib import Path

from manim import *  # noqa: F403

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "shared" / "manim"))
from bbox_dump import attach_bbox_dump  # noqa: E402
from colors import *  # noqa: E402,F403
from style import FONT_BODY, FONT_HEADING, FONT_MONO  # noqa: E402


def make_ruler(row: Text) -> VGroup:
    """A short horizontal ruler that lies against a single row, never a stack."""
    width = row.width + 0.3
    center = row.get_center() + DOWN * 0.35
    bar = Line(LEFT * width / 2, RIGHT * width / 2, color=TEXT, stroke_width=3)
    tick_l = Line(UP * 0.09, DOWN * 0.09, color=TEXT, stroke_width=3)
    tick_r = Line(UP * 0.09, DOWN * 0.09, color=TEXT, stroke_width=3)
    ruler = VGroup(bar, tick_l, tick_r)
    ruler.move_to(center)
    tick_l.move_to(ruler[0].get_left())
    tick_r.move_to(ruler[0].get_right())
    return ruler


def make_x_mark(position, size: float = 0.16) -> VGroup:
    """A drawn cross, not a font glyph, so it never depends on font coverage."""
    l1 = Line(UP * size + LEFT * size, DOWN * size + RIGHT * size, color=TEXT, stroke_width=4)
    l2 = Line(UP * size + RIGHT * size, DOWN * size + LEFT * size, color=TEXT, stroke_width=4)
    mark = VGroup(l1, l2)
    mark.move_to(position)
    return mark


class Beat01(Scene):
    def construct(self):
        attach_bbox_dump(self)
        self.camera.background_color = BG

        features = ["loud", "fast", "sad", "bright"]
        row_ys = [2.3, 1.4, 0.5, -0.4]
        trail_y = -1.4
        left_x = -4.6
        right_x = 4.6

        # --- headers: name the two exact things being compared ---
        taste_header = Text("your taste", font=FONT_BODY, color=TEXT, font_size=30)
        taste_header.move_to([left_x, 3.3, 0])
        song_header = Text("this song", font=FONT_BODY, color=TEXT, font_size=30)
        song_header.move_to([right_x, 3.3, 0])

        self.play(FadeIn(taste_header), FadeIn(song_header), run_time=1.0)
        self.wait(1.0)

        # --- build the left stack, one row per feature ---
        left_rows = VGroup(*[
            Text(word, font=FONT_BODY, color=DATA_OBSERVED, font_size=28).move_to([left_x, y, 0])
            for word, y in zip(features, row_ys)
        ])
        self.play(LaggedStart(*[Write(r) for r in left_rows], lag_ratio=0.3), run_time=2.4)
        self.wait(0.8)

        left_trail = Text("and more", font=FONT_BODY, color=DATA_OBSERVED, font_size=28)
        left_trail.move_to([left_x, trail_y, 0])
        self.play(FadeIn(left_trail), run_time=0.5)
        self.wait(0.6)

        # --- build the right stack, the same features for the song ---
        right_rows = VGroup(*[
            Text(word, font=FONT_BODY, color=DATA_OBSERVED, font_size=28).move_to([right_x, y, 0])
            for word, y in zip(features, row_ys)
        ])
        self.play(LaggedStart(*[Write(r) for r in right_rows], lag_ratio=0.3), run_time=2.4)
        self.wait(0.8)

        right_trail = Text("and more", font=FONT_BODY, color=DATA_OBSERVED, font_size=28)
        right_trail.move_to([right_x, trail_y, 0])
        self.play(FadeIn(right_trail), run_time=0.5)
        self.wait(0.8)

        # --- a single ruler, laid against one row at a time, never the stack ---
        ruler = make_ruler(left_rows[0])
        self.play(
            Create(ruler),
            left_rows[1].animate.set_opacity(0.4),
            left_rows[2].animate.set_opacity(0.4),
            left_rows[3].animate.set_opacity(0.4),
            right_rows.animate.set_opacity(0.4),
            left_trail.animate.set_opacity(0.4),
            right_trail.animate.set_opacity(0.4),
            run_time=1.2,
        )
        self.wait(0.6)

        for i in range(4):
            # the ruler settles against this row on the taste side
            dim_left = [
                left_rows[j].animate.set_opacity(0.4 if j != i else 1.0)
                for j in range(4)
            ]
            self.play(
                Transform(ruler, make_ruler(left_rows[i])),
                *dim_left,
                right_rows[i].animate.set_opacity(0.4),
                run_time=0.7,
            )
            self.wait(0.2)

            # the same ruler tries the matching row on the song side
            self.play(
                Transform(ruler, make_ruler(right_rows[i])),
                right_rows[i].animate.set_opacity(1.0),
                left_rows[i].animate.set_opacity(0.4),
                run_time=0.7,
            )

            mark = make_x_mark([0, row_ys[i], 0])
            self.play(FadeIn(mark), run_time=0.35)
            self.wait(0.35)
            self.play(FadeOut(mark), right_rows[i].animate.set_opacity(0.4), run_time=0.35)

        # --- clear the tangle: the puzzle takes over the empty frame ---
        everything = VGroup(
            taste_header, song_header, left_rows, right_rows, left_trail, right_trail, ruler
        )
        self.play(FadeOut(everything), run_time=1.0)
        self.wait(0.6)

        match_label = Text("match:", font=FONT_BODY, color=TEXT, font_size=36)
        qmark = Text("?", font=FONT_MONO, color=DATA_PARAMS, font_size=48)
        readout = VGroup(match_label, qmark).arrange(RIGHT, buff=0.35)
        readout.move_to([0, -1.2, 0])

        self.play(Write(match_label), Write(qmark), run_time=1.2)
        self.wait(1.0)

        question_text = Text(
            "How do many features\nbecome one match number?",
            font=FONT_BODY,
            color=TEXT,
            font_size=30,
            line_spacing=1.2,
        )
        question_text.move_to([0, 1.3, 0])
        card = RoundedRectangle(
            width=question_text.width + 1.2,
            height=question_text.height + 1.0,
            corner_radius=0.25,
            color=TEXT,
            stroke_width=3,
            fill_opacity=0,
        )
        card.move_to(question_text.get_center())

        self.play(Create(card), Write(question_text), run_time=1.5)
        self.wait(2.0)

        self.play(Indicate(qmark, scale_factor=1.15, color=DATA_PARAMS), run_time=1.0)
        self.wait(6.0)
        self.play(Indicate(card, scale_factor=1.03, color=TEXT), run_time=1.0)
        self.wait(6.0)
        self.play(Indicate(question_text, scale_factor=1.02, color=TEXT), run_time=1.0)
        self.wait(14.4)
