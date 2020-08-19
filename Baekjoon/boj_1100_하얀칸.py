import sys
sys.stdin = open('input_data/1100.txt',"r")

game_board = []
for _ in range(8):
    game_board.append(input())

cnt = 0
for i in range(8):
    for j in range(8):
        if i%2 == 0 and j%2 ==0 and game_board[i][j] =='F':
            cnt +=1
        elif i%2 != 0 and j%2 !=0 and game_board[i][j] =='F':
            cnt +=1
print(cnt)