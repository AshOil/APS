import sys; sys.stdin = open('input_data/2583.txt')
from pprint import pprint
sys.setrecursionlimit(1000000000)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# DFS
def DFS(x,y):
    global count
    count += 1
    visit[x][y] = 1
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0<=tx<N and 0<=ty<M and not visit[tx][ty] and not ground[tx][ty]:
            DFS(tx,ty)

# 정보 불러오기
M, N, k = map(int,input().split())

# 지도 만들기
ground = [[0]*M for _ in range(N)]
visit = [[0]*M for _ in range(N)]
for _ in range(k):
    start_x, start_y, end_x, end_Y = map(int,input().split())
    for i in range(start_x, end_x):
        for j in range(start_y, end_Y):
            ground[i][j] = 1
result = []
for i in range(N):
    for j in range(M):
        count = 0
        if not visit[i][j] and not ground[i][j]:
            DFS(j,i)
            result.append(count)
result.sort()
print(len(result))
print(*result)
