import sys; sys.stdin = open('input_data/1987.txt')

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def DSF(x, y):
    global count
    global max_count
    count += 1
    if count > max_count:
        max_count = count
    alpha_check[ord(ground[x][y]) - ord('A') + 1] = 1
    if count == max_num:
        print(max_num)
        exit()
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < height and 0 <= ty < width and not alpha_check[ord(ground[tx][ty]) - ord('A') + 1]:
            DSF(tx, ty)
            alpha_check[ord(ground[tx][ty]) - ord('A') + 1] = 0
            count -= 1

height, width = map(int, input().split())
ground = []
alpha = ''
for _ in range(height):
    a = input()
    ground.append(a)
    alpha += a
alpha_check = [0] * 27
max_num = len(set(alpha))
max_count = 0
count = 0
DSF(0,0)

print(max_count)