# Grade Scale:
# 90 - 100 = A
# 80 - 89  = B
# 70 - 79  = C
# 60 - 69  = D
# 0 - 59   = F

# Initialize grade variable
grade = None

# Get the score from the user with error handling
try:
    score = float(input("Enter a score between 0 and 100: "))
except ValueError:
    # Handle non-numeric input
    print("Error: Please enter a valid number.")
    grade = None
else:
    # Check if score is within the valid range (0-100)
    if not (0 <= score <= 100):
        grade = None
        print("Error: Score must be between 0 and 100.")
    # Determine grade based on score ranges
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

# Display the result if a valid grade was calculated
if grade is not None:
    print(f"\n{'='*40}")
    print("GRADE RESULT")
    print(f"{'='*40}")
    print(f"Score: {score:.2f}")
    print(f"Grade: {grade}")
    print(f"{'='*40}")
else:
    print("\nUnable to calculate grade. Please try again with a valid score.")

