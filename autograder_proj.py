# 90 - 100 = A
# 80 - 90 = B
# 70 - 80 = C
# 60 - 70 = D
# 0 - 60 = F

# get the score from the user.
score = float(input("Enter a score between 0 and 100:  "))

# check if score between the limit or not and put the grade.
if not ( 0 <= score <= 100):
    grade = None
    print("Enter a number between 0 and 100")
elif score >= 90 and score<=100:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

# print score and grade.
if grade is not None:
    print(f'your score is {score} and your grade is {grade}')
    

