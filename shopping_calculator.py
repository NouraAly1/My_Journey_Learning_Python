"""
A simple shopping calculator that checks if you have enough money to buy three items.
Shows how much you'll have left or how much more you need.
"""

# I created this function to avoid repeating the same validation code multiple times.
# It asks the user for a number and keeps asking until they enter a valid positive number.
def get_valid_number(prompt):
    while True:
        try:
            num = float(input(prompt))
            if num <= 0:
                print("Number must be greater than 0. Please try again.")
                continue
            return num
        except ValueError:
            print("Please enter a valid number")


# Get the amount of money the user has
total_money = get_valid_number("Enter the amount of money you have: ")

# Print separator line
print("_"*20)

# Get the prices of the three items
first_item = get_valid_number("Enter the price of first item: ")
second_item = get_valid_number("Enter the price of second item: ")
third_item = get_valid_number("Enter the price of third item: ")

# Print separator line
print("_"*20)

# Calculate the total cost and remaining amount
total = first_item + second_item + third_item
remaining_amount = total_money - total

# Check if the user has enough money to purchase all items
if total_money >= total:
    print(f'Items have been purchased successfully. Your total is {total:,.2f}$')
    print(f'The remaining amount is {remaining_amount:,.2f}$')
else:
    # User doesn't have enough money - calculate how much more is needed
    money_needed = total - total_money
    print("Sorry, You don't have enough balance")
    print(f'You need to add extra {money_needed:,.2f}$')