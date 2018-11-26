

"""验证费马定理   
   对于任何大于2得n，  不存在整数 adc满足  a的n次方+b的n次方=c的n次方
"""


def check_fermat(a, b, c, n):
    an = pow(a, n)
    bn = pow(b, n)
    cn = pow(c, n)
    if n > 2 and an + bn == cn:
            print("天哪，费马弄错了！")
    else:
        print("不，那样不行")


inputa = int(input('请输入整数a:\n'))
inputb = int(input('请输入整数b:\n'))
inputc = int(input('请输入整数c:\n'))
inputn = int(input('请输入整数n:\n'))
check_fermat(inputa, inputb, inputc, inputn)




