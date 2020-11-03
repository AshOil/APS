# TODO 런타임 9/10 한개만 오류나

import sys; sys.stdin = open('input_data/5204.txt')
from collections import deque

def halfCut(numbers):
    if len(numbers) <= 1 : return numbers
    mid = len(numbers) // 2
    left = halfCut(numbers[:mid])
    right = halfCut(numbers[mid:])
    return sortProcess(left, right)

def sortProcess(left, right):
    global count
    left = deque(left)
    right = deque(right)
    total = deque()
    if left[-1] > right[-1]:
        count += 1

    while left and right:
        if left[0] < right[0]:
            total.append(left.popleft())
        else:
            total.append(right.popleft())
    if left:
        total += left
    if right:
        total += right

    return total

for t in range(1, int(input()) + 1):
    length = int(input())
    numbers = list(map(int, input().split()))
    count = 0
    print('#{} {} {}'.format(t, halfCut(numbers)[len(numbers)//2], count))