from beginner_projects import guess_the_number
from beginner_projects import prime_number_checker

user_selection = -1
while user_selection != 0:
    print('WELCOME TO THE PYTHON FUN FACTORY')
    print("GAMES ON OFFER: ")
    print("1 - GUESS THE NUMBER")
    print("2 - PRIME NUMBER CHECKER")
    print("0 - EXIT")
    user_selection = int(input("SELECT YOUR GAME: "))

    if user_selection == 1:
        guess_the_number.guess_number()
    elif user_selection == 2:
        prime_number_checker.check_number()
