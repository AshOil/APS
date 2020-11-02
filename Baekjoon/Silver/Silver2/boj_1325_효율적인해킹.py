import sys; sys.stdin = open('input_data/1325.txt')
from collections import deque

dot, line = map(int, input().split())
graph = [[] for _ in range(dot + 1)]
for _ in range(line):
    data = list(map(int, sys.stdin.readline().split()))
    graph[data[1]].append(data[0])
max_list = []
max_num = 0

visit = [0] * (dot + 1)
for i in range(1, dot + 1):
    Q = deque()
    if graph[i]:
        Q.append(i)
    count = 0
    while Q:
        now = Q.popleft()
        count += 1
        for w in graph[now]:
            if visit[w]:
                count += visit[w]
            else:
                Q.append(w)
    visit[i] = count

    if max_num < count:
        max_num = count
        max_list = []
        max_list.append(i)
    elif max_num == count:
        max_list.append(i)
print(' '.join(map(str,max_list)))
