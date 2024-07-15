class Room2:
    Trainers="prabhu"
    student_count=25
    subject="Python"

r = Room2()
print(r)


# without using parenthesis for class 
r1=Room2
print(r1)

# by using class object
print(r.Trainers)
print(r.student_count)
print(r.subject)

print(Room2())

# this gives doc of the fucntiton
# print(Room2.__dict__)

# using class name
print(Room2.Trainers)
print(Room2.student_count)
print(Room2.subject)


class Demo:
    a = 10
    b = 20

d = Demo()
print(d)

d1 = Demo()
print(d)

# printing demo
print(d.a)
print(d1.a)
print(d.b)
print(Demo.a)

# After modification
Demo.a = 45
print(Demo.a)
print(d.a)
print(d1.a)

Demo.a = 56
print(Demo.a)
print(d.a)
print(d1.a)


d1.a = "New Data"
print(d1.a)

