import sys; sys.stdin = open('input_data/1949.txt')
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def DFS(x, y, height, length, cut):
    global result
    length += 1
    if length > result:
        result = length
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if tx < 0 or tx >= size or ty < 0 or ty >= size or visit[tx][ty] : continue
        if ground[tx][ty] < height:
            visit[tx][ty] = 1
            DFS(tx, ty, ground[tx][ty], length, cut)
            visit[tx][ty] = 0
        else:
            if not cut:
                for cancut in range(cutting+1):
                    if ground[tx][ty] - cancut < height:
                        visit[tx][ty] = 1
                        DFS(tx, ty, ground[tx][ty] - cancut, length, True)
                        visit[tx][ty] = 0


for t in range(1, int(input()) + 1):
    size, cutting = map(int, input().split())
    ground = [list(map(int, input().split())) for _ in range(size)]
    max_height = 0
    start_point = []
    for x in range(size):
        for y in range(size):
            if ground[x][y] > max_height:
                start_point.clear()
                max_height = ground[x][y]
                start_point.append([x, y])
            elif ground[x][y] == max_height:
                start_point.append([x, y])
    result = 0
    for point in start_point:
        visit = [[0] * size for _ in range(size)]
        x, y = point
        visit[x][y] = 1
        DFS(x, y, ground[x][y], 0, False)
        visit[x][y] = 0
    print('#{} {}'.format(t, result))
