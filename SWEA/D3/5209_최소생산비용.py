import sys; sys.stdin = open('input_data/5209.txt')

def doWork(i,fact, total):
    global min_cost
    visit[i] = 1
    if total +  ground[fact][i] >= min_cost:
        return
    if fact == size - 1:
        total += ground[fact][i]
        if min_cost > total:
            min_cost = total
            return
    for j in range(size):
        if not visit[j]:
            doWork(j, fact+1, total + ground[fact][i])
            visit[j] = 0


for t in range(1, int(input()) + 1):
    size = int(input())
    ground = [list(map(int, input().split())) for _ in range(size)]
    min_cost = 10000
    for i in range(size):
        visit = [0] * size
        doWork(i, 0, 0)
    print('#{} {}'.format(t, min_cost))