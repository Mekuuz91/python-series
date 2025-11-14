print("Welcome to the Leap year Checker!")
game_over = False
while not game_over:
    year = input("Enter a year: ")
    if year == "exit":
        print('Game over')
        game_over = True
    else:
        try:
            year_int = int(year)
            if (year_int % 4 == 0 and year_int % 100 != 0) or year_int % 400 == 0:
                print(f"{year} is a leap")
            else:
                print(f"{year} is not a leap year.")
        except ValueError:
            print("Input Correct Information")

