def add_number(a, b):
    return a + b 
def subtract_number(a, b):
    return a - b
def multiply_number(a, b):
    return a * b
def divide_number(a, b):
    return a / b
num1 = float(input("please enter first number: "))
operator = input("please enter operator: ")
num2 = float(input("please enter second number: "))
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
    if num2 != 0:
        result = divide_number(num1, num2)
        print(result)
    if num2 == 0:
        print("Error division by zero: ")
else:
    print ("operator is not valid")
    