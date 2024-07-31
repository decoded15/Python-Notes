class Employee:
    a=1

class programmer(Employee):
    b=2

class manager(programmer):
    c=3

o=Employee()
print(o.a)
# print(o.b) #this will show error as b attribute is not present in Employee
o=programmer()
print(o.a,o.b)

o=manager()
print(o.a,o.b,o.c)