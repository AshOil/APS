import sys; sys.stdin = open("2.txt")
from pprint import pprint

dx = [1, 1, -1, -1, 1, -1, 0, 0]
dy = [1, -1, 1, -1, 0, 0, 1, -1]

def check_distance(list, house):
    global max_distance
    house_distance = [100]*house_num
    for in_list in list:
        x, y = in_list
        for idx, in_house in enumerate(house):
            house_x, house_y = in_house
            distance = abs(x - house_x) + abs(y - house_y)
            if house_distance[idx] > distance:
                house_distance[idx] = distance
    max_distance.append(max(house_distance))

def make_road(x, y):
    for i in range(8):
        road = []
        for j in range(-max(width, height), max(width, height)):
            tx = x + dx[i] * j
            ty = y + dy[i] * j
            if 0 <= tx < height and 0 <= ty < width:
                if ground[tx][ty]:
                    break
                else:
                    road.append([tx, ty])
        else:
            if len(road) >= 2:
                check_distance(road, house)

T= int(input())
for t in range(1, T + 1):
    width, height = map(int, input().split())
    ground = [list(map(int, input().split())) for _ in range(height)]
    house = []
    for i in range(height):
        for j in range(width):
            if ground[i][j]:
                house.append([i, j])
    house_num = len(house)
    max_distance = []
    for i in range(height):
        for j in range(width):
            make_road(i, j)
    if max_distance:
        print('#{} {}'.format(t, min(max_distance)))
    else:
        print("#{} -1".format(t))
