# get order cost from user 
order_cost = float(input("Enter order cost: "))

# creat a function to add the fees
def total_cost():
    return order_cost + order_cost * 0.10

# print the total cost
print ("The total cost is : ", total_cost())
