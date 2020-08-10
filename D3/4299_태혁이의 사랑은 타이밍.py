import sys
sys.stdin = open('input_data/4299.txt',"r")

T = int(input())

for t in range(1,T+1):
    standard = 11
    day , hour , minute = list(map(int, input().split()))
    day_sum = 0
    if minute >= 11:
        day_sum += minute-11
    else:
        hour -= 1
        day_sum += minute -11 +60

    if hour >= 11:
        day_sum += (hour-11) * 60
    else:
        day -= 1
        day_sum += (hour -11 + 24) *60

    day_sum += (day-11) *60 * 24
    if day_sum < 0:
        print('#{} -1'.format(t))
    else:
        print('#{} {}'.format(t, day_sum))

