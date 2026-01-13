# id = company name + last letters from name + DOB
# email = take off from the '@' till the end and add '@apple.com

#get info from user
company_name = 'apple'
name = input("Enter your name: ").strip()
DOB = input("Enter your date of birth: ")
email = input("Enter your email: ").strip()

# creating the id with slicing the last 3 letters
last_three = name[-3:]
id = company_name + last_three + DOB
print(f'youe id is : {id}')

# edit user's email
index_of_at = email.index("@")
new_email = email[:index_of_at] + '@apple.com'
print(f'your new email is : {new_email}')