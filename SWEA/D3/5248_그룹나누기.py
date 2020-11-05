# TODO 11/04 하다말았음

import sys; sys.stdin = open('input_data/5248.txt')

for t in range(1, int(input()) + 1):
    student, line = map(int, input().split())
    line_data = list(map(int, input().split()))
    for i in range(line):
        line_data.append()