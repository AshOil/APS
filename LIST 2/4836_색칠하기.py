import sys
sys.stdin = open('input_data/4836.txt',"r")


T = int(input())

for t in range(1, T+1):
    paint = int(input())
    vacancy = [[0] *10 for _ in range(10)]
    count = 0
    for _ in range(paint):
        numbers = list(map(int, input() .split()))
        for i in range(numbers[0],numbers[2]+1):
            for j in range(numbers[1],numbers[3]+1):
                vacancy[i][j] += numbers[4]
    for i in vacancy:
        for j in i:
            if j >=3:
                count +=1
    print('#{} {}'.format(t, count))