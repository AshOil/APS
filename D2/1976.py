import sys
sys.stdin = open('input_data/1976.txt','r')

T = int(input())

for t in range(1, T+1):
    numbers = list(map(int,input().split()))
    first_time, first_minute, second_time, second_minute = numbers
    sum_time = first_time + second_time
    sum_min = first_minute + second_minute
    if sum_min >= 60 :
        sum_time += 1
        sum_min -= 60
    if sum_time >= 12 : 
        sum_time -= 12
    print('#{} {} {}'.format(t, sum_time, sum_min))
