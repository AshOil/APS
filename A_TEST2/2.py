import sys; sys.stdin = open('input_data/2.txt')

T = int(input())
for t in range(1, T+1):
    now, target = map(int, input().split())
    kill_list = []
    check_min = []
    check_max = []
    abs_min_x = 300
    abs_max_x = 0
    abs_min_y = 300
    abs_max_y = 0
    for _ in range(now):
        point = list(map(int, input().split()))
        sorted_point = [min(point[0], point[2]), min(point[1], point[3]), max(point[0], point[2]), max(point[1], point[3])]
        if abs_min_x > min(point[0], point[2]):
            abs_min_x = min(point[0], point[2])
        if abs_max_x < max(point[0], point[2]):
            abs_max_x = max(point[0], point[2])
        if abs_min_y > min(point[1], point[3]):
            abs_min_y = min(point[1], point[3])
        if abs_max_y < max(point[1], point[3]):
            abs_max_y = max(point[1], point[3])
        kill_list.append(sorted_point)
        check_min.append([sorted_point[0], sorted_point[1]])
        check_max.append([sorted_point[2], sorted_point[3]])
        min_point = min(sorted_point[0], sorted_point[1])
        max_point = max(sorted_point[2], sorted_point[3])
        if [min_point, min_point] not in check_min:
            check_min.append([min_point, min_point])
    check_min.sort()
    check_max.sort()
    if target == 0:
        print('#{} {}'.format(t, max(abs_max_x - abs_min_x, abs_max_y - abs_min_y)))
        continue
    keep_going = True
    for size in range(1, 301):
        for now_min in check_min:
            residue = now
            min_x, min_y = now_min
            max_x, max_y = min_x + size, min_y + size
            for kill in kill_list:
                if min_x <= kill[0] and min_y <= kill[1] and kill[2] <= max_x and kill[3] <= max_y:
                    residue -= 1
            if residue == target:
                keep_going = False
                break
        if not keep_going:
            print('#{} {}'.format(t, size))
            break

