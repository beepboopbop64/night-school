import sys
from pathlib import Path

from manim import *  # noqa: F403

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "shared" / "manim"))
from bbox_dump import attach_bbox_dump  # noqa: E402
from colors import *  # noqa: E402,F403
from style import FONT_BODY, FONT_HEADING, FONT_MONO  # noqa: E402

import numpy as np  # noqa: E402


def _fit(mob, max_w):
    if mob.width > max_w:
        mob.scale_to_fit_width(max_w)
    return mob


def _bar(left_x, y, value, scale, height, color, filled=True):
    width = max(value * scale, 0.08)
    rect = Rectangle(width=width, height=height)
    if filled:
        rect.set_fill(color, opacity=1.0)
        rect.set_stroke(width=0)
    else:
        rect.set_fill(color, opacity=0.35)
        rect.set_stroke(color=color, width=3)
    rect.move_to(np.array([left_x + width / 2.0, y, 0.0]))
    return rect


class Beat04(Scene):
    def construct(self):
        attach_bbox_dump(self)
        self.camera.background_color = BG

        # ------------------------------------------------------------------
        # Section 1: the retrieval prompt holds as a card, the meter idles.
        # ------------------------------------------------------------------
        card_bg = RoundedRectangle(width=4.6, height=0.75, corner_radius=0.12)
        card_bg.set_fill(SURFACE, opacity=1.0)
        card_bg.set_stroke(TEXT, width=2)
        card_bg.move_to(np.array([0.0, 3.55, 0.0]))
        card_text = Text("retrieval prompt", font=FONT_BODY, font_size=28, color=TEXT)
        _fit(card_text, 4.0)
        card_text.move_to(card_bg.get_center())

        self.play(FadeIn(card_bg), FadeIn(card_text), run_time=1.2)
        self.wait(1.0)

        dial_center = np.array([0.0, -2.7, 0.0])
        dial_radius = 0.85
        arc = Arc(
            radius=dial_radius,
            start_angle=PI,
            angle=-PI,
            arc_center=dial_center,
            color=DATA_PARAMS,
            stroke_width=7,
        )
        pivot = Dot(dial_center, radius=0.07, color=DATA_PARAMS)
        needle = Line(
            dial_center,
            dial_center + UP * 0.72,
            color=DATA_PARAMS,
            stroke_width=6,
        )

        self.play(Create(arc), FadeIn(pivot), Create(needle), run_time=1.2)
        self.wait(1.2)

        song_you_tag = Text("song A", font=FONT_BODY, font_size=26, color=TEXT)
        song_role_tag = Text("song B", font=FONT_BODY, font_size=26, color=TEXT)
        song_you_tag.move_to(np.array([-4.7, 2.1, 0.0]))
        song_role_tag.move_to(np.array([-4.7, 1.65, 0.0]))

        self.play(FadeIn(song_you_tag), FadeIn(song_role_tag), run_time=1.0)
        self.wait(1.8)

        # ------------------------------------------------------------------
        # Section 2: swap songs for a job posting; matched entries multiply
        # and pool into the same lilac readout on the same dial.
        # ------------------------------------------------------------------
        you_tag = song_you_tag
        role_tag = song_role_tag
        you_tag_target = Text("you", font=FONT_BODY, font_size=26, color=TEXT)
        you_tag_target.move_to(song_you_tag.get_center())
        role_tag_target = Text("the role", font=FONT_BODY, font_size=26, color=TEXT)
        role_tag_target.move_to(song_role_tag.get_center())

        self.play(
            Transform(you_tag, you_tag_target),
            Transform(role_tag, role_tag_target),
            card_bg.animate.set_opacity(0.4),
            card_text.animate.set_opacity(0.4),
            run_time=1.0,
        )
        self.wait(0.8)

        categories = ["Python hours", "SQL reps", "nights free"]
        you_vals = [6, 4, 5]
        role_vals = [5, 4, 6]
        row_y = [2.1, 0.5, -1.1]
        baseline_x = -3.6
        scale = 0.3
        bar_h = 0.3
        role_off = -0.45
        label_x = -2.7

        labels = []
        you_bars = []
        role_bars = []
        val_yous = []
        val_roles = []

        for i in range(3):
            lbl = Text(categories[i], font=FONT_BODY, font_size=26, color=TEXT)
            lbl.move_to(np.array([label_x, row_y[i] + 0.55, 0.0]))
            labels.append(lbl)

            yb = _bar(baseline_x, row_y[i], you_vals[i], scale, bar_h, DATA_OBSERVED, filled=True)
            rb = _bar(
                baseline_x, row_y[i] + role_off, role_vals[i], scale, bar_h, DATA_OBSERVED, filled=False
            )
            you_bars.append(yb)
            role_bars.append(rb)

            vy = Text(str(you_vals[i]), font=FONT_MONO, font_size=24, color=TEXT)
            vy.next_to(yb, RIGHT, buff=0.3)
            vr = Text(str(role_vals[i]), font=FONT_MONO, font_size=24, color=TEXT)
            vr.next_to(rb, RIGHT, buff=0.3)
            val_yous.append(vy)
            val_roles.append(vr)

        self.play(FadeIn(labels[0]), Create(you_bars[0]), Create(role_bars[0]), run_time=1.1)
        self.wait(0.6)
        self.play(FadeIn(val_yous[0]), FadeIn(val_roles[0]), run_time=0.8)
        self.wait(0.6)
        self.play(FadeIn(labels[1]), Create(you_bars[1]), Create(role_bars[1]), run_time=1.1)
        self.play(FadeIn(val_yous[1]), FadeIn(val_roles[1]), run_time=0.8)
        self.play(FadeIn(labels[2]), Create(you_bars[2]), Create(role_bars[2]), run_time=1.1)
        self.play(FadeIn(val_yous[2]), FadeIn(val_roles[2]), run_time=0.8)
        self.wait(1.2)

        dots = []
        for i in range(3):
            d = Dot(you_bars[i].get_right() + RIGHT * 0.55, radius=0.09, color=DATA_PARAMS)
            dots.append(d)

        self.play(Create(dots[0]), Create(dots[1]), Create(dots[2]), run_time=0.9)
        self.play(
            dots[0].animate.move_to(dial_center),
            dots[1].animate.move_to(dial_center),
            dots[2].animate.move_to(dial_center),
            needle.animate.rotate(np.radians(-55), about_point=dial_center),
            run_time=1.2,
        )

        score1 = sum(y * r for y, r in zip(you_vals, role_vals))
        readout = Text(f"{score1}", font=FONT_MONO, font_size=34, color=DATA_PARAMS)
        readout.move_to(dial_center + RIGHT * 1.7)
        fit_label = Text("fit score", font=FONT_BODY, font_size=24, color=TEXT)
        fit_label.next_to(readout, DOWN, buff=0.35)

        self.play(FadeOut(dots[0]), FadeOut(dots[1]), FadeOut(dots[2]), Write(readout), run_time=1.0)
        self.play(FadeIn(fit_label), run_time=0.6)
        self.wait(1.4)

        # ------------------------------------------------------------------
        # Section 3: stretch a candidate longer; score climbs, direction
        # never moved. Flag the unearned win.
        # ------------------------------------------------------------------
        dim_group = VGroup(
            card_bg,
            card_text,
            you_tag,
            role_tag,
            labels[0],
            labels[1],
            labels[2],
            role_bars[0],
            role_bars[1],
            role_bars[2],
            val_yous[0],
            val_yous[1],
            val_yous[2],
            val_roles[0],
            val_roles[1],
            val_roles[2],
        )
        self.play(dim_group.animate.set_opacity(0.4), run_time=1.0)
        self.wait(1.0)

        ghosts = []
        for i in range(3):
            edge_x = you_bars[i].get_right()[0]
            g = Line(
                np.array([edge_x, row_y[i] - 0.35, 0.0]),
                np.array([edge_x, row_y[i] + 0.35, 0.0]),
                color=TEXT,
                stroke_width=3,
            )
            g.set_stroke(opacity=0.5)
            ghosts.append(g)

        self.play(Create(ghosts[0]), Create(ghosts[1]), Create(ghosts[2]), run_time=0.8)

        direction_label = Text("direction fixed", font=FONT_BODY, font_size=26, color=TEXT)
        direction_label.move_to(np.array([0.6, 0.5, 0.0]))
        self.play(FadeIn(direction_label), run_time=0.8)
        self.wait(1.0)

        stretch_factor = 1.8
        you_vals2 = [round(v * stretch_factor, 1) for v in you_vals]
        new_bars = [
            _bar(baseline_x, row_y[i], you_vals2[i], scale, bar_h, DATA_OBSERVED, filled=True)
            for i in range(3)
        ]
        score2 = round(sum(y * r for y, r in zip(you_vals2, role_vals)))
        new_readout = Text(f"{score2}", font=FONT_MONO, font_size=34, color=DATA_PARAMS)
        new_readout.move_to(readout.get_center())

        self.play(
            Transform(you_bars[0], new_bars[0]),
            Transform(you_bars[1], new_bars[1]),
            Transform(you_bars[2], new_bars[2]),
            Transform(readout, new_readout),
            needle.animate.rotate(np.radians(-20), about_point=dial_center),
            run_time=1.8,
        )
        self.wait(2.0)

        flag_mark = Triangle(color=DATA_ERROR, fill_opacity=1.0, stroke_width=0)
        flag_mark.scale(0.14)
        flag_mark.rotate(np.radians(90))
        flag_mark.move_to(readout.get_center() + UP * 0.7 + LEFT * 0.3)
        flag_text = Text("size, not fit", font=FONT_BODY, font_size=26, color=DATA_ERROR)
        flag_text.next_to(flag_mark, RIGHT, buff=0.25)

        self.play(FadeIn(flag_mark), FadeIn(flag_text), run_time=1.0)
        self.wait(4.5)

        # ------------------------------------------------------------------
        # Section 4: the walk-home question, and a quiet chip to the menu.
        # ------------------------------------------------------------------
        everything = VGroup(
            card_bg,
            card_text,
            arc,
            pivot,
            needle,
            you_tag,
            role_tag,
            labels[0],
            labels[1],
            labels[2],
            you_bars[0],
            you_bars[1],
            you_bars[2],
            role_bars[0],
            role_bars[1],
            role_bars[2],
            val_yous[0],
            val_yous[1],
            val_yous[2],
            val_roles[0],
            val_roles[1],
            val_roles[2],
            readout,
            fit_label,
            ghosts[0],
            ghosts[1],
            ghosts[2],
            direction_label,
            flag_mark,
            flag_text,
        )
        self.play(FadeOut(everything), run_time=1.0)
        self.wait(0.6)

        card_bg2 = RoundedRectangle(width=8.0, height=3.6, corner_radius=0.2)
        card_bg2.set_fill(SURFACE, opacity=1.0)
        card_bg2.set_stroke(TEXT, width=2)
        card_bg2.move_to(ORIGIN)

        self.play(Create(card_bg2), run_time=1.0)

        long_arrow = Arrow(
            np.array([-2.0, 1.0, 0.0]),
            np.array([0.6, 1.0, 0.0]),
            buff=0,
            color=DATA_OBSERVED,
            stroke_width=7,
            tip_length=0.2,
        )
        short_arrow = Arrow(
            np.array([-2.0, 0.35, 0.0]),
            np.array([-1.1, 0.35, 0.0]),
            buff=0,
            color=DATA_OBSERVED,
            stroke_width=7,
            tip_length=0.2,
        )
        self.play(GrowArrow(long_arrow), GrowArrow(short_arrow), run_time=1.0)

        question_text = Text(
            "Keep the direction. Drop the size. How?",
            font=FONT_BODY,
            font_size=32,
            color=TEXT,
        )
        _fit(question_text, 6.8)
        question_text.move_to(np.array([0.0, -1.0, 0.0]))
        self.play(Write(question_text), run_time=1.5)
        self.wait(1.8)

        chip_bg = RoundedRectangle(width=3.2, height=0.6, corner_radius=0.15)
        chip_bg.set_fill(SURFACE, opacity=0.9)
        chip_bg.set_stroke(TEXT, width=1.5)
        chip_bg.move_to(np.array([4.4, -3.0, 0.0]))
        chip_text = Text("3 ways below", font=FONT_BODY, font_size=24, color=TEXT)
        _fit(chip_text, 2.8)
        chip_text.move_to(chip_bg.get_center())
        chip_text.set_opacity(0.85)
        chip_bg.set_opacity(0.85)
        chip_arrow = Arrow(
            chip_bg.get_bottom(),
            chip_bg.get_bottom() + DOWN * 0.4,
            buff=0.05,
            color=TEXT,
            stroke_width=3,
            tip_length=0.15,
        )
        chip_arrow.set_opacity(0.7)

        self.play(FadeIn(chip_bg), FadeIn(chip_text), GrowArrow(chip_arrow), run_time=1.0)
        self.wait(7.4)
