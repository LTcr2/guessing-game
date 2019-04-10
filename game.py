"""A number-guessing game."""

# Put your code here

from random import randint

name = input("Howdy, what's your name? Type in your name: ")
count = 1
max_guesses = 5

print(name + ", I'm thinking of a number between 1 and 100.")
print("Try to guess my number.")

random_int = randint(1, 100)
print(random_int)

number = []

while True:
    try:
        guess = int(input("Your guess? "))
        if max_guesses == count:
            print("Too many tries!")
            # break
            # play_again = input("Would you like to play again? Enter Y or N. ")

            # if play_again == "Y":
            #     random_int = randint(1, 100)
            #     print(random_int)
            #     continue
            # else:
            #     min_number = min(number)
            #     print("Nice! Your lowest number of guesses was " + str(min_number))
            #     break

        if guess == random_int:
            # count+=1
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


