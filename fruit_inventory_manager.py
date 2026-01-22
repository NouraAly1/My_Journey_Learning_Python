fruits = []

while True:
    fruit = input("Enter fruit name: ").strip()
    
    if fruit.lower() == 'done':
        break
    
    if not fruit:
        print("Invalid entry: Please enter a valid fruit name or 'done' to finish")
        continue
    
    fruits.append(fruit.title())
    print(f"Added: {fruits[-1]}")

if len(fruits) > 0:
    fruits.sort(key=str.lower)
    print(f"\nAll fruits (sorted): {fruits}")
    print(f"Total fruits: {len(fruits)}")
    print(f"First: {fruits[0]}")
    print(f"Last: {fruits[-1]}")
else:
    print("\nNo fruits were entered.")

