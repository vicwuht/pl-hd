filenames = ["dogs.txt","cats.txt"]
for filename in filenames:
    filename = "txt_files\\" + filename
    try:
        with open(filename) as getfile:
            lines = getfile.readline()
    except FileNotFoundError:
        print("文件读取失败，请确认文件位置")
        break
    else:
        for line in lines:
            print(line)
