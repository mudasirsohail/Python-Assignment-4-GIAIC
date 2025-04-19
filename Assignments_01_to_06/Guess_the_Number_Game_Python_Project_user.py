import random

def computer_guess(max_number):
    low = 1
    high = max_number
    feedback = ''
    
    print(f"\nThink of a number between 1 and {max_number}.")
    print("The computer will try to guess it!\n")
    print("Give feedback:")
    print("   - 'L' if the guess is too Low")
    print("   - 'H' if the guess is too High")
    print("   - 'C' if the guess is Correct\n")

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # when low == high

        feedback = input(f"Is {guess} too Low (L), too High (H), or Correct (C)? ").lower()

        if feedback == 'l':
            low = guess + 1
        elif feedback == 'h':
            high = guess - 1
        elif feedback != 'c':
            print("Invalid input. Please enter 'L', 'H', or 'C'.")

    print(f"\nYay! The computer guessed your number {guess} correctly!")

# Start the game
computer_guess(10)
