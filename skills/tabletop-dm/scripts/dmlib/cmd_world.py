"""world list / choose. The world is recorded once per campaign, before the seed."""
import argparse
import random
from pathlib import Path
from typing import Any, Dict, List

from . import data, io_campaign, party_ops
from .errors import DmError


def installed(skill_root: Path) -> List[Dict[str, Any]]:
    worlds, _ = data.list_worlds(skill_root)
    if not worlds:
        raise DmError("no_worlds_found", "the skill has no worlds/<name>/world.json. The install is incomplete.")
    return worlds


def safe_files(world: Dict[str, Any]) -> Dict[str, str]:
    """The files of a world the player may read."""
    return {"bible_file": (world["dir"] / "bible.md").as_posix(),
            "teasers_file": (world["dir"] / "seeds" / "teasers.md").as_posix()}


def resolve(party: Dict[str, Any], skill_root: Path, entries: List[Dict[str, Any]], command: str) -> Dict[str, Any]:
    """The campaign's world. With no world chosen and one installed, that one is recorded (an entry in `entries`)."""
    worlds = installed(skill_root)
    chosen = party["settings"].get("world")
    if chosen is None:
        if len(worlds) > 1:
            raise DmError("world_not_chosen", "this install has %d worlds. Show the player `world list` and run "
                                              "`world choose` first." % len(worlds))
        chosen = worlds[0]["id"]
        party["settings"]["world"] = chosen
        entries.append(io_campaign.change_entry(command, None, "settings.world", None, chosen))
    for world in worlds:
        if world["id"] == chosen:
            return world
    raise DmError("world_unknown", "this campaign is set in '%s', which this install does not have. Worlds: %s."
                  % (chosen, ", ".join(w["id"] for w in worlds)))


def world_list(args: argparse.Namespace, skill_root: Path, rng: random.Random) -> Dict[str, Any]:
    party = io_campaign.load_party(Path(args.campaign))
    worlds = installed(skill_root)
    return {"worlds": [{"id": w["id"], "name": w["name"], "pitch": w["pitch"], "seeds": len(w["seeds"])}
                       for w in worlds],
            "chosen": party["settings"].get("world")}


def world_choose(args: argparse.Namespace, skill_root: Path, rng: random.Random) -> Dict[str, Any]:
    campaign_dir = Path(args.campaign)
    party = io_campaign.load_party(campaign_dir)
    if party["settings"].get("world"):
        raise DmError("world_already_set", "this campaign is already set in %s." % party["settings"]["world"])
    worlds = installed(skill_root)
    ids = [w["id"] for w in worlds]
    name = party_ops.slugify(args.name)
    if name.isdigit() and 1 <= int(name) <= len(ids):
        name = ids[int(name) - 1]             # the player said "the second one"
    if name not in ids:
        raise DmError("world_unknown", "no world '%s'. Worlds: %s." % (args.name, ", ".join(ids)))
    world = worlds[ids.index(name)]
    party["settings"]["world"] = name
    party_ops.commit(campaign_dir, party, [io_campaign.change_entry("world_choose", None, "settings.world", None, name)])
    out = {"world": name, "name": world["name"], "seeds": len(world["seeds"]),
           "next": "read the bible, then show the player the teasers of this world"}  # type: Dict[str, Any]
    out.update(safe_files(world))
    return out
