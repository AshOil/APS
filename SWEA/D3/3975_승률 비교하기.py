import sys
sys.stdin = open('input_data/3975.txt',"r")

T = int(input())

for t in range(1,T+1):
    scores = list(map(int, input().split()))
    BOB = scores[1] * scores[2]
    ALICE = scores[0] * scores[3]

    if BOB> ALICE:
        print('#{} BOB'.format(t))
    elif BOB< ALICE:
        print('#{} ALICE'.format(t))
    else:
        print('#{} DRAW'.format(t))