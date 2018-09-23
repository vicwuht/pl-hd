"""判断是否可以组成三角形"""


def is_triangle(a, b, c):
    if max(a, b, c) <= a+b+c-max(a, b, c):
        print("YES")
    else:
        print("NO")


inputa = int(input('请输入整数a:\n'))
inputb = int(input('请输入整数b:\n'))
inputc = int(input('请输入整数c:\n'))
is_triangle(inputa, inputb, inputc)