# TODO 왜틀린교 ㅠㅠㅠ(파트 7)

import sys; sys.stdin = open('input_data/1459.txt')

x, y, line, cross = map(int, input().split())
if line*2 <= cross:
    print((x + y) * line)
else:
    print(min(max(x, y) * cross + line * min(x, y)%2, min(x,y) *cross + abs(x-y)*line))

