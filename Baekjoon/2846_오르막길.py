import sys
sys.stdin = open('input_data/2846.txt',"r")

length = int(input())
hill = list(map(int, input().split()))
vacancy = [0]* length

for i in range(1, length):
    if hill[i] - hill[i-1] > 0:
        vacancy[i] = hill[i] - hill[i-1] + vacancy[i-1]
    else:
        vacancy[i] = 0

if max(vacancy)>1:
    print(max(vacancy))
else:
    print(0)