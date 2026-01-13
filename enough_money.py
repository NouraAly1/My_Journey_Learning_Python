# get the amount of money user have
money = float(input("Enter the amount of money you have: "))

# print underscore
print("_"*20)

# get the price of first, second and third item
first_item = float(input("Enter the price of first item: "))
second_item = float(input("Enter the price of second item: "))
third_item = float(input("Enter the price of third item: "))


# print underscore
print("_"*20)

# creat variable for total, remaining, and money needed
total = first_item + second_item + third_item
remaining_amount = money - total
money_needed = total - money

# check if customer have enough money or not if yes print purchased successfully if no  print sorry
# and print the remaining amount
if money >= total:
    print(f'Items have been purchased successfully')
    print (f'The remaining amount is {remaining_amount:,.2f}$ ')
else:
    print("Sorry, You don't have enough balance" )
    print(f'You need to add extra {money_needed:,.2f}$')