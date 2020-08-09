import sys
sys.stdin = open('input_data/4466.txt',"r")

T = int(input())

for t in range(1, T+1):
    length, sum_num = list(map(int, input() .split()))
    numbers = list(map(int, input() .split()))
    numbers = sorted(numbers)
    my_sum = 0
    for i in range(1,sum_num + 1):
        my_sum += numbers[-i]
    print('#{} {}'.format(t, my_sum))