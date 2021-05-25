n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
visit = [0]*n
result = 0

def DFS(x):
    visit[x] = 1
    for i in range(n):
        if x != i and computers[x][i] and not visit[i]:
            DFS(i)

for i in range(n):
    if not visit[i]:
        result +=1
        DFS(i)

print(result)
