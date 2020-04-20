from sys import argv

script, filename = argv

print(f"we're going to erase {filename}.")
print("if you don't want that, hit ctrl-c(^c).")
print("if you want do that ,hit Return")

input("?")

print("opening the file...")
target = open(filename, 'w+')

print("Truncating the file. goodbye!")
target.truncate()

print("now i am going tu ask you for three lines.")

line1 = input("line1 :")
line2 = input("line2 :")
line3 = input("line3 :")

print("i am going to write these to the file.")

target.write(line1+"\n"+line2+"\n"+line3+"\n")

target.seek(0,0)  #将文件游标移动到文件开头位置
target.write("good")   #会覆盖原来写的内容
print("your write is:")
print(target.read())



print("and finally, wo close it")

target.close()
