a=int(input("enter any value between 1 and 10:"))

if(a<1 or a>10):
    raise ValueError("value must be between 1 and 10")
