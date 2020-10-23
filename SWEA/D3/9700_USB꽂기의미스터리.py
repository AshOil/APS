import sys; sys.stdin = open('input_data/9700.txt')

for t in range(1, int(input())+1):
    p, q = map(float,input().split())
    # 1. X O
    s1 = (1-p)*q
    # 2. O X O
    s2 = p*(1-q)*q
    if s1 < s2:
        print('#{} YES'.format(t))
    else:
        print('#{} NO'.format(t))