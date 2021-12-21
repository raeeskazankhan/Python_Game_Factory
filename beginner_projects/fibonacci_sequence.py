def fibonacci():
    nth_term = int(input("TO WHAT TERM DO YOU WANT THE SEQUENCE TILL: "))

    fibonacci_sequence = [0, 1]
    if nth_term == 0:
        fibonacci_sequence = [0]
    else:
        for i in range(2, nth_term + 1):
            next_term = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
            fibonacci_sequence.append(next_term)

    print(f"FIBONACCI SEQUENCE TO {nth_term}th TERM IS:")
    print(fibonacci_sequence)
    print("")
