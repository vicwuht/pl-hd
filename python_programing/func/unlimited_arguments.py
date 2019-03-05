# def sandwich_material(*material):
#     #获取不限数量的元素并放到列表中
#     print(material)
#
# sandwich_material('1', '2', '3')
# sandwich_material('1', '2', '3','4')

# def build_profile(first, last, **user_info):
#     """创建一个字典，其中包含我们知道的有关用户的一切"""
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile
# user_profile = build_profile('albert', 'einstein',location='princeton',
#                              field='physics',gender='male')
# print(user_profile)
import car
car = car.make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)