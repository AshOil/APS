#TODO 30퍼에서 틀림

import sys; sys.stdin = open('input_data/1389.txt')
from collections import deque

dot, line = map(int, input().split())
line_data = [list(map(int, input().split())) for _ in range(line)]
sort_line = [[] for _ in range(dot+1)]
sum_check = [0] * (dot+1)
for data in line_data:
    sort_line[data[0]].append(data[1])
    sort_line[data[1]].append(data[0])


Q = deque()
for i in range(1, dot+1):
    Q.append(i)
    total = 0
    visit[i] = 0
    visit = [10000] * (dot+1)
    while Q:
        now = Q.pop()
        if sort_line[now]:
            for next in sort_line[now]:
                if visit[next] > visit[now] + 1:
                    visit[next] = visit[now] + 1
                    Q.append(next)
                    total += visit[next]
    sum_check[i] = total
result = 10000
min_val = 10000
for i in range(1, dot + 1):
    if min_val > sum_check[i]:
        result = i
        min_val = sum_check[i]
print(result)