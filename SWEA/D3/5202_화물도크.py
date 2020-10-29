import sys; sys.stdin = open('input_data/5202.txt')

for t in range(1, int(input()) + 1):
    fedex_num = int(input())
    fedex = [list(map(int, input().split())) for _ in range(fedex_num)]
    fedex.sort()
    end = fedex[0][1]
    count = 1
    for i in range(1, fedex_num):
        if fedex[i][0] >= end:
            count += 1
            end = fedex[i][1]
        if end > fedex[i][1]:
            end = fedex[i][1]
    print('#{} {}'.format(t, count))