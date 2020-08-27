import sys
sys.stdin = open('input_data/5688.txt',"r")

T = int(input())
for t in range(1,T+1):
    number = int(input())
    if abs(number**(1/3) - round(number**(1/3))) < 0.0001:
         print('#{} {}'.format(t, round(number**(1/3))))
    else:
        print('#{} -1'.format(t))

