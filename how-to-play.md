# How to play from a local checkout

This guide is for someone who has just cloned this repository and wants to play. It installs the game into Claude Code straight from your copy of the repo, so you play exactly the version you have checked out.

To install from GitHub instead, or to use the Claude desktop app, ChatGPT or Codex, see `README.md`.

## What you need

- **Claude Code**, signed in with your Claude plan. The game uses your plan and needs no API key.
- **Python 3.9 or newer**, as `python3` (or `python`). Check with `python3 --version`.
- **This repository**, cloned somewhere that will stay put:

  ```
  git clone https://github.com/216software/tabletop-dm.git
  ```

Claude Code reads the plugin from this folder, so do not move or delete it while the game is installed.

## Install

From a terminal, with the path to your clone:

```
claude plugin marketplace add /path/to/tabletop-dm
claude plugin install 216-tabletop-dm@216-tabletop-dm
```

The first line registers your checkout as a plugin source, and the second installs the game from it. Restart Claude Code, or run `/reload-plugins` inside it.

To check that it worked, run `claude plugin list`. You should see `216-tabletop-dm@216-tabletop-dm` marked as enabled.

You can also type the same two steps inside Claude Code: `/plugin marketplace add /path/to/tabletop-dm`, then `/plugin install 216-tabletop-dm@216-tabletop-dm`.

## Start a game

1. **Make a new, empty folder for the game.** That folder is your save game. Use a separate folder for each campaign, and never use the repository itself: the game refuses to start in a folder that is not empty.

   ```
   mkdir -p ~/games/my-campaign
   cd ~/games/my-campaign
   claude
   ```

2. **Say: let's play D&D.** The Dungeon Master takes it from there. Setup takes about five minutes:

   - The DM runs a quick self-test and creates the save files.
   - **You pick a world** from a numbered list, each with a one-line description.
   - Four quick questions: tone, the balance of fights, talk and exploration, difficulty, and length. Answer "defaults" to skip them.
   - **You pick a door,** the adventure that starts your campaign, or say "surprise me".
   - You make a hero. "Quick start" gives you a ready hero from just a name and a class: Fighter, Rogue, Wizard or Cleric.
   - You may take one or two companions.
   - The story begins.

Claude Code will ask permission the first time the DM runs the game's script or writes a save file. Allow it, or the game cannot save.

## Playing

Type what your hero does, in your own words. There are no menus. The DM plays everyone else and describes the world. A small script rolls every die openly and keeps your hit points, spell slots, gold and inventory honest.

Things you can say outside the story:

| Say | To |
|---|---|
| show my sheet | See your character |
| what's in my pack | See your inventory |
| what can I do? | Get three ideas for this moment |
| make it harder, or lighter, or darker | Change the settings |
| let's stop here | Save and stop |

## Stop and come back

Say **let's stop here**. The DM writes a summary and saves.

The game also saves every number the moment it changes, and the story at every scene, so closing the window by accident costs you a scene at most.

To come back, open the same folder in Claude Code and say **continue**:

```
cd ~/games/my-campaign
claude
```

Then type: continue.

If a chat gets very long and the DM starts to forget things, say "let's stop here", start a new chat in the same folder, and say "continue". The DM reloads everything from the save files.

## Your save folder

| File | What it is |
|---|---|
| `journal.md` | The story so far. Yours to read |
| `world.md` | People, places and open quests you know about. Yours to read |
| `party.json`, `log.jsonl` | The numbers, and a record of every roll. Do not edit them |
| `dm-secrets.md` | The DM's notes. Reading it spoils the story |

## Avoiding spoilers

Each world's secrets live in the repository. To play unspoiled, do not open:

- `skills/tabletop-dm/worlds/*/metaplot.md`
- `skills/tabletop-dm/worlds/*/seeds/` (except `teasers.md`)
- `worlds/` at the top of the repo, which holds drafts of worlds still being written

## Getting new versions

After you `git pull` new changes, reinstall the plugin. `claude plugin update` is not enough: it does not notice changes in your checkout unless the version number went up.

```
claude plugin marketplace update 216-tabletop-dm
claude plugin uninstall 216-tabletop-dm@216-tabletop-dm
claude plugin install 216-tabletop-dm@216-tabletop-dm
```

Then restart Claude Code. Your campaigns are safe: they live in their own folders, and reinstalling never touches them.

## Which worlds can I play?

Only the worlds in `skills/tabletop-dm/worlds/` appear in the game. Right now that is **the Senn Vale**. The top-level `worlds/` folder holds worlds that are still being written, such as Fneb, and those do not appear until they move into the skill.

## Uninstall

```
claude plugin uninstall 216-tabletop-dm@216-tabletop-dm
claude plugin marketplace remove 216-tabletop-dm
```

## If something goes wrong

| What you see | What to do |
|---|---|
| The DM says Python is missing | Install Python 3.9 or newer from python.org, then start a new chat |
| `write_guard_failed` | The folder is not empty. Make a new empty folder and start again there |
| "let's play D&D" does nothing special | The plugin is not loaded. Run `claude plugin list`, then restart Claude Code |
| The DM cannot save | Allow Claude Code to run the game's script and write files in your game folder |
| `campaign_busy` | Two commands ran at once. It clears on its own. Say "try that again" |
| Anything else | See "If something goes wrong" in `README.md` |
