# Get user input for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform each operation and print the result
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

# Check for division by zero
if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("Error: Division by zero is not allowed")
