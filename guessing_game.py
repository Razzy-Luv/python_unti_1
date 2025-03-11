#I am going for: "Exceeds Expectations"
#Guessing Game
import random

def start_game(): #Start the game
    print("Welcome to Amanda's Guessing Game!!!")
    high_score = None

    while True: #The random number
        print("I am thinking of a number between 1 and 100...")
        print("Can you guess my number?")
        random_number = random.randint(1, 100)
        attempts = 0

        while True: #The players guess
            try:
                player_number = int(input("Guess a number: "))
                if player_number < 1 or player_number > 100:
                    print("Woah! Easy there cowboy, remember it's a number between 1 and 100.")
                    continue

                attempts += 1

                if player_number > random_number:
                    print("It's lower. Try again!")
                elif player_number < random_number:
                    print("It's higher. Try again!")
                else:
                    print(f"You got it!!! The number was {random_number}!")
                    print(f"It took you {attempts} attempts.")

                    if high_score is None or attempts < high_score:
                        high_score = attempts
                        print(f"New high score! Your best game took {high_score} attempts!")
                    break

                if attempts == 10:
                    print("Wow, double digits already? You're really struggling! 😆")
                elif attempts == 20:
                    print("20 guesses?! Maybe this game isn’t for you... 😂")

            except ValueError:
                print("Oops! Please enter a valid number.")

        play_again = input("Do you want to play again? (yes/no): ").lower() #Do you want to play again?
        if play_again != "yes":
            print("Thank you for playing! Goodbye!")
            break

start_game()