class User():
    """定义一个用户类"""
    def __init__(self,first_name,last_name,gender,age,phone_number):
        """初始化，姓名，性别，年龄，电话"""
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.phone_number = phone_number
        self.login_attempts = 0

    def describe_user(self):
        """打印用户信息"""
        print(self.first_name+' '+self.last_name)
        print("---"+self.gender+' '+self.age+' '+self.phone_number)

    def greet_user(self):
        print("hello! %s ,nice to meet you!" %self.first_name)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0





# user_vic = User('wei', 'wu', 'male', '39', '13965129060')
# user_vic.describe_user()
# user_vic.greet_user()
# user_vic.increment_login_attempts()
# user_vic.increment_login_attempts()
# user_vic.increment_login_attempts()
# print(user_vic.login_attempts)
# user_vic.reset_login_attempts()
# print(user_vic.login_attempts)
# admin = Admin('wei', 'wu', 'male', '39', '13965129060')
# admin.privileges.show_privileges()
