import sys;sys.stdin = open('input_data/5250.txt')

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

def my_way(x, y):
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < size and 0 <= ty < size:
            plus = ground[tx][ty] - ground[x][y]
            if plus <= 0:
                plus = 0
            if visit[tx][ty] > visit[x][y] + plus + 1:
                visit[tx][ty] = visit[x][y] + plus + 1
                my_way(tx, ty)


for t in range(1, int(input()) + 1):
    size = int(input())
    ground = [list(map(int, input().split())) for _ in range(size)]
    visit =[[10000]*size for _ in range(size)]
    visit[0][0] = 1
    my_way(0, 0)
    print(visit)
    print('#{} {}'.format(t, visit[size-1][size-1]-1))
