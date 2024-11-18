import math

# Simple Calculator App with Square Root feature

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def square_root(x):
    if x < 0:
        return "Error! Cannot take the square root of a negative number."
    else:
        return math.sqrt(x)

def calculator():
    print("Welcome to the Python Calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")

    while True:
        choice = input("Enter choice (1/2/3/4/5): ")

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numerical values.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
        
        elif choice == '5':
            try:
                num = float(input("Enter the number to find the square root of: "))
                print(f"Square root of {num} = {square_root(num)}")
            except ValueError:
                print("Invalid input! Please enter a numerical value.")

        else:
            print("Invalid input! Please select a valid operation.")
        
        next_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
        if next_calculation != 'yes':
            print("Thank you for using the calculator!")
            break

# Run the calculator
if __name__ == "__main__":
    calculator()