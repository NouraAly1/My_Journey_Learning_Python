# Order Cost Calculator with Service Fee
# This program calculates the total cost of an order by adding a 10% service fee to the base order cost

# Get order cost from user with error handling
try:
    order_cost = float(input("Enter order cost: "))
except ValueError:
    print("Error: Please enter a valid number")
    exit()

# Function to calculate total cost with 10% service fee
def total_cost():
    return order_cost + order_cost * 0.10

# Validate that order cost is greater than zero
if order_cost <= 0:
    print("Error: Order cost must be greater than 0")
    exit()

# Display the total cost
print(f'The total cost is {total_cost()}')
