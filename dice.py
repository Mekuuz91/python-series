import random
print("Welcome to the dic roll simulator")
roll_again = True
while roll_again:
    dice_roll = input("Roll the dice? (yes/no): ").lower()
    if dice_roll == "no":
        print("Goodbye")
        roll_again = False
    elif dice_roll == "yes":
        dice = random.randint(1, 6)
        print(f"You rolled: {dice}")
    else:
        print("Wrong input, Type 'yes' or 'no' ")
