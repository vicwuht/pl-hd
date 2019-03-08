from die import Die
mydie = Die()
mydie.size =20
print("抛一个%s面的筛子10次：" %mydie.size)
for i in range(0,10):
    print("第%s次" %i)
    mydie.roll_die()
