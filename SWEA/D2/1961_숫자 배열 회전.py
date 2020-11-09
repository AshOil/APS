import sys; sys.stdin = open('input_data/1961.txt')
from copy import deepcopy

for t in range(1, int(input()) + 1):
    print('#{}'.format(t))
    size = int(input())
    ground = [list(map(int, input().split())) for _ in range(size)]
    new_ground = []
    result_line = [[] for _ in range(size)]
    for _ in range(3):
        for idx, i in enumerate(range(size-1, -1, -1)):
            line = list(list(zip(*ground))[i])
            result_line[idx].insert(0, ''.join(map(str, line)))
            new_ground.append(line)
        ground = deepcopy(new_ground)
        new_ground.clear()
    for line in result_line:
        print(*line)


