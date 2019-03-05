class Restaurant():
    """这个宾馆的类"""

    def __init__(self,restaurant_name,cuisine_type):
        """宾馆的两个属性：宾馆名和菜系"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """打印宾馆的两个属性"""
        print("饭店的名称是%s,菜系是%s" %(self.restaurant_name,self.cuisine_type))

    def open_restaurant(self):
        """打印宾馆正在营业的信息"""
        print("餐馆正在营业")

res = Restaurant("全聚德","北京菜")
print(res.restaurant_name)
print(res.cuisine_type)
res.describe_restaurant()
res.open_restaurant()
res2 = Restaurant("狗不理", "包子")
res3 = Restaurant("同庆楼", "徽菜")
res2.describe_restaurant()
res2.open_restaurant()
res3.describe_restaurant()
res3.open_restaurant()
