import sys
sys.stdin = open('input_data/5549.txt',"r")

T = int(input())

for t in range(1,T+1):
    number = int(input())
    if number%2:
        print('#{} Odd'.format(t))
    else:
        print('#{} Even'.format(t))