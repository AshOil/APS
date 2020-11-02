import sys; sys.stdin = open('input_data/2468.txt', "r")
sys.setrecursionlimit(10000000)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def DFS(x, y):
    global a
    visit[x][y] = 1
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if 0 <= new_x < N and 0 <= new_y < N and visit[new_x][new_y] == 0 and case[new_x][new_y] > num_list[a]:
            DFS(new_x, new_y)
N = int(input())
case = [list(map(int, input().split())) for _ in range(N)]
num_list = []
for i in range(N):
    for j in range(N):
        if case[i][j] not in num_list:
            num_list.append(case[i][j])
count = 0
result = []
for a in range(len(num_list)):
    visit = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if case[i][j] > num_list[a] and visit[i][j] == 0:
                count += 1
                DFS(i, j)
    result.append(count)
    count = 0
print(max(result))