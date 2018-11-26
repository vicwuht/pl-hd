"""函数conpare用来比较xy的大小"""


def compare(x, y):
    """
    compare函数比较xy大小
    :param x:
    :param y:
    :return: 1，0，-1
    """
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1


# x = input('请输入X值：\n')
# y = input('请输入Y值：\n')
# print(compare(x, y))
def is_between(x, y, z):
    return (x <= y) and (y <= z)


print(is_between(1, 5, 10))
print(is_between(5, 5, 10))
print(is_between(1, 5, 5))
print(is_between(5, 5, 5))
print(is_between(6, 5, 10))

