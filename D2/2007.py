import sys
sys.stdin = open('input_data/2007.txt','r')

T = int(input())

for t in range(1, T+1):
    long_words = input()
    for i in range(2,10):
        if long_words[:i] == long_words[i:2*i]:
            print('#{} {}'.format(t,i))
            break
       