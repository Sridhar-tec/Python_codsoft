def calculator():
    print("Welcome to Simple Calculator")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print("\nChoose operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        choice = input("Enter operation (+, -, *, /): ")

        if choice == '+':
            result = num1 + num2
        elif choice == '-':
            result = num1 - num2
        elif choice == '*':
            result = num1 * num2
        elif choice == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Cannot divide by zero.")
                return
        else:
            print("Invalid operation selected.")
            return

        print(f"\nResult: {num1} {choice} {num2} = {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Run the calculator
calculator()
