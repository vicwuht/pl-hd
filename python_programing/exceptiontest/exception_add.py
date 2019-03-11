#对加法类型转换进行异常处理

# #1、用ValueError
# try:
#     a = int(input("请输入一个加数："))
#     b = int(input("请输入另一个加数"))
# except ValueError:
#     print("您输入的不是数字")
# else:
#     c = a + b
#     print("两个数相加的结果是：%s" %str(c))

#2、用TypeError是无法实现的，要区分TypeError和ValueError，int()函数本来就可以接受字符串类型，不存在TypeError。
#而是由于str值不在可转换范围，而引发ValueError
a = input("请输入一个加数：")
b = input("请输入另一个加数:")
print(type(a))
print(type(b))
try:
    c = sum(int(a), int(b))
except TypeError:
    print("您输入的不是数字")
else:
    print("两个数相加的结果是：%s" %str(c))

