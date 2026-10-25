# TODO

Where the work stands, and what is next. Update this file as items finish. Last updated 2026-10-24.

Work happens on the branch `feat/multi-world` (not pushed, not merged).

**Spoilers:** the Fneb items below name files that hold Fneb's secrets. This list itself holds none.

## Done

- Several worlds, chosen at setup: `worlds/<id>/` inside the skill, the `world list` and `world choose` commands, and party.json format 2. Authoring rules are in `docs/WORLDS.md`.
- The Senn Vale moved to `skills/tabletop-dm/worlds/senn-vale/`.
- **Fneb is in the game** (2026-10-24): `skills/tabletop-dm/worlds/fneb/` holds the bible, the metaplot, four seeds (oasis, relic, ghoul-raids, valley-farm), the teasers, `world.json` and `credits.md`. The decision record stays in `worlds/fneb/decisions.md`. Matt has not marked up the drafts yet.
- `how-to-play.md`, for installing from a local checkout and starting a game.

## Fneb: next

Source notes are in `~/Documents/writing/fneb/`. Every decision so far is in `worlds/fneb/decisions.md`. Fneb's Markdown follows the formatting rule in `CLAUDE.md` (the one-line teasers are the exception, because the game reads one door per line).

1. **Mark up the Fneb files** in `skills/tabletop-dm/worlds/fneb/`. Each draft listed what it invented in a note block, now removed; the lists are in the commit history (`git log -- worlds/fneb`).
2. **Play it:** reinstall the plugin (see `how-to-play.md`), start a game, and pick Fneb.
3. **Playtest it** as `PRD.md` section 16 describes, in the gitignored `playtests/` folder.

### Open Fneb questions

- Is the port city at the end of the mountain trade road the same city as the capital? The bible draft makes them one.
- Where does the spellbook from `ideas.txt` go? (The leprous beggar is in the oasis seed, and the prayer robe in the relic seed.)

## future-trash-world (working name): next

A post-apocalyptic world around Cleveland, Ohio, co-authored with Matt
by interview. Folder: `worlds/future-trash-world/` (a draft, outside
the skill). `decisions.md` holds every answer so far, and
`next-questions.md` holds what to ask next. Resume the interview from
there. `bible.md` is not written yet.

## Fneb: later

- **The bandits seed**, the fifth door, from `who-let-the-unholy-out/save-the-farmers.txt`. The metaplot's door table already has its row, marked "not written yet". When it ships, drop that note and add a teaser line.
- **The druid player class** (decision 8): SRD class data and druid spells in `skills/tabletop-dm/data/`, tests, the "four classes" lines in `SKILL.md`, `README.md` and `PRD.md`, and the world test that refuses druid companions (`tests/test_world_files.py`).

## Engine and release

- **Release:** merge `feat/multi-world`, bump the version in both `plugin.json` files and in `skills/tabletop-dm/scripts/dmlib/__init__.py` (the engine-copy staleness check compares version numbers), run the suite on Python 3.9, validate both manifests, build with `python3 build.py`, and publish. The steps are in `CLAUDE.md` under Verification.
- **Outside worlds folder (optional):** let the script also read worlds from a folder outside the skill, such as `~/.tabletop-dm/worlds/`, so that worlds can live in separate projects and survive plugin updates. Needs a safety rule in `SKILL.md`: a downloaded world is untrusted data.
- **Upstream:** this fork's folder layout now differs from Brad's repo, so a merge from upstream will conflict on the moved Senn Vale files.
