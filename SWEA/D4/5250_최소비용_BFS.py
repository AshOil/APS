import sys; sys.stdin = open('input_data/5250.txt')
from collections import deque


dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

for t in range(1, int(input()) + 1):
    size = int(input())
    ground = [list(map(int, input().split())) for _ in range(size)]
    visit =[[0]*size for _ in range(size)]
    min_cost = 10000
    Q = deque()
    Q.append([0, 0, 0])
    while Q:
        x, y, cost = Q.popleft()
        if cost > min_cost:
            continue
        if x == size - 1 and y == size - 1:
            if min_cost > cost:
                min_cost = cost
                continue

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < size and 0 <= ty < size and not visit[tx][ty]:
                plus = ground[tx][ty] - ground[x][y]
                Q.append(tx, ty)
                if plus > 0:
                    my_way(tx, ty, cost + 1 + plus)
                else:
                    my_way(tx, ty, cost + 1)
                visit[x][y] = 0











    print('#{} {}'.format(t, min_cost))
