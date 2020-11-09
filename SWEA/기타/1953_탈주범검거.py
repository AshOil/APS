import sys; sys.stdin = open('input_data/1953.txt')
from collections import deque

dx = [0, -1, 0, 1, 0]
dy = [0, 0, 1, 0, -1]

way_out = {
    '1' : [1, 2, 3, 4],
    '2' : [1, 3],
    '3' : [2, 4],
    '4' : [1, 2],
    '5' : [2, 3],
    '6' : [3, 4],
    '7' : [1, 4]
}
way_in = {
    '1' : [1, 2, 3, 4],
    '2' : [1, 3],
    '3' : [2, 4],
    '4' : [3, 4],
    '5' : [1, 4],
    '6' : [1, 2],
    '7' : [2, 3]
}

for t in range(1, int(input()) + 1):
    height, width, x, y, runtime = map(int, input().split())
    ground = [list(map(int, input().split())) for _ in range(height)]
    visit = [[0] * width for _ in range(height)]
    count = 1
    Q = deque()
    Q.append([x, y])
    visit[x][y] = 1
    time = 1
    while Q:
        x, y = Q.popleft()
        if visit[x][y] == runtime:
            continue
        for i in way_out[str(ground[x][y])]:
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < height and 0 <= ty < width and ground[tx][ty] and not visit[tx][ty] and i in way_in[str(ground[tx][ty])]:
                visit[tx][ty] = visit[x][y] + 1
                count +=1
                Q.append([tx,ty])
    print('#{} {}'.format(t, count))