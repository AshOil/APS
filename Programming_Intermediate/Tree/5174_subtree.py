import sys; sys.stdin = open('input_data/5174.txt')


def CountMachine(x):
    global count
    if x:   # 0이 아니라면
        count+=1
        CountMachine(tree[x][0])
        CountMachine(tree[x][1])




for t in range(1, int(input()) + 1):
    line, target = map(int,input().split())
    line_data = list(map(int,input().split()))
    tree = [[0]*3 for _ in range(line+2)]

    for i in range(line):
        parent, child = line_data[i*2], line_data[i*2 +1]
        if not tree[parent][0]:
            tree[parent][0] = child
        else: tree[parent][1] = child
        tree[child][2] = parent

    count = 0
    CountMachine(target)

    print('#{} {}'.format(t, count))