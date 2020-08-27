import sys
sys.stdin = open('input_data/5515.txt',"r")

T = int(input())
calender = {
    '1' : 31, '2' : 29,
    '3' : 31, '4' : 30,
    '5' : 31, '6' : 30,
    '7' : 31, '8' : 31,
    '9' : 30, '10' : 31,
    '11' : 30, '12' : 31,
}
standard = list((1,1))
for t in range(1,T+1):
    sum_day = 3
    today = list(map(int,input().split()))
    for month in range(1, today[0]):
        sum_day += calender[str(month)]
    sum_day += today[1]
    result = sum_day%7

    print('#{} {}'.format(t, result))


