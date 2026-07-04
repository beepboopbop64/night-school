"""Night School shared Manim style: brand fonts + the True-Up motif.

Fonts
-----
The brand TTFs are installed per-user in ``%LOCALAPPDATA%\\Microsoft\\Windows\\Fonts``.
ManimPango's fontconfig backend does not read the Windows per-user font
registry, so :func:`ensure_brand_fonts` registers the files directly with
Pango. It runs once at import.

The Pango family names carry the variable fonts' optical-size axis — use the
``FONT_*`` constants below, never the bare family strings.

The True-Up (BRAND.md)
----------------------
Every key idea enters as a freehand sketch and, at the moment of
formalization, trues into an exact glowing line. In Manim terms: noise
displacement on VMobject points animated to zero atop ``smooth``, with the
Trued Mint glow blooming at settle.

    underline = make_underline(width=5.0)
    roughen(underline)                     # born a sketch
    scene.play(Create(underline))
    scene.play(wobble_once(underline))     # one shiver of intuition
    scene.play(true_up(underline))         # 800ms settle + mint bloom

Hard rule: never on text. Sketchiness lives in lines, never letters.
"""

from __future__ import annotations

import os
from typing import Sequence

import manimpango
import numpy as np
from manim import (
    Animation,
    AnimationGroup,
    ManimColor,
    Succession,
    VGroup,
    VMobject,
    Wait,
    interpolate_color,
    smooth,
)

from colors import BRAND_MINT

# ---------------------------------------------------------------------------
# Fonts
# ---------------------------------------------------------------------------

_FONT_DIR = os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\Windows\Fonts")
_FONT_FILES: tuple[str, ...] = (
    "BricolageGrotesque-VF.ttf",
    "Literata-VF.ttf",
    "Literata-Italic-VF.ttf",
    "IBMPlexMono-Regular.ttf",
    "IBMPlexMono-Italic.ttf",
)

# Pango family names as exposed by the installed files (the "14pt"/"12pt"
# suffixes are the variable fonts' default optical-size instances).
FONT_HEADING = "Bricolage Grotesque 14pt"
FONT_BODY = "Literata 12pt"
FONT_MONO = "IBM Plex Mono"


def ensure_brand_fonts() -> list[str]:
    """Register the brand TTFs with Pango. Returns the list of missing files."""
    missing: list[str] = []
    for name in _FONT_FILES:
        path = os.path.join(_FONT_DIR, name)
        if os.path.isfile(path):
            manimpango.register_font(path)
        else:
            missing.append(path)
    return missing


_MISSING_FONTS = ensure_brand_fonts()
if _MISSING_FONTS:  # pragma: no cover - depends on machine state
    import warnings

    warnings.warn(
        "Night School brand fonts not installed: " + ", ".join(_MISSING_FONTS),
        stacklevel=2,
    )


# ---------------------------------------------------------------------------
# The True-Up motif
# ---------------------------------------------------------------------------

# Default displacement amplitude in scene units. The frame is 8 units tall at
# 1080px, so 0.015 units is roughly 2px — the brand's hand-jitter ceiling.
TRUE_UP_AMPLITUDE = 0.015
TRUE_UP_WAVELENGTH = 0.9
TRUE_UP_RUN_TIME = 0.8

_CLEAN_ATTR = "_true_up_clean_points"


def _hand_jitter(
    points: np.ndarray, amplitude: float, wavelength: float, seed: int
) -> np.ndarray:
    """Low-frequency 2D displacement along a point run, endpoints pinned.

    Two incommensurate sine waves per axis plus a pinch of per-point grain:
    wobble that reads as a hand, not as noise.
    """
    n = len(points)
    if n < 2:
        return np.zeros_like(points)
    rng = np.random.default_rng(seed)
    seg = np.linalg.norm(np.diff(points[:, :2], axis=0), axis=1)
    s = np.concatenate([[0.0], np.cumsum(seg)])
    total = float(s[-1]) if s[-1] > 0 else 1.0
    phase = rng.uniform(0.0, 2.0 * np.pi, size=4)
    tau = 2.0 * np.pi
    wob_x = (
        np.sin(tau * s / wavelength + phase[0]) * 0.62
        + np.sin(tau * s / (wavelength * 2.7) + phase[1]) * 0.38
    )
    wob_y = (
        np.sin(tau * s / (wavelength * 1.4) + phase[2]) * 0.62
        + np.sin(tau * s / (wavelength * 3.3) + phase[3]) * 0.38
    )
    grain = rng.uniform(-1.0, 1.0, size=(n, 2)) * 0.18
    pin = np.minimum(1.0, 6.0 * np.minimum(s, total - s) / total)
    disp = np.zeros_like(points)
    disp[:, 0] = amplitude * (wob_x + grain[:, 0]) * pin
    disp[:, 1] = amplitude * (wob_y + grain[:, 1]) * pin
    return disp


def _family(mobject: VMobject) -> list[VMobject]:
    return [m for m in mobject.get_family() if m.has_points()]


def roughen(
    mobject: VMobject,
    amplitude: float = TRUE_UP_AMPLITUDE,
    wavelength: float = TRUE_UP_WAVELENGTH,
    seed: int = 7,
) -> VMobject:
    """Displace a clean VMobject into its freehand-sketch form.

    Stores the clean points on the mobject so :func:`true_up` knows the exact
    line to settle into. Idempotent per mobject (re-roughening re-jitters from
    the stored clean geometry).
    """
    for i, mob in enumerate(_family(mobject)):
        clean = getattr(mob, _CLEAN_ATTR, None)
        if clean is None:
            clean = mob.points.copy()
            setattr(mob, _CLEAN_ATTR, clean)
        disp = _hand_jitter(clean, amplitude, wavelength, seed + i)
        mob.set_points(clean + disp)
    return mobject


class _Settle(Animation):
    """Displacement -> 0 atop `smooth`: the final frames are exact."""

    def __init__(
        self, mobject: VMobject, settle_color: str | None = None, **kwargs: object
    ) -> None:
        super().__init__(mobject, rate_func=smooth, **kwargs)
        self._settle_color = settle_color

    def begin(self) -> None:
        self._entries: list[tuple[VMobject, np.ndarray, np.ndarray, object]] = []
        for mob in _family(self.mobject):
            clean = getattr(mob, _CLEAN_ATTR, None)
            if clean is None:
                clean = mob.points.copy()
            disp = mob.points - clean
            self._entries.append((mob, clean, disp, mob.get_stroke_color()))
        super().begin()

    def interpolate_mobject(self, alpha: float) -> None:
        a = self.rate_func(alpha)
        k = 1.0 - a
        for mob, clean, disp, start_color in self._entries:
            mob.set_points(clean + disp * k)
            if self._settle_color is not None:
                mob.set_stroke(
                    color=interpolate_color(start_color, ManimColor(self._settle_color), a)
                )

    def finish(self) -> None:
        super().finish()
        for mob, clean, _, _ in self._entries:
            mob.set_points(clean.copy())
            if self._settle_color is not None:
                mob.set_stroke(color=self._settle_color)


class _Bloom(Animation):
    """Glow opacity: sharp rise, then settle to a steady after-light."""

    def __init__(
        self, glow: VGroup, peaks: Sequence[float], settle: float = 0.55, **kwargs: object
    ) -> None:
        super().__init__(glow, **kwargs)
        self._peaks = list(peaks)
        self._settle = settle

    def interpolate_mobject(self, alpha: float) -> None:
        if alpha < 0.35:
            level = smooth(alpha / 0.35)
        else:
            level = 1.0 - (1.0 - self._settle) * smooth((alpha - 0.35) / 0.65)
        for layer, peak in zip(self.mobject.submobjects, self._peaks):
            layer.set_stroke(opacity=peak * level)


def glow_of(
    mobject: VMobject,
    color: str = BRAND_MINT,
    layers: int = 4,
    width_ratio: float = 3.2,
) -> VGroup:
    """Layered wide-stroke copies of the CLEAN geometry — Manim's blur."""
    base = mobject.copy()
    for mob in _family(base):
        clean = getattr(mob, _CLEAN_ATTR, None)
        if clean is not None:
            mob.set_points(clean.copy())
    width = max(m.get_stroke_width() for m in _family(base))
    glow = VGroup()
    for i in range(layers):
        layer = base.copy()
        layer.set_stroke(
            color=color,
            width=width * (1.0 + width_ratio * (i + 1) / layers),
            opacity=0.0,
        )
        layer.set_fill(opacity=0.0)
        glow.add(layer)
    return glow


def _glow_peaks(layers: int, max_opacity: float) -> list[float]:
    return [max_opacity * (1.0 - i / (layers + 1)) ** 2 for i in range(layers)]


def wobble_once(
    mobject: VMobject,
    amplitude: float = TRUE_UP_AMPLITUDE,
    wavelength: float = TRUE_UP_WAVELENGTH,
    seed: int = 21,
    run_time: float = 0.35,
) -> Animation:
    """One organic shiver: the sketch breathes before it trues."""

    class _Wobble(Animation):
        def begin(self_inner) -> None:
            self_inner._entries = []
            for i, mob in enumerate(_family(self_inner.mobject)):
                clean = getattr(mob, _CLEAN_ATTR, None)
                if clean is None:
                    clean = mob.points.copy()
                    setattr(mob, _CLEAN_ATTR, clean)
                start_disp = mob.points - clean
                alt_disp = _hand_jitter(clean, amplitude, wavelength, seed + i)
                self_inner._entries.append((mob, clean, start_disp, alt_disp))
            super(_Wobble, self_inner).begin()

        def interpolate_mobject(self_inner, alpha: float) -> None:
            w = float(np.sin(np.pi * alpha))
            for mob, clean, start_disp, alt_disp in self_inner._entries:
                mob.set_points(clean + start_disp + (alt_disp - start_disp) * w)

    return _Wobble(mobject, run_time=run_time)


def true_up(
    mobject: VMobject,
    run_time: float = TRUE_UP_RUN_TIME,
    settle_color: str | None = None,
    glow_color: str = BRAND_MINT,
    glow_max_opacity: float = 0.5,
    bloom_time: float = 0.55,
) -> Animation:
    """THE signature motif: displacement animates to zero atop `smooth`, and
    the Trued Mint glow blooms at the exact moment displacement hits zero.

    Play the returned animation on a :func:`roughen`'d mobject:
    ``scene.play(true_up(underline))`` (total = run_time + bloom_time).
    ``settle_color`` also trues the stroke color (periwinkle sketch -> mint).
    """
    glow = glow_of(mobject, color=glow_color)
    peaks = _glow_peaks(len(glow.submobjects), glow_max_opacity)
    return AnimationGroup(
        _Settle(mobject, settle_color=settle_color, run_time=run_time),
        Succession(
            Wait(run_time),
            _Bloom(glow, peaks, run_time=bloom_time),
        ),
    )
