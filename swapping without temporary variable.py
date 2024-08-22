# Function to swap two numbers
def swap_numbers(a, b):
    print("Before swapping: a =", a, "b =", b)
    a, b = b, a
    print("After swapping: a =", a, "b =", b)

# Test the function
swap_numbers(5, 10)
