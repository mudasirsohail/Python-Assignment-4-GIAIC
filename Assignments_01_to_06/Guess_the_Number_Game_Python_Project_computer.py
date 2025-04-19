import random

def number_guessing_game(max_number):
    secret_number = random.randint(1, max_number)
    user_guess = 0
    attempts = 0

    print(f"Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and {max_number}. Can you guess it?\n")

    while user_guess != secret_number:
        try:
            user_guess = int(input(" Enter your guess: "))
            attempts += 1

            if user_guess < 1 or user_guess > max_number:
                print(f"Please enter a number within the range 1 to {max_number}.")
            elif user_guess > secret_number:
                print("Too high! Try again.")
            elif user_guess < secret_number:
                print("Too low! Try again.")
        except ValueError:
            print("That's not a valid number. Please try again.")

    print(f"\n Congrats! You guessed the number {secret_number} correctly in {attempts} attempts.")

# Start the game with numbers between 1 and 10
number_guessing_game(10)
