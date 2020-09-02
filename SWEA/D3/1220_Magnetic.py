import sys
sys.stdin = open('input_data/1220.txt')

for t in range(1,11):
    size = int(input())
    ground = [list(map(int, input().split())) for _ in range(size)]
    result = 0
    for i in range(size):
        N_have = False
        for j in range(size):
            if ground[j][i] == 1:
                N_have = True
            elif ground[j][i] == 2 and N_have:
                result += 1
                N_have = False
    print('#{} {}'.format(t,result))

