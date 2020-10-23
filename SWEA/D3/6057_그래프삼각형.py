##### 43~44개 맞음 ###

import sys
sys.stdin = open('input_data/6057.txt')

def DFS(i):
    global result
    global count
    count += 1
    if count == 3:
        if ground[start][i] :
            result += 1
            return
    for j in range(i, dot+1):
        if ground[i][j] and j != start:
            DFS(j)
            count -=1

for t in range(1, int(input())+1):
    dot, line = map(int,input().split())
    line_data = [list(map(int,input().split())) for _ in range(line)]
    ground = [[0]*(dot+1) for _ in range(dot+1)]
    for data in line_data:
        ground[data[0]][data[1]] = 1
        ground[data[1]][data[0]] = 1
    result = 0
    for i in range(1, dot-1):
        count = 0
        start = i
        DFS(i)
    print('#{} {}'.format(t, result))