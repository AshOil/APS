import sys
sys.stdin = open("input_data/4869.txt", 'r')

T = int(input())
for t in range(1, T+1):
    number = int(input())
    if number%20:
        result = 5
        for _ in range(number//20-1):
            result = result*4 + 1
    else:
        result = 3
        for _ in range(number // 20 - 1):
            result = result* 4 -1
    print('#{} {}'.format(t, result))

