import sys
from pathlib import Path

from manim import *  # noqa: F403

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "shared" / "manim"))
from bbox_dump import attach_bbox_dump  # noqa: E402
from colors import *  # noqa: E402,F403
from style import FONT_BODY, FONT_HEADING, FONT_MONO  # noqa: E402

import numpy as np  # noqa: E402


def _direction(theta_deg: float) -> np.ndarray:
    theta = np.radians(theta_deg)
    return np.array([np.cos(theta), np.sin(theta), 0.0])


# --- Layout constants (scene units, frame is 14.2 x 8, origin centered) ----

QUERY_BASE = np.array([0.0, 2.5, 0.0])
QUERY_LEN = 0.65

KEY_BASE_Y = -0.3
KEY_XS = [-4.8, -1.6, 1.6, 4.8]
KEY_ANGLES = [150.0, 110.0, 70.0, 30.0]
KEY_LEN = 0.9

BAR_BASELINE = -1.4
BAR_MAX_H = 1.0
BAR_W = 0.8
READOUT_Y = -2.0

SWEEP_START = 160.0
SWEEP_END = 20.0


class QkSimilarity(Scene):
    def construct(self):
        attach_bbox_dump(self)
        self.camera.background_color = BG

        theta = ValueTracker(SWEEP_START)

        def score(i: int) -> float:
            return float(np.cos(np.radians(theta.get_value() - KEY_ANGLES[i])))

        # --- Build the row of keys (static, held still, receded) ----------
        key_arrows = []
        key_labels = []
        for i, (x, ang) in enumerate(zip(KEY_XS, KEY_ANGLES)):
            base = np.array([x, KEY_BASE_Y, 0.0])
            tip = base + KEY_LEN * _direction(ang)
            arrow = Arrow(
                start=base,
                end=tip,
                buff=0,
                color=DATA_OBSERVED,
                stroke_width=6,
                tip_length=0.2,
            )
            arrow.set_opacity(0.55)
            label = Text(f"k{i + 1}", font=FONT_BODY, color=TEXT, font_size=32)
            label.set_opacity(0.85)
            label.move_to(tip + 0.35 * _direction(ang))
            key_arrows.append(arrow)
            key_labels.append(label)

        self.play(
            Create(key_arrows[0]),
            Write(key_labels[0]),
            Create(key_arrows[1]),
            Write(key_labels[1]),
            run_time=1.4,
        )
        self.play(
            Create(key_arrows[2]),
            Write(key_labels[2]),
            Create(key_arrows[3]),
            Write(key_labels[3]),
            run_time=1.4,
        )

        # --- Build the query vector (the single moving focus) -------------
        def query_tip() -> np.ndarray:
            return QUERY_BASE + QUERY_LEN * _direction(theta.get_value())

        query_arrow = Arrow(
            start=QUERY_BASE,
            end=query_tip(),
            buff=0,
            color=DATA_HEAT,
            stroke_width=7,
            tip_length=0.22,
        )
        query_label = Text("q", font=FONT_BODY, color=TEXT, font_size=34)
        query_label.move_to(query_tip() + 0.35 * _direction(theta.get_value()))

        self.play(Create(query_arrow), Write(query_label), run_time=1.2)

        # --- Build the score bars + readouts under each key ---------------
        def bar_rect(i: int) -> Rectangle:
            s = score(i)
            h = max(max(s, 0.0) * BAR_MAX_H, 0.02)
            opacity = 0.3 + 0.7 * max(s, 0.0)
            rect = Rectangle(
                width=BAR_W,
                height=h,
                fill_color=DATA_PARAMS,
                fill_opacity=opacity,
                stroke_opacity=0,
                stroke_width=0,
            )
            rect.move_to([KEY_XS[i], BAR_BASELINE + h / 2, 0.0])
            return rect

        def readout_text(i: int) -> Text:
            val = score(i)
            txt = Text(f"{val:+.2f}", font=FONT_MONO, color=TEXT, font_size=28)
            txt.move_to([KEY_XS[i], READOUT_Y, 0.0])
            return txt

        bars = [bar_rect(i) for i in range(4)]
        readouts = [readout_text(i) for i in range(4)]

        self.play(
            Create(bars[0]), Write(readouts[0]),
            Create(bars[1]), Write(readouts[1]),
            run_time=1.2,
        )
        self.play(
            Create(bars[2]), Write(readouts[2]),
            Create(bars[3]), Write(readouts[3]),
            run_time=1.2,
        )

        # --- Attach live updaters: the query rotates, everything else reacts
        def update_query_arrow(m):
            m.put_start_and_end_on(QUERY_BASE, query_tip())

        def update_query_label(m):
            m.move_to(query_tip() + 0.35 * _direction(theta.get_value()))

        query_arrow.add_updater(update_query_arrow)
        query_label.add_updater(update_query_label)

        def make_bar_updater(i):
            def _update(m):
                m.become(bar_rect(i))

            return _update

        def make_readout_updater(i):
            def _update(m):
                m.become(readout_text(i))

            return _update

        for i in range(4):
            bars[i].add_updater(make_bar_updater(i))
            readouts[i].add_updater(make_readout_updater(i))

        # --- The sweep: query rotates through directions, keys hold still -
        self.play(theta.animate.set_value(113.3), run_time=4.5, rate_func=linear)
        self.play(theta.animate.set_value(66.7), run_time=4.5, rate_func=linear)
        self.play(theta.animate.set_value(SWEEP_END), run_time=4.5, rate_func=linear)

        # --- Settle: the best-aligned key's bar leads at the final angle --
        query_arrow.clear_updaters()
        query_label.clear_updaters()
        for i in range(4):
            bars[i].clear_updaters()
            readouts[i].clear_updaters()

        self.play(
            Indicate(bars[3], color=DATA_PARAMS),
            Indicate(readouts[3], color=DATA_PARAMS),
            run_time=1.2,
        )
        self.wait(2.0)
