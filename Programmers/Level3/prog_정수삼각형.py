triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
N = len(triangle)
check = [[0]*(i+1) for i in range(len(triangle)-1)]
check.append(triangle[-1])

def get_high(i,j):
    if check[i][j]:
        return check[i][j]
    check[i][j] = max(get_high[i+1][j], get_high[i+1][j+1])


for i in range(N-2 ,-1, -1):
    for j in range(i+1):
        check[i][j] = max(check[i + 1][j], check[i + 1][j + 1]) + triangle[i][j]