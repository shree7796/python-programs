student1 = []
student2 = []
studentss = []

num = int(input("How many students?:  "))
for i in range(0,num):
     name = str(input("input name of student "))
     studentss.append(name)
     roll_no = int(input("enter roll no of student"))
     studentss.append(roll_no)
     branchs = str(input("Enter branch of the student"))
     studentss.append(branchs)
     mark = int(input("input mark of the student"))
     studentss.append(mark)
     student2 = studentss


print(student2)
print(student1)
