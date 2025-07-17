class programmer:
    company="microsoft"
    def __init__(self,name,language,salary,pincode):
        self.name = name
        self.language = language
        self.salary = salary
        self.pincode = pincode

p=programmer("shubham","python",1200000,482004)
print(p.name,p.language,p.salary,p.pincode,end="")