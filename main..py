print("Welcome to the Odd or Even analyzer!")

game_over = False
while not game_over:
    user_choice = input("Enter a number (or type 'exit' to quit): ")
    if user_choice == 'exit':
        print("Goodbye! Thanks for using the analyser.")
        game_over = True
    else:
        try:
            user_choice_int = int(user_choice)
            if user_choice_int % 2 == 0:
                print(f"{user_choice_int} is even.")
            elif user_choice_int % 2 != 0:
                print(f"{user_choice_int} is odd.")
        except ValueError:
            print("Invalid input, please enter a number or type 'exit'.")
