import sys
sys.stdin = open('input_data/5162.txt',"r")

T = int(input())

for t in range(1,T+1):
    a , b , money = list(map(int, input().split()))
    result = 0
    if a> b:
        result = money//b
    else:
        result = money//a

    print('#{} {}'.format(t, result))