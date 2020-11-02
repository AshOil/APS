# TODO 효율성 실패 (시간초과)

N = 5000
from collections import deque



def solution(N):
    lets_go = deque()
    lets_go.append([1, 1])
    min_count = 100
    while lets_go:
        num, count = lets_go.popleft()
        if num > N:
            continue
        if count > min_count:
            continue
        if num == N:
            if count < min_count:
                min_count = count
        if num*2 <= N:
            lets_go.append([num*2, count])
        lets_go.append([num+1, count + 1])
    return min_count

print(solution(N))

