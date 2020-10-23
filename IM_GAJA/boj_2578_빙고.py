import sys; sys.stdin = open('input_data/2578.txt')

game_board = [list(map(int,input().split())) for _ in range(5)]
for i in range(5):
    sero = []
    for j in range(5):
        sero.append(game_board[j][i])
    game_board.append(sero)
daegak_1 = []
daegak_2 = []
for i in range(5):
    daegak_1.append(game_board[i][i])
    daegak_2.append(game_board[i][4-i])
game_board.append(daegak_1)
game_board.append(daegak_2)

call = []
for _ in range(5):
    call += list(map(int,input().split()))
def find():
    for idx, number in enumerate(call):
        count = 0
        for line in game_board:
            if not line:
                count +=1
                if count == 3:
                    return idx
            if number in line:
                line.remove(number)

print(find())

