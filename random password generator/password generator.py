import random
chart = "abcdefghijklmnopqrstwxyz@#*$%^()"

length = int(input("enter length:"))
password = ""


for i in range(length):
    password += random.choice(chart)
print(password)
