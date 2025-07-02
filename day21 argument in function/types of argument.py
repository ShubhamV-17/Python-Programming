# default arguments
#in this case the value be taken from the function defination
def avg(a=10,b=20):
    print(f"average is {(a+b)/2}")
avg()

# in second case
# in this case they ignore the function defination and take the valur of function call
def avg(a=10,b=20):
    print(f"average is {(a+b)/2}")
avg(1,5)


#required arguments
def name(fname ,mname="jhon",lname="whatson"):
    print("hello",fname,mname,lname)
name("james","bond","shubham")
