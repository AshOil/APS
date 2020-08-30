import sys
sys.stdin = open("input_data/4828.txt", 'r')

T = int(input())
for t in range(1,T+1):
    num = int(input())
    numbers = list(map(int, input().split()))
    print('#{} {}'.format(t, max(numbers)-min(numbers)))