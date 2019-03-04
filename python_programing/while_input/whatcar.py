# 这是第7张while循环和用户交互的练习
# car_type = input("what kind of the car you want:")
# print("Let me see if I can find you a %s" %car_type.title())
#
# eater_number = input("How many people eat?")
# if int(eater_number)>8:
#     print("no empty table")
# else:
#     print("have empty table")

# number = input("please input a int:")
# if int(number)%10 == 0:
#     print("%s is Multiple of 10"%number)
# else:
#     print("%s is not Multiple of 10"%number)

# #披萨配料
# isquit = True
# pizza_ingredients = []
# while isquit:
#     getingredient = input("please input the ingredients of pizza:")
#     if getingredient == "quit":
#         isquit = False
#     else:
#         pizza_ingredients.append(getingredient)
# print("the ingredients of pizza is:",end = " ")
# for ingredients in pizza_ingredients:
#     print(ingredients,end =" ")

# #根据年龄判断票价
# isquit = True
# while isquit:
#     getage = input("please input the age of the audience: ")
#     age = int(getage)
#     if age < 3:
#         input("you are free")
#     elif age >= 3 and age <12:
#         input("your ticket is $10")
#     elif age >=12:
#         input("your ticket is $15")

# 制作pizzla
# sandwich_orders = ['tuna', 'pastrami', 'pastrami', 'beaf', 'pastrami', 'egg']
# finished_sandwiches =[]
# while sandwich_orders:
#     sandwich_finished = sandwich_orders.pop(0)
#     finished_sandwiches.append(sandwich_finished)
#     print("I made your %s sandwich"%sandwich_finished)
# print("all sandwichs I finished are: ")
# for sandwich in finished_sandwiches:
#     print(sandwich)

#五香烟熏牛肉（pastrami）卖完了
# sandwich_orders = ['tuna', 'pastrami', 'pastrami', 'beaf', 'pastrami', 'egg']
# print("the pastrami pizzla is saled off")
# pizzla_off = 'pastrami'
# while pizzla_off in sandwich_orders:
#     sandwich_orders.remove(pizzla_off)
# print(sandwich_orders)

#调查用户向往的度假地
responses = {}
polling_active = True
while polling_active:
    name = input("What is your name?")
    place = input("If you could visit one place in the world, where would you go?")
    responses[name] = place
    repeat = input("Would you like to let another person respond? (yes/ no)")
    if repeat == "no":
        polling_active = False
for name,responses in responses.items():
    print("%s ,you want to visit %s." %(name,responses))

