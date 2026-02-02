# A fruit inventory manager that collects fruit names, sorts them, and displays a summary.

fruits = []

# Collect fruit names from user until they type 'done'
while True:
    fruit = input("Enter fruit name: ").strip()
    
    # Stop collecting when user types 'done'
    if fruit.lower() == 'done':
        break
    
    # Skip empty entries
    if not fruit:
        print("Invalid entry: Please enter a valid fruit name or 'done' to finish")
        continue
    
    # Add fruit to list and confirm
    fruits.append(fruit.title())
    print(f"Added: {fruits[-1]}")

# Display sorted summary if fruits were entered
if len(fruits) > 0:
    fruits.sort(key=str.lower)
    print(f"\nAll fruits (sorted): {fruits}")
    print(f"Total fruits: {len(fruits)}")
    print(f"First: {fruits[0]}")
    print(f"Last: {fruits[-1]}")
else:
    print("\nNo fruits were entered.")

