def calculate_():
    print("Enter 5 numbers one by one:")
    numbers = []

    for i in range(5):
        while True:
            try:
                num = float(input(f"Enter number {i+1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    average = sum(numbers) / len(numbers)
    print(f"The average of the entered numbers is: {average}")


if __name__ == "__main__":
    calculate_average()
