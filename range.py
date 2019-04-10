"""A number-guessing game."""

# Put your code here

from random import randint

name = input("Howdy, what's your name? Type in your name: ")
count = 1
max_guesses = 5


def user_range():

    lower_bound = int(input("Please enter a lower bound number: "))
    higher_bound = int(input("Please enter a highrer bound number: "))
    random_int = randint(lower_bound, higher_bound)

    return random_int


print("Try to guess my number.")


print(random_int)

number = []

while True:
    try:
        guess = int(input("Your guess? "))

        if guess == random_int or max_guesses == count:
            if max_guesses == count:
                print("Too many tries!")
            else:
                print("Well done, " + name + "! You found my number in " + str(count) + " tries!")
            
            number.append(count)
            count = 1
            play_again = input("Would you like to play again? Enter Y or N. ")

            if play_again == "Y":
                random_int = randint(1, 100)
                print(random_int)
                continue
            else:
                min_number = min(number)
                print("Nice! Your lowest number of guesses was " + str(min_number))
                break
        elif guess < 1 or guess > 100:
            print("Please choose a number between 1 and 100!")
        elif guess < random_int:
            print("Your guess is too low, try again.")
        else:
            print("Your guess is too high, try again.")
    except ValueError:
        print("Please enter a valid integer")
    count+=1


