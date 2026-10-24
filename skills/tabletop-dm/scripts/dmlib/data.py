"""Loads the rules data that ships in the skill folder. Read-only."""
import difflib
import json
import re
from pathlib import Path
from typing import Any, Dict, List, Tuple

from .errors import DmError

KINDS = ("classes", "spells", "monsters", "equipment")
# One folder per world: worlds/<id>/ with world.json, bible.md, metaplot.md and seeds/.
WORLDS_DIR = "worlds"
WORLD_MANIFEST = "world.json"
_WORLD_ID = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
# lookup takes the singular word.
SINGULAR = {"class": "classes", "spell": "spells", "monster": "monsters", "equipment": "equipment"}


def load_all(skill_root: Path) -> Dict[str, Dict[str, Any]]:
    """Return {"classes": {...}, "spells": {...}, ...} or refuse with every problem found."""
    problems = []  # type: List[str]
    out = {}  # type: Dict[str, Dict[str, Any]]
    for kind in KINDS:
        path = skill_root / "data" / (kind + ".json")
        if not path.is_file():
            problems.append("data/%s.json is missing" % kind)
            continue
        try:
            doc = json.loads(path.read_text())
        except ValueError as exc:
            problems.append("data/%s.json is not valid JSON (%s)" % (kind, exc))
            continue
        if not isinstance(doc, dict) or doc.get("format") != "tabletop-dm/" + kind:
            problems.append("data/%s.json has no 'tabletop-dm/%s' format marker" % (kind, kind))
            continue
        records = doc.get(kind)
        if not isinstance(records, dict) or not records:
            problems.append("data/%s.json has no '%s' records" % (kind, kind))
            continue
        for key, record in records.items():
            if not isinstance(record, dict) or record.get("id") != key:
                problems.append("data/%s.json: entry '%s' must be an object whose id is '%s'" % (kind, key, key))
        out[kind] = records
    if problems:
        raise DmError("data_invalid", "the skill's data files have problems: " + "; ".join(problems))
    return out


def get_record(records: Dict[str, Any], kind_word: str, name: str) -> Dict[str, Any]:
    """One record by id, or a refusal that lists near matches."""
    key = name.strip().lower().replace(" ", "-")
    if key in records:
        return records[key]
    near = difflib.get_close_matches(key, list(records), n=3, cutoff=0.5)
    hint = " Did you mean: %s?" % ", ".join(near) if near else ""
    raise DmError("unknown_name", "no %s '%s'.%s" % (kind_word, name, hint))


def check_party_refs(party: Dict[str, Any], records: Dict[str, Dict[str, Any]]) -> None:
    """Every class and every equipped item on a sheet must exist in the rules data."""
    for cid, character in party["characters"].items():
        if character["class"] not in records["classes"]:
            raise DmError("campaign_file_damaged", "party.json: characters.%s.class is '%s', which is not a class in "
                                                   "this skill's data (%s)."
                          % (cid, character["class"], ", ".join(sorted(records["classes"]))))
        equipped = character["equipped"]
        for item in [equipped.get("armor"), equipped.get("shield")] + list(equipped["weapons"]):
            if item is not None and item not in records["equipment"]:
                raise DmError("campaign_file_damaged", "party.json: characters.%s has '%s' equipped, which is not in "
                                                       "this skill's equipment data. Unequip it by hand, or restore "
                                                       "the file." % (cid, item))


def list_seed_names(world_dir: Path) -> List[str]:
    folder = world_dir / "seeds"
    if not folder.is_dir():
        return []
    return sorted(p.stem for p in folder.glob("*.md") if p.stem != "teasers")


def _read_manifest(folder: Path) -> Dict[str, Any]:
    """A world's world.json, checked. Raises ValueError with the reason."""
    try:
        manifest = json.loads((folder / WORLD_MANIFEST).read_text())
    except (OSError, UnicodeDecodeError, ValueError) as exc:
        raise ValueError("world.json is not valid JSON (%s)" % exc)
    if not isinstance(manifest, dict):
        raise ValueError("world.json must be an object")
    for key in ("name", "pitch"):
        if not isinstance(manifest.get(key), str) or not manifest[key].strip():
            raise ValueError("world.json needs a '%s' of text" % key)
    return manifest


def list_worlds(skill_root: Path) -> Tuple[List[Dict[str, Any]], List[str]]:
    """Every world in worlds/, in id order, and a note for each one that is broken.

    A world is a folder with a world.json. A folder without one is a draft and is ignored.
    """
    folder = skill_root / WORLDS_DIR
    worlds = []  # type: List[Dict[str, Any]]
    problems = []  # type: List[str]
    if not folder.is_dir():
        return worlds, problems
    for path in sorted(folder.iterdir()):
        if not path.is_dir() or not (path / WORLD_MANIFEST).is_file():
            continue
        try:
            if not _WORLD_ID.match(path.name):
                raise ValueError("the folder name must be a lowercase slug")
            manifest = _read_manifest(path)
            seeds = list_seed_names(path)
            if not seeds:
                raise ValueError("it has no seeds/ files")
        except ValueError as exc:
            problems.append("%s: %s" % (path.name, exc))
            continue
        worlds.append({"id": path.name, "name": manifest["name"].strip(), "pitch": manifest["pitch"].strip(),
                       "dir": path, "seeds": seeds})
    return worlds, problems
