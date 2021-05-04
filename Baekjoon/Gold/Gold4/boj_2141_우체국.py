import sys; sys.stdin = open('input_data/2141.txt')
town = int(input())
town_list = []
for _ in range(town):
    town_list.append(list(map(int, input().split())))

min_data = 1000000
for i in range(town_list[0][0], town_list[town-1][0]+1):
    check = 0
    for data in town_list:
        check += data[1] * (max(data[0],i) - min(data[0],i))
    if check < min_data:
        min_data = check
    else:
        print(i-1)
        break

else:
    print(town_list[town-1][0])