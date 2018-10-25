num = int(input("Enter any number for table:--"))
multi = 1


if num<=0:
    print("wrong input")
else:
    for i in range(1, 11):
        multi = num*i
        print(multi)