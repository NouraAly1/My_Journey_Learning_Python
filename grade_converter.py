# Grade Calculator
# This program converts a numeric score (0.0 to 1.0) into a letter grade (A, B, C, D, F)

# Get score from user and handle invalid input
score = input("Enter Score between 0.0 and 1.0: ")
try:
    score = float(score)
except ValueError:
    print ("Error. Please enter a number")
    exit()

# Validate that score is within the valid range
if score < 0.0 or score > 1.0:
    print ("score out of range.")
    exit()
else:
    # Assign letter grade based on score ranges
    if score >= 0.9:
        print ("A")
    elif score >= 0.8:
        print ("B")
    elif score >= 0.7:
        print ("C")
    elif score >= 0.6:
        print ("D")
    else:
        print ("F")