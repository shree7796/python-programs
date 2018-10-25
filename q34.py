num = int(input("till how many numbers"))
sum = 1
print(sum)
if num<=0:
    print('eneter valid number')
else:

    for i in range(2, num+1):
        sum = sum+i
        print(sum)