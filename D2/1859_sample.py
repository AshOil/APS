import sys
sys.stdin = open('input_data/1859.txt',"r")


T = int(input())
for t in range(1, T+1):
    N = int(input())
    data = list(map(int, input() .split()))

    max_val=0
    max_vals=[0]*N
    for i in range(N-1,-1,-1):
        if max_val<data[i]:
            max_val=data[i]
        max_vals[i]=max_val
    ret=0
    for i in range(N):
        ret+=max_vals[i]-data[i]

    # for i in range(N-1,-1,-1):
    #     ret+=max(0,max_vals[i]-data[i])
    
    print('#{} {}'.format(t, ret))