# username = input("please input username:")
# filename = 'txt_files\\username.txt'
# with open(filename, 'w') as username_file:
#     username_file.write(username)

filename = 'txt_files\\guest_book.txt'
while True:
    username = input("please input username:")
    if username == 'q':
        break
    print("hello! %s" %username)
    with open(filename, 'a') as guest_file:
        guest_file.write(username+'\n')