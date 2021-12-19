import random


def rolling_dice():
    user_input = "Y"
    while user_input != "N":
        dice_rolled = random.randint(1, 8)
        print(f"DICE ROLLED, LANDED ON: {dice_rolled}")
        print("")
        user_input = str(input("DO YOU WANT TO CONTINUE? Y OR N: ")).upper()
