import sys
sys.stdin = open('input_data/1954.txt',"r")

T = int(input())
for t in range(1, T+1):
    size = int(input())
    vacancy = [[0] * size for _ in range(size)]
    vacancy[0][0] = 1

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    x = y = 0
    i = 0
    count = 2
    while count < size**2 + 1 :
        tX = x + dx[i]
        tY = y + dy[i]

        if size> tX >= 0 and size> tY >= 0:
            if vacancy[tX][tY] == 0:
                vacancy[tX][tY] = count
                x, y = tX, tY
                count += 1
            else:
                if i < 3: i += 1
                else: i = 0
        else:
            if i<3: i += 1
            else: i = 0

    print('#{}'.format(t))
    for van in vacancy:
        print(*van)


