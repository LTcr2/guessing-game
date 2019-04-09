"""A number-guessing game."""

# Put your code here

from random import randint
name = input("Howdy, what's your name? Type in your name: ")

print(name + ", I'm thinking of a number between 1 and 100.")
print("Try to guess my number.")

random_int = randint(1, 100)
# print(random_int)
guess = int(input("Your guess? "))
count = 0

while guess <= 100 and guess >= 0:
    count+=1
    if guess == random_int:
        print("Well done, " + name + "! You found my number in " + str(count) + " tries!")
        break
    elif guess < random_int:
        print("Your guess is too low, try again.")
        guess = int(input("Your guess? "))
    else:
        print("Your guess is too high, try again.")
        guess = int(input("Your guess? "))