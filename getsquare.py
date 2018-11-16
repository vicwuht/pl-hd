#计算给定一个数的平方根，运用的是牛顿方法
#  y=(x+a/x)/2  当y=x时，x就是a的平方根
#注意浮点数的比较


def square_root(a):
    x = 4
    while True:
        y = (x + a/x) / 2
        if abs(y - x) < 0.00000001:
            break
        x = y
    return y


asqure = int(input("请输入一个整数："))
print(square_root(asqure))
