#Guessing Game--------
#import random
from random import randint

for x in range(1,5):
    guessNumber = int(input("Enter your guess_number between 1 to 5 : "))
    #randomNumber = random.random() * 100
    randomNumber = randint(1,5)
    if guessNumber == randomNumber:
        print("You have won")
    else:
        print("You have lost")
        print("Random number was : ",randomNumber)


#Guessing Game--------
#import random
from random import randint
for x in range(1,10):
    guessNumber = int(input("Enter your Guess Number 1 to 10 : "))
    #randomNumber = random.randint() * 100
    randomNumber =randint(1,10)
    if guessNumber == randomNumber:
        print("You have won ")
    else:
        print("You have lost")
        print("Random Number was : ",randomNumber)
        print("\n")


