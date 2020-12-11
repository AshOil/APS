#TODO 41/50

import sys; sys.stdin = open('input_data/2382.txt')

from collections import deque

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]
way_change = [0, 2, 1, 4, 3]

for t in range(1, int(input()) + 1):
    size, isolation, number = map(int, input().split())
    default = [0, 0, 0]
    origin_ground = [[default] * size for _ in range(size)]
    target_point = deque()
    for _ in range(number):
        x, y, num, way = list(map(int, input().split()))
        origin_ground[x][y] = [num, num, way]
        target_point.append([x, y, 0])
    ground = [[default] * size for _ in range(size)]
    result = 0
    while target_point:
        now_x, now_y, turn = target_point.popleft()
        now_sum, now_max, way = origin_ground[now_x][now_y]
        if turn == isolation:
            result += now_sum
            continue
        tx = now_x + dx[way]
        ty = now_y + dy[way]
        # 모서리 체크
        if tx == 0 or ty == 0 or tx == size - 1 or ty == size - 1:
            now_sum = now_sum//2
            way = way_change[way]

        if ground[tx][ty] == default:
            ground[tx][ty] = [now_sum, now_sum, way]
        else:
            ground[tx][ty][0] += now_sum
            if ground[tx][ty][1] < now_max:
                ground[tx][ty][1] = now_max
                ground[tx][ty][2] = way
        if not target_point:
            for x in range(size):
                for y in range(size):
                    if ground[x][y][0]:
                        target_point.append([x, y, turn+1])
            origin_ground = ground
            ground = [[default] * size for _ in range(size)]
    print('#{} {}'.format(t, result))

