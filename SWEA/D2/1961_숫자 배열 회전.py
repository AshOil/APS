# TODO

import sys; sys.stdin = open('input_data/1961.txt')

T = int(input())
for t in range(1, T+1):
    print('#{}'.format(t))
    size = int(input())
    number_list = []
    for _ in range(size):
        number_list.append(list(input().split()))
    for _ in range(3):
        number_list = list(map(list, zip(number_list[0], number_list[1], number_list[2])))
        for num in number_list:
            num.reverse()
        print(''.join(number_list[0]), end=' ')
    print()
    number_list = list(map(list, zip(number_list[0], number_list[1], number_list[2])))
    for _ in range(3):
        number_list = list(map(list, zip(number_list[0], number_list[1], number_list[2])))
        for num in number_list:
            num.reverse()
        print(''.join(number_list[1]), end=' ')
    print()
    number_list = list(map(list, zip(number_list[0], number_list[1], number_list[2])))
    for _ in range(3):
        number_list = list(map(list, zip(number_list[0], number_list[1], number_list[2])))
        for num in number_list:
            num.reverse()
        print(''.join(number_list[2]), end=' ')
    print()





