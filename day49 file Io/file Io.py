f = open('myfile.txt','r')
text = f.read( )
print(text)
f.close( )

# write mode 
f=open("myfile.txt","w")
character = f.write("I Am Beginer In Coading")
print(character)
f.close()

#append mode
f=open("myfile.txt","a")
alphabats=f.write("yes you can do it")
print(alphabats)
f.close()

# the with statement
with open("myfile.txt","r") as f:
    print(f.read())