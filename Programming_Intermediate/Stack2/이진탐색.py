# 이진탐색

arr = [3, 6, 7, 9, 2, 5, 1, 8]
N = len(arr)

def getMin(lo, hi):   # 매개변수 -> 문제의 크기를 나타내는 값
    # lo : 시작인덱스 , hi : 끝 인덱스
    if lo == hi:
        return arr[lo]
    else:
        mid = (lo + hi) // 2
        left = getMin(lo,mid)
        right = getMin(mid + 1, hi)
        min(left, right)

print(getMin(0, N-1))
