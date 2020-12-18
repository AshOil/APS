import sys; sys.stdin = open('input_data/3307.txt')

for t in range(1, int(input()) + 1):
    length = int(input())
    numbers = list(map(int, input().split()))
    check = [0]*length
    check[0] = 1
    for i in range(1, length)