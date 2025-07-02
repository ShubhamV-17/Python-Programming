# next program of multiplication table
name=input("enter your name:")
num=len(name)
print(f"\n lenth of name {name} is {num}")
print(f"\n {num} multiplication table : \n ")
for i in range (1, 11):
     print(f"{num}X{i}={num*i}")