vic = {'first_name' : 'wei', 'last_name' : 'wu', 'age' : 39, 'city' : 'HEFEI'}
print(vic)

number_like = {'vic' : 14, 'candy' : 4, 'roci' : 8, 'kevin' :29, 'anfor' : 7}
print(number_like)
for name, number in number_like.items():
    print(name + ' like ' + str(number))