import random
n=random.randint(1,100)
a= -1
guesses=0
while(a!=n):
    guesses+=1
    a=int(input("Guess The Number:"))
    if (a>n):
        print("lower number please")
    else:
        print("higher number please")

print(f"you have guesses the number correctly in {guesses} 6attempt")
