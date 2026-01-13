# ask user to enter the number he wants to compare
print('please, enter the number you want to compare\n- - - - - - - - - -')

# get the numbers from user
first_num = float(input('Enter the first number: '))
second_num = float(input('Enter the second number: '))
third_num = float(input('Enter the third number: '))

# print underscores
print ("_---------------")

# compare numbers and print which one is greatest
#if first_num > second_num and first_num > third_num:
#    print(f'{first_num} is the greatest number')
#elif second_num > first_num and second_num > third_num:
 #       print(f'{second_num} is the greatest number')
#else:
#        print(f'{third_num} is the greatest number')

greatest = max(first_num, second_num, third_num)
print(f'{greatest} is the greatest number')
