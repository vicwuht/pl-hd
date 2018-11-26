#数学家尼瓦瑟·拉马努金的pi计算方法


import math


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)


def estimate_pi():
    k = 0
    result = 0

    # den = factorial(k) ** 4 * 396 ** (4 * k)
    # print(den)
    while True:
        aa = factorial(4 * k) * (1103 + 26390 * k) / ((factorial(k) ** 4) * 396 ** (4 * k))
        result = result + aa
        k = k + 1
        if aa < 1e-15:
            break

    p = 2*math.sqrt(2)*result/9801
    return 1/p


print(estimate_pi())
print(math.pi)