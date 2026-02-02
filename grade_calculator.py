# A simple grade calculator that converts numeric scores to letter grades.
# Grade Scale: 90-100=A, 80-89=B, 70-79=C, 60-69=D, 0-59=F

grade = None

# Get score from user and handle invalid input
try:
    score = float(input("Enter a score between 0 and 100: "))
except ValueError:
    # User entered something that's not a number
    print("Error: Please enter a valid number.")
else:
    # Check if score is valid and convert to letter grade
    if not (0 <= score <= 100):
        print("Error: Score must be between 0 and 100.")
        grade = None
    elif score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'

# Display the results if we got a valid grade
if grade is not None:
    print(f"\nScore: {score:.2f}")
    print(f"Grade: {grade}")
else:
    print("\nUnable to calculate grade. Please try again with a valid score.")

