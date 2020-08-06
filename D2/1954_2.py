
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
    for num in range(2, size ** 2 + 1):
        testX = x + dx[i]
        testY = y + dy[i]

        if size> testX >= 0 and size> testY >= 0:
            if vacancy[testX][testY] == 0:
                vacancy[testX][testY] = num
                x, y = testX, testY
            else:
                if i < 3:
                    i += 1
                else:
                    i = 0
                testX = x + dx[i]
                testY = y + dy[i]
                if size > testX >= 0 and size > testY >= 0:
                    if vacancy[testX][testY] == 0:
                        vacancy[testX][testY] = num
                        x, y = testX, testY
        else:
            if i<3:
                i += 1
            else:
                i = 0
            testX = x + dx[i]
            testY = y + dy[i]
            if size > testX >= 0 and size > testY >= 0:
                if vacancy[testX][testY] == 0:
                    vacancy[testX][testY] = num
                    x, y = testX, testY
                else:
                    if i < 3:
                        i += 1
                    else:
                        i = 0
                    testX = x + dx[i]
                    testY = y + dy[i]
                    if size > testX >= 0 and size > testY >= 0:
                        if vacancy[testX][testY] == 0:
                            vacancy[testX][testY] = num
                            x, y = testX, testY

    for van in vacancy:
        print(' '.join(map(str, van)))
    print()


