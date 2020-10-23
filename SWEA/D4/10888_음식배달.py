import sys; sys.stdin = open('input_data/10888.txt')
from itertools import combinations
def powerSet(num_list):
    length = len(num_list)
    result_list = []
    for i in range(1<<length):
        check_list = []
        for j in range(length):
            if i & (1<<j):
                check_list.append(num_list[j])
        result_list.append(check_list)
    return result_list


T = int(input())
for t in range(1, T+1):
    # 지도 그리기
    size = int(input())
    ground = [list(map(int, input().split())) for _ in range(size)]
    restaurant = []
    home = []
    # 레스토랑 위치, 집 위치 파악하기
    for i in range(size):
        for j in range(size):
            if ground[i][j]:
                if ground[i][j] == 1:
                    home.append([i, j])
                else:
                    restaurant.append([i, j, ground[i][j]])

    # 레스토랑에서 모든 집까지의 거리
    restaurant_distance = [[] for _ in range(len(restaurant))]
    for i in range(len(restaurant)):
        for in_home in home:
            restaurant_distance[i].append(abs(in_home[0]-restaurant[i][0]) + abs(in_home[1] - restaurant[i][1]))

    # 조합 구하기
    restaurant_num = [i for i in range(len(restaurant))]
    like_restaurnat = powerSet(restaurant_num)
    result_list = []
    for in_list in like_restaurnat:
        my_restaurant = [100]*len(home)
        total_cost = 0
        # 운영비 더하기
        for i in in_list:
            total_cost += restaurant[i][2]
        # 집에서 주문할 가게 구하기
        for i in in_list:
            for j in range(len(home)):
                if restaurant_distance[i][j] < my_restaurant[j]:
                    my_restaurant[j] = restaurant_distance[i][j]
        total_cost += sum(my_restaurant)
        result_list.append(total_cost)
    print('#{} {}'.format(t, min(result_list)))