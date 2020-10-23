import sys; sys.stdin = open('input_data/magnetic.txt')

def Clockwise(target):
    old_status = list(gear[target])
    gear[target].insert(0, gear[target].pop())
    visit[target] = 1
    if target - 1 >= 0 and old_status[6] != gear[target - 1][2] and not visit[target-1]:
        AntiClock(target - 1)
    if target + 1 < 4 and old_status[2] != gear[target + 1][6] and not visit[target + 1]:
        AntiClock(target + 1)

def AntiClock(target):
    old_status = list(gear[target])
    gear[target].append(gear[target].pop(0))
    visit[target] = 1
    if target - 1 >= 0 and old_status[6] != gear[target - 1][2] and not visit[target-1]:
        Clockwise(target - 1)
    if target + 1 < 4 and old_status[2] != gear[target + 1][6] and not visit[target +1]:
        Clockwise(target + 1)

for t in range(1, int(input())+1):
    turn = int(input())
    gear = [list(map(int, input().split())) for _ in range(4)]
    whatToDo = [list(map(int, input().split())) for _ in range(turn)]
    for ToDo in whatToDo:
        visit = [0] * 4
        target = ToDo[0] - 1
        way = ToDo[1]
        # 돌리기
        if way == 1:
            Clockwise(target)
        else:
            AntiClock(target)
    result = 0
    for i in range(4):
        result += gear[i][0] * (2**i)
    print('#{} {}'.format(t,result))