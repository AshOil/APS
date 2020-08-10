import sys
sys.stdin = open('input_data/2817.txt',"r")

T = int(input())
for t in range(1,T+1):
    length, want = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    count = 0
    for i in range(1<<length):
        num_list = []
        for j in range(length):
            if i & (1<<j):
                num_list.append(numbers[j])
        if sum(num_list) == want:
            count+=1

    print('#{} {}'.format(t, count))


