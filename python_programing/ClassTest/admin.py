from user import User

class Privileges():
    #权限类，只有一个属性，供Admin类调用
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(self.privileges)


class Admin(User):
    #定义一个管理员类型，继承user类
    def __init__(self,first_name,last_name,gender,age,phone_number):
        super().__init__(first_name,last_name,gender,age,phone_number)
        self.privileges = Privileges()