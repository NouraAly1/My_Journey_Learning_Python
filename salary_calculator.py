# ask user for employee name, hours,rate and currency
name = input("Enter employee name: ")
worked_hours = float(input("Enter hours worked: "))
hourly_pay = float(input("Enter hourly pay: "))
currency = input("Enter your currency: ")

# calculate salary
if worked_hours > 100:
    base_pay = 100 * hourly_pay
    over_pay = (worked_hours - 100 ) * (2 * hourly_pay)
    salary = base_pay + over_pay
    print(f'{name} has worked {worked_hours} this month, your salary is {salary:,.2f} {currency}')
else:
    salary = worked_hours * hourly_pay
    print(f'{name} has woked {worked_hours} this month, and your salary is {salary:,.2f} {currency}')