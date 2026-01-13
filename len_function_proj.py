# get the name from user, clean from extra space and 
# make sure the first letter of each word is uppercase
name = input("Enter your name: ").strip().title()

# print name and greet user
print(f"Welcome {name} at Codezilla Python Course")

# get the length of the name and print it
print(f"your name is {len(name)} characters long")
