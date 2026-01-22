# Money Distribution Calculator
# Calculates how much each child receives when dividing money equally

def calculate_per_child(total_amount, num_children):
    """Calculate amount each child receives."""
    return round(total_amount / num_children, 2)

# Get amount of money
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

# Get number of children
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

# Get currency
currency = input("Enter currency: ").strip() or "units"

# Calculate and display result
per_child = calculate_per_child(amount_money, number_children)
print(f"\nEach child should get {per_child:,.2f} {currency}")