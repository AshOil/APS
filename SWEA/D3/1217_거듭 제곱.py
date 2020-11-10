import sys; sys.stdin = open('input_data/1217.txt')

for _ in range(10):
    t = int(input())
    num, mul = map(int, input().split())
    print('#{} {}'.format(t, num**mul))