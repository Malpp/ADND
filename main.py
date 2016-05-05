from random import randint
import sqlite3
import os
import sys

con = sqlite3.connect('db.sqlite3')

level = 1

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

def roll4():

    return randint(1,4)

def roll8():

    return randint(1,8)

def roll12():

    return randint(1,12)

def roll20():

    return randint(1,20)

def roll100():

    return randint(1,100)

def quitDun():

    sys.exit("Thanks for playing")

def rollStairs():

    global level

    with con:

        c = con.cursor()

        roll = str(roll20())
        
        c.execute('SELECT * FROM stairs WHERE Roll=?', (roll,))

        s = c.fetchone()

    s = list(s)

    # 0 = ID
    # 1 = Roll
    # 2 = Size

    if s[2] > 0:

        d = "up"

    else:

        d = "down"

    print "You found stairs going {}".format(d)

    des = raw_input("What do you do? [go/con]: ")

    if des == "go" or des == "g" or des == "y" or des == "GO" or des == "G" or des == "Y":

        print "You go {} {} level(s)".format(d, abs(s[2]))

        level = level - s[2]

        if level < 1:

            print "You have left the dungeon"

            quitDun()

            

def rollTreasure(M=False):

    global level

    def rollT(roll):

        with con:

            c = con.cursor()
            
            c.execute('SELECT * FROM treasure WHERE Roll=?', (roll,))

            t = c.fetchone()

        t = list(t)

        # 0 = ID
        # 1 = Roll
        # 2 = Contents

        content = t[2]
        
        if content == "Copper":

            print "You found {} copper".format(1000*level)

        if content == "Silver":

            print "You found {} silver".format(1000*level)

        if content == "Electrum":

            print "You found {} electrum".format(750*level)

        if content == "Gold":

            print "You found {} gold".format(250*level)

        if content == "Platinum":

            print "You found {} platinum".format(100*level)

        if content == "Gems":

            print "You found {} gem(s)".format(roll4()*level)

        if content == "Jewelry":

            print "You found {} piece(s) of jewelry".format(level)

        if content == "Magic":

            print "You found a magic item!"

    if M:

        rollT(clamp(roll100()+10,1,100))
        rollT(clamp(roll100()+10,1,100))

    else:

        rollT(roll100())


def rollMonster():

    with con:

        c = con.cursor()

        roll = str(roll100())
        
        c.execute('SELECT * FROM monsters WHERE Roll=?', (roll,))

        monster = c.fetchone()

    monster = list(monster)

    # 0 = ID
    # 1 = Roll
    # 2 = Name
    # 3 = NumberOf
    # 4 = HP
    # 5 = Damage
    # 6 = AC
    # 7 = Size
    # 8 = Check
    # 9 = Page

    print "=====\t\t"+monster[2]+"\t\t====="

    if "-" in monster[3]:

        nOf = randint(int(monster[3].split('-')[0]),int(monster[3].split('-')[1]))

    else:

        nOf = int(monster[3])

    print "Number of: "+str(nOf)

    print "HD: "+monster[4]

    HP = monster[4]

    HPS = []

    for i in range(nOf):

        if HP.startswith("="):

            HPS.append(int(HP.split('=')[1]))

        elif "+" in HP or "-" in HP:

            if "+" in HP:

                HPS.append(roll8()*int(HP.split("+")[0])+int(HP.split("+")[1]))

            elif "-" in HP:

                HPS.append(clamp(roll8()*int(HP.split("-")[0]) - int(HP.split("-")[1]), 1, 8*int(HP.split("-")[0]) - int(HP.split("-")[1]) ))

        elif "~" in HP:

			HPS.append(randint(HP.split("~")[0],HP.split("~")[1]))

		else:

            HPS.append(roll8()*int(HP))

    print "HP: "+str(HPS)

    print "Damage: "+monster[5]

    print "AC: "+str(monster[6])

    print "Size: "+monster[7]

    if monster[8] == 1:

        print "Check monster manuel at page {}".format(monster[9])

    else:

        print "Monster manuel page {}".format(monster[9])


def rollRoom():

    with con:

        c = con.cursor()

        roll = str(roll20())
        
        c.execute('SELECT * FROM room WHERE Roll=?', (roll,))

        room = c.fetchone()

    room = list(room)

    # 0 = ID
    # 1 = Roll
    # 2 = Contents

    content = room[2]

    if content == "Empty":

        print "Room is empty!"

    elif content == "Monster":

        print "THERE IS A MONSTER! ROLL INITIATIVE!\n"

        rollMonster()

        raw_input("\nPress enter to continue")

    elif content == "Monster/Treasure":

        print "THERE IS A MONSTER! ROLL INITIATIVE!\n"

        rollMonster()

        raw_input("\nPress enter to continue\n")

        rollTreasure(True)

        raw_input("\nPress enter to continue")

    elif content == "Stairs":

        print "You stumble upon stairs\n"

        rollStairs()

    elif content == "Trap":

        print "ITS A TARP\n"

        print "Roll a trap yourself"

        raw_input("\nPress enter to continue")

    elif content == "Treasure":

        print "BOOTY\n"

        rollTreasure()

        raw_input("\nPress enter to continue")

while True:

    rollRoom()

    
