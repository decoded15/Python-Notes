class Employee:
    name='Dibyansh' #class attribute
    salary=250000
    language='Py'

    def getInfo(self): #self is the object jis par ye method run ho rha hai
        print(f'The language is {self.language} and the salary is {self.salary} ')
    def greet(self):
        print(f'Good Morning {self.name}')
    
    @staticmethod #if static method is mentioned then the function doesnt require any self parameter
    # Sometimes we need a function that does not use the self-parameter. 
    def Hello():
        print('Hello..!!')

ommi=Employee() #ommi is object of class Employee
print(ommi.name,ommi.salary) #object.attribute
ommi.getInfo() #Employee.getInfo(ommi)
ommi.greet()
ommi.Hello()

duni=Employee()
duni.age=15 #age is object/instance attribute
print(duni.name,duni.age,duni.language) #name and language are class attributes
#age is object attribute as it doesnt belong to the class Employee

duni=Employee()
duni.name='Duni' #Instance attributes, take preference over class attributes during assignment & retrieval.
print(duni.name,duni.language) 
'''
When looking up for harry.attribute it checks for the following:
1) Is attribute present in object?
2) Is attribute present in class?
'''

#doubt below..!!
# class student():
#     name='Ommi'
#     age=15

#     def __init__(self,name,age): #dunder method is automatically called
#         self.name=name
#         self.age=age
#         print('I am creating an object')
# a=student() 
# a.sub='Chem'
# print(f'name is {a.name} and age is {a.age} and subject is {a.sub}')
# # rohan=student()
# ommi=student('Dibyansh',15)

class Employee:
    def __init__(self, name):
        self.name=name
    
harry = Employee("Harry")
print(harry.name)
