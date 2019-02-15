#邀请人吃饭的小例子
names = ['candy', 'rodger' ,'cavin' ,'sean']

for i in names:
    message = 'Hello '+ i.title() + '! Please have a dinner with me !'
    print(message)

print(names[-1].title()+ " can not have a dinner with me ")
names[-1] = 'jack'

for i in names:
    message = 'Hello '+ i.title() + '! Please have a dinner with me !'
    print(message)

print("I buyed A BIG DESK!")

names.insert(0, 'roci')
names.insert(2, 'sharp')
names.append('coke')

for name in names:
    message = 'Hello ' + name.title() + '! Please have a dinner with me !'
    print(message)

print("o! sorry ,the big desk cannot be send in time! i just can invite two guests!")


for i in range(len(names)):
    print(len(names))
    if len(names) <= 2:
        break
    popname = names.pop()
    message = 'Sorry ' + popname.title() + '! I will invite you next time !'
    print(message)

for name1 in names:
    message = 'Hello ' + name1.title() + '! Please have a dinner with me !'
    print(message)

del names[0]
del names[0]
print(names)


