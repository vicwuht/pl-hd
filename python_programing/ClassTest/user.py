class user():
    """定义一个用户类"""
    def __init__(self,first_name,last_name,gender,age,phone_number):
        """初始化，姓名，性别，年龄，电话"""
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.phone_number = phone_number

    def describe_user(self):
        """打印用户信息"""
        print(self.first_name+' '+self.last_name)
        print("---"+self.gender+' '+self.age+' '+self.phone_number)

    def greet_user(self):
        print("hello! %s ,nice to meet you!" %self.first_name)

user_vic = user('wei', 'wu', 'male', '39', '13965129060')
user_vic.describe_user()
user_vic.greet_user()

