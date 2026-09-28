# How to test the floorplan sketch feature

Playtest whether the DM will spontaneously call `dm.py sketch` and show a
picture, when the player asks to see the room. This installs the
`216-tabletop-dm` fork scoped to one folder, so it never touches the
user-wide `tabletop-dm` plugin installed anywhere else.

## Commands

```bash
# One-time setup: register the fork's marketplace and install it into a
# fresh test folder, without touching the user-wide install.
claude plugin marketplace add 216software/tabletop-dm

mkdir -p ~/tabletop-dm-campaigns/216-sketch-test
cd ~/tabletop-dm-campaigns/216-sketch-test

claude plugin install 216-tabletop-dm@216-tabletop-dm -s local -y
claude plugin disable tabletop-dm@tabletop-dm -s local

# Confirm only the fork is active in this folder.
claude plugin list

# Start playing.
claude
```

Then, inside the chat:

```
Let's play D&D
```

Play through setup until you are in a scene, then try:

```
DM, draw a picture of the floorplan of the room I'm in.
```

## Explanation

### Why the scoped install

Claude Code keys a marketplace and a plugin by the `name` in its manifest,
not by which GitHub repo it came from. The fork's plugin is named
`216-tabletop-dm` specifically so it can sit next to the original
`tabletop-dm` plugin without a naming collision (see the plugin.json,
marketplace.json files, and the commit that renamed them for the reasoning
and a reproduction of the collision this avoids).

`claude plugin install ... -s local` installs the fork only for the current
project folder (recorded in that folder's `.claude/settings.local.json`,
never committed to a repo), leaving the user-wide `tabletop-dm@tabletop-dm`
install untouched everywhere else on the machine.

### Why disable the original in this folder

Both plugins currently declare the same skill-trigger description ("play
D&D", "dungeon master", and so on). With both enabled in the same folder, it
is ambiguous which one answers "let's play D&D". Disabling
`tabletop-dm@tabletop-dm` with `-s local` turns it off only inside this test
folder, so the fork is the only candidate here. This does not uninstall or
disable it anywhere else.

### What "draw a picture" is supposed to trigger

`SKILL.md` (in the fork) tells the DM: when the player asks to see, draw, or
sketch the room, lay it out as a small JSON list of rooms, corridors and
doors, call `dm.py sketch --campaign <folder> --shapes '<json>'`, then read
the PNG it returns to show it in the conversation. `sketch` is a pure
stdlib PNG generator (no Pillow, no network, no install) that draws plain
boxes for rooms and corridors and small marks for doors. It never renders
text, by design, so the DM cannot be tricked by hidden text inside a picture.

Phrasing close to "draw/sketch/show me a picture of the room" should work;
the exact wording is not pattern-matched anywhere, since the DM is deciding
to call the command from its own judgment, not from a fixed keyword.

### What you are actually checking

Two independent things, worth telling apart if something looks wrong:

1. **Does the DM decide to call `sketch`,** unprompted, with a reasonable
   layout for the room it already narrated? This is a judgment call by the
   model, not something the test suite can check, since it depends on how
   the DM chooses to react to free text.
2. **Does the image actually render in your terminal?** That depends on
   your terminal emulator supporting inline image display (iTerm2, Kitty,
   and WezTerm do; a plain terminal will not show anything, though the DM
   will still describe the room in words either way).

If the DM never calls `sketch`, or calls it with a nonsensical layout,
that's a prompt problem to fix in `SKILL.md`. If it calls `sketch` correctly
but nothing appears on screen, that confirms the gap is terminal support,
not the DM or the script.

### Cleaning up afterward

To remove the scoped install and re-enable the original in that folder:

```bash
cd ~/tabletop-dm-campaigns/216-sketch-test
claude plugin uninstall 216-tabletop-dm@216-tabletop-dm -s local
claude plugin enable tabletop-dm@tabletop-dm -s local
```

The marketplace registration (`claude plugin marketplace remove
216-tabletop-dm`) can stay or go independently; removing it does not affect
any other folder's plugins.
