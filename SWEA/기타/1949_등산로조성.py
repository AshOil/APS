## 실패한거(BFS) 방문처리가 곤란함

import sys; sys.stdin = open('input_data/1949.txt')
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for t in range(1, int(input()) + 1):
    size, cutting = map(int, input().split())
    ground = [list(map(int, input().split())) for _ in range(size)]
    max_height = 0
    Q = deque()
    for x in range(size):
        for y in range(size):
            if ground[x][y] > max_height:
                Q.clear()
                max_height = ground[x][y]
                Q.append([x, y, ground[x][y], 1, False, [[x, y]]])
            elif ground[x][y] == max_height:
                Q.append([x, y, ground[x][y], 1, False, [[x, y]]])
    result = 0
    while Q:
        now_x, now_y, height, length, cut, been = Q.popleft()
        if length > result:
            result = length
        for i in range(4):
            tx = now_x + dx[i]
            ty = now_y + dy[i]
            if [tx, ty] in been: continue
            if tx < 0 or tx >= size or ty < 0 or ty >= size: continue
            if ground[tx][ty] < height:
                been.append([tx, ty])
                Q.append([tx, ty, ground[tx][ty], length+1, cut, been])
            else:
                if not cut:
                    for cancut in range(cutting+1):
                        if ground[tx][ty] - cancut < height:
                            been.append([tx, ty])
                            Q.append([tx, ty, ground[tx][ty] - cancut, length+1, True, been])
    print('#{} {}'.format(t, result))
