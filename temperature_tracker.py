# Temperature Tracker
# Collects temperature readings until you type 'done', then shows stats like average, min, and max

# Start with empty lists to store temperatures
temperatures = []
count = 0

# Keep asking for temperatures until user types 'done'
while True:
    temp_input = input("Enter temperature: ")

    if temp_input.lower() == 'done':
        break

    # Make sure the input is a valid number
    try:
        temp = int(temp_input)
    except ValueError:
        print("Invalid temperature")
        continue

    # Add the valid temperature to our list
    temperatures.append(temp)
    count += 1

# Show all the results if we collected any temperatures
if count > 0:
    print(f"\nAll temperatures: {temperatures}")
    print(f"Total temperatures: {count}")
    print(f"Lowest temperature: {min(temperatures)}")
    print(f"Highest temperature: {max(temperatures)}")
    average = sum(temperatures) / len(temperatures)
    print(f"Average temperature: {average:.2f}")
else:
    print("No valid temperatures were entered")