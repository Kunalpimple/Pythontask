# Ask the user to enter the temperature with unit (e.g., 100C or 212F)
user_input = input("Enter temperature (e.g., 100C or 212F): ").strip()

# Check if input ends with 'C' or 'F' (case-insensitive)
unit = user_input[-1].upper()
value = user_input[:-1]

# Validate the input and perform conversion
if value.replace('.', '', 1).isdigit():
    temp = float(value)

    if unit == "C":
        # Convert Celsius to Fahrenheit
        result = (temp * 9/5) + 32
        print(f"{temp}°C is equal to {result:.2f}°F")
    elif unit == "F":
        # Convert Fahrenheit to Celsius
        result = (temp - 32) * 5/9
        print(f"{temp}°F is equal to {result:.2f}°C")
    else:
        print("❌ Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
else:
    print("❌ Invalid temperature format.")
