marks = [12,54,96,32,7,1,99]
for index, mark in enumerate(marks):
    print(mark)
    if(index==2):
        print("shubham,awesome")
        

# another example
fruits=["apple","banana","mango","orange"]
for index, fruit in enumerate(fruits,start=1):
    print(index,fruit)
    if(index==2):
        print("the king of fruit is mango")
