import sys; sys.stdin = open('input_data/2210.txt')

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def make_number(x, y, number):
    number += str(ground[x][y])
    if len(number) >= 6:
        result_list.append(number)
        return
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < 5 and 0 <= ty < 5:
            make_number(tx, ty, number)


ground = [list(map(int, input().split())) for _ in range(5)]
result_list = []
for x in range(5):
    for y in range(5):
        make_number(x, y, '')
print(len(list(set(result_list))))



