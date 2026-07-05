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
METER_CENTER = np.array([0.0, -2.05, 0.0])
RADIUS = 0.85
NEEDLE_LEN = 0.8
IDLE_ANGLE = 90.0
FINAL_ANGLE = 40.0

CARD_POS = np.array([0.0, 2.6, 0.0])

HEADER_Y = 3.55
ROW_YS = [2.85, 2.15, 1.45, 0.75, 0.05, -0.65]
LABEL_X = -3.7
YOU_X = 0.3
ROLE_X = 3.7
PROD_X = (YOU_X + ROLE_X) / 2.0

CAPTION_POS = np.array([0.0, -2.575, 0.0])
READOUT_POS = np.array([0.0, -3.325, 0.0])
CLOSING_POS = np.array([0.0, 1.2, 0.0])

ROWS = [
    ("Python hours", 8, 6),
    ("SQL reps", 3, 5),
    ("nights free", 4, 2),
    ("years exp", 5, 4),
    ("team size", 2, 3),
    ("commute mins", 1, 1),
]


def direction(angle_deg: float) -> np.ndarray:
    rad = np.radians(angle_deg)
    return np.array([np.cos(rad), np.sin(rad), 0.0])


def make_arrow(start: np.ndarray, angle_deg: float, length: float, color: str) -> Arrow:
    end = start + direction(angle_deg) * length
    return Arrow(
        start,
        end,
        buff=0,
        color=color,
        stroke_width=5,
        max_tip_length_to_length_ratio=0.28,
        max_stroke_width_to_length_ratio=20,
    )


class Beat04(Scene):
    def construct(self):
        attach_bbox_dump(self)
        self.camera.background_color = BG

        # ------------------------------------------------------------------
        # The meter, idling. Built once, reused for the whole beat.
        # ------------------------------------------------------------------
        meter_angle = ValueTracker(IDLE_ANGLE)
        op_tracker = ValueTracker(1.0)

        arc = Arc(
            radius=RADIUS,
            start_angle=PI,
            angle=-PI,
            arc_center=METER_CENTER,
            color=DATA_PARAMS,
            stroke_width=7,
        )
        self.play(Create(arc), run_time=1.0)

        def build_needle():
            needle = make_arrow(METER_CENTER, meter_angle.get_value(), NEEDLE_LEN, DATA_PARAMS)
            needle.set_stroke(opacity=op_tracker.get_value())
            return needle

        needle = build_needle()
        pivot = Dot(METER_CENTER, radius=0.06, color=DATA_PARAMS)
        self.play(GrowArrow(needle), FadeIn(pivot), run_time=0.7)
        needle.add_updater(lambda m: m.become(build_needle()))

        # ------------------------------------------------------------------
        # The recall prompt: the meter idles, dimmed, under the question.
        # ------------------------------------------------------------------
        card_rect = RoundedRectangle(
            corner_radius=0.25,
            width=9.4,
            height=1.7,
            fill_color=SURFACE,
            fill_opacity=0.95,
            stroke_color=TEXT,
            stroke_width=1.5,
        )
        card_rect.move_to(CARD_POS)
        card_text = Text(
            "Rebuild the meter from memory.\nWhich two operations?",
            font=FONT_BODY,
            font_size=28,
            color=TEXT,
            line_spacing=1.2,
        )
        if card_text.width > card_rect.width - 0.8:
            card_text.scale_to_fit_width(card_rect.width - 0.8)
        card_text.move_to(card_rect.get_center())

        self.play(
            FadeIn(card_rect),
            FadeIn(card_text),
            arc.animate.set_opacity(0.4),
            op_tracker.animate.set_value(0.4),
            pivot.animate.set_opacity(0.4),
            run_time=1.2,
        )
        self.wait(6.0)

        self.play(FadeOut(card_rect), FadeOut(card_text), run_time=0.7)
        self.wait(0.4)

        # ------------------------------------------------------------------
        # Different aisle: the song columns become "you" and "the role".
        # ------------------------------------------------------------------
        header_you = Text("you", font=FONT_BODY, font_size=30, color=TEXT)
        header_you.move_to(np.array([YOU_X, HEADER_Y, 0.0]))
        header_role = Text("the role", font=FONT_BODY, font_size=30, color=TEXT)
        header_role.move_to(np.array([ROLE_X, HEADER_Y, 0.0]))
        self.play(FadeIn(header_you), FadeIn(header_role), run_time=0.7)

        row_labels = []
        you_vals = []
        role_vals = []
        for (name, you_v, role_v), y in zip(ROWS, ROW_YS):
            label = Text(name, font=FONT_BODY, font_size=28, color=TEXT)
            label.move_to(np.array([LABEL_X, y, 0.0]))
            you_text = Text(str(you_v), font=FONT_MONO, font_size=30, color=DATA_OBSERVED)
            you_text.move_to(np.array([YOU_X, y, 0.0]))
            role_text = Text(str(role_v), font=FONT_MONO, font_size=30, color=DATA_OBSERVED)
            role_text.move_to(np.array([ROLE_X, y, 0.0]))
            self.play(FadeIn(label), FadeIn(you_text), FadeIn(role_text), run_time=0.55)
            row_labels.append(label)
            you_vals.append(you_text)
            role_vals.append(role_text)

        self.wait(1.5)

        # ------------------------------------------------------------------
        # Matched entries multiply, row by row.
        # ------------------------------------------------------------------
        products = [you_v * role_v for _, you_v, role_v in ROWS]
        prod_texts = []
        for (_, _, _), y, prod in zip(ROWS, ROW_YS, products):
            prod_texts.append(
                Text(str(prod), font=FONT_MONO, font_size=30, color=DATA_PARAMS).move_to(
                    np.array([PROD_X, y, 0.0])
                )
            )

        self.play(
            ReplacementTransform(you_vals[0], prod_texts[0]),
            FadeOut(role_vals[0]),
            ReplacementTransform(you_vals[1], prod_texts[1]),
            FadeOut(role_vals[1]),
            ReplacementTransform(you_vals[2], prod_texts[2]),
            FadeOut(role_vals[2]),
            run_time=1.3,
        )
        self.play(
            ReplacementTransform(you_vals[3], prod_texts[3]),
            FadeOut(role_vals[3]),
            ReplacementTransform(you_vals[4], prod_texts[4]),
            FadeOut(role_vals[4]),
            ReplacementTransform(you_vals[5], prod_texts[5]),
            FadeOut(role_vals[5]),
            run_time=1.3,
        )
        self.wait(0.8)

        # ------------------------------------------------------------------
        # They pool into one number, on the very same dial.
        # ------------------------------------------------------------------
        caption = Text(
            "two arrows in, one number out", font=FONT_BODY, font_size=28, color=DATA_PARAMS
        )
        caption.move_to(CAPTION_POS)
        readout = Text(
            str(sum(products)), font=FONT_MONO, font_size=36, color=DATA_PARAMS
        )
        readout.move_to(READOUT_POS)

        self.play(
            FadeOut(header_you),
            FadeOut(header_role),
            *[FadeOut(label) for label in row_labels],
            *[FadeOut(p) for p in prod_texts],
            arc.animate.set_opacity(1.0),
            op_tracker.animate.set_value(1.0),
            pivot.animate.set_opacity(1.0),
            meter_angle.animate.set_value(FINAL_ANGLE),
            FadeIn(readout),
            FadeIn(caption),
            run_time=2.2,
        )
        self.wait(2.5)

        # ------------------------------------------------------------------
        # Different aisle, same meter.
        # ------------------------------------------------------------------
        closing_line = Text(
            "Different aisle, same meter", font=FONT_BODY, font_size=36, color=TEXT
        )
        if closing_line.width > 11.5:
            closing_line.scale_to_fit_width(11.5)
        closing_line.move_to(CLOSING_POS)

        self.play(
            arc.animate.set_opacity(0.4),
            op_tracker.animate.set_value(0.4),
            pivot.animate.set_opacity(0.4),
            readout.animate.set_opacity(0.4),
            caption.animate.set_opacity(0.4),
            FadeIn(closing_line),
            run_time=1.3,
        )
        self.wait(6.9)
