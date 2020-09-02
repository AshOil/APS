import sys
sys.stdin = open('input_data/4880.txt')

def RSP(lo,hi):
    if lo == hi:
        return new_data[lo]
    else:
        mid = (lo + hi) // 2
        left = RSP(lo, mid)
        right = RSP(mid + 1, hi)
        if left[1] == 1:
            if right[1] == 2: return right
            else: return left
        elif left[1] == 2:
            if right[1] == 3: return right
            else: return left
        elif left[1] == 3:
            if right[1] == 1: return right
            else: return left


T = int(input())
for t in range(1,T+1):
    length = int(input())
    data = list(map(int, input().split()))
    new_data = [[idx, in_data] for idx, in_data in enumerate(data)]
    result = RSP(0,length-1)
    print('#{} {}'.format(t,result[0]+1))
