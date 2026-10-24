"""Structure tests for every installed world: its bible, metaplot and seeds.

SPOILER WALL: these tests read the secret files, so no assertion here may print file content.
Every check is a plain True/False with a message that names the world, the file and the rule only.
"""
import re

from tests.base import REAL_SKILL_ROOT, unittest
from tests.test_data_real import BANNED

WORLDS_DIR = REAL_SKILL_ROOT / "worlds"
SENN_VALE_SEEDS = ["brannocks-cut", "greywater", "hushwood", "sallows", "tollhills"]
SEED_SECTIONS = ["Tone", "Start place", "The opening scene", "What is really going on here", "The local villain",
                 "Other people", "Companion candidates", "If the hero does nothing", "Fights", "Local secrets",
                 "The way in to the larger mystery", "Ways it can end"]
# "The five revelations" and "The nine rumours" in the Senn Vale. Another world may have a different count.
METAPLOT_SECTIONS = ["The truth", "Who is behind it", "How it started", "The clock", r"The \w+ revelations",
                     r"The \w+ rumours", "Which door reaches what", "How to run it", "The moral question"]
MIN_SEEDS = 3
MIN_REVELATIONS = 3


def installed_worlds():
    from dmlib import data

    worlds, problems = data.list_worlds(REAL_SKILL_ROOT)
    return worlds, problems


def revelation_codes(metaplot):
    match = re.search(r"^## The \w+ revelations$", metaplot, re.M)
    part = metaplot[match.end():] if match else ""
    end = part.find("\n## ")
    part = part[:end] if end >= 0 else part
    return sorted(set(re.findall(r"\bR\d+\b", part)), key=lambda code: int(code[1:]))


def story_files(world):
    seeds = world["dir"] / "seeds"
    return ([world["dir"] / "bible.md", world["dir"] / "metaplot.md", seeds / "teasers.md"]
            + [seeds / (n + ".md") for n in world["seeds"]])


class TestWorldFiles(unittest.TestCase):
    def setUp(self):
        self.worlds, self.problems = installed_worlds()

    def test_every_world_manifest_is_sound(self):
        self.assertEqual(self.problems, [])
        self.assertTrue(self.worlds, "the skill ships no world")

    def test_every_world_folder_has_a_manifest(self):
        ids = sorted(w["id"] for w in self.worlds)
        folders = sorted(p.name for p in WORLDS_DIR.iterdir() if p.is_dir())
        self.assertEqual(ids, folders, "a folder in worlds/ has no world.json (keep drafts out of the shipped skill)")

    def test_the_senn_vale_has_exactly_its_five_doors(self):
        senn = [w for w in self.worlds if w["id"] == "senn-vale"]
        self.assertEqual(len(senn), 1)
        self.assertEqual(senn[0]["seeds"], SENN_VALE_SEEDS)
        self.assertEqual(revelation_codes((senn[0]["dir"] / "metaplot.md").read_text()), ["R1", "R2", "R3", "R4", "R5"])

    def test_every_pitch_is_one_player_safe_sentence(self):
        for world in self.worlds:
            words = len(world["pitch"].split())
            self.assertTrue(10 <= words <= 45, "%s: the pitch must be one sentence of about 15 to 40 words" % world["id"])

    def test_every_story_file_exists(self):
        for world in self.worlds:
            for path in story_files(world):
                self.assertTrue(path.is_file(), "%s: %s is missing" % (world["id"], path.name))

    def test_every_world_has_enough_doors_and_only_seeds_in_its_seed_folder(self):
        for world in self.worlds:
            self.assertTrue(len(world["seeds"]) >= MIN_SEEDS, "%s needs at least %d seeds" % (world["id"], MIN_SEEDS))
            names = sorted(p.stem for p in (world["dir"] / "seeds").glob("*.md"))
            self.assertEqual(names, sorted(world["seeds"] + ["teasers"]))

    def test_teasers_has_one_line_per_seed_in_the_documented_format(self):
        for world in self.worlds:
            lines = [ln for ln in (world["dir"] / "seeds" / "teasers.md").read_text().splitlines() if ln.strip()]
            self.assertEqual(len(lines), len(world["seeds"]), "%s: teasers.md must have one line per seed" % world["id"])
            found = []
            for line in lines:
                match = re.match(r"^([a-z0-9-]+): (.+)$", line)
                self.assertTrue(bool(match), "%s: a teaser line is not in the 'name: sentence' format" % world["id"])
                found.append(match.group(1))
                words = len(match.group(2).split())
                self.assertTrue(10 <= words <= 40, "%s: a teaser must be one sentence of about 15 to 30 words" % world["id"])
            self.assertEqual(sorted(found), sorted(world["seeds"]))

    def test_every_seed_has_every_section_in_order(self):
        for world in self.worlds:
            for name in world["seeds"]:
                text = (world["dir"] / "seeds" / (name + ".md")).read_text()
                positions = [text.find("## " + section) for section in SEED_SECTIONS]
                self.assertTrue(all(p >= 0 for p in positions), "%s/%s.md is missing a required section" % (world["id"], name))
                self.assertTrue(positions == sorted(positions), "%s/%s.md has its sections out of order" % (world["id"], name))

    def test_every_seed_is_a_page_or_two(self):
        for world in self.worlds:
            for name in world["seeds"]:
                words = len((world["dir"] / "seeds" / (name + ".md")).read_text().split())
                # Read once per campaign, so length is cheap. The cap only stops a seed becoming a script.
                self.assertTrue(450 <= words <= 1900, "%s/%s.md should be 450 to 1900 words" % (world["id"], name))

    def test_every_metaplot_has_every_section_and_enough_revelations(self):
        for world in self.worlds:
            text = (world["dir"] / "metaplot.md").read_text()
            for section in METAPLOT_SECTIONS:
                self.assertTrue(re.search(r"^## " + section, text, re.M) is not None,
                                "%s: metaplot.md is missing the section '%s'" % (world["id"], section))
            self.assertTrue(len(revelation_codes(text)) >= MIN_REVELATIONS,
                            "%s: metaplot.md needs at least %d revelations, R1, R2 and on" % (world["id"], MIN_REVELATIONS))

    def test_every_seed_points_at_the_metaplot_but_not_all_of_it(self):
        for world in self.worlds:
            codes = revelation_codes((world["dir"] / "metaplot.md").read_text())
            for name in world["seeds"]:
                text = (world["dir"] / "seeds" / (name + ".md")).read_text()
                way_in = text[text.find("## The way in to the larger mystery"):text.find("## Ways it can end")]
                reached = set(re.findall(r"\bR\d+\b", way_in)) & set(codes)
                self.assertTrue(len(reached) >= 2, "%s/%s.md must name the revelations it can reach" % (world["id"], name))
                self.assertTrue(len(reached) < len(codes), "%s/%s.md must not reach every revelation" % (world["id"], name))

    def test_every_revelation_is_reachable_from_at_least_two_doors(self):
        for world in self.worlds:
            text = (world["dir"] / "metaplot.md").read_text()
            table = text[text.find("## Which door reaches what"):text.find("## How to run it")]
            rows = [ln for ln in table.splitlines() if ln.startswith("|") and any(n in ln for n in world["seeds"])]
            for code in revelation_codes(text):
                reach = 0
                for row in rows:
                    cells = [c.strip() for c in row.strip("|").split("|")]
                    if len(cells) >= 2 and re.search(r"\b%s\b" % code, cells[1]):
                        reach += 1
                self.assertTrue(reach >= 2, "%s: %s must be reachable from at least two doors" % (world["id"], code))

    def test_no_em_dashes_and_no_product_identity(self):
        for world in self.worlds:
            for path in story_files(world) + [world["dir"] / "world.json"]:
                text = path.read_text()
                self.assertTrue("\u2014" not in text, "%s: %s contains an em-dash" % (world["id"], path.name))
                lowered = text.lower()
                for term in BANNED:
                    hit = re.search(r"(?<![a-z])" + re.escape(term) + r"(?![a-z])", lowered)
                    self.assertTrue(hit is None, "%s: %s contains a banned product-identity term (index %d of the ban list)"
                                    % (world["id"], path.name, BANNED.index(term)))

    def test_companion_candidates_use_only_the_four_classes(self):
        for world in self.worlds:
            for name in world["seeds"]:
                text = (world["dir"] / "seeds" / (name + ".md")).read_text()
                part = text[text.find("## Companion candidates"):text.find("## If the hero does nothing")].lower()
                self.assertTrue(any(c in part for c in ("fighter", "rogue", "wizard", "cleric")),
                                "%s/%s.md names no class for its companions" % (world["id"], name))
                for other in ("barbarian", "bard", "druid", "monk", "paladin", "ranger", "sorcerer", "warlock"):
                    self.assertTrue(re.search(r"\b%s\b" % other, part) is None,
                                    "%s/%s.md gives a companion a class this build does not have" % (world["id"], name))

    def test_fights_name_monsters_that_exist_in_the_data(self):
        from dmlib import data

        monsters = data.load_all(REAL_SKILL_ROOT)["monsters"]
        names = sorted(monsters, key=len, reverse=True)
        for world in self.worlds:
            for seed in world["seeds"]:
                text = (world["dir"] / "seeds" / (seed + ".md")).read_text()
                part = text[text.find("## Fights"):text.find("## Local secrets")].lower().replace(" ", "-")
                found = [m for m in names if m in part]
                self.assertTrue(len(found) >= 2,
                                "%s/%s.md must name at least two monsters from the rules data in Fights" % (world["id"], seed))
