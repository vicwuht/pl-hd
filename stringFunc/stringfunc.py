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

