# PALINDROME IS A WORD OR PHRASE THAT IS SPELT THE SAME IN REVERSE ORDER

def palindrome():
    palindrome_sequence = str(input("ENTER IN A TEXT TO BE CHECKED: "))
    reverse_text = palindrome_sequence[::-1]

    if palindrome_sequence.lower() == reverse_text.lower():
        print("TEXT IS A PALINDROME!!!")
    else:
        print("TEXT IS NOT A PALINDROME")

    print("")
