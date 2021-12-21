from beginner_projects import guess_the_number
from beginner_projects import prime_number_checker
from beginner_projects import rolling_dice_simulator
from beginner_projects import fibonacci_sequence
from beginner_projects import palidrome

user_selection = -1
while user_selection != 0:
    print('WELCOME TO THE PYTHON FUN FACTORY')
    print("GAMES ON OFFER: ")
    print("1 - GUESS THE NUMBER")
    print("2 - PRIME NUMBER CHECKER")
    print("3 - ROLLING DICE SIMULATOR")
    print("4 - FIBONACCI SEQUENCE")
    print("5 - PALINDROME")
    print("0 - EXIT")
    user_selection = int(input("SELECT YOUR GAME: "))

    if user_selection == 1:
        guess_the_number.guess_number()
    elif user_selection == 2:
        prime_number_checker.check_number()
    elif user_selection == 3:
        rolling_dice_simulator.rolling_dice()
    elif user_selection == 4:
        fibonacci_sequence.fibonacci()
    elif user_selection == 5:
        palidrome.palindrome()

# POTENTIAL PROJECTS TO DO
# HANGMAN, BINARY SEARCH ALGORITHM, ROCK PAPER SCISSORS,
# RANDOM PASSWORD GENERATOR, TIC TAC TOE,
