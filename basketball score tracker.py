basketball_score = []
count = 0
while True :
    score_input = (input("Enter score"))
    if score_input == 'done':
        break
    try:
        score = float(score_input)
    except:
        print("Invalid score")
        continue
    if score < 0 :
        print("Score cannot be negative")
        continue
    basketball_score.append(score)
    count += 1
basketball_score.sort()
print(basketball_score)
print("Total games:", count)
if count > 0:
    print("Lowest score:", basketball_score[0])
    print("Highest score:", basketball_score[-1])
else:
    print("No valid score were entered")

        


