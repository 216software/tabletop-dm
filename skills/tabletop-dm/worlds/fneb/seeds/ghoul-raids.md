# The ghoul raids

## Tone

Folk horror. A valley town that has always burned its dead is ordered to
bury them, and now something comes for the graves every full moon. Grim
and close, with relief from an ancient constable, his hopeless deputy
and the strange, polite wood elves.

## Start place

Broadscale, the market town of the Fneb valley, under the mountains. It
is the night of the full moon, at second watch, in the new graveyard
behind the church.

## The opening scene

The hero is in the graveyard at second watch. Why they are there is the
player's to say: keeping vigil for someone buried there, or paid by the
constable to watch.

Fog comes down off the mountain. A cart creaks out of it, dragged by
four shambling figures, with a lean grey shape walking beside it and
giving orders. They go straight to the newest grave and start to dig
with their hands.

Start the deadline as a secret counter: `track C --name "conjunction"
--set 40 --secret`.

## What is really going on here

This spring, the new valley priest, Brother Severin, banned the burning
of the dead as a druid rite. Broadscale now buries its dead, and every
full moon the dead come for them.

The raiders are Deacon Marl's work. Marl is Severin's man in the valley.
In a cave mouth high above the farms, he has found a way down to the Eye
from this side of the mountain: the caverns the paladins never sealed,
because they never knew of them. Fresh corpses become zombies near the
Eye, and the zombies dig. Where there are no graves, the ghouls take
farmers.

The wood elves of the valley forest have kept two tools of the Young
Ones since the Refusal: a set of three tuning forks of sun-crystal, and
a sealed jar of drifting lights. Struck together in the right places,
the forks bring a cavern down. The elves have watched the raids and are
afraid. They will give the tools only to someone who comes to them
openly.

## The local villain

**Deacon Marl,** a former gravedigger whom Severin raised to deacon, who
calls the Eye "the Watcher" and believes it answers prayers. He has been
promised that nobody he loves will ever die again. He would rather
recruit the hero than kill them. His next three moves, if nobody stops
him:

1. The raids go from monthly to weekly, and the ghouls start taking
   living farmers for the dig.

2. He has the old constable flogged for "druid sympathies", and the old
   man dies of it. Marl has him buried.

3. His diggers break through to the Eye's chamber and start to free the
   gem.

## Other people

- **Constable Moe "Scarback",** positively ancient, a war hero and
  monster-slayer who uses his war hammer as a cane. He knows exactly
  what a ghast is, and nobody listens to him.

- **Assistant Constable Durney,** eager, brave and an idiot, desperate
  to prove himself.

- **Refugee farmers** from the fringe farms, with stories of grey things
  in the barley.

- **A scout from the ranger post** on the mountain road, the only one
  left after the post was found wrecked. She saw ghouls carrying bodies
  up a dry streambed.

- **Old Ash,** an elder of the wood elves, soft-spoken and formal, who
  meets the hero at the forest's edge only after a gift of mead is left
  out on a moonlit night. Old Ash gives the forks and the jar, and asks
  for them back.

- **The old woman at the edge of town,** said to be part elf, who knows
  how to leave the gift properly.

## Companion candidates

- **Durney,** a fighter. Brave, loud and keen, and he never stops
  trying. Secret: he took Deacon Marl's coin to report anyone dealing
  with the elves, and he is starting to feel sick about it.

- **Thistle,** a rogue. A young wood elf scout sent by Old Ash to watch
  the hero and the forks. Polite, curious about everything human, and
  silent on her feet. Secret: if the humans fail or run, she is to take
  the forks home, and she will.

- **Sister Mercy,** a cleric. The town's old priest, before Severin sent
  his deacon. Gentle and tired. Secret: she still burns the dead in
  secret, at night, when the families ask her, and Marl suspects.

## If the hero does nothing

The conjunction counter shows the days left.

- **40:** The full moon raid. Two graves are emptied.

- **33:** The first raid on a living farm. A family is taken.

- **30:** Constable Moe is flogged. He dies, and he is buried.

- **26:** Moe's grave is dug up. Ghouls raid every night now.

- **20:** The diggers reach the Eye. Black spores start to drift down
  the valley.

## Fights

- **The graveyard raid:** a ghast leader, 2 ghouls and 4 zombies
  dragging a cart. The ghast flees if it is hurt badly, and leads the
  hero home.

- **The bait.** Old Ash's potion, poured on straw scarecrows laid on
  tables in the graveyard, makes them look and smell like fresh corpses
  until dawn. The next raid takes them, and the dead are easy to follow:
  the tracks go up a dry streambed to a hidden cave mouth. A Survival
  check (DC 10) is enough, at night or not.

- **Room 1, the outer cave:** walls of puffball mushrooms that burst
  into spores if disturbed (Constitution save DC 12, or poisoned for an
  hour). Bones and rotting meat under the stalagmites, and flies. An
  Intelligence check (DC 13) predicts that something hides among the
  stalagmites: a roper. The ghouls throw it a corpse to get past. A
  locked iron door at the back (thieves' tools, DC 14). Small stone eyes
  in the walls watch everything, and show up to detect magic.

- **Room 2, the carved stairs:** steep stairs down, walls carved with
  glyphs. Anyone who reads them makes a Wisdom save (DC 13), or sees
  armies of dead slaves and is frightened, babbling and desperate to
  flee to the surface, until they pass the save at the end of a turn.
  After a few hundred steps, the stairs split. One way leads to a pen
  where 6 prisoners are held, guarded by 2 ghouls. The other leads down
  to a rune-covered door, magically barred and trapped (Arcana DC 14 to
  undo it, or 2d6 fire damage to whoever opens it by force).

- **Room 3, the great cavern:** very high, wet, with a pond across half
  the floor, insect holes in the walls, and a huge rock pile. 4 zombies
  chip at the walls without stopping.

- **Room 4, the Eye:** the rock is cut back to expose a gem, and a giant
  eye floats inside it. Anyone who comes within 30 feet of the gem makes
  a Wisdom save (DC 13) each turn, or is charmed and walks toward it. A
  creature that passes is immune for the rest of the fight. Deacon Marl
  (a priest) fights here. He kicks over braziers to make walls of fire,
  raises one zombie a round from the corpses on the floor, and calls on
  the hero to kneel and be saved. When he is hurt, he slips away through
  smoke.

**The forks.** Smashing the jar lets out the lights, which drift and
cluster at three points around the cavern. A fork set at each point and
struck by a different hand at the same moment rings with a note that
brings the cavern down within 3 rounds. Striking a fork is an action,
and one hand cannot strike two. The ringing does not kill the Eye. It
buries it deep, and nobody can reach it from the valley side again.
Someone could choose to stay and hold the last fork steady to make sure,
but nobody has to.

Custom stat block for `encounter start --custom`, as a single line:

```json
{
  "name": "Young Roper",
  "count": 1,
  "ac": 15,
  "hp": 45,
  "abilities": {"dex": 8},
  "attacks": [
    {"name": "tendril", "attack_bonus": 5, "damage_expr": "1d6+3",
     "damage_type": "bludgeoning"},
    {"name": "bite", "attack_bonus": 5, "damage_expr": "2d6+3",
     "damage_type": "piercing"}
  ],
  "challenge_rating": 2
}
```

## Local secrets

- The raids started the month the burning ban came in (R1).

- The cave mouth sits on the rim of an old crater, half grown over with
  forest. The town's oldest map shows other craters where the dead
  "walk" in old stories (R1).

- The forks and the jar of lights are worked with the same angels as the
  lantern paintings and the oasis carvings (R2).

- The forks will not ring for one hand alone. The elves say: "Only a
  crowd can sing it" (R5).

- Marl carries a letter from Severin that praises his "patient work
  beneath the mountain" and speaks of a coming conjunction.

## The way in to the larger mystery

- **R1:** the burning ban, the raids and the crater map show that the
  dead walk because of what is buried.

- **R2:** the forks and the lights are Young One tools for keeping the
  Old Ones cut off.

- **R5:** the forks ring only when several people strike them together.

## Ways it can end

- **The cavern comes down.** The raids stop, the prisoners are home, and
  Broadscale burns its dead again, whatever the church says. Severin has
  lost his back door, and he knows who closed it.

- **The forks fail,** because there are not enough hands. The hero
  escapes with the prisoners, and the dig goes on.

- **The hero kneels.** Marl's offer is real: the Eye can make the hero's
  dead walk and talk again. It is a door to a very dark campaign.

- **Thistle takes the forks home** after a retreat, and the elves
  remember who failed them.

- **Moe dies** before the end, and Durney becomes the constable, whether
  anyone likes it or not.
