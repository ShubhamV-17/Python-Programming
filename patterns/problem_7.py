# #question 7


n = 5
alph=65
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    letters =" ".join([chr(65+j)for j in range(i)])
    print(letters)



