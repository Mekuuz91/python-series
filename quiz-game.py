# -----------------------------
# Step 0: Questions Dictionary
# -----------------------------
questions = {
    "What is 10 + 5?": "15",
    "What is the capital of Nigeria?": "abuja",
    "What planet do we live on?": "earth",
    "How many hours are in one day?": "24",
    "What is the opposite of 'hot'?": "cold",
    "What is 7 - 2?": "5",
    "What gas do humans breathe in to stay alive?": "oxygen",
    "What is the first month of the year?": "january",
    "What is the color of grass?": "green",
    "Which animal is known as the King of the Jungle?": "lion"
}

# -----------------------------
# Step 1: History list
# -----------------------------
history = []

# -----------------------------
# Step 2: Function to ask one question
# -----------------------------
def ask_question(question, answer):
    user_answer = input(question + " ")  # Show the question and wait for input
    if user_answer.lower() == answer.lower():  # Case-insensitive check
        print("Correct!")
        return True
    else:
        print(f"Wrong! The correct answer is {answer}.")
        return False

# -----------------------------
# Step 3: Function to play the quiz
# -----------------------------
def play_quiz():
    score = 0  # Track how many answers are correct
    total_questions = len(questions)  # Total number of questions

    # Loop through all questions in the dictionary
    for q, a in questions.items():
        if ask_question(q, a):
            score += 1  # Increment score if correct

    print(f"\nQuiz Complete! You got {score}/{total_questions} correct.")

    # Save result to history
    history.append({"score": score, "total": total_questions})

# -----------------------------
# Step 4: Main Program Loop
# -----------------------------
game_over = False

while not game_over:
    command = input("\nEnter a command (play/history/exit): ").lower()

    if command == "play":
        play_quiz()  # Start a new quiz

    elif command == "history":
        if not history:
            print("No past quiz results yet.")
        else:
            print("\n--- Quiz History ---")
            for index, result in enumerate(history, start=1):
                print(f"Game {index}: {result['score']}/{result['total']} correct")

    elif command == "exit":
        print("Goodbye! Thanks for playing.")
        game_over = True

    else:
        print("Invalid command! Please type: play, history, or exit.")
