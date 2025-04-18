# Import the random library which lets us simulate random things like dice!
import random

# Number of sides on each die to roll
NUM_SIDES: int = 6

def main():
    # Roll two dice
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)
    
    # Get their total
    total: int = die1 + die2
    
    # Print out the results
    print(f"Dice have {NUM_SIDES} sides each.")
    print(f"First die: {die1}")
    print(f"Second die: {die2}")
    print(f"Total of two dice: {total}")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
