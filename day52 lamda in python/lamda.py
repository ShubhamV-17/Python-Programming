def appl(fx,value):
    return 6+fx(value)

double= lambda x:x*2
cube= lambda x:x*x*x

print(double(5))
print(cube(5))
print(appl(cube, 2))