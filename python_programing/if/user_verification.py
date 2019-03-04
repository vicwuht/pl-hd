#user_list = ['vic', 'candy', 'roci', 'admin', 'carolran']
user_list = []
if not user_list:
    print("We need to find some users")
else:
    for user_name in user_list:
        if user_name == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("hello "+user_name+",thank you for logging in again")


current_users = ['Vic', 'candy', 'Roci', 'admin', 'carolran']
new_users = ['jack', 'cathy', 'vic']
currnet_users_change = [name.lower() for name in current_users]
for new_user in new_users:
    if new_user.lower() in currnet_users_change:
        print(new_user+", you need to input another user name")
    else:
        print(new_user+", the user name is not used")

number_list = [i for i in range(1, 10)]
for number in number_list:
    if number == 1:
        print(str(number)+"st")
    elif number == 2 :
        print(str(number) + "nd")
    else:
        print(str(number)+"th")
