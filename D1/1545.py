import sys
sys.stdin = open("input_data/1545.txt","r")

T = int(input())
count = 0
for _ in range(T+1):
    print(T-count, end=' ')
    count += 1