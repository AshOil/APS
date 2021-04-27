
import sys; sys.stdin = open('input_data/1697.txt')
from collections import deque

now, target = map(int, input().split())
if target < now:
    print(now-target)
    exit()
min_count = 10000
check = [10000] * (target*3)
Q = deque()
Q.append(now)
check[now] = 0
while Q:
    now = Q.popleft()
    if now == target:
        if min_count > check[now]:
            min_count = check[now]
            continue
    next_list = [now + 1, now - 1, now * 2]
    for can_next in next_list:
        if can_next < 0 or can_next > (target * 2) or can_next > 100000: continue
        if check[can_next] > check[now] + 1:
            check[can_next] = check[now] + 1
            if check[can_next] > min_count: continue
            Q.append(can_next)
print(check[target])