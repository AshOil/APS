

import sys
sys.stdin = open('input_data/1966.txt',"r")

T = int(input())
for t in range(1, T+1):
    length = str(input())
    numbers = list(map(int, input() .split()))
    new_numbers = ' '.join(map(str,sorted(numbers)))

    print('#{} {}'.format(t, new_numbers))

