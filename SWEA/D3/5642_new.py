import sys
sys.stdin = open('input_data/5642.txt',"r")

T = int(input())

for t in range(1,T+1):
    length = int(input())
    numbers = list(map(int, input().split()))

    vacancy = [0] * length
    vacancy[0] = numbers[0]
    for i in range(1,length):
        if vacancy[i-1] + numbers[i] > 0:
            if numbers[i] > vacancy[i-1] + numbers[i]:
                vacancy[i] = numbers[i]
            else:
                vacancy[i] = vacancy[i-1] + numbers[i]
        else:
            vacancy[i] = 0

    result = False
    for num in numbers:
        if num > 0:
            result = True
    if result:
        print('#{} {}'.format(t, max(vacancy)))
    else:
        print('#{} {}'.format(t, max(numbers)))