def print_twice(s):
    print(s)
    print(s)
def do_twice(f,i):
    f(i)
    f(i)
    a=i
do_twice(print_twice,'good')