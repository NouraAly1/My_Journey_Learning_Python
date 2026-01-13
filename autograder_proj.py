# 90 - 100 = A
# 80 - 90 = B
# 70 - 80 = C
# 60 - 70 = D
# 0 - 60 = F

# get the score from the user
score = float(input("Enter a score between 0 and 100:  "))

if score >= 90 and score <= 100:
    print("A")
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
elif score >= 0:
    print('F')
else:
    print('Enter a number between 0 and 100')
    

