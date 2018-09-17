from TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01
# print(bob)
# fd(bob,100)
# lt(bob)
# pu(bob)
# fd(bob,100)


# def square(t, length):
#     for i in range(4):
#         fd(t, length)
#         lt(t)
#
#
# square(bob, 120)


# def polygon(t, length, n):
#     for i in range(n):
#         fd(t, length)
#         lt(t, 360/n)
#
#
# polygon(bob, 120, 5)


def circle(t, r):
    n=100
    for i in range(n):
        length = math.pi* 2 * r / n
        fd(t, length)
        lt(t, 360/n)


circle(bob, 100)


wait_for_user()