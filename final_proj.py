# ask about name, currency, hours and rate
name = input("Enter employee name: ").strip().title()
currency = input("Enter currency: ").strip().title()
hours = float(input("Enter number of hours worked: "))
hourly_rate = float(input("Enter hourly rate: "))

# calculate salary
salary = hours * hourly_rate

# print salary
print('-'*20)
print (f"The Salary of {name} is {salary:,} {currency}")