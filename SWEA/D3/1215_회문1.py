import sys; sys.stdin = open('input_data/1215.txt')

def verti_check(x, y):
    global result
    my_word = []
    for i in range(length):
        my_word.append(word_board[x+i][y])
    if my_word == my_word[::-1]:
        result += 1

def hori_check(x, y):
    global result
    my_word = []
    for i in range(length):
        my_word.append(word_board[x][y+i])
    if my_word == my_word[::-1]:
        result += 1

for t in range(1, 11):
    length = int(input())
    word_board = [input() for _ in range(8)]
    result = 0
    for x in range(8):
        for y in range(8):
            if y + length <= 8:
                hori_check(x, y)
            if x + length <= 8:
                verti_check(x, y)
    print('#{} {}'.format(t, result))
