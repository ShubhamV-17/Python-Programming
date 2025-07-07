with open("maths.txt") as f:
    i=0
    while True:
        i=i+1
        line = f.readline()
        if not line:
            break
        parts = line.split(",")
        if len(parts) >= 3:
            m1 = parts[0]
            m2 = parts[1]
            m3 = parts[2]

            print(f"marks of student {i} in maths is: {m1}")
            print(f"marks of student {i} in science is: {m2}")
            print(f"marks of student {i} in sst is: {m3}")
            print(line)
        else:
            print("Line does not contain enough data.")
