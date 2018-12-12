import unicodedata
s = 'banana'
ss = 'it is my banana'

#首字母大写  capitalize()
s1 = s.capitalize()
print(s1)
#字符串内所有单词首字母大写  title()
print(ss.title())


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

#find(sub [, start [, end ] ])  查找sub，返回最低索引，找不到返回-1
#rfind(sub[, start[, end]])  返回最高索引
print('find+++++++++++++++')
print(s.find('a'))
print(s.find('c'))
print(s.find('a', 2))
print(s.rfind('a', 2))

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

#index( sub [, start [, end ] ] ) 类似与find，返回索引，如果找不到会抛出异常，这一点区别于find
#rindex( sub [, start [, end ] ] ) 返回最高索引
print('index+++++++++++++')
print(s.index('a'))
print(s.rindex('a'))

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
# True: Unicode数字，全角数字（双字节）
# False: 罗马数字，汉字数字
# Error: byte数字（单字节）
#
# isnumeric()
# True: Unicode数字，全角数字（双字节），罗马数字，汉字数字
# False: 无
# Error: byte数字（单字节）

#isidentifier()  判断字符串是否满足标识符定义规则
#标识符定义规则为：只能是字母或下划线开头、不能包含除数字、字母和下划线以外的任意字符。
#isspace()   判断字符串是否是空白字符（空格，tab，enter）
#isprintable()  判断字符串是否是可答应字符串（制表符、换行都是不可打印字符串）
print(' '.isspace())
print('\t'.isspace())
print('\n'.isspace())
print(''.isspace())
print('aa bb'.isspace())
print(' '.isprintable())
print('\t'.isprintable())
print('\n'.isprintable())
print(''.isprintable())
print('aa\nbb'.isprintable())
print(' '.isidentifier())
print('\t'.isidentifier())
print('\n'.isidentifier())
print(''.isidentifier())
print('aa\nbb'.isidentifier())

#islower()  判断字符串是否为小写
#isupper()  判断字符串是否为大写
print('good'.islower())
print('Good'.islower())
print('GOOD'.isupper())
print('Good'.isupper())

#join()   将可迭代对象(iterable)中的字符串使用S连接起来。  iterable:string list dict tuple set
l = 'python'
print('-'.join(l))

#ljust(width[,fillchar])  左对齐，并用fillchar填充左对齐后多余的width
#rjust(width[,fillchar])  右对齐，从左侧填充
print('just+++++++++++++++')
print(l.ljust(20, 'x'))
print(l.rjust(20, 'x'))

#strip(char)  从两端剥离字符
print('www.baidu.comccc'.strip('wcm'))
#lstrip(char)从左侧剥离
print('commmwww.baidu.com'.lstrip('wcm'))
#rstrip(char) 从右侧剥离
print('commmwww.baidu.com'.rstrip('wcm'))

#str.maketrans() 方法用于给 translate() 方法创建字符映射转换表。是静态行数
#可以只接受一个参数，此时这个参数是个字典类型
#对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串，表示转换的目标。两个字符串的长度必须相同，为一一对应的关系。
#在Python3中可以有第三个参数，表示要删除的字符，也是字符串。
intab = 'aeiou'
outtab = '12345'
deltab = 'thw'

trantab1 = str.maketrans(intab, outtab)
trantab2 = str.maketrans(intab, outtab, deltab)

test = 'this is a string example ... wow!'
print(test.translate(trantab1))
print(test.translate(trantab2))

#partition(sep) 用第一个sep分隔字符串，返回一个含三元素的元祖，第一个元素是sep前部分，第二个元素是sep，第三个元素是sep后部分；
# 如果没有找到sep，则第一个元素是字符串本身，后两个元素是空字符串
# rpartition(sep) 用最后一个sep分隔字符串
#如果没有找到sep，则前两个元素是空字符串，最后一个元素是字符串本身
str_part = "www.runoob.com"
print(str_part.partition("."))
print(str_part.partition("-"))
print(str_part.rpartition("."))
print(str_part.rpartition("-"))


#replace(old,new,count) 用new替换old，如果有count则替换count次
str_rep = 'this is my string,this is my string'
old = 'is'
new = 'was'
print(str_rep.replace(old, new))
print(str_rep.replace(old, new, 2))



