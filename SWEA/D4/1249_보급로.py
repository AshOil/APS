import sys; sys.stdin = open('input_data/1249.txt')
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for t in range(1, int(input()) + 1):
    size = int(input())
    ground = [list(map(int, ' '.join(input()).split())) for _ in range(size)]
    visit = [[100000]*size for _ in range(size)]
    x = y = 0
    Q = deque()
    Q.append([x, y])
    visit[x][y] = 0
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < size and 0 <= ty < size and visit[x][y] + ground[tx][ty] < visit[tx][ty]:
                visit[tx][ty] = visit[x][y] + ground[tx][ty]
                Q.append([tx, ty])
    print('#{} {}'.format(t, visit[size-1][size-1]))



