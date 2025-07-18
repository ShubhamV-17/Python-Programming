class Employee:
    def __init__(self):
        print("constructor of Employee")
    a=1

class programmer(Employee):
    def __init__(self):
        print("constructor of programmer")
    b=2

class manager(programmer):
    def __init__(self):
        super().__init__
        print("constructor of manager")
    c=3

o=Employee()
print(o.a)
#print(o.b) #shoes an error as there is no b attribute in Employee classs

o=programmer()
print(o.a,o.b)

o=manager()
print(o.a,o.b, o.c)