import sys
sys.stdin = open('input_data/6057.txt')

T = int(input())
for t in range(1, T+1):
    dot, line = map(int,input().split())
    line_data = [list(map(int,input().split())) for _ in range(line)]
    