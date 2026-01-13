temperature = []
count = 0
while True:
    temp_input = input("enter temperature: ")
    if temp_input == 'done':
        break
    if temp_input == "":
        print("invalid temperature: ")
        continue
    try:
        temp = int(temp_input)
    except:
        print("invalid temperature")
        break
    temperature.append(temp_input)
    count = count + 1
temperature.sort()
print(temperature)
print("total temperature entered: ",count)
print("the highest temperature: ", temperature[-1])
print("the lowest temperature: ", temperature[0])