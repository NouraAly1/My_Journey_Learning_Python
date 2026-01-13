xh = input("Enter hours")
xr = input("Enter rate")
h = float(xh)
r = float(xr)
if h<= 40:
    reg_pay = h * r
    print("regular pay:", reg_pay)
elif h > 40:
    reg_pay = h * r
    overtime_pay = (h-40) * r * 0.5
    gross_pay = reg_pay + overtime_pay
    print (gross_pay)
