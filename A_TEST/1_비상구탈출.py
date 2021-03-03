import sys; sys.stdin = open('1.txt')

from copy import deepcopy

def combi(go_way, depth):
    global people_num
    if depth == people_num:
        go = deepcopy(go_way)
        can_go.append(go)
        return
    else:
        depth += 1
        go_way.append(1)
        combi(go_way, depth)
        go_way.pop()
        go_way.append(2)
        combi(go_way, depth)
        go_way.pop()


T = int(input())
for t in range(1, T + 1):
    size = int(input())
    ground = [list(map(int, input().split())) for _ in range(size)]
    people = []
    exit = []
    for i in range(size):
        for j in range(size):
            if ground[i][j] == 2:
                exit.append([i, j])
            elif ground[i][j] == 1:
                people.append([i, j])
    people_num = len(people)
    can_go = []
    go_way = []
    combi(go_way, 0)
    count_list = []
    for go in can_go:
        exit_1 = []
        exit_2 = []
        for idx, person in enumerate(people):
            person_x, person_y = person
            if go[idx] == 1:
                exit_x, exit_y = exit[0]
                distance = abs(exit_x - person_x) + abs(exit_y - person_y)
                exit_1.append(distance)
            else:
                exit_x, exit_y = exit[1]
                distance = abs(exit_x-person_x) + abs(exit_y - person_y)
                exit_2.append(distance)
        exit_1.sort()
        exit_2.sort()
        count = 0
        while exit_1 or exit_2:
            count += 1
            if exit_1:
                if exit_1[0] < count:
                    exit_1.pop(0)
            if exit_2:
                if exit_2[0] < count:
                    exit_2.pop(0)
        count_list.append(count)
    print("#{} {}".format(t, min(count_list)))

