# Money Distribution Calculator
# Calculates how much each child receives when dividing money equally

def calculate_per_child(total_amount, num_children):
    """Calculate amount each child receives when dividing money equally."""
    if num_children <= 0:
        raise ValueError("Number of children must be greater than 0")
    return round(total_amount / num_children, 2)

# Get amount of money from user and validate it's a positive number
while True:
    try:
        amount_money = float(input("Enter amount of money: "))
        if amount_money < 0:
            print("Error: Amount cannot be negative.")
            continue
        break
    except ValueError:
        print("Error: Please enter a valid number.")
        continue

# Get number of children from user and validate it's a positive whole number
while True:
    try:
        number_children = int(input("Enter number of children: "))
        if number_children <= 0:
            print("Error: Number must be greater than 0.")
            continue
        break
    except ValueError:
        print("Error: Please enter a whole number.")
        continue

# Get currency from user (defaults to "units" if empty)
currency = input("Enter currency: ").strip() or "units"

# Calculate per-child amount and display the result
per_child = calculate_per_child(amount_money, number_children)
print(f"\nEach child should get {per_child:,.2f} {currency}")