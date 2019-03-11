filename = 'txt_files\learning_python.txt'

#第一种方法，读取所有文件内容一把打印
# with open(filename) as getfile:
#     contents = getfile.read()
#     for i in range(0,3):
#         print(contents)

#第二种方法，读取行然后打印
# for i in range(0,3):
#     with open(filename) as getfile:
#         for line in getfile:
#             print(line.rstrip())

# #第三种方法，读取行然后存到列表中打印
# with open(filename) as getfile:
#     lines = getfile.readlines()
# for i in range(0,3):
#     for line in lines:
#         print(line.rstrip())

#将Python替换成C，采用replace
with open(filename) as getfile:
    lines = getfile.readlines()
for line in lines:
    print(line.rstrip().replace('Python', 'C'))


