#map
def cube(x):
    return x*x*x

l=[1,5,6,8,3]   
newl=list(map(cube,l))


#FILTER
def filter_function(a):
    return a>4
newnewl=list(filter(filter_function,l))
print(newnewl) 