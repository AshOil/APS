import sys; sys.stdin = open('input_data/5189.txt')
from itertools import permutations

for t in range(1, int(input()) + 1):
    size = int(input())
    ground = [list(map(int, input().split())) for _ in range(size)]
    zone = [i for i in range(1, size)]
    course_list = list(map(list, permutations(zone)))
    min_battery = 10000
    for course in course_list:
        total = 0
        stage = 0
        before = 0
        for now in course:
            print(ground[before][now])
            total += ground[before][now]
            before = now
            if total > min_battery:
                break
        total += ground[before][0]
        print(ground[before][0])
        print(total)
        print(course)
        if total < min_battery:
            min_battery = total
    print('#{} {}'.format(t, min_battery))
