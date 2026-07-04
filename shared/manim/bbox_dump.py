"""Per-keyframe bounding-box dump for Night School Manim scenes.

Purpose (ARCHITECTURE.md section 6.1): after a scene renders, a JSON file
lands alongside the movie with per-keyframe bounding boxes of every mobject
on screen. The mechanical pre-checks (harness/checks/bbox.ts) consume it and
reject gross geometry — collisions, out-of-frame elements, unreadable text,
novelty floods — before a single vision token is spent on Iris.

Mechanism: instance-level wrap (chosen over a Scene subclass)
-------------------------------------------------------------
A scene opts in with one line at the top of ``construct()``::

    from bbox_dump import attach_bbox_dump

    class Scene01(Scene):
        def construct(self):
            attach_bbox_dump(self)
            ...

``attach_bbox_dump`` reassigns ``play`` and ``tear_down`` on the *instance*
(instance attributes shadow class methods; the originals are captured as
bound methods, so nothing recurses and no Manim class is globally patched).
Chosen because it is the least invasive option that works on Manim CE
0.20.1: it composes with ANY Scene subclass (Scene, MovingCameraScene,
ThreeDScene) without multiple-inheritance games, and generated scene code
only adds an import plus one call. ``Scene.wait()`` routes through
``play(Wait(...))`` internally, so wrapping ``play`` alone captures waits as
keyframes too.

The dump
--------
A keyframe is the scene state right after each ``play()``/``wait()``
returns — the settled end state of every animation. Written at
``tear_down`` next to the movie file (``<movie stem>.bboxes.json``; falls
back to the image path under ``-s``, then to ``config.media_dir``).

Schema (schemaVersion 1)::

    {
      "schemaVersion": 1,
      "scene": "Scene01",
      "frame": {"width": 14.22, "height": 8.0,
                "pixelWidth": 854, "pixelHeight": 480},
      "keyframes": [
        {"index": 0, "timeSeconds": 2.0, "label": "Write",
         "mobjects": [
           {"id": "m0", "type": "Text", "text": "beat-01: ...",
            "x": 0.0, "y": 3.42, "w": 5.1, "h": 0.38, "opacity": 1.0}
         ]}
      ]
    }

Coordinates are Manim scene units (frame is ``frame.width`` x
``frame.height``, origin at center, +y up); ``x``/``y`` are the bbox
CENTER, ``w``/``h`` the axis-aligned extents. ``id`` is stable across
keyframes for the lifetime of the mobject (the checks use it to count NEW
mobjects per keyframe). Pure containers (exact-type VGroup/Group) are
descended into; everything else — Text, MathTex, Axes, Circle — is recorded
as one atomic box, so a Text is one box, not fifty glyph boxes.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from manim import Group, VGroup, config

_STATE_ATTR = "_bbox_dump_state"

# Exact types descended into; subclasses (Axes is a VGroup subclass) stay atomic.
_CONTAINER_TYPES = (VGroup, Group)


def _has_points(mob: Any) -> bool:
    return any(len(member.points) > 0 for member in mob.get_family())


def _text_of(mob: Any) -> str | None:
    """Text content when the mobject carries any (Text.text, *Tex.tex_string)."""
    for attr in ("text", "tex_string"):
        value = getattr(mob, attr, None)
        if isinstance(value, str) and value:
            return value
    return None


def _opacity_of(mob: Any) -> float:
    """Max fill/stroke opacity across the family; 1.0 when nothing reports one."""
    best = 0.0
    found = False
    for member in mob.get_family():
        for getter_name in ("get_fill_opacity", "get_stroke_opacity"):
            getter = getattr(member, getter_name, None)
            if not callable(getter):
                continue
            try:
                value = float(getter())
            except (TypeError, ValueError):
                continue
            found = True
            best = max(best, value)
    return best if found else 1.0


def _collect(mob: Any, records: list[dict[str, Any]], state: dict[str, Any]) -> None:
    if type(mob) in _CONTAINER_TYPES:
        for sub in mob.submobjects:
            _collect(sub, records, state)
        return
    if not _has_points(mob):
        return
    registry: dict[int, str] = state["registry"]
    key = id(mob)
    if key not in registry:
        registry[key] = f"m{len(registry)}"
        state["refs"].append(mob)  # pin: keeps id() from being recycled mid-render
    center = mob.get_center()
    records.append(
        {
            "id": registry[key],
            "type": type(mob).__name__,
            "text": _text_of(mob),
            "x": round(float(center[0]), 4),
            "y": round(float(center[1]), 4),
            "w": round(float(mob.width), 4),
            "h": round(float(mob.height), 4),
            "opacity": round(_opacity_of(mob), 4),
        }
    )


def _snapshot(scene: Any, state: dict[str, Any], label: str) -> None:
    records: list[dict[str, Any]] = []
    for mob in scene.mobjects:
        _collect(mob, records, state)
    time_seconds = float(getattr(getattr(scene, "renderer", None), "time", 0.0) or 0.0)
    state["keyframes"].append(
        {
            "index": len(state["keyframes"]),
            "timeSeconds": round(time_seconds, 3),
            "label": label,
            "mobjects": records,
        }
    )


def _out_path(scene: Any) -> Path:
    """Next to the movie file; image path under -s; media_dir as last resort."""
    file_writer = getattr(getattr(scene, "renderer", None), "file_writer", None)
    for attr in ("movie_file_path", "image_file_path"):
        target = getattr(file_writer, attr, None)
        if target:
            target = Path(target)
            return target.with_name(target.stem + ".bboxes.json")
    return Path(config.media_dir) / f"{type(scene).__name__}.bboxes.json"


def _write_dump(scene: Any, state: dict[str, Any]) -> Path:
    dump = {
        "schemaVersion": 1,
        "scene": type(scene).__name__,
        "frame": {
            "width": round(float(config.frame_width), 4),
            "height": round(float(config.frame_height), 4),
            "pixelWidth": int(config.pixel_width),
            "pixelHeight": int(config.pixel_height),
        },
        "keyframes": state["keyframes"],
    }
    out = state["out_path"] if state["out_path"] is not None else _out_path(scene)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(dump, indent=1), encoding="utf-8")
    return out


def attach_bbox_dump(scene: Any, out_path: str | Path | None = None) -> Any:
    """Wrap the scene instance so every play()/wait() records a keyframe and
    tear_down() writes the JSON dump. Idempotent. Returns the scene."""
    if getattr(scene, _STATE_ATTR, None) is not None:
        return scene
    state: dict[str, Any] = {
        "keyframes": [],
        "registry": {},
        "refs": [],
        "out_path": Path(out_path) if out_path is not None else None,
    }
    setattr(scene, _STATE_ATTR, state)

    original_play = scene.play
    original_tear_down = scene.tear_down

    def play(*args: Any, **kwargs: Any) -> None:
        original_play(*args, **kwargs)
        label = ", ".join(type(arg).__name__ for arg in args) or "play"
        _snapshot(scene, state, label)

    def tear_down() -> None:
        original_tear_down()
        _write_dump(scene, state)

    scene.play = play
    scene.tear_down = tear_down
    return scene
