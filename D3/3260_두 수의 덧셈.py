import sys
sys.stdin = open('input_data/3260.txt',"r")

T = int(input())
for t in range(1,T+1):
    numbers = list(map(int, input().split()))
    result = sum(numbers)
    print('#{} {}'.format(t, result))