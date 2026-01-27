# id = company name + last letters from name + DOB
# email = take off from the '@' till the end and add '@apple.com

# get info from user
company_name = 'apple'
name = input("Enter your name: ").strip()
DOB = input("Enter your date of birth: ").strip()
email = input("Enter your email: ").strip()

# creating the id with slicing the last 3 letters
last_three = name[-3:]
employee_id = company_name + last_three + DOB
print(f'your id is : {employee_id}')

# edit user's email
try:
    index_of_at = email.index("@")
except ValueError:
    print("Error: Email must contain '@'")
    exit()
new_email = email[:index_of_at] + '@apple.com'
print(f'your new email is : {new_email}')