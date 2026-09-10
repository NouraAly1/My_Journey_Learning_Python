# Temperature List Tracker
# Collects temperature readings until you type 'done', then shows all temperatures sorted with highest and lowest

# Start with empty list and counter
temperature = []
count = 0

# Keep asking for temperatures until user types 'done'
while True:
    temp_input = input("enter temperature: ")
    if temp_input.lower() == 'done':
        break
    if temp_input == "":
        print("invalid temperature: ")
        continue
    
    # Make sure the input is a valid number
    try:
        temp = int(temp_input)
    except ValueError:
        print("invalid temperature")
        continue
    
    # Add the valid temperature to our list
    temperature.append(temp)
    count = count + 1

# Sort temperatures and show the results
temperature.sort()
print(temperature)
print("total temperatures entered: ",count)

# Show highest and lowest if we have any temperatures
if count > 0:
    print("the highest temperature: ", temperature[-1])
    print("the lowest temperature: ", temperature[0])
else:
    print("no valid temperatures were entered")