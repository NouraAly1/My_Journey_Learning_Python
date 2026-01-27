# Basic Calculator
# This program performs basic math operations (addition, subtraction, multiplication, division)
# using functions and handles errors for invalid input and division by zero

# Define functions for each math operation
def add_number(a, b):
    return a + b 
def subtract_number(a, b):
    return a - b
def multiply_number(a, b):
    return a * b
def divide_number(a, b):
    return a / b

# Get input from user and perform calculation
try:
    num1 = float(input("please enter first number: "))
    operator = input("please enter operator: ")
    num2 = float(input("please enter second number: "))
    
    # Perform calculation based on operator
    if operator == '+':
        result = add_number(num1, num2)
        print(result)
    elif operator == '-':
        result = subtract_number(num1, num2)
        print(result)
    elif operator == '*':
        result = multiply_number(num1, num2)
        print(result)
    elif operator == '/':
        # Check for division by zero
        if num2 != 0:
            result = divide_number(num1, num2)
            print(result)
        else:
            print("Error division by zero: ")
    else:
        print("operator is not valid")
except ValueError:
    print("Error: Please enter valid numbers")