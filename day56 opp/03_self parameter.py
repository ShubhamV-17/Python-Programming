class employee:
    language="python" # this is a class attribute
    salary=1200000

    def getInfo(self):
        print (f"The language is {self.language}. The salary is {self.salary}")
    

    @staticmethod # static method is used only when we not include self in an function
    def greet():
        print("goodmorning")


harry = employee()
harry.language="javascript" # this is an instance attribute
print(harry.language,harry.salary)
harry.getInfo()
harry.greet()
