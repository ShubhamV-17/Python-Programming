with open("myfile.txt","r") as f:
    print(type(f))
    f.seek(12)
    print(f.tell())
    data = f.read(26)
    print(data)