class Employee:
    a=1

class programmer(Employee):
    b=2

class manager(programmer):
    c=3

o=Employee()
print(o.a)
#print(o.b) #shoes an error as there is no b attribute in Employee classs

o=programmer()
print(o.a,o.b)

o=manager()
print(o.a,o.b, o.c)