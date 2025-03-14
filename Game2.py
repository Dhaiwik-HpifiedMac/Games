import random
starter = input("Would you like to play the game?  ")
balance = 100
while starter == "yes":
    wager = int(input("How much money do you want to wager?  "))
    if(wager>balance):
        print("You can not bet more than you have!!! ")
        exit()
    side = input("Do you bet on heads or tails?  ")
    if(side == "heads"):
        side = 1
    elif(side == "tails"):
        side = 2
    else:
        print("Chose head or tails!")
    coin = random.randint(1,2)
    if(coin == side):
        balance = balance + wager
    else:
        balance = balance - wager
    if(balance == 0):
        exit()
    print(balance)
    starter = input("Would you like to play another game?  ")

print(balance)
