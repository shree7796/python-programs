num = int(input("Enter any number"))
fact = 1
if num<=0:
    print("wrong input")
else:
    for i in range(1,num+1):
        fact = fact*i
    print(fact)