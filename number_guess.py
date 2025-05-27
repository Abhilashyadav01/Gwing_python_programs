import random

def number_guessing_game():
    print(" Welcome to the Number Guessing Game!")
    print("System generates  a number between 1 and 100.")
    print("Can you guess what it is?\n")

    secret_number = random.randint(1, 100)
    guess = None
    attempts = 0

    while guess != secret_number:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.\n")
            elif guess > secret_number:
                print("Too high! Try again.\n")
            else:
                print(f"🎉 Correct! The number was {secret_number}.")
                print(f"You guessed it in {attempts} attempt(s).")
        except ValueError:
            print("⚠️ Please enter a valid integer.")

# Run the game
if __name__ == "__main__":
    number_guessing_game()
