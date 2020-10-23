n = 5
tower = [[] for _ in range(n)]
print(tower)
floor = 0
number = 1
top_limit = 1
bottom_limit = n - 1
way = True # down
side_way = n
while True:
    if way:
        if floor == bottom_limit:
            way = False
            for _ in range(side_way):
                tower[bottom_limit].append(number)
                number += 1
            side_way -= 2
            floor -= 1
        else:
            tower[floor].append(number)
            floor += 1
            number += 1
    else:
        tower[floor].append(number)
        floor -= 1
        number += 1
