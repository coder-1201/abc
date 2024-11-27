def add_numbers():
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

    total = sum(numbers)
    print(f"The sum of the entered numbers is: {total}")


if __name__ == "__main__":
    add_numbers()
