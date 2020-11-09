#TODO 어려운데?

import sys; sys.stdin = open('input_data/9327.txt')
from collections import deque

for t in range(int(input())):
    dot, line = map(int, input().split())
    route = [[] for _ in range(dot + 1)]
    for _ in range(line):
        x, y = map(int, input().split())
        route[x].append(y)
        route[y].append(x)
    Q = deque()
    for i in range(1, dot + 1):
        visit = [0] * (dot + 1)
        Q.append(i)
        while Q:
            now = Q.popleft()
            if visit