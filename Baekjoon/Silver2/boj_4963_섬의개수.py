import sys
sys.stdin = open('input_data/4963.txt')
sys.setrecursionlimit(100000)

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

def DSF(x, y) :
    visit[x][y] = 1
    for i in range(8):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < height and 0 <= ty < width and ground[tx][ty] and not visit[tx][ty]:
            DSF(tx, ty)

while True :
    width, height = map(int, input().split())
    if width == height == 0:
        break
    ground = [list(map(int, input().split())) for _ in range(height)]
    visit = [[0]* width for _ in range(height)]
    count = 0
    for x in range(height):
        for y in range(width):
            if ground[x][y] and not visit[x][y]:
                DSF(x, y)
                count += 1
    print(count)
