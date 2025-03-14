import random
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
sum = dice1 + dice2
guess = input("What is youre guess? 7 up, 7 down or 7  ")
if((guess == "7 up" and sum > 7) or (guess == "7 down" and sum < 7) or (guess == "7" and sum == 7)):
    print("Great guess! You win! The sum is ",sum,".",sep = "")
else:
    print("Oops! You lost. Better luck next time. The sum was ",sum,".",sep = "")
