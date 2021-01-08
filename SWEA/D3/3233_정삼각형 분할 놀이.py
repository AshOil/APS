import sys; sys.stdin = open('input_data/3233.txt')

for t in range(1, int(input()) + 1):
    big, small = list(map(int, input().split()))
    print('#{} {}'.format(t, (big//small)**2))