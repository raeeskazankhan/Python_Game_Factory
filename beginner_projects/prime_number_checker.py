def prime_number(number):
    prime_checker = True
    for i in range(2, int(number / 2)):
        if number % i == 0:
            prime_checker = False

    if prime_checker:
        print(f"{number} IS A PRIME NUMBER")
    else:
        print(f"{number} IS NOT A PRIME NUMBER")

    print(" ")


def check_number():
    user_input = int(input("ENTER IN A NUMBER TO BE CHECKED: "))
    prime_number(number=user_input)
