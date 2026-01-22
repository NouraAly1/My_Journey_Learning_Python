# Initialize an empty list to store all fruit names
fruits = []

# Start an infinite loop that will continue until the user types 'done'
while True:
    # Prompt the user to enter a fruit name
    fruit = input("Enter fruit name: ").strip()
    
    # Check if the user wants to stop entering fruits
    if fruit.lower() == 'done':
        # Exit the loop if user types 'done'
        break
    
    # Validate that the input is not empty
    if not fruit:
        # Print error message and skip to next iteration if input is empty
        print("Invalid entry: Please enter a valid fruit name or 'done' to finish")
        continue
    
    # Add the valid fruit name to the list
    fruits.append(fruit.title())  # Capitalize first letter of each word
    
    # Display confirmation message
    print(f"✓ Added: {fruits[-1]}")

# Check if at least one valid fruit was entered
if len(fruits) > 0:
    # Sort all fruits alphabetically (case-insensitive)
    fruits.sort(key=str.lower)
    
    # Display the sorted list of all fruits
    print(f"\n{'='*50}")
    print("FRUIT COLLECTION SUMMARY")
    print(f"{'='*50}")
    print(f"All fruits (alphabetically sorted): {fruits}")
    print(f"Total fruits entered: {len(fruits)}")
    print(f"First fruit alphabetically: {fruits[0]}")
    print(f"Last fruit alphabetically: {fruits[-1]}")
    print(f"{'='*50}")
else:
    # Display message if no valid fruits were entered
    print("\nNo fruits were entered.")

