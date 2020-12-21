import sys; sys.stdin = open('input_data/3408.txt')

for t in range(1, int(input()) + 1):
    N = int(input())
    case = (N*(N+1))//2
    print('#{} {} {} {}'.format(t, case, N ** 2, case*2))