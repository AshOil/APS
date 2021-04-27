
import sys; sys.stdin = open('input_data/2206.txt')
from collections import deque
from pprint import pprint

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def min_way():
    global min_step
    Q = deque()
    Q.append([0, 0])
    visit[0][0] = 1
    while Q:
        x, y = Q.popleft()
        if x == height -1 and y == width - 1:
            if visit[x][y] < min_step:
                min_step = visit[x][y]
                return
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < height and 0 <= ty < width and not ground[tx][ty] and not visit[tx][ty]:
                visit[tx][ty] = visit[x][y] + 1
                Q.append([tx, ty])

height, width = map(int,input().split())
ground = [list(map(int,' '.join(input()).split())) for _ in range(height)]

min_step = 10000

first_check = [0,1], [1, 0], [height-1, width-2], [height-2, width-1]
can_break = []
for check in first_check:
    if ground[check[0]][check[1]]:
        can_break.append(check)
for i in range(height):
    for j in range(width):
        if ground[i][j]:
            if 0 <= i-1 and i+1 < height and 0 <= j -1 and j+1 < width:
                if (not ground[i-1][j] and not ground[i+1][j]) or (not ground[i][j-1] and not ground[i][j+1]):
                    can_break.append([i,j])
visit = [[0]* width for _ in range(height)]
min_way()
if can_break:
    for can in can_break:
        visit = [[0] * width for _ in range(height)]
        ground[can[0]][can[1]] = 0
        min_way()
        ground[can[0]][can[1]] = 1
pprint(visit)
if min_step == 10000:
    print(-1)
else:
    print(min_step)



