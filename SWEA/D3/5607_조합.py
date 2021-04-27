

import sys; sys.stdin = open('input_data/5607.txt')

for t in range(1, int(input()) + 1):
    N, R = map(int, input().split())
    result = 1
    for num in range(N, N-R, -1):
        result *= num
        if result > 1234567891:
            result = result%1234567891
    for idx in range(R, 0, -1):
        result /= num
    print('#{} {}'.format(t, int(result)%1234567891))