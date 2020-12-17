import sys; sys.stdin = open('input_data/1493.txt')
from pprint import pprint

ground = [[0]*350 for _ in range(350)]
number_check = [0]
x, y = 0, 0
max_x = 0
now = 1
while now < 50000:
    ground[y][x] = now
    number_check.append([y, x])
    now += 1
    if x == 0:
        x = max_x + 1
        y = 0
        max_x += 1
    else:
        x -= 1
        y += 1

for t in range(1, int(input()) + 1):
    num_1, num_2 = map(int, input().split())
    new_num_x, new_num_y = [number_check[num_1][0] + number_check[num_2][0] + 1, number_check[num_1][1] + number_check[num_2][1] + 1]
    print('#{} {}'.format(t, ground[new_num_x][new_num_y]))
