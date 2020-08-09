import sys
sys.stdin = open('input_data/5603.txt',"r")

T = int(input())

for t in range(1,T+1):
    length = int(input())
    numbers = []
    for _ in range(length):
        numbers.append(int(input()))
    average = int(sum(numbers)/length)
    result = 0
    for num in numbers:
        if num > average:
            result += num - average
    print('#{} {}'.format(t, result))