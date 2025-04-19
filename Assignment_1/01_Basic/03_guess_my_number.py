import random

def main():
    # Generate a random secret number between 1 and 99
    secret_number = random.randint(1, 99)
    
    print("I am thinking of a number between 1 and 99...")

    # Initial user guess
    guess = int(input("Enter a guess: "))
    
    # Continue loop until the correct number is guessed
    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        
        print()  # Add spacing for clarity
        guess = int(input("Enter a new guess: "))
    
    print("Congrats! The number was: " + str(secret_number))

# Required to run main function
if __name__ == '__main__':
    main()
