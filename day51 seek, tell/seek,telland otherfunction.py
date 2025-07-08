# seek() in Python is used to move the file pointer to a specific position in a file.
# tell() return the postion of seek to how much the sentence is to seek at  how much character
# with open("myfile.txt","r") as f:
#     print(type(f))
#     f.seek(12)
#     print(f.tell())
#     data = f.read(26)
#     print(data)

# # tell method
# with open("myfile.txt","r") as f:
#     print(type(f))
#     f.seek(12)
#     print(f.tell())
#     data = f.read(26)
#     print(data)
#trunkate method =
with open("sample.txt","w") as f:
    f.write("hello world!")
    f.truncate(5)
with open("sample.txt","r") as f:
    print(f.read())