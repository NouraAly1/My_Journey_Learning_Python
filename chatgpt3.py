
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