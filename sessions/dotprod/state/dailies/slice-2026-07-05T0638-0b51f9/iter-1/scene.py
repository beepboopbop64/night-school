import sys
from pathlib import Path

from manim import *  # noqa: F403

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "shared" / "manim"))
from bbox_dump import attach_bbox_dump  # noqa: E402
from colors import *  # noqa: E402,F403
from style import FONT_BODY, FONT_HEADING, FONT_MONO  # noqa: E402

import numpy as np  # noqa: E402

# ---------------------------------------------------------------------------
# The persistent meter: same pivot, same static needle, all scene long.
# Only the lilac readout at its foot ever changes.
# ---------------------------------------------------------------------------
PIVOT = np.array([0.0, -2.1, 0.0])
RADIUS = 1.0
READOUT_POS = PIVOT + DOWN * 0.85


def build_meter():
    arc = Arc(
        radius=RADIUS,
        start_angle=PI,
        angle=-PI,
        arc_center=PIVOT,
        color=DATA_PARAMS,
        stroke_width=7,
    )
    pivot_dot = Dot(PIVOT, radius=0.07, color=DATA_PARAMS)
    needle_angle = np.radians(55.0)
    tip = PIVOT + RADIUS * 0.95 * np.array(
        [np.cos(needle_angle), np.sin(needle_angle), 0.0]
    )
    needle = Line(PIVOT, tip, color=DATA_PARAMS, stroke_width=8)
    return arc, pivot_dot, needle


class Beat04(Scene):
    def construct(self):
        attach_bbox_dump(self)
        self.camera.background_color = BG

        # ------------------------------------------------------------------
        # Segment A: the retrieval prompt holds as a card, meter idles
        # ------------------------------------------------------------------
        title = Text("retrieval prompt", font=FONT_HEADING, font_size=32, color=TEXT)
        subtitle = Text("resume -> job posting", font=FONT_MONO, font_size=26, color=TEXT)
        card_content = VGroup(title, subtitle).arrange(DOWN, buff=0.32)
        card_content.move_to(np.array([0.0, 2.3, 0.0]))
        card_rect = RoundedRectangle(
            corner_radius=0.22,
            width=card_content.width + 1.2,
            height=card_content.height + 0.9,
            fill_color=SURFACE,
            fill_opacity=0.95,
            stroke_color=TEXT,
            stroke_width=1.5,
        )
        card_rect.move_to(card_content.get_center())

        self.play(FadeIn(card_rect), FadeIn(title), FadeIn(subtitle), run_time=1.4)

        arc, pivot_dot, needle = build_meter()
        readout_text = Text("--", font=FONT_MONO, font_size=32, color=DATA_PARAMS)
        readout_text.move_to(READOUT_POS)

        self.play(
            Create(arc),
            FadeIn(pivot_dot),
            GrowFromPoint(needle, PIVOT),
            FadeIn(readout_text),
            run_time=1.6,
        )
        self.wait(4.0)
        self.play(FadeOut(card_rect), FadeOut(title), FadeOut(subtitle), run_time=1.0)
        self.wait(1.0)

        # ------------------------------------------------------------------
        # Segment B: same meter, one aisle over -- "you" vs "the role"
        # ------------------------------------------------------------------
        you_header = Text("you", font=FONT_BODY, font_size=30, color=DATA_OBSERVED)
        you_header.move_to(np.array([-0.9, 3.0, 0.0]))
        role_header = Text("the role", font=FONT_BODY, font_size=30, color=TEXT)
        role_header.move_to(np.array([0.9, 3.0, 0.0]))
        self.play(FadeIn(you_header), FadeIn(role_header), run_time=1.0)

        rows_data = [
            ("python hours", 9, 8, 2.1),
            ("sql reps", 6, 7, 1.3),
            ("nights free", 3, 2, 0.5),
        ]
        row_mobs = []
        for label_str, you_v, role_v, y in rows_data:
            label = Text(label_str, font=FONT_BODY, font_size=26, color=TEXT)
            label.move_to(np.array([-4.4, y, 0.0]))
            you_val = Text(str(you_v), font=FONT_MONO, font_size=28, color=DATA_OBSERVED)
            you_val.move_to(np.array([-0.9, y, 0.0]))
            times = Text("×", font=FONT_MONO, font_size=28, color=TEXT)
            times.move_to(np.array([0.0, y, 0.0]))
            role_val = Text(str(role_v), font=FONT_MONO, font_size=28, color=TEXT)
            role_val.move_to(np.array([0.9, y, 0.0]))
            self.play(
                FadeIn(label), FadeIn(you_val), FadeIn(times), FadeIn(role_val),
                run_time=1.4,
            )
            row_mobs.append((label, you_val, times, role_val))
        self.wait(1.5)

        # -- matched entries multiply -----------------------------------------
        products = []
        transforms = []
        fade_labels = []
        for (label, you_val, times, role_val), (_, _, _, y) in zip(row_mobs, rows_data):
            product_val = int(you_val.text) * int(role_val.text)
            product = Text(str(product_val), font=FONT_MONO, font_size=30, color=DATA_PARAMS)
            product.move_to(np.array([0.0, y, 0.0]))
            transforms.append(ReplacementTransform(VGroup(you_val, times, role_val), product))
            fade_labels.append(FadeOut(label))
            products.append(product)
        self.play(*transforms, *fade_labels, run_time=2.1)
        self.wait(1.0)

        # -- and pool into the same lilac readout, on the same dial -----------
        total_score = sum(int(p.text) for p in products)
        new_readout = Text(str(total_score), font=FONT_MONO, font_size=32, color=DATA_PARAMS)
        new_readout.move_to(READOUT_POS)
        self.play(
            *[FadeOut(p, shift=(PIVOT - p.get_center())) for p in products],
            ReplacementTransform(readout_text, new_readout),
            run_time=2.3,
        )
        readout_text = new_readout
        self.play(FadeOut(you_header), FadeOut(role_header), run_time=0.8)
        self.wait(2.5)

        # ------------------------------------------------------------------
        # Segment C: guess card -- one candidate outlined, score hidden
        # ------------------------------------------------------------------
        self.play(FadeOut(readout_text), run_time=0.6)
        self.wait(0.6)

        cand_origin = np.array([-2.6, -0.2, 0.0])
        cand_angle = 60.0
        length_tracker = ValueTracker(1.1)

        def build_candidate():
            a = np.radians(cand_angle)
            end = cand_origin + length_tracker.get_value() * np.array(
                [np.cos(a), np.sin(a), 0.0]
            )
            return Arrow(
                cand_origin,
                end,
                buff=0,
                color=DATA_OBSERVED,
                stroke_width=8,
                max_tip_length_to_length_ratio=0.22,
            )

        candidate = build_candidate()
        c1_label = Text("c1", font=FONT_BODY, font_size=28, color=TEXT)
        c1_label.move_to(cand_origin + np.array([-0.55, 0.35, 0.0]))

        self.play(GrowArrow(candidate), FadeIn(c1_label), run_time=1.3)
        candidate.add_updater(lambda m: m.become(build_candidate()))

        outline = SurroundingRectangle(
            VGroup(candidate, c1_label), color=DATA_OBSERVED, buff=0.22, stroke_width=3
        )
        self.play(Create(outline), run_time=1.0)

        guess_title = Text("guess before you watch", font=FONT_HEADING, font_size=28, color=TEXT)
        guess_line1 = Text("c1 doubles in length --", font=FONT_BODY, font_size=28, color=TEXT)
        guess_line2 = Text("does the score double?", font=FONT_BODY, font_size=28, color=TEXT)
        guess_content = VGroup(guess_title, guess_line1, guess_line2).arrange(DOWN, buff=0.3)
        guess_content.move_to(np.array([3.0, 1.6, 0.0]))
        guess_rect = RoundedRectangle(
            corner_radius=0.2,
            width=guess_content.width + 1.0,
            height=guess_content.height + 0.8,
            fill_color=SURFACE,
            fill_opacity=0.95,
            stroke_color=TEXT,
            stroke_width=1.5,
        )
        guess_rect.move_to(guess_content.get_center())
        self.play(
            FadeIn(guess_rect), FadeIn(guess_title), FadeIn(guess_line1), FadeIn(guess_line2),
            run_time=1.5,
        )
        self.wait(12.0)

        self.play(
            FadeOut(guess_rect), FadeOut(guess_title), FadeOut(guess_line1),
            FadeOut(guess_line2), FadeOut(outline),
            run_time=0.9,
        )
        self.wait(0.6)

        # ------------------------------------------------------------------
        # Segment D: it climbs -- direction holds, size doubles the score
        # ------------------------------------------------------------------
        score_tracker = ValueTracker(50.0 * length_tracker.get_value())

        def build_score_text():
            t = Text(
                f"{score_tracker.get_value():.0f}", font=FONT_MONO, font_size=32,
                color=DATA_PARAMS,
            )
            t.move_to(READOUT_POS)
            return t

        score_readout = always_redraw(build_score_text)
        self.play(FadeIn(score_readout), run_time=0.8)
        self.wait(2.0)

        before_val = score_tracker.get_value()
        self.play(
            length_tracker.animate.set_value(2.2),
            score_tracker.animate.set_value(before_val * 2.0),
            run_time=6.5,
            rate_func=smooth,
        )
        candidate.clear_updaters()
        score_readout.clear_updaters()
        self.wait(1.5)

        after_val = score_tracker.get_value()
        before_label = Text(
            f"before: {before_val:.0f}", font=FONT_MONO, font_size=28, color=DATA_PARAMS
        )
        after_label = Text(
            f"after: {after_val:.0f}", font=FONT_MONO, font_size=28, color=DATA_PARAMS
        )
        stack = VGroup(before_label, after_label).arrange(DOWN, buff=0.35)
        stack.move_to(np.array([3.0, 0.3, 0.0]))
        self.play(FadeIn(before_label), FadeIn(after_label), run_time=1.0)

        flag = Text("size passed straight through", font=FONT_BODY, font_size=26, color=DATA_ERROR)
        flag.next_to(stack, DOWN, buff=0.4)
        self.play(FadeIn(flag), run_time=0.8)
        self.wait(6.0)

        # ------------------------------------------------------------------
        # Segment E: the walk-home question, and a quiet pointer onward
        # ------------------------------------------------------------------
        everything = VGroup(
            arc, pivot_dot, needle, score_readout, candidate, c1_label,
            before_label, after_label, flag,
        )
        self.play(FadeOut(everything), run_time=1.2)
        self.wait(0.6)

        closing_title = Text("still up?", font=FONT_HEADING, font_size=34, color=TEXT)
        closing_body = Text(
            "keep the direction, forget the size --", font=FONT_BODY, font_size=28, color=TEXT
        )
        closing_body2 = Text(
            "what's the cheapest fix?", font=FONT_BODY, font_size=28, color=TEXT
        )
        closing_content = VGroup(closing_title, closing_body, closing_body2).arrange(
            DOWN, buff=0.3
        )
        closing_content.move_to(np.array([0.0, 0.6, 0.0]))
        closing_rect = RoundedRectangle(
            corner_radius=0.22,
            width=closing_content.width + 1.2,
            height=closing_content.height + 0.9,
            fill_color=SURFACE,
            fill_opacity=0.95,
            stroke_color=TEXT,
            stroke_width=1.5,
        )
        closing_rect.move_to(closing_content.get_center())

        self.play(FadeIn(closing_rect), FadeIn(closing_title), run_time=1.3)
        self.play(FadeIn(closing_body), FadeIn(closing_body2), run_time=1.3)
        self.wait(5.0)

        chip = Text(
            "more ways to keep going: extensions menu", font=FONT_BODY, font_size=26, color=TEXT
        )
        chip.set_opacity(0.75)
        chip.move_to(np.array([0.0, -2.6, 0.0]))
        chip_arrow = Arrow(
            closing_rect.get_bottom() + DOWN * 0.1,
            chip.get_top() + UP * 0.05,
            buff=0.05,
            color=TEXT,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.3,
        )
        chip_arrow.set_opacity(0.6)
        self.play(FadeIn(chip_arrow), FadeIn(chip), run_time=1.3)
        self.wait(14.0)
