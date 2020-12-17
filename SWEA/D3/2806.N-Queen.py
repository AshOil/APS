# TODO 1217 개안풀리네

import sys; sys.stdin = open('input_data/2806.txt')

dx = [1, 0, -1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, 1, -1, 1, -1]

def cross_check(x, y):
    for i in range(8):
        for j in range(1, size):
            tx = x + dx[i] * j
            ty = y + dy[i] * j
            if tx < 0 or tx >= size or ty <0 or ty >= size:
                break
            if check[ty][tx]:
                return False
    else:
        return True

def do_chess(x, line):
    check[line][x] = 1
    global result
    if line + 1 == size - 1:
        for i in range(size):
            if cross_check(i, line+1) != False:
                result += 1
    else:
        for i in range(size):
            if cross_check(i, line+1) == False:
                continue
            else:
                do_chess(i, line + 1)


for t in range(1, int(input()) + 1):
    size = int(input())
    result = 0
    if size == 1:
        print("#{} 1".format(t))
        continue
    for x in range(size):
        check = [[0] * size for _ in range(size)]
        do_chess(x, 0)

    print('#{} {}'.format(t, result))



