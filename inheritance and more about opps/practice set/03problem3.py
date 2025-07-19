class Employee:
    salary=1200000
    increment=5
    
    @property
    def salaryafterincrement(self):
        return(self.salary * (self.increment/100))

    @salaryafterincrement.setter
    def salaryafterincrement(self, newsalary):
        self.increment = ((newsalary / self.salary) - 1) * 100

x = Employee()
# print(x.salaryafterincrement)
x.salaryafterincrement=20
print(x.increment)