import sys; sys.stdin = open('input_data/5125.txt')
from itertools import combinations


for t in range(1, int(input())+1):
    number, max_cal = map(int, input().split())
    numbers = [i for i in range(number)]
    taste = []
    cal = []
    for _ in range(number):
        a, b = map(int, input().split())
        taste.append(a)
        cal.append(b)
    powerset = []
    for i in range(1, number+1):
        powerset += (list(combinations(numbers, i)))
    max_taste = 0
    for check in powerset:
        my_taste = 0
        my_cal = 0
        for j in check:
            my_taste += taste[j]
            my_cal += cal[j]
            if my_cal <= max_cal:
                if my_taste > max_taste:
                    max_taste = my_taste
    print('#{} {}'.format(t, max_taste))



