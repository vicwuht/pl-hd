filenames = ["dogs.txt","cats.txt"]
for filename in filenames:
    filename = "txt_files\\" + filename
    print(filename)
    try:
        with open(filename) as getfile:
            lines = getfile.readlines()
            print(lines)
    except FileNotFoundError:
        # print("文件读取失败，请确认文件位置")
        # break
        pass
    else:
        for line in lines:
            print(line.rstrip())
