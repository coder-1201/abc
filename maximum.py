def find_():
    print("Enter 10 numbers one by one:")
    numbers = []

    for i in range(10):
        while True:
            try:
                num = float(input(f"Enter number {i+1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    maximum = max(numbers)
    print(f"The maximum of the entered numbers is: {maximum}")


if __name__ == "__main__":
    find_maximum()
