# get order cost from use 
order_cost = float(input("Enter order cost: "))

# creat a function with adding the fees
def total_cost():
    return order_cost + order_cost * 0.10

# print the total cost
print (f'The total cost is  {total_cost()}')
