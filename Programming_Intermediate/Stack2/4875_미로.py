import sys
sys.stdin = open('input_data/4875.txt')

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def MazeRun(x,y):
    stack.append([x, y])
    while stack:
        visit[y][x] = 1
        x, y = stack.pop()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < size and 0 <= ty < size and ground[tx][ty] == 3:
                print('#{} 1'.format(t))
                return
            if 0 <= tx < size and 0 <= ty < size and not ground[tx][ty] and not visit[ty][tx]:
                stack.append([tx,ty])
    print('#{} 0'.format(t))
    return


T= int(input())

for t in range(1,T+1):
    stack = []
    size = int(input())
    ground = [list(map(int, ' '.join(input()).split())) for _ in range(size)]
    visit = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if ground[i][j] == 2:
                MazeRun(i,j)
