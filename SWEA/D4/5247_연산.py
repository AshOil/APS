import sys; sys.stdin = open('input_data/5247.txt')
from collections import deque

for t in range(1, int(input()) + 1):
    number, target = map(int, input().split())
    turn_check = [10000] * (target*2+1)
    Q = deque()
    Q.append(number)
    turn_check[number] = 0
    while Q:
        number = Q.popleft()
        next_list = [number*2, number+1, number-1, number-10]
        for next in next_list:
            if next <= 0 or next > target * 2: continue
            if turn_check[next] > turn_check[number] + 1 :
                turn_check[next] = turn_check[number] + 1
                Q.append(next)

    print('#{} {}'.format(t, turn_check[target]))