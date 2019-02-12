names = ['candy', 'rodger' ,'cavin' ,'sean']

for i in names:
    message = 'Hello '+ i.title() + '! Please have a dinner with me !'
    print(message)

print(names[-1].title()+ " can not have a dinner with me ")
names[-1] = 'jack'

for i in names:
    message = 'Hello '+ i.title() + '! Please have a dinner with me !'
    print(message)

