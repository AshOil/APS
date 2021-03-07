import sys; sys.stdin = open('input_data/2636.txt')
from pprint import pprint
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def CheezeFind():
    global count
    while Q:
        x, y = Q.pop(0)
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < width and 0 <= ty < height and not cheeze[tx][ty] and not visit[tx][ty]:
                visit[tx][ty] = 1
                Q.append([tx,ty])
            elif 0 <= tx < width and 0 <= ty < height and cheeze[tx][ty] and not visit[tx][ty]:
                cheeze[tx][ty] = 2


width, height = map(int, input().split())
cheeze = [list(map(int, input().split())) for _ in range(width)]
count = 1
count_list = []
while count:
    visit = [[0] * height for _ in range(width)]
    Q = [[0, 0]]
    visit[0][0] = 1
    count = 0
    CheezeFind()
    for i in range(width):
        for j in range(height):
            if cheeze[i][j] == 2:
                count += 1
                cheeze[i][j] = 0
    if count:
        count_list.append(count)

print(len(count_list))
print(count_list[-1])
