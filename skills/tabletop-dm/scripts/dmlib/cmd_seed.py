"""seed list / choose / pick. The seed name is recorded once per campaign, from the campaign's world."""
import argparse
import random
import re
from pathlib import Path
from typing import Any, Dict, List

from . import cmd_world, io_campaign, party_ops
from .errors import DmError


def _seeds(world: Dict[str, Any]) -> List[str]:
    """Seed names in DOOR order: the order of the world's seeds/teasers.md, which is the order the player sees."""
    names = world["seeds"]
    teasers = world["dir"] / "seeds" / "teasers.md"
    ordered = []  # type: List[str]
    if teasers.is_file():
        for line in teasers.read_text().splitlines():
            match = re.match(r"^[-*\s\d.]*([a-z0-9-]+):", line.strip())
            if match and match.group(1) in names and match.group(1) not in ordered:
                ordered.append(match.group(1))
    return ordered + [n for n in names if n not in ordered]


def _record(campaign_dir: Path, party: Dict[str, Any], name: str, world: Dict[str, Any],
            entries: List[Dict[str, Any]], command: str) -> Dict[str, Any]:
    party["settings"]["seed"] = name
    entries.append(io_campaign.change_entry(command, None, "settings.seed", None, name))
    party_ops.commit(campaign_dir, party, entries)
    out = {"world": world["id"], "seed": name,
           "seed_file": (world["dir"] / "seeds" / (name + ".md")).as_posix(),
           "metaplot_file": (world["dir"] / "metaplot.md").as_posix(),
           "next": "copy the seed file into dm-secrets.md under '## Seed', then write the campaign plan"}
    out.update(cmd_world.safe_files(world))
    return out


def _load_unseeded(campaign_dir: Path) -> Dict[str, Any]:
    party = io_campaign.load_party(campaign_dir)
    if party["settings"]["seed"]:
        raise DmError("seed_already_set", "this campaign already chose %s." % party["settings"]["seed"])
    return party


def seed_list(args: argparse.Namespace, skill_root: Path, rng: random.Random) -> Dict[str, Any]:
    party = io_campaign.load_party(Path(args.campaign))
    world = cmd_world.resolve(party, skill_root, [], "seed_list")     # read-only: nothing is saved
    return {"world": world["id"], "seeds": _seeds(world),
            "teasers_file": (world["dir"] / "seeds" / "teasers.md").as_posix()}


def seed_choose(args: argparse.Namespace, skill_root: Path, rng: random.Random) -> Dict[str, Any]:
    campaign_dir = Path(args.campaign)
    party = _load_unseeded(campaign_dir)
    entries = []  # type: List[Dict[str, Any]]
    world = cmd_world.resolve(party, skill_root, entries, "seed_choose")
    names = _seeds(world)
    name = party_ops.slugify(args.name)
    if name.isdigit() and 1 <= int(name) <= len(names):
        name = names[int(name) - 1]           # the player said "door 2"
    if name not in names:
        raise DmError("seed_unknown", "no seed '%s' in %s. Seeds: %s." % (args.name, world["id"], ", ".join(names)))
    return _record(campaign_dir, party, name, world, entries, "seed_choose")


def seed_pick(args: argparse.Namespace, skill_root: Path, rng: random.Random) -> Dict[str, Any]:
    campaign_dir = Path(args.campaign)
    party = _load_unseeded(campaign_dir)
    entries = []  # type: List[Dict[str, Any]]
    world = cmd_world.resolve(party, skill_root, entries, "seed_pick")
    names = _seeds(world)
    index = rng.randint(1, len(names))
    entries.append(io_campaign.roll_entry("seed_pick", {"kind": "seed_pick", "expr": "1d%d" % len(names),
                                                        "rolls": [index], "total": index}))
    out = _record(campaign_dir, party, names[index - 1], world, entries, "seed_pick")
    # The seed name and file are secret. These three are safe to show.
    out.update({"roll": index, "doors": len(names), "door": index,
                "show_the_player": "d%d (%d): door %d" % (len(names), index, index)})
    return out
