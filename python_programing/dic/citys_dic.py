hefei_details = {'country' : 'china', 'population' : 50000000, 'fact' : 'badu'}
tokyo_details = {'country' : 'japan', 'population' : 60000000, 'fact' : 'popular'}
newyork_deatils = {'country' : 'amarican', 'population' : 10000000, 'fact' : 'big'}
citys = {'hefei': hefei_details, 'tokyo': tokyo_details, 'newyork' : newyork_deatils}
for name,citydetails in citys.items():
    print("%s:"%name)
    for keys,details in citydetails.items():
            print("     %s : %s" %(keys,details))