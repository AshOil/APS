import sys
sys.stdin = open("input_data/2070.txt","r")

T = int(input())

for t in range(1, T+1):
    my_list = list(map(int, input() .split()))
    result = ''
    if my_list[0] > my_list[1]:
        result =  '>'
    elif my_list[0] == my_list[1]:
        result =  '='
    else:
        result =  '<'

    print('#{} {}'.format(t, result))