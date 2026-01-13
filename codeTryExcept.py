try:
    result = 10 / 2
    number = int(input("Enter number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError as err1:
    print(err1)

print("success")