'''
Ex13-4-readHello1.py

r (read mode) : 읽기 전용 모드 / 파일 없으면 에러

경로
    절대경로 예) C:\ForGG_Python\Origianl_File\PythonProject-master\Day07\Section13\hello.txt
    상대경로 예) ./upload/hello2.txt
               ../../resources/hello2.txt
        . -> 현재폴더
        .. -> 상위폴더

'''

# 절대경로
file = open('hello.txt', 'rt')
str = file.read()
print(str, end='')
file.close()

# 상대경로
