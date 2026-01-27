# Number Comparison Program
# This program compares three numbers and finds the greatest and smallest values

# Display header message
print('please, enter the number you want to compare\n- - - - - - - - - -')

# Get three numbers from user with error handling
try:
    first_num = float(input('Enter the first number: '))
except ValueError:
    print("Error: Please enter a valid number")
    exit()
try:
    second_num = float(input('Enter the second number: '))
except ValueError:
    print("Error: Please enter a valid number")
    exit()
try:
    third_num = float(input('Enter the third number: '))
except ValueError:
    print("Error: Please enter a valid number")
    exit()

# Print separator line
print ("_"*20)

# Find and display the greatest number using if-elif-else
if first_num > second_num and first_num > third_num:
    print(f'{first_num} is the greatest number')
elif second_num > first_num and second_num > third_num:
    print(f'{second_num} is the greatest number')
else:
    print(f'{third_num} is the greatest number')
#another way to find the greatest and smallestnumber with functions
# Find and display the greatest number using max() function
greatest = max(first_num, second_num, third_num)
print(f'{greatest} is the greatest number')

# Find and display the smallest number using min() function
smallest = min(first_num, second_num, third_num)
print(f'{smallest} is the smallest number')
