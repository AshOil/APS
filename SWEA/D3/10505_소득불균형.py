import sys
sys.stdin = open('input_data/10505.txt','r')

T = int(input())

for t in range(1, T+1):
    number = int(input())
    numbers = list(map(int, input().split()))
    average = sum(numbers)/number
    count = 0
    for num in numbers:
        if num <= average:
            count+=1

    print('#{} {}'.format(t, count))