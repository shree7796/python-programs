list = []
num = int(input("How many n values"))
for i in range(1, num+1):
    num1 = int(input("Enter number "))
    list.append(num1)

print('max element:--',max(list))
print('minimum element:--',min(list))