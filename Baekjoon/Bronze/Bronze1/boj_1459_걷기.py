import sys; sys.stdin = open('input_data/1459.txt')

x, y, line, cross = map(int, input().split())
if line*2 <= cross:
    print((x + y) * line)
else:
    print(min(min(x,y)*cross + abs(x-y)*line, max(x, y) * cross + (x+y)%2 * line))

