m = 4
n = 3
puddles = [[2, 2]]

Ground = [[0]*m for _ in range(n)]
check = [[0]*m for _ in range(n)]
for puddle in puddles:
    Ground[puddle[1]-1][puddle[0]-1] = -1
for i in range(n):
    for j in range(m):
        if not i and not j:
            check[i][j] = 1
        elif not i:
            check[i][j] = check[i][j-1]
        elif not j:
            check[i][j] = check[i-1][j]
        else:
            check[i][j] = check[i-1][j] + check[i][j-1]
        if Ground[i][j] == -1:
            check[i][j] = 0
print(check)

