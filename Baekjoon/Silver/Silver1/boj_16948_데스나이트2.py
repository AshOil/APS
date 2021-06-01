import sys; sys.stdin = open('input_data/16948.txt')

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

size = int(input())
Ground = [[10000]*size for _ in range(size)]
start_x, start_y, end_x, end_y = map(int, input().split())
if abs(start_x - end_x)%2:
    print(-1)
else:
    gap_x = abs(start_x - end_x)//2
    if gap_x%2:
        if not abs(start_y - end_y) % 2:
            print(-1)
    else:
        if abs(start_y - end_y) % 2:
            print(-1)
