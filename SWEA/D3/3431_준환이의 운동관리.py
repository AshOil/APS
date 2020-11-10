import sys; sys.stdin = open('input_data/3431.txt')

for t in range(1, int(input()) + 1):
    mini, maxi, now = map(int, input().split())
    if now > maxi:
        print('#{} -1'.format(t))
    elif mini <= now <= maxi:
        print('#{} 0'.format(t))
    else:
        print('#{} {}'.format(t, mini-now))