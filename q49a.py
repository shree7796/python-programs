'''from collections import namedtuple
Person = namedtuple('Person', 'name date')
t = {70: Person('rahul', 'IT')}
t[70] = Person('name2', t[70].date)
print(t)'''

list = []
n = int(input("How many students?"))
for i in range(0, n):
    a = str(input("Enter student name"))
    list.append(a)

print(list)