from turtleworld import *


def koch(t, x):
    if x < 3:
        fd(t, x)
        return
    else:
        n = x/3
        koch(t, n)
        lt(t, 60)
        koch(t, n)
        rt(t, 120)
        koch(t, n)
        lt(t,60)
        koch(t, n)


def snowflake(t, x):
    for i in range(3):
        koch(t, x)
        rt(t, 120)


t = TurtleWorld()
bob = Turtle()
bob.delay = 0.05
snowflake(bob, 200)
die(bob)

wait_for_user()
