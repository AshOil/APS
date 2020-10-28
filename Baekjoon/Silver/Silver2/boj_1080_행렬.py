import sys; sys.stdin = open('input_data/1080.txt')

height, width = map(int, input().split())
A = [list(map(int, ' '.join(input()).split())) for _ in range(height)]
B = [list(map(int, ' '.join(input()).split())) for _ in range(height)]
result = 0
for i in range(height-2):
    for j in range(width-2):
        if A[i][j] != B[i][j]:
            result += 1
            for x in range(i, i +3):
                for y in range(j, j+3):
                    if A[x][y]:
                        A[x][y] = 0
                    else:
                        A[x][y] = 1
if A == B :
    print(result)
else:
    print(-1)

