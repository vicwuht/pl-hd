from name_function import get_formatted_name
print("please enter q at any time to quit:")
while True:
    first = input("please input your first name:")
    if first == 'q':
        break
    last = input("please input your last name:")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first.title(), last.title())
    print("\tNeatly formatted name: %s." %formatted_name)