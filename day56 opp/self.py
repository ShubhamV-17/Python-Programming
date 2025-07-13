class Employee:
    language="Python" # this is a class attribute
    salary=1000000000

    def info(self):
        print(f"the language is{self.language}. the salary is {self.salary}")

x=Employee()
x.language="c++" #  this is a object attribute
print(x.language,x.salary) 
Employee.info(x)