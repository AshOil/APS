import sys
sys.stdin = open('input_data/2583.txt')
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

M, N, K = list(map(int, input().split()))
matrix = [[0 for _ in range(N)] for _ in range(M)]
result_list = []

def dfs(idx):
    stack = []
    stack.append(idx)
    size = 0

    while stack:
        r, c = stack.pop()
        size += 1

        for i in range(4):
            tr, tc = r + dr[i], c + dc[i]
            if 0 <= tr < M and 0 <= tc < N and matrix[tr][tc] == 0:
                stack.append([tr, tc])
                matrix[tr][tc] = 1

    result_list.append(size)


for _ in range(K):
    l, b, r, t = list(map(int, input().split()))
    for i in range(b,t):
        for j in range(l, r):
            # matrix[M-i-1][j] = 1
            matrix[i][j] = 1

for i in range(M):
    for j in range(N):
        if matrix[i][j] == 0:
            matrix[i][j] = 1
            dfs([i, j])

print(len(result_list))
for i in sorted(result_list):
    print(i, end=' ')