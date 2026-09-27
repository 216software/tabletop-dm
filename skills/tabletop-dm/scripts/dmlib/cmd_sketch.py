"""sketch: a very rough top-down picture of a room, drawn only from flat rectangles.

This never aims for a real drawing, and it never renders text (so a sketch
can never carry a hidden message the way a caption or a label could). It
exists so that when the player asks to see the room, the DM has something
quick to show: rooms, corridors and doors as plain boxes, nothing more.
"""
import argparse
import json
import random
from pathlib import Path
from typing import Any, Dict, List

from . import io_campaign, party_ops
from .errors import DmError
from .pngwriter import Canvas

MAX_CELLS = 40           # a side of the grid, in cells: keeps a sketch a sketch
MAX_SHAPES = 60
CELL_PIXELS = 24
MARGIN_CELLS = 1

ROOM_LINE = (40, 40, 40)
CORRIDOR_LINE = (120, 120, 120)
DOOR_COLOR = (150, 90, 40)
LINE_THICKNESS = 3

_SHAPE_TYPES = ("room", "corridor", "door")


def _load_shapes(text: str) -> List[Dict[str, Any]]:
    try:
        shapes = json.loads(text)
    except json.JSONDecodeError as exc:
        raise DmError("bad_arguments", "--shapes is not valid JSON: %s" % exc)
    if not isinstance(shapes, list) or not shapes:
        raise DmError("bad_arguments", "--shapes must be a non-empty JSON list of rooms, corridors and doors.")
    if len(shapes) > MAX_SHAPES:
        raise DmError("bad_arguments", "a sketch is capped at %d shapes. Simplify it." % MAX_SHAPES)
    for shape in shapes:
        if not isinstance(shape, dict) or shape.get("type") not in _SHAPE_TYPES:
            raise DmError("bad_arguments", "each shape needs a \"type\" of room, corridor or door.")
        for field in ("x", "y"):
            value = shape.get(field)
            if not isinstance(value, (int, float)) or isinstance(value, bool) or value < 0:
                raise DmError("bad_arguments", "a %s needs a non-negative numeric %s." % (shape["type"], field))
        if shape["type"] != "door":
            for field in ("w", "h"):
                value = shape.get(field)
                if not isinstance(value, (int, float)) or isinstance(value, bool) or value <= 0:
                    raise DmError("bad_arguments", "a %s needs a positive numeric %s." % (shape["type"], field))
    return shapes


def _extent(shapes: List[Dict[str, Any]]) -> Any:
    max_x = max(shape["x"] + shape.get("w", 1) for shape in shapes)
    max_y = max(shape["y"] + shape.get("h", 1) for shape in shapes)
    if max_x > MAX_CELLS or max_y > MAX_CELLS:
        raise DmError("bad_arguments", "the sketch is capped at %d cells on a side. Simplify it." % MAX_CELLS)
    return max_x, max_y


def _px(cells: float) -> int:
    return int(round((cells + MARGIN_CELLS) * CELL_PIXELS))


def sketch(args: argparse.Namespace, skill_root: Path, rng: random.Random) -> Dict[str, Any]:
    campaign_dir = Path(args.campaign)
    shapes = _load_shapes(args.shapes)
    max_x, max_y = _extent(shapes)
    width, height = _px(max_x + MARGIN_CELLS), _px(max_y + MARGIN_CELLS)
    canvas = Canvas(width, height)
    for shape in shapes:
        x0, y0 = _px(shape["x"]), _px(shape["y"])
        if shape["type"] == "door":
            half = CELL_PIXELS // 3
            canvas.fill_rect(x0 - half, y0 - half, x0 + half, y0 + half, DOOR_COLOR)
            continue
        x1, y1 = _px(shape["x"] + shape["w"]), _px(shape["y"] + shape["h"])
        line = ROOM_LINE if shape["type"] == "room" else CORRIDOR_LINE
        canvas.outline_rect(x0, y0, x1, y1, line, LINE_THICKNESS)

    name = party_ops.slugify(args.name) if args.name else "sketch"
    if not name:
        raise DmError("bad_arguments", "--name left nothing usable after cleaning. Try a plainer name.")
    art_dir = campaign_dir / "art"
    if art_dir.is_symlink():
        raise DmError("campaign_file_is_symlink", "art is a symbolic link. dm.py will not write through it.")
    art_dir.mkdir(exist_ok=True)
    path = art_dir / (name + ".png")
    io_campaign.atomic_write_bytes(path, canvas.to_png_bytes())
    return {"path": str(path), "name": name, "width": width, "height": height, "shapes": len(shapes)}
