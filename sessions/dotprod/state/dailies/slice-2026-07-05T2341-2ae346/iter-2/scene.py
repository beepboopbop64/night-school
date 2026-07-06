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
ORIGIN = np.array([0.0, 1.3, 0.0])
PROBE_LEN = 1.8
PROBE_START_ANGLE = 85.0
PROBE_END_ANGLE = -85.0

C1_ANGLE = 80.0
C1_LEN_START = 1.4
C1_LEN_END = 2.6
C2_ANGLE, C2_LEN = 30.0, 1.8
C3_ANGLE, C3_LEN = -20.0, 1.6
C4_ANGLE, C4_LEN = -70.0, 1.3

BASELINE_Y = -1.8
BAR_W = 0.6
SCALE = 0.22
MAX_H = 1.0
BAR_XS = (-4.2, -1.4, 1.4, 4.2)


def direction(angle_deg: float) -> np.ndarray:
    rad = np.radians(angle_deg)
    return np.array([np.cos(rad), np.sin(rad), 0.0])


def perp_of(angle_deg: float) -> np.ndarray:
    rad = np.radians(angle_deg)
    return np.array([-np.sin(rad), np.cos(rad), 0.0])


def arrow_for(angle_deg: float, length: float, color: str) -> Arrow:
    end = ORIGIN + direction(angle_deg) * length
    return Arrow(
        ORIGIN,
        end,
        buff=0,
        color=color,
        stroke_width=5,
        max_tip_length_to_length_ratio=0.22,
        max_stroke_width_to_length_ratio=20,
    )


def label_pos(angle_deg: float, length: float) -> np.ndarray:
    tip = ORIGIN + direction(angle_deg) * length
    pos = tip + perp_of(angle_deg) * 0.45 + direction(angle_deg) * 0.15
    # Safety clamp: never let a label drift toward the frame edge (frame is
    # 14.2 x 8 units centered on the origin).
    pos[0] = float(np.clip(pos[0], -6.4, 6.4))
    pos[1] = float(np.clip(pos[1], -3.4, 3.4))
    return pos


class Beat02(Scene):
    def construct(self):
        attach_bbox_dump(self)
        self.camera.background_color = BG

        # -- trackers driving every dynamic element -------------------------
        probe_angle = ValueTracker(PROBE_START_ANGLE)
        c1_len = ValueTracker(C1_LEN_START)
        final_state = {"locked": False}

        def score_c1() -> float:
            return PROBE_LEN * c1_len.get_value() * np.cos(
                np.radians(probe_angle.get_value() - C1_ANGLE)
            )

        def score_c2() -> float:
            return PROBE_LEN * C2_LEN * np.cos(
                np.radians(probe_angle.get_value() - C2_ANGLE)
            )

        def score_c3() -> float:
            return PROBE_LEN * C3_LEN * np.cos(
                np.radians(probe_angle.get_value() - C3_ANGLE)
            )

        def score_c4() -> float:
            return PROBE_LEN * C4_LEN * np.cos(
                np.radians(probe_angle.get_value() - C4_ANGLE)
            )

        # -- origin marker ------------------------------------------------------
        origin_dot = Dot(ORIGIN, radius=0.05, color=TEXT)

        # -- probe: feature numbers fold into an arrow ---------------------------
        probe_base = ORIGIN + direction(PROBE_START_ANGLE) * 1.1
        probe_feat1 = Text("timbre: 0.9", font=FONT_MONO, font_size=26, color=TEXT)
        probe_feat1.move_to(probe_base + np.array([0.0, 0.28, 0.0]))
        probe_feat2 = Text("tempo: 0.6", font=FONT_MONO, font_size=26, color=TEXT)
        probe_feat2.move_to(probe_base + np.array([0.0, -0.28, 0.0]))

        self.play(FadeIn(origin_dot), FadeIn(probe_feat1), FadeIn(probe_feat2), run_time=1.5)

        def build_probe_arrow():
            return arrow_for(probe_angle.get_value(), PROBE_LEN, DATA_HEAT)

        probe_arrow = build_probe_arrow()
        self.play(
            FadeOut(probe_feat1),
            FadeOut(probe_feat2),
            GrowArrow(probe_arrow),
            run_time=1.5,
        )
        probe_arrow.add_updater(lambda m: m.become(build_probe_arrow()))

        probe_label = Text("probe", font=FONT_BODY, font_size=28, color=TEXT)
        probe_label.move_to(ORIGIN + np.array([-1.3, 0.0, 0.0]))
        self.play(FadeIn(probe_label), run_time=1.0)

        # -- candidate c1: feature numbers fold into an arrow --------------------
        c1_base = ORIGIN + direction(C1_ANGLE) * 1.1
        c1_feat1 = Text("brightness: 0.7", font=FONT_MONO, font_size=26, color=TEXT)
        c1_feat1.move_to(c1_base + np.array([0.35, 0.28, 0.0]))
        c1_feat2 = Text("energy: 1.1", font=FONT_MONO, font_size=26, color=TEXT)
        c1_feat2.move_to(c1_base + np.array([0.35, -0.28, 0.0]))
        self.play(FadeIn(c1_feat1), FadeIn(c1_feat2), run_time=1.2)

        def build_c1_arrow():
            return arrow_for(C1_ANGLE, c1_len.get_value(), DATA_OBSERVED)

        c1_arrow = build_c1_arrow()
        self.play(
            FadeOut(c1_feat1),
            FadeOut(c1_feat2),
            GrowArrow(c1_arrow),
            run_time=1.5,
        )
        c1_arrow.add_updater(lambda m: m.become(build_c1_arrow()))

        # c1's label is pinned to its *starting* length so that stretching the
        # arrow later (the length-handle drag) never pushes the label toward
        # the frame edge; the label only ever needs to stay clear of the
        # candidate's own arrow, not chase a growing tip.
        c1_label_anchor = label_pos(C1_ANGLE, C1_LEN_START)
        c1_label = Text("c1", font=FONT_BODY, font_size=28, color=TEXT)
        c1_label.move_to(c1_label_anchor)
        self.play(FadeIn(c1_label), run_time=0.8)

        # -- candidates c2, c3, c4: appear directly as arrows --------------------
        c2_arrow = arrow_for(C2_ANGLE, C2_LEN, DATA_OBSERVED)
        c2_label = Text("c2", font=FONT_BODY, font_size=28, color=TEXT)
        c2_label.move_to(label_pos(C2_ANGLE, C2_LEN))
        self.play(GrowArrow(c2_arrow), FadeIn(c2_label), run_time=1.2)

        c3_arrow = arrow_for(C3_ANGLE, C3_LEN, DATA_OBSERVED)
        c3_label = Text("c3", font=FONT_BODY, font_size=28, color=TEXT)
        c3_label.move_to(label_pos(C3_ANGLE, C3_LEN))
        self.play(GrowArrow(c3_arrow), FadeIn(c3_label), run_time=1.2)

        c4_arrow = arrow_for(C4_ANGLE, C4_LEN, DATA_OBSERVED)
        c4_label = Text("c4", font=FONT_BODY, font_size=28, color=TEXT)
        c4_label.move_to(label_pos(C4_ANGLE, C4_LEN))
        self.play(GrowArrow(c4_arrow), FadeIn(c4_label), run_time=1.2)

        self.wait(2.5)

        # -- prediction card, before any turning ---------------------------------
        card_rect = RoundedRectangle(
            corner_radius=0.25,
            width=6.8,
            height=1.7,
            fill_color=SURFACE,
            fill_opacity=0.95,
            stroke_color=TEXT,
            stroke_width=1.5,
        )
        card_rect.move_to(np.array([0.0, BASELINE_Y, 0.0]))
        card_text = Text(
            "Which candidate tops out?\nCan a score go negative?",
            font=FONT_BODY,
            font_size=28,
            color=TEXT,
            line_spacing=1.2,
        )
        card_text.move_to(card_rect.get_center())

        self.play(FadeIn(card_rect), FadeIn(card_text), run_time=1.5)
        self.wait(8.0)
        self.play(FadeOut(card_rect), FadeOut(card_text), run_time=1.0)

        # -- score bars appear, matching the static prediction moment -----------
        def make_bar(x: float, score_fn):
            def build():
                s = score_fn()
                h = max(min(abs(s) * SCALE, MAX_H), 0.02)
                rect = Rectangle(
                    width=BAR_W,
                    height=h,
                    stroke_width=0,
                    fill_color=DATA_PARAMS,
                    fill_opacity=0.9,
                )
                cy = BASELINE_Y + h / 2 if s >= 0 else BASELINE_Y - h / 2
                rect.move_to(np.array([x, cy, 0.0]))
                return rect

            return build

        def make_readout(x: float, score_fn):
            def build():
                s = score_fn()
                h = min(abs(s) * SCALE, MAX_H)
                y = BASELINE_Y + h + 0.35 if s >= 0 else BASELINE_Y - h - 0.35
                text = f"{round(s):+d}" if final_state["locked"] else f"{s:+.1f}"
                return Text(
                    text, font=FONT_MONO, font_size=26, color=DATA_PARAMS
                ).move_to(np.array([x, y, 0.0]))

            return build

        bar1_build = make_bar(BAR_XS[0], score_c1)
        readout1_build = make_readout(BAR_XS[0], score_c1)
        bar1 = bar1_build()
        readout1 = readout1_build()
        label1 = Text("c1", font=FONT_BODY, font_size=26, color=TEXT)
        label1.move_to(np.array([BAR_XS[0], BASELINE_Y - MAX_H - 0.45, 0.0]))
        self.play(FadeIn(bar1), FadeIn(readout1), FadeIn(label1), run_time=0.8)
        bar1.add_updater(lambda m: m.become(bar1_build()))
        readout1.add_updater(lambda m: m.become(readout1_build()))

        bar2_build = make_bar(BAR_XS[1], score_c2)
        readout2_build = make_readout(BAR_XS[1], score_c2)
        bar2 = bar2_build()
        readout2 = readout2_build()
        label2 = Text("c2", font=FONT_BODY, font_size=26, color=TEXT)
        label2.move_to(np.array([BAR_XS[1], BASELINE_Y - MAX_H - 0.45, 0.0]))
        self.play(FadeIn(bar2), FadeIn(readout2), FadeIn(label2), run_time=0.8)
        bar2.add_updater(lambda m: m.become(bar2_build()))
        readout2.add_updater(lambda m: m.become(readout2_build()))

        bar3_build = make_bar(BAR_XS[2], score_c3)
        readout3_build = make_readout(BAR_XS[2], score_c3)
        bar3 = bar3_build()
        readout3 = readout3_build()
        label3 = Text("c3", font=FONT_BODY, font_size=26, color=TEXT)
        label3.move_to(np.array([BAR_XS[2], BASELINE_Y - MAX_H - 0.45, 0.0]))
        self.play(FadeIn(bar3), FadeIn(readout3), FadeIn(label3), run_time=0.8)
        bar3.add_updater(lambda m: m.become(bar3_build()))
        readout3.add_updater(lambda m: m.become(readout3_build()))

        bar4_build = make_bar(BAR_XS[3], score_c4)
        readout4_build = make_readout(BAR_XS[3], score_c4)
        bar4 = bar4_build()
        readout4 = readout4_build()
        label4 = Text("c4", font=FONT_BODY, font_size=26, color=TEXT)
        label4.move_to(np.array([BAR_XS[3], BASELINE_Y - MAX_H - 0.45, 0.0]))
        self.play(FadeIn(bar4), FadeIn(readout4), FadeIn(label4), run_time=0.8)
        bar4.add_updater(lambda m: m.become(bar4_build()))
        readout4.add_updater(lambda m: m.become(readout4_build()))

        self.wait(2.0)

        # -- sweep 1: turn the probe across every candidate ----------------------
        self.play(
            probe_angle.animate.set_value(PROBE_END_ANGLE),
            run_time=26.0,
            rate_func=linear,
        )
        self.wait(4.0)

        # -- sweep 2: turn back, ending parked exactly on c1 ----------------------
        self.play(
            probe_angle.animate.set_value(C1_ANGLE),
            run_time=18.0,
            rate_func=linear,
        )
        self.wait(4.0)

        # -- length handle: drag c1 longer, direction unchanged --------------------
        def build_handle():
            return Dot(
                ORIGIN + direction(C1_ANGLE) * c1_len.get_value(),
                radius=0.07,
                color=TEXT,
            )

        handle_dot = build_handle()
        self.play(FadeIn(handle_dot), run_time=1.0)
        handle_dot.add_updater(lambda m: m.become(build_handle()))

        self.play(c1_len.animate.set_value(C1_LEN_END), run_time=14.0, rate_func=smooth)
        self.wait(3.0)

        # -- final: probe stays parked, scores land as integers --------------------
        final_state["locked"] = True
        self.wait(4.0)
        self.wait(11.0)
