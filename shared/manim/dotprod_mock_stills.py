"""Hand-built mock stills for the Similarity Meter video, Section 2, take 2.

One persistent stage: the taste column and three song columns never leave.
Each scene is a snapshot of that stage as the attempts play out on it.

    manim render -s -qh dotprod_mock_stills.py A_Totals
"""

from __future__ import annotations

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    Line,
    RoundedRectangle,
    Scene,
    Text,
    VGroup,
)

from colors import BG, DATA_ERROR, DATA_FIT, DATA_HEAT, DATA_OBSERVED, DATA_PARAMS, TEXT
from style import FONT_BODY, FONT_HEADING, FONT_MONO, ensure_brand_fonts

ensure_brand_fonts()


def column(title: str, bass: float, tempo: float, accent: str) -> VGroup:
    head = Text(title, font=FONT_HEADING, font_size=26, color=accent)
    rows = VGroup()
    for name, value in (("bass", bass), ("tempo", tempo)):
        label = Text(name, font=FONT_MONO, font_size=19, color=TEXT).set_opacity(0.7)
        digit = Text(f"{value:g}", font=FONT_MONO, font_size=30, color=accent)
        rows.add(VGroup(label, digit).arrange(RIGHT, buff=0.28))
    rows.arrange(DOWN, buff=0.24, aligned_edge=LEFT)
    card = VGroup(head, rows).arrange(DOWN, buff=0.3)
    frame = RoundedRectangle(
        corner_radius=0.16,
        width=card.width + 0.6,
        height=card.height + 0.5,
        stroke_color=accent,
        stroke_width=1.4,
        stroke_opacity=0.45,
        fill_opacity=0.0,
    ).move_to(card)
    return VGroup(frame, card)


def stage() -> tuple[VGroup, VGroup, VGroup, VGroup, VGroup]:
    taste = column("your taste", 2, 1, DATA_HEAT)
    night = column("Night Drive", 1, 3, DATA_OBSERVED)
    glass = column("Glass Rain", 2, 2, DATA_OBSERVED)
    static = column("Static", 9, 8, DATA_OBSERVED)
    row = VGroup(taste, night, glass, static).arrange(RIGHT, buff=0.8)
    row.to_edge(UP, buff=1.15)
    return row, taste, night, glass, static


def total_tag(value: float, color: str, struck: bool = False) -> VGroup:
    tag = Text(f"total {value:g}", font=FONT_MONO, font_size=22, color=color)
    group = VGroup(tag)
    if struck:
        group.add(
            Line(tag.get_left(), tag.get_right(), stroke_color=DATA_ERROR, stroke_width=2)
        )
        group.set_opacity(0.45)
    return group


def caption(text: str, color: str = TEXT) -> Text:
    return Text(text, font=FONT_BODY, font_size=25, color=color).to_edge(DOWN, buff=0.5)


def header(text: str) -> Text:
    return Text(text, font=FONT_HEADING, font_size=30, color=TEXT).to_edge(UP, buff=0.35)


class A_Totals(Scene):
    """Attempt A: compare totals. Night Drive and Glass Rain tie at closest."""

    def construct(self) -> None:
        self.camera.background_color = BG
        row, taste, night, glass, static = stage()
        title = header("attempt one: compare the totals")
        row.shift(DOWN * 0.35)

        tags = VGroup(
            total_tag(3, DATA_HEAT),
            total_tag(4, DATA_PARAMS),
            total_tag(4, DATA_PARAMS),
            total_tag(17, DATA_PARAMS),
        )
        for tag, col in zip(tags, (taste, night, glass, static)):
            tag.next_to(col, DOWN, buff=0.3)

        tie = Text("both 1 away. tied?", font=FONT_MONO, font_size=20, color=DATA_FIT)
        tie.next_to(VGroup(tags[1], tags[2]), DOWN, buff=0.35)

        ghost = Text(
            "but (3,1) and (1,3) also both total 4, and they are opposites",
            font=FONT_MONO,
            font_size=20,
            color=DATA_ERROR,
        ).next_to(tie, DOWN, buff=0.4)

        self.add(title, row, tags, tie, ghost, caption("totals lose the mix"))


class B_Differences(Scene):
    """Attempt B: differences entry by entry. Keeps the mix; ignores caring."""

    def construct(self) -> None:
        self.camera.background_color = BG
        row, taste, night, glass, static = stage()
        title = header("attempt two: measure the differences")
        row.shift(DOWN * 0.35)

        struck = VGroup(total_tag(3, DATA_HEAT, True), total_tag(4, DATA_PARAMS, True))
        struck[0].next_to(taste, DOWN, buff=0.3)
        struck[1].next_to(night, DOWN, buff=0.3)

        diff = VGroup(
            Text("bass: 2 vs 1, apart 1", font=FONT_MONO, font_size=22, color=DATA_PARAMS),
            Text("tempo: 1 vs 3, apart 2", font=FONT_MONO, font_size=22, color=DATA_PARAMS),
            Text("distance 3", font=FONT_MONO, font_size=26, color=DATA_PARAMS),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        diff.next_to(struck[1], DOWN, buff=0.45)

        bridge = Line(
            taste.get_right() + 0.08 * RIGHT,
            night.get_left() + 0.08 * LEFT,
            stroke_color=DATA_PARAMS,
            stroke_width=2,
        ).set_opacity(0.6)

        self.add(
            title,
            row,
            struck,
            bridge,
            diff,
            caption("closer, but a quality you care nothing about still gets punished"),
        )


class C_Votes(Scene):
    """The repair: your numbers are votes on how much each quality counts."""

    def construct(self) -> None:
        self.camera.background_color = BG
        row, taste, night, glass, static = stage()
        title = header("the repair: your numbers are votes")
        row.shift(DOWN * 0.35)

        votes = VGroup(
            VGroup(
                Text("bass", font=FONT_MONO, font_size=20, color=TEXT).set_opacity(0.7),
                Text("2", font=FONT_MONO, font_size=32, color=DATA_HEAT),
                Text("x", font=FONT_MONO, font_size=24, color=TEXT).set_opacity(0.6),
                Text("1", font=FONT_MONO, font_size=32, color=DATA_OBSERVED),
                Text("=", font=FONT_MONO, font_size=24, color=TEXT).set_opacity(0.6),
                Text("2", font=FONT_MONO, font_size=32, color=DATA_PARAMS),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("tempo", font=FONT_MONO, font_size=20, color=TEXT).set_opacity(0.7),
                Text("1", font=FONT_MONO, font_size=32, color=DATA_HEAT),
                Text("x", font=FONT_MONO, font_size=24, color=TEXT).set_opacity(0.6),
                Text("3", font=FONT_MONO, font_size=32, color=DATA_OBSERVED),
                Text("=", font=FONT_MONO, font_size=24, color=TEXT).set_opacity(0.6),
                Text("3", font=FONT_MONO, font_size=32, color=DATA_PARAMS),
            ).arrange(RIGHT, buff=0.3),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        votes.next_to(VGroup(taste, night), DOWN, buff=0.6)

        legend = Text(
            "your vote x their amount. a 0 vote makes a quality count for nothing",
            font=FONT_MONO,
            font_size=19,
            color=TEXT,
        ).set_opacity(0.75).next_to(votes, DOWN, buff=0.45)

        self.add(title, row, votes, legend, caption("weight the agreement by how much you care"))


class D_Score(Scene):
    """The votes add into 5 under Night Drive; lineage stays visible."""

    def construct(self) -> None:
        self.camera.background_color = BG
        row, taste, night, glass, static = stage()
        title = header("add the votes: one score")
        row.shift(DOWN * 0.35)

        lineage = VGroup(
            Text("bass vote 2", font=FONT_MONO, font_size=22, color=DATA_PARAMS),
            Text("+", font=FONT_MONO, font_size=24, color=TEXT).set_opacity(0.6),
            Text("tempo vote 3", font=FONT_MONO, font_size=22, color=DATA_PARAMS),
        ).arrange(RIGHT, buff=0.35)
        lineage.next_to(VGroup(taste, night), DOWN, buff=0.55)

        box = RoundedRectangle(
            corner_radius=0.16,
            width=2.4,
            height=1.1,
            stroke_color=DATA_FIT,
            stroke_width=2.2,
        )
        score = Text("match: 5", font=FONT_MONO, font_size=32, color=DATA_FIT)
        scorebox = VGroup(box, score.move_to(box)).next_to(lineage, DOWN, buff=0.5)

        self.add(
            title,
            row,
            lineage,
            scorebox,
            caption("the scorebox from the opening finally gets its number"),
        )


class E_Chip(Scene):
    """The recipe compacts to the corner chip the notation will land beside."""

    def construct(self) -> None:
        self.camera.background_color = BG
        row, taste, night, glass, static = stage()
        title = header("the whole recipe, kept")
        row.shift(DOWN * 0.35)
        row.set_opacity(0.5)

        chip_text = Text("2x1 + 1x3 = 5", font=FONT_MONO, font_size=26, color=DATA_PARAMS)
        chip_frame = RoundedRectangle(
            corner_radius=0.14,
            width=chip_text.width + 0.5,
            height=chip_text.height + 0.4,
            stroke_color=DATA_PARAMS,
            stroke_width=1.6,
            stroke_opacity=0.7,
        ).move_to(chip_text)
        chip = VGroup(chip_frame, chip_text).to_corner(UP + RIGHT, buff=0.45)

        line = Text(
            "big when you agree where it matters",
            font=FONT_BODY,
            font_size=30,
            color=DATA_FIT,
        ).move_to(DOWN * 1.2)

        self.add(title, row, chip, line)
