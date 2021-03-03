import sys; sys.stdin = open('input_data/1949.txt')
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def BFS(x, y, height, depth, cutted):
    visit[x][y] = 1
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if not visit[tx][ty] and ground[tx][ty] < height:
            Q.append([tx, ty, ground[tx][ty], depth+1, cutted])



T = int(input())
for t in range(1, 2):
    size, dig = map(int, input().split())
    ground = [list(map(int, input().split())) for _ in range(size)]
    Q = deque()
    top = 1
    for i in range(size):
        for j in range(size):
            if ground[i][j] > top:
                top = ground[i][j]
                Q.clear()
                Q.append([i, j, top, 1, False])
            elif ground[i][j] == top:
                Q.append([i, j, top, 1, False])
    max_course = 0
    while Q:
        visit = [[0]*size for _ in range(size)]
        x, y, height, depth, cutted = Q.popleft()
        if depth > max_course:
            max_course = depth
        BFS(x, y, height, depth, cutted)