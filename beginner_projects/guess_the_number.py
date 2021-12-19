import random


def guess_number():
    computer_guess = random.randint(0, 10)
    user_answer = int(input("CHOOSE A NUMBER FROM 0 TO 10: "))

    counter = 0
    while computer_guess != user_answer:
        counter = counter + 1
        user_answer = int(input("TRY AGAIN. CHOOSE A NUMBER FROM 0 TO 10: "))
        if computer_guess == user_answer:
            print("CORRECT!")
        elif counter > 4:
            counter_answer = input("DO YOU WANT TO TRY AGAIN: YES OR NO: ")
            if str(counter_answer).upper() == "NO":
                print(f"COMPUTER SELECTED {computer_guess}. THANK YOU FOR PLAYING")
                print("")
                break
            else:
                counter = 0
