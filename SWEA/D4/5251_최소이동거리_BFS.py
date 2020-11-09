import sys; sys.stdin = open('input_data/5251.txt')
from collections import deque

for t in range(1, int(input()) + 1):
    min_move = 10000
    end, line = map(int, input().split())
    line_data = [list(map(int, input().split())) for _ in range(line)]
    close_line = [[] for _ in range(end+1)]
    visit = [0] + [10000] * end
    sort_data = [[0]*(end+1) for _ in range(end + 1)]
    for data in line_data:
        close_line[data[0]].append(data[1])
        sort_data[data[0]][data[1]] = data[2]

    Q = deque()
    Q.append(0)
    while Q:
        now = Q.popleft()
        for next in close_line[now]:
            if visit[next] > visit[now] + sort_data[now][next]:
                visit[next] = visit[now] + sort_data[now][next]
                Q.append(next)
    print('#{} {}'.format(t, visit[end]))