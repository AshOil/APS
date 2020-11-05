#TODO 11/04 BFS로 수술중 그만둠

import sys; sys.stdin = open('input_data/5247.txt')
from collections import deque

for t in range(1, int(input()) + 1):
    number, target = map(int, input().split())
    turn_check = [1] * (target*2+1)
    Q = deque()
    Q.append(number)
    result = []
    while Q:
        number = Q.popleft()
        if number == target:
            result.append(turn_check[number])
            continue
        next_list = [number*2, number+1, number-1, number-10]
        for next in next_list:
            if next <= 0 or next > target * 2:
                break
            if turn_check[number] = turn_check[next]:
                turn_check[next] = turn_check[number] + 1
            Q.append(next)


    print('#{} {}'.format(t, result))