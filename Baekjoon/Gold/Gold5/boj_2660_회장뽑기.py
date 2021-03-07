import sys; sys.stdin = open('input_data/2660.txt')
from pprint import pprint
number = int(input())
check = [[0]*(number+1) for _ in range(number+1)]
pprint(check)
line = []
keepgoing = True
while keepgoing:
    in_lin2e = list(map(int,input().split()))
    if in_line[0] == -1:
        keepgoing = False
    else:
        line.append(in_line)

for x,y in line:
    check[y][x] = check[x][y] = 1
pprint(check)

