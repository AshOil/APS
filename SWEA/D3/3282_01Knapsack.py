#TODO 시간초과 12/18

import sys; sys.stdin = open('input_data/3282.txt')

def packing(num, packed, value):
    global result
    if num == packages or size < packed: return
    if value > result:
        result = value
    packing(num + 1, packed + package_data[num][0], value + package_data[num][1])
    packing(num + 1, packed, value)

for t in range(1, int(input()) + 1):
    packages, size = map(int, input().split())
    package_data = [list(map(int, input().split())) for _ in range(packages)]
    result = 0
    packing(0, 0, 0)
    print('#{} {}'.format(t, result))