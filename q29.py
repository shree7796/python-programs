lastmonth = int(input("Enter last months unit:--"))
currentmonth = int(input("Enter current months unit:--"))
units = currentmonth - lastmonth
print("total units:--",units)
if units<=100:
    total = units*2
    print("your total bill is:--",total)
elif units>=101 and units<=200:
    total = units*3
    print("your total bill is:--",total)
elif units>=201 and units<=300:
    total = units*4
    print("your total bill is:--",total)
if units>=301:
    total = units*5
    print("your total bill is:--",total)