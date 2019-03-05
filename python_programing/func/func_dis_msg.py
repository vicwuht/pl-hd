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

# def descirbe_city(city,country="CHINA"):
#     #打印国家和城市的对应，city、country为形参
#     print("%s is in %s" %(city,country))
# descirbe_city("hefei")
# descirbe_city("Tokyo","JAPAN")
# descirbe_city("fujian")

# def city_country(city,country="CHINA"):
#     #此函数接受city，countru两个参数，返回一个字符串，格式如下："city, country"
#     result = city.title()+", "+country.title()
#     return result
# print(city_country('santiago','chile'))
# print(city_country('shanghai'))
# print(city_country('tokyo','japan'))

def make_album(singer, album, number=''):
    #此函数接受歌手名、专辑名两个参数，以及数量的默认参数，返回一个字典
    if number:
        dic_album = {'singer':singer.title(), 'album':album.title(),'number':number+1}
    else:
        dic_album = {'singer': singer.title(), 'album': album.title()}
    return dic_album
while True:
    singer_name = input("请输入一下歌手姓名：")
    album_name = input("请输入专辑名：")
    sings_number = input("请输入专辑中歌曲数量：")
    print(make_album(singer_name, album_name, int(sings_number)))
    repeat = input("是否继续录入？(yes/no)\n")
    if repeat == 'no':
        print("感谢你的参与！")
        break

