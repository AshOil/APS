import sys
sys.stdin = open('input_data/5642.txt',"r")

T = int(input())

for t in range(1,T+1):
    length = int(input())
    numbers = list(map(int, input().split()))

    vacancy = [0] * length
    vacancy[0] = numbers[0]
    for i in range(1,length):
        if numbers[i] > vacancy[i-1] + numbers[i] > 0:
            vacancy[i] = numbers[i]
        elif vacancy[i-1] + numbers[i] > numbers[i]>0:
            vacancy[i] = vacancy[i-1] + numbers[i]
        else:
            vacancy[i] = 0
    max_val=max(vacancy)
    if max_val==0:
        max_val=numbers[0]
        for i in numbers:
            if i>max_val:
                max_val=i
    print('#{} {}'.format(t, max_val))
