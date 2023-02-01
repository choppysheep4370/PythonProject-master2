'''
Ex13-9-readHello6
'''

import sys

with open('hello.txt', 'rt', encoding='UTF-8') as file:
    line_list = file.readlines()
    sys.stdout.writelines(line_list) # 시스템 스탠다드아웃_
    print(line_list)