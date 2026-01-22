# Initialize an empty list to store all temperatures
temperatures = []
count = 0

# Start an infinite loop that will continue until the user types 'done'
while True:
    # Prompt the user to enter a temperature
    temp_input = input("Enter temperature: ")
    
    # Check if the user wants to stop entering temperatures
    if temp_input.lower() == 'done':
        # Exit the loop if user types 'done'
        break
    
    # Try to convert the input string to an integer
    try:
        temp = int(temp_input)
    # If conversion fails (user entered non-numeric value), handle the error
    except:
        # Print error message and skip to next iteration of the loop
        print("Invalid temperature")
        continue
    
    # Add the valid temperature to the list
    temperatures.append(temp)
    
    # Increment the counter by 1
    count += 1

# Check if at least one valid temperature was entered
if count > 0:
    # Display all temperatures entered
    print(f"\nAll temperatures: {temperatures}")
    
    # Display the total number of temperatures entered
    print(f"Total temperatures: {count}")
    
    # Display the lowest temperature
    print(f"Lowest temperature: {min(temperatures)}")
    
    # Display the highest temperature
    print(f"Highest temperature: {max(temperatures)}")
    
    # Calculate and display the average temperature
    average = sum(temperatures) / len(temperatures)
    print(f"Average temperature: {average:.2f}")
else:
    # Display message if no valid temperatures were entered
    print("No valid temperatures were entered")