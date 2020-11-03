import sys; sys.stdin = open('input_data/1247.txt')

def salesRoute(i, distance, count):
    global min_dist
    visit[i] = 1
    if distance > min_dist: return
    if count == members:
        distance += abs(each_house[i][0] - my_home[0]) + abs(each_house[i][1] - my_home[1])
        if distance < min_dist:
            min_dist = distance
            return
    for j in range(1, members+1):
        if not visit[j]:
            salesRoute(j, distance + abs(each_house[i][0] - each_house[j][0]) + abs(each_house[i][1] - each_house[j][1]), count + 1)
            visit[j] = 0

for t in range(1, int(input()) + 1):
    members = int(input())
    house = list(map(int, input().split()))
    each_house = []
    my_company = [house[0], house[1]]
    my_home = [house[2], house[3]]
    for i in range(2, members+2):
        each_house.append([house[2*i], house[2*i+1]])
    each_house = [my_company] + each_house
    visit = [0] * (members + 1)
    min_dist = 100000
    salesRoute(0, 0, 0)
    print('#{} {}'.format(t, min_dist))
