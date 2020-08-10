import sys
sys.stdin = open('input_data/6692.txt',"r")

T = int(input())
for t in range(1,T+1):
    length = int(input())
    percents = [list(map(float,input().split())) for _ in range(length)]
    sum = 0
    for percent in percents:
        sum += percent[0] * percent[1]
    print('#{} {}'.format(t,sum))