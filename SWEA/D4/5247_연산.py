#TODO 11/04 시간초과

import sys; sys.stdin = open('input_data/5247.txt')

def calcul(number, count):
    global min_count
    if number <= 0 or number > 2 * target or count > min_count: return
    if number == target:
        if count < min_count:
            min_count = count
            return
    calcul(number*2, count + 1)
    calcul(number+1, count + 1)
    calcul(number-10, count + 1)
    calcul(number-1, count + 1)



for t in range(1, int(input()) + 1):
    number, target = map(int, input().split())
    for i in range(1, 100):
        if number * (2**i) > target:
            min_count = i + (number * (2**i))-target
            break
    calcul(number, 0)
    print('#{} {}'.format(t, min_count))