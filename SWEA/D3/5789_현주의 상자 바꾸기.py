import sys
sys.stdin = open('input_data/5789.txt',"r")

T = int(input())

for t in range(1,T+1):
    length, turn = list(map(int, input() .split()))
    vacancy = [0]* length
    for i in range(1,turn+1):
        left, right = list(map(int, input() .split()))
        for j in range(left-1, right):
            vacancy[j] = i
    vacancy = ' '.join(map(str, vacancy))
    print('#{} {}'.format(t,vacancy))
