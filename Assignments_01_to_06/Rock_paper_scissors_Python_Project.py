import random

def play():
    print("\n🎮 Welcome to Rock, Paper, Scissors!")
    print("Choose:")
    print("  'r' for Rock")
    print("  'p' for Paper")
    print("  's' for Scissors")

    user = input("\nYour choice: ").lower()
    computer = random.choice(['r', 'p', 's'])

    choices = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}

    if user not in choices:
        return "Invalid choice. Please choose 'r', 'p', or 's'."

    print(f"\nYou chose: {choices[user]}")
    print(f"Computer chose: {choices[computer]}")

    if user == computer:
        return "It's a Tie!"
    
    if is_win(user, computer):
        return "You Won!"
    
    return "Computer Won!"

def is_win(player, opponent):
    # Winning conditions: rock beats scissors, scissors beats paper, paper beats rock
    return (player == 'r' and opponent == 's') or \
           (player == 's' and opponent == 'p') or \
           (player == 'p' and opponent == 'r')

# Run the game
print(play())
