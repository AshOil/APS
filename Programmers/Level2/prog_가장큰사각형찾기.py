#TODO 하기시러


board = [[0]]


def solution(board):
    heigth , width = len(board), len(board[0])
    if len(board) < len(board[0]):
        size = len(board)
    else:
        size = len(board[0])
    for i in range(size, 0, -1):
        for y in range(width - i + 1):
            for x in range(heigth - i + 1):
                square = True
                for z in range(x + i - 1):
                    if sum(board[x][y : y + i]) != i:
                        square = False
                        break

        if square:
            return i**2


print(solution(board))