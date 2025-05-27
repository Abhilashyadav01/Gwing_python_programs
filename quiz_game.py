import random

def number_guessing_game():
    print("Welcome to the Number Guessing Quiz Game!")
    print("You will be asked 5 questions. Each correct answer gives you 1 point.\n")

    score = 0

    # Question 1
    answer1 = input("1. What is (7 + 5) - (10 * 12) * (2-5)? ")
    if answer1.strip() == "324":
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is 324.")

    # Question 2
    answer2 = input("2. Guess a number between 1 and 10: ")
    secret = random.randint(1, 10)
    if answer2.strip().isdigit() and int(answer2) == secret:
        print(f"Amazing! You guessed it right. It was {secret}.")
        score += 1
    else:
        print(f"Oops! The correct number was {secret}.")

    # Question 3
    answer3 = input("3. What is the full form of CPU ")
    if answer3.strip() == "Central Processing Unit":
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is Central Processing Unit.")

    # Question 4
    answer4 = input("4. What number is missing? 5, 10, __, 20 ")
    if answer4.strip() == "15":
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is 15.")

    # Question 5
    answer5 = input("5. What is the square root of 81? ")
    if answer5.strip() == "9":
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is 9.")

    # Final score
    print(f"\nQuiz Over! You scored {score} out of 5.")

# Run the game
if __name__ == "__main__":
    number_guessing_game()
