'''
Ex12-11-practice

김민철 vs 원지훈
윤찬희 vs 이성은
'''

import random
import time

pot = [n for n in range(1, 46)] # 1부터 46의 숫자

jackpot = [] # 잭팟이라는 리스트를 무엇이든 들어갈수 있도록 비워둔채로 선언

for n in range(1, 7): # 1에서 6까지
    random.shuffle(pot) # pot을 랜덤하게 섞는다?
    pick = pot.pop() # ??
    print('{}번째 당첨번호는 {}입니다. '.format(n, pick)) # n번째 당첨 번호는 잭팟에서 뽑은 숫자 pick입니다
    jackpot.append(pick) # 숫자를 뽑아서 jackpot에 저장한다
    time.sleep(2) # 2초동안 멈춤

jackpot.sort() # 오름차순으로 정렬
print('이번 당첨번호는 {} 입니다.'.format(jackpot)) # 잭팟에서 나온숫자를
