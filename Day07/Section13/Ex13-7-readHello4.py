'''
Ex13-7-readHello4
'''
with open('hello.txt', 'rt', encoding='utf-8') as file:
    line_list = file.readlines()
    print(line_list)
    for line in line_list:
        print(line, end='')

