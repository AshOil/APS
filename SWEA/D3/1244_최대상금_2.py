import sys; sys.stdin = open('input_data/1244.txt',"r")
from itertools import permutations

T = int(input())
for t in range(1,T+1):
    number, turn = list(map(int, input().split()))
    number = str(number)
    all_list = list(permutations(number))
    can_list = []
    result_list = []
    for data in all_list:
        count = 0
        for i in range(len(number)):
            if data[i] != number[i]:
                count += 1

        if 2 <= count <= turn ** 2 + 1:
            can_list.append(data)
    for data in can_list:
        result_list.append(int(''.join(data)))
    print(can_list)
    print('#{} {}'.format(t, max(result_list)))


