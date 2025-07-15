class Employee:
    language="Python" # this is a class attribute
    salary=1000000000

    def getinfo(self):
        print(f"the language is {self.language}, the salary is {self.salary}")
    
  
  
    @staticmethod  # this method is used to do not represent the function by self as
    def greet():
        print("good morning")



x=Employee()
x.language="c++" #  this is a object attribute
print(x.language,x.salary) 
Employee.getinfo(x)
Employee.greet()
 