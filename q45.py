list = []

n = int(input("How many numbers you wants to enter?"))
for i in range(0, n):
    a = int(input("Enter values"))
    list.append(a)
print(list)
avg = 0
print("maximum number is",max(list))
print("minimum number in list",min(list))
for i in range(0,n):
    avg = avg+list[i]

avg = avg/n
print("average is:--",avg)
