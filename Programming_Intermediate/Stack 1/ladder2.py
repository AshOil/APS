import sys; sys.stdin = open('ladder.txt')

def check(x,y):
    if x>=100 or x < 0 or y>=100 or y<0 : return False
    if ladder[y][x] ==0: return False
    return True

for t in range(1,11):
    t = int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]
    can_go = []
    for i in range(100):
        if ladder[0][i]==1:
            can_go.append(i)
    count_list = []
    for x in can_go:
        y = 0
        count = 0
        dir = 0
        while y < 100:
            if dir != 2 and check(x-1, y):
                dir = 1
                x -= 1
            elif dir != 1 and check(x+1, y):
                dir =2
                x += 1
            else:
                dir = 0
                y += 1
            count += 1
        count_list.append(count)
    index =count_list.index(min(count_list))
    print('#{} {}'.format(t, can_go[index]))


