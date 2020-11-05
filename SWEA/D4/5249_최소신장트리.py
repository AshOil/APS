import sys; sys.stdin = open('input_data/5249.txt')


for t in range(1, int(input()) + 1):
    dot, line = map(int, input().split())
    line_data = [list(map(int, input().split())) for _ in range(line)]
    data_sort = [[0] * (dot+1) for _ in range(dot+1)]
    for data in line_data:
        data_sort[data[0]][data[1]] = data[2]
        data_sort[data[1]][data[0]] = data[2]
    check_list = [[0, 0]]+[[-1, 1000] for i in range(dot)]
    count = 0
    now = 0
    already = []
    result = 0
    while count < dot + 1:
        already.append(now)
        count += 1
        for i in range(1, dot+1):
            if i not in already and data_sort[now][i] and check_list[i][1] > data_sort[now][i]:
                check_list[i][1] = data_sort[now][i]
                check_list[i][0] = now
        min = 1001
        for i in range(1, dot+1):
            if i not in already:
                if check_list[i][1] < min:
                    min = check_list[i][1]
                    next = i
        result += min
        now = next
    print('#{} {}'.format(t, result - 1001))

