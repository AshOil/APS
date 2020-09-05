import sys
sys.stdin = open('input_data/6019.txt')

for t in range(1, int(input())+1):
    distance, A, B, speed = map(int,input().split())
    result = (distance/(A+B)) * 20
    print('#{} {}'.format(t, result))