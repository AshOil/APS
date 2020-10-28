import sys; sys.stdin = open('input_data/magnetic.txt')
from collections import deque

for t in range(1, int(input()) + 1):
    K = int(input())
    Q = [[]] + [deque(list(map(int, input().split()))) for _ in range(4)]

    for _ in range(K):
        num, dir = map(int, input().split())
        check = [0] * 5
        check[num] = dir

        for i in range(num+ 1, 5):
            if Q[i-1][2] == Q[i][6]: break
            check[i] = -check[i-1]
        for i in range(num-1, 0, -1):
            if Q[i][2] == Q[i+1][6] : break
            check[i] = -check[i+1]

        for i in range(1, 5):
            if check[i] == 1:
                Q[i].appendleft(Q[i].pop())
            elif check[i] == -1:
                Q[i].append(Q[i].popleft())
    ans = 0
    for i in range(1, 5):
        if Q[i][0] == 1:
            ans += (1 << (i-1))
    print(ans)


