# Get numbers from user
try:
    num = float(input("Enter a number: "))
except ValueError:
    print("Error: Please enter a valid number")
    exit()
try:
    num_divide_by = float(input("Enter the number to divide by: "))
except ValueError:
    print("Error: Please enter a valid number")
    exit()
if num_divide_by == 0:
    print("Error: Division by zero is not allowed")
    exit()
# Print separator line
print("_"*20)

# Get the division result
result = num / num_divide_by

# Print the division result
print(f'The division result is {result}')

# Check if number is divisible by or not and print the statement
if num % num_divide_by == 0:
    print(f"{num} is divisible by {num_divide_by}")

else:
    print(f'{num} is not divisible by {num_divide_by}')