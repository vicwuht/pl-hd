def show_magicians(magicians):
    #打印列表
    for name in magicians:
        print(name.title(), end=' ')

def make_great(magicians):
    # magicians1=[]
    # print("1---"+str(id(magicians[0])))
    l=len(magicians)
    for i in range(l):
        # print("all---" + str(id(magicians)))
        # print("1---" + str(id(magicians[i])))
        magicians[i] = "The Great "+magicians[i].title()
        # print("2---" + str(id(magicians[i])))
        # magicians.append("The Great "+magicians[i].title())
   # magicians = ["The Great "+ name.title() for name in magicians]
   #  for magician in magicians:
   #      # print("1---"+str(id(magician)))
   #      magician = "the grate" +magician
        # print("2---" + str(id(magician)))
    # print("2---"+str(id(magicians[0])))
    # return magicians1

magicians = ['vic', 'jackey', 'rodger', 'candy']
print("1---"+str(id(magicians[0])))
make_great(magicians)
print("2---"+str(id(magicians[0])))
show_magicians(magicians)

# show_magicians(magicians_great)