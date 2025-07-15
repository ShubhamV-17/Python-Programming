class calculator:
    def __init__(self,n):
        self.n=n
    def square(self):
        print(f"the square is {self.n*self.n}")

    def cube(self):
        print(f"the cube is {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"the square root is {self.n ** 0.5}")




num = int(input("enter your number:"))
a = calculator(num)
a.square()
a.cube()
a.squareroot()