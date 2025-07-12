import random
'''
-1 for snake
1 for water
0 for gun
'''
computer = random.choice([-1,0,1])
mechoice = input("enter your choice:")
meDict ={"s":-1,"w":1,"g":0}
reverseDict={-1: "snake",1:"water",0:"gun"}
me=meDict[mechoice]

# By now we have two number (variables) ,you and computer
print(f"me choose{reverseDict[me]} \n computer choice {reverseDict[computer]}")

if (computer == me):
    print("draw")

if(computer==-1 and me==1):
    print ("you win")
elif(computer==1 and me==0):
    print ("you win")
elif(computer==0 and me==-1):
    print ("you lose")
elif(computer==1 and me==-1):
    print ("you lose")
elif(computer==-1 and me==0):
    print ("you win")
elif(computer==0 and me==1):
    print ("you lose")
else:
    print("something went wrong !")
