from TurtleWorld import *
import math

# world = TurtleWorld()
# bob = Turtle()
# bob.delay = 0.01
# #封装
# print(bob)
# fd(bob,100)
# lt(bob)
# pu(bob)
# fd(bob,100)

#给函数添加参数的过程称为泛化
# def square(t, length):
#     for i in range(4):
#         fd(t, length)
#         lt(t)
#
#
# square(bob, 120)


def polygon(t, length, n):
    for i in range(n):
        fd(t, length)
        lt(t, 360/n)


# polygon(bob, length=120, n=5)
# #调用函数时可以加上行参名称


#五规画圆，考虑到圆的主要参数就是半径，n属于内部细节，不适合作为接口的参数传入。
def circle(t, r):
    circumference = 2 * math.pi * r
    n = 360
    length = circumference / n
    polygon(t, length, n)


#circle(bob, 120)


#画弧，考虑运用画圆进行重构
# def arc(t, r, angle):
#     arc_length = 2 * math.pi * r *angle / 360  #弧长
#     n = int(arc_length / 3) + 1    #要画的线段数量，按照长为3划分
#     step_length = arc_length / n
#     step_angle = float(angle) /n #单步的角度
#
#     for i in range(n):
#         fd(t, step_length)
#         lt(t,step_angle)


#考虑到arc和polygon最后的代码类似，我们抽取出来形成polyline，达到重构,polyline也可以用来重构polygen

def polyline(t, n, length, angle):
    for i in range(n):
        fd(t, length)
        lt(t, angle)


def arc(t, r, angle):
    arc_length = 2 * math.pi * r *angle / 360  #弧长
    n = int(arc_length / 3) + 1    #要画的线段数量，按照长为3划分
    step_length = arc_length / n
    step_angle = float(angle) /n #单步的角度
    polyline(t, n, step_length, step_angle)
#arc可以用来重构circle


#下面是我的实现防范
# def arc(t, r, angle):
#     n=360
#     for i in range(angle):
#         length = math.pi* 2 * r / n
#         fd(t, length)
#         lt(t, 360/n)


# arc(bob, 100, 180)


# wait_for_user()