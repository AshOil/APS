arr = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

N = len(arr)
M = len(arr[0])

dx = [0,1,0,-1]
dy = [1,0,-1,0]
#대각선도 포함하려면
# dx = [0,0,-1,1,1,-1,1,-1]
# dy = [-1,1,0,0,1,-1,-1,1]


for x in range(N):
    for y in range(M):
        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]
            if testX >= 0 and testX < N and testY >= 0 and testY < M:
                print(arr[testX][testY], end = ' ')

 7 10 5 2 8 11 6 3 12 7 4 10 5 11 9 6 12 10 7 11 8
Process