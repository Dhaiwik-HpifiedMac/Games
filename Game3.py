import random
import time
##position
p1 = input("What is Player 1 name?  ")
pos = 0
rolls = 0
p2 = input("What is Player 2 name?  ")
poss = 0
rollss = 0
def player1():
    global p1
    global pos
    global rolls
    print("Your turn",p1)
    if not(pos>=100):
        rolls = rolls + 1
        die = random.randint(1,6)
        pos = pos + die
        if (pos>100):
            pos = pos-die
            print("Rolling dice...")
            time.sleep(2)
            print("You tried to move",die,"steps")
            print("You're now at",pos)
        else:
            print("Rolling dice...")
            time.sleep(2)
            print("You move",die,"steps")
            print("You're now at",pos)
        if(pos == (44 or 56 or 77 or 82 or 91)):
            print("Oh no! The snake bit you")
            pos = pos-20
            print("You're now at",pos)
        if(pos == (8 or 19 or 37 or 59 or 65)):
            print("Wow! You climbed the ladder")
            pos = pos+30
            print("You're now at",pos)
        print(rolls)
    if(poss==100):
        print(p1,"wins")
        exit()
    
def player2():
    global p2
    global poss
    global rollss
    print("Your turn",p2)
    if not(poss>=100):
        rollss = rollss + 1
        die = random.randint(1,6)
        poss = poss + die
        if (poss>100):
            poss = poss-die
            print("Rolling dice...")
            time.sleep(2)
            print("You tried to move",die,"steps")
            print("You're now at",poss)
        else:
            print("Rolling dice...")
            time.sleep(2)
            print("You move",die,"steps")
            print("You're now at",poss)
        if(pos == (44 or 56 or 77 or 82 or 91)):
            print("Oh no! The snake bit you")
            poss = poss-20
            print("You're now at",pos)
        if(poss == (8 or 19 or 37 or 59 or 65)):
            print("Wow! You climbed the ladder")
            poss = poss+30
            print("You're now at",poss)
    if(poss==100):
        print(p2,"wins")
        exit()
        

while(poss<100 and pos<100):
    player1()
    player2()

