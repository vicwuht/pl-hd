def find(word, letter, start):
    newword = word[start-1:]
    index = 0
    while index < len(newword):
        if newword[index] == letter:
            newindex = index+start-1
            return newindex
        index = index + 1
    return -1


def countget(word, letter):
    count = 0
    for a in word:
        if a == letter:
            count = count + 1
    return count


def countgetwithfind(word, letter):
    count = 0
    index = find(word,letter,1)
    while index >= 0:
        print(index)
        count =count + 1
        word = word[index+1:]
        print(word)
        index =find(word,letter,1)
        print(index)

    return count



getword = input("please input a word:")
getletter = input("please input a letter:")
#getstart = int(input("please input a start number:"))
#print(find(getword, getletter, getstart))
print(countgetwithfind(getword,getletter))
