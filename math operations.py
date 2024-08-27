def calculate(x, n, operation):
    if operation == "Pow":
        return x ** n
    elif operation == "Add":
        return x + n
    elif operation == "Sub":
        return x - n
    elif operation == "Mul":
        return x * n
    elif operation == "Div":
        if n != 0:
            return x / n
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"

x = float(input("Enter the first number: "))
n = float(input("Enter the second number: "))
operation = input("Enter the operation (Pow, Add, Sub, Mul, Div): ")

result = calculate(x, n, operation)
print("Result:", result)
