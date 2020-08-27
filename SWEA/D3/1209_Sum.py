import sys
sys.stdin = open('input_data/1209.txt',"r")

for t in range(1, 11):
    test_num = int(input())
    num_list = [list(map(int, input().split())) for _ in range(100)]
    max_sum = 0
    # 행의 합 구하기
    for i in num_list:
        if sum(i)>max_sum:
            max_sum = sum(i)

    # 열의 합 구하기

    for j in range(100):
        verti_sum = 0
        for i in num_list:
            verti_sum += i[j]
        if verti_sum > max_sum:
            max_sum = verti_sum

    #대각선의 합 구하기
    cross_sum = 0
    for i in range(100):
        cross_sum += num_list[i][i]
    if cross_sum > max_sum:
        max_sum = cross_sum

    cross_sum = 0
    for i in range(100):
        cross_sum += num_list[99-i][99-i]
    if cross_sum > max_sum:
        max_sum = cross_sum
    print('#{} {}'.format(t, max_sum))
