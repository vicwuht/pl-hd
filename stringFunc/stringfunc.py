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
s4=s.center(10,'a')
print(s4)

#count（sub [，start [，end ] ] ） 字符串内sub出现的非重叠的次数

