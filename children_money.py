# get the money, num oe children and currency from user 
amount_money = float(input("Enter amount of money: "))
number_children = float(input("Enter number of children: "))
currency = input("Enter your currency: ")

# creat a function to get each one's amount and round it to the nearest 2 
def each_one():
    return round(amount_money / number_children, 2)

# call the function and print the result
print(f'each one should get {each_one()} {currency}')