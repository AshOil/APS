import sys; sys.stdin = open('input_data/5656.txt')
from copy import deepcopy
from itertools import product
from pprint import pprint

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def whereBoom(shoot):
    number_list = [i for i in range(width)]
    return list(map(list, product(number_list, repeat=shoot)))


def blockDrop():
    for y in range(height):
        for x in range(width):
            if ground[y][x] and not ground[y+1][x]:
                ground[y+1][x] = ground[y][x]
                ground[y][x] = 0

def boom(x, y, damage):
    ground[x][y] = 0
    if damage != 1:
        for i in range(4):
            for j in range(1, damage):
                tx = x + (dx[i] * j)
                ty = y + (dy[i] * j)
                if 0 <= ty < width and 0 <= tx < height and ground[tx][ty]:
                    boom(tx, ty, ground[tx][ty])

def boomDrop(shot):
    global result
    if shot == shoot:
        remain = 0
        for x in range(width):
            for y in range(height):
                if ground[y][x]:
                    remain += 1
        if remain < result:
            result = remain
        return
    else:
        now_target = boom_place[shot]
        for i in range(height):
            if ground[i][now_target]:
                boom(i, now_target, ground[i][now_target])
                boomDrop(shot + 1)
                break
        else:
            return



for t in range(1, int(input()) + 1):
    shoot, width, height = map(int, input().split())
    origin_ground = [list(map(int, input().split())) for _ in range(height)]
    result = 1000
    boom_places = whereBoom(shoot)
    for boom_place in boom_places:
        ground = deepcopy(origin_ground)
        boomDrop(0)
        if result == 0:
            break
    print(result)



