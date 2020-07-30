import sys
sys.stdin = open('input_data/1986.txt','r')

T = int(input())

for t in range(1, T+1):
    number = int(input())
    result = 0
    for num in range(number+1):
        if num%2:
            result += num
        else:
            result -= num

    print('#{} {}'.format(t,result))