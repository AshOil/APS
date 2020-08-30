
## 진행중
import sys
sys.stdin = open('input_data/10570.txt')

T = int(input())
for t in range(1,T+1):
    start, end = map(int,input().split())
    count = 0
    for i in range(start, end+1):
        single = str(i)
        double = str(int(i**(1/2)))
        print(single)
        print(double)
        if single == single[::-1] and double == double[::-1]:
            count +=1
    print('#{} {}'.format(t, count))