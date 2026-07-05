import sys
from pathlib import Path

from manim import *  # noqa: F403

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "shared" / "manim"))
from bbox_dump import attach_bbox_dump  # noqa: E402
from colors import *  # noqa: E402,F403
from style import FONT_BODY, FONT_HEADING, FONT_MONO  # noqa: E402,F401
from style import roughen, true_up, wobble_once  # noqa: E402

import numpy as np  # noqa: E402

# ---------------------------------------------------------------------------
# Geometry constants
# ---------------------------------------------------------------------------
TOP_ORIGIN = np.array([0.0, 1.5, 0.0])
PROBE_OFFSET = np.array([0.4, 0.0, 0.0])
CAND_LEN = 1.2
PROBE_LEN = 1.2
CAND_ANGLE = 90.0

LABEL_POS = np.array([0.0, 3.3, 0.0])
SCORE_POS = np.array([0.0, -0.6, 0.0])

METER_CENTER = np.array([0.0, -0.4, 0.0])
RADIUS = 2.2
TICK_OFFSET = 0.7
NEEDLE_LEN = 2.0
MAX_SCORE = 2.4

ANNOT_POS = np.array([0.0, -1.0, 0.0])
READOUT_POS = np.array([0.0, -1.75, 0.0])
SENTENCE_POS = np.array([0.0, -2.7, 0.0])


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
        max_tip_length_to_length_ratio=0.24,
        max_stroke_width_to_length_ratio=20,
    )


def score_of(angle_deg: float) -> float:
    return MAX_SCORE * np.cos(np.radians(angle_deg))


def fmt_score(value: float) -> str:
    if abs(value) < 0.005:
        return "0.00"
    return f"{value:+.2f}"


class Beat03(Scene):
    def construct(self):
        attach_bbox_dump(self)
        self.camera.background_color = BG

        # ------------------------------------------------------------------
        # Recap: one candidate, one probe, three frozen orientations.
        # ------------------------------------------------------------------
        probe_angle = ValueTracker(90.0)

        candidate_arrow = make_arrow(TOP_ORIGIN, CAND_ANGLE, CAND_LEN, DATA_OBSERVED)
        self.play(GrowArrow(candidate_arrow), run_time=1.0)

        def build_probe_arrow():
            return make_arrow(
                TOP_ORIGIN + PROBE_OFFSET, probe_angle.get_value(), PROBE_LEN, DATA_HEAT
            )

        probe_arrow = build_probe_arrow()
        self.play(GrowArrow(probe_arrow), run_time=1.0)
        probe_arrow.add_updater(lambda m: m.become(build_probe_arrow()))

        def still(word: str, score: float):
            label = Text(word, font=FONT_BODY, font_size=32, color=TEXT)
            label.move_to(LABEL_POS)
            score_text = Text(
                fmt_score(score), font=FONT_MONO, font_size=32, color=DATA_PARAMS
            )
            score_text.move_to(SCORE_POS)
            return label, score_text

        label1, score1 = still("along", score_of(0.0))
        self.play(FadeIn(label1), FadeIn(score1), run_time=1.0)
        self.wait(1.3)

        self.play(FadeOut(label1), FadeOut(score1), run_time=0.4)
        self.play(probe_angle.animate.set_value(0.0), run_time=0.8)
        label2, score2 = still("across", score_of(90.0))
        self.play(FadeIn(label2), FadeIn(score2), run_time=1.0)
        self.wait(1.3)

        self.play(FadeOut(label2), FadeOut(score2), run_time=0.4)
        self.play(probe_angle.animate.set_value(-90.0), run_time=0.8)
        label3, score3 = still("against", score_of(180.0))
        self.play(FadeIn(label3), FadeIn(score3), run_time=1.0)
        self.wait(1.3)

        # ------------------------------------------------------------------
        # Collapse: the three stills become one lilac meter dial.
        # ------------------------------------------------------------------
        probe_arrow.clear_updaters()

        arc = Arc(
            radius=RADIUS,
            start_angle=PI,
            angle=-PI,
            arc_center=METER_CENTER,
            color=DATA_PARAMS,
            stroke_width=8,
        )
        self.play(
            FadeOut(candidate_arrow),
            FadeOut(probe_arrow),
            FadeOut(label3),
            FadeOut(score3),
            Create(arc),
            run_time=1.5,
        )

        oppose_label = Text("oppose", font=FONT_BODY, font_size=30, color=TEXT)
        oppose_label.move_to(METER_CENTER + direction(180.0) * (RADIUS + TICK_OFFSET))
        ignore_label = Text("ignore", font=FONT_BODY, font_size=30, color=TEXT)
        ignore_label.move_to(METER_CENTER + direction(90.0) * (RADIUS + TICK_OFFSET))
        agree_label = Text("agree", font=FONT_BODY, font_size=30, color=TEXT)
        agree_label.move_to(METER_CENTER + direction(0.0) * (RADIUS + TICK_OFFSET))
        self.play(
            FadeIn(oppose_label), FadeIn(ignore_label), FadeIn(agree_label), run_time=1.2
        )

        # ------------------------------------------------------------------
        # Needle, pivot, and the score readout with its dot-product tag.
        # ------------------------------------------------------------------
        meter_angle = ValueTracker(180.0)

        def build_needle():
            return make_arrow(METER_CENTER, meter_angle.get_value(), NEEDLE_LEN, DATA_PARAMS)

        needle = build_needle()
        pivot = Dot(METER_CENTER, radius=0.07, color=DATA_PARAMS)
        annotation = Text("a · b", font=FONT_MONO, font_size=26, color=DATA_PARAMS)
        annotation.move_to(ANNOT_POS)

        def build_readout():
            s = score_of(meter_angle.get_value())
            return Text(
                fmt_score(s), font=FONT_MONO, font_size=36, color=DATA_PARAMS
            ).move_to(READOUT_POS)

        readout = build_readout()
        self.play(
            GrowArrow(needle), FadeIn(pivot), FadeIn(annotation), FadeIn(readout), run_time=1.3
        )
        needle.add_updater(lambda m: m.become(build_needle()))
        readout.add_updater(lambda m: m.become(build_readout()))

        self.wait(1.0)

        # -- the needle swings: oppose -> ignore -> agree ------------------------
        self.play(meter_angle.animate.set_value(90.0), run_time=6.0, rate_func=linear)
        self.wait(1.0)
        self.play(meter_angle.animate.set_value(0.0), run_time=6.0, rate_func=linear)
        self.wait(2.0)

        # ------------------------------------------------------------------
        # The aha sentence trues up beneath the dial.
        # ------------------------------------------------------------------
        sentence = Text(
            "the dot product is a similarity meter",
            font=FONT_BODY,
            font_size=34,
            color=TEXT,
        )
        if sentence.width > 11.5:
            sentence.scale_to_fit_width(11.5)
        sentence.move_to(SENTENCE_POS)
        self.play(FadeIn(sentence), run_time=1.5)

        underline_y = sentence.get_bottom()[1] - 0.3
        underline = Line(
            np.array([sentence.get_left()[0], underline_y, 0.0]),
            np.array([sentence.get_right()[0], underline_y, 0.0]),
            color=TEXT,
            stroke_width=4,
        )
        underline.insert_n_curves(15)
        roughen(underline)
        self.play(Create(underline), run_time=1.0)
        self.play(wobble_once(underline), run_time=0.5)
        self.play(true_up(underline, settle_color=DATA_FIT, glow_color=DATA_FIT))

        self.wait(3.2)
