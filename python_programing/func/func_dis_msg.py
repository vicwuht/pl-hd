# #8.1练习，编写一个函数display_message(),打印一个句子，指出在学习什么并调用
# def display_message():
#     #次函数打印一句话，指出在学习什么
#     print("I am learnging Python")
#
# display_message()

# def favorite_book(title):
#     #打印最喜欢的书，形参为书名
#     print("on of my favorite books is %s" %title.title())
#
# favorite_book("wei chen")

# def make_shirt(size=10, type="I Love Python"):
#     #打印T恤的尺码和样式，形参为尺码、样式
#         print("the shirt size is %s, type is %s" %(size,type))
# make_shirt(5,"nice")
# make_shirt(size=3,type="good")
# make_shirt(type="good",size=6)
# make_shirt()

def descirbe_city(city,country="CHINA"):
    #打印国家和城市的对应，city、country为形参
    print("%s is in %s" %(city,country))
descirbe_city("hefei")
descirbe_city("Tokyo","JAPAN")
descirbe_city("fujian")

