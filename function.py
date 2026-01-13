def computepay(h,r):
    h = float(h)
    r = float(r)
    if h > 40:
        regular = 40 * r
        overtime = (h-40) * (r * 1.5)
        pay = regular + overtime
    else:
        pay = h * r
    return(pay)
hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")
gross_pay = computepay (hrs, rate)
print("Pay" ,gross_pay)
