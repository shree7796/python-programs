maths = int(input('Enter maths marks:--'))
chemistry = int(input('Enter chemistry marks:--'))
physics = int(input('Enter maths physics:--'))
english = int(input('Enter english marks:--'))
hindi = int(input('Enter hindi marks:--'))
sum = maths + chemistry + physics + english + hindi
outof = 500
per = sum/outof*100
print(per,"%")
if per>=60:
    print("A--Grade")
elif per>=50:
    print("B--Grade")
elif per>=40:
    print("c--Grade")
else:
    print("D--Grade")
