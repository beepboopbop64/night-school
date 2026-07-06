"""Hand-built mock stills for the Similarity Meter video, Section 2.

The judge's visual vocabulary for the approved script (2026-07-06):
QualityColumn, sum meters, match checks, product chips, the scorebox.
Render each scene with -s for a still; these compositions seed the real
scene library once Jake signs off on the look.

    manim render -s -qh dotprod_mock_stills.py M3_IntensityContest
"""

from __future__ import annotations

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    Cross,
    Line,
    Rectangle,
    RoundedRectangle,
    Scene,
    Text,
    VGroup,
)

from colors import BG, DATA_ERROR, DATA_FIT, DATA_HEAT, DATA_OBSERVED, DATA_PARAMS, TEXT
from style import FONT_BODY, FONT_HEADING, FONT_MONO, ensure_brand_fonts

ensure_brand_fonts()

DIM = 0.38  # opacity for de-emphasized elements


def quality_column(title: str, bass: float, tempo: float, accent: str, dim: bool = False) -> VGroup:
    """A song (or taste) as its two named entries, digits large and honest."""
    head = Text(title, font=FONT_HEADING, font_size=30, color=accent)
    rows = VGroup()
    for name, value in (("bass", bass), ("tempo", tempo)):
        label = Text(name, font=FONT_MONO, font_size=22, color=TEXT).set_opacity(0.75)
        digit = Text(f"{value:g}", font=FONT_MONO, font_size=34, color=accent)
        row = VGroup(label, digit).arrange(RIGHT, buff=0.32)
        rows.add(row)
    rows.arrange(DOWN, buff=0.28, aligned_edge=LEFT)
    card = VGroup(head, rows).arrange(DOWN, buff=0.4)
    frame = RoundedRectangle(
        corner_radius=0.18,
        width=card.width + 0.7,
        height=card.height + 0.6,
        stroke_color=accent,
        stroke_width=1.6,
        stroke_opacity=0.5,
        fill_opacity=0.0,
    ).move_to(card)
    group = VGroup(frame, card)
    if dim:
        group.set_opacity(DIM)
    return group


def sum_meter(total: float, tall: bool = False, crowned: bool = False) -> VGroup:
    bar = Rectangle(
        width=0.5,
        height=2.6 if tall else max(0.5, total / 9.0),
        fill_color=DATA_PARAMS,
        fill_opacity=0.95,
        stroke_width=0,
    )
    digits = Text(f"{total:g}", font=FONT_MONO, font_size=30, color=DATA_PARAMS)
    group = VGroup(bar, digits).arrange(DOWN, buff=0.22)
    if crowned:
        crown = Text("wins", font=FONT_MONO, font_size=22, color=DATA_ERROR)
        group = VGroup(crown, group).arrange(DOWN, buff=0.18)
    return group


def tombstone(label: str) -> VGroup:
    words = Text(label, font=FONT_MONO, font_size=20, color=TEXT).set_opacity(0.55)
    strike = Line(
        words.get_left() + 0.06 * LEFT,
        words.get_right() + 0.06 * RIGHT,
        stroke_color=DATA_ERROR,
        stroke_width=2.4,
    )
    return VGroup(words, strike)


class M3_IntensityContest(Scene):
    """Idea one fails: the cranked column wins; your taste sits dimmed, unconsulted."""

    def construct(self) -> None:
        self.camera.background_color = BG
        title = Text("idea one: just add them up", font=FONT_HEADING, font_size=34, color=TEXT)
        title.to_edge(UP, buff=0.6)

        taste = quality_column("your taste", 2, 1, DATA_HEAT, dim=True)
        night = quality_column("Night Drive", 1, 3, DATA_OBSERVED)
        glass = quality_column("Glass Rain", 2, 2, DATA_OBSERVED)
        static = quality_column("Static", 9, 8, DATA_OBSERVED)
        columns = VGroup(taste, night, glass, static).arrange(RIGHT, buff=0.85)
        columns.next_to(title, DOWN, buff=0.7)

        sums = VGroup(
            sum_meter(4),
            sum_meter(4),
            sum_meter(17, tall=True, crowned=True),
        )
        for meter, col in zip(sums, (night, glass, static)):
            meter.next_to(col, DOWN, buff=0.4)

        verdict = Text(
            "an intensity contest: whoever is cranked highest wins",
            font=FONT_BODY,
            font_size=26,
            color=DATA_ERROR,
        ).to_edge(DOWN, buff=0.5)

        unconsulted = Text("never consulted", font=FONT_MONO, font_size=18, color=TEXT)
        unconsulted.set_opacity(0.5).next_to(taste, DOWN, buff=0.4)

        self.add(title, columns, sums, verdict, unconsulted)


class M6_ZeroMatches(Scene):
    """Idea two fails: exact matching finds nothing, anywhere."""

    def construct(self) -> None:
        self.camera.background_color = BG
        title = Text("idea two: count exact agreements", font=FONT_HEADING, font_size=34, color=TEXT)
        title.to_edge(UP, buff=0.6)

        pairs = VGroup()
        for yours, theirs in ((2, 1), (1, 3)):
            a = Text(f"{yours}", font=FONT_MONO, font_size=40, color=DATA_HEAT)
            b = Text(f"{theirs}", font=FONT_MONO, font_size=40, color=DATA_OBSERVED)
            duo = VGroup(a, b).arrange(RIGHT, buff=0.5)
            mark = Cross(duo, stroke_color=DATA_ERROR, stroke_width=4).scale(0.72)
            pairs.add(VGroup(duo, mark))
        pairs.arrange(RIGHT, buff=1.6).next_to(title, DOWN, buff=1.0)

        counters = VGroup(
            *[
                Text("matches: 0", font=FONT_MONO, font_size=26, color=DATA_ERROR)
                for _ in range(3)
            ]
        ).arrange(RIGHT, buff=1.2)
        counters.next_to(pairs, DOWN, buff=0.9)

        verdict = Text(
            "near misses count for nothing",
            font=FONT_BODY,
            font_size=26,
            color=TEXT,
        ).set_opacity(0.85).to_edge(DOWN, buff=0.5)

        graveyard = tombstone("idea one").to_corner(UP + RIGHT, buff=0.5)

        self.add(title, pairs, counters, verdict, graveyard)


class M8_Multiply(Scene):
    """The repair: one pair multiplies, your interest times their amount."""

    def construct(self) -> None:
        self.camera.background_color = BG
        title = Text(
            "idea three: multiply each pair, then add",
            font=FONT_HEADING,
            font_size=34,
            color=TEXT,
        ).to_edge(UP, buff=0.6)

        bass_label = Text("bass", font=FONT_MONO, font_size=24, color=DATA_PARAMS)
        yours = Text("2", font=FONT_MONO, font_size=48, color=DATA_HEAT)
        times = Text("x", font=FONT_MONO, font_size=34, color=TEXT).set_opacity(0.6)
        theirs = Text("1", font=FONT_MONO, font_size=48, color=DATA_OBSERVED)
        equals = Text("=", font=FONT_MONO, font_size=34, color=TEXT).set_opacity(0.6)
        product = Text("2", font=FONT_MONO, font_size=48, color=DATA_PARAMS)
        line = VGroup(yours, times, theirs, equals, product).arrange(RIGHT, buff=0.4)
        bass_label.next_to(line, UP, buff=0.5)
        working = VGroup(bass_label, line).move_to(UP * 0.4)

        caption_a = Text("your interest", font=FONT_MONO, font_size=20, color=DATA_HEAT)
        caption_a.next_to(yours, DOWN, buff=0.45)
        caption_b = Text("their amount", font=FONT_MONO, font_size=20, color=DATA_OBSERVED)
        caption_b.next_to(theirs, DOWN, buff=0.45)

        queued = Text("tempo: 1 x 3 next", font=FONT_MONO, font_size=22, color=TEXT)
        queued.set_opacity(0.5).to_edge(DOWN, buff=0.8)

        self.add(title, working, caption_a, caption_b, queued)


class M9_Add(Scene):
    """The products pool into 5, landing in Section 1's empty scorebox."""

    def construct(self) -> None:
        self.camera.background_color = BG
        products = VGroup(
            Text("2", font=FONT_MONO, font_size=44, color=DATA_PARAMS),
            Text("+", font=FONT_MONO, font_size=34, color=TEXT).set_opacity(0.6),
            Text("3", font=FONT_MONO, font_size=44, color=DATA_PARAMS),
        ).arrange(RIGHT, buff=0.4)
        products.move_to(UP * 1.4)

        box = RoundedRectangle(
            corner_radius=0.2,
            width=2.2,
            height=1.4,
            stroke_color=DATA_FIT,
            stroke_width=2.4,
        )
        score = Text("5", font=FONT_MONO, font_size=64, color=DATA_FIT)
        scorebox = VGroup(box, score).move_to(DOWN * 0.6)

        label = Text("the question from the opening, answered", font=FONT_BODY, font_size=24, color=TEXT)
        label.set_opacity(0.75).next_to(scorebox, DOWN, buff=0.55)

        self.add(products, scorebox, label)


class M10_Chip(Scene):
    """The recipe compacts into the chip that anchors the notation later."""

    def construct(self) -> None:
        self.camera.background_color = BG
        chip_text = Text("2x1 + 1x3 = 5", font=FONT_MONO, font_size=30, color=DATA_PARAMS)
        chip_frame = RoundedRectangle(
            corner_radius=0.16,
            width=chip_text.width + 0.6,
            height=chip_text.height + 0.5,
            stroke_color=DATA_PARAMS,
            stroke_width=1.8,
            stroke_opacity=0.7,
        ).move_to(chip_text)
        chip = VGroup(chip_frame, chip_text).to_corner(UP + RIGHT, buff=0.6)

        line = Text(
            "the whole recipe, kept in the corner",
            font=FONT_BODY,
            font_size=28,
            color=TEXT,
        ).set_opacity(0.85)

        note = Text(
            "this chip is what a . b lands next to in the naming scene",
            font=FONT_MONO,
            font_size=20,
            color=DATA_FIT,
        ).set_opacity(0.8).next_to(line, DOWN, buff=0.6)

        self.add(chip, line, note)
