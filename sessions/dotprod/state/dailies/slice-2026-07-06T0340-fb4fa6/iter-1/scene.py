import sys
from pathlib import Path

from manim import *  # noqa: F403

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "shared" / "manim"))
from bbox_dump import attach_bbox_dump  # noqa: E402
from colors import *  # noqa: E402,F403
from style import FONT_BODY, FONT_HEADING, FONT_MONO  # noqa: E402
from style import roughen, true_up, wobble_once  # noqa: E402

import numpy as np  # noqa: E402


class Beat03(Scene):
    def construct(self):
        attach_bbox_dump(self)
        self.camera.background_color = BG

        self.wait(2.5)

        # ---------------------------------------------------------------
        # Section A: three probe stills -- along, across, against
        # ---------------------------------------------------------------
        candidate_vec = np.array([0.8625, 0.9775, 0.0])
        probe_vecs = {
            "along": candidate_vec.copy(),
            "across": np.array([-candidate_vec[1], candidate_vec[0], 0.0]),
            "against": -candidate_vec,
        }
        scores = {"along": "10", "across": "0", "against": "-10"}
        centers_x = {"along": -4.5, "across": 0.0, "against": 4.5}
        wait_after = {"along": 1.8, "across": 2.1, "against": 2.3}
        panel_y = 0.9

        perp_unit = np.array([-candidate_vec[1], candidate_vec[0], 0.0])
        perp_unit = perp_unit / np.linalg.norm(perp_unit)
        perp_offset = perp_unit * 0.16

        panels = {}
        prev_group = None
        for key in ["along", "across", "against"]:
            c = np.array([centers_x[key], panel_y, 0.0])
            cand_arrow = Arrow(
                start=c,
                end=c + candidate_vec,
                buff=0,
                color=DATA_OBSERVED,
                stroke_width=6,
                max_tip_length_to_length_ratio=0.25,
            )
            probe_arrow = Arrow(
                start=c + perp_offset,
                end=c + perp_offset + probe_vecs[key],
                buff=0,
                color=DATA_HEAT,
                stroke_width=6,
                max_tip_length_to_length_ratio=0.25,
            )
            word = Text(key, font=FONT_BODY, font_size=28, color=TEXT)
            word.move_to(c + DOWN * 1.55)
            score = Text(scores[key], font=FONT_MONO, font_size=32, color=DATA_PARAMS)
            score.next_to(word, DOWN, buff=0.35)

            panels[key] = VGroup(cand_arrow, probe_arrow, word, score)

            if key == "along":
                self.play(Create(cand_arrow), Create(probe_arrow), run_time=1.3)
                cand_label = Text(
                    "candidate", font=FONT_BODY, font_size=24, color=DATA_OBSERVED
                )
                cand_label.move_to(c + UP * 1.5 + LEFT * 0.9)
                probe_label = Text("probe", font=FONT_BODY, font_size=24, color=DATA_HEAT)
                probe_label.move_to(c + UP * 1.5 + RIGHT * 0.9)
                self.play(
                    Write(word),
                    Write(score),
                    Write(cand_label),
                    Write(probe_label),
                    run_time=1.4,
                )
                panels[key].add(cand_label, probe_label)
            else:
                anims = [Create(cand_arrow), Create(probe_arrow), Write(word), Write(score)]
                if prev_group is not None:
                    anims.append(prev_group.animate.set_opacity(0.4))
                self.play(*anims, run_time=1.6)

            self.wait(wait_after[key])
            prev_group = panels[key]

        self.wait(0.4)

        all_panels = VGroup(*panels.values())
        dial_center = np.array([0.0, 1.9, 0.0])
        self.play(
            all_panels.animate.move_to(dial_center).scale(0.05).set_opacity(0.0),
            run_time=1.2,
        )
        self.remove(all_panels)

        # ---------------------------------------------------------------
        # Section B: the stills collapse into one lilac meter dial
        # ---------------------------------------------------------------
        radius = 1.1
        arc = Arc(radius=radius, start_angle=PI, angle=-PI, color=DATA_PARAMS, stroke_width=6)
        arc.move_arc_center_to(dial_center)
        pivot = Dot(dial_center, radius=0.06, color=DATA_PARAMS)
        self.play(Create(arc), Create(pivot), run_time=1.2)

        tick_oppose = Text("oppose", font=FONT_BODY, font_size=26, color=TEXT)
        tick_oppose.next_to(dial_center + LEFT * radius, LEFT, buff=0.25)
        tick_ignore = Text("ignore", font=FONT_BODY, font_size=26, color=TEXT)
        tick_ignore.next_to(dial_center + UP * radius, UP, buff=0.25)
        tick_agree = Text("agree", font=FONT_BODY, font_size=26, color=TEXT)
        tick_agree.next_to(dial_center + RIGHT * radius, RIGHT, buff=0.25)
        self.play(Write(tick_oppose), Write(tick_ignore), Write(tick_agree), run_time=1.4)

        needle = Line(
            dial_center, dial_center + LEFT * (radius - 0.15), color=DATA_HEAT, stroke_width=8
        )
        self.play(Create(needle), run_time=0.9)
        self.wait(0.8)

        self.play(Rotate(needle, angle=-PI / 2, about_point=dial_center), run_time=1.5)
        self.wait(0.7)
        self.play(Rotate(needle, angle=-PI / 2, about_point=dial_center), run_time=1.5)
        self.wait(2.3)

        dial_group = VGroup(arc, pivot, tick_oppose, tick_ignore, tick_agree, needle)
        self.play(FadeOut(dial_group), run_time=1.0)

        # ---------------------------------------------------------------
        # Section C: the aha sentence trues up
        # ---------------------------------------------------------------
        sentence = Text(
            "The dot product is\na similarity meter.",
            font=FONT_BODY,
            font_size=34,
            color=TEXT,
        )
        sentence.move_to(np.array([0.0, 1.6, 0.0]))
        underline = Line(LEFT * 3.2, RIGHT * 3.2, color=TEXT, stroke_width=4)
        underline.next_to(sentence, DOWN, buff=0.3)
        roughen(underline)

        self.play(Write(sentence), run_time=1.5)
        self.play(Create(underline), run_time=0.7)
        self.play(wobble_once(underline), run_time=0.35)
        self.play(true_up(underline, settle_color=DATA_FIT))
        self.play(sentence.animate.set_color(DATA_FIT), run_time=0.7)
        self.wait(4.5)

        # ---------------------------------------------------------------
        # Section D: the symbol, trued up next to the worked numbers
        # ---------------------------------------------------------------
        chip = Text(
            "(2, 1) · (1, 3) = 5",
            font=FONT_MONO,
            font_size=36,
            color=TEXT,
            t2c={"(2, 1)": DATA_HEAT, "(1, 3)": DATA_OBSERVED, "5": DATA_PARAMS},
        )
        annotation = Text("a · b", font=FONT_MONO, font_size=36, color=DATA_PARAMS)

        row = VGroup(annotation, chip).arrange(RIGHT, buff=0.9)
        row.move_to(np.array([0.0, -0.5, 0.0]))

        ann_underline = Line(LEFT * 0.55, RIGHT * 0.55, color=TEXT, stroke_width=4)
        ann_underline.next_to(annotation, DOWN, buff=0.2)
        roughen(ann_underline)

        self.play(
            Write(chip),
            sentence.animate.set_opacity(0.4),
            underline.animate.set_opacity(0.4),
            run_time=1.5,
        )
        self.wait(1.2)
        self.play(FadeIn(annotation, shift=UP * 0.2), Create(ann_underline), run_time=1.0)
        self.play(wobble_once(ann_underline), run_time=0.35)
        self.play(true_up(ann_underline, settle_color=DATA_PARAMS, glow_color=DATA_PARAMS))
        self.wait(4.0)

        # ---------------------------------------------------------------
        # Section E: the reading tracks direction -- a small callback
        # ---------------------------------------------------------------
        mini_center = np.array([0.0, -2.3, 0.0])
        mini_r = 0.55
        mini_arc = Arc(radius=mini_r, start_angle=PI, angle=-PI, color=DATA_PARAMS, stroke_width=5)
        mini_arc.move_arc_center_to(mini_center)
        mini_pivot = Dot(mini_center, radius=0.05, color=DATA_PARAMS)
        mini_needle = Line(
            mini_center,
            mini_center + LEFT * (mini_r - 0.1),
            color=DATA_HEAT,
            stroke_width=6,
        )
        self.play(Create(mini_arc), Create(mini_pivot), Create(mini_needle), run_time=1.1)
        self.wait(0.8)
        self.play(Rotate(mini_needle, angle=PI, about_point=mini_center), run_time=2.0)
        self.wait(5.5)
