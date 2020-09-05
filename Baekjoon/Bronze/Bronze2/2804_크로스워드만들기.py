import sys
sys.stdin = open('input_data/2804.txt',"r")

# 빈 보드 형성
word_a, word_b = list(input() .split())
length_a , length_b = len(word_a), len(word_b)
board = [['.']*(length_a-1) for _ in range(length_b-1)]

# 교차점, 위치 파악
cross_char_list = []
cross_char = ''
for char_b in word_b:
    for char_a in word_a:
        if char_a == char_b:
            cross_char_list.append(char_a)

for char_a in word_a:
    if char_a in cross_char_list:
        cross_char = char_a
        break

a_start = word_b.index(cross_char)
b_start = word_a.index(cross_char)

# 가로 넣기
board.insert(a_start,list(word_a))

# 세로 넣기
i = 0
for char_b in word_b:
    if i == a_start:
        pass
    else:
        board[i].insert(b_start,char_b)
    i += 1
for result in board:
    print(''.join(result))

