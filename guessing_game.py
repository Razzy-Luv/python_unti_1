# Import the random module.
import random

# Create the start_game function.
def start_game():
    print("Welcome to Amanda's Guessing Game!!!")
    print("I am thinking of a number between 1 and 100...")
    print("Can you guess my number?")
    random_number = random.randint(1, 100)

    attempts = 0
 
    while True:
        try:
            player_number = int(input("Guess a number:  "))
            attempts += 1

            if player_number > random_number:
                print("It's lower. Try again!")
            elif player_number < random_number:
                print("It's higher. Try again!")
            else:
                print(f"You got it!!!  The number was {random_number}!")
                print(f"It took you {attempts} attempts.")
                print("That's the end... goodbye!")
                break
        except ValueError:
            print("Oops!  Please enter a valid number.")
        if attempts == 10:
            print("Wow, double digits already? You're really struggling! 😆")

        if attempts == 20:
            print("20 guesses?! Maybe this game isn't for you... 😂")

start_game()

