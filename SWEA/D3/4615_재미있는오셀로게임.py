import sys
from pprint import pprint
sys.stdin = open('input_data/4615.txt',"r")

# 8방향 설정
dx = [0, 0, -1, 1, 1, -1, 1, -1]
dy = [-1, 1, 0, 0, 1, -1, -1, 1]

T = int(input())
for t in range(1,T+1):
    size, turn = map(int,input().split())
    game_board = [[0]*(size+1) for _ in range(size+1)]

    # 기본위치 설정
    game_board[size//2][size//2] = game_board[size//2 +1][size//2 +1] = 2
    game_board[size//2+1][size//2] = game_board[size//2][size//2 +1] = 1

    # 둘 자리 input
    for _ in range(turn):
        y, x, color = list(map(int,input().split()))
        game_board[x][y] = color
        for i in range(8):
            check = []
            tx = x + dx[i]
            ty = y + dy[i]
            while  0 < tx <= size and 0 < ty <= size and game_board[tx][ty]:
                if game_board[tx][ty] != color:
                    check.append([tx,ty])
                    tx += dx[i]
                    ty += dy[i]
                else:
                    for data in check:
                        game_board[data[0]][data[1]] =color
                    break
    white = black = 0
    for line in game_board:
        white += line.count(1)
        black += line.count(2)
    print("#{} {} {}".format(t, white, black))


    pprint(game_board)
