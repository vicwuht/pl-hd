def getnumber(n,step):
    numbers = []

    for i in range(0,n,step):
        print(f"At the top i is {i}")
        numbers.append(i)
        print(f"Numbers is {numbers}")

    print("The Numbers:")
    for i in numbers:
        print(i)

getnumber(10,2)
