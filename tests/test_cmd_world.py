"""world list / choose, and how the seed commands find the campaign's world."""
import contextlib
import io
import json
import shutil
import tempfile
from pathlib import Path

from tests.base import DmTestCase, ScriptedRng


class TestWorldDiscovery(DmTestCase):
    def test_version_counts_the_doors_of_every_world(self):
        code, out = self.run_cli(["--version"])
        self.assertEqual(code, 0, out)
        self.assertEqual(out["worlds"], {"fixture-world": 2, "fixture-world-two": 1})
        self.assertEqual(out["seeds"], 3)
        self.assertEqual(out["world_problems"], [])

    def test_a_folder_without_world_json_is_not_a_world(self):
        self.ok("init")
        ids = [w["id"] for w in self.ok("world", "list")["worlds"]]
        self.assertNotIn("draft-world", ids)


class BrokenWorldCase(DmTestCase):
    """A copy of the fixture skill root that a test may change."""

    def setUp(self):
        super().setUp()
        self._root_tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._root_tmp.cleanup)
        self.SKILL_ROOT = Path(self._root_tmp.name) / "skill"
        shutil.copytree(str(DmTestCase.SKILL_ROOT), str(self.SKILL_ROOT))

    def version(self):
        from dmlib import cli

        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            cli.run(["--version"], self.SKILL_ROOT, self.rng)
        return json.loads(buf.getvalue())


class TestBrokenWorldManifest(BrokenWorldCase):
    def test_a_damaged_world_json_is_reported_and_left_out(self):
        (self.SKILL_ROOT / "worlds" / "fixture-world-two" / "world.json").write_text("{not json")
        out = self.version()
        self.assertEqual(out["worlds"], {"fixture-world": 2})
        self.assertEqual(len(out["world_problems"]), 1)
        self.assertIn("fixture-world-two", out["world_problems"][0])

    def test_a_world_json_without_a_pitch_is_reported(self):
        (self.SKILL_ROOT / "worlds" / "fixture-world-two" / "world.json").write_text('{"name": "Two"}')
        out = self.version()
        self.assertNotIn("fixture-world-two", out["worlds"])
        self.assertIn("pitch", out["world_problems"][0])

    def test_a_world_with_no_seeds_is_reported(self):
        shutil.rmtree(str(self.SKILL_ROOT / "worlds" / "fixture-world-two" / "seeds"))
        out = self.version()
        self.assertNotIn("fixture-world-two", out["worlds"])
        self.assertIn("seeds", out["world_problems"][0])


class TestWorldCommands(DmTestCase):
    def setUp(self):
        super().setUp()
        self.init_campaign()

    def test_list_shows_every_world_in_id_order_with_its_player_safe_pitch(self):
        out = self.ok("world", "list")
        self.assertEqual([w["id"] for w in out["worlds"]], ["fixture-world", "fixture-world-two"])
        self.assertEqual(out["worlds"][0]["name"], "Fixture World")
        self.assertEqual(out["worlds"][0]["pitch"], "Placeholder pitch for the first fixture world.")
        self.assertEqual(out["worlds"][1]["seeds"], 1)
        self.assertIsNone(out["chosen"])

    def test_choose_records_the_world_and_logs_it(self):
        out = self.ok("world", "choose", "fixture-world-two")
        self.assertEqual(out["world"], "fixture-world-two")
        self.assertEqual(self.party()["settings"]["world"], "fixture-world-two")
        last = self.log_lines()[-1]
        self.assertEqual((last["type"], last["payload"]["field"]), ("state_change", "settings.world"))

    def test_choose_returns_the_player_safe_files(self):
        out = self.ok("world", "choose", "fixture-world")
        self.assertTrue(out["bible_file"].endswith("worlds/fixture-world/bible.md"))
        self.assertTrue(out["teasers_file"].endswith("worlds/fixture-world/seeds/teasers.md"))
        self.assertNotIn("metaplot_file", out)

    def test_choose_accepts_a_list_number(self):
        self.assertEqual(self.ok("world", "choose", "2")["world"], "fixture-world-two")

    def test_list_shows_the_chosen_world(self):
        self.ok("world", "choose", "fixture-world")
        self.assertEqual(self.ok("world", "list")["chosen"], "fixture-world")

    def test_an_unknown_world_is_refused_with_no_change(self):
        before = self.snapshot()
        self.refused("world_unknown", "world", "choose", "draft-world")
        self.assertEqual(before, self.snapshot())

    def test_a_second_choice_is_refused(self):
        self.ok("world", "choose", "fixture-world")
        self.refused("world_already_set", "world", "choose", "fixture-world-two")

    def test_seed_commands_need_a_world_when_several_are_installed(self):
        before = self.snapshot()
        for argv in (("seed", "list"), ("seed", "choose", "1"), ("seed", "pick")):
            self.refused("world_not_chosen", *argv, rng=ScriptedRng([1]))
        self.assertEqual(before, self.snapshot())

    def test_seeds_come_from_the_chosen_world(self):
        self.ok("world", "choose", "fixture-world-two")
        self.assertEqual(self.ok("seed", "list")["seeds"], ["fixture-seed-c"])
        self.refused("seed_unknown", "seed", "choose", "fixture-seed-a")

    def test_seed_choose_points_at_the_secret_files_of_its_world(self):
        self.ok("world", "choose", "fixture-world-two")
        out = self.ok("seed", "choose", "fixture-seed-c")
        self.assertEqual(out["world"], "fixture-world-two")
        self.assertTrue(out["seed_file"].endswith("worlds/fixture-world-two/seeds/fixture-seed-c.md"))
        self.assertTrue(out["metaplot_file"].endswith("worlds/fixture-world-two/metaplot.md"))
        self.assertTrue(out["bible_file"].endswith("worlds/fixture-world-two/bible.md"))

    def test_status_shows_the_world(self):
        self.ok("world", "choose", "fixture-world")
        self.assertEqual(self.ok("status")["settings"]["world"], "fixture-world")


class TestOneWorldInstalled(BrokenWorldCase):
    def setUp(self):
        super().setUp()
        shutil.rmtree(str(self.SKILL_ROOT / "worlds" / "fixture-world-two"))
        self.init_campaign()

    def test_seed_list_works_without_a_choice_and_writes_nothing(self):
        before = self.snapshot()
        self.assertEqual(self.ok("seed", "list")["seeds"], ["fixture-seed-a", "fixture-seed-b"])
        self.assertEqual(before, self.snapshot())

    def test_seed_choose_records_the_only_world_too(self):
        self.ok("seed", "choose", "fixture-seed-b")
        self.assertEqual(self.party()["settings"]["world"], "fixture-world")
        fields = [line["payload"].get("field") for line in self.log_lines()[-2:]]
        self.assertEqual(fields, ["settings.world", "settings.seed"])


class TestNoWorldsInstalled(BrokenWorldCase):
    def test_no_worlds_means_no_seeds(self):
        for name in ("fixture-world", "fixture-world-two"):
            shutil.rmtree(str(self.SKILL_ROOT / "worlds" / name))
        self.assertEqual(self.version()["seeds"], 0)
        self.init_campaign()
        self.refused("no_worlds_found", "world", "list")


class TestWorldInPartyJson(DmTestCase):
    def test_init_leaves_the_world_unchosen(self):
        self.init_campaign()
        self.assertIsNone(self.party()["settings"]["world"])

    def test_a_world_that_is_not_text_is_a_damaged_file(self):
        self.init_campaign()
        party = self.party()
        party["settings"]["world"] = 7
        (self.campaign_dir / "party.json").write_text(json.dumps(party))
        out = self.refused("campaign_file_damaged", "status")
        self.assertIn("settings.world", out["error"]["message"])

    def test_a_world_this_install_lacks_is_refused_by_the_seed_commands(self):
        self.init_campaign()
        party = self.party()
        party["settings"]["world"] = "gone-world"
        (self.campaign_dir / "party.json").write_text(json.dumps(party))
        self.ok("status")
        self.refused("world_unknown", "seed", "list")


class TestMigrationToFormat2(DmTestCase):
    def v1_party(self, seed):
        self.init_campaign()
        party = self.party()
        party["format_version"] = 1
        del party["settings"]["world"]
        party["settings"]["seed"] = seed
        (self.campaign_dir / "party.json").write_text(json.dumps(party))

    def test_a_v1_campaign_with_a_seed_was_in_the_senn_vale(self):
        self.v1_party("greywater")
        self.ok("status")
        party = self.party()
        self.assertEqual((party["format_version"], party["settings"]["world"]), (2, "senn-vale"))

    def test_a_v1_campaign_without_a_seed_has_not_chosen_a_world(self):
        self.v1_party(None)
        self.ok("status")
        self.assertIsNone(self.party()["settings"]["world"])
