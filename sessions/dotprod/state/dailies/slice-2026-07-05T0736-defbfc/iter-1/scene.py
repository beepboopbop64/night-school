import sys
from pathlib import Path

from manim import *  # noqa: F403

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "shared" / "manim"))
from bbox_dump import attach_bbox_dump  # noqa: E402
from colors import *  # noqa: E402,F403
from style import FONT_BODY, FONT_HEADING, FONT_MONO  # noqa: E402

import numpy as np  # noqa: E402

# ---------------------------------------------------------------------------
# Geometry constants
# ---------------------------------------------------------------------------
CARD_CENTER = np.array([0.0, 3.5, 0.0])
PIVOT = np.array([4.8, 0.3, 0.0])
RADIUS = 1.0
READOUT_POS = np.array([4.8, -0.9, 0.0])
OP_POS = np.array([3.7, 0.3, 0.0])

LABEL_X, YOU_X, ROLE_X = -4.6, -1.8, 0.6
HEADER_Y = 2.3
ROW_YS = [1.6, 0.9, 0.2, -0.5, -1.2, -1.9]
OP2_X = -0.6

ROWS = [
    ("Python hours", 8, 9),
    ("SQL reps", 6, 7),
    ("nights free", 3, 2),
    ("years shipped", 5, 6),
    ("on-call weeks", 4, 5),
    ("certifications", 2, 3),
]


class Beat04(Scene):
    def construct(self):
        attach_bbox_dump(self)
        self.camera.background_color = BG

        # -- retrieval prompt card, holds throughout --------------------------
        card_rect = RoundedRectangle(
            corner_radius=0.2,
            width=5.0,
            height=0.8,
            fill_color=SURFACE,
            fill_opacity=0.95,
            stroke_color=TEXT,
            stroke_width=1.5,
        ).move_to(CARD_CENTER)
        card_text = Text(
            "retrieval prompt", font=FONT_BODY, font_size=28, color=TEXT
        ).move_to(CARD_CENTER)
        self.play(FadeIn(card_rect), FadeIn(card_text), run_time=1.0)
        self.wait(0.4)
        card_group = VGroup(card_rect, card_text)

        # -- meter, rebuilt from memory ---------------------------------------
        arc = Arc(
            radius=RADIUS,
            start_angle=PI,
            angle=-PI,
            arc_center=PIVOT,
            color=DATA_PARAMS,
            stroke_width=8,
        )
        pivot_dot = Dot(PIVOT, radius=0.08, color=DATA_PARAMS)
        self.play(Create(arc), FadeIn(pivot_dot), run_time=1.0)

        needle = Line(PIVOT, PIVOT + UP * 0.85, color=DATA_PARAMS, stroke_width=9)
        self.play(FadeIn(needle), run_time=0.6)
        self.wait(0.4)

        # -- two arrows go in ---------------------------------------------------
        arrow_a = Arrow(
            np.array([2.2, 1.5, 0.0]),
            np.array([3.4, 1.0, 0.0]),
            buff=0,
            color=DATA_OBSERVED,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.25,
        )
        arrow_b = Arrow(
            np.array([2.2, -1.0, 0.0]),
            np.array([3.4, -0.4, 0.0]),
            buff=0,
            color=DATA_OBSERVED,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.25,
        )
        self.play(GrowArrow(arrow_a), GrowArrow(arrow_b), run_time=1.0)
        self.wait(0.5)

        # -- the two operations: multiply, then add ------------------------------
        times_symbol = Text("×", font=FONT_MONO, font_size=36, color=TEXT).move_to(OP_POS)
        self.play(FadeIn(times_symbol), run_time=0.5)
        self.wait(0.3)

        plus_symbol = Text("+", font=FONT_MONO, font_size=36, color=TEXT).move_to(OP_POS)
        self.play(ReplacementTransform(times_symbol, plus_symbol), run_time=0.5)
        self.wait(0.3)

        readout_text = Text(
            "score", font=FONT_MONO, font_size=32, color=DATA_PARAMS
        ).move_to(READOUT_POS)
        self.play(FadeIn(readout_text), run_time=0.6)
        self.wait(1.0)

        meter_group = VGroup(arc, pivot_dot, needle, readout_text)

        # -- one detour worth naming: clear the recall props, both recede -------
        self.play(FadeOut(arrow_a), FadeOut(arrow_b), FadeOut(plus_symbol), run_time=0.6)
        self.play(
            card_group.animate.set_opacity(0.4),
            meter_group.animate.set_opacity(0.4),
            run_time=0.8,
        )
        self.wait(0.3)

        # -- swap the columns: you vs the role -----------------------------------
        header_you = Text("you", font=FONT_BODY, font_size=30, color=TEXT).move_to(
            np.array([YOU_X, HEADER_Y, 0.0])
        )
        header_role = Text(
            "the role", font=FONT_BODY, font_size=30, color=TEXT
        ).move_to(np.array([ROLE_X, HEADER_Y, 0.0]))
        self.play(FadeIn(header_you), FadeIn(header_role), run_time=0.6)
        self.wait(0.2)

        row_mobs = []
        for (label, yv, rv), y in zip(ROWS, ROW_YS):
            lbl = Text(label, font=FONT_BODY, font_size=28, color=TEXT).move_to(
                np.array([LABEL_X, y, 0.0])
            )
            yv_t = Text(str(yv), font=FONT_MONO, font_size=30, color=DATA_OBSERVED).move_to(
                np.array([YOU_X, y, 0.0])
            )
            rv_t = Text(str(rv), font=FONT_MONO, font_size=30, color=DATA_OBSERVED).move_to(
                np.array([ROLE_X, y, 0.0])
            )
            self.play(FadeIn(lbl), FadeIn(yv_t), FadeIn(rv_t), run_time=0.6)
            self.wait(0.15)
            row_mobs.append((lbl, yv_t, rv_t))

        self.wait(1.0)

        table_group = VGroup(
            header_you, header_role, *[m for triple in row_mobs for m in triple]
        )

        # -- matched entries multiply and pool into the same dial ----------------
        self.play(
            table_group.animate.set_opacity(0.4),
            meter_group.animate.set_opacity(1.0),
            run_time=0.8,
        )
        self.wait(0.3)

        times_syms = [
            Text("×", font=FONT_MONO, font_size=32, color=TEXT).move_to(
                np.array([OP2_X, y, 0.0])
            )
            for _, y in zip(ROWS, ROW_YS)
        ]
        self.play(*[FadeIn(t) for t in times_syms[:3]], run_time=0.5)
        self.play(*[FadeIn(t) for t in times_syms[3:]], run_time=0.5)
        self.wait(0.3)

        dots = [
            Dot(np.array([OP2_X, y - 0.4, 0.0]), radius=0.1, color=DATA_PARAMS)
            for _, y in zip(ROWS, ROW_YS)
        ]
        self.play(*[FadeIn(d) for d in dots[:3]], run_time=0.4)
        self.play(*[FadeIn(d) for d in dots[3:]], run_time=0.4)
        self.wait(0.3)

        fit_score = sum(yv * rv for (_, yv, rv) in ROWS)
        new_readout = Text(
            f"fit {fit_score}", font=FONT_MONO, font_size=32, color=DATA_PARAMS
        ).move_to(READOUT_POS)

        pool_anims = [FadeOut(d, shift=PIVOT - d.get_center()) for d in dots]
        pool_anims += [FadeOut(t) for t in times_syms]
        pool_anims.append(ReplacementTransform(readout_text, new_readout))
        self.play(*pool_anims, run_time=1.8)
        self.wait(0.5)

        self.play(Indicate(new_readout, color=DATA_PARAMS, scale_factor=1.15), run_time=0.8)
        self.wait(0.4)
        self.play(table_group.animate.set_opacity(0.25), run_time=0.7)
        self.wait(8.0)
