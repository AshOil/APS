## 왜 틀린지 모르겠다 ㅠㅠ


import sys
sys.stdin = open("input_data/2814.txt",'r')

def DSF(x):
    global count
    global max_count
    count += 1
    if count > max_count:
        max_count = count
    visit[x] = 1
    for i in range(1, dot+1):
        if ground[x][i] and not visit[i]:
            DSF(i)
    count -= 1
    return max_count

T = int(input())
for t in range(1, T+1):
    dot, line = map(int,input().split())
    line_data = [list(map(int,input().split())) for _ in range(line)]
    ground = [[0] * (dot + 1) for _ in range(dot+1)]
    for data in line_data:
        ground[data[0]][data[1]] = 1
        ground[data[1]][data[0]] = 1
    count_list = []

    for x in range(1, dot+1):
        visit = [0] * (dot + 1)
        max_count = 0
        count = 0
        count_list.append(DSF(x))

    print('#{} {}'.format(t, max(count_list)))
