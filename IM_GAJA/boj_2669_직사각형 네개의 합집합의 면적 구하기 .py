import sys; sys.stdin = open('input_data/2669.txt')

squares = [list(map(int,input().split())) for _ in range(4)]

ground = [[0]*101 for _ in range(101)]
count=0
for square in squares:
    start_x, start_y, end_x, end_y = square
    for i in range(start_x, end_x):
        for j in range(start_y, end_y):
            if not ground[i][j]:
                ground[i][j] = 1
                count+=1

print(count)