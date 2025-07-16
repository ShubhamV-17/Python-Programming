'''
question 3

* * * *
* * *
* *
*
'''

# solution
def pattern(n):
    if (n==0):
        return nothing
    print("* "*n)
    pattern(n-1)
pattern(4)