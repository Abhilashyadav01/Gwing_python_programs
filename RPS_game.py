import random

def rock_paper_scissors():
    print("🎮 Welcome to Rock, Paper, Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to play. Type 'quit' to end the game.\n")

    options = ["rock", "paper", "scissors"]
    user_wins = 0
    computer_wins = 0
    round_number = 0

    while True:
        user_choice = input("Your choice: ").lower()

        if user_choice == "quit":
            break
        if user_choice not in options:
            print("Invalid input. Please try again.\n")
            continue

        computer_choice = random.choice(options)
        round_number += 1

        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win this round!")
            user_wins += 1
        else:
            print("Computer wins this round!")
            computer_wins += 1

        print(f"Score after {round_number} round(s) → You: {user_wins} | Computer: {computer_wins}\n")

    print("\n🧾 Final Score")
    print(f"You won {user_wins} time(s).")
    print(f"Computer won {computer_wins} time(s).")
    print("Thanks for playing!")

# Run the game
if __name__ == "__main__":
    rock_paper_scissors()