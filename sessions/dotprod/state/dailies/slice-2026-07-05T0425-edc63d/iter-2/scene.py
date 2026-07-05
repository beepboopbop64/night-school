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
        # Layout: two symmetric feature stacks in the top half (periwinkle,
        # DATA_OBSERVED), converging arrows, and a lilac (DATA_PARAMS) match
        # readout card holding a bare question mark in the lower half. Every
        # row label is a real word (never bare punctuation) so its glyph
        # height always clears the readability floor. The bottom-most strip
        # of the frame stays empty on purpose.
        # ------------------------------------------------------------------
        x_left = -4.5
        x_right = 4.5
        header_y = 3.3
        row_ys = [2.5, 1.7, 0.9, 0.1, -0.7]
        features = ["loud", "fast", "sad", "bright", "more"]

        left_header = Text("LISTENER", font=FONT_HEADING, font_size=34, color=TEXT)
        left_header.move_to([x_left, header_y, 0])
        right_header = Text("SONG", font=FONT_HEADING, font_size=34, color=TEXT)
        right_header.move_to([x_right, header_y, 0])

        self.play(
            FadeIn(left_header, shift=DOWN * 0.2),
            FadeIn(right_header, shift=DOWN * 0.2),
            run_time=1.2,
        )
        self.wait(0.6)

        # Build the two lists row by row, pairing the same feature side by
        # side so the comparison reads directly off the layout. The last row
        # ("more") fades to half opacity to read as the list trailing off,
        # while remaining a full word so it stays legible.
        left_rows = []
        right_rows = []
        last_i = len(features) - 1
        for i, (feat, y) in enumerate(zip(features, row_ys)):
            fade = 0.5 if i == last_i else 1.0
            left_label = Text(feat, font=FONT_BODY, font_size=32, color=DATA_OBSERVED)
            left_label.set_opacity(fade)
            left_label.move_to([x_left, y, 0])
            right_label = Text(feat, font=FONT_BODY, font_size=32, color=DATA_OBSERVED)
            right_label.set_opacity(fade)
            right_label.move_to([x_right, y, 0])
            left_rows.append(left_label)
            right_rows.append(right_label)
            self.play(
                FadeIn(left_label, shift=RIGHT * 0.15),
                FadeIn(right_label, shift=LEFT * 0.15),
                run_time=0.8,
            )
            self.wait(0.4 if i < last_i else 0.6)

        left_group = VGroup(left_header, *left_rows)
        right_group = VGroup(right_header, *right_rows)

        # The unfilled match readout: a lilac card with a question mark
        # standing in for the number nobody has computed yet.
        rect = RoundedRectangle(
            width=3.0,
            height=1.3,
            corner_radius=0.18,
            color=DATA_PARAMS,
            stroke_width=4,
        )
        rect.move_to([0, -2.35, 0])

        arrow_left = Arrow(
            start=[x_left, -1.15, 0],
            end=rect.get_corner(UL) + RIGHT * 0.2 + DOWN * 0.05,
            color=DATA_OBSERVED,
            stroke_width=3,
            buff=0.05,
            max_tip_length_to_length_ratio=0.18,
        )
        arrow_right = Arrow(
            start=[x_right, -1.15, 0],
            end=rect.get_corner(UR) + LEFT * 0.2 + DOWN * 0.05,
            color=DATA_OBSERVED,
            stroke_width=3,
            buff=0.05,
            max_tip_length_to_length_ratio=0.18,
        )

        self.play(Create(arrow_left), Create(arrow_right), run_time=1.0)
        self.wait(0.4)

        self.play(Create(rect), run_time=1.2)
        self.wait(0.5)

        qmark = Text("?", font=FONT_MONO, font_size=72, color=DATA_PARAMS)
        qmark.move_to(rect.get_center())
        self.play(FadeIn(qmark, scale=0.6), run_time=1.0)

        # Focus shifts entirely onto the unanswered readout: the two lists
        # and their arrows recede, the card is the only thing left bright.
        arrows_group = VGroup(arrow_left, arrow_right)
        self.play(
            left_group.animate.set_opacity(0.4),
            right_group.animate.set_opacity(0.4),
            arrows_group.animate.set_opacity(0.4),
            rect.animate.set_stroke(width=6),
            run_time=1.0,
        )
        self.wait(2.0)

        self.play(Indicate(qmark, color=DATA_PARAMS, scale_factor=1.15), run_time=1.0)
        self.wait(3.0)

        self.play(Indicate(qmark, color=DATA_PARAMS, scale_factor=1.15), run_time=1.0)
        self.wait(4.3)
