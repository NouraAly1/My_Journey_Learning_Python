fruit_name = []
count = 0
while True:
    fruit = input("enter fruit_name")
    if fruit.lower() == 'done':
        break
    if fruit == (" "):
        print("Invalid Entry")
        continue
    fruit_name.append(fruit)
    count = count + 1
fruit_name.sort()
print(fruit_name)
print("total fruits entered:", count)
print("first fruit alphabetically:", fruit_name[0])
print("last fruit alphabetically:", fruit_name[-1])