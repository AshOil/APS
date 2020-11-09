import sys; sys.stdin = open('input_data/7576.txt')
from pprint import pprint
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

width, height = map(int,input().split())
ground = [list(map(int,input().split())) for _ in range(height)]
visit = [[0] * width for _ in range(height)]
Q = deque()
for y in range(width):
    for x in range(height):
        if ground[x][y] == 1:
            Q.append([x, y])
            visit[x][y] = 1
        elif ground[x][y] == -1:
            visit[x][y] = -1

while Q:
    x, y = Q.popleft()
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < height and 0 <= ty < width and not visit[tx][ty] and not visit[tx][ty] == -1:
            visit[tx][ty] = visit[x][y] + 1
            Q.append([tx, ty])
pprint(visit)
max_count = 0
for line in visit:
    for num in line:
        if num == 0:
            print(-1)
            exit()
        if num > max_count:
            max_count = num
print(max_count-1)