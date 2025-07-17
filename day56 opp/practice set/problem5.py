from random import randint
class Train:

    def __init__(self,Train_no):
        self.Train_no = Train_no

    def book(self, fro, to):
        print(f"Ticket is book in Train no:{self.Train_no} from {fro} To {to}")

    def get_status(self):
        print(f"Train no:{self.Train_no} is running on Time")

    def get_fare(self, train_no, fro, to):
        print(f"Ticket fare in Train no:{self.Train_no} from {fro} to {to} is {randint(10000,15000)}")

t=Train(12599)
t.book("jabalpur","mumbai")
t.get_status()
t.get_fare(12599, "jabalpur", "mumbai")
