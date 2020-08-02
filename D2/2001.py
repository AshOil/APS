### 진행중 ###


import sys
sys.stdin = open('input_data/2001.txt',"r")


T = int(input())

for t in range(1, T+1):
    N, M = list(map(int, input() .split()))
    fly_numbers = []
    for _ in range(N):
        fly_number = list(map(int, input() .split()))
        fly_numbers.append(fly_number)
    sum_flys = []
    sum_fly = 0
    hori_start = 0
    hori_adjust = M
    verti_start = 0
    verti_adjust = M

    for turn_verti in range(N-M+1):
        hori_start = 0
        hori_adjust = M
        for turn in range(N-M+1):
            sum_fly = 0
            for hori in fly_numbers[hori_start:hori_adjust]:
                sum_fly += sum(hori[verti_start:verti_adjust])
            sum_flys.append(sum_fly)
            hori_adjust += 1
            hori_start += 1
        verti_adjust += 1
        verti_start += 1
    print('#{} {}'.format(t, max(sum_flys)))
    









    # ### 세로 더하기 ##
    # for turn in range(N-M+1):
    #     sum_fly = 0
    #     for hori in fly_numbers[hori_start:hori_adjust]:
    #         print(hori)
    #         sum_fly += sum(hori[verti_start:verti_adjust])
    #     sum_flys.append(sum_fly)
    #     hori_adjust += 1
    #     hori_start += 1
    # print(sum_flys)


