
import sys; sys.stdin = open('input_data/10761.txt')

for t in range(1, int(input()) + 1):
    data = list(input().split())
    data_num = int(data[0])
    Orange = [0] * 101
    Blue = [0] * 101
    for i in range(data_num):
        now = i*2 + 1
        if data[now] == 'O':
            Orange[int(data[now+1])] = 1
        else:
            Blue[int(data[now+1])] = 1
    print(Orange)
    print(Blue)
