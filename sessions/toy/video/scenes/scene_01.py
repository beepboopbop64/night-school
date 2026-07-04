# Toy Manim scene for beat-01 (M1 walking skeleton) — written by the
# scene-render node; do not edit by hand. Deliberately animation-heavy so the
# -ql render takes real wall time (the kill/resume exit test needs a window).
import sys
from pathlib import Path

from manim import *  # noqa: F403

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "shared" / "manim"))
from colors import BG, BRAND_MINT, BRAND_PERIWINKLE, BRAND_ROSE, DATA_HEAT, TEXT  # noqa: E402


class Scene01(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("beat-01: The aha, trued", font_size=28, color=BRAND_PERIWINKLE)
        title.to_edge(UP)
        line1 = Text("A lesson pipeline is a build", font_size=34, color=TEXT)
        line2 = Text("system whose artifacts happen to teach.", font_size=34, color=BRAND_MINT)
        aha = VGroup(line1, line2).arrange(DOWN, buff=0.35)

        self.play(Write(title), run_time=2)
        self.play(Write(line1), run_time=3)
        self.play(Write(line2), run_time=3)
        self.wait(1)
        self.play(aha.animate.scale(0.6).to_edge(UP, buff=1.2), FadeOut(title), run_time=2)

        # A rough shape trues up: circle -> square (the True-Up motif, sketched).
        shape = Circle(radius=1.4, color=BRAND_ROSE, stroke_width=6)
        square = Square(side_length=2.4, color=BRAND_MINT, stroke_width=6)
        self.play(Create(shape), run_time=2)
        self.wait(0.5)
        self.play(Transform(shape, square), run_time=3)
        self.play(Rotate(shape, angle=PI / 2), run_time=2)
        self.play(shape.animate.scale(0.75).set_color(BRAND_PERIWINKLE), run_time=2)
        self.play(shape.animate.scale(4 / 3).set_color(BRAND_MINT), run_time=2)

        # An orbit of artifact dots — receipts around the work.
        dots = VGroup(*[
            Dot(radius=0.06, color=DATA_HEAT).move_to(
                [3.2 * np.cos(k * TAU / 36), 2.1 * np.sin(k * TAU / 36), 0]
            )
            for k in range(36)
        ])
        self.play(LaggedStart(*[FadeIn(dot, scale=3) for dot in dots], lag_ratio=0.06), run_time=4)
        self.play(Rotate(dots, angle=TAU / 3, about_point=ORIGIN), run_time=4)
        self.play(dots.animate.set_color(BRAND_PERIWINKLE), run_time=2)
        self.play(Rotate(dots, angle=-TAU / 3, about_point=ORIGIN), run_time=4)

        receipt = Text("receipt: sha256 - gate - cost", font_size=24, color=DATA_HEAT)
        receipt.next_to(shape, DOWN, buff=0.8)
        self.play(Write(receipt), run_time=2)
        self.wait(1)
        self.play(Indicate(shape, color=BRAND_ROSE), run_time=2)
        self.play(Indicate(receipt, color=BRAND_MINT), run_time=2)
        self.play(Rotate(dots, angle=TAU / 6, about_point=ORIGIN), run_time=3)
        self.wait(1)
        self.play(FadeOut(dots), run_time=2)
        self.play(FadeOut(aha), FadeOut(shape), FadeOut(receipt), run_time=2)
        self.wait(1)
