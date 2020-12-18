import sys; sys.stdin = open('input_data/3456.txt')

for t in range(1, int(input()) + 1):
    a, b, c = list(map(int, input().split()))
    if a == b:
        print('#{} {}'.format(t, c))
    elif a == c:
        print('#{} {}'.format(t, b))
    else:
        print('#{} {}'.format(t, a))
