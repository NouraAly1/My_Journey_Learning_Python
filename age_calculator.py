# ask user for the year, month and day of birth
birth_year = int(input("Enter year of birth: "))
birth_month = int(input("Enter month of birth (1-12): "))
birth_day = int(input('Enter birth day (1-31): '))

# ask user for the current year, month and day
current_year = int(input("Enter current year: "))
current_month = int(input("Enter current month (1-12): "))
current_day = int(input('Enter current day (1-31): '))

# calculate diffrences
years = current_year - birth_year
months = current_month - birth_month
days = current_day - birth_day
# if months are negative
if months < 0:
    years -= 1
    months += 12

if days < 0:
    months -=1
    days +=31

# print age
print(f'You are {years} years {months} months and {days} days old')

#days are slightly in correct working on learning datetime module. 