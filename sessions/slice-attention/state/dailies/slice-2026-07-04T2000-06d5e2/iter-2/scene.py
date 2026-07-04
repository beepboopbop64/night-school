import sys
from pathlib import Path

import numpy as np
from manim import *  # noqa: F403

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "shared" / "manim"))
from bbox_dump import attach_bbox_dump  # noqa: E402
from colors import *  # noqa: E402,F403
from style import FONT_BODY, FONT_HEADING, FONT_MONO  # noqa: E402


def _tip(base: np.ndarray, radius: float, deg: float) -> np.ndarray:
    theta = np.deg2rad(deg)
    return base + radius * np.array([np.cos(theta), np.sin(theta), 0.0])


def _score_fn(query_angle: ValueTracker, key_deg: float):
    key_theta = np.deg2rad(key_deg)
    kv = np.array([np.cos(key_theta), np.sin(key_theta)])

    def get_score() -> float:
        q_theta = np.deg2rad(query_angle.get_value())
        qv = np.array([np.cos(q_theta), np.sin(q_theta)])
        return float(np.dot(qv, kv))

    return get_score


class QkSimilarity(Scene):
    def construct(self):
        attach_bbox_dump(self)
        self.camera.background_color = BG

        # ---- geometry constants -------------------------------------------------
        query_base = np.array([0.0, 2.4, 0.0])
        query_radius = 1.0
        angles_seq = [0.0, 45.0, 90.0, 135.0, 180.0]

        key_degs = [20.0, 60.0, 100.0, 140.0]
        key_xs = [-5.2, -1.75, 1.75, 5.2]
        key_base_y = 0.6
        key_len = 0.9

        bar_baseline_y = -1.6
        bar_max_h = 1.2
        bar_width = 0.6
        readout_y = 0.15

        query_angle = ValueTracker(angles_seq[0])

        # ---- query vector (single focus) -----------------------------------------
        query_tip0 = _tip(query_base, query_radius, angles_seq[0])
        query_arrow = Arrow(
            start=query_base,
            end=query_tip0,
            buff=0,
            color=DATA_HEAT,
            stroke_width=9,
            max_tip_length_to_length_ratio=0.28,
        )
        query_label = Text("q", font=FONT_BODY, color=TEXT, font_size=34)
        query_label.move_to(query_tip0 + 0.4 * (query_tip0 - query_base) / query_radius)

        self.play(Create(query_arrow), Write(query_label), run_time=1.0)

        def query_arrow_updater(mob):
            tip = _tip(query_base, query_radius, query_angle.get_value())
            mob.put_start_and_end_on(query_base, tip)

        def query_label_updater(mob):
            tip = _tip(query_base, query_radius, query_angle.get_value())
            direction = (tip - query_base) / query_radius
            mob.move_to(tip + 0.4 * direction)

        query_arrow.add_updater(query_arrow_updater)
        query_label.add_updater(query_label_updater)

        # ---- keys: fixed direction, held row ---------------------------------------
        key_arrows = []
        key_labels = []
        score_fns = []
        for i, (deg, x) in enumerate(zip(key_degs, key_xs)):
            base = np.array([x, key_base_y, 0.0])
            tip = _tip(base, key_len, deg)
            arrow = Arrow(
                start=base,
                end=tip,
                buff=0,
                color=DATA_OBSERVED,
                stroke_width=6,
                max_tip_length_to_length_ratio=0.3,
            )
            label = Text(f"k{i + 1}", font=FONT_BODY, color=TEXT, font_size=28)
            direction = (tip - base) / key_len
            label.move_to(tip + 0.35 * direction)
            key_arrows.append(arrow)
            key_labels.append(label)
            score_fns.append(_score_fn(query_angle, deg))

        self.play(
            Create(key_arrows[0]),
            Write(key_labels[0]),
            Create(key_arrows[1]),
            Write(key_labels[1]),
            run_time=1.2,
        )
        self.play(
            Create(key_arrows[2]),
            Write(key_labels[2]),
            Create(key_arrows[3]),
            Write(key_labels[3]),
            run_time=1.2,
        )

        def make_key_updater(get_score):
            def updater(mob):
                norm = (get_score() + 1.0) / 2.0
                mob.set_opacity(0.35 + 0.65 * norm)

            return updater

        def make_label_updater(get_score):
            def updater(mob):
                norm = (get_score() + 1.0) / 2.0
                mob.set_opacity(0.55 + 0.45 * norm)

            return updater

        for arrow, label, get_score in zip(key_arrows, key_labels, score_fns):
            arrow.add_updater(make_key_updater(get_score))
            label.add_updater(make_label_updater(get_score))

        # ---- score bars + numeric readouts ------------------------------------------
        bars = []
        readouts = []
        for i, (x, get_score) in enumerate(zip(key_xs, score_fns)):
            s0 = get_score()
            norm0 = (s0 + 1.0) / 2.0
            h0 = max(0.05, norm0 * bar_max_h)
            bar = Rectangle(
                width=bar_width,
                height=h0,
                stroke_width=0,
                fill_color=DATA_PARAMS,
                fill_opacity=0.35 + 0.65 * norm0,
            )
            bar.move_to(np.array([x, bar_baseline_y + h0 / 2.0, 0.0]))
            readout = Text(f"{s0:+.2f}", font=FONT_MONO, color=DATA_PARAMS, font_size=28)
            readout.move_to(np.array([x, readout_y, 0.0]))
            bars.append(bar)
            readouts.append(readout)

        self.play(
            Create(bars[0]), Write(readouts[0]), Create(bars[1]), Write(readouts[1]), run_time=1.0
        )
        self.play(
            Create(bars[2]), Write(readouts[2]), Create(bars[3]), Write(readouts[3]), run_time=1.0
        )

        def make_bar_updater(x, get_score):
            def updater(mob):
                norm = (get_score() + 1.0) / 2.0
                h = max(0.05, norm * bar_max_h)
                mob.stretch_to_fit_height(h)
                mob.move_to(np.array([x, bar_baseline_y + h / 2.0, 0.0]))
                mob.set_fill(color=DATA_PARAMS, opacity=0.35 + 0.65 * norm)

            return updater

        def make_readout_updater(x, get_score):
            def updater(mob):
                new = Text(
                    f"{get_score():+.2f}", font=FONT_MONO, color=DATA_PARAMS, font_size=28
                )
                new.move_to(np.array([x, readout_y, 0.0]))
                mob.become(new)

            return updater

        for x, bar, readout, get_score in zip(key_xs, bars, readouts, score_fns):
            bar.add_updater(make_bar_updater(x, get_score))
            readout.add_updater(make_readout_updater(x, get_score))

        # ---- the sweep: query rotates, scores live-track it -----------------------
        # Driven by UpdateFromAlphaFunc (not ValueTracker.animate/Transform) so the
        # tracker's bare value is mutated directly each frame; this keeps the other
        # mobjects' live updaters (arrow, keys, bars, readouts) in sync without
        # touching any Transform/align_data machinery.
        def make_sweep_updater(start_deg: float, end_deg: float):
            def updater(mob, alpha):
                mob.set_value(start_deg + (end_deg - start_deg) * alpha)

            return updater

        current = angles_seq[0]
        for target in angles_seq[1:]:
            self.play(
                UpdateFromAlphaFunc(query_angle, make_sweep_updater(current, target)),
                run_time=4.0,
                rate_func=linear,
            )
            current = target

        self.wait(2.6)
