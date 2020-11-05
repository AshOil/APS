import sys; sys.stdin = open('input_data/2817.txt',"r")

def BBJH(idx, total):
    global count
    if idx == length:
        if total == want:
            count += 1
        return
    if total > want:
        return
    BBJH(idx+1, total + numbers[idx])
    BBJH(idx+1, total)

for t in range(1,int(input())+1):
    length, want = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    count = 0
    BBJH(0, 0)
    print('#{} {}'.format(t, count))


