import sys
sys.stdin = open("input_data/1652.txt",'r')

size = int(input())
rooms = [input() for _ in range(size)]
garo = sero = 0


for i in range(size):
    garo_count = sero_count = 0
    for j in range(size):
        # 가로검사
        if rooms[i][j] == '.':
            garo_count += 1
        elif rooms[i][j] == 'X' and garo_count>=2:
                garo += 1
                garo_count = 0
        else: garo_count = 0
        
        # 세로검사
        if rooms[j][i] == '.':
            sero_count += 1
        elif rooms[j][i] == 'X' and sero_count>=2:
                sero += 1
                sero_count = 0
        else: sero_count = 0
    # 벽에 닿았을 때 넣어줄 것
    if garo_count >= 2:
        garo += 1
    if sero_count >= 2:
        sero += 1
print(garo, end=' ')
print(sero)
