'''
Ex13-3-appendHello

a (apeend mode) : 추가 모드
'''
file = open('hello.txt', 'at', encoding='UTF-8')
file.write('hello\n')
file.write('nice to meet you\n')
print('hello.txt 파일에 새로운 내용이 추가 되었습니다.')
file.close()

