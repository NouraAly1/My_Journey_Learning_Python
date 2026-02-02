# A grocery price tracker that collects prices, sorts them, and shows the lowest and highest prices.

item_price = []
count = 0

# Collect prices from user until they type 'done'
while True: 
    price_input = input("Enter the price:")
    if price_input == 'done':
        break
    
    # Check if input is a valid number
    try:
        price = float(price_input)
    except ValueError:
        print("Invalid price")
        continue
    
    # Make sure price is not negative
    if price < 0:
        print("price cannot be negative")
        continue
    
    # Add valid price to list
    item_price.append(price)
    count += 1

# Sort prices and display results
item_price.sort()
print(item_price)
print("total_items: ", count)

# Show lowest and highest prices if we have any
if count > 0:
    print("The lowest price: ", item_price[0])
    print("The highest price: ", item_price[-1])
else:
    print("No valid prices were entered")