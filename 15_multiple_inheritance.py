class Employee:
    company='ITC'
    name='Dibyansh'
    salary=20555
    def show(self):
        print(f'The name is {self.name} and the salary is {self.salary}')

class Coder:
    language='python'
    def printlang(self):
        print(f'out of all the languages here is your language : {self.language}')

class programmer(Employee,Coder):  #inheritance
    company='ITC Infotech'
    def showLanguage(self):
        print(f'The language is {self.language}')

a=Employee()
b=programmer()
b.show()
b.showLanguage()
b.printlang()