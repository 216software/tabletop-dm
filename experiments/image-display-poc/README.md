# Image display POC

Scratch material for [216software/tabletop-dm#1](https://github.com/216software/tabletop-dm/issues/1),
"Show images in conversation". Not part of the shipped skill, and `dm.py`
never calls anything here.

Findings so far:

- In Claude Code, having the DM `Read` an image file path renders the image
  inline in the conversation. Unverified in Cowork or claude.ai.
- [`renovation`](https://github.com/Nikolay-Lysenko/renovation) (MIT, YAML
  config, matplotlib) draws clean dungeon-style floorplans, but needs
  `pip install` and Python >= 3.10 — both ruled out for `dm.py` itself by
  `CLAUDE.md`'s hard constraints. Treat it as an offline content-authoring
  tool (like the hand-authored seed `.md` files), not a live in-session
  generator.

## Try it

```
./generate_floorplan.sh          # builds a venv on first run, then renders dungeon.yml
```

Output lands in `output/` (gitignored). Edit `dungeon.yml` to try other
layouts — see `renovation`'s README for the element reference.

## If dynamic, in-session floorplans are wanted later

Write a minimal stdlib-only PNG encoder (`zlib` + `struct`) for simple
line/rectangle dungeon maps, so it can live inside `dm.py`'s own constraints.
