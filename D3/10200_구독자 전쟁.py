import sys
sys.stdin = open('input_data/10200.txt',"r")

T = int(input())

for t in range(1,T+1):
    total, a_team, b_team = list(map(int,input().split()))
    if a_team > b_team:
        big = a_team
        small = b_team
    else:
        big = b_team
        small = a_team
    max_val = small
    if big + small <= total:
        min_val = 0
    else:
        min_val = big + small - total
    print('#{} {} {}'.format(t, max_val, min_val))