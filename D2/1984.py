import sys
sys.stdin = open('input_data/1984.txt',"r")


T = int(input())

for t in range(1, T+1):
    numbers = list(map(int, input() .split()))
    new_list = sorted(numbers)
    real_list = new_list[1:9]
    result = round(sum(real_list)/8)
    print('#{} {}'.format(t,result))