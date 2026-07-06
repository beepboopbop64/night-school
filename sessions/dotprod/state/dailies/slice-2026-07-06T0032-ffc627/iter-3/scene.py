import sys
from pathlib import Path

from manim import *  # noqa: F403

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "shared" / "manim"))
from bbox_dump import attach_bbox_dump  # noqa: E402
from colors import *  # noqa: E402,F403
from style import FONT_BODY, FONT_HEADING, FONT_MONO  # noqa: E402

import numpy as np  # noqa: E402


def _tangle(seed: int, color: str) -> VMobject:
    """A small irregular squiggle: a stand-in for a messy raw signal."""
    rng = np.random.default_rng(seed)
    pts = [[rng.uniform(-0.22, 0.22), rng.uniform(-0.16, 0.16), 0.0] for _ in range(6)]
    path = VMobject(stroke_color=color, stroke_width=4)
    path.set_points_smoothly(pts)
    return path


class Beat05(Scene):
    def construct(self):
        attach_bbox_dump(self)
        self.camera.background_color = BG

        strip_y = 2.55
        xs = [-4.8, -1.6, 1.6, 4.8]

        # =========================================================
        # PART 1 -- the chain replays as four small stills, left to right
        # =========================================================

        # -- still 1: the two stacked tangles from the hook --
        song_icon = _tangle(1, TEXT)
        taste_icon = _tangle(2, TEXT)
        song_label = Text("song", font=FONT_BODY, font_size=24, color=TEXT)
        taste_label = Text("taste", font=FONT_BODY, font_size=24, color=TEXT)
        song_row = VGroup(song_icon, song_label).arrange(RIGHT, buff=0.3)
        taste_row = VGroup(taste_icon, taste_label).arrange(RIGHT, buff=0.3)
        still1 = VGroup(song_row, taste_row).arrange(DOWN, buff=0.35)
        still1.move_to([xs[0], strip_y, 0])

        self.play(
            Create(song_icon),
            Create(taste_icon),
            FadeIn(song_label),
            FadeIn(taste_label),
            run_time=2.2,
        )
        self.wait(0.6)

        # -- still 2: the arrows they folded into --
        conn1 = Arrow(
            still1.get_right(), [xs[1] - 0.9, strip_y, 0],
            buff=0.1, color=TEXT, stroke_width=2,
            max_tip_length_to_length_ratio=0.25,
        )
        song_vec = Arrow(
            [xs[1] - 0.35, strip_y + 0.25, 0], [xs[1] + 0.35, strip_y + 0.25, 0],
            buff=0, color=DATA_OBSERVED, stroke_width=5,
        )
        taste_vec = Arrow(
            [xs[1] - 0.3, strip_y - 0.25, 0], [xs[1] + 0.4, strip_y - 0.25, 0],
            buff=0, color=DATA_OBSERVED, stroke_width=5,
        )
        still2 = VGroup(song_vec, taste_vec)
        self.play(Create(conn1), Create(song_vec), Create(taste_vec), run_time=2.1)
        self.wait(0.5)

        # -- still 3: multiply-and-add pooling into one score bar --
        score_bar = Rectangle(
            width=0.5, height=0.9, fill_color=DATA_PARAMS, fill_opacity=1,
            stroke_color=DATA_PARAMS, stroke_width=2,
        ).move_to([xs[2], strip_y + 0.05, 0])
        score_label = Text("score", font=FONT_BODY, font_size=24, color=TEXT)
        score_label.next_to(score_bar, DOWN, buff=0.35)
        arrow_a = Arrow(
            song_vec.get_right(), [xs[2] - 0.35, strip_y + 0.1, 0],
            buff=0.05, color=TEXT, stroke_width=2,
            max_tip_length_to_length_ratio=0.3,
        )
        arrow_b = Arrow(
            taste_vec.get_right(), [xs[2] - 0.35, strip_y - 0.05, 0],
            buff=0.05, color=TEXT, stroke_width=2,
            max_tip_length_to_length_ratio=0.3,
        )
        still3 = VGroup(score_bar, score_label)
        self.play(
            Create(arrow_a), Create(arrow_b),
            FadeIn(score_bar), FadeIn(score_label),
            run_time=2.1,
        )
        self.wait(0.5)

        # -- still 4: the meter dial with a hairline rose crack --
        conn3 = Arrow(
            still3.get_right(), [xs[3] - 0.75, strip_y, 0],
            buff=0.1, color=TEXT, stroke_width=2,
            max_tip_length_to_length_ratio=0.25,
        )
        dial = Circle(radius=0.55, color=TEXT, stroke_width=3).move_to([xs[3], strip_y, 0])
        needle = Line(dial.get_center(), dial.get_center() + UP * 0.45, color=DATA_PARAMS, stroke_width=4)
        needle.rotate(-0.5, about_point=dial.get_center())
        crack = VMobject(stroke_color=DATA_ERROR, stroke_width=3)
        crack.set_points_as_corners([
            dial.get_center() + np.array([0.12, 0.5, 0]),
            dial.get_center() + np.array([0.0, 0.2, 0]),
            dial.get_center() + np.array([0.16, 0.0, 0]),
        ])
        still4 = VGroup(dial, needle, crack)
        self.play(
            Create(conn3), Create(dial), Create(needle), Create(crack),
            run_time=2.2,
        )
        self.wait(1.0)

        connectors = VGroup(conn1, arrow_a, arrow_b, conn3)
        self.play(
            VGroup(still1, still2, still3, connectors).animate.set_opacity(0.4),
            run_time=1.3,
        )
        self.wait(0.3)

        # =========================================================
        # PART 2 -- one more aisle: score yourself against a job posting
        # =========================================================

        col_you = Rectangle(
            width=2.0, height=1.4, stroke_color=DATA_OBSERVED, stroke_width=2, fill_opacity=0,
        ).move_to([-2.3, -0.3, 0])
        col_post = Rectangle(
            width=2.0, height=1.4, stroke_color=DATA_OBSERVED, stroke_width=2, fill_opacity=0,
        ).move_to([2.3, -0.3, 0])
        header_you = Text("you", font=FONT_BODY, font_size=28, color=TEXT)
        header_you.next_to(col_you, UP, buff=0.35)
        header_post = Text("the posting", font=FONT_BODY, font_size=28, color=TEXT)
        header_post.next_to(col_post, UP, buff=0.35)

        panel_box = SurroundingRectangle(
            VGroup(col_you, col_post, header_you, header_post), buff=0.5, color=TEXT,
        )
        panel_box.set_fill(SURFACE, opacity=1)
        panel_box.set_stroke(TEXT, width=2)

        aside_frame = VGroup(panel_box, col_you, col_post)
        aside_frame.shift(RIGHT * 11)
        self.play(aside_frame.animate.shift(LEFT * 11), run_time=2.1)
        self.wait(0.3)

        self.play(FadeIn(header_you), FadeIn(header_post), run_time=1.3)
        self.wait(0.5)

        row_ys = [0.1, -0.3, -0.7]
        you_vals = [0.6, 0.9, 0.5]
        post_vals = [0.8, 0.6, 0.9]

        you_left = col_you.get_left()[0]
        you_bars = VGroup()
        for y, v in zip(row_ys, you_vals):
            bar = Rectangle(
                width=v, height=0.22, fill_color=DATA_OBSERVED, fill_opacity=1, stroke_width=0,
            ).move_to([you_left + v / 2, y, 0])
            you_bars.add(bar)
        self.play(*[Create(b) for b in you_bars], run_time=1.6)
        self.wait(0.3)

        post_right = col_post.get_right()[0]
        post_bars = VGroup()
        for y, v in zip(row_ys, post_vals):
            bar = Rectangle(
                width=v, height=0.22, fill_color=DATA_OBSERVED, fill_opacity=1, stroke_width=0,
            ).move_to([post_right - v / 2, y, 0])
            post_bars.add(bar)
        self.play(*[Create(b) for b in post_bars], run_time=1.6)
        self.wait(0.5)

        mult_syms = VGroup()
        for y in row_ys:
            sym = Text("×", font=FONT_BODY, font_size=28, color=TEXT).move_to([0, y, 0])
            mult_syms.add(sym)
        self.play(*[FadeIn(s) for s in mult_syms], run_time=1.3)
        self.wait(0.5)

        pooled_dot = Dot(point=[0, row_ys[1], 0], radius=0.12, color=DATA_PARAMS)
        self.play(
            ReplacementTransform(VGroup(you_bars, post_bars, mult_syms), pooled_dot),
            run_time=2.1,
        )
        self.wait(0.3)

        arrow_to_dial = CurvedArrow(
            pooled_dot.get_center(), dial.get_bottom() + DOWN * 0.15,
            color=DATA_PARAMS, stroke_width=3, angle=-0.9,
        )
        self.play(Create(arrow_to_dial), run_time=1.6)
        self.wait(0.3)

        fit_text = Text("0.82", font=FONT_MONO, font_size=32, color=DATA_PARAMS)
        fit_text.next_to(dial, RIGHT, buff=0.35)
        self.play(
            Rotate(needle, angle=0.4, about_point=dial.get_center()),
            FadeIn(fit_text),
            Indicate(crack, color=DATA_ERROR, scale_factor=1.2),
            run_time=1.9,
        )
        self.wait(1.0)

        # =========================================================
        # PART 3 -- the aside slides out, blank columns invite your own pair
        # =========================================================

        self.play(
            panel_box.animate.shift(RIGHT * 11).set_opacity(0),
            FadeOut(pooled_dot),
            FadeOut(arrow_to_dial),
            FadeOut(header_you),
            FadeOut(header_post),
            run_time=2.1,
        )
        self.wait(0.5)

        invitation = Text(
            "Two matching lists of your own", font=FONT_BODY, font_size=28, color=TEXT,
        )
        invitation.next_to(VGroup(col_you, col_post), UP, buff=0.4)
        self.play(FadeIn(invitation), run_time=1.6)
        self.wait(0.8)

        # =========================================================
        # PART 4 -- the walk home, and a chip toward what's next
        # =========================================================

        everything_so_far = VGroup(
            still1, still2, still3, still4, connectors, fit_text,
            invitation, col_you, col_post,
        )
        # Dim the recap in place -- no repositioning, so nothing that was
        # already safely inside the frame can be pushed out of it. The
        # column layout above already leaves a generous, pre-measured gap
        # below the columns (bottom edge at y=-1.0) for the walk-home card.
        self.play(everything_so_far.animate.set_opacity(0.35), run_time=1.3)
        self.wait(0.3)

        # Lay out the walk-home card entirely within the open band below
        # the columns (y roughly -1.4 to -3.6), well clear of the frame's
        # bottom edge (y=-4) and of the dimmed columns above (y=-1.0).
        header2 = Text("For the walk home", font=FONT_HEADING, font_size=32, color=TEXT)
        header2.next_to(VGroup(col_you, col_post), DOWN, buff=0.4)

        question = VGroup(
            Text("What's the cheapest fix", font=FONT_BODY, font_size=26, color=TEXT),
            Text("that keeps the direction, forgets the size?", font=FONT_BODY, font_size=26, color=TEXT),
        ).arrange(DOWN, buff=0.2)
        question.next_to(header2, DOWN, buff=0.35)

        chip = Triangle(color=TEXT, fill_color=TEXT, fill_opacity=0.5, stroke_width=0)
        chip.scale(0.15).rotate(PI)
        chip.next_to(question, DOWN, buff=0.35)

        self.play(Write(header2), run_time=1.6)
        self.wait(0.5)

        self.play(FadeIn(question), run_time=1.6)
        self.wait(0.8)

        self.play(FadeIn(chip), run_time=1.3)
        self.wait(0.7)
