class Employee:
    name="shubham"
    company="TCS"
    def Nst(self):
        print(f"the name of the Employee {self.name} and the language is {self.language}")
    
class coder: 
    language="python"
    def printlanguage(self):
        print(f"out of all the language here is your language {self.language}")

class programmer(Employee,coder):
    salary=120,000,0
    company="TCS Infotech"
    def amazingNst(self):
        print(f"the name of the company {self.company} and the salary is {self.salary}")



a = Employee()
b = programmer()


b.Nst()
b.printlanguage()
b.amazingNst()