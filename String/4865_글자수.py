import sys
sys.stdin = open('input_data/4865.txt',"r")

T = int(input())
for t in range(1, T+1):
    small = input()
    big = input()
    result = 0
    for char in small:
        count = big.count(char)
        if count > result:
            result = count
    print('#{} {}'.format(t,result))