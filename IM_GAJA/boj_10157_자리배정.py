import sys; sys.stdin = open('input_data/10157.txt')
from pprint import pprint

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
height, width = map(int,input().split())
target = int(input())
ground = [[0]* width for _ in range(height)]
x, y = 0, 0
my_way = 1
if target > width*height:
    print(0)
else:
    for i in range(1, width*height+1):
        ground[y][x] = i
        if i == target:
            print(y + 1, x + 1)
            break
        tx = x + dx[my_way]
        ty = y + dy[my_way]
        if tx <0 or ty <0 or tx>=width or ty>=height or ground[ty][tx]:
            my_way += 1
            if my_way == 4:
                my_way = 0
        x += dx[my_way]
        y += dy[my_way]


