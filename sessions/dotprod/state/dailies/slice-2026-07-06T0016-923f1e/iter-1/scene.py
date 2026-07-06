import sys
from pathlib import Path

from manim import *  # noqa: F403

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "shared" / "manim"))
from bbox_dump import attach_bbox_dump  # noqa: E402
from colors import *  # noqa: E402,F403
from style import FONT_BODY, FONT_HEADING, FONT_MONO  # noqa: E402


class Beat04(Scene):
    def construct(self):
        attach_bbox_dump(self)
        self.camera.background_color = BG

        # ------------------------------------------------------------------
        # 1. Retrieval card holds the compressed question; the meter idles.
        # ------------------------------------------------------------------
        card_rect = RoundedRectangle(
            width=3.4, height=1.8, corner_radius=0.15,
            fill_color=SURFACE, fill_opacity=1.0,
            stroke_color=TEXT, stroke_width=2,
        ).move_to([-4.0, 2.5, 0])
        arrow_in1 = Arrow(
            start=[-4.9, 2.3, 0], end=[-4.5, 2.7, 0],
            buff=0, color=DATA_HEAT, stroke_width=5,
        )
        arrow_in2 = Arrow(
            start=[-4.3, 2.3, 0], end=[-3.9, 2.7, 0],
            buff=0, color=DATA_OBSERVED, stroke_width=5,
        )
        qmark = Text("?", font=FONT_MONO, color=TEXT, font_size=34).move_to([-3.3, 2.5, 0])

        self.play(
            Create(card_rect), GrowArrow(arrow_in1), GrowArrow(arrow_in2), Write(qmark),
            run_time=1.6,
        )
        self.wait(0.6)

        arc = Arc(radius=0.9, start_angle=0, angle=PI, color=DATA_PARAMS, stroke_width=6)
        needle = Line(ORIGIN, [0, 0.75, 0], color=DATA_PARAMS, stroke_width=5)
        meter = VGroup(arc, needle)
        meter.move_to([3.3, 2.5, 0])
        self.play(Create(arc), Create(needle), run_time=1.2)

        pivot = needle.get_start()
        self.play(
            Rotate(needle, angle=0.3, about_point=pivot, rate_func=there_and_back),
            run_time=1.8,
        )
        self.wait(4.0)

        # ------------------------------------------------------------------
        # 2. The opening scene comes back: fade the idle moment out.
        # ------------------------------------------------------------------
        self.play(FadeOut(card_rect), FadeOut(arrow_in1), FadeOut(arrow_in2),
                  FadeOut(qmark), FadeOut(arc), FadeOut(needle), run_time=1.0)
        self.wait(2.0)

        # ------------------------------------------------------------------
        # 3. The two tall stacks stand beside the arrows they folded into.
        # ------------------------------------------------------------------
        stack_a = Rectangle(
            width=0.9, height=2.0, fill_color=DATA_HEAT, fill_opacity=0.85,
            stroke_color=DATA_HEAT, stroke_width=2,
        ).move_to([-5.2, -2.0, 0])
        stack_b = Rectangle(
            width=0.9, height=2.0, fill_color=DATA_OBSERVED, fill_opacity=0.85,
            stroke_color=DATA_OBSERVED, stroke_width=2,
        ).move_to([-3.6, -2.0, 0])
        self.play(Create(stack_a), Create(stack_b), run_time=1.4)

        arrow_probe = Arrow(
            start=[-5.2, -1.0, 0], end=[-5.2, 1.2, 0],
            buff=0, color=DATA_HEAT, stroke_width=6,
        )
        arrow_cand0 = Arrow(
            start=[-3.6, -1.0, 0], end=[-3.6, 1.2, 0],
            buff=0, color=DATA_OBSERVED, stroke_width=6,
        )
        self.play(
            TransformFromCopy(stack_a, arrow_probe),
            TransformFromCopy(stack_b, arrow_cand0),
            run_time=1.6,
        )

        label_taste = Text("your taste", font=FONT_BODY, color=TEXT, font_size=30)
        label_taste.next_to(arrow_probe, UP, buff=0.35)
        self.play(Write(label_taste), run_time=1.2)
        self.wait(2.5)

        self.play(Indicate(arrow_probe, color=DATA_HEAT, scale_factor=1.15), run_time=1.2)
        self.wait(0.8)

        # ------------------------------------------------------------------
        # 4. The catalog is a shelf of candidates, arrows all the way down.
        # ------------------------------------------------------------------
        self.play(
            stack_a.animate.set_opacity(0.4),
            stack_b.animate.set_opacity(0.4),
            run_time=0.6,
        )

        cand_xs = [-2.3, -1.0, 0.3, 1.6, 2.9, 4.2]
        cand1, cand2, cand3, cand4, cand5, cand6 = (
            Arrow(start=[x, -1.0, 0], end=[x, 1.2, 0], buff=0,
                  color=DATA_OBSERVED, stroke_width=5)
            for x in cand_xs
        )
        self.play(GrowArrow(cand1), GrowArrow(cand2), GrowArrow(cand3), run_time=1.4)
        self.play(GrowArrow(cand4), GrowArrow(cand5), GrowArrow(cand6), run_time=1.4)

        continuation = VGroup(
            Dot(radius=0.06, color=TEXT), Dot(radius=0.06, color=TEXT), Dot(radius=0.06, color=TEXT)
        ).arrange(RIGHT, buff=0.25).move_to([5.4, 0.1, 0])
        self.play(FadeIn(continuation), run_time=0.8)
        self.wait(2.5)

        self.play(FadeOut(stack_a), FadeOut(stack_b), run_time=0.8)

        # ------------------------------------------------------------------
        # 5. Score bars rank themselves under the shelf.
        # ------------------------------------------------------------------
        baseline = -3.2
        scale_h = 1.6
        values = [0.42, 0.55, 0.31, 0.87, 0.63, 0.24, 0.48]
        all_xs = [-3.6] + cand_xs
        bars = []
        for x, v in zip(all_xs, values):
            h = v * scale_h
            bar = Rectangle(
                width=0.5, height=h, fill_color=DATA_PARAMS, fill_opacity=0.85,
                stroke_color=DATA_PARAMS, stroke_width=2,
            ).move_to([x, baseline + h / 2, 0])
            bars.append(bar)
        bar0, bar1, bar2, bar3, bar4, bar5, bar6 = bars

        self.play(
            LaggedStart(
                GrowFromEdge(bar0, DOWN), GrowFromEdge(bar1, DOWN),
                GrowFromEdge(bar2, DOWN), GrowFromEdge(bar3, DOWN),
                lag_ratio=0.15,
            ),
            run_time=1.6,
        )
        self.play(
            LaggedStart(
                GrowFromEdge(bar4, DOWN), GrowFromEdge(bar5, DOWN), GrowFromEdge(bar6, DOWN),
                lag_ratio=0.15,
            ),
            run_time=1.6,
        )
        self.wait(0.8)

        candidate_arrows = [arrow_cand0, cand1, cand2, cand4, cand5, cand6]
        dim_bars = [bar0, bar1, bar2, bar4, bar5, bar6]
        self.play(
            bar3.animate.set_fill(opacity=1.0),
            *[b.animate.set_opacity(0.35) for b in dim_bars],
            *[a.animate.set_opacity(0.35) for a in candidate_arrows],
            arrow_probe.animate.set_opacity(0.35),
            label_taste.animate.set_opacity(0.35),
            continuation.animate.set_opacity(0.35),
            run_time=1.4,
        )
        self.wait(2.0)

        # The top bar slides forward, as the played song.
        self.play(bar3.animate.shift(UP * 0.3).scale(1.15), run_time=1.8)

        # ------------------------------------------------------------------
        # 6. The data center readout fills its question mark with the score.
        # ------------------------------------------------------------------
        panel = RoundedRectangle(
            width=3.6, height=1.4, corner_radius=0.15,
            fill_color=SURFACE, fill_opacity=1.0,
            stroke_color=DATA_PARAMS, stroke_width=3,
        ).move_to([0.0, 3.05, 0])
        qmark2 = Text("?", font=FONT_MONO, color=TEXT, font_size=40).move_to(panel.get_center())
        self.play(Create(panel), Write(qmark2), run_time=1.6)
        self.wait(1.0)

        score_text = Text("0.87", font=FONT_MONO, color=DATA_PARAMS, font_size=40)
        score_text.move_to(panel.get_center())
        self.play(ReplacementTransform(qmark2, score_text), run_time=1.8)
        self.play(
            Indicate(score_text, color=DATA_PARAMS, scale_factor=1.2),
            Indicate(panel, color=DATA_PARAMS, scale_factor=1.05),
            run_time=1.2,
        )
        self.wait(1.5)
