def (num):
    if num < 0:
        return "Factorial is not defined for negative numbers."
    elif num == 0 or num == 1:
        return 1
    else:
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result


def main():
    while True:
        try:
            number = int(input("Enter a number to find its factorial (or type 'q' to quit): "))
            print(f"The factorial of {number} is: {factorial(number)}")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            break


if __name__ == "__main__":
    main()
