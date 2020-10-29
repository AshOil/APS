import sys; sys.stdin = open('input_data/1325.txt')
sys.setrecursionlimit(100000)

def DFS(x):
    global count
    count += 1
    visit[x] = 1
    for w in graph[x]:
        if result_list[w]:
            count += result_list[w]
        else:
            DFS(w)

dot, line = map(int, input().split())
graph = [[] for _ in range(dot + 1)]
result_list = [0] * (dot+1)

for _ in range(line):
    data = list(map(int, sys.stdin.readline().split()))
    graph[data[1]].append(data[0])
max_list =[]
max_num = 0

for i in range(dot, 0, -1):
    count = 0
    visit = [0] * (dot + 1)
    DFS(i)
    result_list[i] = count
    if max_num < count:
        max_num = count
        max_list = []
        max_list.append(i)
    elif max_num == count:
        max_list.append(i)
print(*max_list)
print(result_list)