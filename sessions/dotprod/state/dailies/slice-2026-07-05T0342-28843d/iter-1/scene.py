import sys
from pathlib import Path

from manim import *  # noqa: F403

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "shared" / "manim"))
from bbox_dump import attach_bbox_dump  # noqa: E402
from colors import *  # noqa: E402,F403
from style import FONT_BODY, FONT_HEADING, FONT_MONO  # noqa: E402

import numpy as np  # noqa: E402

# ---------------------------------------------------------------------------
# Shared geometry: one dial (the "meter") sits fixed at the right for the
# whole scene. Its needle direction never changes; only its readout number
# does. That is the whole point of the beat, made structural.
# ---------------------------------------------------------------------------

DIAL_CENTER = np.array([4.8, 1.6, 0.0])
DIAL_RADIUS = 0.9
READOUT_POS = np.array([4.8, 0.0, 0.0])
SCORE_LABEL_POS = np.array([4.8, -0.8, 0.0])


def make_dial() -> VGroup:
    arc = Arc(
        radius=DIAL_RADIUS, start_angle=PI, angle=-PI, arc_center=DIAL_CENTER,
        color=DATA_PARAMS, stroke_width=7,
    )
    pivot = Dot(DIAL_CENTER, radius=0.07, color=DATA_PARAMS)
    needle = Line(
        DIAL_CENTER, DIAL_CENTER + np.array([0.0, DIAL_RADIUS, 0.0]),
        color=DATA_PARAMS, stroke_width=6,
    )
    group = VGroup(arc, pivot, needle)
    group.set_opacity(0.35)
    return group


class Beat04(Scene):
    def construct(self):
        attach_bbox_dump(self)
        self.camera.background_color = BG

        # ===================================================================
        # PART A - the retrieval prompt holds as a card; the meter idles.
        # ===================================================================
        dial_group = make_dial()
        self.play(
            FadeIn(dial_group[0]), FadeIn(dial_group[1]), FadeIn(dial_group[2]),
            run_time=1.0,
        )

        card_center = np.array([-2.2, 0.3, 0.0])
        card_rect = RoundedRectangle(
            width=6.0, height=3.0, corner_radius=0.25,
            color=TEXT, fill_color=SURFACE, fill_opacity=0.5, stroke_width=2,
        ).move_to(card_center)
        self.play(Create(card_rect), run_time=0.8)

        arrow_a = Arrow(
            np.array([-4.7, 1.0, 0.0]), np.array([-3.1, 1.0, 0.0]),
            buff=0, color=DATA_OBSERVED, stroke_width=7,
            max_tip_length_to_length_ratio=0.2,
        )
        label_a = Text("a", font=FONT_BODY, font_size=28, color=TEXT)
        label_a.move_to(np.array([-4.95, 1.0, 0.0]))
        arrow_b = Arrow(
            np.array([-4.7, -0.4, 0.0]), np.array([-3.1, -0.4, 0.0]),
            buff=0, color=DATA_OBSERVED, stroke_width=7,
            max_tip_length_to_length_ratio=0.2,
        )
        label_b = Text("b", font=FONT_BODY, font_size=28, color=TEXT)
        label_b.move_to(np.array([-4.95, -0.4, 0.0]))
        self.play(
            GrowArrow(arrow_a), GrowArrow(arrow_b), Write(label_a), Write(label_b),
            run_time=1.5,
        )

        qmark = Text("?", font=FONT_HEADING, font_size=54, color=TEXT)
        qmark.move_to(np.array([-1.6, 0.3, 0.0]))
        self.play(Write(qmark), run_time=1.0)

        connect_arrow = Arrow(
            np.array([0.8, 0.3, 0.0]), np.array([3.6, 1.3, 0.0]),
            buff=0, color=DATA_PARAMS, stroke_width=6,
            max_tip_length_to_length_ratio=0.15,
        )
        self.play(GrowArrow(connect_arrow), run_time=1.0)
        self.wait(3.0)

        prompt_group = VGroup(card_rect, arrow_a, arrow_b, label_a, label_b, qmark, connect_arrow)
        self.play(FadeOut(prompt_group), run_time=1.0)

        # ===================================================================
        # PART B - detour: swap songs for a job posting. Same meter.
        # ===================================================================
        header_you = Text("you", font=FONT_BODY, font_size=32, color=TEXT)
        header_you.move_to(np.array([-2.6, 2.9, 0.0]))
        header_role = Text("the role", font=FONT_BODY, font_size=32, color=TEXT)
        header_role.move_to(np.array([0.0, 2.9, 0.0]))
        self.play(Write(header_you), Write(header_role), run_time=1.0)

        row_names = ["Python hours", "SQL reps", "nights free"]
        row_ys = [1.7, 0.6, -0.5]
        you_vals = [8, 5, 3]
        role_vals = [6, 4, 2]
        prods = [48, 20, 6]

        row_labels = [
            Text(name, font=FONT_BODY, font_size=26, color=TEXT).move_to(
                np.array([-5.5, y, 0.0])
            )
            for name, y in zip(row_names, row_ys)
        ]
        self.play(*[Write(t) for t in row_labels], run_time=1.2)

        you_texts = [
            Text(str(v), font=FONT_MONO, font_size=28, color=DATA_OBSERVED).move_to(
                np.array([-2.6, y, 0.0])
            )
            for v, y in zip(you_vals, row_ys)
        ]
        self.play(*[Write(t) for t in you_texts], run_time=1.2)

        role_texts = [
            Text(str(v), font=FONT_MONO, font_size=28, color=TEXT).move_to(
                np.array([0.0, y, 0.0])
            )
            for v, y in zip(role_vals, row_ys)
        ]
        self.play(*[Write(t) for t in role_texts], run_time=1.2)

        mult_texts = [
            Text("×", font=FONT_MONO, font_size=28, color=TEXT).move_to(
                np.array([-1.3, y, 0.0])
            )
            for y in row_ys
        ]
        self.play(*[Write(t) for t in mult_texts], run_time=1.0)

        prod_texts = [
            Text(str(p), font=FONT_MONO, font_size=28, color=DATA_PARAMS).move_to(
                np.array([2.6, y, 0.0])
            )
            for p, y in zip(prods, row_ys)
        ]
        self.play(*[Write(t) for t in prod_texts], run_time=1.2)

        plus_texts = [
            Text("+", font=FONT_MONO, font_size=26, color=TEXT).move_to(
                np.array([2.6, (row_ys[0] + row_ys[1]) / 2.0, 0.0])
            ),
            Text("+", font=FONT_MONO, font_size=26, color=TEXT).move_to(
                np.array([2.6, (row_ys[1] + row_ys[2]) / 2.0, 0.0])
            ),
        ]
        self.play(*[Write(t) for t in plus_texts], run_time=1.0)

        table_group = VGroup(
            header_you, header_role, *row_labels, *you_texts, *role_texts,
            *mult_texts, *prod_texts, *plus_texts,
        )

        pool_arrow = Arrow(
            np.array([2.9, 0.6, 0.0]), np.array([3.7, 1.4, 0.0]),
            buff=0, color=DATA_PARAMS, stroke_width=6,
            max_tip_length_to_length_ratio=0.15,
        )
        self.play(
            GrowArrow(pool_arrow),
            table_group.animate.set_opacity(0.4),
            dial_group.animate.set_opacity(1.0),
            run_time=1.2,
        )

        readout = Text("74", font=FONT_MONO, font_size=34, color=DATA_PARAMS)
        readout.move_to(READOUT_POS)
        score_label = Text("score", font=FONT_BODY, font_size=22, color=TEXT)
        score_label.move_to(SCORE_LABEL_POS)
        self.play(Write(readout), Write(score_label), run_time=1.2)
        self.wait(3.0)

        self.play(FadeOut(VGroup(table_group, pool_arrow)), run_time=1.0)
        self.play(
            FadeOut(readout), FadeOut(score_label),
            dial_group.animate.set_opacity(0.35),
            run_time=1.0,
        )

        # ===================================================================
        # PART C - guess card: one candidate outlined, score hidden.
        # ===================================================================
        cand_origin = np.array([-1.5, -0.3, 0.0])
        angle_deg = 55.0
        direction = np.array(
            [np.cos(np.radians(angle_deg)), np.sin(np.radians(angle_deg)), 0.0]
        )
        score_k = 5.0
        length_tracker = ValueTracker(1.6)

        def make_candidate(length: float) -> Arrow:
            return Arrow(
                cand_origin, cand_origin + length * direction,
                buff=0, color=DATA_OBSERVED, stroke_width=8,
                max_tip_length_to_length_ratio=0.15,
            )

        candidate_arrow = make_candidate(length_tracker.get_value())
        self.play(GrowArrow(candidate_arrow), run_time=1.0)
        candidate_arrow.add_updater(
            lambda m: m.become(make_candidate(length_tracker.get_value()))
        )

        outline = SurroundingRectangle(candidate_arrow, color=TEXT, buff=0.3, stroke_width=2.5)
        self.play(Create(outline), run_time=0.8)

        guess_label = Text("guess", font=FONT_BODY, font_size=28, color=TEXT)
        guess_label.move_to(np.array([-1.1, 1.7, 0.0]))
        self.play(Write(guess_label), run_time=0.8)
        self.wait(4.5)

        # ===================================================================
        # PART D - same direction, longer arrow: the score climbs anyway.
        # ===================================================================
        self.play(
            FadeOut(outline), FadeOut(guess_label),
            dial_group.animate.set_opacity(1.0),
            run_time=1.0,
        )

        def make_score_text(length: float) -> Text:
            value = round(score_k * length)
            t = Text(f"{value}", font=FONT_MONO, font_size=34, color=DATA_PARAMS)
            t.move_to(READOUT_POS)
            return t

        readout2 = make_score_text(length_tracker.get_value())
        score_label2 = Text("score", font=FONT_BODY, font_size=22, color=TEXT)
        score_label2.move_to(SCORE_LABEL_POS)
        self.play(FadeIn(readout2), FadeIn(score_label2), run_time=1.0)
        readout2.add_updater(
            lambda m: m.become(make_score_text(length_tracker.get_value()))
        )

        self.play(length_tracker.animate.set_value(3.6), run_time=6.0, rate_func=linear)
        readout2.clear_updaters()
        candidate_arrow.clear_updaters()
        self.wait(1.0)

        flag_pos = np.array([4.8, -1.6, 0.0])
        pole = Line(
            flag_pos + np.array([0.0, -0.25, 0.0]), flag_pos + np.array([0.0, 0.25, 0.0]),
            color=DATA_ERROR, stroke_width=4,
        )
        pennant = Polygon(
            flag_pos + np.array([0.0, 0.25, 0.0]),
            flag_pos + np.array([0.4, 0.12, 0.0]),
            flag_pos + np.array([0.0, 0.0, 0.0]),
            color=DATA_ERROR, fill_color=DATA_ERROR, fill_opacity=0.9, stroke_width=0,
        )
        flag_icon = VGroup(pole, pennant)
        flag_label = Text("size, not fit", font=FONT_BODY, font_size=24, color=DATA_ERROR)
        flag_label.move_to(flag_pos + np.array([0.0, -0.75, 0.0]))

        self.play(FadeIn(flag_icon), Write(flag_label), run_time=1.2)
        self.wait(3.5)

        # ===================================================================
        # PART E - the walk-home question lands as the closing card.
        # ===================================================================
        self.play(
            FadeOut(
                VGroup(candidate_arrow, dial_group, readout2, score_label2, flag_icon, flag_label)
            ),
            run_time=1.2,
        )

        card_rect2 = RoundedRectangle(
            width=7.6, height=3.2, corner_radius=0.25,
            color=TEXT, fill_color=SURFACE, fill_opacity=0.55, stroke_width=2,
        ).move_to(np.array([0.0, 0.4, 0.0]))
        self.play(Create(card_rect2), run_time=1.0)

        question_text = Text(
            "keep the direction.\ndrop the size.\nhow?",
            font=FONT_BODY, font_size=32, color=TEXT, line_spacing=1.2,
        )
        question_text.move_to(card_rect2.get_center())
        self.play(Write(question_text), run_time=1.5)
        self.wait(2.0)

        chip_rect = RoundedRectangle(
            width=3.6, height=0.9, corner_radius=0.2,
            color=TEXT, fill_color=SURFACE, fill_opacity=0.5, stroke_width=1.5,
        ).move_to(np.array([0.0, -2.6, 0.0]))
        chip_text = Text("extensions below", font=FONT_BODY, font_size=24, color=TEXT)
        chip_text.move_to(chip_rect.get_center())
        self.play(FadeIn(chip_rect), Write(chip_text), run_time=1.2)
        self.wait(6.0)
