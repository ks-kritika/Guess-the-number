import random
import pyttsx3
number= random.randrange(1,50)
guess =int(input("Guess a number between 1 to 50: "))
while guess != number:
    if guess<number:
        print("You need to guess higher. Try again")
        guess = int(input("\nGuess a number between 1 to 50: "))
    else:
        print("You need to guess lower. Try again")
        guess = int(input("\nGuess a number between 1 to 50: "))
print("You guessed the number correctly. The number is ",number)
engine = pyttsx3.init()
engine.say("CONGRATULATIONS! YOU WON")
engine.runAndWait()
engine.stop()