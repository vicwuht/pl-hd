from random import randint
class Die():
    def __init__(self):
        self.size = 6

    def roll_die(self):
        x = randint(1,self.size)
        print(x)