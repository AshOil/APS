import sys; sys.stdin = open('input_data/1873.txt')

looking = ['<', '>', '^', 'v']

for t in range(1, int(input())+1):
    print('#{}'.format(t), end=' ')
    height, width = map(int, input().split())
    ground = [' '.join(input()).split() for _ in range(height)]
    command_num = int(input())
    command = input()
    # 현재 위치 찾기
    for j in range(height):
        for i in range(width):
            if ground[j][i] in looking:
                x, y = i, j
                if ground[y][x] == '<':
                    now_look = 'L'
                elif ground[y][x] == '>':
                    now_look = 'R'
                elif ground[y][x] == '^':
                    now_look = 'U'
                else:
                    now_look = 'D'
    for char in command:
        if char == 'D':
            now_look = 'D'
            if y+1 < height and ground[y+1][x] == '.':
                ground[y+1][x] = 'v'
                ground[y][x] = '.'
                y += 1
            else:
                ground[y][x] = 'v'
        elif char == 'U':
            now_look = 'U'
            if y-1 >= 0 and ground[y - 1][x] == '.':
                ground[y - 1][x] = '^'
                ground[y][x] = '.'
                y -= 1
            else:
                ground[y][x] = '^'
        elif char == 'R':
            now_look = 'R'
            if x + 1 < width and ground[y][x + 1] == '.':
                ground[y][x + 1] = '>'
                ground[y][x] = '.'
                x += 1
            else:
                ground[y][x] = '>'
        elif char == 'L':
            now_look = 'L'
            if x-1 >= 0 and ground[y][x - 1] == '.':
                ground[y][x - 1] = '<'
                ground[y][x] = '.'
                x -= 1
            else:
                ground[y][x] = '<'
        # shooting
        else:
            bullet_x, bullet_y = x, y
            if now_look == 'R' or now_look == 'L':
                for _ in range(width):
                    if now_look == 'R':
                        bullet_x += 1
                        if bullet_x == width: break
                        if ground[y][bullet_x] == '#':
                            break
                        elif ground[y][bullet_x] == '*':
                            ground[y][bullet_x] = '.'
                            break
                    else:
                        bullet_x -= 1
                        if bullet_x == -1: break
                        if ground[y][bullet_x] == '#':
                            break
                        elif ground[y][bullet_x] == '*':
                            ground[y][bullet_x] = '.'
                            break
            else:
                for _ in range(height):
                    if now_look == 'D':
                        bullet_y += 1
                        if bullet_y == height: break
                        if ground[bullet_y][x] == '#':
                            break
                        elif ground[bullet_y][x] == '*':
                            ground[bullet_y][x] = '.'
                            break
                    else:
                        bullet_y -= 1
                        if bullet_y == -1: break
                        if ground[bullet_y][x] == '#':
                            break
                        elif ground[bullet_y][x] == '*':
                            ground[bullet_y][x] = '.'
                            break
    for i in range(height):
        print(''.join(ground[i]))



