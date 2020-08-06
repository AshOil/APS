import sys
sys.stdin = open('input_data/5642.txt',"r")

T = int(input())

for t in range(1,T+1):
    length = int(input())
    numbers = list(map(int, input().split()))
    max_val = 0
    for dist in range(1, length+1):
        start = 0
        for i in range(dist):
            start += numbers[i]
        for i in range(dist, length):
            start += numbers[i] - numbers[i-dist]
            if start > max_val:
                max_val = start
    print('#{} {}'.format(t, max_val))

