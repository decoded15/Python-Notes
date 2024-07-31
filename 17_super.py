class Employee:
    def __init__(self):
        print('Constructor of class Employee..!!')
    a=1

class programmer(Employee):
    def __init__(self):
        print('Constructor of class programmer..!!')
    b=2

class manager(programmer):
    def __init__(self):
        super().__init__() #calls the constructor of base class
        print('Constructor of class manager..!!')
    c=3

# o=Employee()
# print(o.a)
# print(o.b) #this will show error as b attribute is not present in Employee
# o=programmer()
# print(o.a,o.b)

o=manager()
print(o.a,o.b,o.c)