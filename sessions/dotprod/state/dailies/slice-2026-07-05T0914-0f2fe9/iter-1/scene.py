import sys
from pathlib import Path

from manim import *  # noqa: F403

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "shared" / "manim"))
from bbox_dump import attach_bbox_dump  # noqa: E402
from colors import *  # noqa: E402,F403
from style import FONT_BODY, FONT_HEADING, FONT_MONO  # noqa: E402,F401

import numpy as np  # noqa: E402

# ---------------------------------------------------------------------------
# Geometry constants
# ---------------------------------------------------------------------------

IDLE_CENTER = np.array([4.7, 3.1, 0.0])
IDLE_RADIUS = 0.65

CARD_CENTER = np.array([0.0, -0.3, 0.0])
CARD_WIDTH = 11.2
CARD_HEIGHT = 2.4

HEADER_Y = 3.3
ROW1_Y = 2.15
ROW2_Y = 1.0
ROW3_Y = -0.15

LABEL_X = -5.3
YOU_X = -2.6
TIMES_X = -0.9
ROLE_X = 0.8
EQ_X = 2.5
PROD_X = 4.4

METER_CENTER = np.array([0.0, -2.0, 0.0])
RADIUS = 1.05
NEEDLE_LEN = 0.95
MAX_SCORE = 90.0

READOUT_POS = np.array([0.0, -2.75, 0.0])
LABEL_POS = np.array([0.0, -3.45, 0.0])
CLOSING_POS = np.array([0.0, 1.6, 0.0])


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
        stroke_width=6,
        max_tip_length_to_length_ratio=0.28,
        max_stroke_width_to_length_ratio=20,
    )


class Beat04(Scene):
    def construct(self):
        attach_bbox_dump(self)
        self.camera.background_color = BG

        # ------------------------------------------------------------------
        # Phase A: the meter idles (small, dim) while the card asks the
        # actual question.
        # ------------------------------------------------------------------
        idle_arc = Arc(
            radius=IDLE_RADIUS,
            start_angle=PI,
            angle=-PI,
            arc_center=IDLE_CENTER,
            color=DATA_PARAMS,
            stroke_width=5,
        )
        idle_needle = make_arrow(IDLE_CENTER, 120.0, IDLE_RADIUS * 0.85, DATA_PARAMS)
        idle_pivot = Dot(IDLE_CENTER, radius=0.05, color=DATA_PARAMS)
        for m in (idle_arc, idle_needle, idle_pivot):
            m.set_opacity(0.35)

        self.play(Create(idle_arc), GrowArrow(idle_needle), FadeIn(idle_pivot), run_time=1.0)

        card_rect = RoundedRectangle(
            width=CARD_WIDTH,
            height=CARD_HEIGHT,
            corner_radius=0.22,
            color=TEXT,
            stroke_width=2,
            fill_color=SURFACE,
            fill_opacity=1.0,
        ).move_to(CARD_CENTER)

        q_line1 = Text("Two arrows go in.", font=FONT_BODY, font_size=32, color=TEXT)
        q_line2 = Text(
            "What two operations turn them into the score?",
            font=FONT_BODY,
            font_size=32,
            color=TEXT,
        )
        question = VGroup(q_line1, q_line2).arrange(DOWN, buff=0.3)
        if question.width > CARD_WIDTH - 1.2:
            question.scale_to_fit_width(CARD_WIDTH - 1.2)
        question.move_to(CARD_CENTER)

        self.play(FadeIn(card_rect), FadeIn(q_line1), FadeIn(q_line2), run_time=1.2)
        self.wait(5.5)

        self.play(
            FadeOut(idle_arc),
            FadeOut(idle_needle),
            FadeOut(idle_pivot),
            FadeOut(card_rect),
            FadeOut(q_line1),
            FadeOut(q_line2),
            run_time=0.6,
        )

        # ------------------------------------------------------------------
        # Phase B: same meter, different aisle. Two columns, three rows.
        # ------------------------------------------------------------------
        header_you = Text("you", font=FONT_BODY, font_size=30, color=DATA_OBSERVED)
        header_you.move_to([YOU_X, HEADER_Y, 0.0])
        header_role = Text("the role", font=FONT_BODY, font_size=30, color=DATA_OBSERVED)
        header_role.move_to([ROLE_X, HEADER_Y, 0.0])
        self.play(FadeIn(header_you), FadeIn(header_role), run_time=0.6)

        rows_data = [
            ("Python hours", 8, 6, ROW1_Y),
            ("SQL reps", 5, 4, ROW2_Y),
            ("nights free", 3, 1, ROW3_Y),
        ]

        labels, yous, roles = [], [], []
        for name, you_val, role_val, y in rows_data:
            label = Text(name, font=FONT_BODY, font_size=30, color=TEXT)
            label.move_to([LABEL_X, y, 0.0])
            you_t = Text(str(you_val), font=FONT_MONO, font_size=34, color=DATA_OBSERVED)
            you_t.move_to([YOU_X, y, 0.0])
            role_t = Text(str(role_val), font=FONT_MONO, font_size=34, color=DATA_OBSERVED)
            role_t.move_to([ROLE_X, y, 0.0])
            self.play(FadeIn(label), FadeIn(you_t), FadeIn(role_t), run_time=0.7)
            labels.append(label)
            yous.append(you_t)
            roles.append(role_t)

        self.wait(2.0)

        times_syms = []
        for _, _, _, y in rows_data:
            t = Text("×", font=FONT_MONO, font_size=34, color=TEXT)
            t.move_to([TIMES_X, y, 0.0])
            times_syms.append(t)
        self.play(*[FadeIn(t) for t in times_syms], run_time=0.5)

        eq_syms = []
        for _, _, _, y in rows_data:
            e = Text("=", font=FONT_MONO, font_size=34, color=TEXT)
            e.move_to([EQ_X, y, 0.0])
            eq_syms.append(e)
        self.play(*[FadeIn(e) for e in eq_syms], run_time=0.5)

        products = []
        transforms = []
        for i, (name, you_val, role_val, y) in enumerate(rows_data):
            prod_val = you_val * role_val
            prod_t = Text(str(prod_val), font=FONT_MONO, font_size=34, color=DATA_PARAMS)
            prod_t.move_to([PROD_X, y, 0.0])
            source = VGroup(yous[i], times_syms[i], roles[i], eq_syms[i])
            transforms.append(TransformFromCopy(source, prod_t))
            products.append(prod_t)
        self.play(*transforms, run_time=1.2)
        self.wait(0.8)

        # ------------------------------------------------------------------
        # Phase C: the dial reappears. Products pool into one readout.
        # ------------------------------------------------------------------
        table_dim_group = VGroup(
            header_you, header_role, *labels, *yous, *roles, *times_syms, *eq_syms
        )

        arc = Arc(
            radius=RADIUS,
            start_angle=PI,
            angle=-PI,
            arc_center=METER_CENTER,
            color=DATA_PARAMS,
            stroke_width=8,
        )
        meter_angle = ValueTracker(180.0)

        def build_needle():
            return make_arrow(METER_CENTER, meter_angle.get_value(), NEEDLE_LEN, DATA_PARAMS)

        needle = build_needle()
        pivot = Dot(METER_CENTER, radius=0.06, color=DATA_PARAMS)

        self.play(
            table_dim_group.animate.set_opacity(0.35),
            Create(arc),
            GrowArrow(needle),
            FadeIn(pivot),
            run_time=1.2,
        )
        needle.add_updater(lambda m: m.become(build_needle()))
        self.wait(0.8)

        total = sum(y * r for _, y, r, _ in rows_data)
        target_angle = 180.0 * (1.0 - total / MAX_SCORE)

        sum_readout = Text(str(total), font=FONT_MONO, font_size=40, color=DATA_PARAMS)
        sum_readout.move_to(READOUT_POS)

        self.play(
            ReplacementTransform(VGroup(*products), sum_readout),
            meter_angle.animate.set_value(target_angle),
            run_time=1.6,
        )
        needle.clear_updaters()
        self.wait(1.0)

        readout_label = Text(
            "two arrows in, one number out", font=FONT_BODY, font_size=26, color=TEXT
        )
        readout_label.move_to(LABEL_POS)
        self.play(FadeIn(readout_label), run_time=0.8)
        self.wait(2.5)

        # ------------------------------------------------------------------
        # Phase D: the table clears; the closing line lands.
        # ------------------------------------------------------------------
        closing = Text(
            "Different aisle, same meter", font=FONT_BODY, font_size=34, color=TEXT
        )
        if closing.width > 11.5:
            closing.scale_to_fit_width(11.5)
        closing.move_to(CLOSING_POS)

        self.play(FadeOut(table_dim_group), FadeIn(closing), run_time=1.0)
        self.wait(6.2)
