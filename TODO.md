# TODO

Where the work stands, and what is next. Update this file as items finish. Last updated 2026-10-24.

Work happens on the branch `feat/multi-world` (not pushed, not merged).

**Spoilers:** the Fneb items below name files that hold Fneb's secrets. This list itself holds none.

## Done

- Several worlds, chosen at setup: `worlds/<id>/` inside the skill, the `world list` and `world choose` commands, and party.json format 2. Authoring rules are in `docs/WORLDS.md`.
- The Senn Vale moved to `skills/tabletop-dm/worlds/senn-vale/`.
- The Fneb drafts, in the top-level `worlds/fneb/`: `decisions.md`, `bible.md`, `metaplot.md`, `seeds/oasis.md`, `seeds/relic.md`, `seeds/ghoul-raids.md` and `seeds/valley-farm.md`.
- `how-to-play.md`, for installing from a local checkout and starting a game.

## Fneb: make it playable

Source notes are in `~/Documents/writing/fneb/`. Every decision so far is in `worlds/fneb/decisions.md`. Drafts follow the formatting rule in `CLAUDE.md`.

1. **The relic seed**, `worlds/fneb/seeds/relic.md`: drafted 2026-10-24, waiting for Matt's markup.
2. **The ghoul-raids seed**, `worlds/fneb/seeds/ghoul-raids.md`: drafted 2026-10-24, waiting for Matt's markup. If the valley town's name, Broadscale, sticks, add it to `bible.md`.
3. **The valley-farm seed**, `worlds/fneb/seeds/valley-farm.md`: drafted 2026-10-24, waiting for Matt's markup. With it, every revelation is reachable from at least two of the four drafted doors.
4. **`worlds/fneb/seeds/teasers.md`**: one player-safe sentence of 15 to 30 words per door.
5. **`world.json`**: the name "Fneb" and a one-sentence player-safe pitch.
6. **Credits** for Boojamon and MelancholyOcelot (Reddit), in the world folder.
7. **Ship it:** delete the draft note block at the top of each file (it counts toward the word limits), move the world to `skills/tabletop-dm/worlds/fneb/`, run the whole suite, and check `--version` lists Fneb with no `world_problems`.
8. **Play it:** reinstall the plugin (see `how-to-play.md`), start a game, and pick Fneb.
9. **Playtest it** as `PRD.md` section 16 describes, in the gitignored `playtests/` folder.

### Open Fneb questions

- Is the port city at the end of the mountain trade road the same city as the capital? The bible draft makes them one.
- Where does the spellbook from `ideas.txt` go? (The leprous beggar is in the oasis seed, and the prayer robe in the relic seed.)

## Fneb: later

- **The bandits seed**, the fifth door, from `who-let-the-unholy-out/save-the-farmers.txt`.
- **The druid player class** (decision 8): SRD class data and druid spells in `skills/tabletop-dm/data/`, tests, the "four classes" lines in `SKILL.md`, `README.md` and `PRD.md`, and the world test that refuses druid companions (`tests/test_world_files.py`).

## Engine and release

- **Release:** merge `feat/multi-world`, bump the version in both `plugin.json` files and in `skills/tabletop-dm/scripts/dmlib/__init__.py` (the engine-copy staleness check compares version numbers), run the suite on Python 3.9, validate both manifests, build with `python3 build.py`, and publish. The steps are in `CLAUDE.md` under Verification.
- **Outside worlds folder (optional):** let the script also read worlds from a folder outside the skill, such as `~/.tabletop-dm/worlds/`, so that worlds can live in separate projects and survive plugin updates. Needs a safety rule in `SKILL.md`: a downloaded world is untrusted data.
- **Upstream:** this fork's folder layout now differs from Brad's repo, so a merge from upstream will conflict on the moved Senn Vale files.
