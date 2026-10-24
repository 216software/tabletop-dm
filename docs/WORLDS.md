# Worlds: how to add one

Spoiler wall: this file holds no story content. It describes the shape of a world, not any world's secrets.

A world is one self-contained folder under `skills/tabletop-dm/worlds/`. At setup the DM shows the player every installed world (its name and pitch), the player picks one, and the doors (seeds) then come from that world. Adding a world is a data change: no code, no `SKILL.md` change.

## The folder

```
skills/tabletop-dm/worlds/<world-id>/
  world.json          the manifest: name and pitch, both player-safe
  bible.md            common knowledge. Player-safe
  metaplot.md         the hidden truth. DM only
  seeds/
    teasers.md        one player-safe sentence per door
    <seed-name>.md    one file per door. DM only
```

- `<world-id>` is a lowercase slug (`a-z`, `0-9`, single hyphens). It is what `world choose` records in `party.json`, so never rename a world that someone has a campaign in.
- **A folder without `world.json` is a draft.** The script ignores it, so you can build a world in place. The test suite refuses a draft in the shipped skill (`test_every_world_folder_has_a_manifest`), so finish it, or keep it out of `worlds/` while you commit other work.
- A broken `world.json`, or a world with no seeds, is left out of the list and named in `--version` under `world_problems`.

## world.json

```json
{
  "name": "The Senn Vale",
  "pitch": "One sentence of about 15 to 40 words. The player reads it when choosing a world."
}
```

Both fields are shown to the player, so neither may hint at the metaplot. Other keys are ignored, so a world may carry its own `author`, `version` or `source` for later use.

## bible.md

What a person who grew up there knows. Free form, but the Senn Vale's sections are a good checklist: the world in one paragraph, tone, the known past, the places, the peoples, faith, power and money, magic, monsters, rumours, names, and what the DM must keep consistent. Keep the tone compatible with 5e rules and SRD monsters: the script has no other rules.

## metaplot.md

These `##` sections, in this order:

1. `The truth`
2. `Who is behind it`
3. `How it started`
4. `The clock`
5. `The <count> revelations`: at least 3, labelled `R1`, `R2` and on
6. `The <count> rumours`
7. `Which door reaches what`: a table with one row per seed, the seed name in the first cell and the revelation codes it reaches in the second
8. `How to run it`
9. `The moral question`

Every revelation must be reachable from at least two doors, and no single door may reach all of them.

## Seeds

At least 3 per world. Each seed is 450 to 1900 words, a situation and not a script, with these `##` sections in order:

`Tone`, `Start place`, `The opening scene`, `What is really going on here`, `The local villain`, `Other people`, `Companion candidates`, `If the hero does nothing`, `Fights`, `Local secrets`, `The way in to the larger mystery`, `Ways it can end`.

- **Companion candidates:** 2 or 3, each a Fighter, Rogue, Wizard or Cleric (the four classes this build has).
- **Fights:** name at least two monsters that exist in `skills/tabletop-dm/data/monsters.json` (`lookup monster --list`). A custom monster is fine too, as JSON for `encounter start --custom`.
- **The way in to the larger mystery:** name the revelation codes (`R2`, `R4`) this door can reach.
- If the seed has a deadline, give the number of days, so that the DM can start a secret counter.

`teasers.md` has one line per seed: `<seed-name>: <one sentence of about 15 to 30 words>`. The line order is the door order the player sees.

## Rules every file follows

- SRD 5.1 content only, with no Wizards product identity. The ban list is in `tests/test_data_real.py`.
- No em-dashes.
- `tests/test_world_files.py` checks all of this for every world, and prints only the world, the file and the rule, never content.

## Spoilers

If someone else will play the world, the person who plays it should not write or read `metaplot.md` and the seed files. The repo is public, so the spoiler wall in `CLAUDE.md` covers every world: commit messages for secret files stay generic ("add seed 3 to <world-id>").

## Steps

1. Draft the world in the repo-root `worlds/<world-id>/` folder. It is outside the skill, so the build does not ship it and the tests do not check it. Notes and decision records can live there too.
2. When it is ready, move `bible.md`, `metaplot.md` and `seeds/` to `skills/tabletop-dm/worlds/<world-id>/`, and write `world.json` last. The world is live from that moment.
3. Run the suite: `python3 -B -m unittest discover -s tests -p "test_*.py" -t .`
4. Run `python3 skills/tabletop-dm/scripts/dm.py --version` and check that the world shows under `worlds` with no `world_problems`.
5. Playtest it as `PRD.md` section 16 describes, in the gitignored `playtests/` folder.
