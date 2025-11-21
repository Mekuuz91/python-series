import random
print("Welcome to the Dice Rolling Simulator!")
game_over = False
history = []
while not game_over:
    command = input("\nEnter a command (roll/history/exit): ").lower()
    if command == 'roll':
        num_dice = int(input("How many dice do you want to roll."))
        sides = int(input('How many sides should a die have?'))
        results = []
        for i in range(num_dice):
            roll = random.randint(1, sides)
            results.append(roll)
        print("You rolled:", results)
        history.append(results)
    elif command == 'history':
        if not history:
            print("No rolls yet.")
        else:
            for index, roll_list in enumerate(history, start=1):
                print(f"Roll {index}: {roll_list}")
    elif command == 'exit':
        print("Thanks for playing! Goodbye.")
        game_over = True
    else:
        print("Invalid command! Type 'roll', 'history', or 'exit'.")