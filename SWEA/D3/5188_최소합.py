import sys; sys.stdin = open('input_data/5188.txt')


def DFS(x, y, calsum):
    global min_num
    calsum += ground[y][x]
    if calsum > min_num:
        return
    if x == size-1 and y == size -1:
        if calsum < min_num:
            min_num = calsum

    if x < size - 1:
        DFS(x+1, y, calsum)
    if y < size - 1:
        DFS(x, y+1, calsum)


for t in range(1, int(input()) + 1):
    size = int(input())
    ground = [list(map(int, input().split())) for _ in range(size)]
    min_num = 100000
    DFS(0, 0, 0)
    print('#{} {}'.format(t, min_num))