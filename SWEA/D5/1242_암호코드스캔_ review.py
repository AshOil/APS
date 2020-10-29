import sys; sys.stdin = open('input_data/1242.txt')

def conv(num):
    binary = ''
    n = int(num, 16)
    for i in range(3, -1, -1):
        if num&(2**i):
            binary += '1'
        else:
            binary += '0'
    return binary

for t in range(1, int(input()) + 1):
    height, length = map(int, input().split())
