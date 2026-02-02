
#This is just practicing functions.
#This program calculates pay with overtime (1.5x rate for hours over 40).

#Calculates the pay based on hours worked and hourly rate.
#If hours exceed 40, calculates overtime pay at 1.5x the rate.

def computepay(h, r):
    # Convert inputs to float for calculations
    h = float(h)
    r = float(r)
    
    # Calculate pay with overtime if hours exceed 40
    if h > 40:
        regular = 40 * r
        overtime = (h - 40) * (r * 1.5)
        pay = regular + overtime
    else:
        # Calculate regular pay for 40 hours or less
        pay = h * r
    return pay


# Get hours and rate from user
hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")

# Calculate and display the gross pay
gross_pay = computepay(hrs, rate)
print("Pay", gross_pay)
