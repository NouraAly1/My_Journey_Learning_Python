# Grade Scale: 90-100=A, 80-89=B, 70-79=C, 60-69=D, 0-59=F

grade = None

try:
    score = float(input("Enter a score between 0 and 100: "))
except ValueError:
    print("Error: Please enter a valid number.")
    grade = None
else:
    if not (0 <= score <= 100):
        grade = None
        print("Error: Score must be between 0 and 100.")
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

if grade is not None:
    print(f"\nScore: {score:.2f}")
    print(f"Grade: {grade}")
else:
    print("\nUnable to calculate grade. Please try again with a valid score.")

