# ADND Random roller

How these randoms are rolled is you continually enter a room. It uses the randoms table to determine what's inside the room.

currently, the DB only contains level 1 of randoms.

#Plans:

1. Make it roll magic items/gems
2. Add more levels to the DB
3. Add some type of GUI with a loot aquired table

#How to add to the DB:

Get a DB editor for SQLITE like this one (http://sqlitebrowser.org/)

Monsters rows:

ID: auto increment, just like it do its thing
Roll: The number of the roll you need to get (In the future I plan to merge all the rolls together like 1-3, but for now just copy paste)
Name: Name of the monster
NumberOf: Number of monsters, use a single int for a set amount (like 1) or a range to roll for an amount (like 1-4)
HP: A single int (like 2) means it will roll 2 hit die, an int with a + with it will roll the hit die and add to it (same for the subtract), a range of int with a tilda (like 1~4) will roll 1 to 4 hp, an int with a = before it (=1) will set the hp to that number
Damage: Array with each damage as string ['1-4'] for a single attack ranging from 1-4 and ['1-2','1-2','1-3'] for 3 attack with different damages
AC: int with the AC
Size: String of the size
Check: 1 or 0, tell the player if he needs to check the Monster manuel or not
Page: page of the monster in the monster manuel
Level: level at which the monster will appear
