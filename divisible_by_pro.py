# get numbers from user
num = float(input("Enter a number: "))
num_divide_by = float(input("Enter the number to divide by: "))

#print underscore
print("_"*20)

# get the division result
result = num / num_divide_by

# print the division result
print(f'The division result is {result}')

# check if number is divisible by or not and print the statment
if num % num_divide_by == 0:
    print(f"{num} is divisible by {num_divide_by}")

else:
    print(f'{num} is not divisible by {num_divide_by}')