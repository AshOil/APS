import sys; sys.stdin = open('input_data/5251.txt')

def DFS(number, total):
    global min_move
    if total > min_move:
        return
    if number == end:
        if min_move > total:
            min_move = total
            return
    for next in close_line[number]:
        if not visit[next]:
            visit[next] = 1
            DFS(next, total + sort_data[number][next])
            visit[next] = 0


for t in range(1, int(input()) + 1):
    min_move = 10000
    end, line = map(int, input().split())
    line_data = [list(map(int, input().split())) for _ in range(line)]
    close_line = [[] for _ in range(end)]
    visit = [0] * (end+1)
    sort_data = [[0]*(end+1) for _ in range(end + 1)]
    for data in line_data:
        close_line[data[0]].append(data[1])
        sort_data[data[0]][data[1]] = data[2]
    DFS(0, 0)
    print('#{} {}'.format(t, min_move))