# TODO 시간초과/ 메모리초과

import sys; sys.stdin = open('input_data/1325.txt')
sys.setrecursionlimit(100000)
def DFS(x):
    global count
    count += 1
    visit[x] = 1
    count_check[i] = count
    for w in graph[x]:
        if count_check[w]:
            count += count_check[w]
        elif not visit[w]:
            DFS(w)

dot, line = map(int, input().split())
graph = [[] for _ in range(dot + 1)]
for _ in range(line):
    data = list(map(int, sys.stdin.readline().split()))
    graph[data[1]].append(data[0])
count_check = [0]* (dot+1)
max_list =[]
max_num = 0

for i in range(1, dot+ 1):
    count = 0
    visit = [0] * (dot+1)
    DFS(i)

    if max_num < count:
        max_num = count
        max_list.clear()
        max_list.append(i)
    elif max_num == count:
        max_list.append(i)

print(max_num)
print(*max_list)
print(count_check)