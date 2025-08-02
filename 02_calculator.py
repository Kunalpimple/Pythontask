# Define a function to perform the calculation
def calculate(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        # Check to avoid division by zero
        if num2 == 0:
            return "Error: Cannot divide by zero."
        return num1 / num2
    else:
        return "Invalid operator."

# Start a loop to allow repeated calculations
while True:
    # Take two numbers as input from the user
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("⚠️ Please enter valid numbers.")
        continue

    # Ask for the operator
    operator = input("Enter an operator (+, -, *, /): ")

    # Call the calculation function and display result
    result = calculate(num1, num2, operator)
    print("Result:", result)

    # Ask if the user wants to perform another calculation
    again = input("Do you want to calculate again? (yes/no): ")
    if again.lower() != "yes":
        print("Goodbye!")
        break
