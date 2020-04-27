import sys
script, encoding= sys.argv

def main(language_file, encoding):
    line = language_file.readline()
    if line:
        print_line(line, encoding)
        return main(language_file, encoding)

def print_line(line, encoding):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding)
    #设置不同错误的处理方案。默认为 'strict',意为编码错误引起一个UnicodeError。 其他可能得值有 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' 以及通过 codecs.register_error() 注册的任何值。
    cooked_string = raw_bytes.decode(encoding) #str(raw_bytes, encoding = 'utf8')

    print(raw_bytes, "<====>", cooked_string)

languages = open("languages.txt", encoding = "utf-8")

main(languages, encoding)
