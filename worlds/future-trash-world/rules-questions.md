# future-trash-world: questions about the game rules

A parking lot for questions about mechanics, so the world interview
can keep going. We go through this list later, in the mechanics stage.
Decisions already made are in `decisions.md`. Each item below names
the question number or section there when it has one.

Rules context: this world leaves the fifth-edition rules. Each
`world.json` will name its ruleset (`5e` or `skills`), so the engine
needs a second mode. The script owns every number. The model never
makes up a number and never states a relationship value or a risk
number to the player.

Mark an item done by moving it to "Answered" with a pointer to
`decisions.md`.

## Fleeing and unfinished threats (question 79, deferred)

- How does fleeing work? Proposed: a percentile flee check on
  Stealth, Survival or Tactics, adjusted by the situation and by
  gadgets. A clean success is a clean escape. A partial success is an
  escape at a cost (dropped gear, a light wound, being followed). A
  failure means the threat catches the party on its terms. Other
  options offered: fleeing always works at a cost in time and
  supplies, or fleeing is a DM ruling with no rule.

- Who rolls: the party leader, or each member?

- How does the script remember threats the party left behind? Proposed:
  a list the script owns, with where each threat is and how alert it
  is.

- Do left-behind threats change while the party is away (grow, move,
  call others), or stay as they were?

## Skill checks

- How does difficulty adjust the target on a percentile roll-under
  (question 49)? A flat modifier, a multiplier, or named bands?

- What does a gadget boost look like in numbers, and how large is it?

- Is there a critical success or failure (for example, doubles, or a
  roll of 01 or 00)? Is there a partial success band?

- Does a failed check cost anything beyond the failure (time, noise,
  gear wear)?

- Can two characters help on one check? How do group checks work?

## Character creation

- Does the school set a skill's starting value, or does the draw from
  the curve (question 48)? Matt's genius idea favors the draw.

- The curve's shape: mean about 35, right-skewed, most people never
  above 50. The script needs exact parameters or a table of dice.

- How does an occupation work on the 1 to 100 scale (question 43)? It
  gave "a few starting ranks and one or two perks, and its skills
  cost less to raise" on the old 0 to 10 scale. What are the new
  numbers?

- The school gain of +5 to +10, occasionally +0 or +15 (question 50):
  the exact odds.

- The scavenger and the believer get no school gain (positions 2 and
  3). Do they get something else from their upbringing?

## Advancement

- Gain per route: training, study and practice (question 50). Training
  is +5 to +10 with an occasional +0 or +15. The others are
  placeholders: study smaller, practice +1 per full set of marks,
  gains shrinking as a skill rises.

- Training cost by skill. Combat and stealth are cheaper, biological
  engineering and robotics dearer (question 47). How much?

- How are marks earned? Failures count (question 41). How many marks
  make a gain?

- Mission points: how many per mission, and what do they buy?

## Jobs and occupations

- Does a hire involve a roll after the skill minimums (question 44)?
  Proposed: d100 against Persuasion, set by openings and danger.

- Can a character change occupation (the career path)?

- What does a failed application cost?

## Debt

- School debt is a fixed amount by occupation training (question 47).
  What are the amounts, who holds it, and what does it cost per week
  or per month?

- What are the consequences of dropping out?

- Is there interest? Does debt grow if unpaid?

- What happens if the player ignores a debt for a long time?

- Work-off sentences: length, terms, who holds the debt (the arresting
  corporation or a prison operator), whether a prisoner can be bought
  out, whether escape is possible.

## Wounds, the hospital and death

- Wounds: light, serious and critical (question 51). How many of each
  can a character carry before defeat? What are the penalties on
  checks?

- How do wounds heal? Slow rest is free (Healing section). How long
  does each severity take?

- How does the Medicine skill treat a wound, and what does a failure
  cost?

- Hospital bill: sized by wound severity and how far the clinic's
  corporation had to go (question 53). What are the amounts?

- At what bill size does a work-off contract appear (question 53)?

- True death (question 52): the exact triggers. A warned, chosen
  lethal risk, or an unreachable character. How does the script
  decide, and how is the warning given?

- The returned state (question 55): how much does each skill drop,
  how does the personality shift, and how can a rogue AI hack the
  character?

## Relationships

- Table rows (questions 63 and 64): how far does each kind of event
  move a row? Gift, bribe, threat, a favor, a betrayal, a rescue.

- At what thresholds does a row unlock a request or a refusal?

- Does a gift back reduce the row the first gift raised (the leaders
  cancelling their obligation, question 62)? By how much?

- Can the player refuse a gift back to keep an elder obligated?

- How does a row decay with time, if at all?

- How do NPC-to-NPC rows change when the player is not there?

## Gadgets and technology

- The gadget list: four to six to start (question 71). Names, the
  skill each boosts, and the boost.

- How a gadget breaks: a failed check, a roll-under threshold, or a
  use count. How repair and upgrade work.

- What the cloaking gear fools: people and cameras, drones, AI
  sensors (question 70).

- Can a rogue AI hijack a remote drone (question 77)?

- Can an AI or a gadget make a trooper's implants fail? Very rare
  with the right gear (question 71). What does the check look like?

- Corruption: what a failed or very powerful hacking or swarm use
  risks (Rules mapping idea).

## Ruins and risk

- Risk tiers 1 to 5, a stated and a true tier (question 78). What
  numbers does each tier set for encounters, staffing and pay?

- Does risk rise the longer the party stays (alarms spread, the leak
  worsens)?

- How does a left-behind challenge get picked up again?

## Economy

- Many currencies with changing exchange rates. Proposed: one stable
  reference price, with each currency a modifier set by region.

- Pay from a permit is about a third of value, and about two thirds
  on the black market, less the middleman's cut and the risk
  (Treasure hunting). Exact numbers.

- Water cost by distance from the lake (assumed, not confirmed).

- Paying for services in stored electricity.

## Combat

- How combat rounds work under a roll-under percentile system, and
  initiative.

- Weapons and armor on the 1 to 100 scale: how a hit becomes a wound
  level.

- Security members who love to fight may skip the warning (question
  69, a working assumption). Is it an NPC quirk the script rolls?

## Engine and data

- A `ruleset` field in `world.json`, with `5e` and `skills`. What the
  engine does in each mode, and what shared code stays.

- The SRD class, spell, monster and item data and its tests do not fit
  the skill system. What data replaces them, and what
  `tests/test_data_real.py` must allow or refuse for this world?

- Occupations as data: skills, perks, school debt, cost to raise.

- Party format: `party.json` format 2 is for fifth edition. What does
  a skills-mode character sheet look like?

- Rule for `SKILL.md`: never state a relationship value or a risk
  number to the player (question 63).

## Orders and reports

- How does the script decide that an NPC thinks they will not be
  caught (the security members who act on their own, question 79)?
  Proposed: whether anyone with a relationship row against them is
  watching, plus a roll.

- What does a good report from the supervisor give a security member
  (pay, rank, less debt)? Does the player's report from the
  supervisor work the same way?

- Can a player refuse an order from a supervisor, and what does it
  cost (the supervisor's row, a bad report)?

## Detention and investigators

- How does the planted-item scene work as checks: a check to notice
  the item (Streetwise or Stealth, decided in question 79), a check
  to resist the supervisor, a Persuasion roll against the
  investigator?

- How large is the fine and the added debt, and what picks among the
  outcomes (a bigger debt, a harder mission, a labor camp)?

- Can the player find evidence that clears them (a witness, a record
  of the item being planted)?

- How big is the bonus on a smuggling check when the supervisor
  helps (the supervisor has done it for years), and how does it work
  when he smuggles alone?

- How does a back-down work: a check, or the NPC scavenger's row
  about the supervisor and about the player? What does the threat
  cost the supervisor if the NPC refuses?

- What roll or margin counts as the exceptionally good roll that
  makes the investigator take a bribe (question 81)? What does a
  failed bribe cost beyond the row against the player?

## NPC goals

- NPCs with competing goals (the supervisor has four, see
  `decisions.md`). How does the script hold a goal list, and what
  decides which goal an NPC acts on in a scene? Proposed: each goal
  has a weight, and the DM or a roll picks which one leads.

## Creatures and drones

- How are the insect types and the security drones written as data
  for a skills-mode world? The fifth-edition monster data does not
  fit. What does a creature entry hold (skill values, wound
  thresholds, attacks, special effects)?

- How do two hazards fight each other off-screen (the drones and the
  insects), and how does the script track who is winning?

- Insect numbers: the roach swarm (how a swarm of weak attackers
  becomes a threat), the beetle (size classes from dog to car, how
  much its armor resists), and acid spit as a ranged attack that
  damages gear. Wound levels for each (question 93).

- Drone hacking (question 95): the size of the penalty for hacking
  remotely and the bonus for hacking up close with attached
  equipment. What the danger of close hacking is (a counterattack,
  corruption of the hacker, an alarm). Flying drones against ground
  units: do they get different difficulties?

## Answered

(Nothing yet.)
