# future-trash-world: what to discuss next

Resume the interview here. Claude asks one question at a time, with a
recommendation and options. Matt answers, and Claude takes notes in
`decisions.md`. All answers so far are in `decisions.md`.

Question 36 is answered (three roles: fighter, biological expert,
robotics expert) and recorded in `decisions.md`. Its follow-ups are
still open: companions after mission one, the rogue class elsewhere,
the supervisor's rank markers, and the first ruin.

## Next up

0. **Q36, pending: how the player gets a role on the permit team.**
   Recommended: the player picks any class, and the corporation
   assigns the matching team slot (security, infiltrator, medic,
   analyst), with NPCs filling the other slots. Alternatives: four
   fixed roles, or slot first and then a class from a short list.
   Also ask: are the teammates companions the player keeps after the
   first mission, or one-mission characters? Then ask how the
   supervisor's rank shows (badge, clothes) and what the first
   ruin looks like. The crooked supervisor is plot, so it goes in
   the secret files later.

1. **Starting positions 2 and 3.** Position 1 (the permit
   contractor) is done. Matt said he would define two or three.
   For each: who they are, where the game begins, and what they want
   first. Suggested spread: one inside the system (a contractor with
   a permit), one outside it (a scavenger who slipped through the
   cracks), one tied to a belief (a Warlock or trash druid). Each can
   carry the debt hook.

2. **Death and revival.** Assumed permanent, with a leashed clinic
   return. Confirm or change.

3. **The AI taboo penalty.** Assumed that it depends on who you are
   (the poor lose the machine, the wealthy have approved ones).
   Confirm. Can a patched, safe robot ever be accepted?

4. **Water.** Assumed that cost rises with distance from the lake.
   How does a peasant in the dry interior get water, and what does it
   cost?

5. **Names.** React to the placeholders listed in `decisions.md`, and
   name the Cleveland government-corporation. Name the New Amish
   faction if it is changing.

6. **How far do the radicals go?** Trash druids are peaceful
   healers, or do they also sabotage? How far do Foundry Houses go?

## Still open

- Origin of the giant insects. A known fact, or a mystery for a seed?

- What is really downtown, and why is it off-limits? Assumed that the
  official reason is contamination and the real reasons are layered.
  Those layers are plot and stay out of the player-safe bible.

- Can an AI corrupt the nervous-system link of a trooper or an
  implanted player?

- Akron: allied and friendly with Cleveland. Anything more? Other
  cities in play (Lorain, Sandusky, Youngstown)?

- Where is the electricity generated? Perry nuclear plant on the lake
  east of Cleveland is a candidate legend.

- Medicine: who treats the poor, and how reliable are the Moon
  broadcast medical tips?

- Daily life: housing, work shifts, schooling, what a debt looks like
  on paper, how rank is shown (badges, clothes).

- Inspections: who searches what you carry out of the ruins, and can
  you hide small valuables?

- Crime pyramid: tiers, territory, or corporate fronts? Names for
  the top.

- Do the Moon AIs ever act physically (visit, send drones)? Do any
  rogue AIs want something specific?

- Languages, naming style for people, slang, holidays.

## After the interview

1. Write `bible.md` for the world, player-safe, with no plot secrets.
   Follow the format in `docs/WORLDS.md` and Matt's Markdown rules in
   `CLAUDE.md` (72 columns, blank line after every paragraph and list
   item).

2. Write `world.json` (name and pitch, player-safe), `metaplot.md`
   and at least three seeds plus `seeds/teasers.md`. Matt co-writes
   the secret files, so do not show him a diff of them unless he
   asks. Matt is the author here, so the spoiler wall does not hide
   his own material from him, but it still applies to Brad.

3. Engine work this world needs (see `TODO.md`): SRD class reskins,
   the Engineer, Cleric and Warlock flavor, the debt and corruption
   ideas, and variable currencies. The script has no data for a
   non-fantasy setting yet. Check `tests/test_data_real.py` for what
   the data tests refuse.
