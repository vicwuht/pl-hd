#喜欢的旅游地的小例子

travel_places = ['Shanghai', 'chengdu', 'shenzhen', 'yunnan', 'haerbin']
print("原始列表：")
print(travel_places)
print("临时排序列表：")
print(sorted(travel_places))   #可以看到是区分大小写的
print("此时的列表：")
print(travel_places)
print("临时反向排序列表：")
print(sorted(travel_places,reverse=True))
print("此时的列表：")
print(travel_places)
print("反转列表：")
travel_places.reverse()
print(travel_places)
print("恢复反转：")
travel_places.reverse()
print(travel_places)
print("修改列表，按照字母顺序排列")
travel_places.sort()
print(travel_places)
print("修改列表，按照字母反向顺序排列")
travel_places.sort(reverse=True)
print(travel_places)

