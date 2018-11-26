from math import *
from turtleworld import *
from flower import move
# fd(bob, 50)
# lt(bob, 120.0)
# fd(bob, 50)
# lt(bob, 120.0)
# fd(bob, 50)


def draw_triangle(t, angle, r):
    """
    画等边三角形
    :param t: 乌龟名字
    :param angle:等边三角形顶角的角度
    :param r: 等边三角形的腰长
    """
    b_angle = (180-angle)/2
    t_angle = 180 - b_angle
    b_length = r*cos(radians(b_angle))*2
    fd(t, r)
    lt(t, t_angle)
    fd(t, b_length)
    lt(t, t_angle)
    fd(t, r)


def draw_pie(t, n, r):
    d_angle = 360 / n
    start_angle = d_angle / 2
    lt(t, start_angle)
    for i in range(n):
        draw_triangle(t, d_angle, r)
        lt(t, 180)
    rt(t, start_angle)


world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

move(bob, -100)
draw_pie(bob, 5, 50)

move(bob, 100)
draw_pie(bob, 6, 50)

move(bob, 100)
draw_pie(bob, 7, 50)

die(bob)

wait_for_user()

