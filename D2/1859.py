## 진행중 시간문제 발생###

import sys
sys.stdin = open('input_data/1859.txt',"r")


T = int(input())
for t in range(1, T+1):
    length = int(input())
    numbers = list(map(int, input() .split()))
    buy = 0
    sold = 0
    buy_count = 0  
    JJAM = sorted(numbers)[::-1]
    for number in numbers:
        buy += number
        buy_count += 1
        if number == max(numbers):
            sold += number * buy_count
            numbers = numbers[buy_count:]
            buy_count = 0
    print('#{} {}'.format(t,sold-buy))

