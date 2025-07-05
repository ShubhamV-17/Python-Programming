x=4
print(x)

def hello():
    x=5
    y=1# local variable
    print(f"the local x is {x}")
    print("hello happy?sarkar")
print(f"the global x is {x}")
hello()
print(f"the global x is {x}") 


# how we change the global x
x=4
print(x)

def hello():
    global x
    x=5
    y=1# local variable

hello()
print(x)