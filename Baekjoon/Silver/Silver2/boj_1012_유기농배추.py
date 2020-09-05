import sys
from pprint import pprint
sys.stdin = open('input_data/1012.txt')
sys.setrecursionlimit(10**8)  # 재귀 최대 깊이를 늘려 오류 방지

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def DSF(x, y):
    visit[x][y] = 1
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < sero and 0 <= ty < garo and ground[tx][ty] and not visit[tx][ty]:
            DSF(tx,ty)

T= int(input())
for _ in range(T):
    garo, sero , bae_chu = map(int,input().split())
    ground = [[0] * garo for _ in range(sero)]
    for _ in range(bae_chu):
        y,x = map(int, input().split())
        ground[x][y] = 1
    visit = [[0] * garo for _ in range(sero)]

    count = 0
    for y in range(garo):
        for x in range(sero):
            if ground[x][y] and not visit[x][y]:
                count += 1
                DSF(x,y)
    print(count)


