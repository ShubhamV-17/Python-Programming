class twovector:
    def __init__(self,i,j):
        self.i=i
        self.j=j

    def shows (self):
        print(f"the vector is {self.i}i + {self.j}j ")

class threevector(twovector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k

    def show (self):
        print(f"the vector is {self.i}i + {self.j}j + {self.k}k")

x=twovector(1,2)
x.shows()
y=threevector(1,8,6)
y.show()