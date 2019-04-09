"""A number-guessing game."""

# Put your code here

from random import randint

name = input("Howdy, what's your name? Type in your name: ")
count = 0

print(name + ", I'm thinking of a number between 1 and 100.")
print("Try to guess my number.")

random_int = randint(1, 100)

while True:
    try:
        guess = int(input("Your guess? "))

        if guess == random_int:
            print("Well done, " + name + "! You found my number in " + str(count) + " tries!")
            break
        elif guess < 1 or guess > 100:
            print("Please choose a number between 1 and 100!")
            # guess = int(input("Your guess? "))
        elif guess < random_int:
            print("Your guess is too low, try again.")
        else:
            print("Your guess is too high, try again.")
    except ValueError:
        print("Please enter a valid integer")
    count+=1
            
