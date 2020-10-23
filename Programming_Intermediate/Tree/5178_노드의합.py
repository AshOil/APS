import sys; sys.stdin = open('input_data/5178.txt')

for t in range(1, int(input())+1):
    dot, leaf_num, target = map(int,input().split())
    leaf_data = [list(map(int,input().split())) for _ in range(leaf_num)]
    num_list = [0] * (dot+1)
    for data in leaf_data:
        num_list[data[0]] = data[1]
    count = dot
    while count:
        num_list[count // 2] += num_list[count]
        count -= 1

    print('#{} {}'.format(t,num_list[target]))



