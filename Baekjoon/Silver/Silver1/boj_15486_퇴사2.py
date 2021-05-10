import sys; sys.stdin = open('input_data/15486.txt')

n = int(input())
jobs = [[0, 0]]+[list(map(int, input().split())) for _ in range(n)]
print(jobs)