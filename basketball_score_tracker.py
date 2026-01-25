# Basketball Score Tracker
# Keeps track of basketball game scores until the user types 'done', then shows the lowest, highest, and total games played

# Start with empty lists to store scores and keep count
basketball_score = []
count = 0

# Keep asking for scores until user types 'done'
while True:
    score_input = input("Enter score: ")

    if score_input == 'done':
        break

    # Make sure the input is a valid number
    try:
        score = int(score_input)
    except ValueError:
        print("Invalid score")
        continue

    # Don't allow negative scores
    if score < 0:
        print("Score cannot be negative")
        continue

    # Add the valid score to our list and increase the count
    basketball_score.append(score)
    count += 1

# Sort all scores and show the results
basketball_score.sort()
print(basketball_score)
print("Total games:", count)

# Show lowest and highest scores if we have any
if count > 0:
    print("Lowest score:", basketball_score[0])
    print("Highest score:", basketball_score[-1])
else:
    print("No valid score were entered")