import sys
sys.stdin = open("input_data/2029.txt","r")

T = int(input())

for t in range(1, T+1):
    numbers = list(map(int, input() .split()))
    a = numbers[0]//numbers[1]
    b = numbers[0]%numbers[1]

    print('#{} {} {}'.format(t, a, b))