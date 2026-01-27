# ask user for the weight in kg
try:
    weight_kg = float(input("Enter weight in kg: "))
except ValueError:
    print("Error: Please enter a valid number")
    exit()

# Validate that weight is positive
if weight_kg <= 0:
    print("Error: Weight must be greater than 0")
    exit()
# convert from kg to gram
weight_gram = weight_kg * 1000

# print weight in grams
print(f'{weight_kg} kg is {weight_gram} grams')
