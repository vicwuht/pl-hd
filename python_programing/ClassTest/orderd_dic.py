from collections import OrderedDict
word_order_dic = OrderedDict()
word_order_dic['python'] = '一种编程语言'
word_order_dic['list'] = '列表'
word_order_dic['editor'] = '编辑器'
word_order_dic['program'] = '程序'
word_order_dic['compile'] = '编译'
for word,mean in word_order_dic.items():
    print("%s means %s" %(word,mean))

print("===========================")
word_dic = {}
word_dic['python'] = '一种编程语言'
word_dic['list'] = '列表'
word_dic['editor'] = '编辑器'
word_dic['program'] = '程序'
word_dic['compile'] = '编译'
for word, mean in word_dic.items():
    print("%s means %s" % (word, mean))