import sys; sys.stdin = open('input_data/10835.txt')
from collections import deque

N = int(input())
result = 0

left = deque(map(int, input().split()))
right = deque(map(int, input().split()))

while left:
    right_check = True
    left_check = False
    now_left = left.pop()

    while right_check:
        now_right = right.pop()
        if not right : right_check = False
        if now_left > now_right:
            result += now_right
        else:
            right_check = False
            if left: left_check = True

    while left_check:
        now_left = left.pop()
        if not left: left_check = False
        if now_left > now_right:
            result += now_right
        else:
            right_check = False
            if left: left_check = True






