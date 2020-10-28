import sys; sys.stdin = open('input_data/3187.txt')
sys.setrecursionlimit(100000)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def DFS(x, y):
    global wolf
    global sheep
    if ground[x][y] == 'v':
        wolf += 1
    elif ground[x][y] =='k':
        sheep += 1
    visit[x][y] = 1
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < height and 0 <= ty < width and not ground[tx][ty] == '#' and not visit[tx][ty]:
            DFS(tx, ty)

height, width = map(int, input().split())
ground = [list(' '.join(input()).split()) for _ in range(height)]
print(ground)
visit = [[0] * width for _ in range(height)]
print(visit)
total_wolf = 0
total_sheep = 0
for i in range(height):
    for j in range(width):
        wolf = 0
        sheep = 0
        if not visit[i][j] and not ground[i][j] == '#':
            DFS(i, j)
            if wolf < sheep:
                total_sheep += sheep
            else:
                total_wolf += wolf
print(total_sheep, end=' ')
print(total_wolf)
