import random
words = ["combine","minimum","object","silk","economy","eaux","sentiment","major","popular","arrow"]
liswords = list(random.choice(words))
updater = []
for i in range(len(liswords)):
    updater.append("__")
x = [0,1,2,3,4,5,6]
print(updater)
for i in x:
    guess = input("Guess a letter")
    if(guess ==  "C"):
        for j in range(len(updater)):
            if(updater[j] == "__"):
                updater[j] = liswords[j]
                print("You cheater")
                x.remove(x[i+1])
                break
        if("__" not in updater):
            print("Fine you won cheater")
            print(updater)
            break
    if(guess in liswords):
        for i in range(len(updater)):
            if(guess == liswords[i]):
                updater[i] = guess
                x.append((x[-1]+1))
        if("__" not in updater):
            print("Great job you won")
            print(updater)
            break
    print(updater)
if("__" in updater):
    print("Aw man you lost")
