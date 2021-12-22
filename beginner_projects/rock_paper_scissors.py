import random


def rock_paper_scissors():
    user_selection = ""
    while user_selection != "E":
        print("WELCOME TO THE ULTIMATE ROCK PAPER GAME: ")
        print("R - ROCK")
        print("P - PAPER")
        print("S - SCISSORS")
        print("E - EXIT GAME")
        user_selection = str(input("YOUR SELECTION: ")).upper()

        games_selections = ["ROCK", "PAPER", "SCISSORS"]
        computer_choose = random.randint(0, len(games_selections) - 1)
        computer_selection = games_selections[computer_choose]

        if user_selection == "P" and computer_selection == "ROCK":
            print(f"COMPUTER SELECTION: {computer_selection},  YOU WON!\n")
        elif user_selection == "S" and computer_selection == "PAPER":
            print(f"COMPUTER SELECTION: {computer_selection},  YOU WON!\n")
        elif user_selection == "R" and computer_selection == "SCISSORS":
            print(f"COMPUTER SELECTION: {computer_selection},  YOU WON!\n")
        elif user_selection == computer_selection[0]:
            print("DRAW\n")
        elif user_selection == "E":
            print("THANK YOU FOR PLAYING ROCK, PAPER, SCISSORS\n")
        else:
            print(f"SORRY, COMPUTER SELECTION: {computer_selection}, YOU LOST!\n")
