brown = 24
yellow = 24
edge = (brown+4)//2
total = brown+yellow
can_list = [[edge-i, i] for i in range(1, edge//2+1)]
for can in can_list:
    if can[0] * can[1] == total:
        print(can)
