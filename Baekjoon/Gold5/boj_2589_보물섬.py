import sys; sys.stdin = open('input_data/2589.txt')

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def BSF():
    while Q:
        x, y = Q.pop(0)
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < height and 0 <= ty < width and ground[tx][ty] =='L' and not visit[tx][ty]:
                Q.append([tx,ty])
                visit[tx][ty] = visit[x][y] + 1
                max_num.append(visit[tx][ty])

height, width = map(int,input().split())
ground = [list(''.join(input())) for _ in range(height)]

Q = []
max_num = []
for i in range(height):
    for j in range(width):
        visit = [[0] * width for _ in range(height)]
        count = 1
        if ground[i][j] =='L':
            visit[i][j] = 1
            Q.append([i,j])
            BSF()
print(max(max_num)-1)

