item_price = []
count = 0
while True : 
    price_input = (input("Enter the price"))
    if price_input == 'done':
        break
    try:
        price = float(price_input)
    except:
        print("Invalid price")
        continue
    if price < 0:
        print("price cannot be negative")
        continue
    item_price.append(price)
    count += 1
item_price.sort()
print(item_price)
print("item_price: ", count)
if count > 0:
        print("The lowest price: ", item_price[0])
        print("The highest price: ", item_price[-1])
else:
        print("No valid prices were entered")
        