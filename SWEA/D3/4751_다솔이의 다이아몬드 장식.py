import sys; sys.stdin = open('input_data/4751.txt')

for t in range(1, int(input()) + 1):
    word = list(' '.join(input()).split())
    length = len(word)
    size = 1 + length * 4
    board_1 = ['.']*size
    board_2 = ['.']*size
    board_3 = ['.']*size
    for i in range(size):
        if not i % 4:
            board_1[i] = '#'
        if i % 4 == 2:
            board_1[i] = word.pop(0)
            board_3[i] = '#'
    for i in range(size):
        if i % 2:
            board_2[i] = '#'
    print(''.join(board_3))
    print(''.join(board_2))
    print(''.join(board_1))
    print(''.join(board_2))
    print(''.join(board_3))
