# Initialize an empty list to store all basketball scores
basketball_score = []

count = 0

# Start an infinite loop that will continue until the user types 'done'
while True :
    # Prompt the user to enter a score and store it as a string
    score_input = (input("Enter score: "))
    
    # Check if the user wants to stop entering scores
    if score_input == 'done':
        # Exit the loop if user types 'done'
        break
    
    # Try to convert the input string to an integer
    try:
        score = int(score_input)
    # If conversion fails (user entered non-numeric value), handle the error
    except:
        # Print error message and skip to next iteration of the loop
        print("Invalid score")
        continue
    
    # Check if the score is negative (invalid score)
    if score < 0 :
        # Print error message and skip to next iteration
        print("Score cannot be negative")
        continue
    
    # Add the valid score to the list
    basketball_score.append(score)
    
    count += 1

# Sort all scores in ascending order (lowest to highest)
basketball_score.sort()

# Display the sorted list of all scores
print(basketball_score)

# Display the total number of games played
print("Total games:", count)

# Check if at least one valid score was entered
if count > 0:
    # Display the lowest score (first item in sorted list)
    print("Lowest score:", basketball_score[0])
    # Display the highest score (last item in sorted list)
    print("Highest score:", basketball_score[-1])
else:
    # Display message if no valid scores were entered
    print("No valid score were entered")

    


