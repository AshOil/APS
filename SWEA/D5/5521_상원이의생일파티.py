import sys; sys.stdin = open('input_data/5521.txt')


for t in range(1, int(input()) + 1):
    dot, line = map(int,input().split())
    my_friend = [[] for _ in range(dot+1)]
    for _ in range(line):
        data = list(map(int, input().split()))
        my_friend[data[1]].append(data[0])
        my_friend[data[0]].append(data[1])
    invite_list = []
    if my_friend[1]:
        invite_list += my_friend[1]
        for friend in my_friend[1]:
            invite_list += my_friend[friend]
        result = len(list(set(invite_list)))
    else:
        result = 1
    print('#{} {}'.format(t, result-1))