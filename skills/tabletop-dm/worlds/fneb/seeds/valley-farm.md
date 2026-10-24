# The valley farm

## Tone

Hard times on good land, with dark comedy. Turnips, market days, an
auctioneer who never draws breath and a constable older than his war
hammer, all the way up to the day the rent doubles and the soldiers
come. Then it turns grim: trapped children, a flogging, burning woods,
and something wrong with the pigs.

## Start place

The market scales in Broadscale, the Fneb valley's market town, on the
first market day after the spring planting. Granny Moss's farm lies an
hour's walk up the valley, at the edge of the elf woods.

## The opening scene

The hero is in the line at the great scales, with a cart of last year's
stored barley for Granny Moss. Ask the player in one line why they are
with her: a foster child, a hired hand, a neighbour, a grandchild. The
auctioneer rattles, buyers bid by the bushel, and old Constable Moe
leans on his war hammer and tells everyone he once killed a troll with
it.

Then the bidding stops. A young priest climbs onto the auctioneer's
platform: Brother Severin, the valley's new priest. Behind him, twenty
soldiers in orange march in under a black scythe banner. Kindly, he
announces that his predecessor was too tolerant. From today, the
church's rent is doubled. Any dealing with the elves will be punished.
The dead will be buried, not burned like heathens. The Scythe Company is
here to help.

Then he looks out over the crowd, and his eyes rest on the hero.

Start the deadline as a secret counter: `track C --name "conjunction"
--set 48 --secret`.

## What is really going on here

Severin is squeezing the valley for two reasons. He needs money to pay
the Scythe Company and the diggers under the mountain. And he needs the
elves gone, because they can feel the seal failing (see the metaplot).
The rent and the fear are also food for the cabal. Every coin squeezed
out of a hungry farm feeds them a little. Captain Rusk does not know
that. He only knows that clearing the elf woods means new church fields
and a share of the profits for him.

Granny Moss is half elf. Every spring she leaves jugs of mead in wooden
boxes in her fields, marked with ribbons on sticks. The wood elves take
the mead, and on bright moon nights their elders dance through the
fields and bless them. Her farm is the best in the valley for a reason.

Later, as the seal under the mountain fails, black spores drift down the
valley.

## The local villain

**Captain Rusk** of the Scythe Company. He is polite, tidy and bored,
and he has done this in other valleys. He is paid in coin now and in a
share of the cleared woods later. He will burn anything, but he dislikes
waste. His next three moves, if nobody stops him:

1. He baits a trap for the elves with stolen mead, and catches two elf
   children.

2. He flogs Constable Moe for helping them escape.

3. He burns the elf woods, a strip at a time.

Behind him stands **Brother Severin,** who means every gentle word, and
who visits the valley between Haldmouth and the mountain.

## Other people

- **Granny Moss,** sharp, small and very old, who knows the gift ritual
  and will teach it. She knows more about the elves than she lets on.

- **Constable Moe "Scarback",** ancient war hero, who walks with his war
  hammer and has finally found something worth using it on.

- **Assistant Constable Durney,** an idiot looking for a chance to prove
  himself. In this door, he gets one: he helps rescue the elf children.

- **Master Pellow,** the tax collector, who has always taken a sixth and
  now takes double. He is ashamed, and he takes it anyway.

- **The auctioneer,** fast talking and fair, who knows every price in
  the valley.

- **Old Ash,** an elder of the wood elves. If the children come home,
  Old Ash owes the hero a debt.

- **Gorse,** a night druid, who appears the day after the woods start to
  burn. He lost his own grove to Father Hallam thirty years ago, and he
  will bring the ashmouth and the rats down on Broadscale unless someone
  gives him a reason not to.

## Companion candidates

- **Tam Moss,** a fighter. Granny's grandson, big, gentle and stubborn,
  who can lift a cart. Secret: he has been slipping into the elf woods
  to meet an elf girl, and the soldiers have seen him.

- **Ottilie Pellow,** a wizard. The tax collector's daughter and clerk,
  clever and furious with her father. Secret: she has been quietly
  cutting the farmers' tallies for months, and the church's books do not
  add up.

- **Old Bryn,** a cleric of the Green Mother, the hedge-priest who says
  the words over the first furrow. Secret: in the Burnings, he hid two
  elf children in his root cellar, and he still has the cellar.

## If the hero does nothing

The conjunction counter shows the days left.

- **48:** Market day. The rent is doubled.

- **42:** The soldiers trap two elf children with stolen mead.

- **36:** More soldiers arrive. Farms that cannot pay are seized.

- **30:** Constable Moe is flogged for "druid sympathies". He dies, and
  he is buried.

- **26:** Ghouls dig up Moe's grave. The soldiers start burning the elf
  woods.

- **24:** Gorse arrives. Rats swarm Broadscale, and people start
  coughing grey ash.

- **22:** Black spores fall. The fields wither, and the pigs eat the
  blighted fodder.

- **18:** The sows give birth.

## Fights

- **The elf trap:** two elf children are tied to a post by a campfire,
  watched by 3 guards (Scythe soldiers) and 2 wolves (their war dogs).
  Durney turns up to help.

- **The burning woods:** a veteran (Rusk's sergeant) and 4 guards with
  torches. The fire spreads each round, and anyone who ends a turn in it
  takes 1d6 fire damage.

- **Moe's grave:** 2 ghouls, at second watch, the night after the
  burial.

- **Gorse's rats:** 6 giant rats, bolder than any rat should be.

- **The piglets.** After the spores fall, most pigs sicken and die. One
  sow delivers a litter of dead, twisted piglets. A few live. In the
  morning the piglets are gone, and the sow has been eaten. Two nights
  later they come back. Custom, for `encounter start --custom`, as a
  single line:

```json
{
  "name": "Blighted Piglet",
  "count": 4,
  "ac": 11,
  "hp": 9,
  "abilities": {"dex": 13},
  "attacks": [
    {"name": "bite", "attack_bonus": 3, "damage_expr": "1d6+1",
     "damage_type": "piercing"}
  ],
  "challenge_rating": 0.25
}
```

**Farming as downtime.** A farm has 3 plots. Each season, the player
chooses a crop for each plot, and at harvest the DM rolls each plot's
value in gold with a free roll, then pays it with `gold --add`:

| Crop | Harvest roll, in gp |
|---|---|
| Black turnips ("ogre toes") | 1d4+2, whatever the weather |
| Brown barley | 2d4 |
| Elf grain ("silver grass") | 4d6 if the elves blessed it, 1d4 if not |

A Nature check (DC 12) at planting adds +1 to every plot's roll. At the
scales, a Persuasion check (DC 13) adds `1d4` gp to the whole sale. Rent
is paid with `gold --spend`: 1 gp a plot before Severin, and 2 gp a plot
after him. The elves bless a field only if the gift is left properly,
and only while they are still in the woods.

## Local secrets

- Captain Rusk, Master Pellow and Severin's two acolytes have all
  dreamed of a smiling stranger who thanks them for every coin they take
  (R3).

- The black spores drift down from the mountain, from the direction of
  the crater above the valley (R1).

- The dead Moe rises because he was buried, not burned (R1).

- When the soldiers come to seize a farm and the whole lane stands in
  the road together, unarmed, the soldiers hesitate, and the noon light
  seems brighter. Granny Moss calls it "the old way" (R5).

- Granny Moss has a jug of mead older than anyone living, saved, she
  says, "for the day we all say no".

## The way in to the larger mystery

- **R1:** the spores, the rising dead and the burial ban show that the
  dead walk because of what is buried, and that the thing below is
  waking.

- **R3:** the same dream of the smiling stranger, wherever money is
  squeezed, shows that something feeds on it.

- **R5:** a rent strike, if the hero can organise one, is the Refusal at
  village size, and it works.

## Ways it can end

- **The valley refuses.** Every farm keeps back its rent on the same
  day. The soldiers cannot flog everyone, and Rusk will not fight a
  whole valley for a priest's wages. The Scythe Company leaves, and
  Severin has lost his valley.

- **The elves are saved,** but the woods burn, and Gorse is loose and
  grieving.

- **The hero talks Gorse down,** or turns his rats on the soldiers
  instead of the town.

- **The farm is lost.** Granny Moss goes to the elves, and the hero goes
  on the road.

- **The piglets are only the beginning.** The spores keep falling until
  someone deals with what is under the mountain.
