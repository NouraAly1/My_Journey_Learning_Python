temperatures = []
count = 0

while True:
    temp_input = input("Enter temperature: ")
    
    if temp_input.lower() == 'done':
        break
    
    try:
        temp = int(temp_input)
    except:
        print("Invalid temperature")
        continue
    
    temperatures.append(temp)
    count += 1

if count > 0:
    print(f"\nAll temperatures: {temperatures}")
    print(f"Total temperatures: {count}")
    print(f"Lowest temperature: {min(temperatures)}")
    print(f"Highest temperature: {max(temperatures)}")
    average = sum(temperatures) / len(temperatures)
    print(f"Average temperature: {average:.2f}")
else:
    print("No valid temperatures were entered")