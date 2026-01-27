# Get the amount of money user have
try:
    total_money = float(input("Enter the amount of money you have: "))
except ValueError:
    print("Error: Please enter a valid number")
    exit()

# print separator line
print("_"*20)

# Get the price of first, second and third item
try:
    first_item = float(input("Enter the price of first item: "))
except ValueError:
    print("Error: Please enter a valid number")
    exit()
try:
    second_item = float(input("Enter the price of second item: "))
except ValueError:
    print("Error: Please enter a valid number")
    exit()
try:
    third_item = float(input("Enter the price of third item: "))
except ValueError:
    print("Error: Please enter a valid number")
    exit()

# Print separator line
print("_"*20)

# Create variable for total, remaining, and money needed
total = first_item + second_item + third_item
remaining_amount = total_money - total
money_needed = total - total_money

# Check if customer have enough money or not if yes print purchased successfully if no  print sorry
# and print the remaining amount
if total_money >= total:
    print(f'Items have been purchased successfully. Your total is {total:,.2f}$')
    print (f'The remaining amount is {remaining_amount:,.2f}$')
else:
    print("Sorry, You don't have enough balance")
    print(f'You need to add extra {money_needed:,.2f}$')