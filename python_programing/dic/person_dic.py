vic = {'first_name' : 'wei', 'last_name' : 'wu', 'age' : 39, 'city' : 'HEFEI'}
candy = {'first_name' : 'tian', 'last_name' : 'hua', 'age' : 38, 'city' : 'HEFEI'}
rodger = {'first_name' : 'bin', 'last_name' : 'chen', 'age' : 40, 'city' : 'taicang'}

number_like = {'vic' : [14, 17, 27], 'candy' : [4, 14, 24], 'roci' : [12, 5, 18], 'kevin' :[3, 13, 15],
               'anfor' : [7, 77, 777]}
for name, number in number_like.items():
    print(name+' like',end= ' ')
    for numberget in number:
        print(numberget,end= ' ')
    print()
list_people = [vic, candy, rodger]
for people in list_people:
    print(people)