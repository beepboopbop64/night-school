import sys
from pathlib import Path

import numpy as np
from manim import *  # noqa: F403

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "shared" / "manim"))
from bbox_dump import attach_bbox_dump  # noqa: E402
from colors import *  # noqa: E402,F403
from style import FONT_BODY, FONT_HEADING, FONT_MONO  # noqa: E402


class Beat02(Scene):
    def construct(self):
        attach_bbox_dump(self)
        self.camera.background_color = BG

        # ------------------------------------------------------------------
        # Geometry helpers
        # ------------------------------------------------------------------
        origin = np.array([0.0, -0.3, 0.0])
        cand_radius = 2.2
        probe_radius = 3.0
        bar_baseline = -1.7
        bar_width = 0.6
        max_bar_height = 1.2  # reached when |score| == 5
        score_to_height = max_bar_height / 5.0

        def point_at(angle_deg: float, radius: float) -> np.ndarray:
            rad = np.radians(angle_deg)
            return origin + radius * np.array([np.cos(rad), np.sin(rad), 0.0])

        def score(probe_deg: float, cand_deg: float) -> float:
            return 5.0 * np.cos(np.radians(probe_deg - cand_deg))

        # ------------------------------------------------------------------
        # 1. Prediction freeze frame
        # ------------------------------------------------------------------
        card_rect = RoundedRectangle(
            width=6.0, height=3.0, corner_radius=0.25,
            color=TEXT, stroke_width=2, fill_color=SURFACE, fill_opacity=1.0,
        )
        heading = Text("Predict", font=FONT_HEADING, color=TEXT, font_size=40)
        line1 = Text("Top scorer?", font=FONT_BODY, color=TEXT, font_size=32)
        line2 = Text("Any negative?", font=FONT_BODY, color=TEXT, font_size=32)
        card_text = VGroup(heading, line1, line2).arrange(DOWN, buff=0.45)
        card_text.move_to(card_rect.get_center())
        card = VGroup(card_rect, heading, line1, line2)

        self.play(FadeIn(card), run_time=1.0)
        self.wait(3.5)
        self.play(FadeOut(card), run_time=0.7)

        # ------------------------------------------------------------------
        # 2. Build the compass: hinge + zero line
        # ------------------------------------------------------------------
        hinge_dot = Dot(origin, color=TEXT, radius=0.06)
        zero_line = Line(
            np.array([-2.7, bar_baseline, 0.0]),
            np.array([2.7, bar_baseline, 0.0]),
            color=TEXT, stroke_width=2, stroke_opacity=0.35,
        )
        self.play(Create(hinge_dot), Create(zero_line), run_time=0.6)

        # ------------------------------------------------------------------
        # 3. Candidate arrows (periwinkle), two at a time
        # ------------------------------------------------------------------
        candidates = [("A", 160.0), ("B", 110.0), ("C", 70.0), ("D", 20.0)]
        cand_arrows = {}
        cand_labels = {}
        for name, angle in candidates:
            arrow = Arrow(
                origin, point_at(angle, cand_radius), buff=0,
                color=DATA_OBSERVED, stroke_width=6,
                max_tip_length_to_length_ratio=0.18,
            )
            label = Text(name, font=FONT_BODY, color=TEXT, font_size=32)
            label.move_to(point_at(angle, cand_radius + 0.45))
            cand_arrows[name] = arrow
            cand_labels[name] = label

        self.play(
            Create(cand_arrows["A"]), Write(cand_labels["A"]),
            Create(cand_arrows["B"]), Write(cand_labels["B"]),
            run_time=1.3,
        )
        self.play(
            Create(cand_arrows["C"]), Write(cand_labels["C"]),
            Create(cand_arrows["D"]), Write(cand_labels["D"]),
            run_time=1.3,
        )

        # ------------------------------------------------------------------
        # 4. Probe arrow (amber), starts pointed at D
        # ------------------------------------------------------------------
        probe_angle = ValueTracker(20.0)

        probe_arrow = Arrow(
            origin, point_at(probe_angle.get_value(), probe_radius), buff=0,
            color=DATA_HEAT, stroke_width=10,
            max_tip_length_to_length_ratio=0.15,
        )

        def update_probe_arrow(mob: Mobject) -> None:
            mob.become(
                Arrow(
                    origin, point_at(probe_angle.get_value(), probe_radius), buff=0,
                    color=DATA_HEAT, stroke_width=10,
                    max_tip_length_to_length_ratio=0.15,
                )
            )

        probe_arrow.add_updater(update_probe_arrow)

        probe_label = Text("probe", font=FONT_BODY, color=TEXT, font_size=28)

        def update_probe_label(mob: Mobject) -> None:
            mob.move_to(point_at(probe_angle.get_value(), probe_radius + 0.5))

        update_probe_label(probe_label)
        probe_label.add_updater(update_probe_label)

        self.play(FadeIn(probe_arrow), FadeIn(probe_label), run_time=0.9)

        # ------------------------------------------------------------------
        # 5. Score bars + numeric readouts, two at a time
        # ------------------------------------------------------------------
        bars = {}
        nums = {}
        for name, angle in candidates:
            x = point_at(angle, cand_radius)[0]

            def make_bar_updater(cand_deg: float, bx: float):
                def updater(mob: Mobject) -> None:
                    s = score(probe_angle.get_value(), cand_deg)
                    h = max(abs(s) * score_to_height, 0.02)
                    cy = bar_baseline + h / 2 if s >= 0 else bar_baseline - h / 2
                    rect = Rectangle(
                        width=bar_width, height=h, stroke_width=0,
                        fill_color=DATA_PARAMS, fill_opacity=0.85,
                    )
                    rect.move_to(np.array([bx, cy, 0.0]))
                    mob.become(rect)

                return updater

            def make_num_updater(cand_deg: float, bx: float):
                def updater(mob: Mobject) -> None:
                    s = score(probe_angle.get_value(), cand_deg)
                    h = max(abs(s) * score_to_height, 0.02)
                    y = bar_baseline + h + 0.28 if s >= 0 else bar_baseline - h - 0.28
                    txt = Text(str(int(round(s))), font=FONT_MONO, color=DATA_PARAMS, font_size=30)
                    txt.move_to(np.array([bx, y, 0.0]))
                    mob.become(txt)

                return updater

            bar = Rectangle(width=bar_width, height=0.02, fill_color=DATA_PARAMS, fill_opacity=0.85, stroke_width=0)
            bar_upd = make_bar_updater(angle, x)
            bar_upd(bar)
            bar.add_updater(bar_upd)

            num = Text("0", font=FONT_MONO, color=DATA_PARAMS, font_size=30)
            num_upd = make_num_updater(angle, x)
            num_upd(num)
            num.add_updater(num_upd)

            bars[name] = bar
            nums[name] = num

        self.play(FadeIn(bars["A"]), FadeIn(nums["A"]), FadeIn(bars["B"]), FadeIn(nums["B"]), run_time=0.9)
        self.play(FadeIn(bars["C"]), FadeIn(nums["C"]), FadeIn(bars["D"]), FadeIn(nums["D"]), run_time=0.9)

        # ------------------------------------------------------------------
        # 6. Candidates recede: probe becomes the sole moving focus
        # ------------------------------------------------------------------
        self.play(
            cand_arrows["A"].animate.set_opacity(0.45),
            cand_labels["A"].animate.set_opacity(0.45),
            cand_arrows["B"].animate.set_opacity(0.45),
            cand_labels["B"].animate.set_opacity(0.45),
            cand_arrows["C"].animate.set_opacity(0.45),
            cand_labels["C"].animate.set_opacity(0.45),
            cand_arrows["D"].animate.set_opacity(0.45),
            cand_labels["D"].animate.set_opacity(0.45),
            run_time=0.6,
        )

        # ------------------------------------------------------------------
        # 7. Turn the probe: first pass, pausing on each candidate
        # ------------------------------------------------------------------
        self.play(probe_angle.animate.set_value(70.0), run_time=1.6, rate_func=linear)
        self.wait(0.5)
        self.play(probe_angle.animate.set_value(110.0), run_time=1.4, rate_func=linear)
        self.wait(0.5)
        self.play(probe_angle.animate.set_value(160.0), run_time=1.4, rate_func=linear)
        self.wait(0.5)
        self.play(probe_angle.animate.set_value(190.0), run_time=1.0, rate_func=linear)
        self.wait(0.5)
        self.play(probe_angle.animate.set_value(20.0), run_time=6.0, rate_func=linear)
        self.wait(0.8)

        # ------------------------------------------------------------------
        # 8. Watch again: bars answer, candidates never move
        # ------------------------------------------------------------------
        self.play(probe_angle.animate.set_value(190.0), run_time=6.0, rate_func=linear)
        self.wait(0.6)
        self.play(probe_angle.animate.set_value(20.0), run_time=4.5, rate_func=linear)
        self.wait(0.6)

        # ------------------------------------------------------------------
        # 9. Probe parks; scores land as integers
        # ------------------------------------------------------------------
        self.wait(5.0)
