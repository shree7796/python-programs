list1 = [1,2,3,9,0]
list2 = [1,2,3,4,0]
list3 = []
for i in range(0, 5):
    if list1[i]==list2[i]:
        list3.append(list1[i])


print('common Elements are:--',list3)