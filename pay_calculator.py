# Pay Calculator
# Calculates employee pay based on hours worked - regular pay for first 40 hours, overtime at 1.5x rate for hours over 40

# Get hours worked and hourly rate from user
h = float(input("Enter hours: "))
r = float(input("Enter rate: "))

# Calculate pay for regular hours (40 or less)
if h <= 40:
    reg_pay = h * r
    print("regular pay:", reg_pay)

# Calculate pay with overtime (over 40 hours)
elif h > 40:
    reg_pay = 40 * r
    overtime_pay = (h-40) * r * 1.5
    gross_pay = reg_pay + overtime_pay
    print("regular pay: ", reg_pay)
    print("overtime pay: ", overtime_pay)
    print("gross pay:", gross_pay)
