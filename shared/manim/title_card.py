"""Night School video title card — the fixed brand surface (BRAND.md).

Silent 10pm Sky field. One warm lit-window rectangle blooms on. The session
title arrives in Bricolage cream. A freehand underline draws itself, wobbles
once, and TRUES with the mint glow — the True-Up, on the card that opens
every session. `NIGHT SCHOOL · SESSION NN` in Plex Mono small caps. Under
five seconds, always.

Render (from this directory):
    manim -qh title_card.py TitleCard
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import numpy as np
from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    Create,
    CubicBezier,
    FadeIn,
    Line,
    RoundedRectangle,
    Scene,
    Text,
    VGroup,
    smooth,
)

from colors import BG, BRAND_MINT, BRAND_PERIWINKLE, DATA_HEAT, TEXT
from style import (
    FONT_HEADING,
    FONT_MONO,
    roughen,
    true_up,
    wobble_once,
)


def _lit_window() -> VGroup:
    """One warm window, lit after hours: amber panes behind a dark muntin."""
    frame = RoundedRectangle(
        corner_radius=0.06,
        width=0.95,
        height=1.35,
        stroke_width=0,
        fill_color=DATA_HEAT,
        fill_opacity=0.92,
    )
    mullion = Line(frame.get_top(), frame.get_bottom(), stroke_color=BG, stroke_width=5)
    transom = Line(frame.get_left(), frame.get_right(), stroke_color=BG, stroke_width=5).shift(
        UP * 0.22
    )
    halo = VGroup(
        *[
            RoundedRectangle(
                corner_radius=0.10 + 0.07 * (i + 1),
                width=0.95 + 0.22 * (i + 1),
                height=1.35 + 0.22 * (i + 1),
                stroke_width=0,
                fill_color=DATA_HEAT,
                fill_opacity=0.10 * (1.0 - i / 4.0),
            )
            for i in range(4)
        ]
    )
    return VGroup(halo, frame, mullion, transom)


class TitleCard(Scene):
    def construct(self) -> None:
        self.camera.background_color = BG

        # --- the one lit window, up and off to the left -------------------
        window = _lit_window().scale(0.9).move_to(np.array([-4.9, 2.2, 0.0]))

        # --- title in Bricolage cream --------------------------------------
        title = Text(
            "Attention Is a Soft Lookup Table",
            font=FONT_HEADING,
            font_size=58,
            color=TEXT,
            weight="MEDIUM",
        )
        title.scale_to_fit_width(min(title.width, 11.5))
        title.move_to(np.array([0.0, 0.35, 0.0]))

        # --- the freehand underline (a line, never letters) ----------------
        left = title.get_corner(DOWN + LEFT) + DOWN * 0.42
        right = title.get_corner(DOWN + RIGHT) + DOWN * 0.42
        span = right - left
        # Born pre-formal: periwinkle sketch; trues into an exact mint line.
        underline = CubicBezier(
            left,
            left + span * 0.3 + UP * 0.05,
            left + span * 0.7 + DOWN * 0.05,
            right + UP * 0.02,
        ).set_stroke(color=BRAND_PERIWINKLE, width=5)
        roughen(underline, amplitude=0.02, seed=11)

        # --- session line in Plex Mono small caps ---------------------------
        session = Text(
            "NIGHT SCHOOL · SESSION 01",
            font=FONT_MONO,
            font_size=22,
            color=BRAND_PERIWINKLE,
        )
        session.next_to(underline, DOWN, buff=0.55)

        # --- the card, under five seconds -----------------------------------
        self.wait(0.15)
        self.play(FadeIn(window, scale=0.94), run_time=0.8, rate_func=smooth)
        self.play(
            FadeIn(title, shift=UP * 0.18),
            run_time=0.75,
            rate_func=smooth,
        )
        self.play(Create(underline), run_time=0.6, rate_func=smooth)
        self.play(wobble_once(underline, seed=29))  # one shiver: intuition
        self.play(true_up(underline, settle_color=BRAND_MINT))  # rigor, glowing
        self.play(FadeIn(session, shift=UP * 0.08), run_time=0.45, rate_func=smooth)
        self.wait(0.35)
