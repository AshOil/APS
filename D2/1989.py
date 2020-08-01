
### 진행중 ###


import sys
sys.stdin = open('input_data/1989.txt',"r")

T = int(input())
for t in range(1, T+1):
    word = input()
    reversed_word = word[::-1]
    if word == reversed_word:
        result = '1'
    else:
        result = '0'
    print('#{} {}'.format(t, result))