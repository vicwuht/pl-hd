import unicodedata
s = 'banana'

#首字母大写
s1 = s.capitalize()
print(s1)

#都小写   casefolde和lower的区别在于lower只支持ASCII 也就是 'A-Z'有效。
# 汉语 & 英语环境下面，继续用 lower()没问题；要处理其它语言且存在大小写情况的时候再用casefold()
s2 = s1.casefold()
s3 = s1.lower()
print(s2)
print(s3)

#str.center（width [，fillchar ] ）
# 返回以现有字符串为中心，以指定字符填充前后的字符串。如果宽度小于现在字符串长度，则返回原字符串。
s4=s.center(10, 'a')
print(s4)

#count（sub [，start [，end ] ] ） 字符串内sub出现的非重叠的次数

#encode(encoding='UTF-8',errors='strict')  以指定的编码方式返回byte类型对象，编码
str = "中文"
print(str.encode('utf-8'))
print(str.encode('gb2312'))


#endswith(suffix[, start[, end]])  字符串是否以suffix结尾  ，可以指定查找的开始与结束为止,位置和切片一样，含前不含后
print(s.endswith('a'))
print(s.endswith('a', 0, 3))

#expandtabs(tabsize) 方法把字符串中的 tab 符号('\t')转为空格，tab 符号('\t')默认的空格数是 8，可以指定tabsize。
str1 = "this is\tstring example....wow!!!";
print("Original string: " + str1);
print("Defualt exapanded tab: " +  str1.expandtabs());
print("Double exapanded tab: " +  str1.expandtabs(16));

#find(sub [，start [，end ] ])  查找sub，返回最低索引
print(s.find('a'))
print(s.find('a', 2))

#format(* args，** kwargs)  类似于%显示
print("My name is %s and weight is %d kg!" % ('Zara', 21) )
print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
print("网站名：{}, 地址 {}".format("菜鸟教程", "www.runoob.com"))
# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))
# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的
#也可以用来表示数字
# ^, <, > 分别是居中、左对齐、右对齐，后面带宽度， : 号后面带填充的字符，只能是一个字符，不指定则默认是用空格填充。
# + 表示在正数前显示 +，负数前显示 -；  （空格）表示在正数前加空格
# b、d、o、x 分别是二进制、十进制、八进制、十六进制。
print("{:.2f}".format(3.1415926))
#{}可以转意
print ("{} 对应的位置是 {{0}}".format("runoob"))

class Default(dict):
    def __missing__(self, key):
         return key
print("{name} was born in {country}".format_map(Default(name='Guido')))
#print("{name} was born in {get}".format(name='Guido'))
#否则format少个参数会不执行

#index( sub [，start [，end ] ] )  类似与find，返回索引，如果找不到，返回-1
print(s1.find('c'))

#isalnum()  方法检测字符串是否由字母和数字组成。
strnum = '123456ab'
strnum1 = '.1234'
strnum2 = '801014'
print(strnum.isalnum())
print(strnum1.isalnum())

#isalpha() 方法检测字符串是否只由字母组成。
print(strnum.isalpha())

# isasscii()  字符串是否是asscii码
# Return true if the string is empty or all characters in the string are ASCII, false otherwise.
# ASCII characters have code points in the range U+0000-U+007F. 3.7新特性

#isdecimal() 方法检查字符串是否只包含十进制字符。这种方法只存在于unicode对象。
print(strnum.isdecimal())
print(strnum2.isdecimal())

#isdigit() 方法检测字符串是否只由数字组成。
print(strnum.isdigit())
print(strnum2.isdigit())

#isnumeric() 方法检测字符串是否只由数字组成。这种方法是只针对unicode对象。
schina = '四'
print(schina.isnumeric())
print(unicodedata.numeric('四'))
# isdigit()
# True: Unicode数字，byte数字（单字节），全角数字（双字节），罗马数字
# False: 汉字数字
# Error: 无
#
# isdecimal()
# True: Unicode数字，，全角数字（双字节）
# False: 罗马数字，汉字数字
# Error: byte数字（单字节）
#
# isnumeric()
# True: Unicode数字，全角数字（双字节），罗马数字，汉字数字
# False: 无
# Error: byte数字（单字节）







