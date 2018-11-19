for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n,'=', x, '*', int(n/x))
            break
    else:    #在break之后，else后的语句不会被执行
        print(n,'is a prime number')
