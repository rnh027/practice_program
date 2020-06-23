def computepay(h,r):
    pay = 0
    if h>=40:
        h = h-40
        pay = 40*r
        r = r*1.5
    pay = pay + h*r

    return pay
try:
	hrs = float(input("Enter Hours:"))
	rate = float(input("Enter Rate:"))
except:
    print("Enter valid number")
p = computepay(hrs,rate)
print("Pay",p)
