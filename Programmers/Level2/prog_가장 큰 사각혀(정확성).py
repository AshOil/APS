def solution(board):
    height , width = len(board), len(board[0])
    size = min(height, width)
    for i in range(size, 0, -1):
        for x in range(height - i + 1):
            for y in range(width - i + 1):
                square = True
                if board[x][y]:
                    for z in range(i):
                        if 0 in board[x+z][y:y+i]:
                            square = False
                            break
                    if square:
                        return i**2
    return 0