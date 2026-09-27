import json

from tests.base import DmTestCase

ROOM = json.dumps([
    {"type": "room", "x": 0, "y": 0, "w": 5, "h": 5},
    {"type": "door", "x": 5, "y": 2},
    {"type": "corridor", "x": 5, "y": 2, "w": 3, "h": 1},
    {"type": "room", "x": 8, "y": 0, "w": 3, "h": 4},
])


class TestSketch(DmTestCase):
    def setUp(self):
        super().setUp()
        self.init_campaign()

    def test_writes_a_real_png_under_the_campaign_folder(self):
        out = self.ok("sketch", "--shapes", ROOM)
        path = self.campaign_dir / "art" / (out["name"] + ".png")
        self.assertTrue(path.is_file())
        self.assertEqual(path.read_bytes()[:8], b"\x89PNG\r\n\x1a\n")
        self.assertEqual(out["path"], str(path))
        self.assertGreater(out["width"], 0)
        self.assertGreater(out["height"], 0)

    def test_default_name_is_sketch(self):
        out = self.ok("sketch", "--shapes", ROOM)
        self.assertEqual(out["name"], "sketch")

    def test_custom_name_is_slugified_into_the_filename(self):
        out = self.ok("sketch", "--shapes", ROOM, "--name", "The Goblin Den!")
        self.assertEqual(out["name"], "the-goblin-den")
        self.assertTrue((self.campaign_dir / "art" / "the-goblin-den.png").is_file())

    def test_regenerating_the_same_name_overwrites_it(self):
        first = self.ok("sketch", "--shapes", ROOM, "--name", "room")
        bigger = json.dumps([{"type": "room", "x": 0, "y": 0, "w": 20, "h": 20}])
        second = self.ok("sketch", "--shapes", bigger, "--name", "room")
        self.assertNotEqual(first["width"], second["width"])
        path = self.campaign_dir / "art" / "room.png"
        self.assertEqual(path.read_bytes()[:8], b"\x89PNG\r\n\x1a\n")

    def test_refuses_invalid_json(self):
        self.refused("bad_arguments", "sketch", "--shapes", "not json")

    def test_refuses_a_shape_with_an_unknown_type(self):
        bad = json.dumps([{"type": "castle", "x": 0, "y": 0, "w": 1, "h": 1}])
        self.refused("bad_arguments", "sketch", "--shapes", bad)

    def test_refuses_an_empty_shape_list(self):
        self.refused("bad_arguments", "sketch", "--shapes", "[]")

    def test_refuses_a_room_with_no_size(self):
        bad = json.dumps([{"type": "room", "x": 0, "y": 0}])
        self.refused("bad_arguments", "sketch", "--shapes", bad)

    def test_refuses_a_sketch_too_big_to_be_simple(self):
        bad = json.dumps([{"type": "room", "x": 0, "y": 0, "w": 1000, "h": 1000}])
        self.refused("bad_arguments", "sketch", "--shapes", bad)

    def test_a_refusal_writes_no_file(self):
        before = self.snapshot()
        self.refused("bad_arguments", "sketch", "--shapes", "[]")
        self.assertFalse((self.campaign_dir / "art").exists())
        self.assertEqual(self.snapshot(), before)
