import random

print("Welcome to the Number Guessing Game!")

history = []

def get_guess():
    while True:
        guess = input("Enter your guess: ")
        try:
            guess_int = int(guess)
            return guess_int
        except ValueError:
            print("Invalid input! Please enter a number.")


def play_game():
    print("\nChoose a difficulty:")
    print("1. Easy (1–10)")
    print("2. Medium (1–50)")
    print("3. Hard (1–100)")
    print("4. Custom")

    choice = input("Enter your choice (1/2/3/4): ")

    # Set difficulty range
    if choice == "1":
        upper_limit = 10
        difficulty_name = "Easy"
    elif choice == "2":
        upper_limit = 50
        difficulty_name = "Medium"
    elif choice == "3":
        upper_limit = 100
        difficulty_name = "Hard"
    elif choice == "4":
        upper_limit = int(input("Enter a custom upper limit: "))
        difficulty_name = f"Custom ({upper_limit})"
    else:
        print("Invalid difficulty. Returning to menu...")
        return

    # Generate secret number
    secret_number = random.randint(1, upper_limit)
    attempts = 0

    print(f"\nI'm thinking of a number between 1 and {upper_limit}. Try to guess it!")

    while True:
        guess = get_guess()
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break

    # Save to history
    history.append({
        "difficulty": difficulty_name,
        "secret_number": secret_number,
        "attempts": attempts
    })


# Main program loop
game_over = False

while not game_over:
    command = input("\nEnter a command (play/history/exit): ").lower()

    if command == "play":
        play_game()

    elif command == "history":
        if not history:
            print("No game history yet.")
        else:
            print("\n--- Game History ---")
            for index, game in enumerate(history, start=1):
                print(f"Game {index}: Difficulty {game['difficulty']}, "
                      f"Secret Number: {game['secret_number']}, Attempts: {game['attempts']}")

    elif command == "exit":
        print("Goodbye!")
        game_over = True

    else:
        print("Invalid command! Please type: play, history, or exit.")
