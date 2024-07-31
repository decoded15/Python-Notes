class Employee:
    company='ITC'
    def show(self):
        print(f'The name is {self.name} and the salary is {self.salary}')

# class programmer:
#     company='ITC Infotech'
#     def show(self):
#         print(f'The name is {self.name} and the salary is {self.salary}')

#     def showLanguage(self):
#         print(f'The language is {self.language}')

class programmer(Employee):  #inheritance
    company='ITC Infotech'
    def showLanguage(self):
        print(f'The language is {self.language}')

a=Employee()
b=programmer()
print(a.company)
print(b.company)