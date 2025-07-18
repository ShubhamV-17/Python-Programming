class Employee:
    company="TCS"
    def Nst(self):
        print(f"the name of the Employee {self.name} and the salary is {self.salary}")
    
# class programmer:
#     company="TCS Infotech"
#     def Nst(self):
#         print(f"the name is {self.name} and the salary is {self.salary}")
    
#     def showNst(self):
#         print(f"the name is {self.name} and the salary is {self.salary}")

class programmer(Employee):
    company="TCS Infotech"
    def Nst(self:
        print(f"the name of the Employee {self.name} and the salary is {self.salary}"))



a = Employee()
b = programmer()
print(a.company , b.company)