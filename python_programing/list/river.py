river_country = {'nile': 'egypt', 'amazonRiver': 'brasil', 'changjiang River': 'china'}
for river,country in river_country.items():
    print("The %s runs through %s" %(river.title(),country.title()))

for river in river_country:
    print(river, end =' ')

print()

for country in river_country.values():
    print(country, end="    ")