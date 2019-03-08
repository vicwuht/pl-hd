class Restaurant():
    """这个宾馆的类"""

    def __init__(self,restaurant_name,cuisine_type):
        """宾馆的两个属性：宾馆名和菜系"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """打印宾馆的两个属性"""
        print("饭店的名称是%s,菜系是%s" %(self.restaurant_name,self.cuisine_type))

    def open_restaurant(self):
        """打印宾馆正在营业的信息"""
        print("餐馆正在营业")

    def number_served_add(self, n):
        self.number_served += n

    def  number_served(self):
        return self.number_served

    def increment_number_served(self,n):
        self.number_served += n
        return self.number_served

#冰激凌小店
class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ['milk', 'chocolate', 'strawberry']

    def show_flavors(self):
        print(self.flavors)


# res = Restaurant("全聚德","北京菜")
# print(res.restaurant_name)
# print(res.cuisine_type)
# res.describe_restaurant()
# res.open_restaurant()
# res.number_served_add(5)
# res.increment_number_served(20)
# print("全聚德今天有%s人就餐" %res.number_served)
# res2 = Restaurant("狗不理", "包子")
# res3 = Restaurant("同庆楼", "徽菜")
# res2.describe_restaurant()
# res2.open_restaurant()
# res3.describe_restaurant()
# res3.open_restaurant()


