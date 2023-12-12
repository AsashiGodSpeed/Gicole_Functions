
def find_smallest_factor(n):
    
    if n < 2:
        print("Invalid input. Enter a number greater than 2.")
        return

    for i in range(2, n + 1):
        if n % i == 0:
            print(f"The smallest factor of {n} is: {i}")
            break

def find_prime_numbers(start, end):
    if end < start:
        print(f"Enter a number greater than {start}.")
        return

    print(f"Prime numbers between {start} and {end} are: ", end="")

    for num in range(start, end + 1):
        if num < 2:
            continue
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")
    print("\n")

while True:
    print("Options:")
    print("1. Find the smallest factor of n")
    print("2. Find prime numbers within a range")
    print("0. TERMINATOR")

    choice = int(input("Enter your choice: "))

    if choice == 0:
        print("Program terminated.")
        break
    elif choice == 1:
        integer = int(input("Enter an integer >= 2: "))
        find_smallest_factor(integer)
    elif choice == 2:
        start = int(input("Enter a number [start]: "))
        end = int(input("Enter a number [end]: "))
        find_prime_numbers(start, end)
    else:
        print("Invalid choice. Please enter 0, 1, or 2.")
