# Age Calculator
# Calculates your age in years, months, and days based on your birth date and current date

# Get birth date from user and validate input
try:
    birth_year = int(input("Enter year of birth: "))
    birth_month = int(input("Enter month of birth (1-12): "))
    if not (1 <= birth_month <= 12):
        print("Invalid input. Month must be between 1 and 12.")
        exit()
    birth_day = int(input('Enter birth day (1-31): '))
    if not (1 <= birth_day <= 31):
        print("Invalid input. Day must be between 1 and 31.")
        exit()
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

# Get current date from user and validate input
try:
    current_year = int(input("Enter current year: "))
    current_month = int(input("Enter current month (1-12): "))
    if not (1 <= current_month <= 12):
        print("Invalid input. Month must be between 1 and 12.")
        exit()
    current_day = int(input('Enter current day (1-31): '))
    if not (1 <= current_day <= 31):
        print("Invalid input. Day must be between 1 and 31.")
        exit()
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

# Make sure birth date is not in the future
if (birth_year > current_year) or (birth_year == current_year and birth_month > current_month) or (birth_year == current_year and birth_month == current_month and birth_day > current_day):
    print("Error: Birth date cannot be in the future.")
    exit()

# Calculate the difference between current date and birth date
years = current_year - birth_year
months = current_month - birth_month
days = current_day - birth_day

# Adjust if months are negative (birthday hasn't occurred this year)
if months < 0:
    years -= 1
    months += 12

# Adjust if days are negative (borrow days from previous month)
if days < 0:
    months -= 1
    days += 30
    # If months became negative after borrowing, borrow from years
    if months < 0:
        years -= 1
        months += 12

# Display the calculated age
print(f'You are {years} years {months} months and {days} days old')
