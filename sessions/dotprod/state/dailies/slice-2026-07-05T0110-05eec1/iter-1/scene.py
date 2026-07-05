import sys
from pathlib import Path

from manim import *  # noqa: F403

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "shared" / "manim"))
from bbox_dump import attach_bbox_dump  # noqa: E402
from colors import *  # noqa: E402,F403
from style import FONT_BODY, FONT_HEADING, FONT_MONO  # noqa: E402

import numpy as np  # noqa: E402

CAND_START = np.array([-1.0, -2.6, 0.0])
CAND_ANGLE = np.radians(58)
CAND_DIR = np.array([np.cos(CAND_ANGLE), np.sin(CAND_ANGLE), 0.0])
SCORE_POS = np.array([3.0, -1.6, 0.0])
SCORE_K = 2.0  # score = SCORE_K * candidate length -- direction never changes


def _candidate_arrow(length: float) -> Arrow:
    return Arrow(
        CAND_START,
        CAND_START + CAND_DIR * length,
        buff=0,
        color=DATA_OBSERVED,
        stroke_width=8,
        tip_length=0.22,
    )


def _score_text(length: float) -> Text:
    value = SCORE_K * length
    t = Text(f"score {value:0.2f}", font=FONT_MONO, font_size=32, color=DATA_PARAMS)
    t.move_to(SCORE_POS)
    return t


class Beat04(Scene):
    def construct(self):
        attach_bbox_dump(self)
        self.camera.background_color = BG

        # ------------------------------------------------------------------
        # Phase 1: the retrieval prompt holds as a card; the meter idles.
        # ------------------------------------------------------------------
        card_rect = RoundedRectangle(
            width=3.6,
            height=1.8,
            corner_radius=0.22,
            color=TEXT,
            fill_color=SURFACE,
            fill_opacity=1.0,
            stroke_width=2,
        )
        card_rect.move_to(np.array([-3.8, 2.0, 0.0]))
        card_label = Text("retrieval prompt", font=FONT_HEADING, font_size=28, color=TEXT)
        if card_label.width > 3.1:
            card_label.scale_to_fit_width(3.1)
        card_label.move_to(card_rect.get_center())

        self.play(Create(card_rect), Write(card_label), run_time=1.8)

        pivot = np.array([2.6, 1.3, 0.0])
        radius = 1.0
        arc = Arc(
            radius=radius,
            start_angle=PI,
            angle=-PI,
            arc_center=pivot,
            color=DATA_PARAMS,
            stroke_width=7,
        )
        pivot_dot = Dot(pivot, radius=0.07, color=DATA_PARAMS)
        needle_angle = np.radians(35)
        needle = Line(
            pivot,
            pivot + 0.85 * np.array([np.cos(needle_angle), np.sin(needle_angle), 0.0]),
            color=DATA_OBSERVED,
            stroke_width=7,
        )
        meter_label = Text("meter", font=FONT_BODY, font_size=24, color=TEXT)
        meter_label.move_to(pivot + DOWN * 0.7)

        self.play(
            Create(arc), FadeIn(pivot_dot), FadeIn(needle), FadeIn(meter_label), run_time=2.0
        )
        self.wait(2.0)

        card_group = VGroup(card_rect, card_label)
        meter_group = VGroup(arc, pivot_dot, needle, meter_label)

        # ------------------------------------------------------------------
        # Phase 2: one candidate stretches; direction holds; score climbs.
        # ------------------------------------------------------------------
        candidate_arrow = _candidate_arrow(1.0)
        candidate_label = Text("candidate", font=FONT_BODY, font_size=24, color=DATA_OBSERVED)
        candidate_label.move_to(CAND_START + DOWN * 0.55)

        score_text = _score_text(1.0)

        self.play(
            GrowArrow(candidate_arrow),
            FadeIn(candidate_label),
            FadeIn(score_text),
            run_time=1.8,
        )
        self.wait(1.2)

        direction_note = Text("direction unchanged", font=FONT_BODY, font_size=24, color=TEXT)
        direction_note.move_to(np.array([-2.9, -1.5, 0.0]))

        self.play(
            card_group.animate.set_opacity(0.4),
            meter_group.animate.set_opacity(0.4),
            FadeIn(direction_note),
            run_time=1.0,
        )

        stretch_tracker = ValueTracker(1.0)

        def _update_arrow(mob):
            mob.become(_candidate_arrow(stretch_tracker.get_value()))

        def _update_score(mob):
            mob.become(_score_text(stretch_tracker.get_value()))

        candidate_arrow.add_updater(_update_arrow)
        score_text.add_updater(_update_score)

        self.play(stretch_tracker.animate.set_value(2.4), run_time=3.5)

        candidate_arrow.clear_updaters()
        score_text.clear_updaters()

        flag_triangle = Triangle(color=DATA_ERROR, fill_color=DATA_ERROR, fill_opacity=1.0)
        flag_triangle.scale(0.14)
        flag_label = Text("unearned win", font=FONT_BODY, font_size=24, color=DATA_ERROR)
        flag_group = VGroup(flag_triangle, flag_label).arrange(RIGHT, buff=0.25)
        flag_group.move_to(np.array([3.0, -2.7, 0.0]))

        self.play(FadeIn(flag_group), run_time=1.2)
        self.wait(2.5)

        everything = VGroup(
            card_group,
            meter_group,
            candidate_arrow,
            candidate_label,
            score_text,
            direction_note,
            flag_group,
        )
        self.play(FadeOut(everything), run_time=1.2)

        # ------------------------------------------------------------------
        # Phase 3: the walk-home question lands; a chip points to more.
        # ------------------------------------------------------------------
        card2 = RoundedRectangle(
            width=7.0,
            height=2.6,
            corner_radius=0.25,
            color=TEXT,
            fill_color=SURFACE,
            fill_opacity=1.0,
            stroke_width=2,
        )
        card2.move_to(np.array([0.0, 0.4, 0.0]))
        tag2 = Text("for the walk home", font=FONT_HEADING, font_size=24, color=TEXT)
        tag2.move_to(card2.get_center() + UP * 0.75)
        title2 = Text(
            "same direction, smaller size?", font=FONT_BODY, font_size=30, color=TEXT
        )
        if title2.width > 6.2:
            title2.scale_to_fit_width(6.2)
        title2.move_to(card2.get_center() + DOWN * 0.15)

        self.play(Create(card2), Write(tag2), Write(title2), run_time=2.0)
        self.wait(1.3)

        chip_rect = RoundedRectangle(
            width=3.6,
            height=0.9,
            corner_radius=0.18,
            color=TEXT,
            fill_color=SURFACE,
            fill_opacity=1.0,
            stroke_width=2,
        )
        chip_rect.move_to(np.array([0.0, -3.3, 0.0]))
        chip_text = Text("3 ways to continue", font=FONT_MONO, font_size=24, color=TEXT)
        if chip_text.width > 3.0:
            chip_text.scale_to_fit_width(3.0)
        chip_text.move_to(chip_rect.get_center())
        chip_group = VGroup(chip_rect, chip_text)

        self.play(FadeIn(chip_group), run_time=1.3)
        self.wait(6.0)
