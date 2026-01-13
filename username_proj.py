# get name from user, birth year, month and date
name = input("Enter your name: ").strip()
year = int(input("Enter your Birth Year: "))
month = int(input("Enter your Birth Month: "))
day = int(input("Enter your Birth Day: "))

# replace, lower case and create username
username = f'{name.lower().replace(" ", "_")}'
username = f'{username}_{day}_{month}_{int(year+len(name))}'
username = f'{username}@codezilla.com'

# greet user
print("_"*20)
print(f"Hello, {name.title()}")

# print username
print(f'Your Username is ...\n{username}')