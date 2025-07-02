a=int(input("enter the number :"))
print(f"multiplicationtable of {a} is:")
try:
    for i in range(1,11):
         print(f"{a}X{i}={a*i}")
except Exception as e:
     print(e)   

