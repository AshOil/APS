import sys
sys.stdin = open('input_data/5948.txt',"r")

T = int(input())

for t in range(1,T+1):
    sum_list = set()
    number_list = list(map(int, input() .split()))
    for i1 in number_list:
        for i2 in number_list:
            if i2 != i1:
                for i3 in number_list:
                    if i3 != i1 and i3 != i2:
                        sum_list.add(i1 + i2 + i3)
    my_sum = sorted(sum_list)
    length = len(my_sum) - 5
    print('#{} {}'.format(t,my_sum[length]))
        
