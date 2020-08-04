import sys
sys.stdin = open('input_data/0816.txt',"r")

T = int(input())

for t in range(1,T+1):
    number = int(input())
    if number ==1 :
        print('#{} 1 1'.format(t))
    else:
        print('#{} {} {}'.format(t,2*((number-1)**2)+1, 2*(number**2) -1))