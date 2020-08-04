import sys
sys.stdin = open('input_data/4835.txt',"r")

T = int(input())

for t in range(1, T+1):
    length, friend = list(map(int, input() .split()))
    numbers = list(map(int, input() .split()))
    sum_list = []
    for i in range(length - friend +1):
        sum_num = 0
        for i2 in range(i,friend+i):
            sum_num += numbers[i2]
        sum_list.append(sum_num)
    min_num = max_num = sum_list[0]
    for num in sum_list:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    print('#{} {}'.format(t, max_num - min_num))
        


