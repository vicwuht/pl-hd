f = open('ex22.txt', 'a+')
f.write("\nline4")
f.seek(0)
print("ex22 is " + f.read())
f.close
