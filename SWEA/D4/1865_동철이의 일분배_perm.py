import sys; sys.stdin = open('input_data/1865.txt')

for t in range(1, int(input()) + 1):
    worker = int(input())
    worksheet = [list(map(int, input().split())) for _ in range(worker)]
