import json

def storagenum(filename):
    num = input("请输入你想的数字：")
    with open(filename, 'w') as snum:
        json.dump(num,snum)

def getnumber(filename):
    with open(filename) as getnum:
        younum = json.load(getnum)
    print("您输入的数字是：%s" %younum)
filename = 'usernum.txt'
try:
    getnumber(filename)
except FileNotFoundError:
    storagenum(filename)
    getnumber(filename)
except json.decoder.JSONDecodeError:
    storagenum(filename)
    getnumber(filename)







