import sys; sys.stdin = open('input_data/4371.txt')


for t in range(1, int(input()) + 1):
    N = int(input())
    timeline = [int(input()) -1 for _ in range(N)]
    timeline.pop(0)
    result = 0
    while timeline:
        result += 1
        ship = timeline.pop(0)
        if not timeline:
            break
        for i in range(ship, 10000000000, ship):
            if i > timeline[-1]:
                break
            else:
                if i in timeline:
                    timeline.remove(i)
                    if not timeline:
                        break
                else:
                    pass
    print('#{} {}'.format(t, result))


