import sys; sys.stdin = open('input_data/5250.txt')
from collections import deque

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

for t in range(1, int(input()) + 1):
    size = int(input())
    ground = [list(map(int, input().split())) for _ in range(size)]
    visit =[[100000]*size for _ in range(size)]
    Q = deque()
    Q.append([0, 0])
    visit[0][0] = 0
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < size and 0 <= ty < size:
                plus = ground[tx][ty] - ground[x][y]
                if plus > 0:
                    if visit[tx][ty] > visit[x][y] + plus + 1:
                        visit[tx][ty] = visit[x][y] + plus + 1
                        Q.append([tx, ty])
                else:
                    if visit[tx][ty] > visit[x][y] + 1:
                        visit[tx][ty] = visit[x][y] + 1
                        Q.append([tx, ty])

    print('#{} {}'.format(t, visit[size-1][size-1]))